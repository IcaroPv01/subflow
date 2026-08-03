"""QC checks for subtitle SRTs — readability / timing / formatting.

Netflix-style profile by default: max 42 chars/line, max 2 lines, CPS warn 17
/ error 20, duration 1.0–7.0 s, min gap 80 ms, overlap = error.
"""

from __future__ import annotations

from pathlib import Path

from .srt import parse

# Default limits (overridable via CLI).
MAX_LINE_LEN = 42
MAX_LINES = 2
CPS_WARN = 17.0
CPS_ERROR = 20.0
MIN_DUR = 1.0
MAX_DUR = 7.0
MIN_GAP_MS = 80


def check(cues, max_line_len=MAX_LINE_LEN, max_lines=MAX_LINES,
          cps_warn=CPS_WARN, cps_error=CPS_ERROR, min_dur=MIN_DUR,
          max_dur=MAX_DUR, min_gap_ms=MIN_GAP_MS):
    """Return issues: list of (cue_index, severity, message)."""
    issues = []
    for i, c in enumerate(cues):
        idx = i + 1
        dur_ms = c[1] - c[0]
        dur = dur_ms / 1000.0
        text_lines = [ln for ln in c[2] if ln.strip()]
        joined = " ".join(text_lines)
        nchars = len(joined)

        if not text_lines:
            issues.append((idx, "ERROR", "empty cue"))
            continue

        if dur_ms <= 0:
            issues.append((idx, "ERROR", f"invalid duration ({dur:.2f}s)"))
        else:
            if dur < min_dur:
                issues.append((idx, "WARN", f"short duration ({dur:.2f}s < {min_dur}s)"))
            if dur > max_dur:
                issues.append((idx, "WARN", f"long duration ({dur:.2f}s > {max_dur}s)"))
            cps = nchars / dur
            if cps > cps_error:
                issues.append((idx, "ERROR", f"CPS {cps:.1f} > {cps_error} ({nchars} chars / {dur:.2f}s)"))
            elif cps > cps_warn:
                issues.append((idx, "WARN", f"CPS {cps:.1f} > {cps_warn} ({nchars} chars / {dur:.2f}s)"))

        if len(text_lines) > max_lines:
            issues.append((idx, "ERROR", f"{len(text_lines)} lines (max {max_lines})"))

        for ln in text_lines:
            if len(ln) > max_line_len:
                issues.append((idx, "WARN", f"line with {len(ln)} chars (>{max_line_len}): {ln!r}"))

        # gap / overlap with the next cue
        if i + 1 < len(cues):
            gap = cues[i + 1][0] - c[1]
            if gap < 0:
                issues.append((idx, "ERROR", f"overlap with next ({gap} ms)"))
            elif gap < min_gap_ms:
                issues.append((idx, "WARN", f"short gap to next ({gap} ms < {min_gap_ms} ms)"))
    return issues


def qc_srt(input_path, report_path=None, **limits):
    """Run QC on an SRT file. Writes a report if report_path is given.

    Returns (report_text, n_cues, n_errors, n_warnings).
    """
    cues = parse(input_path)
    issues = check(cues, **limits)
    errors = [x for x in issues if x[1] == "ERROR"]
    warns = [x for x in issues if x[1] == "WARN"]

    lines = [
        f"QC report — {input_path}",
        f"Cues: {len(cues)} | ERRORS: {len(errors)} | WARNINGS: {len(warns)}",
        "=" * 60,
    ]
    if not issues:
        lines.append("No problems found.")
    for idx, sev, msg in issues:
        lines.append(f"[{sev}] #{idx}: {msg}")
    report = "\n".join(lines) + "\n"

    if report_path:
        p = Path(report_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(report, encoding="utf-8")
    return report, len(cues), len(errors), len(warns)
