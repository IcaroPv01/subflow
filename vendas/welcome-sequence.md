# Welcome Sequence (3 e-mails para novos compradores)

> Configurar no Hotmart: automação de e-mails pós-compra. Cada e-mail é enviado automaticamente após X horas/dias.

## E-mail 1 — Imediato após a compra (5 minutos depois)

**Assunto:** Bem-vindo ao SubFlow! Comece aqui 👇

**Corpo:**

Oi, [nome]!

Parabéns pela compra do **SubFlow**. Você agora tem acesso ao pipeline 100% local de legendagem profissional.

**3 passos para começar em 5 minutos:**

1. **Instale o CLI**
   ```bash
   git clone https://github.com/IcaroPv01/subflow.git
   cd subflow
   pip install -e .
   ```

2. **Baixe o Faster-Whisper-XXL**
   - Windows: https://github.com/Purfview/whisper-standalone-win/releases
   - Coloque em `./tools/whisper.exe`

3. **Rode seu primeiro filme**
   ```bash
   subflow init --name meu-filme
   subflow run "URL_DO_VIDEO" --src-lang fr --tgt-lang pt
   ```

**Recursos úteis:**
- 📘 [Guia gratuito PT-BR (PDF, 9 seções)](https://raw.githubusercontent.com/IcaroPv01/subflow/main/vendas/isca/guia-legendagem-profissional-pt-br.pdf)
- 🎯 [Demo online (HF Space)](https://huggingface.co/spaces/IcaroPv01/subflow-demo)
- 📚 [Comparativo vs outras ferramentas](https://github.com/IcaroPv01/subflow/blob/main/vendas/comparativo.md)

Dúvidas? Responda este e-mail.

Boas legendas! 🎬
— Icaro

---

## E-mail 2 — 48h depois (depois de testar)

**Assunto:** 3 dicas para tirar o máximo do SubFlow

**Corpo:**

Oi, [nome]!

Espero que você já tenha rodado o SubFlow no seu primeiro vídeo. Aqui vão 3 dicas que vão economizar horas:

### 1. Construa um glossário rico ANTES de traduzir
O `subflow glossary build` extrai termos automaticamente. Mas editar `glossary/glossary.md` ANTES de começar a tradução vale ouro — economiza 20% do tempo da passada humana.

### 2. Rode `langcheck` ANTES de traduzir
Áudio em árabe/mandarim/japonês pode ter alucinações do Whisper. O langcheck pega 95% delas. Detectar antes = corrigir 1 vez, não 3.

### 3. Use `--batch 30` (não 50)
Batches menores = contexto mais limpo pra tradução. Testei 20, 30, 50 — **30 é o sweet spot** para qualidade vs velocidade.

**Bônus:** Se você está traduzindo documentários, o [caso real do filme Soleil Ô](https://github.com/IcaroPv01/subflow/blob/main/vendas/divulgacao/youtube-demo-roteiro.md) mostra como aplicar tudo isso em 7h50 para um filme de 104 min.

Próximo passo: tente o `subflow qc --profile netflix --max-cps 17 --max-peak-cps 20` e veja a mágica acontecer.

Abraço,
— Icaro

---

## E-mail 3 — 7 dias depois (engajamento / upsell)

**Assunto:** Bônus secreto: templates PT-BR + upgrade Pro (24h)

**Corpo:**

Oi, [nome]!

Uma semana com o SubFlow — espero que esteja salvando horas no seu trabalho.

Como bônus pelos primeiros compradores, quero te dar **2 presentes**:

### 🎁 Bônus 1: 30 templates PT-BR editáveis
Markdown editável com prompts de tradução por gênero (documentário, ficção, palestra, entrevista). Respondendo este e-mail com "QUERO", eu te envio.

### 🚀 Bônus 2: Upgrade Pro por 50% off (24h só)
O **SubFlow Pro** (era R$ 129,90) está por **R$ 64,90 só para você**. Inclui:
- Todos os 30 templates PT-BR
- Pack de CPS profiles (Netflix, Disney+, Prime, Globoplay)
- Glossário cinematográfico (nomes de movimentos, escolas)
- Atualizações vitalícias
- Acesso ao Discord privado de legendadores

[QUERO O PRO POR R$ 64,90 →](https://pay.hotmart.com/E107014071J)

(Promo válida só nas próximas 24h.)

Até a próxima,
— Icaro

---

## Configuração no Hotmart

1. **Automação de e-mails** → Configurar sequência:
   - E-mail 1: dispara 5 min após `compra_aprovada`
   - E-mail 2: dispara 48 h após `compra_aprovada`
   - E-mail 3: dispara 168 h (7 dias) após `compra_aprovada`
2. Use merge tags: `{{nome}}`, `{{email}}`, `{{data_compra}}`
3. Configure o cupom `SUBFLOW50` no produto Pro (50% off = R$ 64,90 de R$ 129,90)
