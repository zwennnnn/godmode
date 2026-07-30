---
name: Programming Languages
slug: programming-languages
source: https://roadmap.sh/python + https://roadmap.sh/golang + https://roadmap.sh/rust + https://roadmap.sh/java + https://roadmap.sh/ruby + https://roadmap.sh/php
last-updated: 2026-07-30
tech-count: 6
status: in-progress
---

# Programming Languages

> **Category:** The major general-purpose programming languages for backend, systems, scripting, and web development in 2026.
> **Sources:** [roadmap.sh/python](https://roadmap.sh/python), [roadmap.sh/golang](https://roadmap.sh/golang), [roadmap.sh/rust](https://roadmap.sh/rust), [roadmap.sh/java](https://roadmap.sh/java), [roadmap.sh/ruby](https://roadmap.sh/ruby), [roadmap.sh/php](https://roadmap.sh/php)

This roadmap covers the dominant general-purpose languages beyond JS/TS (covered in `frontend-backend/`). Each entry focuses on the language core + the dominant framework / runtime, so you can pick the right language for the right job.

---

## Technologies (build order)

| # | Technology | File | Status |
|---|-----------|------|--------|
| 1 | Python | [python.md](python.md) | placeholder |
| 2 | Go | [go.md](go.md) | placeholder |
| 3 | Rust | [rust.md](rust.md) | placeholder |
| 4 | Java | [java.md](java.md) | placeholder |
| 5 | Ruby | [ruby.md](ruby.md) | placeholder |
| 6 | PHP | [php.md](php.md) | placeholder |

---

## Quick Decision Guide

### If you're doing AI/ML / data science

**Python** is the only answer. Pair with FastAPI (web), pandas / NumPy / Polars (data), scikit-learn / PyTorch (ML). Use **uv** as the package manager.

### If you're building cloud-native backends / CLI tools / DevOps tooling

**Go**. Goroutines, single static binary, the language of Kubernetes / Docker / Terraform. Use Gin / stdlib `net/http`.

### If you're building performance-critical systems / WebAssembly / embedded

**Rust**. Memory safety + C++ performance. Use Axum / Actix for web; wasm-bindgen for browser.

### If you're in enterprise / banking / Android

**Java** with Spring Boot. Virtual threads (Java 21+) + GraalVM Native Image made Java modern again.

### If you're shipping a Rails-style web app fast

**Ruby** with Rails 8. Convention over configuration; Sidekiq for jobs; YJIT for performance.

### If you're in shared hosting / WordPress / Laravel shops

**PHP** with Laravel. Universal deployment; the world's most-deployed server language.

### If you're unsure

Start with **TypeScript** (in [`../frontend-backend/`](../frontend-backend/)) or **Python**. They cover the most use cases with the gentlest learning curve.

---

## Cross-references

- For JavaScript / TypeScript, see [`../frontend-backend/typescript.md`](../frontend-backend/typescript.md).
- For mobile-native languages, see [`../mobile/swift-ios.md`](../mobile/swift-ios.md) and [`../mobile/kotlin-android.md`](../mobile/kotlin-android.md).
- For AI/ML frameworks in Python, see [`../ai-ml-llm/README.md`](../ai-ml-llm/README.md).

---

## Build progress

**Phase 6 in progress** as of 2026-07-30. See [`../godmode.md`](../godmode.md) under `## Progress Tracker`.