# Scoring Rubric

> What each criterion means and how to assign a 0–100 score. Every tech `.md` file uses this rubric. Keep it consistent — `scripts/validate-md.py` will check.

---

## Criteria (the canonical set)

These are the criteria referenced in [`weights.json`](weights.json). Tech files may include more criteria if they need them (e.g. `security_compliance` for an enterprise DB), but must include the **core 7** below.

### Core (always present in every tech `.md`)

| Criterion | What it measures | How to score |
|-----------|------------------|--------------|
| **maturity** | How battle-tested is it? Years in production, breaking-change frequency, deprecation history. | 90+ = 5+ years, multiple major companies, no recent rewrites. 50 = 2–3 years, some churn. <30 = <1 year or pre-1.0. |
| **community** | Size and activity of the community. GitHub stars, Discord/Slack size, Stack Overflow questions, conference talks. | 90+ = top-10 in its space, active RFC process. 50 = solid niche community. <30 = solo maintainer or near-zero activity. |
| **learning_curve** | How long until a competent engineer is productive. Documentation quality, conceptual surface area, magic-vs-explicit ratio. | 90+ = clear docs, opinionated, fast onboarding. 50 = needs a book. <30 = requires PhD-level theory. |
| **performance** | Raw capability — throughput, latency, memory, scalability ceiling. Includes benchmark results when available. | 90+ = best-in-class benchmarks. 50 = average for the category. <30 = known to be slow or scales poorly. |
| **cost** | Total cost of ownership. License fees, infra spend, engineering time, opportunity cost. | 90+ = free, runs on a laptop. 50 = moderate infra or paid tier needed at scale. <30 = enterprise pricing or runaway cloud bills. |
| **dx** | Developer experience. Tooling, error messages, IDE support, hot reload, debug-ability. | 90+ = "just works", great errors, first-class tools. 50 = workable but rough edges. <30 = daily friction. |
| **production_readiness** | Is it used in production by real companies at scale? Observability, deployment ergonomics, upgrade path. | 90+ = Netflix/Google/Banks scale. 50 = production-usable but rare in big orgs. <30 = toy-grade. |

### Optional (add per-category as needed)

| Criterion | When to add | Notes |
|-----------|-------------|-------|
| **security** | Auth, crypto, data-handling techs | CVE history, audit-ability, defaults. |
| **support** | Commercial / enterprise tech | Vendor SLAs, paid support, LTS. |
| **innovation** | Cutting-edge AI/ML, experimental runtimes | Recent breakthroughs, novel approach, research citations. |
| **ecosystem_integrations** | Glue tech (queues, APIs, frameworks) | How many things plug into it natively. |
| **model_quality** | LLM/embedding models | Benchmark scores (MMLU, HumanEval, retrieval accuracy). |
| **latency** | Real-time / inference techs | p50/p99 numbers. |
| **flexibility** | Frameworks, ORMs, configs | How many ways can you use it; escape hatches. |

---

## Scoring conventions

- **Integer 0–100**. No decimals. Round to nearest integer.
- **Evidence required.** Every score in a tech `.md` must have a one-line "evidence" note. *"Battle-tested since 2016"* is enough. *"Feels fast"* is not.
- **Calibrate against peers.** Before publishing a tech file, compare scores to sibling techs in the same category. If your new entry scores 90 on maturity but the rest of the category is at 50–70, you're probably inflating it.
- **Date the score.** Scoring matrix `last-updated` field tracks when scores were last calibrated. Stale scores (>12 months) should be re-checked.

---

## Anti-patterns in scoring

- ❌ **Halo effect.** "I love this tool" → giving it 90 across the board without checking each criterion.
- ❌ **Recency bias.** A 6-month-old hyped tool scoring 95 on maturity just because it's in the news.
- ❌ **Vendor-driven scoring.** Copying scores from a vendor blog post uncritically.
- ❌ **All-eggs-in-one-basket.** A single tech scoring 100/100 on everything — that's marketing, not reality.

---

## How weights and scores interact

- `weights.json` says **what matters** for the user's stage.
- `rubric.md` defines **how to score** each criterion.
- `tech.md` files provide **the actual scores** (with evidence).
- `decision-engine.md` multiplies them and ranks.

Example for `mvp-speed` stage + a hypothetical framework:
```
maturity: 70  × 0.10  = 7.0
community: 95 × 0.20  = 19.0
learning_curve: 90 × 0.25 = 22.5
performance: 60 × 0.05  = 3.0
cost: 80 × 0.15       = 12.0
dx: 95 × 0.20         = 19.0
production_readiness: 50 × 0.05 = 2.5
                       ----------
total = 85.0  → strong fit for MVP stage
```

---

## Versioning

This file is owned by the model (with user approval). Major criterion additions/removals should be logged in `godmode.md`.