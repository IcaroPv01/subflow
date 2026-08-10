# GUIA-LOGIN-DONO — destravar todos os canais (2026-08-10)

> Ordem de prioridade: cada login destrava N canais. Faça na ordem.
> Tempo estimado total: ~15 min. Após cada login, avise a instância — ela dispara o post na hora.

## 🔴 PRIORIDADE 1 — destrava os canais de maior alcance

### 1. Hacker News
- **URL:** https://news.ycombinator.com/login
- **Método:** email + senha (ou GitHub OAuth)
- **Tempo:** 1–2 min
- **Status:** ⛔ Bloqueado (o IP do Orca está com rate limit do HN — mas com login manual via navegador pode funcionar)
- **O que fazer após logar:** publicar **Show HN** (Submit → título + texto de `vendas/divulgacao/show-hn.txt` + link do vídeo YouTube)
- **Post pronto:** `vendas/divulgacao/show-hn.txt` (title + body + comentário com checkout/cupom)

### 2. GitHub (browser)
- **URL:** https://github.com/login
- **Método:** conta IcaroPv01 (email + senha)
- **Tempo:** 1–2 min
- **Status:** ⛔ Deslogado no browser (o gh CLI está autenticado, mas o browser do Orca não)
- **O que fazer após logar:** destrava OAuth de **Peerlist, DevHunt, LaunchBoosts, Hashnode, Hugging Face** (todos via GitHub)
- **Cadastros prontos:** `vendas/peerlist-cadastro.md`, `vendas/devhunt-cadastro.md`

### 3. Reddit (conta técnica)
- **URL:** https://www.reddit.com/login
- **Método:** conta técnica (NÃO usar a pessoal — restrição do dono). Criar nova se preciso (email + senha)
- **Tempo:** 2–3 min (inclui criação se necessário)
- **Status:** ⛔ Deslogado; posts antigos (r/whisper 1vfs2ug, r/SideProject 1vfvdl9) foram REMOVIDOS pelos filtros
- **O que fazer após logar:** re-postar nos 5 subs (r/commandline, r/opensource, r/LocalLLaMA, r/Translation, r/VideoEditing) + r/selfhosted + r/TranslationStudies
- **Posts prontos:** `vendas/textos-prontos.md` (seção 5) + `vendas/COMUNIDADES-NICHO.md`

### 4. Dev.to
- **URL:** https://dev.to/enter
- **Método:** email magic link (conta técnica)
- **Tempo:** 1–2 min
- **Status:** ⛔ Deslogado
- **O que fazer após logar:** publicar artigo "How I built a 100% local subtitle pipeline with Whisper" com embed do YouTube + link checkout
- **Artigo pronto:** `vendas/divulgacao/devto-article.md` (+ instruções de embed em `vendas/textos-prontos.md` seção 4)

### 5. Hugging Face
- **URL:** https://huggingface.co/login
- **Método:** GitHub OAuth
- **Tempo:** 1 min (junto com o GitHub)
- **Status:** ⛔ Deslogado
- **O que fazer após logar:** (a) criar Space Gradio com `vendas/demo-online/`; (b) postar em discuss.huggingface.co
- **Texto pronto:** `vendas/textos-prontos.md` (seção 6/Discord) e `vendas/COMUNIDADES-NICHO.md`

## 🟡 PRIORIDADE 2 — destrava canais secundários

### 6. Hashnode
- **URL:** https://hashnode.com/login
- **Método:** GitHub OAuth
- **Tempo:** 1 min (junto com o GitHub)
- **Status:** ⛔ Deslogado
- **O que fazer após logar:** publicar clone do artigo Dev.to com embed do YouTube
- **Artigo pronto:** mesmo `devto-article.md`

### 7. BetaList
- **URL:** https://betalist.com/login
- **Método:** email ou Google OAuth
- **Tempo:** 1–2 min
- **Status:** ⛔ Deslogado
- **O que fazer após logar:** cadastrar SubFlow (título + URL + descrição 280 chars com link do vídeo)
- **Texto pronto:** `vendas/textos-prontos.md` (seção 7)

### 8. Product Hunt
- **URL:** https://www.producthunt.com/login
- **Método:** Google/GitHub
- **Tempo:** 1–2 min
- **Status:** ⛔ Deslogado
- **O que fazer após logar:** cadastrar com `vendas/divulgacao/product-hunt.md` + link do vídeo + GIF; agendar ter/qua 08:00 PT
- **Texto pronto:** `vendas/divulgacao/product-hunt.md`

### 9. Club Hotmart (welcome sequence)
- **URL:** https://club.hotmart.com/oauth/login?productId=8248938
- **Método:** conta Hotmart separada (o domínio é diferente do app.hotmart)
- **Tempo:** 1–2 min
- **Status:** ⛔ Deslogado (a sessão do app.hotmart NÃO cobre o club)
- **O que fazer após logar:** configurar os 3 e-mails da welcome sequence (Área de membros > Automação)
- **Conteúdo pronto:** `vendas/welcome-sequence.md`

### 10. Chrome real (webhook oficial)
- **URL:** https://app.hotmart.com/webhooks (no Chrome real do usuário, não no Orca)
- **Método:** sessão Hotmart já existente no Chrome real
- **Tempo:** 2 min
- **Status:** ⛔ Bloqueado (o SPA não renderiza no browser embutido do Orca; o Chrome real está em tier 'read' para o computer-use)
- **O que fazer após logar:** criar webhook POST → `https://stuck-beats-interstate-vacuum.trycloudflare.com/hotmart/webhook` + eventos PURCHASE_APPROVED + PURCHASE_COMPLETE
- **Instruções:** `vendas/CHECKLIST-DONO-FOCO-HOTMART.md` (item webhook)

### 11. IndieHackers
- **URL:** https://www.indiehackers.com/sign-up
- **Método:** NEXT com username `icaropv01` (já preenchido) + email
- **Tempo:** 2–3 min (o sign-up estava bloqueado por Cloudflare na minha sessão)
- **Status:** ⛔ Bloqueado (Cloudflare)
- **O que fazer após logar:** publicar launch no product-launch group com link do vídeo + checkout
- **Texto pronto:** `vendas/textos-prontos.md` (modelo show-and-tell)

## ✅ JÁ PRONTOS (sem login do dono)
- YouTube demo publicado: https://www.youtube.com/watch?v=8wywC_Evx9E
- AI Tool Directory: submetido (aguardando review)
- Discussion #1 + README + PR #26: com links de checkout/cupom
- Página customizada + checkout + cupom: no ar
- Monitoramento de vendas: ativo (loop 24h + webhook)

## 📋 Checklist rápido (marque ao logar)
- [ ] HN → Show HN
- [ ] GitHub (browser) → Peerlist, DevHunt, LaunchBoosts, Hashnode, HF
- [ ] Reddit (técnica) → 5 subs + r/selfhosted + r/TranslationStudies
- [ ] Dev.to → artigo com embed
- [ ] HF → Space Gradio + discuss
- [ ] Hashnode → clone artigo
- [ ] BetaList → cadastro
- [ ] Product Hunt → cadastro agendado
- [ ] Club Hotmart → welcome sequence
- [ ] Chrome real → webhook oficial
- [ ] IndieHackers → launch
