"""Language-map sampling — the "hard languages" differentiator.

Slice N clips spread across the film, transcribe each with automatic language
detection, and build a language map. Segments that deviate from the expected
language (or from the majority) are flagged: this is how ASR hallucination is
caught (e.g. a forced-French pass "inventing" French over Hassaniya Arabic
song). Retranscribe the flagged segments in their real language afterwards.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from . import transcribe as _t
from .srt import fmt_ms

LANG_RE = re.compile(r"language\s*[=:]\s*['\"]?([a-z]{2,3})['\"]?", re.IGNORECASE)
PROB_RE = re.compile(r"(?:prob|probability)\s*[=:]\s*([0-9]*\.?[0-9]+)", re.IGNORECASE)


def probe_duration(audio: str, tools_dir=None) -> float:
    ffprobe = _find("ffprobe.exe", tools_dir) or _find("ffprobe", tools_dir)
    if not ffprobe:
        raise RuntimeError("ffprobe not found (pass --tools-dir or install ffmpeg)")
    r = subprocess.run(
        [ffprobe, "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", audio],
        capture_output=True, text=True)
    try:
        return float(r.stdout.strip().splitlines()[-1])
    except (ValueError, IndexError):
        raise RuntimeError(f"could not read duration of {audio}: {r.stderr}")


def slice_clip(audio: str, start_ms: int, duration_s: float, out_wav: Path,
               tools_dir=None):
    ffmpeg = _find("ffmpeg.exe", tools_dir) or _find("ffmpeg", tools_dir)
    if not ffmpeg:
        raise RuntimeError("ffmpeg not found (pass --tools-dir or install ffmpeg)")
    subprocess.run(
        [ffmpeg, "-y", "-ss", f"{start_ms / 1000:.3f}", "-i", audio,
         "-t", f"{duration_s:.2f}", "-vn", "-ac", "1", "-ar", "16000",
         str(out_wav)],
        check=True, capture_output=True)


def detect_python(clip: str, model="large-v2", device="auto",
                  compute_type="int8_float16", model_dir=None):
    """Language detection via faster-whisper (returns probability)."""
    from faster_whisper import WhisperModel
    if model_dir:
        model = str(Path(model_dir) / model)
    m = WhisperModel(model, device=device, compute_type=compute_type)
    _, info = m.transcribe(clip, language=None)
    return info.language, info.language_probability


def detect_binary(clip: str, out_dir: Path, tools_dir=None, model="large-v2",
                  device="auto", compute_type="int8_float16", model_dir=None):
    """Language detection via the standalone binary: run with auto-detect and
    parse the log. Returns (language, probability|None)."""
    exe = _t.find_whisper(tools_dir)
    if not exe:
        raise RuntimeError("no faster-whisper binary or package available")
    clip_path = Path(clip)
    log_path = out_dir / (clip_path.stem + "_detect.log")
    # no --language flag: the binary auto-detects by default
    cmd = [exe, str(clip_path), "-o", str(out_dir), "-f", "srt",
           "--model", model, "--device", device,
           "--compute_type", compute_type, "--standard"]
    if model_dir:
        cmd += ["--model_dir", str(Path(model_dir).resolve())]
    r = subprocess.run(cmd, capture_output=True, text=True)
    log = (r.stdout or "") + "\n" + (r.stderr or "")
    log_path.write_text(log, encoding="utf-8", errors="replace")
    m = LANG_RE.search(log)
    if not m:
        return None, None
    lang = m.group(1).lower()
    p = PROB_RE.search(log)
    prob = float(p.group(1)) if p else None
    return lang, prob


def pick_times(duration_s: float, n: int, avoid_ends_s: float = 10.0):
    """n evenly spaced sample times, avoiding the first/last 10 s."""
    if duration_s <= 2 * avoid_ends_s:
        return [int(duration_s / 2 * 1000)]
    lo, hi = avoid_ends_s, duration_s - avoid_ends_s
    step = (hi - lo) / n
    return [int((lo + i * step) * 1000) for i in range(n)]


def run_langcheck(audio: str, srt_path=None, clips: int = 10, duration_s: float = 12.0,
                  expected=None, out_dir=None, tools_dir=None,
                  model="large-v2", device="auto", compute_type="int8_float16",
                  model_dir=None):
    """Sample clips across the film, detect the language of each, write
    `_detect.log` and `_summary.md`, and return the per-clip results."""
    out_dir = Path(out_dir) if out_dir else Path(audio).parent
    out_dir.mkdir(parents=True, exist_ok=True)
    total = probe_duration(audio, tools_dir)
    times = pick_times(total, clips)

    # prefer the Python package (gives probability), fall back to binary log
    use_python = False
    try:
        import faster_whisper  # noqa: F401
        use_python = True
    except ImportError:
        use_python = False

    log_lines, rows = [], []
    for k, start_ms in enumerate(times, 1):
        clip_wav = out_dir / f"clip_{k:02d}_t{start_ms // 1000:06d}.wav"
        slice_clip(audio, start_ms, duration_s, clip_wav, tools_dir)
        if use_python:
            lang, prob = detect_python(str(clip_wav), model, device,
                                       compute_type, model_dir)
        else:
            lang, prob = detect_binary(str(clip_wav), out_dir, tools_dir,
                                       model, device, compute_type, model_dir)
        rows.append({
            "clip": k, "start_ms": start_ms,
            "start": fmt_ms(start_ms), "duration_s": duration_s,
            "lang": lang or "?", "prob": prob,
        })
        log_lines.append(
            f"clip {k:02d} | start {fmt_ms(start_ms)} | language = {lang or '?'} "
            f"| probability = {prob:.2f}" if prob is not None else
            f"clip {k:02d} | start {fmt_ms(start_ms)} | language = {lang or '?'}")

    # majority + flags
    counts = {}
    for r in rows:
        if r["lang"] != "?":
            counts[r["lang"]] = counts.get(r["lang"], 0) + 1
    majority = max(counts, key=counts.get) if counts else None
    flagged = [r for r in rows if
               (expected and r["lang"] not in (expected, "?"))
               or (not expected and majority and r["lang"] not in (majority, "?"))]

    summary = [
        "# Language map — SubFlow langcheck",
        "",
        f"Audio: {audio} | duration: {total:.0f}s | clips: {len(rows)} "
        f"({duration_s}s each)",
        f"Expected language: {expected or 'auto (majority)'}",
        f"Majority detected: {majority or 'n/a'}",
        f"Flagged clips: {len(flagged)} (transcribe these in their real "
        f"language and rebuild the affected cues)",
        "",
        "| # | start | duration | detected | prob |",
        "|---|---|---|---|---|",
    ]
    for r in rows:
        flag = " ⚠️" if r in flagged else ""
        prob_txt = f"{r['prob']:.2f}" if r["prob"] is not None else "-"
        summary.append(f"| {r['clip']} | {r['start']} | {r['duration_s']}s "
                       f"| {r['lang']}{flag} | {prob_txt} |")
    summary.append("")
    (out_dir / "_detect.log").write_text("\n".join(log_lines) + "\n", encoding="utf-8")
    (out_dir / "_summary.md").write_text("\n".join(summary), encoding="utf-8")

    for line in log_lines:
        print(line)
    print(f"\nSummary: {out_dir / '_summary.md'}")
    if flagged:
        print(f"⚠️  Flagged {len(flagged)} clip(s) for language deviation — "
              f"retranscribe those segments in their real language.")
    else:
        print("No language deviations flagged.")
    return rows


def _find(name: str, tools_dir=None):
    from .download import find_tool
    return find_tool(name, tools_dir)
