---
name: Elasticsearch
category: databases
status: researched
last-updated: 2026-07-30
sources:
  - https://www.elastic.co/elasticsearch
  - https://www.elastic.co/docs/
  - https://github.com/elastic/elasticsearch
  - https://www.elastic.co/docs/explore-analyze/query-filter/languages/querydsl
  - https://www.elastic.co/observability
  - https://www.elastic.co/security
  - https://opensearch.org/
  - https://github.com/opensearch-project/OpenSearch
  - https://www.elastic.co/blog/elastic-license-v2
  - https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html
  - https://www.elastic.co/docs/api/doc/elasticsearch/operation/search
  - https://github.com/elastic/elasticsearch-py
  - https://github.com/elastic/elasticsearch-js
  - https://www.elastic.co/downloads
  - https://opensearch.org/docs/latest/
  - https://www.elastic.co/blog/elastic-license-faq
tags: [elasticsearch, opensearch, search, full-text, observability, security, kibana, elastic-stack]
---

# Elasticsearch

## One-liner

The dominant distributed search + analytics engine — built on Apache Lucene, used for full-text search, log analytics (ELK), SIEM, APM, and increasingly for vector + generative AI search.

## What It Is

Elasticsearch is a distributed, RESTful search and analytics engine built on Apache Lucene. It stores documents as JSON, indexes them in a custom Lucene-based structure, and exposes a query DSL for full-text + structured + vector search.

The 2026 ecosystem (Elastic Stack / ELK / OpenSearch):

| Component | Notes |
|-----------|-------|
| **Elasticsearch** | The search engine. |
| **Kibana** | Visualization UI (dashboards, Canvas, Vega). |
| **Logstash** | Data ingestion pipeline (server-side). |
| **Beats** | Lightweight shippers (Filebeat, Metricbeat, etc.). |
| **Elastic Observability** | APM, logs, metrics, uptime, synthetics. |
| **Elastic Security** | SIEM, endpoint. |
| **Elasticsearch's vector search** | kNN + HNSW; competes with Pinecone / pgvector. |
| **Elastic's ES|QL** | New SQL-like query language (2023+). |
| **OpenSearch** | AWS-led open-source fork (Apache 2.0) after Elastic's 2021 license change. |
| **OpenSearch Dashboards** | Kibana-equivalent for OpenSearch. |

### License context
- **Elasticsearch 7.11+ (2021)** — Elastic changed license from Apache 2.0 to SSPL + Elastic License v2 (source-available, not OSI-open).
- **OpenSearch** — AWS forked Elasticsearch 7.10.2 and continued under Apache 2.0.
- **Both** continue to evolve; APIs largely compatible.

The 2026 baseline:
- **Elasticsearch 8.x** — vector search native, ES|QL, ML features.
- **OpenSearch 2.x** — Apache 2.0; vector search via k-NN plugin; ML plugin.

Adoption: Elasticsearch is the **dominant search engine** for app + log analytics. Used by Netflix, Uber, Slack, Shopify, GitHub, Wikimedia, Microsoft, every Fortune 500 for log analytics. OpenSearch is the default for AWS-native shops.

## When To Use It

### Search
- **Full-text search** — better than LIKE / FTS in most DBs.
- **Faceted search** — filters + aggregations on documents.
- **Multi-language search** — built-in analyzers for 30+ languages.
- **Vector + hybrid search** — kNN + BM25 in one query.

### Observability
- **Log aggregation (ELK / OpenSearch)** — the default.
- **APM** — application performance monitoring.
- **Metrics + uptime + synthetics** — Elastic Observability.

### Security
- **SIEM** — security information & event management.
- **Endpoint security** — Elastic Security.

### General analytics
- **Time-series** — log + metric analytics; aggregations are rich.
- **Geospatial** — geo_shape + geo_point queries.

## When NOT To Use It

- **You just need a primary database** — Postgres + extensions is simpler.
- **You don't have search requirements** — overkill.
- **Cost-sensitive** — Elasticsearch can get expensive at scale; OpenSearch is cheaper on AWS.
- **Strong ACID transactions** — Elasticsearch is not transactional.
- **Tiny dataset** — sqlite / Postgres is simpler.
- **You want fully open source** — OpenSearch is the Apache 2.0 choice.

## Why It Matters in 2026

Three forces:

1. **Vector search is native.** Elastic's kNN + HNSW + hybrid retrieval make it a serious AI/RAG backend. Combine with BM25 for hybrid search.
2. **ELK is still the default for log analytics.** OpenSearch on AWS + Elasticsearch elsewhere — the ELK pattern is everywhere.
3. **OpenSearch is the open-source fork.** After Elastic's 2021 license change, AWS forked OpenSearch; both continue to evolve. Apache 2.0 vs SSPL is a real choice.

Practitioner playbook in 2026:
1. **Search**: Elasticsearch or OpenSearch; both index JSON documents; expose REST + query DSL.
2. **Log analytics**: ELK (Elastic) or OpenSearch (AWS-native).
3. **Vector search**: Elasticsearch with kNN; OpenSearch with k-NN plugin.
4. **Hybrid (BM25 + vectors)**: built-in; both engines.
5. **Schema**: explicit mappings; don't rely on dynamic mapping alone.
6. **Sharding + replicas**: pre-plan capacity.

## Scoring Matrix (0–100)

### Elasticsearch
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 95 | 15+ years old; battle-tested at every scale. |
| Community | 95 | Massive; the default for log analytics. |
| Learning curve | 60 | Query DSL takes study; cluster management non-trivial. |
| Performance | 95 | Distributed search is fast; aggregations excellent. |
| Cost | 60 | Can be expensive at scale; managed cheaper than self-host. |
| DX | 85 | Kibana excellent; query DSL powerful; cluster ops heavy. |
| Production readiness | 95 | Battle-tested. |

### OpenSearch
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 85 | 5+ years (fork of ES 7.10). |
| Community | 80 | AWS-driven; smaller than ES but growing. |
| Learning curve | 60 | Same as ES (compatible). |
| Performance | 90 | Similar to ES. |
| Cost | 80 | Free OSS; managed via AWS OpenSearch Service. |
| DX | 80 | Compatible APIs; OpenSearch Dashboards. |
| Production readiness | 90 | AWS-native; production at scale. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Postgres FTS (tsvector)** | You already have Postgres; small scale. | You need distributed search; complex analyzers. |
| **Algolia / Typesense** | Hosted search-as-a-service. | You need self-host / cost-sensitive. |
| **Meilisearch** | OSS; lightweight; Rust-fast. | You need full Lucene feature set. |
| **Typesense** | Hosted; typo-tolerant. | You need Lucene-grade features. |
| **OpenSearch** | AWS; fully open source. | You need Elastic commercial features. |
| **Vector DB (Pinecone, Weaviate)** | Pure vector search; AI-native. | You need BM25 + structured filters too. |

## Sources

- [Elasticsearch](https://www.elastic.co/elasticsearch) — 2026
- [Elastic Docs](https://www.elastic.co/docs/) — 2026
- [Elasticsearch GitHub (elastic/elasticsearch)](https://github.com/elastic/elasticsearch) — 2026
- [Query DSL](https://www.elastic.co/docs/explore-analyze/query-filter/languages/querydsl) — 2026
- [Elastic Observability](https://www.elastic.co/observability) — 2026
- [Elastic Security](https://www.elastic.co/security) — 2026
- [OpenSearch](https://opensearch.org/) — 2026
- [OpenSearch GitHub (opensearch-project/OpenSearch)](https://github.com/opensearch-project/OpenSearch) — 2026
- [Elastic License v2 Blog](https://www.elastic.co/blog/elastic-license-v2) — 2021
- [Elasticsearch Reference](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html) — 2026
- [Elasticsearch Search API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/search) — 2026
- [elasticsearch-py](https://github.com/elastic/elasticsearch-py) — 2026
- [elasticsearch-js](https://github.com/elastic/elasticsearch-js) — 2026
- [Elastic Downloads](https://www.elastic.co/downloads) — 2026
- [OpenSearch Docs](https://opensearch.org/docs/latest/) — 2026
- [Elastic License FAQ](https://www.elastic.co/blog/elastic-license-faq) — 2026