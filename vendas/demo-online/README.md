# SubFlow — Hugging Face Space (Gradio UI)

Demo online 100% gratuita, rodando o SubFlow dentro do Space (CPU, modelos Whisper small).

## Estrutura
```
demo-online/
  app.py              # Gradio UI (upload de vídeo/áudio, transcrição + clean + QC)
  requirements.txt    # gradio, faster-whisper, yt-dlp, ffmpeg
  README.md           # este
```

## Como publicar (passos para a instância)
1. Criar Space em huggingface.co/new-space (SDK: Gradio, hardware: CPU basic — free)
2. Subir estes 3 arquivos via interface web ou `huggingface-cli upload`
3. O Space demora ~3 min para buildar (instala faster-whisper ~460 MB)
4. URL pública: `huggingface.co/spaces/IcaroPv01/subflow-demo`

## Limitações conhecidas
- CPU basic = modelos small/medium apenas (large-v2 fica pesado)
- Timeout 5 min em vídeos longos (free tier) — chunkear em clipes de 2-5 min
- Memória 16 GB (modelo medium cabe)
