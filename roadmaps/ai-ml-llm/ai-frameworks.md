---
name: AI Frameworks
category: ai-ml-llm
status: researched
last-updated: 2026-07-30
sources:
  - https://blog.langchain.com/langchain-v1/
  - https://langchain-ai.github.io/langgraph/
  - https://www.langchain.com/resources/ai-agent-frameworks
  - https://www.llamaindex.ai/llamaindex
  - https://www.llamaindex.ai/workflows
  - https://www.zenml.io/blog/llamaindex-vs-langchain
  - https://haystack.deepset.ai/
  - https://github.com/deepset-ai/haystack
  - https://dspy.ai/
  - https://mirascope.com/
  - https://github.com/BrainBlend-AI/atomic-agents
  - https://ai.pydantic.dev/
  - https://www.crewai.com/
  - https://github.com/microsoft/autogen
  - https://www.braintrust.dev/articles/best-ai-agent-frameworks-2026
  - https://alicelabs.ai/en/insights/best-ai-agent-frameworks-2026
  - https://pub.towardsai.net/top-ai-agent-frameworks-in-2026-a-production-ready-comparison-7ba5e39ad56d
tags: [langchain, llamaindex, haystack, dspy, pydantic-ai, crewai, autogen, agents, orchestration]
---

# AI Frameworks

## One-liner

Libraries that abstract LLM calls, retrieval, tool-use, and agent loops so you don't glue everything together by hand — the difference between "an afternoon prototype" and "an afternoon of plumbing".

## What It Is

An AI framework sits between your application code and the raw LLM API. It handles the boring but essential parts: prompt templating, output parsing, retry/error handling, tool/function-calling conventions, retrieval orchestration, agent loops, streaming, observability hooks. The 2026 landscape is large but converges into four use-case clusters:

| Cluster | Framework(s) | Best for |
|---------|--------------|----------|
| **General-purpose orchestration** | [LangChain](https://blog.langchain.com/langchain-v1/) + [LangGraph](https://langchain-ai.github.io/langgraph/) | Any LLM app; especially production agents with state, persistence, human-in-the-loop |
| **Retrieval-first** | [LlamaIndex](https://www.llamaindex.ai/llamaindex) + Workflows | RAG-heavy apps; document indexing; agent loops where retrieval is the core job |
| **Pipelines / NLP heritage** | [Haystack](https://haystack.deepset.ai/) (deepset) | Enterprise search; traditional NLP pipelines; large-document ingestion; on-prem |
| **Programmatic / typed** | [DSPy](https://dspy.ai/), [Mirascope](https://mirascope.com/), [PydanticAI](https://ai.pydantic.dev/) | Compile / optimize prompts; strong typing; schema-enforced outputs |
| **Multi-agent collaboration** | [CrewAI](https://www.crewai.com/), [AutoGen](https://github.com/microsoft/autogen), [Atomic Agents](https://github.com/BrainBlend-AI/atomic-agents) | Multi-agent patterns (role-based, conversational, composable) |

The 2024–2026 maturation story:

- **LangChain v1** (Oct 2024) stabilized the API after years of churn. **LangGraph v1.0** became the default for production agents — stateful cyclical graphs, durable execution (pause/resume/recover), human-in-the-loop, LangGraph Studio IDE, LangGraph Platform for managed deploy.
- **LlamaIndex Workflows** (2025) added an event-driven orchestration layer for multi-agent systems in plain Python/TypeScript — no separate DSL.
- **DSPy** matured from research framework to production tool; programmatic prompt compilation and optimization against labeled data.
- **PydanticAI** brought FastAPI-style ergonomics to typed LLM apps.
- **CrewAI, AutoGen, Atomic Agents** each carved a niche in multi-agent patterns (role-play, conversation, atomic composition).

Practitioner consensus in 2026 (per [Braintrust 2026 framework review](https://www.braintrust.dev/articles/best-ai-agent-frameworks-2026), [Alice Labs 2026 ranking](https://alicelabs.ai/en/insights/best-ai-agent-frameworks-2026), [Towards AI 2026 comparison](https://pub.towardsai.net/top-ai-agent-frameworks-in-2026-a-production-ready-comparison-7ba5e39ad56d)):

- **Default pick for production agents**: LangGraph (state, persistence, observability).
- **Default pick for RAG-heavy apps**: LlamaIndex Workflows.
- **Pick for pipeline-heavy enterprise search**: Haystack.
- **Pick for typed / schema-strict outputs**: PydanticAI or DSPy.
- **Pick for multi-agent by role**: CrewAI or AutoGen (still evolving).
- **Pick for "prompts as code" with optimization**: DSPy.

## When To Use It

- **You're shipping anything beyond a single LLM call.** Retries, output parsing, and tool routing are solved problems; don't reinvent them.
- **You need an agent loop** that persists state, survives crashes, and can be human-approved mid-flow → LangGraph.
- **Your app is RAG-centric** with heavy document ingestion and complex retrieval → LlamaIndex Workflows.
- **You want compile-time guarantees on LLM output shape** → PydanticAI (or DSPy for the optimization angle too).
- **You're in enterprise / on-prem / regulated** with traditional NLP heritage → Haystack (deepset's track record + Apache 2.0).
- **You want version-controlled, optimizable prompts** with a labeled dataset → DSPy.

## When NOT To Use It

- **You're calling one LLM once.** Just use the raw SDK. The framework tax (abstractions, learning curve, lock-in) is not worth it.
- **You don't have a clear agent or pipeline structure.** A framework won't save a poorly designed system.
- **You need sub-50ms latency.** Framework overhead is real; for ultra-low-latency paths, bypass the framework and call the API directly.
- **You're on a tiny corpus where naive RAG works.** A framework adds dependency surface for no benefit.
- **You're a one-person prototype.** Pick the simplest framework that fits (often LangChain or LlamaIndex). Don't optimize for hypothetical future scale.
- **You're evaluating DSPy without a labeled dataset.** DSPy's optimization is its whole point — without labels, it's just a heavier version of every other framework.

## Why It Matters in 2026

Three forces make the framework choice more consequential, not less:

1. **Agent production demands persistence and observability.** Pre-2024, "agents" were demos. Post-2024, they're in production at every serious AI company — and the frameworks that solved durable execution, human-in-the-loop, and tracing (LangGraph, LlamaIndex Workflows) are now the default. Hand-rolling these is a multi-month detour.
2. **DSPy / PydanticAI moved prompt engineering from craft to engineering.** Programmatic prompts + type-safe outputs are the biggest quality-and-maintainability win of the last two years. Teams not using them are leaving reliability on the table.
3. **MCP (Model Context Protocol) integration** is becoming table stakes. LangChain, LlamaIndex, PydanticAI all shipped MCP support in 2025; framework choice increasingly hinges on whose MCP integrations you trust.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 80 | LangChain/LlamaIndex/Haystack are 3+ years old and battle-tested; newer entrants (PydanticAI, Atomic Agents) are 1–2 years old. |
| Community | 95 | LangChain alone has more stars, tutorials, blog posts, and Stack Overflow answers than any other LLM library; the ecosystem dwarfs any single competitor. |
| Learning curve | 55 | Each framework has its own mental model (chains, indexes, pipelines, signatures, state graphs); choosing between them is itself a project. |
| Performance | 70 | Framework overhead is measurable (~10–50ms per call, plus abstraction cost). Well-optimized code can approach raw SDK performance but rarely matches it. |
| Cost | 75 | Open-source frameworks are free; you pay in engineering time to learn them, debug abstractions, and stay current with breaking changes. |
| DX (developer experience) | 80 | LangGraph Studio + LangSmith are best-in-class; LlamaIndex Workflows is excellent; PydanticAI is the most Pythonic; DSPy has the steepest curve. |
| Production readiness | 90 | All top frameworks are in production at multiple Fortune 500s. LangGraph Platform, Haystack Enterprise, and LlamaIndex Cloud are managed offerings. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Raw LLM SDK** (openai, anthropic, google-generativeai) | You need maximum control, minimum latency, or are doing something the framework doesn't model well. | You need retries, output parsing, tool routing, agent loops, observability — anything beyond a single call. |
| **Managed agent platforms** (Bedrock Agents, Vertex AI Agent Builder, Azure AI Agent Service) | You're already all-in on one cloud and want zero-ops agent hosting. | You need portability, custom logic, or are deploying on multiple clouds / on-prem. |
| **No-code / low-code agent builders** (n8n, Langflow, Flowise) | You're not a developer or you're prototyping a workflow quickly. | You need version control, testing, type safety, or production hardening. |
| **Hand-rolled orchestration** | You have a very specific architecture no framework supports, and the cost of locking into one is too high. | You're rebuilding a worse version of LangGraph. Stop. |
| **DSPy specifically** | You have labeled training data and want to compile / optimize prompts. | You're prototyping and don't have labels yet. |

## Sources

- [LangChain Blog — LangChain v1](https://blog.langchain.com/langchain-v1/) — 2024-10
- [LangGraph Docs](https://langchain-ai.github.io/langgraph/) — 2026
- [LangChain — AI Agent Frameworks Resource](https://www.langchain.com/resources/ai-agent-frameworks) — 2026
- [LlamaIndex — Official](https://www.llamaindex.ai/llamaindex) — 2026
- [LlamaIndex — Workflows](https://www.llamaindex.ai/workflows) — 2026
- [ZenML — LlamaIndex vs LangChain](https://www.zenml.io/blog/llamaindex-vs-langchain) — 2025-09
- [Haystack (deepset)](https://haystack.deepset.ai/) — 2026
- [Haystack GitHub](https://github.com/deepset-ai/haystack) — 2026
- [DSPy — Official Site](https://dspy.ai/) — 2026
- [Mirascope](https://mirascope.com/) — 2026
- [Atomic Agents GitHub (BrainBlend AI)](https://github.com/BrainBlend-AI/atomic-agents) — 2025+
- [PydanticAI](https://ai.pydantic.dev/) — 2026
- [CrewAI](https://www.crewai.com/) — 2026
- [AutoGen GitHub (Microsoft)](https://github.com/microsoft/autogen) — 2026
- [Braintrust — Best AI agent frameworks 2026](https://www.braintrust.dev/articles/best-ai-agent-frameworks-2026) — 2026-07
- [Alice Labs — Best AI Agent Frameworks 2026](https://alicelabs.ai/en/insights/best-ai-agent-frameworks-2026) — 2026-04
- [Towards AI — Top AI Agent Frameworks 2026](https://pub.towardsai.net/top-ai-agent-frameworks-in-2026-a-production-ready-comparison-7ba5e39ad56d) — 2026-04