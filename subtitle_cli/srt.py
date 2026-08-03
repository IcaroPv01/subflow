"""Shared SRT parsing / serialization utilities for SubFlow."""

from __future__ import annotations

import re
from pathlib import Path

TS_RE = re.compile(
    r"(\d{2}):(\d{2}):(\d{2})[,.](\d{3})\s*-->\s*"
    r"(\d{2}):(\d{2}):(\d{2})[,.](\d{3})"
)


def to_ms(h, m, s, ms):
    return ((int(h) * 60 + int(m)) * 60 + int(s)) * 1000 + int(ms)


def fmt_ms(ms):
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def norm(text: str) -> str:
    return text.lstrip("\ufeff").replace("\r\n", "\n").replace("\r", "\n").strip()


def read_text(path) -> str:
    return Path(path).read_text(encoding="utf-8", errors="replace")


def parse(path_or_text):
    """Parse SRT (path or text) -> list of cues [start_ms, end_ms, [lines]].

    Empty lines inside a cue body are dropped (matches the clean-up passes).
    """
    text = read_text(path_or_text) if isinstance(path_or_text, (str, Path)) else path_or_text
    cues = []
    for b in re.split(r"\n\s*\n", norm(text)):
        lines = b.split("\n")
        ti = next((i for i, l in enumerate(lines) if TS_RE.search(l)), None)
        if ti is None:
            continue
        m = TS_RE.search(lines[ti])
        start = to_ms(*m.group(1, 2, 3, 4))
        end = to_ms(*m.group(5, 6, 7, 8))
        body = [l for l in lines[ti + 1:] if l.strip()]
        cues.append([start, end, body])
    return cues


def serialize(cues) -> str:
    """Serialize cues (renumbered 1..N) to SRT text."""
    out = []
    for k, (start, end, body) in enumerate(cues, 1):
        out.append(str(k))
        out.append(f"{fmt_ms(start)} --> {fmt_ms(end)}")
        out.extend(body)
        out.append("")
    return "\n".join(out).rstrip("\n") + "\n"
