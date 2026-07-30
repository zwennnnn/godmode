---
name: Vector Databases
category: ai-ml-llm
status: researched
last-updated: 2026-07-30
sources:
  - https://ann-benchmarks.com/
  - https://link.springer.com/article/10.1007/s10791-024-09449-w
  - https://www.pinecone.io/
  - https://weaviate.io/
  - https://qdrant.tech/
  - https://milvus.io/
  - https://github.com/pgvector/pgvector
  - https://docs.trychroma.com/
  - https://lancedb.github.io/lancedb/
  - https://www.elephantsql.com/blog/pgvector
  - https://huggingface.co/docs/text-embeddings-inference
  - https://github.com/erikbern/ann-benchmarks
  - https://www.cockroachlabs.com/blog/vector-search-performance/
tags: [vector-db, ann, hnsw, embeddings, rag, semantic-search]
---

# Vector Databases

## One-liner

Specialized stores that index high-dimensional embedding vectors for fast approximate-nearest-neighbor (ANN) search — the retrieval layer under nearly every modern RAG system.

## What It Is

A vector database stores records as vectors (typically 384–4096 dimensions, output of an embedding model) and answers similarity queries — *"give me the top-K vectors most similar to this query vector"* — in milliseconds, even when the collection contains hundreds of millions of vectors. They use **ANN** (Approximate Nearest Neighbor) algorithms to trade a tiny amount of recall for huge speedups over exact search.

The dominant algorithm family is **HNSW** (Hierarchical Navigable Small World), a graph-based index that gives the best recall-vs-latency tradeoff for in-memory workloads. Other approaches include **IVF-PQ** (inverted file + product quantization — used by Faiss, good for memory-constrained settings), **ScaNN** (Google's ANN library), and **DiskANN** (Microsoft's disk-resident index for billion-scale). [ANN-Benchmarks](https://ann-benchmarks.com/) is the canonical public benchmark for these algorithms; the [Springer journal paper](https://link.springer.com/article/10.1007/s10791-024-09449-w) (2024) describes the methodology.

The 2026 production landscape splits into **purpose-built vector DBs** ([Pinecone](https://www.pinecone.io/), [Weaviate](https://weaviate.io/), [Qdrant](https://qdrant.tech/), [Milvus](https://milvus.io/)), **embedded / in-process** ([Chroma](https://docs.trychroma.com/), [LanceDB](https://lancedb.github.io/lancedb/)), and **extensions to existing DBs** ([pgvector](https://github.com/pgvector/pgvector) for Postgres, MongoDB Atlas Vector Search, Elasticsearch dense_vector, ClickHouse, CockroachDB).

Key features that distinguish them in 2026:

| Feature | Why it matters |
|---------|----------------|
| **Hybrid search** (vector + BM25/keyword) | Beats pure-vector on real enterprise corpora where exact terms (SKUs, names, codes) matter. |
| **Metadata filtering** with vectors | "Top-K similar to query, filtered by tenant = X and date > Y". |
| **Hybrid indexes** (HNSW + DiskANN) | Keep hot data in memory, cold data on disk; billion-scale without RAM blowup. |
| **GPU acceleration** | NVIDIA cuVS / RAFT speedups for batch ingest + query. Milvus leads here. |
| **Quantization** | 1-bit / 2-bit (RaBitQ, LVQ) compression cuts memory 8–32×. |
| **Managed vs self-host** | Pinecone = managed-only; Weaviate/Qdrant/Milvus = both. |

## When To Use It

- **You're building RAG** — every modern RAG pipeline needs vector search as its core retrieval primitive.
- **You're doing semantic search** over text, images, audio, video, code, or any embedding-able content.
- **You're building recommendation systems** that need "more like this" retrieval.
- **You're deduplicating / clustering** at scale (e.g. fraud detection, support-ticket grouping).
- **You're a team with vector search as a primary workload** — purpose-built DBs beat shoehorning it into Postgres at >10M vectors.

## When NOT To Use It

- **You have <100k vectors and they're already in Postgres.** Use [pgvector](https://github.com/pgvector/pgvector) — one extension, no new infra, transactional consistency.
- **You need exact nearest neighbors.** ANN is approximate by definition; use exact kNN for small datasets or where 100% recall matters.
- **Your "vectors" are <50 dimensions.** Plain SQL with a similarity UDF may be faster and cheaper.
- **You need to query by relational joins** as the primary access pattern. Use a relational DB; vectors are secondary.
- **You have no embedding model.** Vectors without an embedding model are just numbers — pick the model first.
- **You're building OLTP with vector as a side feature.** Adding vector to Postgres/MongoDB is fine; pulling in Pinecone for occasional queries is over-engineering.

## Why It Matters in 2026

Three forces are reshaping the space:

1. **Billion-scale is the new million-scale.** DiskANN + hybrid in-memory/disk indexes make billion-vector deployments routine on commodity hardware. [Pinecone Serverless](https://www.pinecone.io/) (launched 2024) and Weaviate's serverless tier both target the long-tail of "lots of vectors but not Netflix-scale" customers.
2. **Hybrid is the new default.** Pure vector search loses on real-world corpora where keyword exactness matters (legal, medical, code, product catalogs). Weaviate, Qdrant, and Milvus all shipped first-class hybrid (BM25 + dense) in 2024–2025. Practitioner reports (including [Cockroach Labs vector benchmarks](https://www.cockroachlabs.com/blog/vector-search-performance/)) show hybrid outperforms pure-vector by 10–25% on retrieval accuracy.
3. **Embedded databases are eating the bottom of the market.** Chroma and LanceDB (both 2023+) made vector search feel like SQLite — no server, no infra, perfect for prototyping and small/medium deployments. LanceDB's columnar storage (built on the Lance format) gives surprisingly good performance even at 100M+ vectors on a single machine.

Production picks in 2026 by use case (consensus from practitioner surveys + benchmarks):
- **Fastest time-to-prod**: Pinecone (managed).
- **Hybrid search**: Weaviate.
- **Filtered search on metadata**: Qdrant (Rust, fastest filtered queries).
- **Billion-scale enterprise**: Milvus (distributed-native).
- **Already on Postgres**: pgvector (extension).
- **Prototyping / small corpus**: Chroma or LanceDB.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 90 | ANN research from the 2010s; production vector DBs since 2019 (Pinecone); HNSW the de-facto algorithm since ~2018. |
| Community | 95 | Every LLM stack assumes vector search; frameworks (LangChain, LlamaIndex) have first-class integrations for all 6+ major vector DBs. |
| Learning curve | 70 | Conceptually simple ("embed, store, search"); tuning HNSW params (ef_construction, M), quantization tradeoffs, and hybrid fusion weights takes practice. |
| Performance | 90 | Sub-10ms p99 on million-scale with HNSW in memory; billion-scale with DiskANN at 50–100ms. GPU acceleration gives another 10–100× for batch. |
| Cost | 70 | Self-hosted Qdrant/Milvus: cheap on commodity hardware. Pinecone managed: gets expensive fast at scale. pgvector: nearly free (existing Postgres). |
| DX (developer experience) | 85 | Pinecone = easiest API; Weaviate/Qdrant = clean SDKs; pgvector = SQL; Chroma = Pythonic. |
| Production readiness | 90 | Every serious LLM product uses a vector DB in production. Major options are battle-tested. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **pgvector (Postgres extension)** | You already have Postgres; your vector set is <10M; you want transactional consistency. | Billion-scale; you don't want to tune Postgres shared_buffers / maintenance for HNSW. |
| **Full-text search (Elasticsearch, Meilisearch, Typesense)** | Your queries are keyword-heavy and don't benefit much from semantic similarity. | You need true semantic matching on natural language queries. |
| **In-memory similarity (Faiss, hnswlib)** | You're a library author or you want zero-server; you can manage persistence yourself. | You need multi-process access, filtering, or persistence. |
| **Embedding model + brute-force cosine** | You have <100k vectors and need exact results. | You have >1M vectors — brute force is too slow. |
| **Knowledge graph / structured retrieval** | Your queries are about relationships, not similarity. | Your data is prose and queries are natural-language. |

## Sources

- [ANN-Benchmarks — Official Site](https://ann-benchmarks.com/) — 2026
- [Springer — ANN-Benchmarks: A benchmarking tool for ANN algorithms](https://link.springer.com/article/10.1007/s10791-024-09449-w) — 2024
- [Pinecone](https://www.pinecone.io/) — 2026
- [Weaviate](https://weaviate.io/) — 2026
- [Qdrant](https://qdrant.tech/) — 2026
- [Milvus](https://milvus.io/) — 2026
- [pgvector — GitHub](https://github.com/pgvector/pgvector) — 2026
- [Chroma Docs](https://docs.trychroma.com/) — 2026
- [LanceDB](https://lancedb.github.io/lancedb/) — 2026
- [ElephantSQL — pgvector guide](https://www.elephantsql.com/blog/pgvector) — 2025
- [HuggingFace — Text Embeddings Inference](https://huggingface.co/docs/text-embeddings-inference) — 2026
- [ANN-Benchmarks GitHub (erikbern/ann-benchmarks)](https://github.com/erikbern/ann-benchmarks) — 2026
- [CockroachDB — Vector Search Performance](https://www.cockroachlabs.com/blog/vector-search-performance/) — 2025