# DevHunt — cadastro do SubFlow (preparado)

> Para colar quando o dono logar no DevHunt (via GitHub).
> URL: https://devhunt.org — "Submit your Dev Tool" (requer login; aceita GitHub).

## Como cadastrar
1. Acessar https://devhunt.org → **Sign In** → **GitHub** (conta IcaroPv01)
2. Clicar **"Submit your Dev Tool"**
3. Colar os dados abaixo (formulário similar ao Product Hunt: name, tagline, description, links, media)

## Dados do produto

- **Name:** SubFlow
- **Tagline (<=60 chars):** 100% local Whisper subtitle pipeline with Netflix-style QC
- **URL:** https://github.com/IcaroPv01/subflow

## Descrição (EN, formato Product Hunt)

```
SubFlow turns any video (URL or file) into professional translated subtitles, fully offline — no per-minute API cost.

Pipeline: download → transcribe with Whisper (int8_float16 fits 4GB GPUs) → glossary → batch translate → build SRT → clean → Netflix-style QC → langcheck.

Why it's unique:
1. Netflix-style QC built in: ≤42 chars/line, CPS 17/20, no overlaps, ≥1s duration, with a violations report.
2. langcheck re-decodes each cue and compares detected vs expected language — catches ASR hallucination (a forced-French pass once "invented" French over Hassaniya Arabic song lyrics).
3. Translation is text-only keyed by cue number — timestamps never drift.

Real case: a 104-min documentary (Med Hondo, 1977) subtitled in ~7h50, half the manual time.

MIT-licensed Python (stdlib only). Works on Windows/macOS/Linux.
```

## Links
- **Demo video:** https://www.youtube.com/watch?v=8wywC_Evx9E
- **Repo:** https://github.com/IcaroPv01/subflow
- **Sales page (PT-BR):** https://icarovenzon352.hotmart.host/subflow-legendas-profissionais-de-qualquer-video-100-local-f419da64-0079-4a97-9c03-33f796bb241c
- **Checkout:** https://pay.hotmart.com/E107014071J (coupon **SUBFLOW15** = 15% off)

## Tags / Topics
`whisper` `subtitles` `transcription` `cli` `opensource` `video` `developer-tools` `local-first`

## Media (para upload)
- **Screenshot 1:** `vendas/assets/terminal.png`
- **Screenshot 2:** `vendas/assets/qc_depois.png`
- **GIF:** `vendas/assets/demo.gif`
- **Video:** https://www.youtube.com/watch?v=8wywC_Evx9E

## First comment (após publicar)
```
Author here. The 90-second demo: https://www.youtube.com/watch?v=8wywC_Evx9E
Free PT-BR guide: https://raw.githubusercontent.com/IcaroPv01/subflow/main/vendas/isca/guia-legendagem-profissional-pt-br.pdf
Support / commercial license (US$ 9.99, coupon SUBFLOW15 = 15% off): https://pay.hotmart.com/E107014071J
```
