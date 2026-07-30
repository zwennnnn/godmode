---
name: Agent Design
category: ai-ml-llm
status: researched
last-updated: 2026-07-30
sources:
  - https://www.anthropic.com/engineering/building-effective-agents
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
  - https://openai.com/index/a-practical-guide-to-building-agents/
  - https://modelcontextprotocol.io/specification/2026-07-28/server/tools
  - https://blog.modelcontextprotocol.io/posts/2026-07-28/
  - https://www.contextstudios.ai/blog/mcp-ecosystem-in-2026-what-the-v127-release-actually-tells-us
  - https://medium.com/@anandtopu/the-future-of-mcp-how-agents-get-connected-in-2026-ee24d62c0c43
  - https://levelup.gitconnected.com/model-context-protocol-explained-why-every-ai-developer-needs-to-know-mcp-in-2026-bf0ed0d1f845
  - https://arxiv.org/abs/2210.03629
  - https://www.promptingguide.ai/techniques/react
  - https://lilianweng.github.io/posts/2023-06-23-agent/
  - https://www.braintrust.dev/articles/best-ai-agent-frameworks-2026
tags: [agents, react, tool-use, mcp, planning, routing, reflection, anthropic, openai]
---

# Agent Design

## One-liner

Architectural patterns for LLM systems that autonomously decide *what to do next* — when to call a tool, when to ask the user, when to plan, when to stop.

## What It Is

An AI agent is an LLM-driven loop that interleaves **reasoning** and **acting** against external tools, data, and APIs until it reaches a goal. Unlike a single-turn RAG call (fixed pipeline), an agent chooses its own path: it can query a database, browse the web, write code, run it, see the output, and iterate.

The 2024–2026 maturation has produced a small, well-understood taxonomy of patterns (synthesized from [Anthropic's *Building Effective Agents*](https://www.anthropic.com/engineering/building-effective-agents) (2024, updated 2025), [OpenAI's *A Practical Guide to Building Agents*](https://openai.com/index/a-practical-guide-to-building-agents/) (2025), and [Lilian Weng's foundational post](https://lilianweng.github.io/posts/2023-06-23-agent/)):

| Pattern | Mental model | When to use | When NOT to use |
|---------|--------------|-------------|-----------------|
| **Reflection / Self-critique** | Generate → critique → revise | Code gen, long-form writing, anything where the model can judge its own output | Fast retrieval paths; the critique step adds latency with no quality gain |
| **Tool-use (single-step)** | LLM decides one tool call, returns result | Structured data lookups, API calls, when the answer is a single retrieval | Multi-step problems requiring several dependent calls |
| **ReAct (Reason + Act)** | Interleave reasoning + tool calls; observe result, continue | Multi-step research, debugging, anything where the next step depends on the last | Tasks with no observable feedback; tight latency budgets |
| **Plan-and-Execute** | Planner LLM decomposes goal into subtasks; executor runs them | Multi-step workflows >5 steps, decomposable problems | Real-time decisions where the plan can't be known in advance |
| **Routing / Orchestrator-Worker** | Classifier routes request to a specialized agent or tool | Mixed-domain requests; multi-agent systems; >20 tools | Single-purpose apps; the routing overhead exceeds the savings |
| **Multi-agent collaboration** | Multiple agents with different roles (CrewAI, AutoGen) | Complex tasks needing distinct expertise/personas | Adds coordination overhead; only worth it when roles are clearly distinct |
| **Computer use / GUI agents** | LLM controls a browser/OS via screenshots/clicks | Workflows without APIs; legacy systems | Anything with a clean API; high-stakes workflows |

The protocol layer under all of this in 2026 is **MCP — Model Context Protocol** ([spec 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/server/tools), [release blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/)). MCP is to tool-use what HTTP is to web requests: an open standard, originally developed by Anthropic, that standardizes how agents *discover, describe, and invoke* tools across vendors. The 2026-07-28 spec is "a major step toward making agent infrastructure work like the rest of the web: stateless, cacheable, routable" ([Context Studios analysis](https://www.contextstudios.ai/blog/mcp-ecosystem-in-2026-what-the-v127-release-actually-tells-us)).

Anthropic's 2025 best practices (cross-referenced with OpenAI's guide):
- Tools are **APIs**: invest in JSON schemas, structured errors, idempotency.
- Keep **tool counts manageable** (≤10–20 per agent); beyond that, route via sub-agent.
- **Sandbox tool execution**; require human-in-the-loop for high-stakes actions (file delete, payments, external sends).
- **Log full trajectories** (prompts, tool calls, results) for evals + incident review.
- **Set token budgets** per task; fail gracefully instead of looping forever.
- Evaluate at the **trajectory level**, not just final output — did the agent take a reasonable path?
- Use **LLM-as-judge** for open-ended outcomes and **assertion-based** evals for tool-call correctness.

## When To Use It

- **The task is open-ended and multi-step.** "Research X and write a report" needs planning; "lookup Y" doesn't.
- **The answer requires multiple sources or tools.** Anything beyond a single retrieval or computation.
- **You want to automate a knowledge-work flow.** Coding, research, data analysis, customer support triage.
- **You need adaptive behavior.** The path to the answer depends on intermediate results.
- **You're prototyping a workflow that *might* become an agent.** Start with a tool-use loop; add planning/reflection as needed.

## When NOT To Use It

- **A simple RAG or single tool call solves it.** Agents add cost and unpredictability — don't reach for one when the path is obvious.
- **Latency budget is tight.** Even a 3-step agent adds 3–10s end-to-end.
- **The decision is deterministic / rule-based.** Just write the code.
- **You can't observe / measure the trajectory.** Agents without trajectory evals become undebuggable black boxes.
- **High-stakes actions are taken without confirmation.** Don't let an agent send emails, delete data, or move money without human-in-the-loop.
- **You're shipping to a regulated industry without audit trail.** The audit trail is mandatory, not optional.

## Why It Matters in 2026

Three forces are reshaping agent design:

1. **MCP became the connective tissue.** Pre-MCP, every framework invented its own tool protocol. Post-MCP (mid-2024 → 2026), there's one open standard; Claude, OpenAI, Google, and most frameworks support it. The question is no longer "how does my agent call tools" but "what tools should my agent have."
2. **Production reliability caught up.** Anthropic's 2024–2025 work on context engineering, durable execution, and trajectory-level evals made "agent in production" no longer a contradiction. LangGraph, LlamaIndex Workflows, and the Anthropic Agent SDK all ship durable execution (pause/resume/recover) and human-in-the-loop primitives.
3. **Pattern consolidation.** The wild-west of "agents" has converged into ~5 well-named patterns. Vendor docs ([Anthropic](https://www.anthropic.com/engineering/building-effective-agents), [OpenAI](https://openai.com/index/a-practical-guide-to-building-agents/), Google, Microsoft) agree on the taxonomy. ReAct is the default; Plan-and-Execute for long-horizon; Routing for mixed domains.

Practitioner consensus in 2026 (per [Braintrust 2026 framework review](https://www.braintrust.dev/articles/best-ai-agent-frameworks-2026)):
- Start with **tool-use**; graduate to **ReAct** when you need >1 call per task.
- Add **planning** when workflows exceed 5 steps.
- Add **routing** when tool count or domain count exceeds ~10–20.
- Add **reflection** for code / writing, skip for retrieval.
- Use **MCP** for any tool you might want to share with another agent or system.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 75 | Patterns (ReAct, planning, routing) are 3+ years old in research; production-grade since 2024. MCP is 2 years old and rapidly stabilizing. |
| Community | 95 | Massive — every LLM vendor ships agent guides; MCP ecosystem has hundreds of servers; "Building Effective Agents" is one of the most-read engineering blog posts of 2024–2025. |
| Learning curve | 50 | Each pattern is simple in isolation; composing them and debugging trajectories is hard. MCP + tool design + eval setup is multi-week learning. |
| Performance | 70 | Agents add latency (3–10s typical multi-step) and cost (3–10× single-call). Quality gains are real but conditional on good tool design and trajectory evals. |
| Cost | 65 | Per-task cost is 3–10× single-call LLM. Multi-agent systems can be 20–50×. Token budgets are mandatory. |
| DX (developer experience) | 75 | LangGraph Studio + LangSmith are best-in-class for debugging; raw Anthropic/OpenAI SDKs require more plumbing; MCP tool development is straightforward. |
| Production readiness | 80 | Real in production at many companies, but failure modes are still being discovered (infinite loops, runaway costs, prompt-injection via tool outputs). Human-in-the-loop is the default for anything consequential. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Pure RAG (no agent)** | Single-step retrieval over a stable corpus. | The answer requires multiple tools or depends on intermediate results. |
| **Fixed pipeline (chains)** | The order of steps is known and stable; you want predictability. | The next step depends on what the previous step returned. |
| **Multi-agent (CrewAI/AutoGen)** | Roles are clearly distinct and benefit from specialization. | Most apps — a single well-tooled agent is enough; multi-agent adds coordination overhead. |
| **Human-in-the-loop workflow** | The cost of a wrong action is high (legal, financial, medical). | The user expects a real-time, autonomous experience. |
| **Code generation + execution** | The task is genuinely computational; you can sandbox the code. | The task is conversational or retrieval-heavy. |
| **Fine-tuned single-purpose model** | The task is narrow, high-volume, and well-defined enough to fine-tune. | The task requires adaptability to new tools or context. |

## Sources

- [Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) — 2024 (updated 2025)
- [Anthropic — Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — 2025-09
- [Anthropic Platform Docs — Tool Use Overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) — 2026
- [OpenAI — A Practical Guide to Building Agents](https://openai.com/index/a-practical-guide-to-building-agents/) — 2025
- [Model Context Protocol — Tools Spec (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) — 2026-07
- [Model Context Protocol — 2026-07-28 Release Blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/) — 2026-07
- [Context Studios — MCP Ecosystem in 2026 (v1.27 release)](https://www.contextstudios.ai/blog/mcp-ecosystem-in-2026-what-the-v127-release-actually-tells-us) — 2026
- [Medium — The Future of MCP: How Agents Get Connected in 2026](https://medium.com/@anandtopu/the-future-of-mcp-how-agents-get-connected-in-2026-ee24d62c0c43) — 2026
- [LevelUp — Model Context Protocol Explained (MCP in 2026)](https://levelup.gitconnected.com/model-context-protocol-explained-why-every-ai-developer-needs-to-know-mcp-in-2026-bf0ed0d1f845) — 2026-01
- [arXiv 2210.03629 — ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) — 2022
- [Prompting Guide — ReAct Technique](https://www.promptingguide.ai/techniques/react) — 2025
- [Lilian Weng — LLM-Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) — 2023
- [Braintrust — Best AI Agent Frameworks 2026](https://www.braintrust.dev/articles/best-ai-agent-frameworks-2026) — 2026-07