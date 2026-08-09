# SubFlow Webhook Server

Servidor Flask que recebe webhooks do Hotmart (notificação de vendas) e registra cliques no checkout.

## Rodar localmente
```bash
pip install -r requirements.txt
python server.py
```

Servidor roda em http://127.0.0.1:5050

## Expor publicamente (para Hotmart webhook)
```bash
ngrok http 5050
# copia a URL https://xxxx.ngrok-free.app
```

## Configurar webhook no Hotmart
1. Acesse https://app.hotmart.com/webhooks
2. Adicione URL: `https://your-server/hotmart/webhook`
3. Selecione eventos: `PURCHASE_APPROVED`, `PURCHASE_COMPLETE`, `PURCHASE_BILLET_PRINTED`
4. Salve

## Endpoints
- `POST /hotmart/webhook` — recebe eventos
- `POST /click/checkout` — registra cliques (adicionar na página customizada)
- `GET /status` — última venda + total
- `GET /sales` — lista de vendas

## Adicionar tracking na página de vendas
Cole no HTML da página customizada do Hotmart:
```html
<script>
document.querySelector('a[href*="pay.hotmart.com"], #buy-button, button.comprar, .cta-button')
  ?.addEventListener('click', () => {
    fetch('https://your-server/click/checkout', {method:'POST'});
  });
</script>
```

## Banco de dados
SQLite em `~/.subflow/sales.sqlite` — pode ser inspecionado com `sqlite3 ~/.subflow/sales.sqlite`.
