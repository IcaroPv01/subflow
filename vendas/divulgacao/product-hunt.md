# Product Hunt — SubFlow submission

> Criado pela instância de execução (não existia no repo). Base: show-hn.txt + README-en.md.
> **Ação:** agendar para terça/quarta 08:00 PT (perfil de lançamento).

## Título
SubFlow — 100% local Whisper subtitle pipeline (transcribe + translate + QC)

## Tagline (<=60 chars)
Local Whisper subtitles: transcribe+translate+QC, no API cost

## URL
https://github.com/IcaroPv01/subflow

## Descrição (o que é)
SubFlow is an MIT-licensed CLI + Claude Code skill that turns any video (URL or file) into clean, translated subtitles — fully offline, no per-minute API cost. Pipeline: download → transcribe (Whisper, local) → glossary → batch translate → build → clean → QC → langcheck.

## Destaques (3 bullets)
1. **Netflix-style QC built in** — ≤42 chars/line, CPS 17/20, no overlaps, ≥1s duration; the `qc` subcommand writes a report with every violation.
2. **langcheck catches ASR hallucination** — re-decodes each cue and compares detected vs expected language (a forced-French pass once "invented" French over Hassaniya Arabic song lyrics).
3. **Translation stays text-only** — batches of plain text files, then the CLI rebuilds the SRT preserving timing. Zero risk of desync.

## Caso de uso real
Documentary translation (PT-BR): a 104-min film that took ~14 h manually now takes ~7 h 50 — same quality.

## First comment (checkout + guia)
Free 9-section PT-BR guide on professional subtitling: raw.githubusercontent.com/IcaroPv01/subflow/main/vendas/isca/guia-legendagem-profissional-pt-br.pdf
Support the project / commercial license (US$ 9,99): https://pay.hotmart.com/E107014071J

## Tópicos
#developer-tools #ai #opensource #video #subtitles #whisper

## Imagens
- Terminal: vendas/assets/terminal.png
- QC antes/depois: vendas/assets/qc_antes.png + qc_depois.png
- langcheck: vendas/assets/langcheck.png
- Demo GIF: vendas/assets/demo.gif