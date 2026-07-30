---
name: Application Security (AppSec)
category: cyber-security
status: researched
last-updated: 2026-07-30
sources:
  - https://owasp.org/
  - https://owasp.org/www-project-top-ten/
  - https://owasp.org/www-project-top-ten/2025/
  - https://owasp.org/www-project-api-security/
  - https://cheatsheetseries.owasp.org/
  - https://owasp.org/www-project-application-security-verification-standard/
  - https://github.com/OWASP/CheatSheetSeries
  - https://github.com/returntocorp/semgrep
  - https://semgrep.dev/
  - https://github.com/gitleaks/gitleaks
  - https://github.com/aquasecurity/trivy
  - https://www.aquasec.com/products/trivy/
  - https://snyk.io/
  - https://github.com/snyk/cli
  - https://github.com/anchore/syft
  - https://github.com/anchore/grype
  - https://www.veracode.com/
tags: [appsec, owasp, owasp-top-10, sast, dast, sca, secure-coding, vulnerability-scanning]
---

# Application Security (AppSec)

## One-liner

The discipline of building secure applications — secure coding practices, the OWASP Top 10, vulnerability scanning (SAST / DAST / SCA), and the threat modeling that prevents the most common breaches.

## What It Is

AppSec covers the security of the applications you build. It includes:

| Layer | What |
|-------|------|
| **Secure coding** | Patterns + anti-patterns for input validation, auth, crypto, etc. |
| **Threat modeling** | Identify what could go wrong before coding (STRIDE, PASTA). |
| **SAST** (Static Application Security Testing) | Scan source for vulns (Semgrep, Snyk Code, CodeQL). |
| **DAST** (Dynamic Application Security Testing) | Probe running app (OWASP ZAP, Burp Suite). |
| **SCA** (Software Composition Analysis) | Find vulns in dependencies (Snyk Open Source, Trivy, npm audit). |
| **Secrets scanning** | Find leaked secrets in code (Gitleaks, TruffleHog). |
| **Container scanning** | Find vulns in images (Trivy, Grype, Snyk Container). |
| **IaC scanning** | Find misconfigurations in Terraform / K8s (Checkov, tfsec). |
| **Penetration testing** | Manual + automated security testing (see [penetration-testing.md](penetration-testing.md)). |
| **Bug bounty** | Crowdsourced vuln finding. |

### The 2026 security frameworks (app-focused)

| Framework | Source | Notes |
|-----------|--------|-------|
| **[OWASP Top 10](https://owasp.org/www-project-top-ten/)** | OWASP | The canonical web app risk list; 2025 update. |
| **[OWASP API Security Top 10](https://owasp.org/www-project-api-security/)** | OWASP | API-specific risks. |
| **[OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)** | OWASP | Verification standard; depth checklist. |
| **[OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)** | OWASP | Practical secure coding guides. |
| **NIST SP 800-53** | NIST | General controls. |
| **CWE** | MITRE | Common Weakness Enumeration. |
| **CVE** | MITRE | Specific vulnerabilities. |

### OWASP Top 10 (the canonical web app risk list)

The 2025 edition (latest at writing):
1. **Broken Access Control**
2. **Cryptographic Failures**
3. **Injection** (SQL injection, XSS, command injection, etc.)
4. **Insecure Design**
5. **Security Misconfiguration**
6. **Vulnerable and Outdated Components**
7. **Identification and Authentication Failures**
8. **Software and Data Integrity Failures**
9. **Security Logging and Monitoring Failures**
10. **Server-Side Request Forgery (SSRF)**

### Top tools (2026)

| Tool | Purpose |
|------|---------|
| **[Semgrep](https://semgrep.dev/)** | SAST; fast; OSS + cloud. |
| **[Snyk](https://snyk.io/)** | SAST + SCA + container + IaC; commercial. |
| **[Trivy](https://www.aquasec.com/products/trivy/)** | Vulnerability scanner; SCA + container + IaC. |
| **[OWASP ZAP](https://www.zaproxy.org/)** | DAST; free. |
| **[Burp Suite](https://portswigger.net/burp)** | DAST / web security testing. |
| **[CodeQL](https://codeql.github.com/)** | SAST from GitHub. |
| **[Gitleaks](https://github.com/gitleaks/gitleaks)** | Secrets scanning. |
| **[TruffleHog](https://github.com/trufflesecurity/trufflehog)** | Secrets scanning; verified. |
| **[Checkov](https://www.checkov.io/)** | IaC scanning. |
| **[tfsec](https://github.com/aquasecurity/tfsec)** | Terraform scanning. |
| **[Grype](https://github.com/anchore/grype)** | Container vuln scanning. |
| **[Syft](https://github.com/anchore/syft)** | SBOM generation. |
| **[Veracode](https://www.veracode.com/)** | Enterprise AppSec platform. |

Adoption: AppSec is non-optional for any production system. SAST + SCA in CI is baseline. OWASP Top 10 is required reading for every dev. Bug bounties are common at major companies.

## When To Use It

- **You're shipping any production app** — period.
- **You have a public-facing API** — OWASP API Top 10.
- **You want to find vulns before attackers do** — pentest.
- **You want to comply (SOC 2, PCI, HIPAA)** — AppSec evidence.
- **You have a bug bounty program** — validate fixes.
- **You want to use AI for code** — AI code is more likely to have security bugs; AppSec scans catch them.

## When NOT To Use It

- **You're building a static site** — minimal risk.
- **You're prototyping** — defer security to production-readiness stage.
- **You have no users yet** — premature.
- **You don't have CI** — security scanning requires automation.

## Why It Matters in 2026

Three forces:

1. **AI-generated code introduces more vulns.** Copilot / Cursor / Claude Code generate code faster than humans can review for security. Automated scanning is mandatory.
2. **Supply-chain attacks.** npm / PyPI / Docker Hub compromises are regular. SCA tools are the defense.
3. **Regulatory pressure.** EU EAA (2025), US SEC disclosure rules, DORA — security incidents must be disclosed.

Practitioner playbook in 2026:
1. **SAST in CI** — Semgrep or Snyk Code.
2. **SCA in CI** — Snyk Open Source, npm audit, Trivy.
3. **Secrets scanning in pre-commit + CI** — Gitleaks / TruffleHog.
4. **Container scanning** — Trivy / Grype before push.
5. **DAST in staging** — OWASP ZAP.
6. **Pentest before major launches** — annual or per release.
7. **Bug bounty** — HackerOne / Bugcrowd.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 95 | OWASP since 2003; mature discipline. |
| Community | 100 | Massive; OWASP; conferences. |
| Learning curve | 60 | Many tools; concepts easy; mastery takes years. |
| Performance | 90 | Tools are fast; integrate in CI. |
| Cost | 75 | OSS free; commercial (Snyk, Veracode) paid. |
| DX | 80 | Tools getting better; some still noisy. |
| Production readiness | 100 | Every production system. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **No AppSec** | Never. | — |
| **SAST only** | Find code-level bugs. | Dependency vulns. |
| **DAST only** | Find runtime bugs. | Code-level bugs. |
| **Pentest only** | Periodic validation. | Continuous coverage. |
| **Bug bounty only** | Find vulns in production. | Foundational security. |

## Sources

- [OWASP](https://owasp.org/) — 2026
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) — 2026
- [OWASP Top 10 2025](https://owasp.org/www-project-top-ten/2025/) — 2025
- [OWASP API Security](https://owasp.org/www-project-api-security/) — 2026
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) — 2026
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) — 2026
- [OWASP CheatSheetSeries GitHub](https://github.com/OWASP/CheatSheetSeries) — 2026
- [Semgrep GitHub (returntocorp/semgrep)](https://github.com/returntocorp/semgrep) — 2026
- [Semgrep](https://semgrep.dev/) — 2026
- [Gitleaks GitHub (gitleaks/gitleaks)](https://github.com/gitleaks/gitleaks) — 2026
- [Trivy GitHub (aquasecurity/trivy)](https://github.com/aquasecurity/trivy) — 2026
- [Trivy](https://www.aquasec.com/products/trivy/) — 2026
- [Snyk](https://snyk.io/) — 2026
- [Snyk CLI GitHub (snyk/cli)](https://github.com/snyk/cli) — 2026
- [Syft GitHub (anchore/syft)](https://github.com/anchore/syft) — 2026
- [Grype GitHub (anchore/grype)](https://github.com/anchore/grype) — 2026
- [Veracode](https://www.veracode.com/) — 2026