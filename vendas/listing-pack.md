# SubFlow — Listing Pack & Milestones

Log de execução da campanha de divulgação (supervisor/watchdog 08/2026).
Atualizado por: instância deepseek-v4-flash (execução via CLI + orca browser).

## Links canônicos
- Repo: https://github.com/IcaroPv01/subflow
- Checkout Hotmart (US$ 9,99): https://pay.hotmart.com/E107014071J
- PDF gratuito (guia PT-BR): https://raw.githubusercontent.com/IcaroPv01/subflow/main/vendas/isca/guia-legendagem-profissional-pt-br.pdf
- Landing EN: https://icaropv01.github.io/subflow/ (vendas/landing/index.html)

---

## Milestones

### 2026-08-09 — Sessão de execução (deepseek-v4-flash)

#### Verificações iniciais
- [x] Repo clonado: `~/Documents/Claude/Projects/subflow` (main, eb75e80)
- [x] Assets confirmados: vendas/assets/*.png + demo.gif; divulgacao/*.txt; demo-online/ (app.py Gradio); isca/guia PDF; landing/
- [ ] **Hotmart vendas** — BLOQUEADO: app.hotmart.com redireciona para SSO; browser sem sessão logada. Requer login do dono.
- [ ] **PromptBase** — NÃO ENCONTRADA listagem "subflow" na busca pública (promptbase.com/marketplace?q=subflow → 0 hits; /search → Page Not Found). Requer login para verificar perfil do vendedor.
- [ ] **IndieHackers** — BLOQUEADO: sign-up requer conta/sessão. Requer login do dono.
- [ ] **r/whisper** — NÃO LOCALIZADO o post do SubFlow (busca em r/whisper e r/SideProject sem resultados; perfil reddit "icaropv01" não existe). Verificar com o dono o username/post real.

#### Assets gerados (sem login)
- [x] **YouTube demo** `vendas/assets/subflow_demo.mp4` (90 s, 1280x720, 7 cenas conforme roteiro; hooks, split-screen QC antes/depois, langcheck, caso real, CTA PDF, end screen). Frames validados.
- [x] **Artigo Dev.to/Hashnode** `vendas/divulgacao/devto-article.md` (~800 palavras EN: "How I built a 100% local subtitle pipeline with Whisper").
- [x] **Product Hunt copy** `vendas/divulgacao/product-hunt.md` (criado — não existia no repo).

#### Publicações — TODAS BLOQUEADAS por sessão
- [ ] YouTube upload (studio.youtube.com)
- [ ] X/Twitter thread (7 tweets)
- [ ] LinkedIn post
- [ ] Show HN + comentário checkout
- [ ] Dev.to
- [ ] Hashnode
- [ ] BetaList
- [ ] Product Hunt (schedule ter/qua 08:00 PT)
- [ ] Hugging Face Space (demo-online/)
- [ ] Lobsters (pular se precisar convite)

#### Promoção cruzada
- [ ] Comentário próprio com checkout em cada post
- [x] **Discussion #1** — atualizada via gh CLI (comentário #discussioncomment-17954844): link do PDF gratuito adicionado; Show HN pendente (link será inserido quando publicado).
- [x] gh CLI autenticado (IcaroPv01) — canal GitHub via API funcional (sem depender do browser).

#### Preparado (aguardando sessão)
- [x] Thread X (7 tweets) lida e pronta para postar — `vendas/divulgacao/twitter-thread-en.txt`
- [x] app.py do demo-online validado (sintaxe OK) — pronto para HF Space
- [x] Repo sem PRs/issues abertos (PR #26 já tratado)

---

## Blocker de sessão (crítico)
O browser embutido do Orca (perfil `default`, partition `persist:orca-browser`) **não tem sessão logada** em nenhum serviço (GitHub mostra página de visitante). Ferramentas Chrome MCP (Control Chrome / Claude in Chrome) e Windows-MCP/computer-use **não estão conectadas** nesta instância. Todas as publicações exigem login do dono.

**Necessário (ação humana):**
1. Logar no browser do Orca: Hotmart (conta do vendedor), Google/YouTube, X, LinkedIn, HN, Dev.to, Hashnode, BetaList, Product Hunt, Hugging Face, Reddit.
2. OU reconectar o Chrome MCP (Chrome real do usuário, que tem as sessões).
3. Confirmar o username real do Reddit e o post do r/whisper.
### 2026-08-09 — Sessão 2 (supervisor, restrições dono: sem redes sociais pessoais)
- [x] **Hotmart vendas (verificação a):** página de Vendas (app.hotmart.com/sales) **SEM vendas** — tabela vazia, 0 registros. Produto SubFlow ativo (pagina manage 8248938 OK, logado como Icaro Venzon).
- [x] **PromptBase (verificação b):** listagem "subflow" NAO publicada — busca pública 0 hits; /sell mostra formulário de criação (dropdowns: item type inclui "Agent Skill", generation Text/Images/Videos, preço), mas preenchido com outro prompt ("Vibrant Startup Logos"). Criar listagem nova quando possível.
- [x] **IndieHackers (verificação c):** BLOQUEADO por desafio Cloudflare (indiehackers.com/sign-up) após 2 tentativas + reload. Tentar novamente em outra janela/sessão.
- [x] **r/whisper (verificação d):** post do SubFlow NAO localizado — busca global "subflow", "IcaroPv01" e feed r/whisper sem resultados (sub é do app social Whisper, não do ASR). Username Reddit não confirmado.

### 2026-08-09 — YouTube publicado (sessão 2)
- [x] **YouTube demo PUBLICADO** — "Subtitle a whole film in under 8 hours (Whisper, local, free)", 1:31, visibilidade Público.
      Link: https://www.youtube.com/watch?v=8wywC_Evx9E
      (Título ajustado pelo dono: "under 8 hours" — o filme leva ~7h50, menos de 8h.)
- [x] Descrição com links: repo, PDF gratuito, checkout Hotmart.

### 2026-08-09 — Hotmart página v2 (sessão 2)
- [x] **Página v2 criada** — `vendas/hotmart-page-v2.html` (hero + demo.gif, bullets, pipeline 1 comando, comparativo, testemunhos, garantia 7 dias, bônus, FAQ, CTA checkout). Commit 4c4d69a.
- [ ] **Editar via UI** — BLOQUEADO: editor do Hotmart Pages não abre no browser embutido do Orca (cliques JS e reais falham; runtime instável; iframe app-vlc cross-origin). **Ação do supervisor:** subir `vendas/hotmart-page-v2.html` manualmente no Hotmart Pages (Editar → HTML) e publicar.
- [x] Hotmart logado como Icaro Venzon; produto ativo (US$ 9,99; links go/pay E107014071J).

### 2026-08-09 — PromptBase em progresso (sessão 2)
- [ ] **PromptBase** — formulário de criação em andamento (etapa 2/4 "Skill File"): item type=Agent Skill, runtime=Claude Skill, preço=$8.99, nome=subflow, trigger preenchido, SKILL.md body + tools preenchidos. **Faltam:** etapa 3/4 (exemplos) e 4/4 (publicar).
- [ ] Runtime do Orca instável (cai repetidamente após ~2min de uso intenso) — retomar quando estabilizar.
