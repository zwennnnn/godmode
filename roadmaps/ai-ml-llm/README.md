---
name: AI/ML/LLM Engineer
slug: ai-ml-llm
source: https://roadmap.sh/ai-ml-llm-engineer
last-updated: 2026-07-30
tech-count: 12
status: researched
---

# AI/ML/LLM Engineer Roadmap

> **Category:** Technologies for building production AI/ML systems — with focus on LLM-powered applications in 2026.
> **Source:** [roadmap.sh/ai-ml-llm-engineer](https://roadmap.sh/ai-ml-llm-engineer)

This roadmap covers the core stack for an engineer who ships AI features: prompt design, retrieval, fine-tuning, evaluation, frameworks, agent design, ops, multimodal, and safety. All 12 technologies below are researched, scored, and sourced (see each file's frontmatter for `last-updated` and `sources`).

---

## Technologies (all researched 2026-07-30)

| # | Technology | File | Status |
|---|-----------|------|--------|
| 1 | Prompt Engineering | [prompt-engineering.md](prompt-engineering.md) | researched |
| 2 | RAG Architectures | [rag-architectures.md](rag-architectures.md) | researched |
| 3 | Vector Databases | [vector-databases.md](vector-databases.md) | researched |
| 4 | Embeddings | [embeddings.md](embeddings.md) | researched |
| 5 | AI Frameworks | [ai-frameworks.md](ai-frameworks.md) | researched |
| 6 | Agent Design | [agent-design.md](agent-design.md) | researched |
| 7 | Fine-Tuning LLMs | [fine-tuning-llms.md](fine-tuning-llms.md) | researched |
| 8 | Model Evaluation | [model-evaluation.md](model-evaluation.md) | researched |
| 9 | LLM Ops (LLMOps) | [llm-ops.md](llm-ops.md) | researched |
| 10 | Multimodal Models | [multimodal-models.md](multimodal-models.md) | researched |
| 11 | Speech & Vision | [speech-and-vision.md](speech-and-vision.md) | researched |
| 12 | AI Safety & Alignment | [ai-safety-alignment.md](ai-safety-alignment.md) | researched |

---

## Quick Decision Guide

### If you're building an LLM-powered SaaS in MVP / speed mode

The minimal viable stack:

1. **Prompt engineering** — invest first; high ROI, free.
2. **Embeddings** — pick one (`text-embedding-3-large`, `voyage-3`, or open `Qwen3-Embedding-4B`).
3. **Vector database** — pgvector (if small, on Postgres) or Pinecone/Qdrant (if you want zero-ops).
4. **RAG** — naive → Advanced (with reranking); only escalate to Hybrid/Agentic when quality demands it.
5. **AI framework** — LangChain or LlamaIndex if you want batteries-included; raw SDK if you're a solo dev.
6. **LLM Ops** — at minimum: log every call, track cost + latency, prompt-cache if you have repetitive prompts.
7. **Model evaluation** — 100-case golden dataset + RAGAS for RAG.

Don't reach for fine-tuning, agent design, multimodal, or speech until the above is solid.

### If you're going to production / scale

Add:

- **Fine-tuning** only if you have labeled data and a measurable eval; small model (GPT-4o-mini / Llama) fine-tuned often beats prompted large model at 1/10 the cost.
- **Agent design** only if you actually need tool use / multi-step reasoning; MCP is the standard for tools now.
- **Model evaluation** — deep. RAGAS, LLM-as-judge (G-Eval), trajectory evals for agents.
- **LLM Ops** — full stack: Langfuse or Helicone for tracing, semantic cache, online evals, cost alerts.
- **Multimodal / speech** if your product needs images/audio/video/PDFs.
- **AI Safety** — guardrails (Lakera / NeMo), red-teaming against OWASP Top 10.

### If you're in research / experimental mode

- Local models (Llama 3.x, Qwen) via vLLM or Ollama.
- Custom fine-tuning with TRL + Unsloth.
- Custom evals — don't trust public benchmarks for niche tasks.
- DSPy for programmatic prompt optimization.
- Open-source embeddings (bge, NV-Embed, Qwen3-Embedding).

---

## Cross-references

- If the project also needs a web UI, see [`../frontend-backend/README.md`](../frontend-backend/README.md) (Phase 3).
- If the project needs cloud deployment, see [`../devops-cloud/README.md`](../devops-cloud/README.md) (Phase 4).
- If the project is a mobile AI app, see [`../mobile/README.md`](../mobile/README.md) (Phase 5).

---

## Build progress

**Phase 2 complete** as of 2026-07-30. See [`../godmode.md`](../godmode.md) under `## Progress Tracker`. Next: Phase 3 (frontend-backend roadmap).