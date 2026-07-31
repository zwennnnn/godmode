---
description: Discover today's ProductHunt launches, find products missing from a target market (default: read from godmode.md), score on market-gap + quality + feasibility + fit, then scaffold projects/<slug>/ with a customized plan. Fully autonomous.
argument-hint: [market]
allowed-tools: WebSearch, WebFetch, Bash, Read, Write, Edit, Glob
---

# /godhunt — Autonomous ProductHunt → Project Scaffold

> **Trigger:** user types `/godhunt [market]` (e.g. `/godhunt Turkey`).
> **Argument** (`$ARGUMENTS`): target market (e.g. `Turkey`, `Brazil`, `Indonesia`, `global`). Optional — if omitted, read from `godmode.md` → `## Current User Profile` → `primary_domain`. If still unclear, default to `"global"`.
> **Behavior:** discover today's ProductHunt launches, find products missing from `<market>`, score, and scaffold a `projects/<slug>/` directory. Fully autonomous — no user input beyond the slash argument.

## Protocol (agent must follow exactly)

1. **Fetch today's ProductHunt launches.**
   - `WebSearch`: `site:producthunt.com today launches` or `site:producthunt.com launched yesterday`.
   - Alternative: scrape `https://www.producthunt.com/launches`.

2. **Per-product gap analysis in `$ARGUMENTS`.** For each candidate:
   - `WebSearch`: `"<product name>" <market>`
   - `WebSearch`: `"<product name>" <market> competitor`
   - Determine: does the product already exist or have a strong local competitor in `<market>`?

3. **Score each candidate** (autonomous; no user input):
   - `market_gap` (0–100): How absent is this category in `<market>`? (high = good gap)
   - `quality` (0–100): Traction (votes, comments), team credibility
   - `feasibility` (0–100): Can the MVP be built with **only** an AI API + a web/mobile stack?
   - `market_fit_potential` (0–100): Will this succeed in `<market>` if we build it?

   ```
   composite = 0.35·market_gap + 0.20·quality + 0.25·feasibility + 0.20·market_fit_potential
   ```

4. **Pick top candidate** with `composite ≥ 80`. If none qualifies, stop and tell the user "no candidate found today".

5. **Decide customization mode:**
   - **customize** if there's any local traction or partial overlap → add 3–5 market-specific features (localization, local payment, regulatory compliance, pricing in local currency).
   - **as-is** if highly original and no local alternatives.

6. **Run the scaffolder:**
   ```bash
   python scripts/hunt.py create \
       --name "<Display Name>" \
       --slug "<url-slug>" \
       --ph-url "<producthunt-url>" \
       --market "<market>" \
       --mode customize|as-is \
       --market-score NN --feasibility-score NN --quality-score NN \
       --short-description "..." --market-justification "..." \
       --mvp-scope "..." --features "f1,f2,f3,..." \
       --frontend "..." --backend "..." --db "..." --auth "..." --deploy "..." \
       --customizations "..." --ph-description "..."
   ```
   The script uses `templates/project-readme.md` and `templates/project-plan.md`.

7. **Log** to `godmode.md` under `## Recent Decisions`.

8. **Tell the user:**
   > "Project scaffolded at `projects/<slug>/`. Run `/godproject <slug>` to scaffold the code."

## Rules

- ❌ **Never** ask the user clarifying questions inside `/godhunt`. All decisions are made from `godmode.md` + scoring + gap analysis.
- ✅ **Always** invoke the Python script with all required arguments.
- ✅ **Always** log to `godmode.md`.
- ✅ **Always** output the project path + next step.

## Example

```
> /godhunt Turkey

[agent fetches PH launches, runs gap analysis, picks top candidate]

Created project: projects/turkce-ai-destek/
  README.md  (market fit + tech stack + customizations)
  PLAN.md    (6-phase build plan)
  src/, tests/  (empty)
  .env.example (Minimax API key)

Next: /godproject turkce-ai-destek
```
