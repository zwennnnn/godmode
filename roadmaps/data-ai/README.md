---
name: Data Engineering, Analytics, and MLOps
slug: data-ai
source: https://roadmap.sh/data-engineer + https://roadmap.sh/data-analyst + https://roadmap.sh/bi-analyst + https://roadmap.sh/mlops + https://roadmap.sh/machine-learning
last-updated: 2026-07-30
tech-count: 4
status: in-progress
---

# Data Engineering, Analytics, and MLOps

> **Category:** The data stack for building, deploying, and operating data pipelines, analytics dashboards, and machine learning systems in production.
> **Sources:** [roadmap.sh/data-engineer](https://roadmap.sh/data-engineer), [roadmap.sh/data-analyst](https://roadmap.sh/data-analyst), [roadmap.sh/bi-analyst](https://roadmap.sh/bi-analyst), [roadmap.sh/mlops](https://roadmap.sh/mlops), [roadmap.sh/machine-learning](https://roadmap.sh/machine-learning)

This roadmap covers the people + systems that turn raw data into dashboards, reports, and ML-powered features. Note: AI/ML/LLM application development is covered separately in [`../ai-ml-llm/`](../ai-ml-llm/); this roadmap focuses on the data platform, analytics, and ML operations layer.

---

## Technologies (build order)

| # | Technology | File | Status |
|---|-----------|------|--------|
| 1 | Data Engineering (ETL / Pipelines) | [data-engineering.md](data-engineering.md) | placeholder |
| 2 | Data Analytics (SQL + Visualization) | [data-analytics.md](data-analytics.md) | placeholder |
| 3 | BI & Reporting (Tableau / Power BI / Looker) | [bi-reporting.md](bi-reporting.md) | placeholder |
| 4 | MLOps (Model Deployment / Monitoring / Feature Stores) | [mlops.md](mlops.md) | placeholder |

---

## Quick Decision Guide

### If you're building data pipelines (ETL / ELT)

Start with **Data Engineering** ([data-engineering.md](data-engineering.md)). Modern stack: Fivetran/Airbyte + Snowflake/BigQuery/Databricks + dbt + Prefect/Dagster.

### If you're an analyst / business user

Start with **Data Analytics** ([data-analytics.md](data-analytics.md)). Master SQL + stats + a BI tool (Tableau / Power BI / Metabase).

### If you're an enterprise BI / reporting team

**BI & Reporting** ([bi-reporting.md](bi-reporting.md)). Tableau / Power BI / Looker / Metabase / Lightdash.

### If you ship ML models to production

**MLOps** ([mlops.md](mlops.md)). MLflow + dbt + BentoML or vLLM + Arize/Evidently.

### If you do AI/ML/LLM applications (prompts, RAG, agents)

See [`../ai-ml-llm/README.md`](../ai-ml-llm/README.md) for the LLM-specific layer. This roadmap is for the data + classical ML platform.

---

## Cross-references

- For LLM application development, see [`../ai-ml-llm/README.md`](../ai-ml-llm/README.md).
- For databases (Postgres, ClickHouse, etc.), see [`../databases/README.md`](../databases/README.md).
- For Python (the dominant language here), see [`../programming-languages/python.md`](../programming-languages/python.md).

---

## Build progress

**Phase 8 in progress** as of 2026-07-30. See [`../godmode.md`](../godmode.md) under `## Progress Tracker`.