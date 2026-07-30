---
name: FastAPI
category: backend-frameworks
status: researched
last-updated: 2026-07-30
sources:
  - https://fastapi.tiangolo.com/
  - https://github.com/tiangolo/fastapi
  - https://fastapi.tiangolo.com/tutorial/
  - https://fastapi.tiangolo.com/advanced/
  - https://fastapi.tiangolo.com/deployment/
  - https://pydantic-docs.helpmanual.io/
  - https://docs.pydantic.dev/
  - https://github.com/pydantic/pydantic
  - https://www.starlette.io/
  - https://github.com/encode/starlette
  - https://www.uvicorn.org/
  - https://github.com/encode/uvicorn
  - https://sqlmodel.tiangolo.com/
  - https://github.com/fastapi/sqlmodel
tags: [fastapi, python, async, api, pydantic, openapi, uvicorn, starlette]
---

# FastAPI

## One-liner

The modern, fast (high-performance) Python web framework for building APIs — async-first, type-driven, automatic OpenAPI docs, and the default for new Python APIs in 2026.

## What It Is

[FastAPI](https://fastapi.tiangolo.com/) is a modern, fast (high-performance) Python web framework for building APIs with Python 3.7+ based on standard Python type hints. Key features:

- **Fast** — on par with NodeJS / Go (Starlette + Pydantic).
- **Type-driven** — Python type hints drive validation, serialization, OpenAPI.
- **Async-first** — built on Starlette + asyncio.
- **Automatic OpenAPI + Swagger UI + ReDoc**.
- **Pydantic integration** — validation, settings, serialization.

The 2026 baseline is **FastAPI 0.115+** with:

- **Pydantic v2** — Rust-backed; 5–50× faster validation.
- **Annotated dependencies** — cleaner DI.
- **Async / await** — native.
- **WebSockets**, **StreamingResponse**, **Server-Sent Events**.
- **Background tasks** + integration with Celery / ARQ / Taskiq.
- **OAuth2 + JWT** helpers.
- **OpenTelemetry** integration.

Adoption: FastAPI overtook Flask as the #2 Python web framework (behind Django). Used by Microsoft, Uber, Netflix (parts), every new Python API.

## When To Use It

- **Modern Python API** — async, type-safe, fast.
- **Microservices** — small, fast, deployable.
- **ML model serving** — async inference.
- **You want OpenAPI / Swagger** automatically.
- **You prefer type hints** — TS-like DX in Python.

## When NOT To Use It

- **Full-stack web app with admin / CMS** — Django is better.
- **You need Flask-style simplicity** — FastAPI is more structured.
- **Synchronous, simple apps** — Flask is simpler.

## Why It Matters in 2026

Three forces made FastAPI the default for new Python APIs in 2026: (1) Pydantic v2 is Rust-backed — 5–50× faster validation; (2) Async-first design matches the Node/Go world; (3) Automatic OpenAPI + Swagger UI save weeks. FastAPI is the right default for any new Python API that isn't a full-stack monolith.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 90 | 7+ years; v1 stable since 2023. |
| Community | 95 | Massive; default for new Python APIs. |
| Learning curve | 80 | Pydantic + type hints; familiar for TS devs. |
| Performance | 95 | Async + Pydantic v2 = top of Python benchmarks. |
| Cost | 100 | Free OSS. |
| DX | 95 | Auto-docs; type-safe; best Python DX. |
| Production readiness | 95 | Used at Microsoft, Uber, Netflix (parts). |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Django + DRF** | Full-stack with admin. | Pure API; you want async-first. |
| **Flask** | Minimal; sync. | You want async + types. |
| **Litestar** | You want even faster. | Ecosystem matters. |
| **Node.js (Express/Hono)** | Full-stack JS. | You want Python. |

## Sources

- [FastAPI](https://fastapi.tiangolo.com/) — 2026
- [FastAPI GitHub (tiangolo/fastapi)](https://github.com/tiangolo/fastapi) — 2026
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/) — 2026
- [FastAPI Advanced](https://fastapi.tiangolo.com/advanced/) — 2026
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/) — 2026
- [Pydantic Docs](https://docs.pydantic.dev/) — 2026
- [Pydantic GitHub (pydantic/pydantic)](https://github.com/pydantic/pydantic) — 2026
- [Starlette](https://www.starlette.io/) — 2026
- [Starlette GitHub (encode/starlette)](https://github.com/encode/starlette) — 2026
- [Uvicorn](https://www.uvicorn.org/) — 2026
- [Uvicorn GitHub (encode/uvicorn)](https://github.com/encode/uvicorn) — 2026
- [SQLModel](https://sqlmodel.tiangolo.com/) — 2026
- [SQLModel GitHub (fastapi/sqlmodel)](https://github.com/fastapi/sqlmodel) — 2026