# CHECKLIST DO DONO — Foco Hotmart (tráfego para o checkout)

> Atualizado: 2026-08-10. Tudo verificado e no ar.

## Links canônicos
- **Checkout:** https://pay.hotmart.com/E107014071J
- **Página customizada:** https://icarovenzon352.hotmart.host/subflow-legendas-profissionais-de-qualquer-video-100-local-f419da64-0079-4a97-9c03-33f796bb241c
- **Cupom:** `SUBFLOW15` (15% off)
- **Preço:** R$ 55,86 (~US$ 9,99)
- **Webhook:** https://stuck-beats-interstate-vacuum.trycloudflare.com/hotmart/webhook (server Flask ativo, testado)
- **Loop de monitoramento:** `vendas/webhook/monitor_loop.sh` (ativo 24h, checagem 30min, log em `monitor-vendas.log`)
- **Vendas:** 0 reais (monitorando)

## O que já está no ar
- [x] Página customizada publicada (Hero, vídeo, benefícios, pipeline, comparativo, garantia, FAQ)
- [x] Checkout configurado (Pix, Cartão, PayPal, Mercado Pago, cupom ativo)
- [x] Cupom SUBFLOW15 (15%)
- [x] Vídeo YouTube: https://www.youtube.com/watch?v=8wywC_Evx9E
- [x] Webhook testado (venda simulada registrada: US$ 9,99)
- [x] README + Discussion #1 + PR #26 com links de checkout

## O que fazer para converter (próximos passos)
1. **Logar no Hotmart Club** (club.hotmart.com) → configurar welcome sequence (3 e-mails de `vendas/welcome-sequence.md`)
2. **Chrome real** → app.hotmart.com/webhooks → URL do túnel + eventos PURCHASE_APPROVED/COMPLETE
3. **Logar no Reddit** (conta técnica) → re-postar nos subs (r/whisper, r/SideProject removidos pelos filtros) + posts novos (r/commandline, r/opensource, r/LocalLLaMA, r/Translation, r/VideoEditing) com link do checkout
4. **Show HN** (HN logado, rate limit expirado) → postar `show-hn.txt` + link do vídeo
5. **Dev.to / Hashnode** → artigo "How I built a 100% local subtitle pipeline with Whisper" + embed do vídeo + link do checkout
6. **BetaList / Product Hunt / HF Space** → cadastrar com link do checkout
7. **Discord** (HF, LocalLLaMA, IndieHackers) → posts com link do vídeo + checkout

## Textos prontos
- `vendas/textos-prontos.md` — todos os posts/comentários com links
- `vendas/divulgacao/show-hn.txt` — Show HN
- `vendas/divulgacao/devto-article.md` — artigo Dev.to/Hashnode
- `vendas/divulgacao/product-hunt.md` — Product Hunt