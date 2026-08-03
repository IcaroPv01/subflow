---
name: subflow
description: Turn a video (local file or URL) into professional translated subtitles (SRT) — download, transcribe with Whisper, build a glossary, translate in batches, clean, QC and verify languages. Use when the user wants subtitles for a film/video in another language, wants a video transcribed, or wants an SRT cleaned/QC'd.
---

# SubFlow — video → professional subtitles

Full pipeline: **download → transcribe → glossary → translate (batches) → build → clean → QC → langcheck → independent review**.

The CLI engine (`subtitle_cli`, stdlib-only) does the mechanical work; **you** (the agent) do the actual translation and the quality judgment. The golden rule: *the AI translates text, scripts guarantee timings* — never let translation drift into timing.

## Project layout (create with `subflow init`)

```
audio/          downloaded audio track
video/          optional light video for visual QC
transcription/  source-language SRT from Whisper
glossary/       glossary (names/places/terms) before translating
translation/    batch text files (translation/*.txt) + built SRTs
qc/             QC reports
```

## Requirements (check before starting)

- `subflow` CLI: Python ≥ 3.10, stdlib only.
- Transcription: the **Faster-Whisper-XXL standalone binary** (works on any Python, GPU optional; `--compute-type int8_float16` fits large models in 4 GB GPUs) **or** `pip install faster-whisper`.
- `yt-dlp` + `ffmpeg` for downloads.
- Pass `--tools-dir` when tools are bundled in a folder (e.g. `tools/`).

## Step-by-step

### 1. Download
`subflow run URL --password P --src-lang XX --tools-dir tools` (audio only, ~fast).
Troubleshooting: Vimeo stalls on bandwidth → pull the stream directly with ffmpeg; Python 3.14 blocks most AI libs → use standalone binaries.

### 2. Transcribe
Whisper with `--standard`, `int8_float16` on GPU. **Do not force a language blindly** — pass `auto` or the language you are confident about, then verify (step 7).

### 3. Build the glossary (before any translation)
Create `glossary/glossary.md` from `templates/glossary_template.md`: every proper noun (people, places, organizations, political terms, titles) with columns *Source | Translation | Notes*. Golden rule: **consistent spelling across the whole SRT** — this is what separates amateur from professional subtitles.

### 4. Translate in batches (text only — never timestamps)
Split the source cues into batches (e.g. 100–150 cues each) and translate each batch into `translation/<prefix>NNN.txt`. Format per block:

```
<cue number from the source SRT>
<translated text, ≤2 lines, ≤42 chars/line>
```

Use `templates/prompt_batch.txt` as your translation prompt. Rules:
- Translate **text only**, keyed by cue number. The build step maps text to the source timestamps — zero timing risk.
- ≤ 42 chars per line, ≤ 2 lines per cue.
- Apply the glossary exactly; flag any new proper noun found in the batch and add it to the glossary.
- Correct ASR errors you can detect (e.g. Whisper heard "Rio de Janeiro" for "Río de Oro", or "police aérien" for "Polisário").

### 5. Build
`subflow build --source transcription/audio.srt --text-dir translation --output translation/out.srt`
Checks: missing/extra cue numbers, >2 lines, >42 chars. All must be clean.

### 6. Clean + QC
`subflow clean --input out.srt --output out_cps.srt --merge --extend` then
`subflow qc out_cps.srt --report qc/qc_report.txt`
- `merge` joins mid-sentence cuts (Whisper fragments) to the previous cue — improves CPS without touching sync.
- `extend` stretches each cue's end into the following silence (never overlaps) until ~15 CPS.
- QC profile: ≤42 chars/line, ≤2 lines, CPS warn 17 / error 20, duration 1–7 s, min gap 80 ms, overlap = error.
- If errors remain, fix the worst CPS/overlap cues by hand (Subtitle Edit) — the human eye/ear owns the final pass.

### 7. Langcheck — verify the language map (the "hard languages" step)
Whisper **hallucinates** when forced to a wrong language (real case: a French-forced pass invented French over Hassaniya Arabic song — the translation had been translating an invention).
`subflow langcheck AUDIO --srt transcription/audio.srt --clips 10 --expected XX --tools-dir tools`
- Slices clips across the film, auto-detects language per clip, writes `_summary.md`, flags deviations.
- For flagged segments: **retranscribe in their real language**, reconcile with the other transcription, rebuild the affected cues.

### 8. Independent review (cheap, unbiased)
Spawn **separate, cheaper-model agents** and *don't* tell them your conclusions:
- one re-maps the languages of the whole film from scratch;
- one (reading the source language) re-translates a flagged section and compares with yours.
Both should confirm your work; fix whatever they find.

### 9. Deliver
Final SRT (`out_cps.srt`) + QC report + glossary. Mark known gaps (e.g. repeated song) for the human to decide (`♪` markers in Subtitle Edit).

## When to refuse / warn

- If the source audio is unclear or the transcription quality is too poor to translate reliably, say so and propose a different model/preset before translating garbage.
- Copyright: subtitling a video for personal/educational use is fine; remind the user that redistributing copyrighted film content requires rights.
