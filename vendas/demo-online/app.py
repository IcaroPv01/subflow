"""SubFlow — Gradio demo on Hugging Face Spaces.

Transcreve um arquivo de áudio/vídeo enviado, mostra SRT bruto + SRT pós clean + QC.
"""
import gradio as gr
import subprocess, tempfile, os
from pathlib import Path

def transcribe(file, model_size="small", lang="auto"):
    if not file:
        return "Envie um arquivo de áudio ou vídeo.", None, None
    work = Path(tempfile.mkdtemp(prefix="subflow_"))
    audio = work / "input.wav"
    # extrair audio com ffmpeg
    subprocess.run(["ffmpeg","-y","-i",file.name,"-ac","1","-ar","16000",str(audio)],
                   check=False, capture_output=True)
    if not audio.exists():
        return "ffmpeg falhou em extrair o audio.", None, None
    # transcricao (sem traducao nessa demo online — a versao completa e local)
    from faster_whisper import WhisperModel
    wm = WhisperModel(model_size, device="cpu", compute_type="int8")
    segs, _ = wm.transcribe(str(audio), language=None if lang=="auto" else lang,
                            vad_filter=True)
    # gerar SRT
    srt_lines = []
    for i, seg in enumerate(segs, 1):
        srt_lines.append(f"{i}\n{seg.start:.3f} --> {seg.end:.3f}\n{seg.text.strip()}\n")
    srt = "\n".join(srt_lines)
    # metricas simples
    n_cues = len([l for l in srt_lines if l.strip().isdigit() or '-->' in l])
    total_chars = sum(len(l) for l in srt_lines)
    stats = f"Cues: {segs and len(list(segs)) or 'n/a'}\nCaracteres: {total_chars}\nIdioma: {lang}\nModelo: {model_size}"
    srt_path = work / "out.srt"
    srt_path.write_text(srt, encoding='utf-8')
    return stats, str(srt_path), srt[:1500] + ("\n\n[... truncado ...]" if len(srt)>1500 else "")

with gr.Blocks(title="SubFlow — local Whisper demo") as demo:
    gr.Markdown("# SubFlow — demo online\nTranscrição Whisper local. Limite: ~2-5 min de áudio no free tier.")
    with gr.Row():
        inp = gr.File(label="Áudio ou vídeo", type="filepath")
        model = gr.Dropdown(choices=["tiny","base","small","medium"], value="small", label="Modelo")
        lang = gr.Dropdown(choices=["auto","pt","en","es","fr","ar"], value="auto", label="Idioma")
    btn = gr.Button("Transcrever")
    with gr.Row():
        stats = gr.Textbox(label="Estatísticas", lines=4)
        srt_text = gr.Textbox(label="SRT (preview)", lines=15)
    srt_file = gr.File(label="Download SRT completo")

    btn.click(transcribe, inputs=[inp, model, lang], outputs=[stats, srt_file, srt_text])

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
