---
name: Cyber Security
category: cyber-security
status: researched
last-updated: 2026-07-30
sources:
  - https://en.wikipedia.org/wiki/Computer_security
  - https://en.wikipedia.org/wiki/Information_security
  - https://www.cisa.gov/
  - https://www.nist.gov/cyberframework
  - https://owasp.org/
  - https://www.sans.org/
  - https://www.sans.org/security-resources/posters/22/english/cheat-sheet
  - https://www.cvedetails.com/
  - https://nvd.nist.gov/
  - https://attack.mitre.org/
  - https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final
  - https://csrc.nist.gov/publications/detail/sp/800-63/4/final
  - https://cheatsheetseries.owasp.org/
  - https://www.cisecurity.org/cis-benchmarks
  - https://www.nist.gov/cyberframework
  - https://www.cyber.gov.au/
tags: [cyber-security, infosec, cia-triad, threat-model, nist-csf, mitre-attack, owasp]
---

# Cyber Security

## One-liner

The discipline of protecting systems, networks, data, and users from attack — the foundational knowledge every engineer + DevOps + tech lead needs in 2026.

## What It Is

Cyber security (or infosec) is the practice of defending computer systems, networks, applications, and data from attack, damage, or unauthorized access. It spans:

| Layer | What |
|-------|------|
| **Application security (AppSec)** | See [application-security.md](application-security.md). |
| **Network security** | See [network-security.md](network-security.md). |
| **Endpoint security** | Laptops, phones, IoT devices. |
| **Cloud security** | AWS / GCP / Azure configurations. |
| **Identity & Access Management (IAM)** | Auth, MFA, RBAC. |
| **Cryptography** | Symmetric / asymmetric, hashing, TLS. |
| **Penetration testing** | See [penetration-testing.md](penetration-testing.md). |
| **Incident response** | Detection + response to breaches. |
| **Threat modeling** | STRIDE, PASTA, attack trees. |
| **Compliance** | GDPR, HIPAA, SOC2, PCI-DSS, ISO 27001. |

### The CIA triad (foundational)

- **Confidentiality** — only authorized access.
- **Integrity** — data is accurate + unaltered.
- **Availability** — systems are up when needed.

### The 2026 security frameworks

| Framework | Source | Notes |
|-----------|--------|-------|
| **NIST CSF 2.0** | NIST | Govern, Identify, Protect, Detect, Respond, Recover. |
| **NIST SP 800-53** | NIST | 1000+ controls; the US federal standard. |
| **MITRE ATT&CK** | MITRE | Adversary tactics / techniques catalog. |
| **OWASP Top 10** | OWASP | The web app risks; see [application-security.md](application-security.md). |
| **CIS Controls** | Center for Internet Security | Prioritized security actions. |
| **NIST SP 800-63** | NIST | Digital identity guidelines. |
| **ISO 27001 / 27002** | ISO | International ISMS standard. |
| **SOC 2** | AICPA | Trust services criteria for SaaS. |
| **PCI-DSS** | PCI SSC | Payment card industry. |
| **HIPAA** | US HHS | Healthcare PHI. |
| **GDPR** | EU | Personal data. |
| **DORA** | EU | Financial services (2025+). |

### Security roles

| Role | Focus |
|------|-------|
| **Security Engineer** | Build secure systems; review code. |
| **AppSec Engineer** | Application security (SAST, DAST, SCA). |
| **Pentester** | Find vulnerabilities. |
| **Red Team** | Adversary simulation. |
| **Blue Team** | Defenders (SOC, incident response). |
| **Security Architect** | Design secure systems. |
| **GRC** | Governance, Risk, Compliance. |
| **CISO** | Security leadership. |

### The 2026 threat landscape

| Threat | 2026 status |
|--------|-------------|
| **Ransomware** | Still #1; double-extortion; supply-chain attacks. |
| **Supply-chain attacks** | (e.g. SolarWinds, 3CX, npm packages) — growing. |
| **AI-powered attacks** | Deepfakes; AI-generated phishing; LLM jailbreaks. |
| **Cloud misconfiguration** | #1 cloud breach cause. |
| **Credential theft** | #1 initial access vector. |
| **Zero-day exploits** | Mobile + browsers + virtualization. |

Adoption: Cyber security is one of the fastest-growing tech disciplines. ~5M unfilled jobs globally; every company needs security. CISO is now a board-level role at every Fortune 500.

## When To Use It

- **You're building any user-facing system** — required by law + ethics.
- **You're handling PII / PHI / PCI data** — compliance required.
- **You operate cloud infrastructure** — misconfiguration is the #1 breach cause.
- **You're designing a new system** — bake security in from day one.
- **You want to find bugs in your systems** — pentest.

## When NOT To Use It

- **You have no users / no data** — premature.
- **You're building a static website** — basic TLS is enough.
- **You're a one-person hobby project** — basic hygiene only.
- **Compliance theater** — don't write policies you don't enforce.

## Why It Matters in 2026

Three forces:

1. **AI is both weapon and shield.** Attackers use AI for phishing + deepfakes + code analysis. Defenders use AI for detection + triage + vuln scanning. The arms race is real.
2. **Regulatory pressure is global.** EU EAA (2025), DORA (2025), NIS2 (EU), updated US Executive Orders — security is regulated.
3. **Supply-chain attacks are the new normal.** SolarWinds → 3CX → npm package attacks → xz-utils backdoor. Defense requires SBOM, signed packages, attestation.

Practitioner playbook in 2026:
1. **NIST CSF 2.0** — baseline framework.
2. **OWASP Top 10** — for apps.
3. **MITRE ATT&CK** — for detection / response.
4. **Zero Trust** — "never trust, always verify" (NIST SP 800-207).
5. **Defense in depth** — multiple layers.
6. **Bolt-on basics**: MFA everywhere, patching, least privilege, logging.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 50+ years; well-established discipline. |
| Community | 100 | Massive; conferences (Black Hat, DEF CON, RSA); CTFs. |
| Learning curve | 50 | Many domains; takes years to master. |
| Performance | N/A | Discipline. |
| Cost | 80 | Frameworks free; tools + people $$$ . |
| DX | 75 | Tools getting better; still manual-heavy. |
| Production readiness | 100 | Every production system. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **No security (just ship)** | Never. | — |
| **Compliance only** | Regulated industry minimum. | Real security. |
| **Penetration test only** | Validate specific concerns. | Holistic security. |
| **Bug bounty** | Find bugs in production. | Foundational security. |
| **AI-driven everything** | Triage + detection. | Strategic decisions. |

## Sources

- [Wikipedia — Computer Security](https://en.wikipedia.org/wiki/Computer_security) — 2026
- [Wikipedia — Information Security](https://en.wikipedia.org/wiki/Information_security) — 2026
- [CISA](https://www.cisa.gov/) — 2026
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) — 2026
- [OWASP](https://owasp.org/) — 2026
- [SANS Institute](https://www.sans.org/) — 2026
- [SANS Cheat Sheets](https://www.sans.org/security-resources/posters/22/english/cheat-sheet) — 2026
- [CVE Details](https://www.cvedetails.com/) — 2026
- [National Vulnerability Database](https://nvd.nist.gov/) — 2026
- [MITRE ATT&CK](https://attack.mitre.org/) — 2026
- [NIST SP 800-53 Rev 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final) — 2026
- [NIST SP 800-63-4 (Digital Identity)](https://csrc.nist.gov/publications/detail/sp/800-63/4/final) — 2026
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) — 2026
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) — 2026
- [NIST CSF 2.0](https://www.nist.gov/cyberframework) — 2026
- [Australian Cyber Security Centre](https://www.cyber.gov.au/) — 2026