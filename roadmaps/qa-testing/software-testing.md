---
name: Software Testing
category: qa-testing
status: researched
last-updated: 2026-07-30
sources:
  - https://roadmap.sh/software-testing
  - https://en.wikipedia.org/wiki/Software_testing
  - https://martinfowler.com/testing/
  - https://www.istqb.org/
  - https://en.wikipedia.org/wiki/Test-driven_development
  - https://en.wikipedia.org/wiki/Behavior-driven_development
  - https://github.com/testdouble/contributors
  - https://github.com/goldbergyoni/javascript-testing-best-practices
  - https://martinfowler.com/bliki/TestPyramid.html
  - https://www.thoughtworks.com/insights/blog/practical-test-pyramid
tags: [testing, tdd, bdd, unit-testing, integration-testing, e2e-testing, test-pyramid]
---

# Software Testing

## One-liner

The discipline of verifying software works correctly — unit + integration + end-to-end tests, the testing pyramid, and the methodologies (TDD, BDD) that structure how teams write tests.

## What It Is

[Software testing](https://en.wikipedia.org/wiki/Software_testing) is the practice of verifying that software behaves as expected. It spans unit tests (single function), integration tests (multiple components), end-to-end tests (full user flows), performance, security, accessibility, and more.

The 2026 testing pyramid (per [Martin Fowler](https://martinfowler.com/bliki/TestPyramid.html)):

```
        /\
       /  \      E2E tests (few, slow, expensive)
      /----\
     /      \    Integration tests (moderate count)
    /--------\
   /          \  Unit tests (many, fast, cheap)
  /____________\
```

Key methodologies:

| Methodology | Description |
|-------------|-------------|
| **TDD** (Test-Driven Development) | Red-green-refactor cycle: write failing test, make it pass, refactor. |
| **BDD** (Behavior-Driven Development) | Tests as specifications; Gherkin syntax (Given/When/Then). |
| **Property-based testing** | Generate random inputs; check invariants (fast-check, Hypothesis). |
| **Mutation testing** | Verify tests by mutating code (Stryker, PIT). |
| **Contract testing** | API consumer/provider contracts (Pact). |

Adoption: Testing is universal. Every modern codebase has unit tests; most have integration; many have E2E.

## When To Use It

- **Every project** — period.
- **Critical paths** — extra rigor.
- **Public APIs** — contract tests.
- **UI flows** — E2E tests.

## When NOT To Use It

- **Throwaway code** — skip.
- **100% coverage as a goal** — diminishing returns.
- **Tests of trivial code** — getters / setters.

## Why It Matters in 2026

Three forces: (1) AI-generated code needs tests to verify; (2) AI-assisted testing — LLMs write test cases; (3) Faster CI = more test runs = faster feedback.

Practitioner playbook: (1) Test pyramid: many unit, fewer integration, few E2E; (2) TDD or at least test-after for critical code; (3) Mocking at the right level; (4) Coverage as a smell-test, not a goal; (5) Fast tests in CI; (6) Property-based tests for parsers / serializers.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 50+ years. |
| Community | 100 | Universal. |
| Learning curve | 65 | Concepts easy; mocking + E2E take study. |
| Performance | N/A | Practice. |
| Cost | 90 | Free tools. |
| DX | 85 | Modern tools are good. |
| Production readiness | 100 | Every project. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Manual testing only** | Exploratory / UX. | Regression. |
| **No tests** | Throwaway. | Production. |
| **Formal verification** | Safety-critical. | Most apps. |
| **Property-based testing** | Parsers / invariants. | Simple CRUD. |

## Sources

- [roadmap.sh/software-testing](https://roadmap.sh/software-testing) — 2026
- [Wikipedia — Software Testing](https://en.wikipedia.org/wiki/Software_testing) — 2026
- [Martin Fowler — Testing](https://martinfowler.com/testing/) — 2026
- [ISTQB](https://www.istqb.org/) — 2026
- [Wikipedia — Test-Driven Development](https://en.wikipedia.org/wiki/Test-driven_development) — 2026
- [Wikipedia — Behavior-Driven Development](https://en.wikipedia.org/wiki/Behavior-driven_development) — 2026
- [testdouble contributors](https://github.com/testdouble/contributors) — 2026
- [JavaScript Testing Best Practices (Yoni Goldberg)](https://github.com/goldbergyoni/javascript-testing-best-practices) — 2026
- [Martin Fowler — Test Pyramid](https://martinfowler.com/bliki/TestPyramid.html) — 2026
- [ThoughtWorks — Practical Test Pyramid](https://www.thoughtworks.com/insights/blog/practical-test-pyramid) — 2026