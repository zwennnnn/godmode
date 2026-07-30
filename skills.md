---
name: skills.sh and Agent Skills
description: The skills.sh registry for AI coding agents (Claude Code, Cursor, Codex) — install, browse, build custom skills, integrate with godmode.
slug: skills
---

# skills.sh and Agent Skills

> **What:** skills.sh is the registry + CLI for distributing "Agent Skills" — folders of instructions, scripts, and resources that AI coding agents (Claude Code, Cursor, Codex, others) load on demand to perform specialized tasks better.
> **Why:** Skills let you package procedural knowledge (project conventions, deployment steps, security review checklists) into reusable units that any agent can pick up automatically.
> **How this connects to godmode:** godmode itself is essentially a massive skill — `CLAUDE.md` + `godmode.md` + `rules.md` make every LLM behave like a godmode-augmented tech advisor. Skill mechanism = the distribution format for that.

---

## What is skills.sh?

[skills.sh](https://skills.sh) is an open registry for Agent Skills, launched by Vercel in January 2026. It complements [Anthropic's official Agent Skills spec](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) with a hosted registry + CLI.

The official Anthropic concept of **Claude Skills** (folders in `.claude/skills/`) and **skills.sh** (the registry) work together. Skills.sh is the npm-style package manager for skills.

### Key URLs

- [skills.sh](https://skills.sh) — The registry.
- [skills.sh Docs](https://skills.sh/docs) — Quick start + CLI reference.
- [Vercel Agent Skills Docs](https://vercel.com/docs/agent-skills) — Vercel-specific.
- [Anthropic Skills Repo](https://github.com/anthropics/skills) — Official examples.
- [Anthropic Skills Cookbook](https://github.com/anthropics/skills-cookbook) — Practical recipes.
- [Claude Code Skills Docs](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) — Claude-specific.
- [Claude Skills SDK](https://docs.claude.com/en/api/skills-sdk) — SDK reference.
- [awesome-claude-skills (ComposioHQ)](https://github.com/ComposioHQ/awesome-claude-skills) — Curated list.

---

## How to find a skill (findskill equivalent)

### Browsing the registry

| Method | How |
|--------|-----|
| **Web** | [skills.sh](https://skills.sh) — search by name, tag, owner. |
| **CLI search** | `npx skills search <query>` |
| **CLI list** | `npx skills list` (lists installed skills) |
| **GitHub topics** | Search `agent-skill` on GitHub. |
| **awesome-claude-skills** | Curated list at [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills). |

### CLI quick reference (skills.sh)

```bash
# Install a skill from the registry
npx skills add <owner>/<repo>

# Install with a target agent (Claude Code, Cursor, Codex, ...)
npx skills add <owner>/<repo> --agent claude-code

# Search the registry
npx skills search <query>

# List installed skills
npx skills list

# Remove a skill
npx skills remove <skill-name>

# Update installed skills
npx skills update

# Create a new skill (interactive)
npx skills create
```

---

## What is an Agent Skill?

A **skill** is a folder containing:

```
my-skill/
├── SKILL.md              # Required: frontmatter + instructions
├── scripts/               # Optional: executable scripts
├── resources/             # Optional: templates, examples
└── README.md              # Optional
```

The `SKILL.md` has YAML frontmatter:

```markdown
---
name: my-skill-name
description: Short description for the agent to know when to use this skill.
---

# Skill instructions

Markdown body with the actual procedural knowledge.
```

The agent **dynamically loads** skills based on relevance to the current task. Unlike slash commands (user-triggered), skills are **agent-triggered**.

---

## godmode as a skill

Godmode itself is essentially a skill bundle:

| Component | Skill-like element |
|-----------|-------------------|
| `CLAUDE.md` | The boot sequence + behavior contract. |
| `godmode.md` | Session memory (auto-updated). |
| `rules.md` | Untouchable rules. |
| `decision-engine.md` | The decision algorithm. |
| `roadmaps/**/*.md` | Knowledge base loaded on demand. |

To make godmode a **distributable skill** via skills.sh:

```bash
# From inside the godmode repo:
npx skills create
# → interactive prompts for name, description, etc.

# Or manually:
mkdir .claude/skills/godmode-tech-advisor
cp CLAUDE.md godmode.md rules.md decision-engine.md .claude/skills/godmode-tech-advisor/
cp -r roadmaps/ .claude/skills/godmode-tech-advisor/

# Publish:
npx skills add <your-username>/godmode
```

After publishing, anyone can install godmode into their project:

```bash
npx skills add your-username/godmode
```

And their Claude Code / Cursor / Codex agent will load the godmode system on demand.

---

## Popular skills (examples)

| Skill | Use |
|-------|-----|
| `vercel/vercel-deploy` | Deploy to Vercel correctly. |
| `anthropics/webapp-testing` | Test web apps via Playwright. |
| `anthropics/pdf-processing` | Read + extract PDF content. |
| `anthropics/brand-guidelines` | Apply Anthropic brand styles. |
| `ComposioHQ/*` | Various third-party integrations. |

Browse the full registry at [skills.sh](https://skills.sh).

---

## When To Use It

- **You want to share team conventions** with the AI agent — packaging them as a skill.
- **You want to standardize a workflow** — testing, deployment, security review.
- **You want reusable AI capabilities** — install once, use in every project.
- **You want godmode itself to be reusable** — package it as a skill.

## When NOT To Use It

- **Your conventions are one-off** — just put them in CLAUDE.md or .cursorrules.
- **You want subagents** — different concept (isolated agent instances, not on-demand knowledge).
- **You want slash commands** — different concept (user-triggered, not agent-triggered).

## Why It Matters in 2026

Three forces:

1. **AI coding agents became ubiquitous.** Claude Code, Cursor, Codex, Copilot — every dev uses at least one. Skills are the standard way to extend them.
2. **Distribution + reuse matter.** Putting your CLAUDE.md in every repo is duplication; publishing a skill = install in one command.
3. **Godmode itself benefits.** godmode is a ~110-file knowledge base; distributing as a skill makes it instantly usable in any project.

Practitioner playbook in 2026:
1. **Start simple** — write your CLAUDE.md / .cursorrules first.
2. **Reuse patterns** — when you copy the same conventions to a new repo, it's time for a skill.
3. **Browse skills.sh** — see what's available before writing your own.
4. **Publish** — share your team's skills; contribute to the community.
5. **Iterate** — skill content evolves with your codebase.

## Scoring Matrix (0–100)

### skills.sh (registry + CLI)
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 80 | Launched Jan 2026; backed by Vercel. |
| Community | 85 | Fast-growing; built on the agent-skill concept. |
| Learning curve | 85 | Easy to install; creating skills is straightforward. |
| Performance | 90 | Quick install; lightweight. |
| Cost | 100 | Free OSS. |
| DX | 90 | npm-like DX; good docs. |
| Production readiness | 80 | New but stable. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **skills.sh + Claude Skills** | Distribution; reuse; team. | One-off project conventions. |
| **CLAUDE.md / .cursorrules** | Single project; simple. | Multi-project reuse. |
| **Slash commands** | User-triggered actions. | Agent-triggered knowledge. |
| **Subagents** | Isolated agent contexts. | Reusable knowledge. |
| **MCP servers** | Tool integration. | Procedural knowledge. |

## Sources

- [skills.sh — Agent Skills Registry](https://skills.sh) — 2026
- [skills.sh Docs](https://skills.sh/docs) — 2026
- [Vercel — Agent Skills Docs](https://vercel.com/docs/agent-skills) — 2026
- [Vercel — Installing Agent Skills](https://vercel.com/docs/agent-skills/install) — 2026
- [Vercel — Agent Skills Launch Blog](https://vercel.com/blog/agent-skills-launch) — 2026
- [Anthropic Skills GitHub (anthropics/skills)](https://github.com/anthropics/skills) — 2026
- [Anthropic Skills Cookbook (anthropics/skills-cookbook)](https://github.com/anthropics/skills-cookbook) — 2026
- [Anthropic Agent Skills Examples](https://github.com/anthropics/skills/tree/main/examples) — 2026
- [Claude Code — Agent Skills Overview](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) — 2026
- [Claude Skills Best Practices](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices) — 2026
- [Claude Skills SDK](https://docs.claude.com/en/api/skills-sdk) — 2026
- [awesome-claude-skills (ComposioHQ)](https://github.com/ComposioHQ/awesome-claude-skills) — 2026
- [Claude Log — Skills vs Sub-Agents vs Slash Commands](https://claudelog.com/mechanics/skills-vs-others) — 2026
- [Marin Marinov — Claude Agent Skills Complete Guide](https://medium.com/@marin-marinov) — 2026
- [Claude Skills Official Page](https://www.claude.com/product/skills) — 2026