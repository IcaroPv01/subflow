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