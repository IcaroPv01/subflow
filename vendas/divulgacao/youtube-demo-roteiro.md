# Roteiro YouTube (60-90s demo) — SubFlow

**Título:** "Subtitle a whole film in 8 hours (Whisper, local, free)"
**Thumbnail:** terminal screenshot + "100% local" + "PT-BR friendly"

## Cena 1 (0-10s) — Hook
Corte seco: terminal em tela cheia. Texto overlay grande:

> "Legendando 30 minutos de vídeo em 90 minutos."
> "Sem custo de API. Sem upload."

## Cena 2 (10-25s) — Comando único
Terminal rodando:
```bash
subflow init --name demo-film
subflow run "https://youtu.be/..." --src-lang fr --tgt-lang pt
```
Overlay: "1 comando. 8 minutos depois: SRT pronto."

## Cena 3 (25-40s) — Antes/depois do QC
Split screen:
- Esquerda: SRT bruto do Whisper (com erros visíveis, CPS alto, overlaps)
- Direita: SRT pós `subflow clean + qc` (limpo, ≤42 chars, 0 erros)
Overlay: "QC estilo Netflix. Automático."

## Cena 4 (40-55s) — langcheck
Terminal:
```bash
subflow langcheck audio/audio.wav --srt transcription/audio.srt --expected fr
```
Output: "ASR hallucination detected at cue 142 (expected: fr, got: en)"
Overlay: "Detecta alucinação do Whisper."

## Cena 5 (55-70s) — Caso real
Foto do filme *Soleil Ô* (Med Hondo, 1977).
Overlay: "Filme de 104 min legendado em 7h50."
Texto: "De 14h para 7h50. Metade do tempo."

## Cena 6 (70-80s) — CTA
Texto grande: "Grátis: PDF com o pipeline completo"
Botão → link do PDF no GitHub raw

## Cena 7 (80-90s) — End screen
Logo SubFlow + "github.com/IcaroPv01/subflow" + setas para vídeo relacionado.

---

## Thumbnail (texto + visual)
- Fundo: terminal preto com output do SubFlow
- Texto branco grande: "Subtitle a FILM in 8 hours"
- Texto amarelo: "100% local · Whisper"
- Logo SubFlow pequeno no canto
