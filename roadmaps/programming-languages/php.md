---
name: PHP
category: programming-languages
status: researched
last-updated: 2026-07-30
sources:
  - https://www.php.net/
  - https://docs.php.az/
  - https://github.com/php/php-src
  - https://packagist.org/
  - https://getcomposer.org/
  - https://laravel.com/
  - https://laravel.com/docs
  - https://github.com/laravel/framework
  - https://symfony.com/
  - https://symfony.com/doc/current/index.html
  - https://github.com/symfony/symfony
  - https://wordpress.org/
  - https://developer.wordpress.org/
  - https://github.com/WordPress/WordPress
  - https://slimframework.com/
  - https://www.php-fig.org/psr/
  - https://github.com/php-fig/fig-standards
tags: [php, laravel, symfony, wordpress, composer, psr, web, scripting, shared-hosting]
---

# PHP

## One-liner

The web's most-deployed server-side language (77%+ of all websites with a known server-side language) — modern PHP 8.4 is a far cry from its early reputation, and Laravel + Symfony make it a productive choice for web apps in 2026.

## What It Is

PHP (PHP: Hypertext Preprocessor) is a server-side scripting language originally designed for web development (Rasmus Lerdorf, 1995). It's evolved from a templating language into a modern, JIT-compiled, strongly-typed language with a mature framework ecosystem.

The 2026 baseline is **PHP 8.4+** with:

- **JIT compiler** (PHP 8.0+) — significant performance boost for CPU-bound code.
- **Strict types** with `declare(strict_types=1)`.
- **Named arguments**, **readonly properties**, **enums** (8.1+), **fibers** (8.1+).
- **Property hooks** (8.4).
- **Asymmetric visibility** (8.4).
- **Modern OOP** — interfaces, traits, generics (8.4 docs), attributes.
- **Composer** + **Packagist** — the standard package manager.
- **PSR standards** (PHP-FIG) — interoperability across frameworks.

Dominant frameworks / libraries:

| Domain | Tool |
|--------|------|
| **Full-stack web** | [Laravel](https://laravel.com/) (the dominant framework), [Symfony](https://symfony.com/) (enterprise-grade, components used everywhere) |
| **CMS** | [WordPress](https://wordpress.org/) (43% of all websites), Drupal, Joomla |
| **Micro-framework** | [Slim](https://slimframework.com/), Lumen (Laravel micro) |
| **E-commerce** | Magento, WooCommerce, Shopware, PrestaShop |
| **ORM** | Eloquent (Laravel), Doctrine (Symfony) |
| **Templating** | Blade (Laravel), Twig (Symfony) |
| **Testing** | PHPUnit, Pest (Laravel) |

Adoption: PHP powers **~77% of all websites with a known server-side language** (W3Techs, 2025). WordPress alone is ~43% of all websites. Laravel is the most-starred PHP framework on GitHub. PHP is the default for shared hosting, the de-facto language for content sites, and a major player in e-commerce.

## When To Use It

- **Web apps with Laravel or Symfony** — modern, productive, batteries-included.
- **WordPress / WooCommerce** — the CMS default; massive ecosystem.
- **Shared hosting environments** — PHP is everywhere.
- **E-commerce** — Magento, Shopware, WooCommerce all PHP.
- **Legacy maintenance** — huge amount of existing PHP codebases.
- **You want cheap deployment** — PHP is universally supported by every shared host.
- **You want a quick full-stack MVP** — Laravel ships auth, ORM, queues, mail, broadcasting out of the box.

## When NOT To Use It

- **AI/ML / data science** — Python dominates.
- **Mobile native** — Swift / Kotlin.
- **High-throughput / low-latency backends** — Go / Rust / Java.
- **Frontend in browser** — JS / TS.
- **You want a "modern" stack for new development** — Node/TS or Go has more momentum in 2026.
- **Strong static typing by default** — TypeScript / Java / Rust.
- **You want compile-time guarantees** — PHP is interpreted (with JIT).

## Why It Matters in 2026

Three forces:

1. **PHP 8.x killed the old criticisms.** JIT, readonly properties, enums, fibers, named arguments — modern PHP is unrecognizable from PHP 5. The "PHP is bad" memes are stale.
2. **Laravel remains hugely productive.** One artisan command scaffolds a CRUD; Eloquent ORM is one of the most-loved ORMs; Laravel Forge + Vapor handle deploys; Livewire + Inertia make modern SPA-style UIs without an API layer.
3. **WordPress + WooCommerce still dominate the web.** ~43% of all websites run WordPress; the entire plugin ecosystem is PHP. PHP is the language of content management.

Practitioner defaults in 2026:
- **Framework**: **Laravel 11+** (default for new apps) or Symfony for enterprise.
- **Package manager**: Composer.
- **Coding standard**: PSR-12.
- **Testing**: PHPUnit or Pest (modern Laravel).
- **Static analysis**: PHPStan / Psalm.
- **Frontend**: Livewire + Alpine.js (default Laravel); or Inertia.js + React/Vue for SPA; or API-only with a separate frontend.
- **Deployment**: Laravel Forge / Vapor / Ploi; or Docker + standard CI/CD.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 30+ years old (1995); the most-deployed server-side language. |
| Community | 90 | Massive; Laravel / Symfony / WordPress ecosystems are enormous. |
| Learning curve | 80 | Easy to start (especially with Laravel); modern PHP features take study. |
| Performance | 70 | JIT closed much of the gap; still slower than Go / Java for CPU work. |
| Cost | 100 | Free; runs on the cheapest shared hosting. |
| DX | 85 | Laravel is best-in-class for productivity; Composer is excellent. |
| Production readiness | 95 | Powers ~77% of websites with known backend language. Battle-tested at scale. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Node.js / TypeScript** | Full-stack JS; web-first. | You want Laravel productivity. |
| **Python + Django** | AI/ML; data science. | You want a more web-focused framework. |
| **Ruby + Rails** | Convention over configuration; developer happiness. | Hiring pool is smaller; performance similar. |
| **Java + Spring Boot** | Enterprise; static typing; performance. | You want productivity. |
| **Go** | Performance; simple deployment. | You want a full-stack framework. |
| **C# / ASP.NET** | Microsoft shop. | Cross-platform community. |

## Sources

- [PHP Official Site](https://www.php.net/) — 2026
- [PHP Manual](https://docs.php.az/) — 2026
- [PHP GitHub (php/php-src)](https://github.com/php/php-src) — 2026
- [Packagist](https://packagist.org/) — 2026
- [Composer](https://getcomposer.org/) — 2026
- [Laravel](https://laravel.com/) — 2026
- [Laravel Docs](https://laravel.com/docs) — 2026
- [Laravel GitHub (laravel/framework)](https://github.com/laravel/framework) — 2026
- [Symfony](https://symfony.com/) — 2026
- [Symfony Docs](https://symfony.com/doc/current/index.html) — 2026
- [Symfony GitHub (symfony/symfony)](https://github.com/symfony/symfony) — 2026
- [WordPress](https://wordpress.org/) — 2026
- [WordPress Developer Resources](https://developer.wordpress.org/) — 2026
- [WordPress GitHub (WordPress/WordPress)](https://github.com/WordPress/WordPress) — 2026
- [Slim Framework](https://slimframework.com/) — 2026
- [PHP-FIG PSR Standards](https://www.php-fig.org/psr/) — 2026
- [PHP-FIG GitHub (php-fig/fig-standards)](https://github.com/php-fig/fig-standards) — 2026