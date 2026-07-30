---
name: Penetration Testing
category: cyber-security
status: researched
last-updated: 2026-07-30
sources:
  - https://www.offsec.com/
  - https://www.kali.org/
  - https://github.com/topics/pentesting
  - https://owasp.org/www-project-web-security-testing-guide/
  - https://github.com/rapid7/metasploit-framework
  - https://www.metasploit.com/
  - https://portswigger.net/burp
  - https://portswigger.net/web-security
  - https://www.zaproxy.org/
  - https://github.com/zaproxy/zaproxy
  - https://owasp.org/www-project-top-ten/
  - https://www.hackerone.com/
  - https://www.bugcrowd.com/
  - https://www.sans.org/cyber-security-skills-roadmap/
  - https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/
  - https://www.offensive-security.com/pwk-online/
tags: [pentesting, penetration-testing, bug-bounty, kali, metasploit, burp-suite, owasp-zap, ethical-hacking]
---

# Penetration Testing

## One-liner

The practice of ethically attacking your own systems to find vulnerabilities before real attackers do — methodology, tools, certifications, and bug bounty platforms in 2026.

## What It Is

Penetration testing (pentesting) is the authorized simulation of an attack on a system to evaluate its security. Pentesters use the same tools and techniques as real attackers, but with permission and a goal of finding + reporting vulnerabilities.

### Types of pentesting

| Type | Description |
|------|-------------|
| **Black box** | No internal knowledge; simulates external attacker. |
| **White box** | Full source + architecture access; deeper coverage. |
| **Gray box** | Partial knowledge (e.g. user credentials); realistic for insider threats. |
| **External** | Targeting internet-facing assets. |
| **Internal** | Testing from inside the network (post-breach simulation). |
| **Web app** | OWASP Top 10 focused. |
| **Mobile** | iOS / Android specific. |
| **Network** | Infrastructure + segmentation + firewalls. |
| **Cloud** | AWS / GCP / Azure configurations + IAM. |
| **Red team** | Full-scope adversary simulation; multi-week. |
| **Bug bounty** | Continuous; open to external researchers. |

### The pentesting methodology (PTES / OWASP WSTG)

1. **Pre-engagement** — scope, rules of engagement, NDA.
2. **Reconnaissance** — passive + active info gathering.
3. **Threat modeling** — identify likely attack vectors.
4. **Vulnerability analysis** — automated + manual scans.
5. **Exploitation** — verify vulns are real, demonstrate impact.
6. **Post-exploitation** — what can we do after compromise? (privilege escalation, lateral movement, data exfil).
7. **Reporting** — executive + technical findings + remediation.
8. **Re-test** — verify fixes.

### The 2026 pentesting toolkit

| Category | Tools |
|----------|-------|
| **OS** | [Kali Linux](https://www.kali.org/), Parrot OS. |
| **Frameworks** | [Metasploit](https://www.metasploit.com/), Cobalt Strike (commercial). |
| **Web app** | [Burp Suite](https://portswigger.net/burp), [OWASP ZAP](https://www.zaproxy.org/). |
| **Network scanning** | Nmap, Masscan, RustScan. |
| **Web app recon** | httpx, subfinder, nuclei, katana. |
| **Password attacks** | Hashcat, John the Ripper. |
| **Wireless** | Aircrack-ng, Wifite. |
| **Active Directory** | BloodHound, CrackMapExec, Mimikatz. |
| **Exploit DB** | [Exploit-DB](https://www.exploit-db.com/), GitHub PoCs. |
| **AI-assisted** | [Burp AI](https://portswigger.net/burp), custom GPTs. |

### Top certifications (2026)

| Cert | Issuer | Focus |
|------|--------|-------|
| **OSCP** | OffSec | Hands-on pentest; the gold standard. |
| **OSWE** | OffSec | Web app exploitation. |
| **OSEP** | OffSec | Experienced pentester. |
| **CRTP** | Altered Security | Active Directory. |
| **CEH** | EC-Council | Broad ethical hacking (commercial). |
| **GPEN** | GIAC | Penetration testing. |
| **PNPT** | TCM Security | Practical; junior-friendly. |
| **eCPPT** | INE Security eLearn | Practical. |
| **CBBH** | Hack The Box | Bug bounty hunter. |

### Bug bounty platforms (2026)

| Platform | Notes |
|----------|-------|
| **[HackerOne](https://www.hackerone.com/)** | The largest; HackerOne + GitHub. |
| **[Bugcrowd](https://www.bugcrowd.com/)** | Crowdsourced; enterprise programs. |
| **Intigriti** | European; growing. |
| **YesWeHack** | European; growing. |
| **Open Bug Bounty** | Free; smaller programs. |
| **Meta Bug Bounty** | Facebook / Instagram / WhatsApp. |
| **Google VRP** | Google / Chrome / Android. |
| **Microsoft Bug Bounty** | Windows / Azure / 365. |
| **Apple Security Bounty** | iOS / macOS. |

Adoption: Pentesting is a $5B+ industry. Every Fortune 500 has an annual pentest; SOC 2 requires it. Bug bounty programs are standard at Google, Meta, Microsoft, Apple, every major tech company.

## When To Use It

- **You ship a public-facing app** — pentest before major launches.
- **You have SOC 2 / PCI / HIPAA** — required.
- **You want to find your own bugs** — before attackers do.
- **You have an M&A** — diligence pentest of target.
- **You want to validate your AppSec program** — pentest vs SAST.
- **You want to make $$$ as a researcher** — bug bounty.

## When NOT To Use It

- **You have no systems to test** — premature.
- **You haven't done basic SAST + SCA** — pentest is the top of the security pyramid.
- **You can't act on findings** — useless if you don't fix.
- **You have a personal blog** — overkill.

## Why It Matters in 2026

Three forces:

1. **AI-augmented pentesting.** Burp AI + custom GPTs automate recon + vuln finding. Pentesters focus on creativity + impact.
2. **Continuous pentesting is the new annual.** HackerOne + Bugcrowd offer always-on engagements.
3. **Regulatory requirement.** SOC 2, PCI-DSS, HIPAA, EU DORA — pentest is mandatory in many contexts.

Practitioner playbook in 2026:
1. **Annual pentest** — third-party firm.
2. **Bug bounty** — continuous; lower severity findings.
3. **Internal red team** — for mature programs.
4. **Use AI** — Burp AI + custom tools to amplify.
5. **Report well** — executive + technical + reproducible PoC.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 50+ years; well-established. |
| Community | 100 | Massive; conferences; CTFs; bug bounty. |
| Learning curve | 50 | Many tools; methodology takes years. |
| Performance | N/A | Practice. |
| Cost | 60 | Pentest firms $$$; bug bounty = free + payout. |
| DX | 80 | Tools getting better; AI helps. |
| Production readiness | 100 | Every serious company. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **SAST / DAST** | Continuous; low cost. | Deep exploitation. |
| **Bug bounty** | Continuous external eyes. | Periodic deep audits. |
| **Red team** | Full-scope adversary sim. | Single-system pentest. |
| **Self-assessment (SAST + SCA)** | Always. | Pentest is the top of pyramid. |
| **No testing** | Never. | — |

## Sources

- [OffSec](https://www.offsec.com/) — 2026
- [Kali Linux](https://www.kali.org/) — 2026
- [GitHub — Pentesting Topic](https://github.com/topics/pentesting) — 2026
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) — 2026
- [Metasploit GitHub (rapid7/metasploit-framework)](https://github.com/rapid7/metasploit-framework) — 2026
- [Metasploit](https://www.metasploit.com/) — 2026
- [Burp Suite (PortSwigger)](https://portswigger.net/burp) — 2026
- [PortSwigger Web Security Academy](https://portswigger.net/web-security) — 2026
- [OWASP ZAP](https://www.zaproxy.org/) — 2026
- [OWASP ZAP GitHub (zaproxy/zaproxy)](https://github.com/zaproxy/zaproxy) — 2026
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) — 2026
- [HackerOne](https://www.hackerone.com/) — 2026
- [Bugcrowd](https://www.bugcrowd.com/) — 2026
- [SANS Cyber Security Skills Roadmap](https://www.sans.org/cyber-security-skills-roadmap/) — 2026
- [EC-Council CEH](https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/) — 2026
- [OffSec PWK Online (OSCP)](https://www.offensive-security.com/pwk-online/) — 2026