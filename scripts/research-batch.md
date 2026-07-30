# Research Batch — Per-Technology Protocol

> **For the model** (or any human contributor). This is the step-by-step protocol for turning a stub MD into a real, scored, sourced technology knowledge file.

---

## When to use this

- You just generated stubs with `scripts/scrape-roadmap.py`, OR
- The user asked to research a specific tech that's not yet covered, OR
- An existing tech `.md` is stale (>12 months) and needs refreshing.

---

## The protocol (per technology)

### Step 1 — Read the stub
Read `roadmaps/<category>/<tech>.md`. Note the `parent` field for context — what part of the roadmap this tech sits in.

### Step 2 — Official source (always first)
WebFetch or browse to the **official documentation / homepage** of the technology.

Extract:
- 1–2 sentence "what it is" description (paraphrase, don't quote).
- Authoritative version info (current major version, last release date).
- Pricing / licensing model.
- The 2–3 top official features claimed.

Update the `.md` `## What It Is` section + add the official URL to `## Sources` with the current `YYYY-MM`.

### Step 3 — Market context (2025–2026)
WebSearch:
- `"<tech>" 2026 trends`
- `"<tech>" benchmarks 2025` or `2026`
- `"<tech>" vs <top-2-alternatives>` (use your judgment on which alternatives)

Goal: 3+ unique third-party sources from 2025–2026. Good sources:
- Benchmark studies (e.g. MLPerf, Stanford HELM, independent benchmarks).
- Engineering blog posts from companies using it at scale (Netflix, Uber, Stripe, etc.).
- Conference talks (PyData, KubeCon, NeurIPS, etc.).
- Analyst reports (Gartner, Forrester — use with caveats).

If you can't find 3 recent sources, **say so honestly** in the `.md` and note it as a limitation.

### Step 4 — Scoring (use `scoring/rubric.md`)
For each criterion in the rubric:
1. Look at the score you want to give.
2. Write a **one-line evidence note** explaining *why* that score.
3. Check against peer techs in the same category — your scores should be comparable.
4. Update the `Scoring Matrix` table in the `.md`.

Never give all-100 or all-50. Use the full range.

### Step 5 — "When to use" / "When not to use"
This is the most opinionated section. Use your sources:
- "When to use" should reflect what the **official docs** AND **production users** actually recommend.
- "When not to use" should reflect what the **critics / competitors / post-mortems** warn against.
- 3–5 bullets each, no more.

### Step 6 — Alternatives table
Pick the 2–3 most common alternatives. For each:
- One specific case where the alternative is **better** than this tech.
- One specific case where the alternative is **worse**.

Avoid generic "X is faster" claims — be specific (e.g. "X has 2× lower p99 latency for batch workloads >1M docs").

### Step 7 — Final pass
Before saving:
- Frontmatter is complete: `name`, `category`, `status` (now `researched`), `last-updated`, `sources` (3+ URLs), `tags`.
- Every `##` section has content — no `*TODO*` left.
- Scoring matrix has evidence for every cell.
- Sources section has every URL with `YYYY-MM` date.

Update frontmatter:
- `status: placeholder` → `status: researched`
- `last-updated:` → today's `YYYY-MM`
- `sources:` → list of URLs

### Step 8 — Validate
Run:
```
python scripts/validate-md.py roadmaps/<category>/<tech>.md
```
Fix any errors before moving to the next tech.

### Step 9 — Log to `godmode.md`
Update the progress tracker:
- Mark the tech `[x]`.
- Append to `## Recent Decisions` if there was a noteworthy learning (e.g. a surprising scoring outcome).

---

## Batch processing tips

- Process techs **one at a time, in build order**. Don't try to do 10 in parallel in one context — context budget explodes.
- If a tech's scoring has a surprising outcome (e.g. you expected 90 but evidence shows 60), **document the surprise** in the `.md` (one line at the top).
- If a tech is deprecated or sunset, mark `status: outdated` and link to a replacement.
- If a tech is brand-new (<6 months), mark `status: experimental` and lower the maturity/community scores accordingly.

---

## Time budget

Aim for:
- Official source read: ~3 min
- WebSearch for benchmarks/alternatives: ~5 min
- Scoring + writing the `.md`: ~10 min
- Validate + log: ~2 min

Total: ~20 min per tech. For 12 techs in a roadmap, that's ~4 hours. That's expected — this is a real research project, not a paste job.

---

## What to do if you get stuck

- **No good sources?** Mark the `.md` with `status: placeholder` and note in `godmode.md` that the tech needs more research. Don't fake the score.
- **Too many conflicting benchmarks?** Pick the most recent and the most rigorous (peer-reviewed > vendor blog > forum post). Note the conflict in the scoring evidence.
- **Tech is mid-major-version-change?** Wait one release cycle if possible, or document the change risk prominently.