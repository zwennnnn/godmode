#!/usr/bin/env python3
"""Add the missing Why It Matters / Scoring Matrix / Comparison With Alternatives sections to framework files."""
import re
from pathlib import Path

# Per-file content for the missing sections
CONTENT = {
    "django.md": {
        "why": "Three forces keep Django relevant in 2026: (1) Async ORM matured — `async def` + `aget()` work everywhere, making Django viable for real-time features. (2) The admin panel is still unmatched — every Django app gets a free CRUD UI. (3) The ecosystem (DRF, Wagtail, Celery, Channels) is mature and vast. Practitioner playbook: start with Django for any Python web app with admin; switch to FastAPI only if you're building a pure API with no admin needs.",
        "matrix": "| Maturity | 95 | 20+ years; LTS releases; battle-tested at scale. |\n| Community | 100 | Massive; biggest Python web framework. |\n| Learning curve | 75 | Conventions help; ORM takes study. |\n| Performance | 75 | Improved with async; not as fast as FastAPI/Go. |\n| Cost | 100 | Free OSS. |\n| DX | 90 | Admin panel is unbeatable. |\n| Production readiness | 100 | Battle-tested at Instagram, Pinterest scale. |",
        "alternatives": "| Alternative | Better when | Worse when |\n|-------------|-------------|------------|\n| **FastAPI** | Pure API server; async-first. | You need admin / CMS. |\n| **Flask** | Minimal / micro-framework. | You want batteries-included. |\n| **Rails** | You're in Ruby. | You want Python. |\n| **Spring Boot** | Enterprise Java. | You want Python. |\n| **Laravel** | PHP full-stack. | You want Python. |"
    },
    "fastapi.md": {
        "why": "Three forces made FastAPI the default for new Python APIs in 2026: (1) Pydantic v2 is Rust-backed — 5–50× faster validation; (2) Async-first design matches the Node/Go world; (3) Automatic OpenAPI + Swagger UI save weeks. FastAPI is the right default for any new Python API that isn't a full-stack monolith.",
        "matrix": "| Maturity | 90 | 7+ years; v1 stable since 2023. |\n| Community | 95 | Massive; default for new Python APIs. |\n| Learning curve | 80 | Pydantic + type hints; familiar for TS devs. |\n| Performance | 95 | Async + Pydantic v2 = top of Python benchmarks. |\n| Cost | 100 | Free OSS. |\n| DX | 95 | Auto-docs; type-safe; best Python DX. |\n| Production readiness | 95 | Used at Microsoft, Uber, Netflix (parts). |",
        "alternatives": "| Alternative | Better when | Worse when |\n|-------------|-------------|------------|\n| **Django + DRF** | Full-stack with admin. | Pure API; you want async-first. |\n| **Flask** | Minimal; sync. | You want async + types. |\n| **Litestar** | You want even faster. | Ecosystem matters. |\n| **Node.js (Express/Hono)** | Full-stack JS. | You want Python. |"
    },
    "express.md": {
        "why": "Express 5 (released 2024) brought async error handling and Promise support, modernizing the original Node.js framework. Express remains the default for new Node.js APIs and the basis for many other frameworks (NestJS, Fastify started from Express concepts). The middleware ecosystem is unmatched.",
        "matrix": "| Maturity | 100 | 14+ years; the original. |\n| Community | 100 | Massive; middleware ecosystem. |\n| Learning curve | 85 | Easy; unopinionated. |\n| Performance | 80 | Good; Fastify / Hono are faster. |\n| Cost | 100 | Free OSS. |\n| DX | 85 | Simple; many middleware. |\n| Production readiness | 100 | Battle-tested everywhere. |",
        "alternatives": "| Alternative | Better when | Worse when |\n|-------------|-------------|------------|\n| **Fastify** | Maximum Node.js perf. | Middleware ecosystem matters. |\n| **Hono** | Edge runtimes; modern. | Stable ecosystem matters. |\n| **NestJS** | Opinion + structure. | You want minimal. |\n| **Koa** | Modern async middleware. | Ecosystem matters. |"
    },
    "nestjs.md": {
        "why": "Three forces made NestJS the default for serious Node.js backends: (1) TypeScript-first + decorators = enterprise-friendly DX; (2) Angular-inspired structure scales to large teams; (3) Built-in microservices, GraphQL, WebSockets, queues. NestJS is the right default for TypeScript backends at scale.",
        "matrix": "| Maturity | 85 | 8+ years; stable. |\n| Community | 90 | Fast-growing; loved by TS devs. |\n| Learning curve | 70 | Decorators + DI; familiar for Angular/Spring devs. |\n| Performance | 80 | Fastify-based; good. |\n| Cost | 100 | Free OSS. |\n| DX | 90 | Excellent TS DX. |\n| Production readiness | 95 | Used at Adidas, Roche, Autodesk. |",
        "alternatives": "| Alternative | Better when | Worse when |\n|-------------|-------------|------------|\n| **Express** | Minimal; flexibility. | You want structure + DI. |\n| **Fastify** | Maximum Node.js perf. | You want opinion + DI. |\n| **tRPC** | TS-only monorepo. | Public API / multi-client. |\n| **Spring Boot** | Java enterprise. | You want Node.js. |"
    },
    "spring-boot.md": {
        "why": "Spring Boot 3 + Java 21 virtual threads + GraalVM native = Java's biggest modernization in years. Spring Boot is the dominant enterprise Java backend; .NET Aspire (2024+) is the new kid. For any serious Java backend in 2026, Spring Boot is the default.",
        "matrix": "| Maturity | 100 | Spring since 2003; Boot since 2014. |\n| Community | 100 | Massive; enterprise standard. |\n| Learning curve | 60 | Steep; magic + DI + Spring idioms. |\n| Performance | 90 | Virtual threads + GraalVM native. |\n| Cost | 90 | OSS free; commercial support available. |\n| DX | 85 | Spring Initializr is great; mature tools. |\n| Production readiness | 100 | Battle-tested at every enterprise. |",
        "alternatives": "| Alternative | Better when | Worse when |\n|-------------|-------------|------------|\n| **Quarkus** | Cloud-native + native compile. | You're not on K8s. |\n| **Micronaut** | Compile-time DI. | Ecosystem matters. |\n| **Helidon** | Oracle shop. | You want ecosystem. |\n| **ASP.NET Core** | Microsoft shop. | You want JVM. |"
    },
    "laravel.md": {
        "why": "Laravel 11/12 streamlined the framework; Laravel 12 added workerman / roadrunner integration for true concurrency. Laravel remains the most productive PHP framework; Vapor enables serverless on AWS Lambda. Default for PHP web apps in 2026.",
        "matrix": "| Maturity | 95 | 14+ years old; battle-tested. |\n| Community | 100 | Massive; #1 PHP framework. |\n| Learning curve | 80 | Elegant syntax; docs are excellent. |\n| Performance | 80 | Octane + PHP 8.3 + JIT is fast. |\n| Cost | 100 | Free OSS; Vapor paid for serverless. |\n| DX | 95 | Eloquent + Blade + Tinker = best PHP DX. |\n| Production readiness | 95 | Used everywhere. |",
        "alternatives": "| Alternative | Better when | Worse when |\n|-------------|-------------|------------|\n| **Symfony** | Enterprise; components. | You want Laravel productivity. |\n| **WordPress** | Content / blog. | Web app. |\n| **CodeIgniter** | Small footprint. | Laravel ecosystem. |\n| **CakePHP** | Legacy. | New project. |"
    },
    "ruby-on-rails.md": {
        "why": "Rails 8 (Dec 2024) reasserted Rails as the most productive full-stack web framework: built-in deployment via Kamal, SQLite default for dev, Hotwire native, Solid Queue/Cache/Cable (DB-backed defaults). YJIT made Ruby fast. Rails remains the default for convention-over-configuration web apps.",
        "matrix": "| Maturity | 100 | 21+ years old; battle-tested. |\n| Community | 90 | Massive; Shopify / GitHub ecosystem. |\n| Learning curve | 80 | Convention over configuration; great docs. |\n| Performance | 75 | YJIT improved a lot; still slower than Go. |\n| Cost | 100 | Free OSS. |\n| DX | 95 | Generators + scaffolding = best productivity. |\n| Production readiness | 100 | Battle-tested. |",
        "alternatives": "| Alternative | Better when | Worse when |\n|-------------|-------------|------------|\n| **Laravel** | You're in PHP. | You want Ruby. |\n| **Django** | Python full-stack. | You want Ruby. |\n| **Phoenix** | You want Elixir / soft real-time. | Hiring pool. |\n| **Next.js** | TypeScript-first. | You want Ruby. |"
    },
    "aspnet-core.md": {
        "why": ".NET 9/10 + ASP.NET Core = the most modern, performant, batteries-included backend framework. TechEmpower benchmarks consistently rank ASP.NET Core at the top. Blazor lets you write C# end-to-end (server + WebAssembly). .NET Aspire (2024) is the new cloud-native orchestration stack. ASP.NET Core is the right default for C# / Microsoft shops.",
        "matrix": "| Maturity | 95 | ASP.NET since 2002; Core since 2016. |\n| Community | 95 | Massive; Microsoft + .NET Foundation. |\n| Learning curve | 70 | Steep; C# + .NET idioms + DI + middleware. |\n| Performance | 100 | Top of TechEmpower benchmarks. |\n| Cost | 95 | Free OSS; Visual Studio paid for Pro features. |\n| DX | 90 | VS Code / Rider / Visual Studio are excellent. |\n| Production readiness | 100 | Battle-tested at Microsoft, Stack Overflow, Dell. |",
        "alternatives": "| Alternative | Better when | Worse when |\n|-------------|-------------|------------|\n| **Spring Boot** | JVM ecosystem. | You want .NET. |\n| **Node.js + NestJS** | JS ecosystem. | You want C# / .NET. |\n| **Go** | Maximum simplicity. | You want batteries-included. |"
    },
    "vue.md": {
        "why": "Vue 3 + Composition API + Pinia + Nuxt 3 + Vite + Vitest is a complete end-to-end stack. Vue is the #2 frontend framework by npm downloads and is loved for its gentle learning curve. For teams that want React DX without React JSX, Vue is the default.",
        "matrix": "| Maturity | 95 | 11+ years; Vue 3 stable since 2020. |\n| Community | 100 | Massive; #2 frontend framework. |\n| Learning curve | 90 | Templates + Composition API; gentle. |\n| Performance | 85 | Proxy-based reactivity; fast. |\n| Cost | 100 | Free OSS. |\n| DX | 95 | Vite + Pinia + Vue DevTools = best-in-class. |\n| Production readiness | 95 | Battle-tested at scale. |",
        "alternatives": "| Alternative | Better when | Worse when |\n|-------------|-------------|------------|\n| **React** | You want JSX + biggest ecosystem. | You want HTML templates. |\n| **Svelte** | You want compile-time minimal. | You want bigger ecosystem. |\n| **Angular** | Enterprise; you want opinion + DI. | You want flexibility. |"
    },
    "angular.md": {
        "why": "Angular 19/20 with Signals + standalone components + zoneless change detection made Angular modern again. Angular remains the enterprise default for large SPAs at banks, insurance, government. Strong typing by default + DI + opinionated structure = maintainable at scale.",
        "matrix": "| Maturity | 100 | Since 2016 (Angular 2+); 10 years. |\n| Community | 95 | Massive; enterprise standard. |\n| Learning curve | 60 | Steep; RxJS + decorators + DI. |\n| Performance | 85 | Signals + zoneless = big speedup. |\n| Cost | 100 | Free OSS. |\n| DX | 80 | Opinionated; CLI is great. |\n| Production readiness | 100 | Battle-tested at every enterprise. |",
        "alternatives": "| Alternative | Better when | Worse when |\n|-------------|-------------|------------|\n| **React** | You want JSX + flexibility. | You want opinion + structure. |\n| **Vue** | You want gentle curve. | You want enterprise opinion. |\n| **Svelte** | You want minimal bundle. | You want full ecosystem. |"
    },
    "svelte.md": {
        "why": "Svelte 5 Runes ($state, $derived, $effect) made reactivity explicit. SvelteKit 2 + Vite + form actions + adapters is a complete full-stack stack. Svelte is the #1 most loved frontend framework in Stack Overflow surveys for 3+ years. For small-to-medium apps, Svelte is the most elegant choice.",
        "matrix": "| Maturity | 85 | 10+ years; Svelte 5 stable since 2024. |\n| Community | 90 | Fast-growing; most-loved framework. |\n| Learning curve | 95 | Easiest of the big three. |\n| Performance | 95 | Compile-time = no runtime overhead. |\n| Cost | 100 | Free OSS. |\n| DX | 95 | Elegant; minimal boilerplate. |\n| Production readiness | 90 | Used at NYT, Apple, Spotify (parts). |",
        "alternatives": "| Alternative | Better when | Worse when |\n|-------------|-------------|------------|\n| **React** | You want biggest ecosystem. | You want minimal bundle. |\n| **Vue** | You want HTML templates. | You want compile-time. |\n| **Solid** | You want React-like JSX + signals. | You want template syntax. |"
    },
    "astro.md": {
        "why": "Astro 5 Server Islands (Dec 2024) brought selective server rendering inside otherwise-static pages. Astro's content layer + zero-JS-by-default + multi-framework integration = the default for content-driven sites in 2026. Used by Microsoft, Google, Cloudflare for docs + marketing.",
        "matrix": "| Maturity | 85 | Since 2021; v5 stable since 2024. |\n| Community | 90 | Fast-growing; default for content sites. |\n| Learning curve | 90 | Islands are intuitive; templates easy. |\n| Performance | 100 | Zero JS by default; islands hydrate selectively. |\n| Cost | 100 | Free OSS. |\n| DX | 95 | Best for content + marketing. |\n| Production readiness | 95 | Used by Microsoft, Google docs. |",
        "alternatives": "| Alternative | Better when | Worse when |\n|-------------|-------------|------------|\n| **Next.js** | Heavy SPA / dashboard. | You want zero-JS marketing. |\n| **SvelteKit** | You want Svelte end-to-end. | You want framework-agnostic islands. |\n| **Qwik** | You want resumability. | You want simpler islands model. |\n| **Hugo / Jekyll** | Pure static. | You need some interactivity. |"
    },
    "solidjs.md": {
        "why": "SolidJS gives you React's JSX DX with fine-grained reactivity (no virtual DOM). Solid 1.9/2.x + SolidStart is a complete stack. Solid is at the top of performance benchmarks among React-like frameworks in 2026.",
        "matrix": "| Maturity | 80 | Since 2018; stable since 1.0 (2023). |\n| Community | 75 | Smaller but passionate. |\n| Learning curve | 80 | React-like + signals mental model. |\n| Performance | 100 | Top of React-like benchmarks. |\n| Cost | 100 | Free OSS. |\n| DX | 90 | Fine-grained + JSX + great types. |\n| Production readiness | 85 | Used by Chrome DevTools team, GitHub (parts). |",
        "alternatives": "| Alternative | Better when | Worse when |\n|-------------|-------------|------------|\n| **React** | You want biggest ecosystem. | You want fine-grained perf. |\n| **Svelte** | You want compile-time + templates. | You want JSX. |\n| **Vue** | You want HTML templates + ecosystem. | You want signals + JSX. |"
    },
    "qwik.md": {
        "why": "Qwik 1.x (released 2023) stabilized resumability. The architecture is genuinely novel — instead of hydration, the server serializes state into HTML; the client resumes without re-executing. The fastest TTI framework in 2026 Core Web Vitals benchmarks. Best for slow mobile devices / emerging markets.",
        "matrix": "| Maturity | 80 | 1.x stable since 2023. |\n| Community | 75 | Smaller but growing. |\n| Learning curve | 70 | New mental model ($ markers, QRLs). |\n| Performance | 100 | Fastest TTI; near-zero JS by default. |\n| Cost | 100 | Free OSS. |\n| DX | 80 | Different from React/Vue; learning curve. |\n| Production readiness | 80 | Used by Builder.io, select perf-critical sites. |",
        "alternatives": "| Alternative | Better when | Worse when |\n|-------------|-------------|------------|\n| **Astro** | Content + islands. | You want resumability everywhere. |\n| **SvelteKit** | Familiar Svelte stack. | You want zero JS always. |\n| **Next.js** | You want React ecosystem. | You want min JS shipped. |"
    }
}

def fix_file(file_path: Path):
    content = file_path.read_text(encoding="utf-8")
    name = file_path.name

    if name not in CONTENT:
        return False, f"No content for {name}"

    data = CONTENT[name]

    # Add missing sections before Sources
    # Find the Sources section and insert before it
    sources_match = re.search(r"^## Sources\s*$", content, re.MULTILINE)
    if not sources_match:
        return False, f"No Sources section in {name}"

    insert_pos = sources_match.start()
    new_sections = f"""## Why It Matters in 2026

{data["why"]}

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
{data["matrix"]}

## Comparison With Alternatives

{data["alternatives"]}

"""

    new_content = content[:insert_pos] + new_sections + content[insert_pos:]
    file_path.write_text(new_content, encoding="utf-8")
    return True, f"Updated {name}"


# Process all framework files
files_to_fix = [
    # backend-frameworks
    "roadmaps/backend-frameworks/django.md",
    "roadmaps/backend-frameworks/fastapi.md",
    "roadmaps/backend-frameworks/express.md",
    "roadmaps/backend-frameworks/nestjs.md",
    "roadmaps/backend-frameworks/spring-boot.md",
    "roadmaps/backend-frameworks/laravel.md",
    "roadmaps/backend-frameworks/ruby-on-rails.md",
    "roadmaps/backend-frameworks/aspnet-core.md",
    # frontend-frameworks
    "roadmaps/frontend-frameworks/vue.md",
    "roadmaps/frontend-frameworks/angular.md",
    "roadmaps/frontend-frameworks/svelte.md",
    "roadmaps/frontend-frameworks/astro.md",
    "roadmaps/frontend-frameworks/solidjs.md",
    "roadmaps/frontend-frameworks/qwik.md",
]

base = Path("c:/Users/yagiz/OneDrive/Desktop/godmode")
results = []
for f in files_to_fix:
    full = base / f
    if not full.exists():
        results.append((False, f"MISSING: {f}"))
        continue
    ok, msg = fix_file(full)
    results.append((ok, msg))

for ok, msg in results:
    print(("OK  " if ok else "FAIL") + " " + msg)