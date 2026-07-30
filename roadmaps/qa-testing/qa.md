---
name: QA (Quality Assurance)
category: qa-testing
status: researched
last-updated: 2026-07-30
sources:
  - https://roadmap.sh/qa
  - https://www.istqb.org/
  - https://en.wikipedia.org/wiki/Quality_assurance
  - https://www.atlassian.com/continuous-delivery/software-testing
  - https://martinfowler.com/testing/
  - https://www.gov.uk/service-manual/technology/quality-assurance-testing-your-service
  - https://www.ministryoftesting.com/
  - https://dojo.ministryoftesting.com/
  - https://www.scrum.org/resources/blog/what-does-qa-team-do-agile
tags: [qa, quality-assurance, manual-testing, bug-tracking, agile, testing-process]
---

# QA (Quality Assurance)

## One-liner

The discipline + processes that ensure shipped software meets quality standards — test planning, manual + automated testing coordination, bug tracking, and the team culture that catches defects before users do.

## What It Is

QA is the broader discipline of ensuring software quality. It includes test strategy, test planning, manual testing, coordination with engineering, bug triage, release readiness, and the processes that make shipping safe. In 2026, QA often blends with engineering (QA engineers write automation; SDET role).

The 2026 stack:

| Activity | Tools / Practices |
|----------|-------------------|
| **Test planning** | TestRail, Zephyr, qTest, Xray; or GitHub Projects + Test Plans. |
| **Manual testing** | Exploratory testing sessions; session-based test management (SBTM). |
| **Bug tracking** | Jira, Linear, GitHub Issues, Sentry, Shortcut. |
| **Test case management** | TestRail, Zephyr Scale, qTest. |
| **QA in CI/CD** | Automated test gates; quality dashboards. |
| **Release readiness** | Go/no-go meetings; QA sign-off; feature flags for staged rollouts. |
| **Risk-based testing** | Prioritize tests by impact + likelihood. |
| **Shift-left** | QA involved early; requirements review. |
| **Accessibility testing** | Manual + automated (see [`../design-ux/accessibility.md`](../design-ux/accessibility.md)). |
| **Beta programs** | TestFlight, Google Play Beta, in-house beta cohorts. |

Adoption: Every product team has QA — explicit or implicit. Some teams have dedicated QA engineers; others distribute the role across devs.

## When To Use It

- **You're shipping a product** — QA is mandatory.
- **You want a quality culture** — QA processes help.
- **You have a complex app** — manual + automated QA.

## When NOT To Use It

- **Tiny project** — devs do it.
- **Pure internal tool** — skip formal QA.

## Why It Matters in 2026

Three forces: (1) AI-assisted testing — LLMs write test cases + exploratory tests; (2) Shift-left QA — QA earlier in dev cycle; (3) Quality engineering > manual testing — modern QA engineers code.

Practitioner playbook: (1) Define test strategy (unit + integration + E2E + manual); (2) QA involved in requirements + design; (3) Bug triage process; (4) Test plans per release; (5) Production monitoring + crash reporting as QA signal.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 50+ years; well-established. |
| Community | 90 | Ministry of Testing; ISTQB. |
| Learning curve | 65 | Process + tools take study. |
| Performance | N/A | Practice. |
| Cost | 85 | Free + paid tools. |
| DX | 80 | Modern tools are good. |
| Production readiness | 100 | Every product. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **No QA (devs only)** | Tiny project. | Production product. |
| **Outsourced QA** | Short-term / specific scope. | Long-term / quality culture. |
| **Crowdsourced testing** | Bug bounty / exploratory. | Regression / smoke. |
| **AI-generated QA** | Test case generation. | Final acceptance. |

## Sources

- [roadmap.sh/qa](https://roadmap.sh/qa) — 2026
- [ISTQB](https://www.istqb.org/) — 2026
- [Wikipedia — Quality Assurance](https://en.wikipedia.org/wiki/Quality_assurance) — 2026
- [Atlassian — Continuous Delivery Testing](https://www.atlassian.com/continuous-delivery/software-testing) — 2026
- [Martin Fowler — Testing](https://martinfowler.com/testing/) — 2026
- [GOV.UK Service Manual — Quality Assurance](https://www.gov.uk/service-manual/technology/quality-assurance-testing-your-service) — 2026
- [Ministry of Testing](https://www.ministryoftesting.com/) — 2026
- [Ministry of Testing Dojo](https://dojo.ministryoftesting.com/) — 2026
- [Scrum.org — QA in Agile](https://www.scrum.org/resources/blog/what-does-qa-team-do-agile) — 2026