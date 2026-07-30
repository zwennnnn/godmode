---
name: Claude Code
category: modern-ai
status: researched
last-updated: 2026-07-30
sources:
  - https://docs.claude.com/en/docs/claude-code/overview
  - https://docs.anthropic.com/en/docs/claude-code
  - https://github.com/anthropics/claude-code
  - https://docs.anthropic.com/en/docs/claude-code/quickstart
  - https://docs.claude.com/en/docs/claude-code/memory
  - https://docs.claude.com/en/docs/claude-code/skills
  - https://docs.claude.com/en/docs/claude-code/sub-agents
  - https://docs.anthropic.com/en/docs/claude-code/hooks
  - https://docs.claude.com/en/docs/claude-code/changelog
  - https://docs.anthropic.com/en/docs/claude-code/best-practices
  - https://docs.claude.com/en/docs/claude-code/settings
tags: [claude-code, ai-coding, anthropic, agent, terminal, cli, claude, mcp, skills]
---

# Claude Code

## One-liner

Anthropic's official AI coding agent for the terminal — the dominant CLI-based coding assistant in 2026, with sub-agents, skills, hooks, and a memory system for persistent project knowledge.

## What It Is

[Claude Code](https://docs.claude.com/en/docs/claude-code/overview) is Anthropic's official command-line coding agent. It runs in your terminal, understands your entire codebase, and uses Claude (Sonnet / Opus / Haiku) to read files, edit code, run commands, and ship features autonomously. It's the reference implementation of the "AI coding agent" category.

The 2026 baseline includes:

- **Claude Code 2.x** — current stable.
- **Models** — Claude Opus 4.7 / Sonnet 4.5 / Haiku 4.5 in 2026.
- **Sub-agents** — isolated agents for parallel work.
- **Agent Skills** — `.claude/skills/` (see [`/skills.md`](/skills.md)).
- **Hooks** — Pre/post tool call hooks for deterministic control.
- **CLAUDE.md** — project-level instructions (this very repo uses one).
- **Memory** — auto-managed memory files; project + user scope.
- **MCP (Model Context Protocol)** — connect to tools / data sources.
- **Plan mode** — read-only; Claude proposes, you approve.
- **Multi-modal** — image input.

Adoption: Claude Code is the **#1 AI coding agent** by 2026. Used at every Anthropic customer + most AI-forward startups. Competes with Cursor, Codex, GitHub Copilot CLI.

## When To Use It

- **You want a terminal-based coding agent** — Claude Code's home turf.
- **You ship features end-to-end** — Claude Code can read + edit + run + commit.
- **You want sub-agents for parallel work** — built-in.
- **You want project-level memory** — CLAUDE.md + auto-memory.
- **You want MCP integration** — connect to any tool.
- **You want to package team conventions** — skills.

## When NOT To Use It

- **You want IDE-only** — use Cursor.
- **You want GitHub PR-based review** — Copilot is more integrated.
- **You want minimal AI in your loop** — use raw Claude API instead.

## Why It Matters in 2026

Three forces: (1) Terminal-based agents won — Claude Code + Codex CLI + Gemini CLI are the dominant pattern; (2) Skills + memory made the agent extensible; (3) MCP became the standard for tool integration. Claude Code is the reference implementation.

Practitioner playbook in 2026: (1) Install + authenticate; (2) Add `CLAUDE.md` to every repo; (3) Use `/init` to bootstrap; (4) Define sub-agents for specialized tasks; (5) Add skills for team conventions; (6) Use plan mode for risky changes.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 90 | 1.5+ years; Anthropic's flagship product. |
| Community | 100 | Massive; default in AI-forward teams. |
| Learning curve | 80 | Easy to start; sub-agents + skills take study. |
| Performance | 90 | Claude 4.x is best-in-class. |
| Cost | 70 | Pay per token; can be expensive. |
| DX | 95 | CLI + plan mode + sub-agents + memory = excellent. |
| Production readiness | 95 | Used everywhere. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Cursor** | IDE-first; GUI. | Terminal-first. |
| **Codex CLI** | OpenAI ecosystem. | Anthropic ecosystem. |
| **GitHub Copilot** | PR review integration. | Autonomous coding. |
| **Raw API** | Programmatic. | You want agent loop. |
| **Continue** | VS Code + multiple models. | You want Claude-first. |

## Sources

- [Claude Code Overview](https://docs.claude.com/en/docs/claude-code/overview) — 2026
- [Claude Code Docs (Anthropic)](https://docs.anthropic.com/en/docs/claude-code) — 2026
- [Claude Code GitHub (anthropics/claude-code)](https://github.com/anthropics/claude-code) — 2026
- [Claude Code Quickstart](https://docs.anthropic.com/en/docs/claude-code/quickstart) — 2026
- [Claude Code Memory](https://docs.claude.com/en/docs/claude-code/memory) — 2026
- [Claude Code Skills](https://docs.claude.com/en/docs/claude-code/skills) — 2026
- [Claude Code Sub-Agents](https://docs.claude.com/en/docs/claude-code/sub-agents) — 2026
- [Claude Code Hooks](https://docs.anthropic.com/en/docs/claude-code/hooks) — 2026
- [Claude Code Changelog](https://docs.claude.com/en/docs/claude-code/changelog) — 2026
- [Claude Code Best Practices](https://docs.anthropic.com/en/docs/claude-code/best-practices) — 2026
- [Claude Code Settings](https://docs.claude.com/en/docs/claude-code/settings) — 2026