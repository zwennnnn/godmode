---
name: BI and Reporting
category: data-ai
status: researched
last-updated: 2026-07-30
sources:
  - https://www.tableau.com/learn
  - https://www.tableau.com/
  - https://powerbi.microsoft.com/
  - https://powerbi.microsoft.com/learning/
  - https://cloud.google.com/looker
  - https://cloud.google.com/looker/docs
  - https://www.metabase.com/
  - https://github.com/metabase/metabase
  - https://github.com/apache/superset
  - https://preset.io/
  - https://docs.lightdash.com/
  - https://github.com/lightdash/lightdash
  - https://cube.dev/
  - https://github.com/cube-js/cube.js
  - https://www.thoughtspot.com/
  - https://mode.com/
  - https://hex.tech/
  - https://docs.snowflake.com/
tags: [bi, reporting, tableau, power-bi, looker, metabase, superset, lightdash, thoughtspot, semantic-layer]
---

# BI and Reporting

## One-liner

Self-service business intelligence tools that turn warehouse data into dashboards, reports, and embedded analytics — the layer between your data warehouse and your business users.

## What It Is

BI (Business Intelligence) tools are how business users explore data without writing SQL. They provide:

- **Drag-and-drop dashboards** — for non-technical users.
- **Self-service reporting** — business users answer their own questions.
- **Scheduled reports** — daily/weekly email digests.
- **Embedded analytics** — BI inside your own product (SaaS dashboards for customers).
- **Semantic layer** — shared definitions (a "user" is a user across every dashboard).
- **Governance** — row-level security, certified data sources.

### The 2026 landscape

| Tier | Tools |
|------|-------|
| **Enterprise BI (paid)** | [Tableau](https://www.tableau.com/), [Power BI](https://powerbi.microsoft.com/), [Looker](https://cloud.google.com/looker), ThoughtSpot, Mode, Hex, Sigma. |
| **OSS BI** | [Metabase](https://www.metabase.com/), [Apache Superset](https://github.com/apache/superset), Lightdash. |
| **Hosted / Managed OSS** | [Preset](https://preset.io/) (managed Superset), Lightdash Cloud. |
| **AI-powered BI** | ThoughtSpot (AI-augmented search), Mode AI, Hex (AI notebooks). |
| **Semantic layer** | [Cube](https://cube.dev/), dbt Semantic Layer, LookML. |

### Semantic layer (the 2026 hotness)

The **semantic layer** is a translation between warehouse tables and business definitions:

- **dbt Semantic Layer** (MetricFlow) — define metrics once in dbt, query from any BI tool.
- **Cube** — semantic layer for any BI tool; TypeScript / Python.
- **LookML** — Looker's purpose-built modeling language.
- **Tableau Calculated Fields** — Tableau-native.

This is the answer to "what does 'active user' mean?" — defined once, used everywhere.

### BI tool comparison (2026)

| Tool | Strength | Weakness | Best for |
|------|----------|----------|----------|
| **Tableau** | Best visualization; rich analysis. | Expensive; steep learning curve. | Enterprise analytics teams. |
| **Power BI** | Microsoft integration; cheap. | Visualization weaker than Tableau. | Microsoft shops. |
| **Looker** | Code-based modeling (LookML); embedded analytics. | Developer-heavy; needs data team. | Data teams + embedded SaaS. |
| **Metabase** | Easiest to deploy; OSS; great for non-technical users. | Less viz power than Tableau. | Startups; OSS preference. |
| **Superset** | Rich viz; OSS; Airbnb-origin. | Ops complexity. | OSS shops with engineering teams. |
| **Lightdash** | dbt-native; OSS; semantic layer built-in. | Younger; smaller community. | dbt shops. |
| **ThoughtSpot** | AI search; natural-language queries. | Enterprise pricing. | Enterprises wanting AI-first BI. |
| **Mode / Hex** | Notebook-style + viz; Python integration. | Less polished for pure dashboards. | Data scientists + analysts. |

Adoption: Power BI is the **#1 BI tool by market share** (Microsoft); Tableau is #2; Looker is the leader for embedded SaaS analytics; Metabase has >40K OSS deployments.

## When To Use It

### Tableau / Power BI / Looker
- **Enterprise** with dedicated analytics team.
- **Self-service** for business users.
- **Embedded analytics** (Looker, Cube).
- **You need mature governance + security.**

### Metabase / Superset / Lightdash
- **OSS preference.**
- **Startup / mid-market.**
- **You want quick setup + low ops cost** (Metabase).
- **You're a dbt shop** (Lightdash).

### ThoughtSpot / Mode AI / Hex
- **AI-first queries** (natural language).
- **Mixed technical + business audiences.**

### Cube / dbt Semantic Layer
- **Multiple BI tools** consuming the same definitions.
- **You want one source of truth** for metrics.

## When NOT To Use It

### Tableau / Power BI
- **Tiny team / OSS preference** — Metabase / Superset is cheaper.
- **You want quick setup** — Tableau deployment is heavy.

### Metabase / Superset
- **You need rich enterprise viz** — Tableau wins.
- **You need LookML-style code-based modeling** — Looker wins.

### Looker
- **No data team to maintain LookML** — too developer-heavy.

### Any BI tool
- **You don't have a data warehouse** — BI reads from warehouses.
- **You have <100 users** — Excel / Google Sheets may be enough.

## Why It Matters in 2026

Three forces:

1. **AI is augmenting BI.** Natural-language queries ("show me revenue by region last quarter") are real in 2026. ThoughtSpot, Mode AI, Hex AI, Power BI Copilot — AI is becoming a first-class BI feature.
2. **Semantic layers are the new gold.** "What does active user mean?" should be answered once. dbt Semantic Layer + Cube are the emerging standards.
3. **OSS BI matured.** Metabase + Superset + Lightdash can compete with Tableau for most use cases, at 10% the cost.

Practitioner playbook in 2026:
1. **Default for startups**: **Metabase** or **Lightdash** (dbt-native).
2. **Default for enterprise**: **Tableau** (best viz) or **Power BI** (Microsoft shops).
3. **For embedded SaaS analytics**: **Looker** or **Cube**.
4. **Semantic layer**: Define metrics in dbt Semantic Layer or Cube; consume from BI tools.
5. **AI features**: pick a BI tool with strong AI (Tableau Pulse, Power BI Copilot, ThoughtSpot).

## Scoring Matrix (0–100)

### Tableau
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 20+ years old; the gold standard for viz. |
| Community | 95 | Massive; certifications; conferences. |
| Learning curve | 60 | Steep; powerful but complex. |
| Performance | 90 | In-memory engine; handles millions of rows. |
| Cost | 50 | Expensive; per-user pricing. |
| DX | 90 | Best viz UX in the industry. |
| Production readiness | 100 | Standard in enterprise. |

### Metabase
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 85 | 10+ years; battle-tested. |
| Community | 90 | OSS community; loved by startups. |
| Learning curve | 90 | Easy to set up; easy for non-technical users. |
| Performance | 80 | Handles most use cases; struggles at very large scale. |
| Cost | 95 | OSS free; paid tiers reasonable. |
| DX | 90 | Easiest BI to deploy. |
| Production readiness | 90 | Used at thousands of startups. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Tableau** | Enterprise; rich viz. | OSS / cost-sensitive. |
| **Power BI** | Microsoft shop. | OSS / best viz. |
| **Looker** | Embedded SaaS; data team. | Startup with no data team. |
| **Metabase** | Startup; OSS preference. | Enterprise governance. |
| **Superset** | OSS with engineering team. | Non-technical users. |
| **Lightdash** | dbt shop; OSS. | Enterprise compliance. |
| **ThoughtSpot** | AI-first queries. | OSS preference. |
| **Excel / Sheets** | Ad-hoc personal analysis. | Real BI / multiple users. |

## Sources

- [Tableau Learning](https://www.tableau.com/learn) — 2026
- [Tableau](https://www.tableau.com/) — 2026
- [Power BI](https://powerbi.microsoft.com/) — 2026
- [Power BI Learning](https://powerbi.microsoft.com/learning/) — 2026
- [Google Cloud Looker](https://cloud.google.com/looker) — 2026
- [Looker Docs](https://cloud.google.com/looker/docs) — 2026
- [Metabase](https://www.metabase.com/) — 2026
- [Metabase GitHub (metabase/metabase)](https://github.com/metabase/metabase) — 2026
- [Apache Superset GitHub](https://github.com/apache/superset) — 2026
- [Preset](https://preset.io/) — 2026
- [Lightdash Docs](https://docs.lightdash.com/) — 2026
- [Lightdash GitHub (lightdash/lightdash)](https://github.com/lightdash/lightdash) — 2026
- [Cube](https://cube.dev/) — 2026
- [Cube GitHub (cube-js/cube.js)](https://github.com/cube-js/cube.js) — 2026
- [ThoughtSpot](https://www.thoughtspot.com/) — 2026
- [Mode](https://mode.com/) — 2026
- [Hex](https://hex.tech/) — 2026
- [Snowflake Docs](https://docs.snowflake.com/) — 2026