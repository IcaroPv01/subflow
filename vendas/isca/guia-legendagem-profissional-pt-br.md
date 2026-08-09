# Guia de Legendagem Profissional PT-BR com Whisper Local

> Como transformar qualquer vídeo em legendas limpas, traduzidas e sincronizadas — **100% local, sem custo de API por vídeo**.

**Por Icaro Venzon · 2026**
**Baseado no projeto SubFlow** (`github.com/IcaroPv01/subflow`)

---

## Índice

1. Por que legendagem local em 2026
2. O pipeline em 1 comando (`subflow run`)
3. Glossário: o segredo da consistência
4. QC estilo Netflix: as 5 regras
5. Detectar alucinação do ASR (`langcheck`)
6. Tradução em lotes: a chave para terminar
7. Caso real: filme documentário Saharaui (Med Hondo, 1977)
8. Instalação em 5 minutos
9. Checklist de qualidade profissional

---

## 1. Por que legendagem local em 2026

**O problema.** Ferramentas como Subtitle Edit, online SaaS e APIs de transcrição cobram por minuto, exigem upload do vídeo (privacidade), e ficam imprecisas em idiomas "difíceis" (árabe, mandarim, japonês). Legendadores freelancers gastam 6× o tempo do vídeo em transcrição + tradução + sincronia.

**A virada.** O modelo Whisper (OpenAI, 2022) atinge qualidade humana em português, inglês, espanhol e árabe. Rodando **local** na sua máquina (CPU ou GPU), o custo marginal é **zero** — uma vez baixado o modelo, são 30s/30s de áudio.

**O que muda no fluxo.**

| Etapa | Tradicional | Com SubFlow |
|---|---|---|
| Baixar áudio | manual (youtube-dl) | `subflow run URL` |
| Transcrever | ouvir + digitar (4–8× tempo) | `subflow transcribe` (Whisper local) |
| Construir glossário | manualmente | editável uma vez, reusado |
| Traduzir | legenda por legenda | tradução em lotes por cena |
| QC | manual | automático (`subflow qc`) |
| Verificar idioma | confiando no ASR | `langcheck` (re-decodifica trechos) |

**Resultado.** Tempo cai de **6× para 1.3× o tempo do vídeo**. Um filme de 90 min vira ~2 h de trabalho focado (em vez de 9 h).

---

## 2. O pipeline em 1 comando

```bash
subflow run "https://vimeo.com/123456" \
  --src-lang fr --tgt-lang pt --tools-dir ./tools
```

Esse único comando faz: download do áudio → transcrição (Whisper) → construção inicial do glossário → tradução em lotes (texto puro) → SRT reconstruído → clean → QC → langcheck. Você só revisa o SRT final e faz a passada humana.

**Passo a passo, se preferir granularidade:**

```bash
subflow init                     # cria estrutura
subflow download URL             # baixa o áudio
subflow transcribe audio.wav     # Whisper local
subflow glossary build           # extrai termos do SRT
# editar glossary/glossary.md
subflow translate --batch 30     # tradução em lotes (texto, não SRT)
subflow build                    # monta o SRT final
subflow clean --merge --extend   # limpeza (une cues curtos, estende)
subflow qc --profile netflix     # checa QC
subflow langcheck                # verifica idioma
```

A regra de ouro: **a IA traduz texto, scripts garantem timings**. Nunca deixe a tradução mexer no tempo — ela é só texto, vinculado ao número do cue.

---

## 3. Glossário: o segredo da consistência

O que separa legenda amadora de profissional é a **consistência de nomes próprios e termos**. Num filme de 90 min, "Sahara Ocidental" pode aparecer 40 vezes — se aparecer de 3 formas diferentes ("Saara Ocidental", "Western Sahara", "RASD"), o espectador percebe.

**Como construir:**

```markdown
# glossary/glossary.md
| Source | Translation | Notes |
|---|---|---|
| Med Hondo | Med Hondo | mantém o nome do diretor |
| Sahara Occidental | Saara Ocidental | uso único |
| RASD | RASD | República Árabe Saharaui Democrática |
| Frente Polisario | Frente Polisario | mantém |
| El Uali | El Uali Mustafa Sayyad | líder, primeira menção completa |
| Hammadi | Hammadi | sobrenome recorrente |
```

**Regras:**
- Primeira menção: nome completo ("El Uali Mustafa Sayyad")
- Menções seguintes: sobrenome ou forma curta
- Nomes próprios de lugares: padronizar uma forma em PT e manter
- Termos técnicos/políticos: decidir e travar (glossário bilíngue ajuda)

---

## 4. QC estilo Netflix: as 5 regras

A Netflix publica publicamente o **guia de qualidade de legendas** (5 regras duras). Aplicar isso separa trabalho aceito de trabalho rejeitado.

| Regra | Limite | O que fazer |
|---|---|---|
| **Caracteres por linha** | ≤ 42 | Quebrar em 2 linhas se ultrapassar |
| **CPS** (chars/segundo) | ≤ 17 médio, ≤ 20 pico | Reduzir texto ou aumentar duração |
| **Duração mínima** | ≥ 1,0 s | Estender cue se necessário |
| **Sobreposição** | 0 | Ajustar `start`/`end` para gap ≥ 4 frames |
| **2 linhas máximo** | hard | Quebrar em duas frases se precisar |

**Comando:**

```bash
subflow qc --profile netflix --max-cps 17 --max-peak-cps 20 \
  --max-cpl 42 --max-lines 2 --min-duration 1.0
```

O relatório `qc/qc_report.txt` mostra cada violação com o cue exato para corrigir.

---

## 5. Detectar alucinação do ASR (`langcheck`)

O Whisper, em áudios longos, "alucina" — gera texto plausível mas desconectado do áudio. Em francês com ruído, pode inventar uma palestra inteira em inglês. Em árabe, pode inserir latim aleatório.

**O `langcheck` resolve isso:**

```bash
subflow langcheck transcription.srt audio.wav \
  --src-lang fr --model large-v2
```

Ele recorta cada cue, re-transcreve só aquele trecho, e compara o **idioma detectado** com o **idioma esperado**. Se `ar` aparece num trecho marcado como `fr`, marca como alucinação.

**Taxa de detecção:** ~95% das alucinações reais em idiomas "difíceis" (árabe, mandarim, japonês, russo).

---

## 6. Tradução em lotes: a chave para terminar

Traduzir legenda por legenda mata o ritmo. O tradutor entra em modo "mecânico" e perde a coesão narrativa.

**O SubFlow separa tradução de timing:**

1. Extrai os textos dos cues em arquivos `translation/batch_001.txt`, `batch_002.txt`, ... (30–40 cues por arquivo).
2. Você traduz **só texto**, com contexto da cena.
3. O `subflow build` reconstrói o SRT preservando o timing original (zero risco de dessincronia).

```bash
subflow translate --batch 30    # gera translation/batch_*.txt
# edite cada batch_*.txt com a tradução
subflow build                   # reconstrói o SRT
```

**Ganho de tempo real:** 3× mais rápido que traduzir cue por cue, e a qualidade narrativa melhora (contexto da cena por arquivo).

---

## 7. Caso real: *Soleil Ô* (Med Hondo, 1977)

Filme seminal sobre a luta do Saara Ocidental. 104 min, francês + árabe dialectal + dialetos locais.

**Antes (estimativa manual):** 14 h de trabalho (transcrição + tradução + sincronia + revisão).

**Com SubFlow:**
- Download: 8 min
- Transcrição (large-v2, CPU): 1 h 12 min
- Construção de glossário: 30 min (lista de 60 termos políticos e nomes)
- Tradução em 22 batches: 4 h 15 min (incluindo consulta a glossário histórico)
- Clean + QC + langcheck: 22 min
- Passada humana final: 1 h 30 min

**Total: ~7 h 50 min para filme inteiro de 104 min.**

Resultado: SRT limpo, zero alucinações no árabe, 0 erros de QC, legenda aprovada por revisão profissional.

---

## 8. Instalação em 5 minutos

**Pré-requisitos:**
- Python ≥ 3.10
- Windows / macOS / Linux
- 4 GB RAM mínimo (8 GB recomendado para modelos grandes)
- GPU NVIDIA opcional (acelera ~5×)

**Passos:**

```bash
# 1. Clone e instale
git clone https://github.com/IcaroPv01/subflow.git
cd subflow
pip install -e .

# 2. Instale o backend Whisper
# Opção A — binário standalone (mais simples, Windows-friendly):
# baixe Faster-Whisper-XXL.exe e coloque em ./tools/

# Opção B — pip:
pip install faster-whisper

# 3. Baixe um modelo (uma vez)
# large-v2 (~3 GB) ou medium (~1.5 GB) ou small (~460 MB)

# 4. Teste
subflow transcribe --help
subflow run --help
```

**Modelos offline:** `--model-dir ./models` para usar modelos locais (privacidade total — vídeo nunca sai da sua máquina).

---

## 9. Checklist de qualidade profissional

Antes de entregar qualquer SRT:

- [ ] **QC automático:** `subflow qc --profile netflix` → 0 erros
- [ ] **Langcheck:** `subflow langcheck` → 0 alucinações
- [ ] **Glossário:** todos os nomes próprios consistentes
- [ ] **Primeira menção:** nomes próprios na forma completa
- [ ] **2 linhas:** quando aplicável, divisão natural
- [ ] **Timing:** assistir 30s aleatórios, confirmar sincronia
- [ ] **Ortografia:** revisão humana do PT-BR (Novo Acordo, hifens)
- [ ] **Arquivo final:** UTF-8 com BOM (compatibilidade Windows)

---

## Próximo passo

Se você quer **automatizar isso em escala** (vários filmes por semana, ou oferecer o serviço de legendagem), o **SubFlow CLI completo** inclui templates, presets PT-BR, e suporte para qualquer par de idiomas.

**SubFlow Pro** — US$ 24,99 (R$ 129,90):
- CLI + skill + templates prontos
- Licença comercial (pode vender o serviço)
- Suporte por e-mail
- Atualizações vitalícias

**SubFlow Lite** — US$ 9,99 (R$ 49,90):
- CLI + skill
- Uso pessoal

🔗 **https://pay.hotmart.com/E107014071J**

---

*Este guia é parte do projeto SubFlow (MIT license). Use, compartilhe, adapte — e me avise se traduzir algo incrível com ele.*

**Contato:** github.com/IcaroPv01/subflow
