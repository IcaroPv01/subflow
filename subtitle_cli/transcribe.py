"""Transcribe audio to SRT.

Primary path: the Faster-Whisper-XXL standalone binary (Purfview build) —
works on any Python, includes GPU support, bundles everything.
Fallback: the `faster-whisper` Python package.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from .srt import read_text

BINARY_NAMES = ("faster-whisper-xxl.exe", "faster-whisper-xxl", "faster-whisper")


def find_whisper(tools_dir=None):
    if tools_dir:
        base = Path(tools_dir)
        for name in BINARY_NAMES:
            p = base / name
            if p.is_file():  # is_file, not exists: a bundle dir may share the name
                return str(p)
        # bundled layouts nest the exe in a subfolder (e.g. tools/Faster-Whisper-XXL/)
        for name in BINARY_NAMES:
            for p in base.rglob(name):
                if p.is_file():
                    return str(p)
    for name in BINARY_NAMES:
        w = shutil.which(name)
        if w:
            return w
    return None


def transcribe_binary(audio: str, out_dir, model="large-v2", device="auto",
                      compute_type="int8_float16", language=None,
                      tools_dir=None, model_dir=None, extra=()):
    """Transcribe via the standalone binary. Returns the SRT path produced."""
    exe = find_whisper(tools_dir)
    if not exe:
        raise RuntimeError(
            "faster-whisper binary not found. Pass --tools-dir (folder with "
            "faster-whisper-xxl.exe) or install the 'faster-whisper' package."
        )
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    cmd = [exe, str(audio), "-o", str(out_dir), "-f", "srt",
           "--model", model, "--device", device,
           "--compute_type", compute_type, "--standard"]
    if model_dir:
        cmd += ["--model_dir", str(model_dir)]
    if language and language.lower() != "auto":
        cmd += ["--language", language]
    cmd += list(extra)
    print(" ".join(cmd))
    subprocess.run(cmd, check=False)
    srts = sorted(out_dir.glob("*.srt"), key=lambda p: p.stat().st_mtime)
    if not srts:
        raise RuntimeError("transcription produced no .srt output")
    return str(srts[-1])


def transcribe_python(audio: str, out_dir, model="large-v2", device="auto",
                      compute_type="int8_float16", language=None, model_dir=None):
    """Transcribe via the faster-whisper Python package (fallback).

    Returns (srt_path, detected_language, language_probability).
    """
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        raise RuntimeError(
            "no standalone binary found and 'faster-whisper' is not installed. "
            "pip install faster-whisper, or pass --tools-dir."
        )
    import json

    from .srt import serialize

    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    if model_dir:
        model = str(Path(model_dir) / model)
    model_obj = WhisperModel(model, device=device, compute_type=compute_type)
    segments, info = model_obj.transcribe(audio, language=None if language in (None, "auto") else language)
    cues = []
    for seg in segments:
        cues.append([int(seg.start * 1000), int(seg.end * 1000),
                     [seg.text.strip()]])
    # group short segments into 2-line cues like the binary preset would
    cues = _group_cues(cues)
    srt_path = out_dir / (Path(audio).stem + ".srt")
    srt_path.write_text(serialize(cues), encoding="utf-8")
    meta = {"language": info.language, "language_probability": info.language_probability}
    (out_dir / (Path(audio).stem + ".meta.json")).write_text(
        json.dumps(meta, ensure_ascii=False), encoding="utf-8")
    return str(srt_path), info.language, info.language_probability


def _group_cues(cues, max_chars=84, max_gap_ms=500):
    """Fold tiny whisper segments into 2-line cues (rough analogue of the
    binary's standard preset). Purely a fallback convenience."""
    out = []
    for c in cues:
        if out and c[0] - out[-1][1] <= max_gap_ms:
            prev_text = " ".join(out[-1][2])
            if len(prev_text) + len(c[2][0]) <= max_chars:
                out[-1][1] = c[1]
                out[-1][2] = [prev_text + " " + c[2][0]]
                continue
        out.append(list(c))
    return out
