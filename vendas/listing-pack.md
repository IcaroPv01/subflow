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
- [ ] **PromptBase** — formulário em andamento (etapa 2/4 "Skill File"), campos preenchidos via JS: item type=Agent Skill, runtime=Claude Skill, preço=$8.99, nome=subflow, trigger, SKILL.md body (pipeline completo), tools="Bash, Read, Edit, Grep, Glob". **Faltam:** etapa 3/4 (exemplos), 4/4 (publicar), e o clique "Next" (runtime caiu antes).
- [ ] **Runtime do Orca instável** — canal de browser (snapshot/eval/goto) em crash loop persistente após kill/restart; canal de app (tab list/status) OK. **Ação do dono:** reiniciar o app Orca (fechar e abrir) ou reconectar o Chrome MCP. Retomar PromptBase (etapa 2/4 salva) quando estabilizar.

- [x] **Discussion #1** — atualizada via gh CLI com link do YouTube publicado (discussioncomment-17955781).

### 2026-08-09 — Divulgação do vídeo YouTube (sessão 2, via gh CLI)
- [x] **README**: seção "Resources" adicionada com link do vídeo (commit c0e5d1e).
- [x] **Discussion #1**: corpo atualizado com link + embed do vídeo (updateDiscussion OK) + comentário com link (17955926) + PDF (17954844).
- [x] **Textos prontos**: `vendas/divulgacao/textos-prontos.md` (Reddit comments r/whisper + r/SideProject, Show HN com vídeo, Dev.to/Hashnode com embed, 5 posts Reddit novos, Discord 3 servers, BetaList, PH, 4 diretórios SEO).
- [x] **Instruções Hotmart**: `vendas/como-subir-pagina-hotmart.md` (para o dono subir a página v2).
- [ ] Browser Orca: ainda em crash loop — retomar PromptBase (2/4) + canais quando voltar.

### 2026-08-09 — Estado final (aguardando restart manual do Orca pelo dono)
- [ ] **Browser Orca**: crash loop persiste mesmo após kill + open via CLI (canal de app OK, CDP do browser morto). **Ação do dono:** fechar a janela do app Orca e reabrir manualmente (não apenas CLI).
- [ ] **Pendente quando browser voltar:** PromptBase etapa 3/4 (payout Stripe — blocker humano) + 4/4 + publicar; Show HN; Dev.to; Hashnode; BetaList; Product Hunt; HF Space; Discord (3 servers); Reddit posts novos (5); comentários r/whisper + r/SideProject; diretórios SEO (4); IndieHackers sign-up.
- [ ] **Loop 30 min:** checar vendas Hotmart + responder comentários (iniciar quando browser voltar).

### 2026-08-09 — PromptBase etapas 2/4 e 3/4 (sessão 2, retomada)
- [x] **Etapa 2/4 COMPLETA** — validação passou (o clique em "Next: Enable Payouts" avançou): skill name=subflow, trigger, SKILL.md body (pipeline completo), tools, 2 exemplos, modelo **claude-5-sonnet**, setup instructions.
- [x] **Etapa 3/4 (Payout)**: método **Instant USDC** selecionado, país **Brazil** (BR) setado, botão "Enable Payouts" clicado.
- [ ] **BLOCKER HUMANO DO DONO**: o fluxo abriu verificação de identidade (Zoneless/USDC) pedindo: legal name, email, date of birth, home address. **Ação do dono:** preencher os dados pessoais no navegador (aba PromptBase) e completar. Depois: etapa 4/4 (review) + publicar.

### 2026-08-09 — PromptBase re-executado (sessão 2, 2ª tentativa pós-restart)
- [x] **Etapa 1/4 + 2/4 REFEITAS e validadas** (o restart resetou o SPA): Agent Skill + Claude Skill + $8.99 + nome subflow + descrição + SKILL.md body completo (frontmatter name/description/allowed-tools + corpo) + 2 exemplos + setup.
- [x] **Etapa 3/4**: Instant USDC + Brazil (BR) + "Enable Payouts" clicado → fluxo **Zoneless (verificação de identidade) aberto**.
- [ ] **BLOCKER HUMANO (dono):** preencher no Zoneless: legal name, email, date of birth, home address (país Brazil). Depois: voltar ao PromptBase → etapa 4/4 (review) → publicar.

### 2026-08-09 ~14:20 — PromptBase no ponto máximo (3ª execução, com técnica de espera 3s)
- [x] **Técnica descoberta:** o React do PromptBase precisa de ~3s entre preencher e clicar Next (registra os valores antes da validação). Fluxo: etapa 1/4 (Agent Skill+Text+$8.99+SubFlow+desc) → Skill Details (Agent Skill+Claude Skill+$8.99+subflow+desc) → Skill File (9 campos: name, when-to-use, SKILL.md body, tools, 2 exemplos, setup) → Payout (USDC+Brazil) → Enable Payouts → **Zoneless aberto**.
- [ ] **BLOCKER HUMANO (dono):** Zoneless pede legal name, email, date of birth, home address (dropdown de países aberto). Preencher → volta ao PromptBase → etapa 4/4 (review) → publicar.

### 2026-08-09 ~14:30 — Reddit posts verificados
- [x] **r/whisper 1vfs2ug**: post existe (autor Objective_Wrap2408) mas **REMOVIDO** ("Desculpe, este post foi removido") — sem o que comentar.
- [x] **r/SideProject 1vfvdl9**: post existe mas **REMOVIDO pelos filtros do Reddit** — sem o que comentar.
- [ ] **Ação:** quando houver sessão Reddit, re-postar (ou contatar mods) com link do vídeo + checkout. Textos prontos em vendas/textos-prontos.md.

### 2026-08-09 ~14:35 — Tarefas sem login concluídas
- [x] **README**: seção Resources com link do YouTube (verificado via gh api — já estava, commit c0e5d1e).
- [x] **Discussion #1**: corpo com link+embed do vídeo + 2 comentários com vídeo (verificado via GraphQL — já estava).
- [x] **vendas/textos-prontos.md**: criado na raiz vendas/ (todos os textos com link do vídeo para Show HN, Dev.to, Hashnode, BetaList, PH, HF, Discord, Reddit, diretórios SEO).
- [x] **vendas/CHECKLIST-DONO.md**: criado — 13 itens humanos pendentes (Zoneless, Hotmart re-login, página v2, webhook, sessões técnicas, IndieHackers, r/selfhosted, Sponsors, GoTranscript, Reddit login; Twitter/LinkedIn/FB/IG proibidos).
- [x] **Reddit**: posts 1vfs2ug e 1vfvdl9 REMOVIDOS pelos filtros — re-post pendente com sessão.
- [ ] **Show HN + Dev.to**: aguardando sessão (HN e Dev.to deslogados).

### 2026-08-09 ~14:45 — Hotmart verificado (browser voltou)
- [x] **Tarefa 1**: navegado para products/manage/8248938 — painel OK, screenshot capturado.
- [x] **Tarefa 2**: **0 vendas** (Minhas vendas: "Total de 0 registros entre 10/07 e 09/08", "Nenhum resultado encontrado").
- [x] **Tarefa 3**: **checkout NO AR** — pay.hotmart.com/E107014071J carrega: "SubFlow — Legendas profissionais de qualquer vídeo, 100% local", autor ICARO PIETRO VENZON, R$ 55,86, cartão+PayPal.
- [x] **Tarefa 4**: editor do Hotmart Pages **abriu** (janela editor.pages.hotmart.com, AI mode) — página já publicada (20260804-v0001) com CTA correto. Editor AI não aceita HTML inline → fallback hotmart-page-v2.html continua disponível para upload manual se quiser o layout customizado.

### 2026-08-09 ~14:55 — Tarefas 5-8 (Show HN, Dev.to, Hashnode, BetaList)
- [ ] **Show HN**: HN BLOQUEADO com "Sorry." (rate limit do HN por navegacao automatizada rapida — costuma durar ~30min+). **Acao:** aguardar ~30-60min e tentar de novo, ou o dono posta manualmente com vendas/divulgacao/show-hn.txt + link do video.
- [ ] **Dev.to**: exige login (sem conta tecnica logada) — pular até o dono logar.
- [ ] **Hashnode**: exige login (callbackUrl=%2Fdrafts) — pular até o dono logar.
- [ ] **BetaList**: exige login (betalist.com/sign_in) — pular até o dono logar.

### 2026-08-10 ~21:40 — HOTMART: PÁGINA DE VENDAS PUBLICADA (foco total do dono)
- [x] **Página customizada PUBLICADA** via editor AI do Hotmart Pages (janela editor.pages.hotmart.com):
  - URL: https://icarovenzon352.hotmart.host/subflow-legendas-profissionais-de-qualquer-video-100-local-f419da64-0079-4a97-9c03-33f796bb241c
  - Seções adicionadas via prompts AI: Hero (headline + CTA verde "Comprar R$ 55,86"), Benefícios (6 cards: Whisper local, tradução lotes, QC Netflix, anti-alucinação, 100% privado, 2x rápido), Vídeo YouTube embed (8wywC_Evx9E), Pipeline, Comparativo (SubFlow vs Subtitle Edit vs Whisper API), Garantia 7 dias, FAQ, CTA final "Comprar SubFlow Agora".
  - Screenshots: vendas/demo/_hotmart-editor-final.png + temp do preview.
- [x] **Checkout confirmado no ar**: pay.hotmart.com/E107014071J (R$ 55,86, cartão+PayPal).
- [x] **0 vendas** confirmado em Minhas vendas.
- [ ] **PRÓXIMO**: configurar webhook de vendas (tarefa 3), order bumps/upsells (4), welcome sequence (6), cupom SUBFLOW15 (7), afiliados (8).

### 2026-08-10 ~22:00 — Webhook Hotmart: SPA nao renderiza no browser embutido
- [ ] **Webhook**: app.hotmart.com/products/manage/8248938/webhooks e /connect/webhooks nao renderizam (SPA limita no browser embutido; /webhooks = not-found). Seção "Ferramentas" do produto abre /tools/list/producer (vazio). **Acao do dono:** configurar webhook manualmente no Chrome real: Produto > Ferramentas > Webhooks, URL https://stuck-beats-interstate-vacuum.trycloudflare.com/hotmart/webhook, eventos PURCHASE_APPROVED + PURCHASE_COMPLETE. Server Flask ativo e testado.

### 2026-08-10 ~22:11 — HOTMART: CUPOM CRIADO
- [x] **Cupom SUBFLOW15 = 15% de desconto** (todas as ofertas, válido desde 09/08/2026, America/Sao_Paulo).
  - Detalhe técnico: o campo de porcentagem usa máscara decimal brasileira — "15" vira "0,15" (0,15%), "1500" vira "15,00" (15%). O fill via CDP registra corretamente.
- [ ] **Próximo:** order bumps/upsells (Precificação e ofertas), welcome sequence (Área de membros), afiliados.
