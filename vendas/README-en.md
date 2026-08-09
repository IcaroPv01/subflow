# SubFlow — Local-first subtitle pipeline

> **One CLI. One command. Professional subtitles from any video, 100% locally.**

```
$ subflow run "https://archive.org/soleil-o.mp4" --src-lang fr --tgt-lang pt
[1/6] downloading audio ... done
[2/6] transcribing (faster-whisper, large-v2, int8_float16)... 1247 cues
[3/6] building glossary (60 terms)... done
[4/6] translating in 22 batches... 4h15
[5/6] building SRT... done
[6/6] clean + QC + langcheck... 0 errors
Done in 7h 52min -> translation/out_clean.srt
```

A 104-min documentary subtitled in 7h50. Same quality as 14h of manual work.

## Why SubFlow

| | SubFlow | Subtitle Edit | Descript | OpenAI Whisper API |
|---|---|---|---|---|
| Cost per video | **$0** | $0 | $24/mo | ~$1/film |
| Privacy | **100% local** | local | ❌ upload | ❌ upload |
| Automatic QC | **Netflix-style** | partial | partial | ❌ |
| Hallucination detection | **langcheck** | ❌ | ❌ | ❌ |
| Batch translation | **yes (text-only)** | ❌ | yes | ❌ |
| License | **MIT** | GPL | proprietary | proprietary |

**SubFlow is the only open-source pipeline that combines local Whisper + Netflix-style QC + hallucination detection + batch translation.**

See [vendas/comparativo.md](https://github.com/IcaroPv01/subflow/blob/main/vendas/comparativo.md) for the full comparison.

## Use cases

- **Professional subtitlers**: 6× → 1.3× video length, same quality
- **Translation agencies**: license the pipeline to scale (commercial license: $9.99)
- **Documentary / indie film**: any source language → any target, including Arabic, Mandarin, Japanese
- **Privacy-sensitive work** (legal, medical, corporate): video never leaves the machine

## What's inside

- `subtitle_cli` — stdlib-only Python (works on any Python 3.10+)
- `faster-whisper` integration (or standalone Whisper-XXL binary)
- `yt-dlp` + `ffmpeg` for downloads
- `SKILL.md` — Claude Code skill (agent-assisted translation)

## Quickstart

```bash
pip install .
subflow init --name my-film
subflow run "https://youtu.be/..." --src-lang fr --tgt-lang pt
# ... translate the batches ...
subflow build --source transcription/audio.srt --text-dir translation --output out.srt
subflow clean --input out.srt --output out_clean.srt --merge --extend
subflow qc --profile netflix --input out_clean.srt
subflow langcheck --audio audio.wav --srt transcription/audio.srt --src-lang fr
```

## Resources

- [Free PT-BR guide (PDF)](https://raw.githubusercontent.com/IcaroPv01/subflow/main/vendas/isca/guia-legendagem-profissional-pt-br.pdf) — 9 sections, 15-min read
- [Try the demo](https://huggingface.co/spaces/IcaroPv01/subflow-demo) — free, no signup
- [Comparison vs alternatives](https://github.com/IcaroPv01/subflow/blob/main/vendas/comparativo.md)

## License & pricing

- **CLI + skill**: MIT (use freely for personal/non-commercial)
- **Commercial license** (sell subtitle services, white-label): $9.99 — pay.hotmart.com/E107014071J
- **Pro tier** (templates, PT-BR presets, lifetime updates): $24.99

## Feedback

Open an issue, discussion, or reach out via the repo. I'm actively iterating.
