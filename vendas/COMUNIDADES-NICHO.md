# Comunidades de nicho — legendas/Whisper (10 canais)

> Para divulgar o SubFlow em comunidades de legendagem/Whisper/transcrição.
> Use o TEXTO PADRÃO no final. Atualizado: 2026-08-10.

## Comunidades

| # | Comunidade | URL | Tipo | Como postar | Público |
|---|---|---|---|---|---|
| 1 | **r/selfhosted** | https://www.reddit.com/r/selfhosted/ | Subreddit (~500k) | Post showcase "100% local, no cloud" | Devs selfhosted — público exato |
| 2 | **r/LocalLLaMA** | https://www.reddit.com/r/LocalLLaMA/ | Subreddit (~300k) | Post técnico [P] com benchmarks | Devs IA local — público exato |
| 3 | **r/TranslationStudies** | https://www.reddit.com/r/TranslationStudies/ | Subreddit (~30k) | Post sobre QC estilo Netflix + langcheck | Tradutores profissionais |
| 4 | **r/VideoEditing** | https://www.reddit.com/r/VideoEditing/ | Subreddit (~1.9M) | Workflow de legendagem local | Editores de vídeo |
| 5 | **r/commandline** | https://www.reddit.com/r/commandline/ | Subreddit (~100k) | "CLI tool: 1 comando → SRT" | Entusiastas CLI |
| 6 | **OpenAI Dev Community (Whisper)** | https://community.openai.com/c/api/whisper | Fórum | Responder tópicos de alucinação/desync com link | Devs Whisper — público exato |
| 7 | **VideoHelp Forum** | https://forum.videohelp.com | Fórum | Tópico "100% local subtitle pipeline" na seção Subtitle | Tradutores/legenders |
| 8 | **Hugging Face Discuss** | https://discuss.huggingface.co | Fórum | Tutorial "local Whisper + QC" na categoria Show & Tell | Devs ML |
| 9 | **SubtitleEdit Forum** | https://www.nikse.dk/SubtitleEdit/Help | Fórum/GitHub | Issue/discussion "external QC integration" | Usuários de legendagem |
| 10 | **Lobsters** | https://lobste.rs | Agregação dev (curated) | Post "Show HN"-style (requer convite) | Devs seniores |

## Texto padrão curto (para colar)

```
[Show and tell] SubFlow — 100% local Whisper subtitle pipeline (transcribe + translate + Netflix-style QC + ASR-hallucination checks)

I built a CLI + Claude Code skill that turns any video into professional translated subtitles, fully offline — no API cost, no cloud.

Pipeline: download → Whisper transcription (int8_float16 fits 4GB GPUs) → glossary → batch translation → build SRT → clean → Netflix-style QC (≤42 chars/line, CPS 17/20, no overlaps) → langcheck (catches ASR hallucination — e.g. Whisper inventing French over Hassaniya Arabic lyrics).

Real case: a 104-min documentary that took ~14h manually now takes ~7h50.

Repo (MIT): https://github.com/IcaroPv01/subflow
90s demo: https://www.youtube.com/watch?v=8wywC_Evx9E
Sales page (PT-BR): https://icarovenzon352.hotmart.host/subflow-legendas-profissionais-de-qualquer-video-100-local-f419da64-0079-4a97-9c03-33f796bb241c
Checkout: https://pay.hotmart.com/E107014071J (coupon SUBFLOW15 = 15% off)
```

## Regras por comunidade

- **r/selfhosted**: formato showcase, SEM link de venda direto no post (link nos comentários)
- **r/LocalLLaMA**: post [P] com detalhe técnico (int8_float16, VAD, langcheck)
- **r/MachineLearning**: regras rígidas de autopromoção — link só do repo MIT
- **r/TranslationStudies**: foco em QC profissional, não em venda
- **OpenAI Dev Community**: responder tópicos existentes (não criar spam) — melhor resultado
- **VideoHelp**: postar como solução/ferramenta, responder dúvidas de Whisper

## Status

| # | Comunidade | Status |
|---|---|---|
| 1–5 | Subreddits | ⛔ Requer login Reddit (conta técnica) — textos prontos |
| 6 | OpenAI Dev Community | 🔍 Testar (requer login OpenAI) |
| 7 | VideoHelp | 🔍 Testar (requer cadastro) |
| 8 | HF Discuss | 🔍 Testar (requer login HF) |
| 9 | SubtitleEdit | 🔍 Testar |
| 10 | Lobsters | ⛔ Requer convite |
