---
name: Accessibility (a11y / WCAG)
category: design-ux
status: researched
last-updated: 2026-07-30
sources:
  - https://www.w3.org/WAI/standards-guidelines/wcag/
  - https://www.w3.org/WAI/ARIA/
  - https://www.w3.org/WAI/
  - https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
  - https://www.w3.org/TR/WCAG22/
  - https://webaim.org/
  - https://webaim.org/articles/evaluationguide/
  - https://www.a11yproject.com/
  - https://www.a11yproject.com/checklist/
  - https://www.deque.com/axe/devtools/
  - https://github.com/dequelabs/axe-core
  - https://github.com/pa11y/pa11y
  - https://www.section508.gov/
  - https://www.ada.gov/
  - https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32019L0882
  - https://github.com/w3c/aria
  - https://www.boia.org/
tags: [accessibility, a11y, wcag, aria, screen-reader, ada, eaa, compliance]
---

# Accessibility (a11y / WCAG)

## One-liner

Designing and building products that work for everyone — including users with visual, auditory, motor, cognitive, and neurological disabilities — and complying with WCAG, ADA, and EAA in 2026.

## What It Is

Accessibility (a11y) is the practice of ensuring products are usable by people with the widest possible range of abilities. It's:

- **Ethical** — ~15–20% of the world's population has a disability; inaccessible products exclude them.
- **Legal** — ADA (US), EAA (EU, enforced from 2025), AODA (Ontario), Equality Act (UK), and more.
- **UX win** — accessible design is usually better design (clear focus order, semantic structure, good contrast).
- **SEO win** — semantic HTML + accessibility = better search ranking.

### The 2026 standards

| Standard | Description |
|----------|-------------|
| **[WCAG 2.2](https://www.w3.org/TR/WCAG22/)** | W3C's Web Content Accessibility Guidelines; current version 2.2 (Oct 2023). AA = the legal baseline. |
| **[WCAG 2.1](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-21/)** | Still widely cited; AA. |
| **WCAG 3.0** | In draft; new structure; not legal yet. |
| **[WAI-ARIA](https://www.w3.org/WAI/ARIA/)** | Accessible Rich Internet Applications — semantic attributes for JS widgets. |
| **[Section 508](https://www.section508.gov/)** | US federal procurement. |
| **[ADA](https://www.ada.gov/)** | US civil rights law; web accessibility enforced via litigation. |
| **[European Accessibility Act (EAA)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32019L0882)** | EU law; enforced from June 2025 for products/services. |
| **[EN 301 549](https://www.etsi.org/deliver/etsi_en/301500_301599/301549/)** | EU harmonized standard; maps to WCAG. |

### WCAG 2.2 levels (and what's required)

- **A** — minimum; non-negotiable.
- **AA** — the legal baseline; required by ADA, EAA, most laws.
- **AAA** — enhanced; not always achievable but strive for key pages.

The four POUR principles:
- **Perceivable** — info must be presentable to users in ways they perceive.
- **Operable** — UI components + navigation must be operable.
- **Understandable** — info + UI operation must be understandable.
- **Robust** — content must work with current + future tools.

### Key WCAG 2.2 success criteria (highlights)

| Criterion | Level | What |
|-----------|-------|------|
| 1.1.1 Non-text Content | A | Alt text for images. |
| 1.3.1 Info and Relationships | A | Semantic HTML. |
| 1.4.3 Contrast (Minimum) | AA | 4.5:1 for normal text; 3:1 for large. |
| 1.4.11 Non-text Contrast | AA | 3:1 for UI components. |
| 2.1.1 Keyboard | A | All functionality via keyboard. |
| 2.4.7 Focus Visible | AA | Visible focus indicator. |
| 2.5.8 Target Size (Minimum) | AA (2.2) | 24×24 CSS px touch targets. |
| 3.3.2 Labels or Instructions | A | Form fields labeled. |
| 4.1.2 Name, Role, Value | A | ARIA for custom widgets. |

### Testing tools (2026)

| Tool | Purpose |
|------|---------|
| **[axe DevTools](https://www.deque.com/axe/devtools/)** ([axe-core](https://github.com/dequelabs/axe-core)) | Browser extension + CI integration; the standard. |
| **[Pa11y](https://github.com/pa11y/pa11y)** | CLI + CI integration. |
| **Lighthouse** | Built into Chrome DevTools; quick a11y audit. |
| **NVDA / JAWS / VoiceOver** | Screen reader testing. |
| **WebAIM Contrast Checker** | Color contrast. |
| **Stark (Figma plugin)** | Contrast + a11y in Figma. |
| **The A11y Project Checklist** | Manual checklist. |

Adoption: Accessibility is now a **legal requirement** in major jurisdictions (US ADA litigation, EU EAA). Every serious product team has an a11y owner or specialist. The "skip accessibility" era is over.

## When To Use It

- **You're building any user-facing product** — required by law + ethics.
- **You're a public-sector org** — Section 508 / EN 301 549 mandatory.
- **You ship in EU** — EAA mandatory since June 2025.
- **You want SEO wins** — semantic HTML helps.
- **You want to reduce support costs** — accessible design = fewer confused users.

## When NOT To Use It

- **You're building internal admin tools for yourself** — still good practice but lower stakes.
- **You're prototyping** — but add it before shipping.

## Why It Matters in 2026

Three forces:

1. **EAA enforcement.** Since June 2025, EU companies must comply. Fines + lawsuits are real.
2. **AI-assisted a11y.** Tools like Stark, Figma AI, axe AI help fix issues at design + code time.
3. **Design systems bake it in.** shadcn/ui, Radix, Material 3 — accessibility by default.

Practitioner playbook in 2026:
1. **Design with a11y in mind** — color contrast (WCAG AA), touch targets (24×24 min), semantic structure.
2. **Code semantically** — use proper HTML elements, ARIA only when needed.
3. **Test in CI** — axe-core + Pa11y in CI gates.
4. **Manual testing** — keyboard navigation; screen reader (NVDA + VoiceOver); zoom to 200%.
5. **Document** — accessibility statement (EAA requires it).

## Scoring Matrix (0–100)

### WCAG 2.2
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 25+ years of WCAG; v2.2 stable. |
| Community | 100 | Massive; W3C + WebAIM + a11y project. |
| Learning curve | 70 | Principles easy; edge cases take study. |
| Performance | N/A | Practice + tooling. |
| Cost | 95 | Free standards; free tools (axe, Pa11y). |
| DX | 80 | Getting better (axe DevTools, Stark, etc.). |
| Production readiness | 100 | Every production site needs it. |

### axe DevTools
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 90 | 8+ years; standard. |
| Community | 90 | Large; widely integrated. |
| Learning curve | 85 | Easy to install + interpret. |
| Performance | 90 | Fast; runs in CI. |
| Cost | 85 | Free; paid extensions for advanced. |
| DX | 90 | Excellent. |
| Production readiness | 95 | Used at scale. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **WCAG 2.2 AA** | Default legal baseline. | You want AAA. |
| **axe DevTools** | Automated testing in CI. | Manual exploratory testing. |
| **Pa11y** | CI integration. | Real user testing. |
| **Lighthouse** | Quick audits. | Deep audits. |
| **Manual (NVDA / VoiceOver)** | Real screen-reader testing. | Automated check. |
| **None** | Never (legal + ethical). | — |

## Sources

- [W3C WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/) — 2026
- [W3C ARIA](https://www.w3.org/WAI/ARIA/) — 2026
- [W3C WAI](https://www.w3.org/WAI/) — 2026
- [What's New in WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/) — 2026
- [WCAG 2.2 Spec](https://www.w3.org/TR/WCAG22/) — 2023
- [WebAIM](https://webaim.org/) — 2026
- [WebAIM Evaluation Guide](https://webaim.org/articles/evaluationguide/) — 2026
- [The A11y Project](https://www.a11yproject.com/) — 2026
- [A11y Project Checklist](https://www.a11yproject.com/checklist/) — 2026
- [Deque axe DevTools](https://www.deque.com/axe/devtools/) — 2026
- [axe-core GitHub (dequelabs/axe-core)](https://github.com/dequelabs/axe-core) — 2026
- [Pa11y GitHub (pa11y/pa11y)](https://github.com/pa11y/pa11y) — 2026
- [Section 508](https://www.section508.gov/) — 2026
- [ADA (US Dept of Justice)](https://www.ada.gov/) — 2026
- [European Accessibility Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32019L0882) — 2019, enforced 2025
- [ARIA GitHub (w3c/aria)](https://github.com/w3c/aria) — 2026
- [BOIA — Bureau of Internet Accessibility](https://www.boia.org/) — 2026