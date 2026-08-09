# Textos de divulgação prontos (vídeo YouTube = 8wywC_Evx9E)

> Preparados pela instância de execução para colar quando o browser voltar.
> Vídeo: https://www.youtube.com/watch?v=8wywC_Evx9E
> Embed: `<iframe width="560" height="315" src="https://www.youtube.com/embed/8wywC_Evx9E" frameborder="0" allowfullscreen></iframe>`
> Checkout: https://pay.hotmart.com/E107014071J
> Repo: https://github.com/IcaroPv01/subflow

---

## 1. Comentário no r/whisper post (reddit.com/r/whisper/comments/1vfs2ug)

```
Built on top of Whisper — this is exactly the kind of workflow it enables. I put together
SubFlow, a 100% local pipeline: download → transcribe → glossary → batch translate →
build → clean → QC → langcheck. The QC is Netflix-style (≤42 chars/line, CPS 17/20, no
overlaps) and langcheck re-decodes each cue to catch ASR hallucination — a forced-French
pass once "invented" French over Hassaniya Arabic song lyrics.

90-second demo (local, free, no API cost): https://www.youtube.com/watch?v=8wywC_Evx9E
Repo (MIT): https://github.com/IcaroPv01/subflow
Free PT-BR guide: https://raw.githubusercontent.com/IcaroPv01/subflow/main/vendas/isca/guia-legendagem-profissional-pt-br.pdf
```

## 2. Comentário no r/SideProject post (reddit.com/r/SideProject/comments/1vfvdl9)

```
Same spirit — built SubFlow while translating documentaries: a 100% local subtitle
pipeline (Whisper + batch translation + Netflix-style QC + ASR-hallucination checks).
A 104-min film went from ~14h to ~7h50 of work.

90-second video demo: https://www.youtube.com/watch?v=8wywC_Evx9E
Repo (MIT): https://github.com/IcaroPv01/subflow
Checkout (US$ 9.99, optional): https://pay.hotmart.com/E107014071J
```

## 3. Show HN (news.ycombinator.com/submit)

Title: `Show HN: SubFlow — 100% local Whisper subtitle pipeline (transcribe+translate+QC)`

Body:

```
I built a CLI + Claude Code skill that turns any video (URL or file) into clean, translated subtitles — fully offline, no per-minute API cost.

Pipeline: download → transcribe (Whisper, local) → glossary → batch translate → build → clean → QC → langcheck.

90-second demo: https://www.youtube.com/watch?v=8wywC_Evx9E

What's unique:

1. Netflix-style QC is built in: ≤42 chars/line, CPS 17/20, no overlaps, ≥1s duration. The `qc` subcommand generates a report with every violation.

2. `langcheck` re-decodes each cue and compares detected vs expected language. Catches ASR hallucination (a forced-French pass once "invented" French over Hassaniya Arabic song lyrics).

3. Translation stays text-only — batches of 30 cues are plain text files you translate, then the CLI rebuilds the SRT preserving timing. Zero risk of desync.

I use it for documentary translation (PT-BR). A 104-min film that took ~14h manually now takes ~7h50 — same quality.

It's MIT-licensed Python (stdlib only, plus faster-whisper or the standalone binary). Repo: github.com/IcaroPv01/subflow

There's a free 9-section PT-BR guide on professional subtitling: raw.githubusercontent.com/IcaroPv01/subflow/main/vendas/isca/guia-legendagem-profissional-pt-br.pdf

Curious what HN thinks. Feedback on QC defaults, translation batch size, and the langcheck heuristic especially welcome.
```

Comentário próprio no Show HN (após publicar):

```
Author here. The 90-second demo video: https://www.youtube.com/watch?v=8wywC_Evx9E
Free PT-BR guide on the full workflow: https://raw.githubusercontent.com/IcaroPv01/subflow/main/vendas/isca/guia-legendagem-profissional-pt-br.pdf
Support the project / commercial license (US$ 9.99): https://pay.hotmart.com/E107014071J
```

## 4. Dev.to / Hashnode (artigo com embed)

Título: `How I built a 100% local subtitle pipeline with Whisper`
Tags: `whisper, subtitles, cli, opensource`
Artigo completo: `vendas/divulgacao/devto-article.md`
Adicionar no topo (após o intro):

```
<iframe width="560" height="315" src="https://www.youtube.com/embed/8wywC_Evx9E" frameborder="0" allowfullscreen></iframe>

**90-second demo** — the whole pipeline in one command, fully local.
```

Adicionar no final (antes do repo):

```
**Demo video:** https://www.youtube.com/watch?v=8wywC_Evx9E
**Support the project (US$ 9.99):** https://pay.hotmart.com/E107014071J
```

## 5. Reddit posts novos (formato Show HN)

### r/commandline
Title: `SubFlow — 100% local Whisper subtitle pipeline as a single CLI command`

```
I built a CLI that turns any video into clean, translated subtitles — fully local, no API cost.

$ subflow run video.mp4 --src-lang fr --tgt-lang pt
# download → transcribe (Whisper) → glossary → translate → build → clean → QC → langcheck

Netflix-style QC built in (≤42 chars/line, CPS 17/20, no overlaps), plus langcheck which re-decodes each cue to catch ASR hallucination. Translation is text-only keyed by cue number, so timestamps never drift.

90-second demo: https://www.youtube.com/watch?v=8wywC_Evx9E
Repo (MIT): https://github.com/IcaroPv01/subflow
```

### r/opensource
Title: `SubFlow — open-source 100% local subtitle pipeline (Whisper + QC), MIT`

```
I open-sourced the pipeline I use to translate documentaries: download → Whisper transcription → glossary → batch translation → build → clean → Netflix-style QC → langcheck (ASR hallucination detection). Everything runs locally; MIT-licensed Python (stdlib only).

A 104-min film that took ~14h manually now takes ~7h50.

Demo: https://www.youtube.com/watch?v=8wywC_Evx9E
Repo: https://github.com/IcaroPv01/subflow
```

### r/LocalLLaMA
Title: `[P] SubFlow — local Whisper subtitle pipeline with QC and ASR-hallucination checks`

```
I built a Whisper-based pipeline that runs entirely on-device (int8_float16 fits large-v2 in a 4 GB GPU) and adds what Whisper alone lacks for subtitling: Netflix-style QC (≤42 chars/line, CPS 17/20, no overlaps), batch translation that never touches timestamps, and langcheck — which re-decodes each cue and compares detected vs expected language, catching hallucinations (a forced-French pass once "invented" French over Hassaniya Arabic song lyrics).

Benchmarks welcome — curious how it compares on your hardware. Repo (MIT): https://github.com/IcaroPv01/subflow
Demo: https://www.youtube.com/watch?v=8wywC_Evx9E
```

### r/Translation
Title: `Free tool: 100% local subtitling pipeline (Whisper + QC + anti-hallucination)`

```
For translators who subtitle: I built a local pipeline that transcribes with Whisper, lets you translate in controllable batches, and runs Netflix-style QC (≤42 chars/line, CPS 17/20, no overlaps) + langcheck that catches ASR hallucinations in other languages (a real case: Whisper invented French lyrics over an Arabic song).

Free PT-BR guide on the full professional workflow: https://raw.githubusercontent.com/IcaroPv01/subflow/main/vendas/isca/guia-legendagem-profissional-pt-br.pdf
Demo: https://www.youtube.com/watch?v=8wywC_Evx9E
Repo (MIT): https://github.com/IcaroPv01/subflow
```

### r/VideoEditing
Title: `Local subtitle workflow: Whisper + batch translation + Netflix-style QC (demo)`

```
If you subtitle videos for clients, this is the pipeline I use: transcribe locally with Whisper, translate in batches, then a QC pass enforces ≤42 chars/line, CPS 17/20 and no overlaps — plus langcheck catches ASR hallucination (Whisper once "invented" French over an Arabic song).

90-second demo video: https://www.youtube.com/watch?v=8wywC_Evx9E
Repo (MIT): https://github.com/IcaroPv01/subflow
Free guide (PT-BR): https://raw.githubusercontent.com/IcaroPv01/subflow/main/vendas/isca/guia-legendagem-profissional-pt-br.pdf
```

## 6. Discord posts (HF #show-and-tell, LocalLLaMA #tools, IndieHackers #show-and-tell)

```
[Show and tell] SubFlow — 100% local subtitle pipeline (Whisper + QC + anti-hallucination)

I built a local pipeline that turns any video into translated subtitles: download → Whisper transcription (int8_float16 fits a 4 GB GPU) → glossary → batch translation → build → Netflix-style QC (≤42 chars/line, CPS 17/20, no overlaps) → langcheck (re-decodes each cue to catch ASR hallucination — a forced-French pass once invented French over Hassaniya Arabic song lyrics).

90-second demo: https://www.youtube.com/watch?v=8wywC_Evx9E
GIF: https://raw.githubusercontent.com/IcaroPv01/subflow/main/vendas/assets/demo.gif
Repo (MIT): https://github.com/IcaroPv01/subflow
Optional support (US$ 9.99): https://pay.hotmart.com/E107014071J
```

## 7. BetaList

Title: `SubFlow`
URL: `https://github.com/IcaroPv01/subflow`
Description (280 chars):

```
Turn any video into professional translated subtitles, 100% local. Whisper transcription, batch translation, Netflix-style QC and ASR-hallucination checks. One command, no API cost. Demo: youtube.com/watch?v=8wywC_Evx9E
```

## 8. Product Hunt (producthunt.com/posts/new)

Usar `vendas/divulgacao/product-hunt.md` + adicionar:
- URL do vídeo: `https://www.youtube.com/watch?v=8wywC_Evx9E` (no campo "Video URL" se houver, senão no first comment)
- GIF demo: `https://raw.githubusercontent.com/IcaroPv01/subflow/main/vendas/assets/demo.gif`
- Schedule: terça/quarta 08:00 PT

## 9. Diretórios SEO

### AlternativeTo (alternativeto.net) — "Add software"
Name: `SubFlow` · URL: repo GitHub · Type: Video subtitling / CLI tool
Description: `100% local subtitle pipeline: Whisper transcription, batch translation, Netflix-style QC and ASR-hallucination checks. Demo: youtube.com/watch?v=8wywC_Evx9E`

### OpenTools (opentools.ai) — "Submit tool"
Name: `SubFlow` · URL: repo · Category: AI / Video
Description: `Local-first subtitling: transcribe, translate, QC and language-check any video. Demo: youtube.com/watch?v=8wywC_Evx9E`

### OpenAlternative (openalternative.co) — "Submit"
Name: `SubFlow` · URL: repo · Alternative to: Descript / Subtitle Edit
Description: `Fully local Whisper subtitle pipeline with Netflix-style QC and anti-hallucination checks. Demo: youtube.com/watch?v=8wywC_Evx9E`

### TAAIFT (taaift.com) — submit
Name: `SubFlow` · URL: repo
Description: `100% local AI subtitling: transcribe + translate + QC + langcheck in one command. Demo: youtube.com/watch?v=8wywC_Evx9E`

## 10. Discussion #1 do repo (feito via gh CLI)
- [x] Comentário com link do vídeo (discussioncomment-17955926)
- [x] Comentário com PDF gratuito (discussioncomment-17954844)
- [ ] Embed do vídeo no corpo da discussion (requer edição do corpo — fazer via gh quando possível)