---
name: Network Security
category: cyber-security
status: researched
last-updated: 2026-07-30
sources:
  - https://en.wikipedia.org/wiki/Network_security
  - https://en.wikipedia.org/wiki/Computer_network
  - https://www.cloudflare.com/learning/network-layer-security/
  - https://cheatsheetseries.owasp.org/cheatsheets/Network_Security_Cheat_Sheet.html
  - https://www.sans.org/network-security/
  - https://csrc.nist.gov/publications/detail/sp/800-41/rev-1/final
  - https://csrc.nist.gov/publications/detail/sp/800-77/rev-1/final
  - https://csrc.nist.gov/publications/detail/sp/800-207/final
  - https://www.wireguard.com/
  - https://www.wireshark.org/
  - https://www.cloudflare.com/learning/ddos/glossary/tls-encryption/
  - https://github.com/ovh/tat
  - https://tailscale.com/
  - https://www.cloudflare.com/learning/access-management/zero-trust-network-access-ztna/
  - https://www.zscaler.com/
tags: [network-security, tls, firewall, vpn, zero-trust, segmentation, ids, ips, waf]
---

# Network Security

## One-liner

The discipline of protecting networks — firewalls, intrusion detection, TLS, VPNs, zero-trust, segmentation — the foundation of every secure system.

## What It Is

Network security covers the protection of data in transit + the infrastructure that moves it. Layers:

| Layer | What |
|-------|------|
| **TLS / HTTPS** | Encrypting data in transit (TLS 1.3). |
| **Firewalls** | Filtering traffic by IP / port / protocol (stateful, WAF). |
| **Intrusion Detection / Prevention (IDS / IPS)** | Detecting + blocking attacks (Snort, Suricata, Zeek). |
| **VPNs** | Encrypted tunnels between networks (WireGuard, IPsec, OpenVPN). |
| **Zero Trust** | "Never trust, always verify" — every request authenticated (NIST SP 800-207). |
| **Network segmentation** | Dividing networks into zones; lateral movement limits. |
| **DDoS protection** | Mitigating volumetric attacks (Cloudflare, AWS Shield, Akamai). |
| **Network Access Control (NAC)** | Authenticating + authorizing devices on the network. |
| **DNS security** | DNSSEC, DNS filtering (Pi-hole, Cloudflare 1.1.1.1 for Families). |
| **Email security** | SPF, DKIM, DMARC for anti-spoofing. |
| **Wireless security** | WPA3, evil twin detection. |

### The 2026 network security stack

| Layer | Tools / Concepts |
|-------|------------------|
| **TLS** | Let's Encrypt (free certs); TLS 1.3 default. |
| **Firewalls** | iptables / nftables (Linux); pfSense / OPNsense (open source); cloud-native Security Groups (AWS / GCP / Azure). |
| **WAF** | Cloudflare WAF, AWS WAF, ModSecurity, Azure WAF. |
| **DDoS** | Cloudflare, AWS Shield, Akamai, Fastly. |
| **IDS / IPS** | Snort, Suricata, Zeek; cloud-native (AWS GuardDuty, Azure Sentinel). |
| **VPN / Zero-Trust** | **WireGuard** (modern default), Tailscale, Cloudflare Tunnel, **Cloudflare Access**, **Zscaler**, **Tailscale** (overlay). |
| **Network observability** | Wireshark, tcpdump, Zeek. |
| **DNS security** | DNSSEC, Cloudflare DNS, Quad9. |

### The shift to Zero Trust

Traditional "castle + moat" (VPN + perimeter firewall) is being replaced by **Zero Trust**:
- **Every request authenticated** — no implicit trust based on network location.
- **Least privilege** — minimum access needed.
- **Assume breach** — design as if the attacker is already inside.
- **Verify explicitly** — multiple signals (identity, device, location, behavior).
- **Microsegmentation** — fine-grained network policies.

**NIST SP 800-207** is the canonical Zero Trust Architecture document.

### VPNs vs Zero Trust

| Aspect | VPN | Zero Trust (ZTNA) |
|--------|-----|--------------------|
| **Trust model** | Network = trusted | No network = trusted |
| **Performance** | Hairpinning; latency | Direct routing; lower latency |
| **User experience** | Always-on; slow connect | App-by-app; instant |
| **Compromise impact** | Full network access | Limited to app |
| **Adoption** | Legacy | Modern default |

Adoption: Zero Trust is the new standard for enterprise networks. The US federal government mandated it (Executive Order 14028, 2021). Cloudflare Access, Zscaler, Tailscale, Cloudflare WARP are the dominant players.

## When To Use It

- **You're operating any internet-facing service** — TLS + WAF + DDoS protection.
- **You have multiple offices / remote workers** — VPN or Zero Trust.
- **You operate regulated workloads** — segmentation + access control.
- **You're moving to the cloud** — cloud-native security groups + WAF + Zero Trust.
- **You're modernizing a legacy VPN** — Zero Trust is the path.

## When NOT To Use It

- **Static website** — basic TLS + Cloudflare CDN is enough.
- **You're 100% on a managed PaaS** — they handle it.
- **You're prototyping** — defer to production-readiness.
- **You can't operate it** — use a managed service.

## Why It Matters in 2026

Three forces:

1. **Zero Trust is the new default.** US gov mandate + industry shift; VPNs are legacy.
2. **AI-assisted attacks.** DDoS amplification, AI-driven network scanning — defenses need AI too.
3. **Cloud-native networking.** VPCs, security groups, IAM, mesh VPNs — all cloud-first.

Practitioner playbook in 2026:
1. **TLS everywhere** — Let's Encrypt + TLS 1.3.
2. **Zero Trust for remote access** — Cloudflare Access / Tailscale.
3. **WAF + DDoS** — Cloudflare (default).
4. **IDS / IPS for visibility** — Suricata + Zeek.
5. **Network segmentation** — VPCs + security groups.
6. **DNS security** — DNSSEC + Cloudflare DNS.

## Scoring Matrix (0–100)

### Cloudflare (representative of modern stack)
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | Battle-tested at every scale. |
| Community | 95 | Massive. |
| Learning curve | 85 | Easy to start; deep features. |
| Performance | 100 | Best-in-class. |
| Cost | 80 | Free tier; paid reasonable. |
| DX | 95 | Excellent. |
| Production readiness | 100 | Battle-tested. |

### Zero Trust (concept)
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 80 | Standard since 2021 (US mandate). |
| Community | 90 | Growing; Zscaler, Cloudflare, Tailscale. |
| Learning curve | 60 | Architecture shift; takes study. |
| Performance | 90 | Better than VPN. |
| Cost | 75 | Managed; per-user pricing. |
| DX | 80 | Getting better. |
| Production readiness | 90 | Used at every Fortune 500. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **VPN** | Legacy; simple; small teams. | Modern enterprise; security. |
| **Zero Trust (ZTNA)** | Modern default. | Legacy integration; very small teams. |
| **No encryption** | Never. | — |
| **Hardware firewall only** | On-prem legacy. | Cloud-native; remote work. |
| **WAF** | Public web apps. | Internal apps. |

## Sources

- [Wikipedia — Network Security](https://en.wikipedia.org/wiki/Network_security) — 2026
- [Wikipedia — Computer Network](https://en.wikipedia.org/wiki/Computer_network) — 2026
- [Cloudflare — Network Layer Security](https://www.cloudflare.com/learning/network-layer-security/) — 2026
- [OWASP Network Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Network_Security_Cheat_Sheet.html) — 2026
- [SANS Network Security](https://www.sans.org/network-security/) — 2026
- [NIST SP 800-41 Rev 1 (Firewalls)](https://csrc.nist.gov/publications/detail/sp/800-41/rev-1/final) — 2026
- [NIST SP 800-77 Rev 1 (IPsec VPNs)](https://csrc.nist.gov/publications/detail/sp/800-77/rev-1/final) — 2026
- [NIST SP 800-207 (Zero Trust Architecture)](https://csrc.nist.gov/publications/detail/sp/800-207/final) — 2026
- [WireGuard](https://www.wireguard.com/) — 2026
- [Wireshark](https://www.wireshark.org/) — 2026
- [Cloudflare — TLS](https://www.cloudflare.com/learning/ddos/glossary/tls-encryption/) — 2026
- [Tailscale](https://tailscale.com/) — 2026
- [Cloudflare — Zero Trust Network Access (ZTNA)](https://www.cloudflare.com/learning/access-management/zero-trust-network-access-ztna/) — 2026
- [Zscaler](https://www.zscaler.com/) — 2026