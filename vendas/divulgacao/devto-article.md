# How I built a 100% local subtitle pipeline with Whisper

*By Icaro Venzon — the story behind [SubFlow](https://github.com/IcaroPv01/subflow), an MIT-licensed CLI + Claude Code skill that turns any video into clean, translated subtitles, fully offline.*

---

## The problem: subtitling is 4–8× the runtime of the video

I translate documentaries into Brazilian Portuguese. For years, the workflow was the same painful loop: transcribe the audio (4–8× the video length), sync the timestamps, translate, then run quality control by hand — checking line lengths, reading speed, overlaps. A 104-minute film meant roughly 14 hours of work, most of it mechanical.

In 2024 I started automating. The result is **SubFlow**: a single command that takes a video URL or file and produces a clean, translated SRT — with Netflix-style QC built in.

```
subflow run https://youtu.be/... --src-lang fr --tgt-lang pt
```

## The pipeline

```
download → transcribe (Whisper, local) → glossary → batch translate → build → clean → QC → langcheck
```

Everything runs locally. No per-minute API cost, no uploading your footage anywhere.

### 1. Transcription with Whisper

SubFlow uses `faster-whisper` (or the standalone binary) with a VAD filter to skip silence. The default model is `large-v2` with `int8_float16` quantization — which is what makes it run on a modest 4 GB laptop GPU without quality loss. A forced-language pass keeps the transcription consistent when the source is known.

### 2. Glossary first

Before translating, SubFlow builds a glossary of proper nouns (people, places, organizations) so every name appears identically across the whole file. For a documentary about the Western Sahara, that's the difference between "Polisario" appearing five different ways and one consistent way.

### 3. Translation stays text-only

This is the design decision I'm proudest of: **the AI never touches the timestamps**. Translation happens in batches of ~30 cues as plain text files, keyed by cue number. A small script then rebuilds the SRT by matching translated text back to the original timing. Zero risk of desync — the most common failure mode in AI subtitling is eliminated by construction.

### 4. QC, automated

The `qc` subcommand checks every cue against a Netflix-style profile:

- ≤42 characters per line, ≤2 lines
- Reading speed: CPS 17 (warn) / 20 (error)
- No overlaps, minimum 1 s duration

It writes a report listing every violation by cue number. The `clean` subcommand then fixes what can be fixed automatically: merging cues split mid-sentence and extending cue ends into silence to bring reading speed into range.

### 5. langcheck: catching ASR hallucination

The most interesting bug I hit: forcing Whisper to transcribe in French, it once "invented" plausible French lyrics over a Hassaniya Arabic song — a classic ASR hallucination. `langcheck` re-decodes each cue and compares the detected language against the expected one, flagging cues where the model drifted. It's a cheap, targeted guard against the subtlest failure mode of speech-to-text.

## The numbers

A 104-minute documentary that took ~14 h manually now takes **~7 h 50 min** end-to-end with SubFlow — same quality, with a QC report that says so. The remaining time is mostly the human pass: watching the film and fine-tuning reading comfort, which is genuinely hard to automate.

## Why open source

The tool is MIT-licensed, Python stdlib only (plus faster-whisper or the standalone binary). No lock-in, no SaaS account, no watermark. You can read every line of the pipeline.

If you subtitle anything — films, lectures, podcasts — the free 9-section guide (PT-BR) covers the full professional workflow: [guia-legendagem-profissional-pt-br.pdf](https://raw.githubusercontent.com/IcaroPv01/subflow/main/vendas/isca/guia-legendagem-profissional-pt-br.pdf)

**Repo:** [github.com/IcaroPv01/subflow](https://github.com/IcaroPv01/subflow)

*Feedback welcome — especially on QC defaults, translation batch size, and the langcheck heuristic.*