---
name: Data Analytics
category: data-ai
status: researched
last-updated: 2026-07-30
sources:
  - https://en.wikipedia.org/wiki/Data_analysis
  - https://www.sql.org/
  - https://www.postgresql.org/docs/
  - https://mode.com/sql-tutorial
  - https://github.com/cfpb/dbt-tutorial
  - https://pandas.pydata.org/
  - https://numpy.org/
  - https://duckdb.org/
  - https://duckdb.org/docs/
  - https://www.kaggle.com/learn
  - https://www.tableau.com/learn
  - https://powerbi.microsoft.com/learning/
  - https://www.looker.com/training
  - https://www.metabase.com/
  - https://github.com/metabase/metabase
  - https://preset.io/
  - https://github.com/apache/superset
  - https://www.khanacademy.org/math/statistics-probability
tags: [data-analytics, sql, pandas, numpy, duckdb, excel, sheets, kaggle, statistics, visualization]
---

# Data Analytics

## One-liner

Turning raw data into insights for business decisions — SQL, statistics, and visualization are the core toolkit; the modern analyst works in a warehouse + BI tool, not Excel.

## What It Is

Data analytics is the practice of asking questions of data and communicating the answers. It spans four layers:

1. **Data extraction** — SQL queries against the warehouse.
2. **Analysis** — statistics, segmentation, funnel analysis, cohort analysis.
3. **Visualization** — charts, dashboards, narratives.
4. **Communication** — reports, presentations, decisions.

The 2026 baseline:

| Skill | Tools |
|-------|-------|
| **SQL** | Postgres, Snowflake, BigQuery, DuckDB (local) |
| **Statistics** | Probability, hypothesis testing, regression, A/B testing |
| **Data manipulation** | Pandas (Python), Polars, DuckDB, R, Excel |
| **Visualization** | Tableau, Power BI, Looker, Metabase, Apache Superset, Observable |
| **Narrative** | Reports, dashboards, presentations |
| **Domain knowledge** | Product analytics, growth, finance, marketing |

### Career levels (per [Kaggle Learn](https://www.kaggle.com/learn), [Mode SQL Tutorial](https://mode.com/sql-tutorial))

| Level | What you do | Tools |
|-------|-------------|-------|
| **Analyst** | Pull data; build reports; answer ad-hoc questions. | SQL, spreadsheets, basic BI. |
| **Senior Analyst** | Own metrics; design experiments; mentor. | SQL (advanced), statistics, BI tools. |
| **Analytics Engineer** | Build the data models; own dbt; bridge analyst + engineer. | dbt, SQL, Python. |
| **Data Scientist** | Predictive modeling; ML; causal inference. | Python (pandas, scikit-learn), statistics. |
| **Analytics Lead / Manager** | Set team strategy; communicate with executives. | Mix + people skills. |

### Dominant SQL skills (the non-negotiables)
- `SELECT`, `WHERE`, `GROUP BY`, `ORDER BY`, `LIMIT`, `JOIN` (INNER / LEFT / RIGHT / FULL).
- Aggregates: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`, `ARRAY_AGG`.
- Window functions: `ROW_NUMBER`, `RANK`, `LAG`, `LEAD`, `FIRST_VALUE`, `SUM() OVER`.
- CTEs (`WITH ... AS`).
- Self joins.
- Date / time functions.
- String functions.
- Pivoting + unpivoting.
- Query plan analysis (`EXPLAIN ANALYZE`).

### Dominant visualization tools (2026)

| Tool | Sweet spot |
|------|------------|
| **[Tableau](https://www.tableau.com/learn)** | Enterprise BI; rich viz; mature. |
| **[Power BI](https://powerbi.microsoft.com/learning/)** | Microsoft shop; good Excel integration. |
| **[Looker](https://www.looker.com/training)** | LookML (code-based modeling); Google Cloud. |
| **[Metabase](https://www.metabase.com/)** | OSS; easy to deploy; loved by startups. |
| **[Apache Superset](https://github.com/apache/superset)** | OSS; Airbnb-origin; rich viz. |
| **[Preset](https://preset.io/)** | Managed Superset. |
| **Observable / Hex / Mode** | Notebook-style analytics + viz. |
| **Streamlit / Dash** | Python-built custom dashboards. |

Adoption: Data analytics is one of the largest tech disciplines. Tableau has >100K customers; Power BI is the #1 BI tool by market share; SQL is the #2 most-used language in the world; every company has analysts.

## When To Use It

- **You're making business decisions** — every claim should be backed by data.
- **You want to measure product / growth / operations** — analytics is the answer.
- **You want to do A/B testing** — statistics + experimentation.
- **You're a data analyst** — these are your core tools.
- **You're a product manager / engineer / founder** — basic data literacy is required.

## When NOT To Use It

- **You don't have data** — analyze first when you have it.
- **You need real-time predictions** — that's ML (data scientist).
- **You're shipping a feature** — engineering, not analytics.
- **You just want to look at data** — direct DB query is fine.

## Why It Matters in 2026

Three forces:

1. **SQL + a modern warehouse is the default.** Snowflake / BigQuery + dbt + Metabase / Tableau is the modern analyst stack. Spreadsheet-dependent analysts are being replaced.
2. **AI tools amplify analysts.** Natural language to SQL (e.g. Text-to-SQL in BigQuery, Snowflake Cortex) lets analysts move faster. But knowing SQL is still required to verify + iterate.
3. **Causal inference + experimentation matter more.** Beyond "what happened" — analysts are increasingly doing "why" and "what if" work via A/B tests, causal DAGs, uplift modeling.

Practitioner playbook in 2026:
1. **SQL** — non-negotiable; master window functions + CTEs.
2. **Statistics** — at minimum A/B testing, regression, hypothesis testing.
3. **Python or R** — pandas / NumPy for data manipulation; scikit-learn for ML.
4. **Visualization** — pick one BI tool + learn it deeply (Tableau / Power BI / Metabase).
5. **dbt** — for analytics engineers building the data models.
6. **Domain** — pick a domain (product, growth, finance, marketing) and go deep.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | Excel (1985); SQL (1986); Tableau (2003); mature. |
| Community | 100 | Massive; Tableau / Power BI / Looker / Metabase all huge. |
| Learning curve | 65 | SQL is easy to start; statistics + viz tools take study. |
| Performance | 90 | Warehouses scale to petabytes; BI tools handle millions of rows. |
| Cost | 80 | BI tools are paid; OSS alternatives exist. |
| DX | 80 | Tableau + Looker excellent; Power BI learning curve. |
| Production readiness | 100 | Every company has analysts; every BI tool is in production. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Just use Excel** | Ad-hoc personal analysis. | Real analytics at scale. |
| **ML / Data Science** | Predictive work. | Descriptive + diagnostic work (analytics). |
| **Business intelligence consultant** | Small company, no in-house analyst. | Medium+ company; full-time hire is cheaper. |
| **No analytics (gut feel)** | Never. | Always. |

## Sources

- [Wikipedia — Data Analysis](https://en.wikipedia.org/wiki/Data_analysis) — 2026
- [SQL.org](https://www.sql.org/) — 2026
- [PostgreSQL Docs](https://www.postgresql.org/docs/) — 2026
- [Mode SQL Tutorial](https://mode.com/sql-tutorial) — 2026
- [dbt Tutorial (cfpb)](https://github.com/cfpb/dbt-tutorial) — 2026
- [pandas](https://pandas.pydata.org/) — 2026
- [NumPy](https://numpy.org/) — 2026
- [DuckDB](https://duckdb.org/) — 2026
- [DuckDB Docs](https://duckdb.org/docs/) — 2026
- [Kaggle Learn](https://www.kaggle.com/learn) — 2026
- [Tableau Learning](https://www.tableau.com/learn) — 2026
- [Power BI Learning](https://powerbi.microsoft.com/learning/) — 2026
- [Looker Training](https://www.looker.com/training) — 2026
- [Metabase](https://www.metabase.com/) — 2026
- [Metabase GitHub (metabase/metabase)](https://github.com/metabase/metabase) — 2026
- [Preset](https://preset.io/) — 2026
- [Apache Superset GitHub](https://github.com/apache/superset) — 2026
- [Khan Academy — Statistics & Probability](https://www.khanacademy.org/math/statistics-probability) — 2026