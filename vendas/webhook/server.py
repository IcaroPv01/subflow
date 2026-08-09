"""Servidor Flask que recebe webhooks do Hotmart e notifica o supervisor.

Endpoints:
- POST /hotmart/webhook  -> recebe evento do Hotmart (configurar em app.hotmart.com/webhooks)
- POST /click/checkout    -> registra clique no botão de compra
- GET  /status            -> estado atual (última venda, total)
- GET  /sales             -> lista de vendas registradas

Rodar: python vendas/webhook/server.py
Expor publicamente via: ngrok http 5050
"""
import json
import os
import sqlite3
from datetime import datetime
from pathlib import Path
from flask import Flask, request, jsonify

DB = Path.home() / '.subflow' / 'sales.sqlite'
DB.parent.mkdir(exist_ok=True)

def db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init():
    with db() as c:
        c.executescript('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ts TEXT NOT NULL,
            event TEXT NOT NULL,
            product_id TEXT,
            product_name TEXT,
            buyer_email TEXT,
            buyer_name TEXT,
            price REAL,
            currency TEXT,
            status TEXT,
            raw_json TEXT
        );
        CREATE TABLE IF NOT EXISTS clicks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ts TEXT NOT NULL,
            ip TEXT,
            ua TEXT,
            referer TEXT
        );
        ''')

app = Flask(__name__)
init()

@app.post('/hotmart/webhook')
def hotmart_webhook():
    data = request.json or {}
    event = data.get('event', 'UNKNOWN')
    payload = data.get('data', {}) if isinstance(data, dict) else {}
    buyer = payload.get('buyer', {}) if isinstance(payload, dict) else {}
    product = payload.get('product', {}) if isinstance(payload, dict) else {}
    price = payload.get('price', {}) if isinstance(payload, dict) else {}
    ts = datetime.now().isoformat(timespec='seconds')
    print(f'[{ts}] EVENT: {event} | {product.get("name")} | {buyer.get("email")} | {price.get("value")} {price.get("currency")}')
    if event in ('PURCHASE_APPROVED', 'PURCHASE_COMPLETE', 'PURCHASE_BILLET_PRINTED'):
        with db() as c:
            c.execute('''INSERT INTO sales (ts, event, product_id, product_name, buyer_email, buyer_name, price, currency, status, raw_json)
                         VALUES (?,?,?,?,?,?,?,?,?,?)''',
                      (ts, event, product.get('id'), product.get('name'),
                       buyer.get('email'), buyer.get('name'),
                       price.get('value'), price.get('currency'),
                       event, json.dumps(data)))
            c.commit()
    return ('', 204)

@app.post('/click/checkout')
def click_checkout():
    ts = datetime.now().isoformat(timespec='seconds')
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    ua = request.headers.get('User-Agent', '')
    ref = request.headers.get('Referer', '')
    print(f'[{ts}] CLICK from {ip} (referer: {ref})')
    with db() as c:
        c.execute('INSERT INTO clicks (ts, ip, ua, referer) VALUES (?,?,?,?)', (ts, ip, ua, ref))
        c.commit()
    return ('', 204)

@app.get('/status')
def status():
    with db() as c:
        sales = c.execute("SELECT COUNT(*) as n, COALESCE(SUM(price),0) as total FROM sales WHERE event IN ('PURCHASE_APPROVED','PURCHASE_COMPLETE')").fetchone()
        clicks = c.execute('SELECT COUNT(*) as n FROM clicks').fetchone()
        last = c.execute("SELECT ts, product_name, buyer_email, price, currency FROM sales ORDER BY id DESC LIMIT 1").fetchone()
    return jsonify({
        'sales_count': sales['n'],
        'sales_total': sales['total'],
        'clicks_count': clicks['n'],
        'last_sale': dict(last) if last else None,
    })

@app.get('/sales')
def sales():
    with db() as c:
        rows = c.execute("SELECT * FROM sales ORDER BY id DESC LIMIT 100").fetchall()
    return jsonify([dict(r) for r in rows])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=False)
