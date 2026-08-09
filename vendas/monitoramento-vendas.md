# Monitoramento de Vendas (manual até gerarmos OAuth Hotmart)

> Como verificar vendas sem precisar logar no Hotmart.

## Caminho 1 — Hotmart Connect (OAuth, melhor)

Quando você gerar as credenciais OAuth do Hotmart Connect, podemos:
- Criar um cron job que verifica `/v1/sales/history` a cada hora
- Notificar no Discord/Slack quando houver venda
- Salvar histórico em SQLite

**Como gerar as credenciais:**
1. Acesse https://app.hotmart.com/connect
2. Crie uma aplicação (nome: "SubFlow Sales Monitor", tipo: server-side)
3. Solicite scopes: `sales.read`, `products.read`
4. Copie `client_id` e `client_secret`
5. Salve em `.env` na pasta do projeto

Quando tiver, eu configuro o monitoramento automático.

## Caminho 2 — Verificação manual (atual, via você)

Para verificar vendas agora:
1. Acesse https://app.hotmart.com
2. Menu: Vendas > Minhas vendas
3. Filtre por produto: SubFlow
4. Veja se há registros de vendas aprovadas

## Caminho 3 — Pixel de conversão no checkout

Posso adicionar um pixel (webhook) na página customizada que registra cliques no botão de compra. Quando o usuário clicar em "Comprar", um POST é enviado para um endpoint nosso. Útil para medir interesse vs conversão.

Endpoint exemplo (Flask):
```python
from flask import Flask, request
app = Flask(__name__)
@app.post("/checkout-click")
def track():
    ts = datetime.now().isoformat()
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    print(f"[{ts}] checkout click from {ip}")
    return ("ok", 200)
if __name__ == "__main__":
    app.run(port=5050)
```

Quando configurarmos, eu adiciono o JS na página de vendas que faz POST no endpoint.

## Caminho 4 — Alertas via e-mail do Hotmart

O Hotmart envia e-mail para o produtor a cada venda. Configure para:
- Encaminhar para um e-mail com filtro que adiciona tag "SubFlow-venda"
- Eu posso ler essa caixa e atualizar o estado

## Caminho 5 — Webhook Hotmart

O Hotmart permite configurar webhooks em https://app.hotmart.com/webhooks (configurações de API). Quando uma venda é aprovada, o Hotmart faz POST para uma URL sua com os dados da venda.

Endpoint sugerido (precisa de servidor público — pode usar ngrok ou cloudflare tunnel):
```
https://your-server.com/hotmart/webhook
```

Payload exemplo:
```json
{
  "event": "PURCHASE_APPROVED",
  "data": {
    "product": {"id": 8248938, "name": "SubFlow"},
    "buyer": {"name": "...", "email": "..."},
    "price": {"value": 9.99, "currency": "USD"}
  }
}
```

Se quiser, eu posso configurar um pequeno servidor (Python/Flask) com ngrok para receber esses webhooks.
