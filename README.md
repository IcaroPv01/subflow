# SubFlow

**Turn any video into professional subtitles.** From a URL or a local file, SubFlow
transcribes, translates (LLM-assisted), cleans and quality-checks subtitles — and
verifies that the transcription isn't hallucinating a language. Runs locally, no
per-video API cost.

- **Full pipeline, one command** — `subflow run` downloads the audio, transcribes it,
  and hands off to the skill for translation; `build`/`clean`/`qc` finish the job.
- **Professional QC built in** — Netflix-style profile (≤42 chars/line, ≤2 lines,
  CPS 17/20, duration 1–7 s, no overlaps) plus automatic clean-up passes that fix
  Whisper's mid-sentence cuts and stretch cue ends into silence to hit reading speed.
- **Handles hard languages** — `langcheck` samples clips across the film and maps
  the real languages, catching ASR hallucination (a forced-French pass once
  "invented" French over Hassaniya Arabic song — that section was translating an
  invention).
- **Zero timing risk** — translation is text-only, keyed by cue number; timestamps
  always come from the source transcription.
- **Cheap to run** — everything is local: a standalone Whisper binary (fits large
  models in a 4 GB GPU via `int8_float16`), stdlib-only Python, optional GPU.

## Quickstart

```bash
pip install .                # from the skill/ folder; provides `subflow`
subflow init --name my-film  # create the project layout
subflow run "https://..." --password P --src-lang fr --tools-dir tools
# ... translate the batches (the SubFlow skill does this for you) ...
subflow build --source transcription/audio.srt --text-dir translation --output translation/out.srt
subflow clean --input translation/out.srt --output translation/out_cps.srt --merge --extend
subflow qc translation/out_cps.srt --report qc/qc_report.txt
subflow langcheck audio/audio.m4a --srt transcription/audio.srt --expected fr
```

## Requirements

- Python ≥ 3.10 (standard library only)
- One of: **Faster-Whisper-XXL standalone binary** (Windows, GPU optional) or
  `pip install faster-whisper`
- Offline models: pass `--model-dir` to keep Whisper fully local (no downloads)
- `yt-dlp` + `ffmpeg` for URL downloads (local files skip this)

## How translation works

The SubFlow **skill** (Claude Code) runs the pipeline: it builds a glossary first
(consistent proper-noun spelling = professional subtitles), translates in batches
using the template prompt, and runs an **independent, cheap-model review** that
re-checks the language map and re-translates flagged sections blindly. The CLI
guarantees the mechanics; the skill owns the translation quality.

## QC profile (defaults, all configurable)

| Check | Threshold |
|---|---|
| Line length | ≤ 42 chars |
| Lines per cue | ≤ 2 |
| Reading speed (CPS) | warn > 17, error > 20 |
| Duration | 1.0 – 7.0 s |
| Gap to next cue | ≥ 80 ms; overlap = error |

## Selling points

- Works with **any source → any target language** (your choice, including Arabic-script ones).
- One human pass at the end (Subtitle Edit) — the AI does 95%.
- No GPU required (slow but works on CPU); GPU makes it minutes, not hours.

## License

MIT. The bundled binaries (yt-dlp, ffmpeg, Faster-Whisper) are not part of this
package — download them separately per their own licenses.
