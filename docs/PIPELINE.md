# SubFlow pipeline — how each stage works

This document explains *why* each stage exists. It is the engineering
justification behind the tool — useful for buyers who want to trust the output.

## 1. Download (yt-dlp + ffmpeg)

Only the **audio track** is downloaded for transcription (~fast, small). A light
video copy is optional, kept for the final human visual pass. On Vimeo, direct
downloads can stall on bandwidth limits — workaround: pull the stream directly
with ffmpeg (`yt-dlp -g URL` to get the stream URL, then `ffmpeg -i URL -c copy out.m4a`).

## 2. Transcribe (Faster-Whisper / faster-whisper)

The standalone Faster-Whisper-XXL build works on any Python version (important:
Python 3.14+ blocks most AI pip packages, so standalone binaries are the robust
path). `--compute-type int8_float16` quantization fits `large-v2` in a 4 GB GPU
with near-identical quality — that is what makes big models run on small machines.

The `--standard` preset produces timed cues. Never assume the forced language is
correct — Whisper **hallucinates** when the real language differs (see langcheck).

## 3. Glossary

Before translating, list every proper noun with a fixed spelling. Human
translators do this; most automated pipelines skip it — and it shows. Consistent
spelling across the whole SRT is the cheapest quality upgrade available.

## 4. Translate in batches (text only)

This is the core engineering decision: translation is done **text-only**, keyed
by cue number, and a script maps the text onto the original timestamps. The AI
(LLM) does what it is good at (translation); the script does what it is good at
(precision). Timing errors become impossible by construction.

## 5. Build

`build` re-uses the exact source timestamp lines and only swaps the text. It
reports missing/extra cue numbers, >2-line cues and >42-char lines, so nothing
silently breaks.

## 6. Clean

Two conservative passes, neither touches start times, neither creates overlaps:

- **merge**: Whisper cuts sentences mid-word, leaving tiny tails (e.g. "o norte ao
  sul.", 0.32 s, absurd CPS). Tails are joined to the previous cue only when the
  previous cue doesn't end in punctuation (i.e. a real mid-sentence cut), the gap
  is ≤ 250 ms, and the combined text still fits 2×42 chars.
- **extend**: each cue's end is stretched into the following silence (never past
  `next_start − min_gap`, never past 7 s) until reading speed reaches ~15 CPS.
  Real result: CPS errors dropped 86 → 15 on a 64-minute documentary.

## 7. QC

Readability/timing audit: line length, line count, CPS, durations, gaps, overlaps.
Defaults are Netflix-style and all configurable via CLI flags. Output is a
prioritized report for the human final pass.

## 8. Langcheck — the "hard languages" differentiator

Whisper forced to one language can transcribe *invented* text over foreign audio.
Real case: a 1977 documentary's final song was in Hassaniya Arabic, but a
French-forced pass produced plausible-sounding French — the translation of that
section was translating an invention.

`langcheck` samples N clips spread across the film and runs each with **automatic
language detection**, producing a language map (`_summary.md`). Clips deviating
from the expected language (or the majority) are flagged; those segments are then
re-transcribed in their real language and reconciled. This turns "the model lied
to us" from a silent disaster into a detected, fixable condition.

## 9. Independent review

A second, cheaper, independent agent re-does the language map from scratch and
re-translates flagged sections *blind* (without seeing your conclusions), then
compares. Independent review costs little and catches bias — the same reason
peer review works in science.

## Appendix — ASR error correction

Examples of transcription errors caught during translation (Hondo, 1977):
Whisper heard "Rio de Janeiro" instead of **Río de Oro** (a region); "police
aérien" instead of **Polisário** (the movement). The translator's ear + glossary
fixes these; the QC report then confirms the SRT is clean.
