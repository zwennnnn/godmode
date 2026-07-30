---
name: AI Red Teaming
category: cyber-security
status: researched
last-updated: 2026-07-30
sources:
  - https://www.nist.gov/itl/ai-risk-management-framework
  - https://owasp.org/www-project-top-10-for-large-language-model-applications/
  - https://genai.owasp.org/
  - https://arxiv.org/abs/2212.08073
  - https://www.anthropic.com/news/core-views-on-ai-safety
  - https://www.anthropic.com/safety
  - https://deepmind.google/safety/
  - https://www.lakera.ai/
  - https://www.lakera.ai/blog
  - https://github.com/lakera-ai/gandalf
  - https://www.promptingguard.ai/
  - https://www.guardrailsai.com/
  - https://github.com/guardrails-ai/guardrails
  - https://www.rebuff.ai/
  - https://github.com/lakera-ai/rebuff
  - https://www.nist.gov/itl/ai-risk-management-framework
tags: [ai-red-teaming, ai-security, prompt-injection, jailbreak, llm-security, ai-safety, owasp-llm-top-10]
---

# AI Red Teaming

## One-liner

The discipline of attacking AI / LLM systems — prompt injection, jailbreaks, data exfiltration, excessive agency — the new frontier of security in 2026.

## What It Is

AI red teaming is the practice of adversarially testing AI / LLM systems to find failure modes before attackers (or users) do. It combines:

- **Traditional red teaming** — find vulnerabilities.
- **AI-specific threats** — prompt injection, jailbreaks, model theft, data leakage.
- **Safety testing** — biases, hallucinations, harmful outputs.
- **Capability testing** — does the model do what it claims?

### The 2026 AI threat landscape

| Threat | Description |
|--------|-------------|
| **Prompt injection (direct)** | User types malicious prompt to override system. |
| **Prompt injection (indirect)** | Poisoned content in retrieved docs / web pages / tool outputs. |
| **Jailbreaks** | Bypassing safety alignment (DAN, role-play exploits). |
| **Data exfiltration** | Extracting training data or other users' data via prompts. |
| **Excessive agency** | Agent takes harmful actions (LLM06 OWASP). |
| **Model theft** | Stealing model weights via API abuse. |
| **Membership inference** | Determining if data was in training set. |
| **Adversarial inputs** | Inputs that fool image / audio models. |
| **Bias + harmful outputs** | Discrimination, hate, illegal advice. |
| **Hallucinations** | Confident wrong answers in critical domains. |

### Frameworks

| Framework | Source | Notes |
|-----------|--------|-------|
| **[OWASP Top 10 for LLM Applications](https://genai.owasp.org/)** | OWASP | The canonical AI risk list (2025). |
| **[NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)** | NIST | AI Risk Management Framework. |
| **MITRE ATLAS** | MITRE | Adversarial threat landscape for AI. |
| **EU AI Act** | EU | Regulates AI by risk tier (2024+). |
| **Anthropic Responsible Scaling Policy** | Anthropic | Voluntary commitments. |
| **Google DeepMind Safety** | DeepMind | Frontier safety framework. |
| **OpenAI Preparedness Framework** | OpenAI | Risk tracking. |

### OWASP Top 10 for LLMs (2025)

1. **Prompt Injection**
2. **Sensitive Information Disclosure**
3. **Supply Chain** (model + data poisoning)
4. **Data and Model Poisoning**
5. **Improper Output Handling**
6. **Excessive Agency**
7. **System Prompt Leakage**
8. **Vector and Embedding Weaknesses** (RAG-specific)
9. **Misinformation**
10. **Unbounded Consumption** (DoS via prompt)

### AI red teaming methodology

1. **Threat modeling** — what can go wrong?
2. **Attack library** — known prompts + techniques (e.g. Gandalf attacks, public jailbreaks).
3. **Automated scans** — Garak, PyRIT, Lakera; probe for known vulns.
4. **Manual exploration** — creative attackers find new jailbreaks.
5. **Safety evaluations** — pre-deployment benchmarks (HarmBench, AdvBench).
6. **Continuous** — models + prompts change; re-test.

### Top tools (2026)

| Tool | Purpose |
|------|---------|
| **[Lakera Guard](https://www.lakera.ai/)** + [Gandalf](https://github.com/lakera-ai/gandalf) | Prompt injection detection; red team. |
| **[PyRIT](https://github.com/Azure/PyRIT)** (Microsoft) | Python Risk Identification Toolkit. |
| **[Garak](https://github.com/NVIDIA/garak)** | LLM vulnerability scanner. |
| **[Prompting Guard](https://www.promptingguard.ai/)** | Open-source prompt firewall. |
| **[Guardrails AI](https://www.guardrailsai.com/)** | Output validation + safety. |
| **[Rebuff](https://github.com/lakera-ai/rebuff)** | Prompt injection detection. |
| **[Vellum AI Guardrails](https://www.vellum.ai/)** | Evaluation + guardrails. |
| **[Microsoft AI Red Team](https://github.com/microsoft/AI-Red-Team)** | Methodology. |

Adoption: AI red teaming is the fastest-growing security discipline. Every major LLM vendor has internal red teams. NIST published AI RMF (2023). EU AI Act entered force (2024). Anthropic / Google / OpenAI publish red team findings.

## When To Use It

- **You ship an LLM-powered product** — required.
- **You use RAG** — indirect prompt injection via retrieved docs.
- **You build agents that take actions** — excessive agency is real.
- **You handle PII / PHI / financial data** — data exfiltration is the threat.
- **You're in EU** — EU AI Act requires risk assessment.
- **You want safety evaluations** — benchmarks + human eval.

## When NOT To Use It

- **You don't use LLMs** — N/A.
- **You're prototyping** — defer to production-readiness.
- **You can't act on findings** — useless.

## Why It Matters in 2026

Three forces:

1. **LLMs are in production everywhere.** Customer support, search, agents — every product has an LLM attack surface.
2. **Indirect prompt injection is unsolved.** No silver bullet; defense in depth.
3. **EU AI Act + US Executive Orders** — AI red teaming is a regulatory requirement.

Practitioner playbook in 2026:
1. **Map OWASP LLM Top 10** — to your system.
2. **Automated scans** — Garak + Lakera Guard + PyRIT in CI.
3. **Manual red team quarterly** — creative human attackers find what automated tools miss.
4. **Defense in depth** — input validation + guardrails + output filtering + sandboxing.
5. **Log everything** — every prompt, every tool call, every action.
6. **Human-in-the-loop for high stakes** — confirmation before file delete / payment / external send.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 70 | Young discipline (3+ years); evolving fast. |
| Community | 90 | Massive; OWASP + every AI lab. |
| Learning curve | 50 | Many attack types; creative. |
| Performance | N/A | Practice. |
| Cost | 80 | OSS tools free; managed $$$ . |
| DX | 75 | Tools maturing. |
| Production readiness | 80 | Every AI product. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **No AI security** | Never (for LLM products). | — |
| **Traditional AppSec** | Classical web/API security. | LLM-specific threats. |
| **Vendor safety only** | You trust the provider's safety. | Your app-specific risks. |
| **Bug bounty** | Find vulns. | Ongoing monitoring. |
| **AI safety evals (benchmarks)** | Pre-deployment. | Live threats. |

## Sources

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — 2026
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — 2026
- [OWASP GenAI Security Project](https://genai.owasp.org/) — 2026
- [Constitutional AI (arXiv 2212.08073)](https://arxiv.org/abs/2212.08073) — 2022
- [Anthropic — Core Views on AI Safety](https://www.anthropic.com/news/core-views-on-ai-safety) — 2026
- [Anthropic Safety](https://www.anthropic.com/safety) — 2026
- [DeepMind Safety](https://deepmind.google/safety/) — 2026
- [Lakera](https://www.lakera.ai/) — 2026
- [Lakera Blog](https://www.lakera.ai/blog) — 2026
- [Gandalf GitHub (lakera-ai/gandalf)](https://github.com/lakera-ai/gandalf) — 2026
- [Prompting Guard](https://www.promptingguard.ai/) — 2026
- [Guardrails AI](https://www.guardrailsai.com/) — 2026
- [Guardrails AI GitHub (guardrails-ai/guardrails)](https://github.com/guardrails-ai/guardrails) — 2026
- [Rebuff GitHub (lakera-ai/rebuff)](https://github.com/lakera-ai/rebuff) — 2026
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) — 2026