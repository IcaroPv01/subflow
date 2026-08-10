# Comparativo: SubFlow vs alternativas (2026)

| Recurso | **SubFlow** | Subtitle Edit | Aegisub | Descript | Whisper CLI puro | OpenAI Whisper API |
|---|---|---|---|---|---|---|
| **Custo por vídeo** | R$ 0 (local) | R$ 0 (local) | R$ 0 (local) | US$ 24/mês (Pro) | R$ 0 (local) | US$ 0,006/min (~$1/filme) |
| **Privacidade** | ✅ 100% local | ✅ local | ✅ local | ❌ upload | ✅ local | ❌ upload |
| **Transcrição automática** | ✅ Whisper | ❌ manual | ❌ manual | ✅ | ✅ Whisper | ✅ Whisper |
| **Tradução automática** | ✅ em batches (você revisa) | ❌ | ❌ | ✅ | ❌ | ❌ |
| **QC automático** | ✅ estilo Netflix | ⚠️ parcial | ✅ manual | ⚠️ parcial | ❌ | ❌ |
| **Detecção de alucinação ASR** | ✅ `langcheck` | ❌ | ❌ | ❌ | ❌ | ❌ |
| **CPS / chars por linha / overlap** | ✅ automático | ⚠️ parcial | ⚠️ manual | ❌ | ❌ | ❌ |
| **Qualquer par de idiomas** | ✅ (100+) | ✅ | ✅ | ⚠️ 23 idiomas | ✅ | ✅ |
| **Funciona offline** | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ |
| **Tradução preserva timing** | ✅ (text-only) | n/a | n/a | ⚠️ sim | n/a | n/a |
| **Pipeline reproduzível** | ✅ 1 comando | ❌ | ❌ | ❌ | ❌ | ❌ |
| **CLI + scriptável** | ✅ | ❌ | ❌ | ❌ | ⚠️ parcial | ⚠️ API |
| **Integração com agente IA** | ✅ SKILL.md | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Licença comercial para revend** | ✅ R$ 49,90 | ✅ grátis | ✅ grátis | ⚠️ limitado | ✅ | ⚠️ ToS |
| **Tamanho do instalador** | ~10 MB | ~50 MB | ~30 MB | n/a (SaaS) | ~5 MB | n/a |
| **Suporte GPU** | ✅ int8_float16 | n/a | n/a | ✅ | ✅ | n/a (cloud) |
| **Curva de aprendizado** | 5 min (1 comando) | 30 min | 1-2h | 10 min | 20 min | 5 min |
| **Manutenção ativa (2026)** | ✅ | ⚠️ lenta | ⚠️ lenta | ✅ | ✅ | ✅ |

## Quando **NÃO** usar o SubFlow

- Você só precisa de **legendas para 1 vídeo curto** (use Whisper CLI puro, é mais simples)
- Você **não tem GPU nem CPU potente** (modelos large ficam lentos; prefira API)
- Você quer **tradução 100% automática** sem revisão (SubFlow é projetado para revisão humana)

## Quando **usar** o SubFlow

- Você **traduz vídeos profissionalmente** (legendas, dublagem, conteúdo bilíngue)
- Você quer **privacidade total** (clientes confidenciais, jurídicos, médicos)
- Você faz **volume** (5+ vídeos por semana) e o custo de API pesa
- Você precisa de **QC profissional** (Netflix, Disney+, Globoplay)
- Você trabalha com **idiomas difíceis** (árabe, mandarim, japonês, russo) onde ASR alucina

## Resumo em uma frase

> SubFlow é o **único pipeline open-source que une Whisper local + QC estilo Netflix + detecção de alucinação + tradução em batches**, automatizando 95% do trabalho braçal de legendagem profissional.

---

## 🛒 Comprar SubFlow

- **Checkout:** https://pay.hotmart.com/E107014071J — R$ 55,86 (~US$ 9,99)
- **Cupom:** `SUBFLOW15` = **15% off**
- **Página do produto (PT-BR):** https://icarovenzon352.hotmart.host/subflow-legendas-profissionais-de-qualquer-video-100-local-f419da64-0079-4a97-9c03-33f796bb241c
- **Demo (90s):** https://www.youtube.com/watch?v=8wywC_Evx9E
- Garantia incondicional de **7 dias**.
