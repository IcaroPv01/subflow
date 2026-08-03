"""SubFlow command-line interface.

Usage:
    subflow init [--name NAME]                     create project layout
    subflow download URL [--password P] [--tools-dir D] [--out-dir D]
    subflow transcribe AUDIO [--model M] [--device D] [--compute-type C]
                           [--language L] [--tools-dir D] [--out-dir D]
    subflow build --source SRC.srt --text-dir DIR [--prefix P] [--output OUT]
    subflow clean --input IN.srt --output OUT.srt [--merge] [--extend] [...]
    subflow qc FILE.srt [--report R] [--cps-warn X] [...]
    subflow langcheck AUDIO [--srt S] [--clips N] [--duration S]
                          [--expected LANG] [--tools-dir D] [--out-dir D]
    subflow run URL [--password P] [--src-lang L] [--tools-dir D]
                    [--project-dir D]

Pure standard library — Python >= 3.10.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from . import build as _build
from . import clean as _clean
from . import download as _download
from . import langcheck as _langcheck
from . import qc as _qc
from . import transcribe as _transcribe

PROJECT_DIRS = ("audio", "video", "transcription", "glossary", "translation", "qc")


def cmd_init(args):
    base = Path(args.project_dir)
    for d in PROJECT_DIRS:
        (base / d).mkdir(parents=True, exist_ok=True)
    if args.name:
        (base / "NOTES.md").write_text(
            f"# {args.name}\n\nPipeline: download -> transcribe -> glossary -> "
            f"translate (batches) -> build -> clean -> QC\n", encoding="utf-8")
    print(f"Project layout created in {base}")
    for d in PROJECT_DIRS:
        print(f"  {base / d}/")


def cmd_download(args):
    out = _download.download_audio(args.url, args.out_dir, password=args.password,
                                   tools_dir=args.tools_dir)
    print(f"Downloaded: {out}")


def cmd_transcribe(args):
    out = _transcribe.transcribe_binary(
        args.audio, args.out_dir, model=args.model, device=args.device,
        compute_type=args.compute_type, language=args.language,
        tools_dir=args.tools_dir, model_dir=args.model_dir)
    print(f"Transcription: {out}")


def cmd_build(args):
    srt, report = _build.build(args.source, args.text_dir, prefix=args.prefix,
                               output=args.output, max_line=args.max_line)
    print(f"Source cues: {report['source']} | translated: {report['translated']} "
          f"| missing: {len(report['missing'])} | extra: {len(report['extra'])}")
    for i in report["missing"][:60]:
        print(f"  MISSING #{i}")
    for i in report["extra"][:60]:
        print(f"  EXTRA (not in source) #{i}")
    if report["three_lines"]:
        print(f">2 lines: {report['three_lines']}")
    if report["long_lines"]:
        print(f"Lines >{args.max_line} chars: {len(report['long_lines'])}")
        for i, n, ln in report["long_lines"][:60]:
            print(f"  #{i} ({n}): {ln}")
    if not (report["missing"] or report["extra"] or report["long_lines"]
            or report["three_lines"]):
        print("OK: all indexes match, <=2 lines, <=42 chars/line.")
    if args.output:
        print(f"Output: {args.output}")


def cmd_clean(args):
    if args.merge:
        n, out_n, merged = _clean.merge_srt(
            args.input, args.output if not args.extend else args.output + ".tmp",
            backup_path=args.backup, max_line=args.max_line,
            max_gap_ms=args.max_gap_ms)
        print(f"Merge: {n} -> {out_n} cues ({merged} tails joined)")
        if args.extend:
            _clean.extend_srt(args.output + ".tmp", args.output,
                              target_cps=args.target_cps,
                              min_gap_ms=args.min_gap_ms,
                              max_dur_ms=args.max_dur_ms,
                              last_pad_ms=args.last_pad_ms)
            Path(args.output + ".tmp").unlink(missing_ok=True)
            print(f"Extend: done -> {args.output}")
    elif args.extend:
        n, changed = _clean.extend_srt(
            args.input, args.output, target_cps=args.target_cps,
            min_gap_ms=args.min_gap_ms, max_dur_ms=args.max_dur_ms,
            last_pad_ms=args.last_pad_ms)
        print(f"Extend: {changed}/{n} cues stretched -> {args.output}")
    else:
        print("Nothing to do: pass --merge and/or --extend", file=sys.stderr)
        sys.exit(1)


def cmd_qc(args):
    report, n, errors, warns = _qc.qc_srt(
        args.srt, report_path=args.report,
        max_line_len=args.max_line_len, max_lines=args.max_lines,
        cps_warn=args.cps_warn, cps_error=args.cps_error,
        min_dur=args.min_dur, max_dur=args.max_dur, min_gap_ms=args.min_gap_ms)
    print(f"Cues: {n} | ERRORS: {errors} | WARNINGS: {warns}")
    if args.report:
        print(f"Report: {args.report}")


def cmd_langcheck(args):
    _langcheck.run_langcheck(
        args.audio, srt_path=args.srt, clips=args.clips,
        duration_s=args.duration, expected=args.expected,
        out_dir=args.out_dir, tools_dir=args.tools_dir,
        model=args.model, device=args.device, compute_type=args.compute_type,
        model_dir=args.model_dir)


def cmd_run(args):
    base = Path(args.project_dir)
    for d in PROJECT_DIRS:
        (base / d).mkdir(parents=True, exist_ok=True)
    audio = _download.download_audio(args.url, base / "audio",
                                     password=args.password,
                                     tools_dir=args.tools_dir)
    srt = _transcribe.transcribe_binary(
        audio, base / "transcription", model=args.model, device=args.device,
        compute_type=args.compute_type, language=args.src_lang,
        tools_dir=args.tools_dir, model_dir=args.model_dir)
    print(f"\n=== Transcription done: {srt} ===")
    print("Next steps (the SubFlow skill does this for you):")
    print(f"  1. Build the glossary in {base / 'glossary'}")
    print(f"  2. Translate the cues in batches -> {base / 'translation'} (text only)")
    print(f"  3. subflow build --source {srt} --text-dir {base / 'translation'} "
          f"--output {base / 'translation' / 'out.srt'}")
    print(f"  4. subflow clean --input {base / 'translation' / 'out.srt'} "
          f"--output {base / 'translation' / 'out_cps.srt'} --merge --extend")
    print(f"  5. subflow qc {base / 'translation' / 'out_cps.srt'}")
    print(f"  6. subflow langcheck {audio} --srt {srt} "
          f"--expected {args.src_lang or 'auto'}")


def main(argv=None):
    p = argparse.ArgumentParser(
        prog="subflow", description="Turn any video into professional subtitles.")
    p.add_argument("--version", action="version", version=__version__)
    sub = p.add_subparsers(dest="command", required=True)

    pi = sub.add_parser("init", help="create project layout")
    pi.add_argument("--name")
    pi.add_argument("--project-dir", default=".")
    pi.set_defaults(func=cmd_init)

    pd = sub.add_parser("download", help="download audio from a video URL")
    pd.add_argument("url")
    pd.add_argument("--password")
    pd.add_argument("--tools-dir")
    pd.add_argument("--out-dir", default="audio")
    pd.set_defaults(func=cmd_download)

    pt = sub.add_parser("transcribe", help="transcribe audio to SRT")
    pt.add_argument("audio")
    pt.add_argument("--model", default="large-v2")
    pt.add_argument("--device", default="auto")
    pt.add_argument("--compute-type", default="int8_float16")
    pt.add_argument("--language", default=None, help="source language or 'auto'")
    pt.add_argument("--tools-dir")
    pt.add_argument("--model-dir", help="local folder containing the Whisper model")
    pt.add_argument("--out-dir", default="transcription")
    pt.set_defaults(func=cmd_transcribe)

    pb = sub.add_parser("build", help="map translation batches onto source timestamps")
    pb.add_argument("--source", required=True)
    pb.add_argument("--text-dir", required=True)
    pb.add_argument("--prefix", default="pt_text_")
    pb.add_argument("--output")
    pb.add_argument("--max-line", type=int, default=42)
    pb.set_defaults(func=cmd_build)

    pc = sub.add_parser("clean", help="merge fragments and/or extend to silence")
    pc.add_argument("--input", required=True)
    pc.add_argument("--output", required=True)
    pc.add_argument("--merge", action="store_true")
    pc.add_argument("--extend", action="store_true")
    pc.add_argument("--backup")
    pc.add_argument("--max-line", type=int, default=42)
    pc.add_argument("--max-gap-ms", type=int, default=250)
    pc.add_argument("--target-cps", type=float, default=15.0)
    pc.add_argument("--min-gap-ms", type=int, default=120)
    pc.add_argument("--max-dur-ms", type=int, default=7000)
    pc.add_argument("--last-pad-ms", type=int, default=3000)
    pc.set_defaults(func=cmd_clean)

    pq = sub.add_parser("qc", help="QC report (readability / timing)")
    pq.add_argument("srt")
    pq.add_argument("--report")
    pq.add_argument("--max-line-len", type=int, default=42)
    pq.add_argument("--max-lines", type=int, default=2)
    pq.add_argument("--cps-warn", type=float, default=17.0)
    pq.add_argument("--cps-error", type=float, default=20.0)
    pq.add_argument("--min-dur", type=float, default=1.0)
    pq.add_argument("--max-dur", type=float, default=7.0)
    pq.add_argument("--min-gap-ms", type=int, default=80)
    pq.set_defaults(func=cmd_qc)

    pl = sub.add_parser("langcheck", help="sample clips and map languages")
    pl.add_argument("audio")
    pl.add_argument("--srt")
    pl.add_argument("--clips", type=int, default=10)
    pl.add_argument("--duration", type=float, default=12.0)
    pl.add_argument("--expected")
    pl.add_argument("--model", default="large-v2")
    pl.add_argument("--device", default="auto")
    pl.add_argument("--compute-type", default="int8_float16")
    pl.add_argument("--tools-dir")
    pl.add_argument("--model-dir", help="local folder containing the Whisper model")
    pl.add_argument("--out-dir")
    pl.set_defaults(func=cmd_langcheck)

    pr = sub.add_parser("run", help="download + transcribe + handoff")
    pr.add_argument("url")
    pr.add_argument("--password")
    pr.add_argument("--src-lang")
    pr.add_argument("--model", default="large-v2")
    pr.add_argument("--device", default="auto")
    pr.add_argument("--compute-type", default="int8_float16")
    pr.add_argument("--tools-dir")
    pr.add_argument("--model-dir", help="local folder containing the Whisper model")
    pr.add_argument("--project-dir", default=".")
    pr.set_defaults(func=cmd_run)

    args = p.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
