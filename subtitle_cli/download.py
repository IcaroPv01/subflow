"""Download audio (and optional light video) via yt-dlp."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


def find_tool(name: str, tools_dir=None):
    if tools_dir:
        base = Path(tools_dir)
        p = base / name
        if p.is_file():  # is_file, not exists: a bundle dir may share the name
            return str(p)
        # bundled layouts often nest tools in subfolders (e.g. tools/bin/,
        # tools/Faster-Whisper-XXL/, tools/ffmpeg-*/bin/): search recursively
        for p in base.rglob(name):
            if p.is_file():
                return str(p)
    return shutil.which(name)


def download_audio(url: str, out_dir, password=None, tools_dir=None,
                   max_filesize_mb: int = 0):
    """Download the audio track of `url` for transcription.

    Returns the path of the downloaded file. Pass `--video-password` via
    `password` for protected streams (e.g. Vimeo password screens).

    Note: on Vimeo, direct downloads can stall on bandwidth limits; if that
    happens, fetch the stream directly with ffmpeg — see docs/PIPELINE.md.
    """
    yt = find_tool("yt-dlp.exe", tools_dir) or find_tool("yt-dlp", tools_dir)
    if not yt:
        raise RuntimeError("yt-dlp not found (pass --tools-dir or install yt-dlp)")
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    cmd = [yt, "-f", "bestaudio", "-o", str(out_dir / "%(title)s.%(ext)s")]
    if password:
        cmd += ["--video-password", password]
    if max_filesize_mb > 0:
        cmd += ["--max-filesize", f"{max_filesize_mb}M"]
    subprocess.run(cmd, check=False)
    # newest media file in out_dir is the download
    media = [p for p in out_dir.iterdir() if p.suffix.lower() in
             (".m4a", ".mp3", ".opus", ".webm", ".wav", ".aac", ".flac")]
    if not media:
        raise RuntimeError("no audio file produced by yt-dlp")
    return str(max(media, key=lambda p: p.stat().st_mtime))
