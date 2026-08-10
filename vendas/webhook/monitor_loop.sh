#!/bin/bash
# Loop de monitoramento de vendas (30 min) — loga em monitor-vendas.log
LOG=/c/Users/i.venzon/Documents/Claude/Projects/subflow/vendas/webhook/monitor-vendas.log
for i in $(seq 1 48); do
  TS=$(date '+%Y-%m-%d %H:%M:%S')
  STATUS=$(curl -s http://127.0.0.1:5050/status 2>/dev/null)
  echo "[$TS] $STATUS" >> "$LOG"
  sleep 1800
done
