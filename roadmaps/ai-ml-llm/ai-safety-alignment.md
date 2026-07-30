---
name: AI Safety and Alignment
category: ai-ml-llm
status: researched
last-updated: 2026-07-30
sources:
  - https://owasp.org/www-project-top-10-for-large-language-model-applications/
  - https://www.lasso.security/blog/owasp-top-10-llm-2025
  - https://www.appsecengineer.com/blog/owasp-top-10-for-llm-applications-2025
  - https://www.robustintelligence.com/blog/owasp-top-10-llm-security-2025
  - https://github.com/owasp/llm-top-10
  - https://atlas.mitre.org/
  - https://www.lakera.ai/
  - https://www.lakera.ai/blog/lakera-guard-prompt-injection
  - https://github.com/lakera-ai/rebuff
  - https://github.com/NVIDIA/NeMo-Guardrails
  - https://www.anthropic.com/safety
  - https://www.deepmind.google/safety
  - https://www.constitutionalai.ai/
  - https://alignmentforum.org/posts/state-of-alignment-2026
  - https://arxiv.org/abs/2212.08073
  - https://docs.anthropic.com/en/docs/build-with-claude/guardrails
  - https://learn.microsoft.com/en-us/azure/ai-services/content-safety/
tags: [safety, alignment, guardrails, prompt-injection, owasp, lakera, nemo-guardrails, constitutional-ai, red-teaming]
---

# AI Safety and Alignment

## One-liner

The practices and tools that prevent your LLM system from being jailbroken, leaking data, hallucinating dangerously, or causing real-world harm — covering input/output guardrails, red-teaming, alignment training, and threat modeling.

## What It Is

AI safety in the LLM era has two layers:

**1. Application-layer safety (what most teams mean in practice)**
- **Guardrails** — input filters (block prompt injection, PII, off-topic) and output filters (block secrets, harmful content, format violations).
- **Red-teaming** — adversarial testing to find failure modes before users do.
- **Threat modeling** — mapping risks per [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/).
- **Monitoring** — detecting jailbreak attempts, data exfiltration, abuse in production.

**2. Frontier-model alignment (what labs do)**
- **RLHF / Constitutional AI / DPO / ORPO** — alignment training to make the base model helpful, harmless, and honest.
- **Interpretability** — understanding why models do what they do (Anthropic, DeepMind research).
- **Scalable oversight** — supervising superhuman model behavior with weaker supervisors.
- **Adversarial robustness** — defending against jailbreaks, prompt injection, model stealing.

The 2025 OWASP Top 10 for LLM Applications ([OWASP project](https://owasp.org/www-project-top-10-for-large-language-model-applications/), [Lasso Security analysis](https://www.lasso.security/blog/owasp-top-10-llm-2025), [AppSecEngineer breakdown](https://www.appsecengineer.com/blog/owasp-top-10-for-llm-applications-2025)) — the canonical threat list every production team should map against:

| Risk | Summary |
|------|---------|
| **LLM01: Prompt Injection** | Malicious inputs that hijack model behavior — direct (user types it) or indirect (hidden in retrieved docs / web pages / tool outputs). #1 risk. |
| **LLM02: Sensitive Information Disclosure** | Model leaks PII, secrets, training data, or proprietary info in outputs. |
| **LLM03: Supply Chain** | Compromised models, datasets, or pre-trained weights; poisoned training data. |
| **LLM04: Data and Model Poisoning** | Adversarial training data / fine-tuning that backdoors the model. |
| **LLM05: Improper Output Handling** | Downstream code trusts LLM output without validation → XSS, SQL injection, RCE. |
| **LLM06: Excessive Agency** | Agent takes harmful actions autonomously — file deletion, payments, emails. |
| **LLM07: System Prompt Leakage** | Model reveals its system prompt (revealing IP, bypassing constraints). |
| **LLM08: Vector and Embedding Weaknesses** | RAG-specific: embedding inversion, retrieval poisoning, embedding-space attacks. |
| **LLM09: Misinformation** | Hallucinations presented as fact; outdated knowledge. |
| **LLM10: Unbounded Consumption** | Cost / resource DoS — prompt-injection-induced infinite loops, expensive API calls. |

Major tools and frameworks:

| Tool | What it does |
|------|--------------|
| **[Lakera Guard](https://www.lakera.ai/)** + [Rebuff](https://github.com/lakera-ai/rebuff) (now part of Lakera) | Prompt-injection detection; production guardrail API. |
| **[NVIDIA NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)** | Programmable rails for dialogue management, input/output validation, safety policies. |
| **Microsoft Azure AI Content Safety** | Managed content moderation (hate, violence, sexual, self-harm). |
| **Anthropic / OpenAI built-in safety** | System-level refusals; cannot be fully relied on for app-specific rules. |
| **Constitutional AI** ([paper](https://arxiv.org/abs/2212.08073)) | Alignment method where the model critiques itself against a written constitution. |
| **[MITRE ATLAS](https://atlas.mitre.org/)** | Adversarial threat matrix for ML/AI — counterpart to MITRE ATT&CK. |

## When To Use It

- **You're putting any LLM in front of users.** Even simple chatbots need at minimum: input length limits, output PII scanning, prompt-injection detection.
- **You're building an agent** that touches files, APIs, payments, or external sends. Excessive agency (LLM06) is the #1 cause of production incidents.
- **You have a RAG system** with untrusted content (web pages, user uploads, third-party docs). Indirect prompt injection via retrieved content is the most underrated 2026 risk.
- **You're in a regulated industry** (healthcare, finance, legal, government). Audit + guardrails are not optional.
- **You process PII or secrets.** Output scanning is mandatory.
- **You want to ship confidently.** Red-teaming finds problems before your users do.

## When NOT To Use It

- **You're a solo developer prototyping a personal tool.** Skip the enterprise guardrails; use the built-in model safety.
- **Your "users" are only you.** Trust yourself.
- **You're doing offline batch processing** with no untrusted input. Different threat model.
- **You're using a model purely as a deterministic function** (structured extraction with no agency). Less surface area.
- **You try to make the model itself perfectly safe.** You can't — build defense in depth around it.

## Why It Matters in 2026

Three forces are reshaping AI safety:

1. **Prompt injection is unsolved and ubiquitous.** Per OWASP 2025, it's the #1 risk. Indirect prompt injection (poisoned web pages, malicious docs in your RAG corpus) is the scariest 2026 vector because it bypasses every input filter on the user message. There is no silver bullet; defense in depth is the only strategy.
2. **Agents created a new attack surface.** LLMs that take actions (LLM06 — Excessive Agency) are now in production. The 2026 OWASP update leans further into agentic AI vulnerabilities — tool-use misuse, multi-step attacks, lateral movement across MCP servers.
3. **Regulatory pressure is real.** EU AI Act (in force since 2024–2025), US Executive Orders, sector-specific guidance. Guardrails + audit trails are becoming legal requirements, not just best practices.

Practitioner playbook in 2026:
1. **Map your system against OWASP Top 10.** Identify which risks apply.
2. **Defense in depth**: input validation + prompt-injection detection (Lakera / Rebuff) + output scanning (PII, secrets, content) + agent action sandboxing (human-in-the-loop for high-stakes actions).
3. **Red-team quarterly.** Use [MITRE ATLAS](https://atlas.mitre.org/) as your checklist. Track regressions.
4. **Log everything.** Every prompt, every tool call, every action. Forensics depends on it.
5. **Sandbox agent tools.** Default-deny; allowlist; require confirmation for high-stakes actions.
6. **Train users + developers.** Both humans in the loop need to know what to look for.
7. **Plan for incidents.** Have a runbook for "agent did something bad" before it happens.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 65 | OWASP LLM Top 10 published 2023, updated 2025; guardrails tooling is 2–3 years old; frontier alignment is decades of research but still open problems. |
| Community | 85 | OWASP + MITRE ATLAS are mainstream; red-teaming is a growing profession; every serious AI company has a safety team. |
| Learning curve | 50 | Threat modeling is a skill; guardrail tuning is iterative; red-teaming is an art. |
| Performance | 60 | No solution is perfect — adversarial robustness is an arms race; false positives hurt UX; false negatives are catastrophic. |
| Cost | 75 | OWASP / MITRE: free. Lakera Guard / NeMo Guardrails / Azure Content Safety: per-request. Red-teaming: significant engineering time. |
| DX (developer experience) | 70 | NeMo Guardrails has a good DSL; Lakera is API-simple; OWASP/MITRE are docs. Tuning is the hard part. |
| Production readiness | 75 | Guardrails + content safety are production-ready; indirect prompt-injection defenses are still research-grade; alignment at the frontier-model level is ongoing. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Built-in model safety** (Anthropic, OpenAI refusals) | You need basic harmful-content blocking for free. | You need app-specific rules (no internal jargon, no specific competitor mentions). |
| **Content moderation APIs** (Azure, AWS Comprehend, Perspective) | You process user-generated content at scale. | You need semantic-level understanding of attempts to subvert the model. |
| **NeMo Guardrails (programmable)** | You want a single DSL for input/output/dialogue control. | You want minimal infra or you're not in the NVIDIA ecosystem. |
| **Lakera Guard / Rebuff** | You need prompt-injection detection specifically; you want managed. | You need on-prem or extreme customization. |
| **Human-in-the-loop** | High-stakes decisions; low volume. | Real-time, high-volume. |
| **Fine-tuning for safety** | You have a niche where the base model is consistently failing. | You need broad coverage; alignment fine-tuning is expensive and incomplete. |

## Sources

- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — 2025
- [Lasso Security — OWASP LLM Top 10 2025 Changes](https://www.lasso.security/blog/owasp-top-10-llm-2025) — 2025
- [AppSecEngineer — OWASP LLM Top 10 Risks 2025 Breakdown](https://www.appsecengineer.com/blog/owasp-top-10-for-llm-applications-2025) — 2025
- [Robust Intelligence — Evaluating LLM Security: OWASP Methodology 2025](https://www.robustintelligence.com/blog/owasp-top-10-llm-security-2025) — 2025
- [OWASP LLM Top 10 GitHub](https://github.com/owasp/llm-top-10) — 2025
- [MITRE ATLAS](https://atlas.mitre.org/) — 2026
- [Lakera](https://www.lakera.ai/) — 2026
- [Lakera Blog — Lakera Guard Prompt Injection](https://www.lakera.ai/blog/lakera-guard-prompt-injection) — 2026
- [Rebuff GitHub (now part of Lakera)](https://github.com/lakera-ai/rebuff) — 2026
- [NVIDIA NeMo Guardrails GitHub](https://github.com/NVIDIA/NeMo-Guardrails) — 2026
- [Anthropic — Safety](https://www.anthropic.com/safety) — 2026
- [Google DeepMind — Safety](https://www.deepmind.google/safety) — 2026
- [Constitutional AI](https://www.constitutionalai.ai/) — 2026
- [Alignment Forum — State of AI Alignment 2026](https://alignmentforum.org/posts/state-of-alignment-2026) — 2026
- [arXiv 2212.08073 — Constitutional AI (Bai et al.)](https://arxiv.org/abs/2212.08073) — 2022
- [Anthropic Docs — Guardrails](https://docs.anthropic.com/en/docs/build-with-claude/guardrails) — 2026
- [Azure AI Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/) — 2026