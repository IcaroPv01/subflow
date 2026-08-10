# HOTMART NO AR — SubFlow

> Resumo executivo do estado do Hotmart (2026-08-10). Tudo verificado.

## Links
| Item | URL |
|---|---|
| **Página customizada** | https://icarovenzon352.hotmart.host/subflow-legendas-profissionais-de-qualquer-video-100-local-f419da64-0079-4a97-9c03-33f796bb241c |
| **Checkout** | https://pay.hotmart.com/E107014071J |
| **Cupom** | `SUBFLOW15` (15% off) |
| **Preço** | R$ 55,86 (~US$ 9,99) |
| **Webhook** | https://stuck-beats-interstate-vacuum.trycloudflare.com/hotmart/webhook |
| **Loop de monitoramento** | `vendas/webhook/monitor_loop.sh` (PID 6782, 24h, 30min/check) |
| **Vendas reais** | 0 (monitorando) |

## O que está no ar (verificado)
1. **Página customizada publicada** — Hero + vídeo YouTube + 6 benefícios + pipeline + comparativo (vs Subtitle Edit/Descript/Whisper API) + garantia 7 dias + FAQ + CTA.
2. **Checkout configurado** — Dados: nome/email/celular; Pagamento: Pix, Cartão, PayPal, Mercado Pago; cupom ativo; híbrido; parcelado em destaque.
3. **Cupom SUBFLOW15** — 15% de desconto, todas as ofertas.
4. **Vídeo demo YouTube** — https://www.youtube.com/watch?v=8wywC_Evx9E (90s, público).
5. **Webhook testado** — venda simulada registrada (US$ 9,99) via túnel cloudflared; server Flask ativo na porta 5050.
6. **Trajetos de tráfego** — README, Discussion #1, PR #26 (awesome-whisper) com links de checkout.

## Pendências (ação manual do dono)
- Logar em club.hotmart.com → welcome sequence (3 e-mails prontos)
- Chrome real → app.hotmart.com/webhooks → URL do túnel
- Reddit (conta técnica) → re-posts + posts novos
- Show HN / Dev.to / Hashnode / BetaList / PH / HF Space / Discord

## Estrutura de arquivos
```
vendas/
├── HOTMART-NO-AR.md          (este arquivo)
├── CHECKLIST-DONO-FOCO-HOTMART.md
├── CHECKLIST-DONO.md
├── listing-pack.md           (milestones completos)
├── welcome-sequence.md       (3 e-mails)
├── textos-prontos.md         (posts/comentários)
├── como-subir-pagina-hotmart.md
├── hotmart-page-v2.html      (HTML da página — backup)
├── comparativo.md
├── isca/guia-legendagem-profissional-pt-br.md
└── webhook/                  (server + túnel + monitor loop)
```
---

## Estado atual (2026-08-10, rodada de tráfego)

### Canais com link do checkout (ativos)
- ✅ **README** (repo) — checkout + cupom + página customizada
- ✅ **Discussion #1** (GitHub) — checkout + cupom + página + vídeo + PDF
- ✅ **PR #26** (Awesome-Whisper-Apps) — checkout + cupom + demo
- ✅ **Vídeo YouTube** (descrição) — repo + PDF + checkout
- ✅ **Guia PDF** (fim do guia) — checkout + cupom SUBFLOW15
- ✅ **comparativo.md** — seção "Comprar SubFlow" (checkout + cupom + demo)

### Canais pendentes (ação do dono — login)
- ⏸️ Show HN — rate limit do HN ativo (retry falhou: "Sorry.")
- ⏸️ Dev.to / Hashnode / BetaList / PH / HF Space — sem conta técnica logada
- ⏸️ Reddit — posts r/whisper e r/SideProject removidos pelos filtros; sem sessão
- ⏸️ Discord — sem login

### Canais extras (pesquisa — `vendas/canais-extras.md`)
- 🔍 18 diretórios AI (Toolify, AI Tool Directory, TopAI, Peerlist, AiToolHunt, DevHunt...)
- 🔍 6 comunidades Whisper/legendas (OpenAI Dev Community, VideoHelp, Cursor Forum...)
- Todos com texto padrão de submissão pronto (EN) no arquivo.

### Vendas
- **0 reais** (webhook status confirmado: 2 vendas simuladas de teste, sales_total=9.99)

---

## Canais: publicados vs pendentes (2026-08-10 ~02:00)

### ✅ Publicados / no ar
1. **YouTube demo** — https://www.youtube.com/watch?v=8wywC_Evx9E
2. **Página customizada** — icarovenzon352.hotmart.host/subflow-legendas...
3. **Checkout** — pay.hotmart.com/E107014071J (Pix, Cartão, PayPal, Mercado Pago, cupom SUBFLOW15)
4. **AI Tool Directory** — submetido (aguardando review)
5. **awesome-video PR #114** — aberto (Subtitle & Caption Tools)
6. **awesome-ai-tools PR #1945** — aberto (Developer tools)
7. **GitHub Discussion #1** — links checkout/cupom/página
8. **PR #26 (Awesome-Whisper-Apps)** — comentário com checkout
9. **README** — links checkout/cupom/página

### ⛔ Bloqueados (aguardando login do dono)
- Show HN (IP penalizado), Reddit (sem sessão), Dev.to, Hashnode, BetaList, Product Hunt, HF Space, Discord, IndieHackers (Cloudflare)
- Webhook oficial Hotmart (SPA não renderiza no Orca — Chrome real)
- Welcome sequence Club (login separado)

### ⛔ Bloqueados por restrição/inexistência
- awesome-whisper (contribuidores anteriores), awesome-claude-code (permissão), awesome-selfhosted (~200 stars), awesome-chatgpt (não encaixa), 7 repos inexistentes
- Diretórios: 17 da lista v1 bloqueados (login/pago/404) + 7 da v2 (pago/invite/404)

---

## PRs abertos (atualizado 2026-08-10 ~02:45)

| PR | Repo | Status |
|---|---|---|
| [PR #26](https://github.com/danielrosehill/Awesome-Whisper-Apps/pull/26) | Awesome-Whisper-Apps | Aberto (comentario com checkout) |
| [PR #114](https://github.com/krzemienski/awesome-video/pull/114) | awesome-video | Aberto (Subtitle & Caption Tools) |
| [PR #1945](https://github.com/mahseema/awesome-ai-tools/pull/1945) | awesome-ai-tools | Aberto (Developer tools) |
| AI Tool Directory | — | Submetido (aguardando review) |

## Cadastros GitHub (tarefa 2)
- ⛔ **Peerlist**: so Google OAuth (nao GitHub) — pular
- ⛔ **DevHunt**: precisa GitHub logado no browser (OAuth redirecionou para login) — para quando dono logar
- ⛔ **LaunchBoosts / Hashnode / HF**: idem GitHub — para quando dono logar
- ✅ **Cadastros prontos para colar**: peerlist-cadastro.md, devhunt-cadastro.md (quando logar)

---

## ESTADO FINAL (2026-08-10 ~03:30)

### ✅ Publicados / no ar
1. **Hotmart checkout** — pay.hotmart.com/E107014071J (Pix, Cartão, PayPal, Mercado Pago, cupom SUBFLOW15=15%)
2. **Página customizada** — icarovenzon352.hotmart.host/subflow-legendas... (Hero, vídeo, benefícios, pipeline, comparativo, garantia, FAQ)
3. **YouTube demo** — https://www.youtube.com/watch?v=8wywC_Evx9E (90s, público)
4. **Guia PDF** (vendas/isca/...) — checkout + cupom no fim
5. **PR #26** (Awesome-Whisper-Apps) — comentário com checkout
6. **PR #114** (awesome-video) — Subtitle & Caption Tools
7. **PR #1945** (awesome-ai-tools) — Developer tools
8. **AI Tool Directory** — submetido (aguardando review)
9. **Discussion #1 + README** — links checkout/cupom/página/vídeo
10. **8 tópicos no repo** (whisper, subtitles, transcription, cli, local-first, video, ai, opensource)

### ⏸️ Pendentes (login do dono)
- Reddit posts (5 subs + r/selfhosted + r/TranslationStudies + r/AIDeveloperNews)
- Dev.to / Hashnode / BetaList / Product Hunt / HF Space / Discord
- Show HN (IP penalizado)
- Club Hotmart welcome sequence (login separado)
- Webhook oficial Chrome (SPA não renderiza no Orca)
- Peerlist (só Google OAuth) / DevHunt / LaunchBoosts / Hashnode / HF (precisam GitHub logado no browser)
- RepoRanker / TinyLaunch / SubmitALLAI (login ou CAPTCHA humano)

### ⛔ Bloqueados definitivamente
- 18+ diretórios testados (lista v1-v5 em canais-extras*.md): login, pago ($99/$247/$497), 404, domínio morto, invite code
- IP do HN penalizado (automação)
- awesome-whisper (sindresorhus) restrito a contribuidores anteriores
- awesome-claude-code / awesome-python / awesome-vibe-coding / awesome-ai-agents-2026 — não encaixa ou restrito
- GitHub NÃO logado no browser (OAuth não completa)

### 💰 Vendas
- **0 reais** — monitorando 24h via loop (30min/check) + webhook cloudflared (server Flask :5050)

---

## Canais extras v6 descobertos (2026-08-10 ~04:00)
- **Tiny Startups** (tinystartups.com) — newsletter 20k founders, submit grátis com conta
- **JustFree.io** — diretório curado indie (submit no site)
- **Fazier** — leaderboard diário estilo PH (free, dofollow)
- **8 diretórios com backlink recíproco** (Tool Pilot, Foundr, Wavel, Based Tools, Buzzmatic, Look AI Tools, AI Toolz Dir, AI Tool Trek) — grátis em troca de link
- Testados bloqueados: Pitchwall (pago), Try.tools (404/promo), Publite/WIP/Launched.today (SPA vazio), launched.io/submit.coffee (mortos)

---

## 3 QUASE-PRONTOS (dono finaliza em 3 min — CHECKLIST-3-1MIN.md)
- ⚠️ **Tool Pilot** — form 95% preenchido; falta dropdown "Type of tool" + Submit
- ⚠️ **AI Toolz Dir** — 6 campos preenchidos; falta modal "Get listed for free" + categoria
- ⚠️ **SubmitALLAI** — 11 campos preenchidos; falta reCAPTCHA humano + Submit

## Vendas (verificação final)
- **0 reais** — webhook confirmado (2 vendas simuladas de teste, US$ 9,99)

---

## Canal novo quase-pronto (2026-08-10, v7)
- ⚠️ **Dofollow.Tools** — wizard 2 etapas preenchido (todos os campos + categorias Video/AI + Web + Freemium) — falta upload do LOGO (30s manual) + Submit. Backlink dofollow.
- 🔍 **Spiff.store / DataLook.io / BestOfWeb** — ativos, forms a testar.
