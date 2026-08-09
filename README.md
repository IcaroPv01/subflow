# SubFlow

[![Buy on Hotmart](https://img.shields.io/badge/Buy-Hotmart-orange)](https://pay.hotmart.com/E107014071J)


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

**Download:** grab the latest wheel/zip (no build needed) from
[Releases](https://github.com/IcaroPv01/subflow/releases) — or build from source:

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


## Free guide (PT-BR)

A 9-section e-book on professional PT-BR subtitling with local Whisper — covers the
pipeline, Netflix-style QC, glossary construction, ASR hallucination detection, and a
real case study (104-min film in 7h50). Free PDF (~20 KB):

**[Download the free guide (PDF, PT-BR)](https://raw.githubusercontent.com/IcaroPv01/subflow/main/vendas/isca/guia-legendagem-profissional-pt-br.pdf)**
| [Landing page (PT-BR)](https://raw.githubusercontent.com/IcaroPv01/subflow/main/vendas/landing/guia-gratuito.html)
| [Landing page (EN)](https://raw.githubusercontent.com/IcaroPv01/subflow/main/vendas/landing/index.html)
| [Watch the GIF demo](https://raw.githubusercontent.com/IcaroPv01/subflow/main/vendas/assets/demo.gif)
| [Compare with alternatives](https://github.com/IcaroPv01/subflow/blob/main/vendas/comparativo.md)

## Resources

- **Video demo (YouTube):** [Subtitle a whole film in under 8 hours (Whisper, local, free)](https://www.youtube.com/watch?v=8wywC_Evx9E)
- **Buy on Hotmart (US$ 9.99):** https://pay.hotmart.com/E107014071J

## License

MIT. The bundled binaries (yt-dlp, ffmpeg, Faster-Whisper) are not part of this
package — download them separately per their own licenses.
