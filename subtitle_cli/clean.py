"""Clean-up passes for subtitle SRTs.

merge  — join continuation fragments (mid-sentence cuts) to the previous cue.
extend — stretch each cue's END into the following silence to lower CPS.

Both never touch start times (a cue never appears before its speech) and
never create overlaps.
"""

from __future__ import annotations

from pathlib import Path

from .srt import parse, read_text, serialize

DEFAULT_MAX_LINE = 42
DEFAULT_MAX_GAP_MS = 250
NO_MERGE_AFTER = set('.?!:,…")»')


def wrap2(text: str, max_line: int = DEFAULT_MAX_LINE):
    """Wrap text into 2 lines of <= max_line chars, best-balanced split."""
    if len(text) <= max_line:
        return [text]
    words = text.split()
    best = None
    for k in range(1, len(words)):
        l1, l2 = " ".join(words[:k]), " ".join(words[k:])
        if len(l1) <= max_line and len(l2) <= max_line:
            score = abs(len(l1) - len(l2))
            if best is None or score < best[0]:
                best = (score, [l1, l2])
    return best[1] if best else None


def merge_cues(cues, max_line: int = DEFAULT_MAX_LINE, max_gap_ms: int = DEFAULT_MAX_GAP_MS):
    """Merge continuation tails into the previous cue. Conservative rule:
    only merge when the previous cue does not end in punctuation (i.e. it is a
    mid-sentence cut) and the gap is small and the combined text fits 2 lines."""
    out = []
    i, n, merged = 0, len(cues), 0
    while i < n:
        start, end, body = cues[i][0], cues[i][1], list(cues[i][2])
        j = i + 1
        while j < n:
            prev = " ".join(body).strip()
            if not prev or prev[-1] in NO_MERGE_AFTER:
                break
            gap = cues[j][0] - end
            if gap < 0 or gap > max_gap_ms:
                break
            combined = (prev + " " + " ".join(cues[j][2]).strip()).strip()
            wrapped = wrap2(combined, max_line)
            if wrapped is None:
                break
            end = cues[j][1]
            body = wrapped
            merged += 1
            j += 1
        out.append([start, end, body])
        i = j
    return out, merged


def extend_cues(cues, target_cps: float = 15.0, min_gap_ms: int = 120,
                max_dur_ms: int = 7000, last_pad_ms: int = 3000):
    """Extend each cue's END into the following silence (never shrink, never
    overlap) until the reading speed reaches ~target_cps (if there is room)."""
    changed = 0
    for i in range(len(cues)):
        start, end, body = cues[i]
        nchars = len(" ".join(body))
        if nchars == 0:
            continue
        limit = (cues[i + 1][0] - min_gap_ms) if i + 1 < len(cues) else (end + last_pad_ms)
        desired = start + int(nchars / target_cps * 1000)
        new_end = max(end, min(desired, limit, start + max_dur_ms))
        if new_end > end:
            cues[i][1] = new_end
            changed += 1
    return cues, changed


def merge_srt(input_path, output_path, backup_path=None,
              max_line=DEFAULT_MAX_LINE, max_gap_ms=DEFAULT_MAX_GAP_MS):
    cues = parse(input_path)
    if backup_path:
        Path(backup_path).write_text(read_text(input_path), encoding="utf-8")
    merged_cues, merged = merge_cues(cues, max_line, max_gap_ms)
    Path(output_path).write_text(serialize(merged_cues), encoding="utf-8")
    return len(cues), len(merged_cues), merged


def extend_srt(input_path, output_path, target_cps=15.0, min_gap_ms=120,
               max_dur_ms=7000, last_pad_ms=3000):
    cues = parse(input_path)
    cues, changed = extend_cues(cues, target_cps, min_gap_ms, max_dur_ms, last_pad_ms)
    Path(output_path).write_text(serialize(cues), encoding="utf-8")
    return len(cues), changed
