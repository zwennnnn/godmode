---
name: Python
category: programming-languages
status: researched
last-updated: 2026-07-30
sources:
  - https://www.python.org/
  - https://docs.python.org/3/
  - https://peps.python.org/
  - https://github.com/python/cpython
  - https://pypi.org/
  - https://www.jetbrains.com/lp/devecosystem-2024/
  - https://survey.stackoverflow.co/2024/technology/
  - https://djangoproject.com/
  - https://docs.djangoproject.com/
  - https://fastapi.tiangolo.com/
  - https://github.com/tiangolo/fastapi
  - https://flask.palletsprojects.com/
  - https://github.com/pallets/flask
  - https://docs.python.org/3/howto/uvloop.html
  - https://pydantic-docs.helpmanual.io/
  - https://pandas.pydata.org/
  - https://numpy.org/
  - https://pytorch.org/
  - https://scikit-learn.org/
tags: [python, django, fastapi, flask, pandas, numpy, pytorch, ml, scripting, backend]
---

# Python

## One-liner

The world's most popular general-purpose language for AI/ML, data science, scripting, and web backends — readable, batteries-included, with the deepest library ecosystem of any language.

## What It Is

Python is a dynamically-typed, garbage-collected, multi-paradigm language (object-oriented, functional, procedural) designed for readability. Created by Guido van Rossum in 1991, it's now the default language for AI/ML, data science, scientific computing, scripting, automation, and a major backend language.

The 2026 baseline is **Python 3.13+** (and 3.14 in beta) with:

- **Faster CPython** — the Faster CPython project (py 3.11+) shipped 10–60% speedups; 3.13 added a JIT compiler (experimental).
- **uv** — the Astral-built package manager that replaced pip + venv + pyenv for most workflows (~100× faster than pip).
- **Type hints mature** — `dict`, `list`, `Optional`, `TypedDict`, `Protocol`, generics all standard; mypy + ruff for enforcement.
- **Pydantic v2** — Rust-backed; the standard for runtime validation + settings.
- **Free-threading** (PEP 703) — experimental in 3.13, true multi-threaded Python (no GIL) coming.
- **Match statements**, structural pattern matching, exception groups (3.11+).
- **Async / asyncio** mature for IO-bound workloads.

Dominant frameworks / libraries:

| Domain | Tool |
|--------|------|
| **Web backend** | [Django](https://www.djangoproject.com/) (full-featured), [FastAPI](https://fastapi.tiangolo.com/) (modern async), [Flask](https://flask.palletsprojects.com/) (minimal) |
| **Data science** | [pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/), [Polars](https://pola.rs/), [DuckDB-Python](https://duckdb.org/) |
| **ML / DL** | [scikit-learn](https://scikit-learn.org/), [PyTorch](https://pytorch.org/), TensorFlow, JAX, XGBoost |
| **LLM apps** | LangChain, LlamaIndex, DSPy, PydanticAI |
| **Validation** | [Pydantic](https://docs.pydantic.dev/) v2, attrs, marshmallow |
| **Testing** | pytest, hypothesis |
| **Packaging** | uv, hatch, poetry, pdm |
| **Type checking** | mypy, pyright, ruff |

Adoption: Python is the **#1 most-used language on GitHub** (since 2019), the #1 language for AI/ML by a wide margin, the default for data science, and a top-3 backend language. Per [Stack Overflow 2024](https://survey.stackoverflow.co/2024/technology/) and [JetBrains DevEcosystem 2024](https://www.jetbrains.com/lp/devecosystem-2024/): ~50%+ of developers use Python regularly.

## When To Use It

- **AI / ML / data science** — the default; everything is here first.
- **Scripting / automation / glue code** — `python my_script.py` is the lingua franca.
- **Web backend** — Django for full-featured, FastAPI for modern async, Flask for minimal.
- **Scientific computing** — NumPy / SciPy / pandas are best-in-class.
- **DevOps / SRE tooling** — Ansible, Boto3, every cloud SDK, every CI system.
- **Data pipelines / ETL** — Airflow, Prefect, dbt-Python, Dagster.
- **Education / quick prototyping** — readability wins.
- **You need the largest library ecosystem of any language.**

## When NOT To Use It

- **CPU-bound performance-critical code** — Rust / C++ / Go are 10–100× faster. Use Python for orchestration, native for hot paths.
- **Mobile native apps** — Swift / Kotlin.
- **Frontend in the browser** — JS / TS.
- **Embedded / microcontroller** — C / Rust / MicroPython for tiny scripts only.
- **Real-time / low-latency systems** — the GIL hurts; use Go / Rust.
- **Large monolith teams with strict type discipline** — TypeScript or Java may serve you better.

## Why It Matters in 2026

Three forces:

1. **The AI/ML era made Python mandatory.** Every serious ML / LLM work happens in Python. Not because Python is the best language — but because the libraries (PyTorch, JAX, scikit-learn, transformers, LangChain) all live there.
2. **Tooling caught up.** uv (Rust-backed package manager), ruff (Rust-backed linter), Pydantic v2 (Rust-backed validation), Free-threaded Python (PEP 703) — Python's classic complaints (slow, packaging chaos, GIL) are being systematically fixed.
3. **Type hints + Pydantic matured.** Modern Python looks much more like TypeScript than Python 2. The "untyped scripting language" reputation is outdated.

Practitioner defaults in 2026:
- **Package manager**: **uv** (default for new projects).
- **Type checking**: mypy strict or pyright.
- **Linting / formatting**: ruff (replaces flake8 + isort + black).
- **Web**: Django (full), FastAPI (modern async), Flask (minimal).
- **Validation**: Pydantic v2.
- **Testing**: pytest + hypothesis.
- **ML**: PyTorch + HuggingFace Transformers.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 35+ years old (1991); the lingua franca of AI/ML. |
| Community | 100 | #1 on GitHub; PyPI has >600K packages; massive tutorial ecosystem. |
| Learning curve | 85 | Easiest general-purpose language to start; mastery (async, metaclasses, descriptors) takes study. |
| Performance | 65 | Faster CPython improved a lot; still ~10× slower than C/Rust for CPU work. |
| Cost | 100 | Free; runs anywhere. |
| DX | 85 | uv + ruff + Pydantic = great DX; Jupyter notebooks are best-in-class for data. |
| Production readiness | 95 | Used at Google, Instagram, Spotify, Netflix, Dropbox, Reddit, every ML lab. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **JavaScript / TypeScript** | You need web + backend in one language. | You need the ML/data ecosystem. |
| **Go** | You need raw performance + simple deployment (single binary). | You need the ML ecosystem. |
| **Rust** | You need maximum performance + safety. | You want to ship fast. |
| **Java** | Enterprise; Android; JVM ecosystem. | You want to move fast. |
| **Ruby** | You love Rails / convention over configuration. | You want bigger ecosystem / ML. |
| **C++** | Systems programming; game engines. | You want productivity. |
| **R** | Pure statistics / academic data analysis. | You want general-purpose. |
| **Julia** | Numerical / scientific computing with near-C speed. | Ecosystem is smaller. |

## Sources

- [Python Official Site](https://www.python.org/) — 2026
- [Python 3 Docs](https://docs.python.org/3/) — 2026
- [Python Enhancement Proposals (PEPs)](https://peps.python.org/) — 2026
- [CPython GitHub (python/cpython)](https://github.com/python/cpython) — 2026
- [PyPI](https://pypi.org/) — 2026
- [JetBrains Developer Ecosystem 2024](https://www.jetbrains.com/lp/devecosystem-2024/) — 2024
- [Stack Overflow Developer Survey 2024](https://survey.stackoverflow.co/2024/technology/) — 2024
- [Django](https://www.djangoproject.com/) — 2026
- [Django Docs](https://docs.djangoproject.com/) — 2026
- [FastAPI](https://fastapi.tiangolo.com/) — 2026
- [FastAPI GitHub (tiangolo/fastapi)](https://github.com/tiangolo/fastapi) — 2026
- [Flask](https://flask.palletsprojects.com/) — 2026
- [Flask GitHub (pallets/flask)](https://github.com/pallets/flask) — 2026
- [uvloop (asyncio event loop)](https://docs.python.org/3/howto/uvloop.html) — 2026
- [Pydantic Docs](https://docs.pydantic.dev/) — 2026
- [pandas](https://pandas.pydata.org/) — 2026
- [NumPy](https://numpy.org/) — 2026
- [PyTorch](https://pytorch.org/) — 2026
- [scikit-learn](https://scikit-learn.org/) — 2026