"""Assemble a target-language SRT by mapping translation batches onto source
timestamps.

Timestamps come 100% from the source transcription -> zero timing risk.
Translation is text-only, keyed by cue number (see templates/prompt_batch.txt).
"""

from __future__ import annotations

import re
from pathlib import Path

from .srt import TS_RE, norm, read_text

DEFAULT_MAX_LINE = 42


def parse_source(path):
    """Return (order, ts) where order is the source cue-number sequence and
    ts maps cue number -> original timestamp line."""
    blocks = re.split(r"\n\s*\n", norm(read_text(path)))
    order, ts = [], {}
    for b in blocks:
        lines = b.split("\n")
        ti = next((i for i, l in enumerate(lines) if TS_RE.search(l)), None)
        if ti is None or ti == 0:
            continue
        idx = lines[ti - 1].strip()
        order.append(idx)
        ts[idx] = lines[ti].strip()
    return order, ts


def parse_text(paths):
    """Parse translation batch files -> dict cue_number -> [lines].

    Expected format per block: a cue number line, then the translated text.
    """
    d = {}
    for p in sorted(paths):
        blocks = re.split(r"\n\s*\n", norm(read_text(p)))
        for b in blocks:
            lines = b.split("\n")
            if not lines or not lines[0].strip():
                continue
            idx = lines[0].strip()
            body = list(lines[1:])
            while body and not body[-1].strip():
                body.pop()
            d[idx] = body
    return d


def build(source, text_dir, prefix="pt_text_", output=None, max_line=DEFAULT_MAX_LINE):
    """Map translations onto source timestamps.

    Returns (srt_text, report). Writes `output` if given.
    """
    order, ts = parse_source(source)
    texts = parse_text(list(Path(text_dir).glob(prefix + "*.txt")))

    missing = [i for i in order if i not in texts]
    extra = [i for i in texts if i not in ts]

    out, longlines, threelines = [], [], []
    for i in order:
        body = texts.get(i, ["<<MISSING>>"])
        if len([l for l in body if l.strip()]) > 2:
            threelines.append(i)
        for ln in body:
            if len(ln) > max_line:
                longlines.append((i, len(ln), ln))
        out.append(i)
        out.append(ts[i])
        out.extend(body)
        out.append("")

    srt_text = "\n".join(out).rstrip("\n") + "\n"
    report = {
        "source": len(order),
        "translated": len(texts),
        "missing": missing,
        "extra": extra,
        "three_lines": threelines,
        "long_lines": longlines,
    }
    if output:
        Path(output).write_text(srt_text, encoding="utf-8")
    return srt_text, report
