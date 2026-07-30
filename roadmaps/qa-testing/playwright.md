---
name: Playwright
category: qa-testing
status: researched
last-updated: 2026-07-30
sources:
  - https://playwright.dev/
  - https://playwright.dev/docs/intro
  - https://github.com/microsoft/playwright
  - https://playwright.dev/docs/api/class-playwright
  - https://playwright.dev/docs/test-assertions
  - https://playwright.dev/docs/test-fixtures
  - https://playwright.dev/docs/ci
  - https://playwright.dev/docs/trace-viewer
  - https://playwright.dev/docs/codegen
  - https://playwright.dev/docs/accessibility-testing
tags: [playwright, e2e-testing, microsoft, browser-automation, testing, typescript, codegen]
---

# Playwright

## One-liner

Microsoft's modern end-to-end testing framework for web apps — fast, reliable, multi-browser (Chromium / Firefox / WebKit), with auto-waiting + trace viewer + codegen; the #1 E2E choice for new web projects in 2026.

## What It Is

[Playwright](https://playwright.dev/) is an open-source framework for reliable end-to-end testing of modern web apps. Maintained by Microsoft, it supports Chromium (Chrome, Edge), Firefox, and WebKit (Safari). Includes a test runner (`@playwright/test`), auto-waiting assertions, trace viewer, codegen, and component testing.

The 2026 baseline:

- **Playwright 1.50+** — current stable.
- **`@playwright/test`** — built-in test runner (Jest-compatible).
- **Auto-waiting** — waits for elements to be ready before clicking.
- **Trace viewer** — DOM + network + console replay of failures.
- **Codegen** — `npx playwright codegen` records your actions as test code.
- **Component testing** — test Vue / React / Svelte components in isolation.
- **Accessibility testing** — `@axe-core/playwright` integration.
- **Parallel execution** — by default.
- **Multi-browser** — Chromium, Firefox, WebKit.
- **CI/CD ready** — GitHub Actions + sharding.

Adoption: Playwright overtook Cypress as the #1 E2E testing tool in 2024–2025. Used by Microsoft, Google (parts), every modern web project.

## When To Use It

- **Modern web app E2E testing** — Playwright.
- **Cross-browser testing** — Chromium + Firefox + WebKit.
- **Component testing** — Vue / React / Svelte.
- **Visual regression** — via screenshot comparison.
- **API + UI testing in one** — Playwright API requests.

## When NOT To Use It

- **You want simpler setup** — Vitest for unit only.
- **You're locked into Selenium** — migration cost.
- **Pure backend / non-browser** — use Vitest / Jest.

## Why It Matters in 2026

Three forces: (1) Multi-browser is the default; (2) Trace viewer + codegen improved DX; (3) AI-assisted test generation — Playwright MCP + Claude Code can write tests from prompts.

Practitioner playbook: (1) Install + write first test; (2) Use locators (`getByRole`, `getByText`); (3) Codegen for new flows; (4) Trace viewer for debugging; (5) Parallel + sharded on CI; (6) Component tests for reusable UI.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 95 | 5+ years; battle-tested. |
| Community | 95 | Massive; #1 E2E. |
| Learning curve | 85 | Easy to start; advanced takes study. |
| Performance | 95 | Fast; parallel + sharding. |
| Cost | 100 | Free OSS. |
| DX | 95 | Codegen + trace viewer + auto-wait = best-in-class. |
| Production readiness | 95 | Battle-tested. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Cypress** | You want simpler dashboard. | You want multi-browser + speed. |
| **Selenium** | Legacy; mobile (Appium). | New project. |
| **WebdriverIO** | Mobile + cross-platform. | Web-only. |
| **Puppeteer** | Just Chromium. | Cross-browser. |
| **Vitest + Testing Library** | Component tests. | E2E flows. |

## Sources

- [Playwright](https://playwright.dev/) — 2026
- [Playwright Intro](https://playwright.dev/docs/intro) — 2026
- [Playwright GitHub (microsoft/playwright)](https://github.com/microsoft/playwright) — 2026
- [Playwright API](https://playwright.dev/docs/api/class-playwright) — 2026
- [Playwright Assertions](https://playwright.dev/docs/test-assertions) — 2026
- [Playwright Fixtures](https://playwright.dev/docs/test-fixtures) — 2026
- [Playwright CI](https://playwright.dev/docs/ci) — 2026
- [Playwright Trace Viewer](https://playwright.dev/docs/trace-viewer) — 2026
- [Playwright Codegen](https://playwright.dev/docs/codegen) — 2026
- [Playwright Accessibility Testing](https://playwright.dev/docs/accessibility-testing) — 2026