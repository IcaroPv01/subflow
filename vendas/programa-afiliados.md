# Programa de Afiliados — SubFlow (Hotmart)

> Configurar no Hotmart: Programa de Afiliados → ativar → definir comissão.

## Configuração inicial

- **Comissão:** 30% (US$ 2,99 por venda do Lite a US$ 9,99 / US$ 7,49 por venda do Pro a US$ 24,99)
- **Cookie:** 60 dias
- **Material disponível:** banner 1280x640 (vendas/assets/banner.png), GIF demo (vendas/assets/demo.gif), screenshots, copy de e-mail, posts para redes sociais
- **Página do afiliado:** vendas/landing/index.html + vendas/landing/guia-gratuito.html (para captura)

## Copy para o afiliado usar (e-mail)

**Assunto:** Conheça o SubFlow — pipeline de legendagem 100% local

**Corpo:**

Oi, [nome],

Se você trabalha com tradução de vídeos, áudio ou legendagem, esse produto vai te interessar:

**SubFlow** — CLI + skill open-source que automatiza 95% do trabalho braçal de legendagem profissional.

Por que recomendo:
- **100% local** (privacidade total — vídeo nunca sai da máquina)
- **QC estilo Netflix automático** (≤42 chars/linha, CPS 17/20, sem overlaps)
- **Detecção de alucinação** do Whisper (pega o que outros passam batido)
- **Tradução em batches** (3× mais rápido)
- **MIT licensed** (use, adapte, contribua)

Caso real: filme documentário de 104 min legendado em 7h50 (mesma qualidade que 14h manual).

Está por **R$ 49,90** (comercial) ou **R$ 129,90** (Pro com templates PT-BR + atualizações vitalícias).

🔗 [Ver oferta](https://pay.hotmart.com/E107014071J)

[Seu nome de afiliado]

---

## Copy para post de redes sociais do afiliado

**Twitter/X:**
Acabei de testar o SubFlow pra legendagem local. 100% open-source, MIT, Whisper local, QC estilo Netflix e detecção de alucinação do ASR. Documentário de 104 min em 7h50. Vale cada centavo. [link]

**LinkedIn:**
Publiquei uma análise do SubFlow, o novo pipeline open-source de legendagem profissional. O diferencial: privacidade total + QC automático + tradução em batches. Para quem trabalha com legendagem, vale conhecer. [link]

## Material visual para o afiliado

Todos em `vendas/assets/`:
- `banner.png` — banner oficial 1280x640 (usar no topo da página)
- `demo.gif` — GIF 116KB mostrando o terminal rodando
- `terminal.png` — print do pipeline completo
- `qc_antes.png` + `qc_depois.png` — antes/depois do QC
- `langcheck.png` — detecção de alucinação
- `glossary.png` — glossário PT-BR

## Banners pré-prontos (códigos HTML)

```html
<!-- Banner 728x90 -->
<a href="https://pay.hotmart.com/E107014071J?aff=SEU_ID">
  <img src="https://raw.githubusercontent.com/IcaroPv01/subflow/main/vendas/assets/banner.png" 
       width="728" alt="SubFlow — pipeline de legendagem local">
</a>
```

```html
<!-- Botão texto -->
<a href="https://pay.hotmart.com/E107014071J?aff=SEU_ID" 
   style="display:inline-block; padding:12px 24px; background:#1a237e; color:#fff; 
          text-decoration:none; border-radius:6px; font-weight:600;">
  SubFlow — pipeline 100% local
</a>
```

## Estratégia de comissão

| Cenário | Comissão atual | Recomendado |
|---|---|---|
| Venda direta (sem afiliado) | 100% | — |
| Venda via afiliado | 30% | 30-40% (atrativo) |
| Venda via afiliado Pro | 30% | 40-50% (ticket maior) |
| Venda recorrente (assinatura) | 30% recorrente | **50% recorrente** (alto LTV) |

## Ranking de canais de afiliado (sugestão)

1. **Canais de tradução/legendagem no YouTube** (alto CPM, audiência segmentada)
2. **Comunidades PT-BR** (r/brasil, grupos Facebook de tradutores, Discord)
3. **Newsletters de IA/tools** (The Batch, TLDR AI, Ben's Bites)
4. **LinkedIn** (post + artigo longo)
5. **Twitter/X** (thread de 5-7 tweets)
6. **Blogs de nicho** (legendagem, tradução, dublagem)
