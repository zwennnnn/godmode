# godmode

> **A weighted-scoring technology decision engine, packaged as an Agent Skill for AI coding agents.**
>
> A curated knowledge base of **117+ technologies** from [roadmap.sh](https://roadmap.sh), organized across **17 roadmaps**, with a working **weighted-scoring engine** that picks the best tech for your project.

[![Install with skills.sh](https://img.shields.io/badge/skills.sh-install-blue)](https://skills.sh) [![GitHub](https://img.shields.io/badge/GitHub-zwennnnn%2Fgodmode-black)](https://github.com/zwennnnn/godmode) [![MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE) [![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)

When you ask an AI coding agent (Claude Code, Cursor, Codex, etc.) "what database should I use" or "what's the best stack for a SaaS MVP", godmode:

1. Reads the user's profile from `godmode.md`.
2. Picks the right stage profile (`mvp-speed`, `production-scale`, `research-experimental`, `enterprise-compliance`).
3. Runs `python scripts/score.py` to compute weighted scores from the curated `.md` files.
4. Returns **top 3 recommendations** with full transparency — weights, scores, sources, and trade-offs.
5. Logs the decision to `godmode.md` so the next session continues seamlessly.

---

## What's inside

```
godmode/
├── SKILL.md              # Agent Skills manifest (Claude Code / Cursor / skills.sh)
├── CLAUDE.md             # System prompt for AI agents
├── godmode.md            # Session memory (auto-updated)
├── rules.md              # Untouchable rules
├── decision-engine.md    # Weighted-scoring algorithm
├── scoring/
│   ├── weights.json      # Stage profiles (mvp-speed, production-scale, etc.)
│   └── rubric.md         # Scoring criteria definitions
├── templates/            # MD templates
├── scripts/
│   ├── score.py          # Weighted-scoring engine (the heart)
│   ├── research.py       # Scaffolder for new tech MD files
│   ├── validate-md.py    # Schema validator
│   ├── scrape-roadmap.py # roadmap.sh scraper
│   └── research-batch.md # Research protocol
├── skills.md             # skills.sh + Claude Agent Skills guide
└── roadmaps/             # 17 roadmaps × 5–12 techs each = 117+ tech files
    ├── ai-ml-llm/        (12 techs)
    ├── frontend-backend/ (10)
    ├── devops-cloud/     (10)
    ├── mobile/           (10)
    ├── programming-languages/ (6)
    ├── system-design/    (5)
    ├── data-ai/          (4)
    ├── databases/        (6)
    ├── design-ux/        (6)
    ├── game-development/ (6)
    ├── cyber-security/   (6)
    ├── backend-frameworks/ (8)
    ├── frontend-frameworks/ (6)
    ├── modern-ai/        (5)
    ├── infra-tools/      (6)
    ├── qa-testing/       (5)
    └── people-process/   (6)
```

---

## Quick start

### 1. Score tech for your project

```bash
# What tech should I use for an MVP web app?
python scripts/score.py --roadmap frontend-backend --stage mvp-speed --top 3

# What about production-scale?
python scripts/score.py --roadmap frontend-backend --stage production-scale --top 5

# Search across all roadmaps
python scripts/score.py --stage mvp-speed --query "vector database" --top 5

# JSON output for downstream tools
python scripts/score.py --json
```

### 2. Validate the knowledge base

```bash
python scripts/validate-md.py --all
# PASS: 0 error(s) across 134 file(s).
```

### 3. Add a new tech

```bash
# Interactive — prompts for each field
python scripts/research.py --interactive

# Or pass everything on the CLI
python scripts/research.py --name "Redis" --roadmap databases \
  --sources "https://redis.io/" --tags "cache,in-memory" \
  --maturity 100 --community 100 --learning-curve 85 --performance 100 --cost 70 --dx 90 --production-readiness 100 \
  --one-liner "In-memory data store used as cache, broker, leaderboard, and pub/sub."
```

### 4. Install as an Agent Skill

**Universal — install via skills.sh (works with Claude Code, Cursor, Codex):**
```bash
npx skills add zwennnnn/godmode
```

**For Claude Code (in a project):**
```bash
# Place this directory at .claude/skills/godmode/ in your project.
# Then Claude Code will auto-discover the SKILL.md.
cp -r godmode/ .claude/skills/godmode/
```

**For Cursor:**
```bash
# Add the key files to .cursor/rules/:
cp CLAUDE.md godmode.md rules.md decision-engine.md .cursor/rules/
```

---

## How the scoring works

The algorithm is documented in [`decision-engine.md`](decision-engine.md). Summary:

```
score(tech, stage) = Σ weight[stage][criterion] × tech.score[criterion]
```

For each tech in a roadmap, godmode reads the scoring matrix from its `.md` file, multiplies each criterion score by the stage weight (from `scoring/weights.json`), and sums. Top 3 by score become recommendations.

Every recommendation includes:
- The weighted score (transparent math).
- Why it fits the user's specific profile.
- Trade-offs (cost, complexity, learning curve, when NOT to use).
- Source links from the `.md` file.

---

## Stage profiles

| Stage | Best for | Priorities |
|-------|----------|------------|
| `mvp-speed` | Startups, prototypes, fast iteration | Learning curve, DX, community, cost. |
| `production-scale` | Real users, real money, real traffic | Maturity, performance, production readiness. |
| `research-experimental` | Cutting-edge / innovation | Innovation, performance, DX. |
| `enterprise-compliance` | Banking, healthcare, regulated | Maturity, support, security. |

Edit `scoring/weights.json` to tune.

---

## Adding new technologies

When the user asks about a tech not in the knowledge base:

1. Use WebSearch to research: official docs, 2026 trends, vs alternatives, production case studies.
2. Run `python scripts/research.py --interactive` and fill the prompts.
3. Validate: `python scripts/validate-md.py <new-file>.md`.
4. The new tech is now part of the knowledge base and will be included in future scoring.

See `scripts/research-batch.md` for the full protocol.

---

## Contributing

Want to add a tech, fix a score, or improve a `When NOT To Use` section?

1. Edit the relevant `roadmaps/<category>/<tech>.md` file.
2. Run `python scripts/validate-md.py` to ensure schema compliance.
3. (Optional) Run `python scripts/score.py --roadmap <category> --stage mvp-speed` to verify the score change.

PRs welcome.

---

## License

MIT. Use it, fork it, ship it.

---

## Acknowledgements

- [roadmap.sh](https://roadmap.sh) — the source of truth for what technologies to cover.
- [Anthropic](https://www.anthropic.com/) — Claude Code + the Agent Skills specification.
- [Vercel](https://vercel.com/) — [skills.sh](https://skills.sh) registry.
- Every open-source technology documented in `roadmaps/`.