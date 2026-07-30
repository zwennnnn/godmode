---
name: ClickHouse
category: databases
status: researched
last-updated: 2026-07-30
sources:
  - https://clickhouse.com/
  - https://clickhouse.com/docs/
  - https://github.com/ClickHouse/ClickHouse
  - https://clickhouse.com/docs/en/sql-reference/
  - https://clickhouse.com/docs/en/operations/
  - https://clickhouse.com/docs/en/engines/
  - https://clickhouse.com/cloud
  - https://clickhouse.com/company
  - https://clickhouse.com/docs/en/operations/tips/
  - https://github.com/ClickHouse/clickhouse-go
  - https://github.com/ClickHouse/clickhouse-js
  - https://clickhouse.com/docs/en/integrations/
  - https://github.com/Altinity/clickhouse-backup
  - https://www.tinybird.co/
  - https://docs.peerdb.io/
  - https://github.com/ClickHouse/ch-go
tags: [clickhouse, olap, columnar, analytics, real-time, sql, time-series]
---

# ClickHouse

## One-liner

The fastest open-source column-oriented OLAP database — petabyte-scale real-time analytics with SQL, originally built at Yandex for their analytics product and now the default for high-throughput analytical workloads.

## What It Is

ClickHouse is a column-oriented DBMS designed for **online analytical processing (OLAP)** at scale — fast aggregation queries over billions to trillions of rows, with sub-second response times. It's the dominant open-source OLAP database, used by everyone who outgrows Postgres + dbt.

The 2026 baseline is **ClickHouse 24+ / 25+** with:

- **MergeTree engine** family — the default; column-oriented + sparse indexing + background merges.
- **Real-time ingestion** — direct inserts, Kafka engine, MaterializedPostgreSQL (CDC).
- **SQL dialect** — mostly PostgreSQL-compatible + ClickHouse extensions.
- **Distributed tables** — sharding + replication across clusters.
- **Materialized views** — for pre-aggregation.
- **Dictionary** — in-memory key-value for joins.
- **External data sources** — PostgreSQL, MySQL, Kafka, S3.
- **ClickHouse Cloud** — fully managed; serverless option.
- **JSON / JSONEachRow** — flexible schema; semi-structured data.
- **Vector search** — k-NN + ANN; competes with Elasticsearch for hybrid retrieval.
- **ChDB** — embedded ClickHouse (like SQLite).

Adoption: ClickHouse is the **fastest-growing OLAP database**. Used by Uber, Cloudflare, Discord, eBay, GitLab, LinkedIn, Spotify, Lyft, every high-scale analytics shop. ~10K+ GitHub stars; massive community.

## When To Use It

- **OLAP at scale** — billions of rows, sub-second aggregations.
- **Real-time analytics** — events, logs, metrics; ingest + query.
- **Time-series** — better than InfluxDB / TimescaleDB for high cardinality.
- **Log analytics alternative** — ClickHouse + Grafana vs ELK.
- **Product analytics** — events stream, dashboards.
- **AI observability** — vector + structured data in one.
- **Embedded analytics** — ChDB for in-process.

## When NOT To Use It

- **OLTP** — no high-concurrency single-row updates.
- **You don't have scale** — Postgres + dbt is simpler.
- **Strong transactions** — not its strength; use Postgres.
- **You need real-time + transactional + joins** — use Postgres for OLTP, sync to ClickHouse for analytics.
- **Tiny dataset** — overkill.

## Why It Matters in 2026

Three forces:

1. **OLAP workloads demand column-oriented storage.** Row-oriented DBs (Postgres) are great for OLTP but slow for analytics on huge tables. ClickHouse is the standard for the analytical side.
2. **Real-time + OLAP converged.** MaterializedPostgreSQL + Kafka engines let you query live data with sub-second freshness, no ETL delay.
3. **ClickHouse Cloud + open formats.** Managed ClickHouse + Iceberg/Delta integration means you can query open table formats directly.

Practitioner playbook in 2026:
1. **Schema design**: wide tables, ORDER BY chosen for query patterns.
2. **Engines**: MergeTree (default), ReplacingMergeTree (dedup), SummingMergeTree, AggregatingMergeTree.
3. **Materialized views**: pre-aggregate for dashboards.
4. **Ingestion**: direct INSERT, Kafka, MaterializedPostgreSQL (CDC from Postgres).
5. **Managed**: ClickHouse Cloud (serverless) or Tinybird (HTTP API).

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 90 | 10+ years old; Yandex origin; battle-tested. |
| Community | 95 | Massive; fastest-growing OLAP DB. |
| Learning curve | 65 | SQL + engines + sharding + materialized views take study. |
| Performance | 100 | The fastest OLAP DB on the market. |
| Cost | 80 | Self-host cheap; managed serverless reasonable. |
| DX | 80 | SQL dialect; excellent docs; cloud UI polished. |
| Production readiness | 95 | Used at every hyperscale. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Postgres + dbt** | Small scale; you already have Postgres. | You have billions of rows. |
| **Snowflake / BigQuery / Redshift** | Serverless / managed; you want zero ops. | Self-host / cost-sensitive. |
| **Apache Druid** | Real-time + OLAP. | You want pure SQL. |
| **TimescaleDB** | Time-series with Postgres compatibility. | You need true column-oriented + distributed. |
| **DuckDB** | Embedded OLAP; local analytics. | Distributed; production scale. |
| **Elasticsearch** | Full-text + log search. | You need SQL aggregations. |

## Sources

- [ClickHouse](https://clickhouse.com/) — 2026
- [ClickHouse Docs](https://clickhouse.com/docs/) — 2026
- [ClickHouse GitHub (ClickHouse/ClickHouse)](https://github.com/ClickHouse/ClickHouse) — 2026
- [SQL Reference](https://clickhouse.com/docs/en/sql-reference/) — 2026
- [Operations Docs](https://clickhouse.com/docs/en/operations/) — 2026
- [Table Engines](https://clickhouse.com/docs/en/engines/) — 2026
- [ClickHouse Cloud](https://clickhouse.com/cloud) — 2026
- [ClickHouse Company](https://clickhouse.com/company) — 2026
- [Performance Tips](https://clickhouse.com/docs/en/operations/tips/) — 2026
- [clickhouse-go (GitHub ClickHouse/clickhouse-go)](https://github.com/ClickHouse/clickhouse-go) — 2026
- [clickhouse-js (GitHub ClickHouse/clickhouse-js)](https://github.com/ClickHouse/clickhouse-js) — 2026
- [Integrations](https://clickhouse.com/docs/en/integrations/) — 2026
- [clickhouse-backup (Altinity)](https://github.com/Altinity/clickhouse-backup) — 2026
- [Tinybird](https://www.tinybird.co/) — 2026
- [PeerDB](https://docs.peerdb.io/) — 2026
- [ch-go (GitHub ClickHouse/ch-go)](https://github.com/ClickHouse/ch-go) — 2026