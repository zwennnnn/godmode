---
name: Speech and Vision
category: ai-ml-llm
status: researched
last-updated: 2026-07-30
sources:
  - https://openai.com/research/whisper
  - https://github.com/openai/whisper
  - https://platform.openai.com/docs/guides/speech-to-text
  - https://platform.openai.com/docs/guides/text-to-speech
  - https://elevenlabs.io/
  - https://cartesia.ai/
  - https://github.com/neonbjb/tortoise-tts
  - https://github.com/coqui-ai/TTS
  - https://github.com/yl4579/StyleTTS2
  - https://github.com/RVC-Boss/GPT-SoVITS
  - https://github.com/anthropics/claude-cookbooks
  - https://pytorch.org/vision/stable/models.html
  - https://github.com/facebookresearch/segment-anything
  - https://github.com/ultralytics/ultralytics
  - https://github.com/roboflow/supervision
  - https://docs.aws.amazon.com/rekognition/
  - https://cloud.google.com/vision
  - https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/
tags: [speech, stt, tts, whisper, elevenlabs, cartesia, tortoise, vision, object-detection, segmentation, ocr, aws-rekognition]
---

# Speech and Vision

## One-liner

Specialized models and pipelines for **speech** (speech-to-text, text-to-speech, voice cloning, real-time conversation) and **classical computer vision** (object detection, segmentation, OCR, image classification) — the layer below multimodal LLMs.

## What It Is

This category covers two distinct sub-domains that sit *adjacent* to multimodal LLMs:

### A) Speech
1. **Speech-to-Text (STT / ASR)** — audio → text. Used for transcription, voice commands, call analytics, captioning.
2. **Text-to-Speech (TTS)** — text → audio. Used for voice assistants, audiobooks, video narration, accessibility.
3. **Voice cloning** — clone a specific voice from a short sample; used for personalization, dubbing, brand voice.
4. **Real-time speech-to-speech** — full duplex conversation; used in voice agents.

### B) Classical Computer Vision
Tasks that predate VLMs and still win on cost/latency for narrow use cases:
- **Image classification** — what's in this image?
- **Object detection** — YOLO, DETR, RT-DETR — bounding boxes around objects.
- **Instance segmentation** — pixel-perfect masks (Segment Anything, Mask R-CNN).
- **OCR** — text extraction from images (Tesseract, AWS Textract, Google Document AI).
- **Face recognition** — FaceNet, ArcFace.
- **Pose estimation** — OpenPose, MediaPipe.
- **Depth estimation** — MiDaS, Depth Anything.
- **Image generation** — Stable Diffusion, FLUX, Midjourney, DALL-E (out of scope here; see separate roadmap).

## Speech — Tools in 2026

### STT (Speech-to-Text)

| Tool | Notes |
|------|-------|
| **[OpenAI Whisper](https://github.com/openai/whisper)** | Open-source; multilingual; runs locally; large-v3 / turbo variants. |
| **Whisper API** (OpenAI) | Managed Whisper; easy; pricing per minute. |
| **OpenAI GPT-4o transcribe** | Newer; better accuracy on noisy audio; more expensive. |
| **Deepgram** | Real-time STT; very low latency; good for voice agents. |
| **AssemblyAI** | Production STT with diarization, sentiment. |
| **Azure Speech** / **AWS Transcribe** / **Google STT** | Cloud-managed; enterprise compliance. |

### TTS (Text-to-Speech)

| Tool | Notes |
|------|-------|
| **[ElevenLabs](https://elevenlabs.io/)** | Industry leader on naturalness + voice cloning; Eleven Multilingual v2 / Turbo. |
| **[Cartesia](https://cartesia.ai/)** | Ultra-low-latency Sonic / Ink models; popular for real-time agents. |
| **[OpenAI TTS](https://platform.openai.com/docs/guides/text-to-speech)** | Managed; high quality; tts-1 / tts-1-hd. |
| **Google Cloud TTS / Azure TTS** | Enterprise; many languages. |
| **Open-source**: [Tortoise TTS](https://github.com/neonbjb/tortoise-tts), [Coqui TTS](https://github.com/coqui-ai/TTS), [StyleTTS 2](https://github.com/yl4579/StyleTTS2), [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) | Self-hostable; quality varies; great for customization. |

### Real-time voice agents
Combine STT (Deepgram / Whisper streaming) + LLM + TTS (Cartesia / ElevenLabs streaming) + a turn-taking model (like [LiveKit](https://livekit.io/) or [Pipecat](https://github.com/pipecat-ai/pipecat)). GPT-4o native audio in/out is the simplest path.

## Vision — Tools in 2026

| Tool | Notes |
|------|-------|
| **Object detection** | [YOLO v11/v12 (Ultralytics)](https://github.com/ultralytics/ultralytics), RT-DETR, DINO |
| **Segmentation** | [Segment Anything 2 (SAM 2)](https://github.com/facebookresearch/segment-anything) — Meta's foundation segmentation model |
| **OCR** | [Tesseract](https://github.com/tesseract-ocr/tesseract) (open-source), AWS Textract, Google Document AI, Azure CV |
| **Classification** | torchvision models, HuggingFace timm, EfficientNet, ConvNeXt |
| **Managed CV APIs** | [AWS Rekognition](https://docs.aws.amazon.com/rekognition/), [Google Cloud Vision](https://cloud.google.com/vision), [Azure Computer Vision](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/) — detection, OCR, moderation, labels |
| **Pipelines** | [Roboflow Supervision](https://github.com/roboflow/supervision) — CV pipeline library |

## When To Use It

### Speech
- **You're building voice agents / IVR / call centers** → STT + LLM + TTS pipeline, or GPT-4o native audio.
- **You need meeting/call transcription** → Whisper, Deepgram, or AssemblyAI.
- **You need accessible audio content** (audiobooks, video narration) → ElevenLabs or OpenAI TTS.
- **You need multilingual voice** → ElevenLabs Multilingual v2, or per-language TTS.
- **You need on-device STT (privacy, latency)** → Whisper large-v3-turbo or Distil-Whisper.

### Vision
- **You need real-time object detection** (security, retail analytics, sports) → YOLO or RT-DETR.
- **You need pixel-perfect segmentation** (image editing, medical imaging) → SAM 2.
- **You need high-volume OCR at low cost** → AWS Textract, Google Document AI, or Tesseract.
- **You need image classification** with a known fixed label set → fine-tuned ResNet/EfficientNet/ConvNeXt beats a VLM.
- **You need to label training data** → SAM 2 + Roboflow.
- **You need to detect faces / moderate content** → AWS Rekognition / Google Vision / Azure CV.

## When NOT To Use It

### Speech
- **You only need text-to-text understanding** — skip the audio round-trip.
- **Latency budget is <500ms for full-duplex conversation** — even the best pipelines are 600–1500ms; GPT-4o native audio is closer.
- **You need 100% accurate transcription of domain jargon** (medical, legal) — fine-tune Whisper on your domain.
- **Tortoise TTS for real-time** — Tortoise is high-quality but slow (~10× real-time). Use Cartesia or ElevenLabs.

### Vision
- **You need language reasoning about images** — use a VLM (see `multimodal-models.md`).
- **You need a single model that handles many vision tasks** — VLMs replace CV pipelines for general use.
- **You need to recognize thousands of classes from natural-language descriptions** — VLMs again.

## Why It Matters in 2026

Three forces:

1. **Real-time voice agents shipped to production.** 2024–2025 was the year of "voice agent demos." 2026 is the year of "voice agents in production at call centers, sales, support" — with sub-second latency, interruption handling, and tool use. The STT/TTS quality bar is now "indistinguishable from human" for many use cases.
2. **VLMs didn't kill classical CV.** For narrow, high-volume, low-latency tasks (OCR, detection, segmentation), dedicated CV models are still 10–100× cheaper and faster than VLMs. The smart play is hybrid: VLM for reasoning, CV pipeline for the heavy lifting.
3. **Speech models are fully commoditized on the open-source side.** Whisper, Coqui TTS, StyleTTS 2, and Tortoise are all production-usable. Closed APIs win on quality and latency; open-source wins on cost and privacy.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 90 | Whisper (2022), YOLO (2015), Tesseract (1980s but constantly updated), TTS wave after GPT-SoVITS / StyleTTS 2 — decades of production use. |
| Community | 95 | Whisper, YOLO, Segment Anything, Tesseract — all have massive communities and ecosystems. |
| Learning curve | 70 | API is straightforward; tuning, deploying at scale, fine-tuning on custom data takes real work. |
| Performance | 90 | Frontier STT/TTS reaches human parity on many benchmarks; modern detection/segmentation exceeds human accuracy on standard tasks. |
| Cost | 75 | Open-source is free; managed APIs are cheap; GPU for self-host is non-trivial. |
| DX (developer experience) | 85 | Excellent libraries (transformers, ultralytics, supervision); managed APIs are one-liners. |
| Production readiness | 95 | Battle-tested at every scale; classical CV is the most reliable ML in production. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Multimodal LLMs** (see `multimodal-models.md`) | You need language reasoning about images / documents. | You need high-throughput, low-latency, narrow vision tasks. |
| **Specialized enterprise APIs** (Textract, Rekognition, Document AI) | High-volume, compliance-heavy, no in-house ML team. | You want customization, on-prem, or low cost. |
| **Open-source models** | Privacy, cost, customization, offline. | You need a polished UI / SLA / support. |
| **Human-in-the-loop** | High-stakes, low-volume (medical, legal). | Anything time-sensitive or high-volume. |
| **Native audio models** (GPT-4o audio) | Real-time voice-to-voice; simplest integration. | You need fine control over voice, language, latency, or cost. |

## Sources

- [OpenAI — Whisper Research](https://openai.com/research/whisper) — 2026
- [OpenAI Whisper GitHub](https://github.com/openai/whisper) — 2026
- [OpenAI Platform — Speech-to-Text Guide](https://platform.openai.com/docs/guides/speech-to-text) — 2026
- [OpenAI Platform — Text-to-Speech Guide](https://platform.openai.com/docs/guides/text-to-speech) — 2026
- [ElevenLabs](https://elevenlabs.io/) — 2026
- [Cartesia](https://cartesia.ai/) — 2026
- [Tortoise TTS GitHub](https://github.com/neonbjb/tortoise-tts) — 2026
- [Coqui TTS GitHub](https://github.com/coqui-ai/TTS) — 2026
- [StyleTTS 2 GitHub](https://github.com/yl4579/StyleTTS2) — 2026
- [GPT-SoVITS GitHub](https://github.com/RVC-Boss/GPT-SoVITS) — 2026
- [Anthropic Claude Cookbooks (multimodal examples)](https://github.com/anthropics/claude-cookbooks) — 2026
- [PyTorch Vision Models](https://pytorch.org/vision/stable/models.html) — 2026
- [Segment Anything GitHub (Meta)](https://github.com/facebookresearch/segment-anything) — 2026
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) — 2026
- [Roboflow Supervision](https://github.com/roboflow/supervision) — 2026
- [AWS Rekognition Docs](https://docs.aws.amazon.com/rekognition/) — 2026
- [Google Cloud Vision](https://cloud.google.com/vision) — 2026
- [Azure Computer Vision](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/) — 2026