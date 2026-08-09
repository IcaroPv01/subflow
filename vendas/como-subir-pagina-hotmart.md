# Como subir a página de vendas v2 no Hotmart (manual)

> Para o dono. A instância não consegue editar via browser (iframe app-vlc cross-origin bloqueia o acesso).

## Passo a passo

1. Acesse **https://app.hotmart.com** (logado como Icaro Venzon).
2. Menu lateral: **Produtos → SubFlow** (ou direto: https://app.hotmart.com/products/manage/8248938).
3. Aba **Página do produto** (ou "Página de vendas").
4. Na página customizada "SubFlow — Legendas profissionais de qualquer vídeo, 100% local", clique em **Editar** (o editor abre em nova aba).
5. No editor do Hotmart Pages: **bloco HTML** (ou "Código" / "Embed") — cole o conteúdo de **`vendas/hotmart-page-v2.html`** (arquivo no repo, commit `4c4d69a`).
6. **Imagens:** o HTML referencia `assets/demo.gif` (relativo). No Hotmart Pages, faça upload do GIF (`vendas/assets/demo.gif`) e ajuste o `src` para a URL do upload (ou use o link raw do GitHub: `https://raw.githubusercontent.com/IcaroPv01/subflow/main/vendas/assets/demo.gif`).
7. **Botão de compra:** o CTA aponta para `https://pay.hotmart.com/E107014071J` — confirme que o Hotmart não substituiu por outro link. Se o editor oferecer bloco "Botão de venda" nativo, prefira-o (gera o link correto automaticamente).
8. **Publicar** (botão Publicar no editor) e confira a página ao vivo.

## Checklist do conteúdo (v2)

- [ ] Hero com badge + CTA (US$ 9,99)
- [ ] Demo GIF (assets/demo.gif)
- [ ] 6 bullets de valor (transcrição, tradução, QC Netflix, anti-alucinação, privacidade, 2× rápido)
- [ ] Pipeline em 1 comando (terminal)
- [ ] Tabela comparativa (SubFlow vs Subtitle Edit vs Descript vs Whisper API)
- [ ] Testemunhos (3)
- [ ] Garantia de 7 dias
- [ ] Bônus (guia PDF + skill + scripts)
- [ ] FAQ (6 perguntas)
- [ ] CTA final + link do repo

## Alternativa (se quiser mais simples)

O Hotmart aceita **página externa**: o produto já tem `https://go.hotmart.com/E107014071J` (página de vendas externa). Se preferir, hospede o `hotmart-page-v2.html` no GitHub Pages (a landing já existe em `vendas/landing/`) e aponte o produto para lá.