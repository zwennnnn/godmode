---
name: System Design and Architecture
slug: system-design
source: https://roadmap.sh/system-design + https://roadmap.sh/software-architect + https://roadmap.sh/software-design-architecture + https://roadmap.sh/computer-science + https://roadmap.sh/datastructures-and-algorithms
last-updated: 2026-07-30
tech-count: 5
status: in-progress
---

# System Design and Architecture

> **Category:** The patterns, principles, and computer-science fundamentals that separate senior engineers from juniors — system design, software architecture, design patterns, CS fundamentals, and data structures & algorithms.
> **Sources:** [roadmap.sh/system-design](https://roadmap.sh/system-design), [roadmap.sh/software-architect](https://roadmap.sh/software-architect), [roadmap.sh/software-design-architecture](https://roadmap.sh/software-design-architecture), [roadmap.sh/computer-science](https://roadmap.sh/computer-science), [roadmap.sh/datastructures-and-algorithms](https://roadmap.sh/datastructures-and-algorithms)

This roadmap covers what every senior engineer / staff+ engineer is expected to know: how to design systems that scale, how to choose architectures (monolith / microservices / event-driven), design patterns, and the CS fundamentals that underpin every interview and every real-world decision.

---

## Technologies (build order)

| # | Technology | File | Status |
|---|-----------|------|--------|
| 1 | System Design | [system-design.md](system-design.md) | placeholder |
| 2 | Software Architecture | [software-architecture.md](software-architecture.md) | placeholder |
| 3 | Design Patterns | [design-patterns.md](design-patterns.md) | placeholder |
| 4 | Computer Science Fundamentals | [computer-science.md](computer-science.md) | placeholder |
| 5 | Data Structures & Algorithms | [data-structures-algorithms.md](data-structures-algorithms.md) | placeholder |

---

## Quick Decision Guide

### For interview prep (junior → mid → senior)

1. Start with **DSA** ([data-structures-algorithms.md](data-structures-algorithms.md)) — LeetCode / NeetCode pattern recognition.
2. Then **System Design** ([system-design.md](system-design.md)) — caching, sharding, CAP, queues, load balancing.
3. Then **Software Architecture** ([software-architecture.md](software-architecture.md)) — monolith vs microservices, event-driven, CQRS.

### For senior+ engineering

- **Software Architecture** for the patterns (microservices, event-driven, CQRS, event sourcing).
- **Design Patterns** ([design-patterns.md](design-patterns.md)) for the GoF + modern (Saga, Outbox, Circuit Breaker).
- **System Design** for distributed system trade-offs.
- **Computer Science** ([computer-science.md](computer-science.md)) for OS / networks / DB / compilers depth.

### For staff+ / principal

Deep architectural judgment + the politics of tech choices. Read Fowler / Kleppmann / Evans; study real-world architectures (Netflix, Uber, Discord, Cloudflare blogs).

---

## Cross-references

- For specific cloud / scaling primitives, see [`../devops-cloud/README.md`](../devops-cloud/README.md).
- For specific languages, see [`../programming-languages/README.md`](../programming-languages/README.md).
- For databases (CAP theorem, sharding, replication), see [`../databases/README.md`](../databases/README.md).

---

## Build progress

**Phase 7 in progress** as of 2026-07-30. See [`../godmode.md`](../godmode.md) under `## Progress Tracker`.