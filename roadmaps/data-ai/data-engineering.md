---
name: Data Engineering
category: data-ai
status: researched
last-updated: 2026-07-30
sources:
  - https://www.dataengineeringweekly.org/
  - https://github.com/dbt-labs/dbt-core
  - https://docs.getdbt.com/
  - https://spark.apache.org/docs/latest/
  - https://airflow.apache.org/docs/
  - https://github.com/apache/airflow
  - https://github.com/prefecthq/prefect
  - https://docs.prefect.io/
  - https://github.com/dagster-io/dagster
  - https://docs.dagster.io/
  - https://www.kestra.io/
  - https://github.com/kestra-io/kestra
  - https://www.postgresql.org/docs/
  - https://docs.snowflake.com/
  - https://docs.aws.amazon.com/glue/
  - https://cloud.google.com/dataflow
  - https://delta.io/
  - https://github.com/delta-io/delta
tags: [data-engineering, etl, elt, dbt, spark, airflow, prefect, dagster, pipelines, data-warehouse]
---

# Data Engineering

## One-liner

Building the pipelines, warehouses, and infrastructure that turn raw data into trusted, queryable data products — the foundation for analytics, ML, and business decisions.

## What It Is

Data engineering is the discipline of building **reliable, scalable data pipelines** that move data from source systems (apps, databases, APIs, events) into a warehouse / lake where it can be queried for analytics, BI, ML, and operational use.

### The modern data stack (2026)

| Layer | Tools |
|-------|-------|
| **Sources** | Operational DBs (Postgres), SaaS APIs (Stripe, Salesforce, HubSpot), event streams (Kafka), app logs. |
| **Ingestion** | Fivetran, Airbyte, Stitch (managed); custom Kafka consumers; CDC (Debezium). |
| **Storage** | Data warehouse (Snowflake, BigQuery, Redshift, Databricks); data lake (S3, GCS, Delta Lake, Iceberg). |
| **Transformation** | **dbt** (SQL + tests + docs), Spark, Flink (for streaming). |
| **Orchestration** | **Airflow**, **Prefect**, **Dagster**, Kestra. |
| **Quality** | dbt tests, Great Expectations, Soda, Monte Carlo. |
| **Lineage** | OpenLineage, DataHub, Atlan. |
| **Reverse ETL** | Hightouch, Census (sync warehouse back to SaaS). |

### Key concepts

| Concept | Description |
|---------|-------------|
| **ETL** vs **ELT** | ETL = transform before load (legacy). ELT = load raw, transform in warehouse (modern default). |
| **CDC** (Change Data Capture) | Stream row-level changes from source DB. Debezium is the open-source default. |
| **Batch vs Streaming** | Batch = periodic (hourly). Streaming = continuous (Kafka + Flink). |
| **Lakehouse** | Lake + warehouse — Delta Lake, Iceberg, Apache Hudi. |
| **Star schema / Snowflake schema** | Fact tables + dimension tables. |
| **Slowly Changing Dimensions (SCD)** | Track historical changes in dim tables (SCD Type 1/2/3/4/6). |
| **Idempotency** | Re-running a pipeline produces the same result. |
| **Data contracts** | Schema + SLA agreement between producer and consumer. |
| **Medallion architecture** | Bronze (raw) → Silver (cleaned) → Gold (aggregated). |
| **Data mesh** | Domain-oriented decentralized data ownership (Zhamak Dehghani). |

### Dominant tools in 2026

| Tool | Role |
|------|------|
| **[dbt](https://www.getdbt.com/)** | SQL-based transformations with tests + docs + lineage. The default. |
| **[Apache Airflow](https://airflow.apache.org/)** | Python-based orchestration; the legacy default; complex. |
| **[Prefect](https://www.prefect.io/)** | Modern orchestration; Pythonic; less ops overhead than Airflow. |
| **[Dagster](https://dagster.io/)** | Asset-centric orchestration; software-engineered approach. |
| **[Apache Spark](https://spark.apache.org/)** | Distributed processing for big data. |
| **[Delta Lake](https://delta.io/)** | Lakehouse storage format with ACID. |
| **Snowflake / BigQuery / Databricks** | Managed warehouses. |

Adoption: Data engineering is one of the fastest-growing engineering disciplines. Every company with significant data has a data engineering team. The dbt community alone has >50K practitioners; Snowflake + Databricks + BigQuery are billion-dollar businesses.

## When To Use It

- **You have any data you want to analyze** — you need a pipeline.
- **You're building a data warehouse / lakehouse** — dbt + Snowflake/Databricks is the default.
- **You're doing ETL / ELT** — pick Airflow / Prefect / Dagster for orchestration.
- **You need real-time data** — Kafka + Flink.
- **You're migrating from a monolith to a data-driven architecture** — data mesh / data contracts.
- **You have data quality issues** — invest in tests + monitoring.

## When NOT To Use It

- **You're a tiny startup** — Fivetran + BigQuery + dbt + a single analyst is enough.
- **You don't have data** — premature.
- **You just need logs** — observability tools handle this.
- **You're over-engineering** — a cron + SQL script can be a "pipeline" early on.

## Why It Matters in 2026

Three forces:

1. **AI training runs on data pipelines.** Every LLM fine-tune, every ML model, every RAG system needs clean, fresh, queryable data. Data engineering is the upstream of every AI application.
2. **dbt became the lingua franca.** SQL-based transformations with version control + tests + docs + lineage. The "modern data stack" (Fivetran + Snowflake + dbt) is the default for new companies.
3. **Lakehouse + open table formats matured.** Delta Lake, Apache Iceberg, Apache Hudi — open table formats give warehouses ACID + lake flexibility. Snowflake + Databricks + BigQuery all support them.

Practitioner playbook in 2026:
1. **Modern data stack default**: Fivetran / Airbyte + Snowflake / BigQuery + dbt + Prefect / Dagster.
2. **Orchestration**: Prefect or Dagster (over Airflow for new projects).
3. **Transformations**: dbt for SQL; Spark for heavy distributed processing.
4. **Streaming**: Kafka + Flink / Materialize / RisingWave for real-time.
5. **Quality**: dbt tests + Great Expectations + Soda at ingest.
6. **Lineage**: OpenLineage + DataHub / Atlan.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 90 | ETL tools 20+ years; modern data stack 8+ years mature. |
| Community | 95 | Massive; dbt Slack has 80K+ members; conferences, blogs. |
| Learning curve | 55 | Many tools; SQL is easy, Spark/Airflow take study. |
| Performance | 90 | dbt + warehouse scales to petabytes. |
| Cost | 70 | Warehouses expensive at scale (Snowflake $$); Spark infra costs. |
| DX | 80 | dbt is excellent; Airflow is dated. |
| Production readiness | 95 | Used at every data-driven company. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Skip the warehouse; use app DBs** | Tiny projects. | You need analytics at scale. |
| **Hand-rolled ETL scripts** | One-off. | Production pipelines. |
| **NoSQL data lake** | Unstructured data only. | You need query power. |
| **Real-time only (Kafka + Flink)** | Real-time is the only requirement. | You also need batch + historical. |

## Sources

- [Data Engineering Weekly](https://www.dataengineeringweekly.org/) — 2026
- [dbt Core GitHub (dbt-labs/dbt-core)](https://github.com/dbt-labs/dbt-core) — 2026
- [dbt Docs](https://docs.getdbt.com/) — 2026
- [Apache Spark Docs](https://spark.apache.org/docs/latest/) — 2026
- [Apache Airflow Docs](https://airflow.apache.org/docs/) — 2026
- [Apache Airflow GitHub](https://github.com/apache/airflow) — 2026
- [Prefect GitHub (prefecthq/prefect)](https://github.com/prefecthq/prefect) — 2026
- [Prefect Docs](https://docs.prefect.io/) — 2026
- [Dagster GitHub (dagster-io/dagster)](https://github.com/dagster-io/dagster) — 2026
- [Dagster Docs](https://docs.dagster.io/) — 2026
- [Kestra](https://www.kestra.io/) — 2026
- [Kestra GitHub (kestra-io/kestra)](https://github.com/kestra-io/kestra) — 2026
- [PostgreSQL Docs](https://www.postgresql.org/docs/) — 2026
- [Snowflake Docs](https://docs.snowflake.com/) — 2026
- [AWS Glue](https://docs.aws.amazon.com/glue/) — 2026
- [Google Cloud Dataflow](https://cloud.google.com/dataflow) — 2026
- [Delta Lake](https://delta.io/) — 2026
- [Delta Lake GitHub (delta-io/delta)](https://github.com/delta-io/delta) — 2026