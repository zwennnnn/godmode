---
name: RAG Architectures
category: ai-ml-llm
status: researched
last-updated: 2026-07-30
sources:
  - https://www.ibm.com/think/topics/retrieval-augmented-generation
  - https://www.meilisearch.com/blog/rag-types
  - https://www.puppygraph.com/blog/rag-techniques
  - https://www.premai.io/blog/advanced-rag-methods-simple-hybrid-agentic-graph-explained/
  - https://medium.com/@Micheal-Lanham/pipeline-rag-vs-agentic-rag-vs-knowledge-graph-rag-what-actually-works-and-when-47a26649a457
  - https://arxiv.org/html/2508.05660v1
  - https://docs.ragas.io/en/latest/concepts/metrics/index.html
  - https://docs.ragas.io/en/latest/concepts/metrics/context_precision.html
  - https://docs.ragas.io/en/latest/concepts/metrics/faithfulness.html
  - https://arxiv.org/abs/2309.15217
  - https://github.com/explodinggradients/ragas
  - https://www.zenml.com/llmops/langchain-vs-haystack-vs-llamaindex
  - https://www.confident-ai.com/blog/comparing-3-llm-frameworks-langchain-vs-haystack-vs-llamaindex
  - https://www.datalead.ai/blog/rag-framework-benchmarks-2026
tags: [rag, retrieval, vector-search, hybrid-search, agentic-rag, graphrag, evaluation]
---

# RAG Architectures

## One-liner

Patterns for retrieving external knowledge at inference time and feeding it to an LLM as context — the de-facto way to keep LLMs factual, fresh, and grounded.

## What It Is

Retrieval-Augmented Generation (RAG) is an architecture, not a single product: at query time, you **retrieve** relevant snippets from an external knowledge base, **augment** the prompt with those snippets, and let the LLM **generate** an answer grounded in them. The model itself stays frozen; only the retrieval index changes.

The discipline has matured from "naive vector search + prompt" into a family of distinct patterns, each with different cost / accuracy / complexity trade-offs ([Meilisearch lists 14 variants](https://www.meilisearch.com/blog/rag-types); [PuppyGraph groups them into 7](https://www.puppygraph.com/blog/rag-techniques)). The most important distinctions in 2026:

| Pattern | Mental model | Strength | Weakness |
|---------|--------------|----------|----------|
| **Naïve / Standard RAG** | embed query → top-k vectors → stuff into prompt | dead simple; works on small corpora | brittle on multi-hop or out-of-distribution queries |
| **Advanced RAG** | + pre-retrieval (rewriting, HyDE) and post-retrieval (reranking, compression) | big quality lift for modest complexity | more moving parts to tune |
| **Hybrid RAG** | combine BM25 / keyword + vector + (optionally) graph | best for heterogeneous enterprise data | ranking fusion is its own art |
| **GraphRAG** | use a knowledge graph for entity/relationship retrieval | excels at multi-hop reasoning over connected data | graph construction cost; doesn't fit unstructured corpora |
| **Multi-hop RAG** | decompose question → retrieve per sub-question → synthesize | investigative research, troubleshooting | latency; failure modes compound |
| **Agentic RAG** | LLM agent decides *if*, *when*, *what* to retrieve; can call tools | open-ended tasks; real-time data | harder to evaluate; cost unpredictable |
| **Adaptive / Iterative RAG** | judge component decides whether to re-retrieve | self-correcting; data drift | extra LLM calls per query |

The 2026 frontier is **Hybrid Agentic RAG** ([arXiv 2508.05660](https://arxiv.org/html/2508.05660v1) — Open-Source Agentic Hybrid RAG Framework, Aug 2025): a graph + vector fusion under an agentic control loop, replacing fixed pipelines with query-adaptive orchestration.

Evaluation has its own stack now — most teams use [RAGAS](https://docs.ragas.io/en/latest/concepts/metrics/index.html) (faithfulness, context precision, context recall, answer relevancy, answer correctness) as the standard metric suite, with [BEIR](https://github.com/beir-cellar/beir) for retrieval-quality benchmarking at the index layer.

## When To Use It

- **Your LLM needs facts it wasn't trained on** — proprietary docs, fresh news, internal knowledge bases. This is the default choice for ~70% of production LLM apps in 2026.
- **Your knowledge base updates frequently** — RAG refreshes on the next index rebuild; fine-tuning requires retraining.
- **You need auditable answers** — you can show the user the retrieved snippets, not just the LLM's output.
- **You're building customer support / internal Q&A / research assistants** — all canonical RAG use cases.
- **You're in MVP mode** — naïve RAG is fast to ship; you can graduate to Advanced → Hybrid → Agentic as quality demands rise.
- **You need to comply with "show your work"** — retrieved context is a natural citation mechanism.

## When NOT To Use It

- **The model already knows the answer.** Don't retrieve common knowledge.
- **Your data is purely structural and the model just needs to follow a fixed format.** Use function calls / structured output, not RAG.
- **Latency budget is sub-100ms.** Even naïve RAG adds 200–800ms; agentic RAG can blow past 5s.
- **You need to teach a new skill or style.** RAG retrieves facts, not skills — use fine-tuning or DSPy for behavior changes.
- **Your corpus is tiny (<100 docs) and fits in the model's context window.** Just paste it.
- **You haven't instrumented retrieval quality yet.** A RAG system without retrieval-quality metrics is a coin flip — instrument first with RAGAS.

## Why It Matters in 2026

Three forces keep RAG at the center of production AI:

1. **It's the cheapest path to fresh, factual answers.** Fine-tuning for knowledge costs GPU-hours and drifts; RAG re-indexes in minutes and stays current.
2. **It composes with everything.** RAG + function calling, RAG + agents, RAG + structured output, RAG + GraphRAG — RAG is the *base layer* that other patterns sit on top of.
3. **The evaluation stack caught up.** [RAGAS](https://docs.ragas.io/en/latest/concepts/metrics/index.html) (introduced 2023, widely adopted by 2025) and [BEIR](https://github.com/beir-cellar/beir) for retrieval mean you can now *measure* RAG quality the same way you measure any ML system. Pre-RAGAS, RAG was vibes.

Practitioner consensus in 2026 ([ZenML framework comparison Jan 2026](https://www.zenml.com/llmops/langchain-vs-haystack-vs-llamaindex), [DataLead 2026 benchmarks](https://www.datalead.ai/blog/rag-framework-benchmarks-2026), [Confident AI comparison Feb 2026](https://www.confident-ai.com/blog/comparing-3-llm-frameworks-langchain-vs-haystack-vs-llamaindex)):

- **Naïve RAG** is a learning toy; production starts at **Advanced RAG** (with reranking).
- **Hybrid** (BM25 + vector) wins on heterogeneous enterprise data — pure-vector loses on keyword-heavy or exact-match queries.
- **GraphRAG** is the right answer when relationships matter (fraud, supply chain, org charts) and the wrong answer for prose corpora.
- **Agentic RAG** is the new ceiling for quality but the new floor for cost — use only when quality > cost.
- **Hybrid Agentic** is the 2026 emerging winner for high-stakes, multi-source tasks.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 85 | In production since 2023 (ChatGPT retrieval plugin era); now standard in most LLM backends. |
| Community | 95 | Universal — every LLM vendor ships a RAG cookbook; entire framework ecosystem (LangChain, LlamaIndex, Haystack, Verba) is built around it. |
| Learning curve | 60 | Naïve RAG fits in a weekend; Advanced/Hybrid is weeks; Agentic + GraphRAG is months and requires eval-driven iteration. |
| Performance | 85 | Measurably outperforms no-RAG and fine-tuning-on-facts on factual QA benchmarks (RAGAS, BEIR). Hybrid > pure vector on enterprise data. |
| Cost | 75 | Vector DB + embedding + reranker + LLM cost; cheaper than fine-tuning but non-trivial at scale. Agentic RAG can 5–10× naive cost. |
| DX (developer experience) | 80 | Many frameworks (LangChain, LlamaIndex, Haystack, DSPy, Verba); managed services (Vertex AI Search, Bedrock Knowledge Bases, Azure AI Search). |
| Production readiness | 90 | Most LLM-backed products shipped in 2025–2026 use RAG. Evaluated via RAGAS or similar in CI. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Fine-tuning** | You need the model to *behave* differently (style, skill, format), not know different facts. | The knowledge changes weekly; you can't afford retraining cycles. |
| **Long-context models (1M+ tokens)** | Your entire corpus fits in the context window and queries need global reasoning across it (e.g. codebase Q&A over a small repo). | Your corpus is larger than context, or you need to filter for relevance (RAG wins on cost + accuracy). |
| **DSPy / programmatic pipelines** | You want version-controlled, optimizable retrieval + generation pipelines; you have evaluation data. | You're still prototyping and don't have labels yet. |
| **Knowledge base + function calling** | The answer is a lookup against a structured API (CRUD on a record). | The answer requires synthesizing across multiple unstructured docs. |
| **Web search / Browse tools** | Your knowledge base is the open web and freshness beats accuracy. | You need provable provenance or internal-only sources. |

## Sources

- [IBM — What is RAG?](https://www.ibm.com/think/topics/retrieval-augmented-generation) — 2026
- [Meilisearch — 14 types of RAG](https://www.meilisearch.com/blog/rag-types) — 2025
- [PuppyGraph — 7 Types of RAG Techniques Explained](https://www.puppygraph.com/blog/rag-techniques) — 2026-02
- [Premai — Advanced RAG Methods: Simple, Hybrid, Agentic, Graph](https://www.premai.io/blog/advanced-rag-methods-simple-hybrid-agentic-graph-explained/) — 2025
- [Medium — Pipeline RAG vs Agentic RAG vs Knowledge Graph RAG](https://medium.com/@Micheal-Lanham/pipeline-rag-vs-agentic-rag-vs-knowledge-graph-rag-what-actually-works-and-when-47a26649a457) — 2025
- [arXiv 2508.05660 — Open-Source Agentic Hybrid RAG Framework](https://arxiv.org/html/2508.05660v1) — 2025-08
- [RAGAS Docs — Metrics Index](https://docs.ragas.io/en/latest/concepts/metrics/index.html) — 2026
- [RAGAS Docs — Context Precision](https://docs.ragas.io/en/latest/concepts/metrics/context_precision.html) — 2026
- [RAGAS Docs — Faithfulness](https://docs.ragas.io/en/latest/concepts/metrics/faithfulness.html) — 2026
- [arXiv 2309.15217 — RAGAS: Automated Evaluation of RAG](https://arxiv.org/abs/2309.15217) — 2023
- [RAGAS GitHub](https://github.com/explodinggradients/ragas) — 2026
- [ZenML — LangChain vs Haystack vs LlamaIndex](https://www.zenml.com/llmops/langchain-vs-haystack-vs-llamaindex) — 2026-01
- [Confident AI — Comparing 3 LLM Frameworks](https://www.confident-ai.com/blog/comparing-3-llm-frameworks-langchain-vs-haystack-vs-llamaindex) — 2026-02
- [DataLead — RAG Framework Benchmarks 2026](https://www.datalead.ai/blog/rag-framework-benchmarks-2026) — 2026-03