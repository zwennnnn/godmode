---
name: SQL Deep Dive
category: databases
status: researched
last-updated: 2026-07-30
sources:
  - https://en.wikipedia.org/wiki/SQL
  - https://www.postgresql.org/docs/current/sql.html
  - https://www.postgresql.org/docs/
  - https://dev.mysql.com/doc/refman/8.0/en/
  - https://learn.microsoft.com/en-us/sql/t-sql/language-reference
  - https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/
  - https://mode.com/sql-tutorial
  - https://selectstarsql.com/
  - https://pgexercises.com/
  - https://github.com/pgexercises/exercises
  - https://use-the-index-luke.com/
  - https://www.sqlite.org/lang.html
  - https://github.com/Xe/hoard
  - https://sqlbolt.com/
  - https://www.khanacademy.org/computing/computer-programming/sql
tags: [sql, postgresql, mysql, sql-server, oracle, query-optimization, indexing, joins]
---

# SQL Deep Dive

## One-liner

The structured query language that powers relational databases — mastering SQL beyond `SELECT *` is the single highest-ROI skill for anyone working with data.

## What It Is

SQL (Structured Query Language) has been the standard for relational databases since the 1970s. Modern SQL is far more powerful than the basics — window functions, CTEs, recursive queries, JSON operators, full-text search, and more.

The 2026 SQL dialects:

| Dialect | Vendor | Notes |
|---------|--------|-------|
| **PostgreSQL SQL** | Postgres (open source) | Most-feature-rich SQL; the modern default. |
| **MySQL SQL** | Oracle (open source) | The classic; widely deployed; simpler than PG. |
| **T-SQL** | Microsoft SQL Server | Enterprise; rich procedural extensions. |
| **PL/SQL** | Oracle | Enterprise; procedural extensions. |
| **SQLite SQL** | SQLite | Embedded; subset of PG/MySQL. |
| **ANSI SQL** | Standard | The common subset; portable across vendors. |

### Core SQL skill set (the non-negotiables)

| Skill | Examples |
|-------|----------|
| **CRUD** | `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `MERGE` (UPSERT). |
| **Filtering** | `WHERE`, `AND/OR/NOT`, `IN`, `BETWEEN`, `LIKE`, `ILIKE`, `IS NULL`. |
| **Joins** | `INNER`, `LEFT/RIGHT/FULL OUTER`, `CROSS`, `SELF`, lateral joins. |
| **Aggregation** | `GROUP BY`, `HAVING`, `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`, `ARRAY_AGG`, `STRING_AGG`, `PERCENTILE_CONT`. |
| **Subqueries** | Scalar, correlated, `IN`, `EXISTS`. |
| **CTEs** | `WITH ... AS` — readable subqueries. |
| **Window functions** | `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, `LEAD`, `FIRST_VALUE`, `LAST_VALUE`, `NTILE`, `SUM() OVER`, `AVG() OVER`. |
| **Set ops** | `UNION`, `INTERSECT`, `EXCEPT`. |
| **Joins revisited** | Lateral joins; LATERAL correlated subqueries. |
| **JSON** | `->`, `->>`, `@>`, `JSONB_PATH_QUERY` (Postgres). |
| **Full-text** | `to_tsvector`, `to_tsquery`, `@@` (Postgres). |
| **Recursive CTEs** | `WITH RECURSIVE`. |
| **Pivot / Unpivot** | (DB-specific). |
| **Indexes** | B-tree, Hash, GIN, GiST, BRIN; partial indexes; expression indexes. |
| **Explain plans** | `EXPLAIN ANALYZE` — read query plans. |
| **Transactions** | `BEGIN`, `COMMIT`, `ROLLBACK`; isolation levels. |
| **Constraints** | `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `CHECK`, `NOT NULL`. |
| **Views + Materialized Views**. |
| **Common Table Expressions (CTEs) vs Subqueries vs Temp Tables.** |

### The skill ladder

| Level | You can... |
|-------|-----------|
| **Beginner** | Write `SELECT ... WHERE ... GROUP BY`. |
| **Intermediate** | Joins, CTEs, window functions, indexes. |
| **Advanced** | Recursive CTEs, JSON operators, query plan optimization, materialized views, partitioning. |
| **Expert** | Locking semantics, isolation levels, replication, custom indexes (GIN/GiST), extension development. |

### Why SQL beats ORMs (most of the time)

- **SQL is set-based** — operations on whole result sets; ORMs often fall back to row-by-row.
- **SQL is declarative** — describe *what* you want, not *how* to get it.
- **SQL is portable** — same skills across vendors.
- **SQL is the lingua franca** — every BI tool, every data tool, every DBA speaks it.

Adoption: SQL is the **#2 most-used language** in the world (per Stack Overflow surveys). Every backend developer, every analyst, every data engineer uses it daily. PostgreSQL SQL is the modern default.

## When To Use It

- **Any relational database** — SQL is the only option.
- **Data analysis** — SQL is the most efficient tool for warehouse queries.
- **OLTP backends** — every CRUD app uses SQL.
- **Reporting** — SQL is the foundation.
- **Data engineering** — dbt is SQL.
- **AI/ML pipelines** — feature extraction via SQL is real.

## When NOT To Use It

- **Document data with no relations** — MongoDB / CouchDB.
- **OLAP at petabyte scale** — ClickHouse / BigQuery have SQL but different paradigms.
- **Graph traversal** — Neo4j Cypher, GQL.
- **Time-series** — InfluxQL / Flux.
- **Search** — Elasticsearch DSL (or just use SQL if PG FTS suffices).

## Why It Matters in 2026

Three forces:

1. **PostgreSQL dominated.** The features (window functions, CTEs, JSONB, FTS, generated columns, partitioning) made PG the default. Knowing PG SQL = knowing the most-feature-rich SQL.
2. **AI-assisted SQL matured.** Text-to-SQL is real in 2026 (BigQuery, Snowflake Cortex, natural-language query). But knowing SQL is still required to verify + iterate.
3. **The data stack is SQL-centric.** dbt is SQL. Modern data warehouses are SQL. ETL tools accept SQL. SQL is the universal data language.

Practitioner playbook in 2026:
1. **Master Postgres SQL** — the most-feature-rich.
2. **Practice on real datasets** — LeetCode SQL, pgexercises.com, Mode tutorial.
3. **Read query plans** — `EXPLAIN ANALYZE` is the most important command for performance.
4. **Understand indexes** — B-tree default; GIN for JSON + FTS; BRIN for time-series.
5. **Know window functions** — they're the most powerful SQL feature.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 50+ years old; the standard. |
| Community | 100 | Massive; every backend / data engineer uses it. |
| Learning curve | 70 | Basics easy; advanced takes study. |
| Performance | 95 | Modern query planners are excellent; indexed queries are fast. |
| Cost | 100 | Free; built into every DB. |
| DX | 85 | pgcli / modern tools are great; psql works. |
| Production readiness | 100 | The default for OLTP + analytics. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **NoSQL (MongoDB, DynamoDB)** | Document data; horizontal scale. | You need joins + transactions. |
| **ORM (Prisma, SQLAlchemy, Hibernate)** | You want object-oriented code. | You need complex queries; performance matters. |
| **OLAP SQL (BigQuery, ClickHouse)** | Petabyte analytics. | OLTP / low-latency queries. |
| **Graph query (Cypher, GQL)** | Graph traversal. | Tabular data. |
| **pandas / Polars** | Local analysis. | Server-side data. |

## Sources

- [Wikipedia — SQL](https://en.wikipedia.org/wiki/SQL) — 2026
- [PostgreSQL SQL Reference](https://www.postgresql.org/docs/current/sql.html) — 2026
- [PostgreSQL Docs](https://www.postgresql.org/docs/) — 2026
- [MySQL Reference Manual](https://dev.mysql.com/doc/refman/8.0/en/) — 2026
- [T-SQL Reference (Microsoft)](https://learn.microsoft.com/en-us/sql/t-sql/language-reference) — 2026
- [Oracle SQL Reference](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/) — 2026
- [Mode SQL Tutorial](https://mode.com/sql-tutorial) — 2026
- [Select Star SQL](https://selectstarsql.com/) — 2026
- [PGExercises](https://pgexercises.com/) — 2026
- [PGExercises GitHub (pgexercises/exercises)](https://github.com/pgexercises/exercises) — 2026
- [Use The Index, Luke (Markus Winand)](https://use-the-index-luke.com/) — 2026
- [SQLite SQL](https://www.sqlite.org/lang.html) — 2026
- [SQLBolt](https://sqlbolt.com/) — 2026
- [Khan Academy — SQL](https://www.khanacademy.org/computing/computer-programming/sql) — 2026