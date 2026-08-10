# CHECKLIST DO DONO — Passos humanos pendentes (SubFlow)

> Consolidado pela instância deepseek em 2026-08-09. Cada item exige ação humana
> (dados pessoais, login, upload manual ou decisão). Atualizar conforme resolver.

---

## 🔴 Urgente (destravam publicação)

### 1. PromptBase — Zoneless (verificação de identidade)
- **Onde:** navegador do Orca, aba PromptBase (promptbase.com/sell) — fluxo Zoneless aberto na tela.
- **O que fazer:** preencher legal name, email, date of birth, home address (país: Brazil — dropdown já aberto).
- **Depois:** volta ao PromptBase → etapa 4/4 (review) → **Publicar**. (O formulário 1–3/4 já está salvo: Agent Skill, Claude Skill, $8.99, skill `subflow`, SKILL.md body, 2 exemplos, setup, USDC+Brazil.)
- **Feito quando:** a listagem "subflow" aparece pública em promptbase.com.

### 2. Hotmart — re-login (SSO)
- **Onde:** https://app.hotmart.com (o restart do browser apagou a sessão).
- **O que fazer:** logar como Icaro Venzon → Vendas > Minhas vendas (loop de 30 min manual).
- **Feito quando:** `app.hotmart.com/sales` carrega sem redirecionar para sso.hotmart.com/login.

### 4. Hotmart — configurar webhook oficial (CHROME REAL)
- **Onde:** app.hotmart.com → Produto SubFlow → Ferramentas → Webhooks (o SPA não renderiza essa seção no browser embutido do Orca; usar o Chrome real).
- **O que fazer:** webhook POST → `https://stuck-beats-interstate-vacuum.trycloudflare.com/hotmart/webhook` (produto 8248938), eventos PURCHASE_APPROVED + PURCHASE_COMPLETE. O server Flask já está rodando (porta 5050) e testado (venda id 1 de teste).
- **Feito quando:** uma compra de teste gera registro em `~/.subflow/sales.sqlite`.

### 5. Sessões técnicas no browser (para eu publicar)
- **Onde:** navegador do Orca (ou reconectar o Chrome MCP).
- **O que fazer:** logar: **Hacker News** (conta técnica), **Dev.to** (perfil técnico), **Hashnode**, **BetaList**, **Hugging Face**, **Reddit** (conta técnica).
- **Feito quando:** cada site carrega logado (ex.: HN não mostra "You have to be logged in").

---

## 🟡 Importante (desbloqueiam canais)

### 6. IndieHackers — sign-up + launch
- **Onde:** https://www.indiehackers.com/sign-up (bloqueado por Cloudflare na minha sessão).
- **O que fazer:** completar sign-up (username icaropv01), publicar launch no product-launch group com link do vídeo.
- **Feito quando:** post de launch visível em indiehackers.com.

### 7. r/selfhosted — flair humana
- **Onde:** reddit.com/r/selfhosted.
- **O que fazer:** flair/post do SubFlow exige aprovação humana (regras do sub).
- **Feito quando:** post publicado/respondido.

### 8. GitHub Sponsors — dados bancários
- **Onde:** github.com/sponsors (perfil IcaroPv01).
- **O que fazer:** configurar conta bancária/payout para aceitar sponsors.
- **Feito quando:** "Sponsors" ativo no perfil.

### 9. GoTranscript — cadastro/parceria
- **Onde:** gotranscript.com.
- **O que fazer:** decidir se cadastra o SubFlow como ferramenta/parceria (ou pular).
- **Feito quando:** decidido.

### 10. Reddit — login para posts novos (5 subs)
- **Onde:** reddit.com (conta técnica).
- **O que fazer:** logar para eu postar nos 5 subs (r/commandline, r/opensource, r/LocalLLaMA, r/Translation, r/VideoEditing) + comentários nos posts existentes (r/whisper 1vfs2ug, r/SideProject 1vfvdl9).
- **Feito quando:** reddit.com logado.

---

## ⚫ Bloqueados por decisão do dono (não fazer)

### 11. Twitter/X — PROIBIDO (rede social pessoal)
### 12. LinkedIn — PROIBIDO (rede social pessoal)
### 13. Facebook/Instagram — PROIBIDO

---

## ✅ Já resolvido pela instância (referência)

- YouTube demo publicado: https://www.youtube.com/watch?v=8wywC_Evx9E
- README com seção Resources + vídeo (commit c0e5d1e)
- Discussion #1: corpo + comentários com link/embed do vídeo + PDF gratuito
- PromptBase: etapas 1–3/4 preenchidas (aguardando Zoneless — item 1)
- Webhook server + túnel cloudflared ativos (testados)
- Textos prontos: `vendas/textos-prontos.md` (todos os canais com link do vídeo)
- Instruções Hotmart: `vendas/como-subir-pagina-hotmart.md`
- Página v2: `vendas/hotmart-page-v2.html` (com pixel de clique no checkout)
### 14. Logar em club.hotmart.com (welcome sequence)
- **Onde:** https://club.hotmart.com/oauth/login?productId=8248938
- **O que fazer:** logar no Club (domínio separado — a sessão do app.hotmart NÃO cobre) e configurar os 3 e-mails da welcome sequence (`vendas/welcome-sequence.md`): imediato (boas-vindas + 3 passos), 48h (3 dicas), 7 dias (bônus + upgrade Pro).
- **Feito quando:** automação com 3 e-mails visível em Área de membros > Automação.

### 15. Chrome real para webhook oficial
- **Onde:** Chrome do usuário → https://app.hotmart.com/webhooks (ou Produto > Ferramentas > Webhooks).
- **O que fazer:** criar webhook POST → `https://stuck-beats-interstate-vacuum.trycloudflare.com/hotmart/webhook`, eventos PURCHASE_APPROVED + PURCHASE_COMPLETE. (O browser embutido do Orca não renderiza essa seção do SPA; o Chrome externo está em tier 'read' para o computer-use.)
- **Feito quando:** webhook ativo no Hotmart (o server Flask já está rodando e testado — venda simulada registrada).

