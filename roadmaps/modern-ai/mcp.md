---
name: Model Context Protocol (MCP)
category: modern-ai
status: researched
last-updated: 2026-07-30
sources:
  - https://modelcontextprotocol.io/
  - https://modelcontextprotocol.io/docs/
  - https://modelcontextprotocol.io/docs/concepts/architecture
  - https://modelcontextprotocol.io/docs/concepts/tools
  - https://modelcontextprotocol.io/docs/concepts/resources
  - https://modelcontextprotocol.io/docs/concepts/prompts
  - https://modelcontextprotocol.io/docs/concepts/transports
  - https://github.com/modelcontextprotocol
  - https://docs.anthropic.com/en/docs/agents-and-tools/mcp
  - https://docs.claude.com/en/docs/agents-and-tools/mcp
  - https://cursor.com/docs/context/mcp
tags: [mcp, model-context-protocol, anthropic, ai-agents, tool-use, claude-code, cursor]
---

# Model Context Protocol (MCP)

## One-liner

Anthropic's open protocol that standardizes how AI agents connect to tools, data sources, and prompts — the "USB-C for AI integrations" — adopted by Claude Code, Cursor, and the major agent frameworks in 2026.

## What It Is

The [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) is an open standard for connecting AI agents to tools, data, and prompts. Launched by Anthropic in late 2024; adopted by Claude Code, Cursor, OpenAI's Agents SDK, and most major agent frameworks by 2026.

Three primitive concepts:

- **Tools** — actions the model can invoke (search DB, send email, run script).
- **Resources** — data sources the model can read (files, DB tables, API responses).
- **Prompts** — pre-written prompt templates the user can invoke.

Architecture:

```
┌──────────┐     JSON-RPC      ┌────────────┐
│  Agent   │ ────────────────► │ MCP Server │
│ (Claude) │     over stdio    │ (your tool) │
└──────────┘     or HTTP+SSE    └────────────┘
```

Adoption: MCP is **the de facto standard** for AI tool integration in 2026. Used by Claude Code, Cursor, OpenAI Agents SDK, LangGraph, every major AI agent framework. Hundreds of community MCP servers (GitHub, Slack, Postgres, Notion, etc.).

## When To Use It

- **You're building an AI agent** — MCP is the standard for tools.
- **You want to expose tools to Claude Code / Cursor** — write an MCP server.
- **You want portable AI integrations** — same server works across agents.

## When NOT To Use It

- **You have a single agent / single tool** — direct integration is simpler.
- **You don't need cross-agent compatibility** — vendor-specific SDK may be enough.
- **Real-time / streaming is critical** — MCP is request/response.

## Why It Matters in 2026

Three forces: (1) Tool fragmentation was the bottleneck for AI agents — MCP solved it; (2) Network effects — every major agent framework supports MCP; (3) Open source — anyone can write a server; ecosystem exploded.

Practitioner playbook in 2026: (1) Use MCP servers in Claude Code (e.g. GitHub MCP); (2) Write your own MCP servers for proprietary tools (Python SDK / TypeScript SDK); (3) Publish to community registry; (4) Combine multiple MCP servers for rich agents.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 90 | 1.5+ years; de facto standard. |
| Community | 100 | Massive; Anthropic + OpenAI + Cursor + community. |
| Learning curve | 80 | Easy for consumers; medium for server authors. |
| Performance | 85 | JSON-RPC overhead; fine for most use cases. |
| Cost | 95 | Free; open standard. |
| DX | 85 | Good SDKs (TS + Python); improving. |
| Production readiness | 95 | Battle-tested. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **OpenAI Function Calling** | You're OpenAI-only. | Multi-agent. |
| **LangChain Tools** | LangChain ecosystem. | Cross-agent. |
| **Custom REST APIs** | Custom logic. | Cross-agent. |
| **MCP** | Cross-agent; tools for AI. | Non-AI systems. |

## Sources

- [Model Context Protocol](https://modelcontextprotocol.io/) — 2026
- [MCP Docs](https://modelcontextprotocol.io/docs/) — 2026
- [MCP Architecture](https://modelcontextprotocol.io/docs/concepts/architecture) — 2026
- [MCP Tools](https://modelcontextprotocol.io/docs/concepts/tools) — 2026
- [MCP Resources](https://modelcontextprotocol.io/docs/concepts/resources) — 2026
- [MCP Prompts](https://modelcontextprotocol.io/docs/concepts/prompts) — 2026
- [MCP Transports](https://modelcontextprotocol.io/docs/concepts/transports) — 2026
- [MCP GitHub (modelcontextprotocol)](https://github.com/modelcontextprotocol) — 2026
- [Anthropic MCP Docs](https://docs.anthropic.com/en/docs/agents-and-tools/mcp) — 2026
- [Claude Code MCP](https://docs.claude.com/en/docs/agents-and-tools/mcp) — 2026
- [Cursor MCP Docs](https://cursor.com/docs/context/mcp) — 2026