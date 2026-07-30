---
name: Django
category: backend-frameworks
status: researched
last-updated: 2026-07-30
sources:
  - https://www.djangoproject.com/
  - https://docs.djangoproject.com/
  - https://github.com/django/django
  - https://docs.djangoproject.com/en/stable/
  - https://docs.djangoproject.com/en/stable/intro/
  - https://docs.djangoproject.com/en/stable/topics/
  - https://www.djangoproject.com/start/
  - https://docs.djangoproject.com/en/stable/ref/contrib/
  - https://www.django-rest-framework.org/
  - https://github.com/encode/django-rest-framework
  - https://wagtail.org/
  - https://channels.readthedocs.io/
  - https://docs.celeryq.dev/
  - https://github.com/celery/celery
tags: [django, python, web-framework, orm, django-rest-framework, wagtail, channels, celery]
---

# Django

## One-liner

Python's "batteries-included" web framework — full-stack with ORM, admin, auth, and templating out of the box — the default for serious Python web apps in 2026.

## What It Is

[Django](https://www.djangoproject.com/) is a high-level Python web framework that encourages rapid development + clean, pragmatic design. It includes nearly everything you need to build a web app: ORM, admin panel, authentication, URL routing, template engine, forms, admin, internationalization, security (CSRF, XSS protection), and more.

The 2026 baseline is **Django 5.x**:

- **Django 5.1** (2024) — `django.db.models.BetterResult`, async ORM improvements.
- **Django 5.2 LTS** (2025) — long-term support.
- **Async ORM** (Django 4.1+) — async views + async ORM queries.
- **DRF (Django REST Framework)** — the standard for REST APIs.
- **Django Channels** — WebSockets + async protocols.
- **Wagtail** — Django-based CMS (popular).
- **Celery** — task queue (Django-friendly).

Adoption: Django is one of the **top 3 Python web frameworks** (with Flask + FastAPI). Used by Instagram, Pinterest, Disqus, Mozilla, National Geographic, every "Python web app."

## When To Use It

- **Full-stack web app in Python** — Django's sweet spot.
- **CMS / content-heavy site** — Wagtail + Django.
- **Admin panel out of the box** — Django admin is unbeatable.
- **Mature ORM** — Django ORM is best-in-class for Python.
- **Batteries-included** — auth, sessions, i18n, security all built in.
- **You want fast prototyping** — Django admin + scaffold = MVP fast.

## When NOT To Use It

- **Pure API server** — FastAPI is leaner + faster + better async.
- **Real-time / heavy async** — Django Channels exists but is heavyweight.
- **Microservices** — Django is monolithic; consider Flask / FastAPI per service.
- **You hate "magic"** — Django does a lot implicitly; some devs prefer explicit.

## Why It Matters in 2026

Three forces keep Django relevant in 2026: (1) Async ORM matured — `async def` + `aget()` work everywhere, making Django viable for real-time features. (2) The admin panel is still unmatched — every Django app gets a free CRUD UI. (3) The ecosystem (DRF, Wagtail, Celery, Channels) is mature and vast. Practitioner playbook: start with Django for any Python web app with admin; switch to FastAPI only if you're building a pure API with no admin needs.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 95 | 20+ years; LTS releases; battle-tested at scale. |
| Community | 100 | Massive; biggest Python web framework. |
| Learning curve | 75 | Conventions help; ORM takes study. |
| Performance | 75 | Improved with async; not as fast as FastAPI/Go. |
| Cost | 100 | Free OSS. |
| DX | 90 | Admin panel is unbeatable. |
| Production readiness | 100 | Battle-tested at Instagram, Pinterest scale. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **FastAPI** | Pure API server; async-first. | You need admin / CMS. |
| **Flask** | Minimal / micro-framework. | You want batteries-included. |
| **Rails** | You're in Ruby. | You want Python. |
| **Spring Boot** | Enterprise Java. | You want Python. |
| **Laravel** | PHP full-stack. | You want Python. |

## Sources

- [Django](https://www.djangoproject.com/) — 2026
- [Django Docs](https://docs.djangoproject.com/) — 2026
- [Django GitHub (django/django)](https://github.com/django/django) — 2026
- [Django Getting Started](https://docs.djangoproject.com/en/stable/) — 2026
- [Django Intro](https://docs.djangoproject.com/en/stable/intro/) — 2026
- [Django Topics](https://docs.djangoproject.com/en/stable/topics/) — 2026
- [Django Start](https://www.djangoproject.com/start/) — 2026
- [Django Contrib Packages](https://docs.djangoproject.com/en/stable/ref/contrib/) — 2026
- [Django REST Framework](https://www.django-rest-framework.org/) — 2026
- [DRF GitHub (encode/django-rest-framework)](https://github.com/encode/django-rest-framework) — 2026
- [Wagtail CMS](https://wagtail.org/) — 2026
- [Django Channels](https://channels.readthedocs.io/) — 2026
- [Celery](https://docs.celeryq.dev/) — 2026
- [Celery GitHub (celery/celery)](https://github.com/celery/celery) — 2026