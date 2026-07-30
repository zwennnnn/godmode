---
name: Ruby on Rails
category: backend-frameworks
status: researched
last-updated: 2026-07-30
sources:
  - https://rubyonrails.org/
  - https://guides.rubyonrails.org/
  - https://github.com/rails/rails
  - https://guides.rubyonrails.org/getting_started.html
  - https://guides.rubyonrails.org/active_record_basics.html
  - https://guides.rubyonrails.org/action_controller_overview.html
  - https://guides.rubyonrails.org/active_job_basics.html
  - https://guides.rubyonrails.org/action_mailer_basics.html
  - https://guides.rubyonrails.org/routing.html
  - https://guides.rubyonrails.org/asset_pipeline.html
  - https://kamal-deploy.org/
  - https://hotwired.dev/
tags: [rails, ruby-on-rails, ruby, web-framework, active-record, hotwire, kamal, action-mailer]
---

# Ruby on Rails

## One-liner

David Heinemeier Hansson's "convention over configuration" web framework — Rails 8 (2024) reasserts Rails as the most productive full-stack web framework with built-in deployment, SQLite default, and Hotwire.

## What It Is

[Ruby on Rails](https://rubyonrails.org/) is a server-side web application framework written in Ruby that follows the MVC pattern. It emphasizes "convention over configuration" and "don't repeat yourself" — generators + sensible defaults ship a working CRUD app in minutes.

The 2026 baseline is **Rails 8** (released 2024):

- **Rails 8** — major release; built-in deployment via Kamal; SQLite default for dev.
- **Hotwire** (Turbo + Stimulus) — SPA-like UX without writing JS.
- **Import Maps** — default asset pipeline.
- **Solid Queue** — built-in queue adapter (DB-backed).
- **Solid Cache** — built-in cache.
- **Solid Cable** — Action Cable (WebSockets) backed by DB.
- **Authentication generator** — `bin/rails generate authentication`.
- **Propshaft** — new asset pipeline.
- **Kamal** — Docker-based deployment built-in.

Adoption: Rails remains dominant for Rails-native web apps. Used by Shopify, GitHub, GitLab, Basecamp/HEY, Discourse, Mastodon, every Rails startup.

## When To Use It

- **Web app / API** — Rails's sweet spot.
- **Convention over configuration** — Rails's design philosophy.
- **Fast prototyping** — generators + scaffolding = MVP fast.
- **Full-stack with Hotwire** — minimal JS for SPA-like UX.
- **You want batteries-included** — ActiveRecord, ActionMailer, ActiveJob, ActionCable.

## When NOT To Use It

- **You don't use Ruby** — wrong framework.
- **You want maximum performance** — Go / Rust better.
- **Microservices** — Rails is monolithic per app; use multiple Rails apps.

## Why It Matters in 2026

Rails 8 (Dec 2024) reasserted Rails as the most productive full-stack web framework: built-in deployment via Kamal, SQLite default for dev, Hotwire native, Solid Queue/Cache/Cable (DB-backed defaults). YJIT made Ruby fast. Rails remains the default for convention-over-configuration web apps.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 21+ years old; battle-tested. |
| Community | 90 | Massive; Shopify / GitHub ecosystem. |
| Learning curve | 80 | Convention over configuration; great docs. |
| Performance | 75 | YJIT improved a lot; still slower than Go. |
| Cost | 100 | Free OSS. |
| DX | 95 | Generators + scaffolding = best productivity. |
| Production readiness | 100 | Battle-tested. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Laravel** | You're in PHP. | You want Ruby. |
| **Django** | Python full-stack. | You want Ruby. |
| **Phoenix** | You want Elixir / soft real-time. | Hiring pool. |
| **Next.js** | TypeScript-first. | You want Ruby. |

## Sources

- [Ruby on Rails](https://rubyonrails.org/) — 2026
- [Rails Guides](https://guides.rubyonrails.org/) — 2026
- [Rails GitHub (rails/rails)](https://github.com/rails/rails) — 2026
- [Getting Started with Rails](https://guides.rubyonrails.org/getting_started.html) — 2026
- [Active Record Basics](https://guides.rubyonrails.org/active_record_basics.html) — 2026
- [Action Controller Overview](https://guides.rubyonrails.org/action_controller_overview.html) — 2026
- [Active Job Basics](https://guides.rubyonrails.org/active_job_basics.html) — 2026
- [Action Mailer Basics](https://guides.rubyonrails.org/action_mailer_basics.html) — 2026
- [Rails Routing](https://guides.rubyonrails.org/routing.html) — 2026
- [Asset Pipeline](https://guides.rubyonrails.org/asset_pipeline.html) — 2026
- [Kamal (Deploy)](https://kamal-deploy.org/) — 2026
- [Hotwire](https://hotwired.dev/) — 2026