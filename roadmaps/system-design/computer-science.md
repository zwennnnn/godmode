---
name: Computer Science Fundamentals
category: system-design
status: researched
last-updated: 2026-07-30
sources:
  - https://teachyourselfcs.com/
  - https://github.com/ossu/computer-science
  - https://github.com/jwasham/coding-interview-university
  - https://www.compsciedu.com/
  - https://en.wikipedia.org/wiki/Computer_science
  - https://en.wikipedia.org/wiki/Operating_system
  - https://en.wikipedia.org/wiki/Computer_network
  - https://en.wikipedia.org/wiki/Database
  - https://en.wikipedia.org/wiki/Compiler
  - https://craftinginterpreters.com/
  - https://web.archive.org/web/20230327000047/http://computationstructures.com/
  - https://missing.csail.mit.edu/
  - https://github.com/ruppysuppy/Computer-Science-Resources
  - https://ocw.mit.edu/courses/6-0006-introduction-to-cs-and-programming-using-python-fall-2016/
  - https://www.coursera.org/specializations/introduction-to-computer-science-and-programming
tags: [computer-science, algorithms, data-structures, operating-systems, networks, databases, compilers, fundamentals]
---

# Computer Science Fundamentals

## One-liner

The core CS knowledge every senior engineer is expected to have — algorithms, data structures, operating systems, networks, databases, compilers, and how computers actually work.

## What It Is

CS fundamentals are the topics taught in a traditional CS degree that are still relevant to professional engineering. They are not about writing code in a specific language; they're about understanding what's happening under the hood.

### Core topics

| Topic | What it covers | Why it matters |
|-------|----------------|----------------|
| **Algorithms** | Sorting, searching, graph algorithms, dynamic programming, greedy, divide & conquer. | Every problem you solve has an algorithmic shape. |
| **Data Structures** | Arrays, linked lists, trees, heaps, hash tables, graphs, tries. | Right structure = 1000× performance. |
| **Complexity Analysis** | Big-O, big-Theta, big-Omega; amortized; space-time trade-offs. | Predicts performance; guides design. |
| **Operating Systems** | Processes, threads, memory mgmt, virtual memory, file systems, IPC, scheduling. | Everything you do runs on an OS. |
| **Computer Networks** | OSI model, TCP/IP, UDP, HTTP/3, DNS, TLS, routing, congestion. | Every API call is a network call. |
| **Databases** | Relational model, SQL, indexing, transactions, ACID, B-trees, query optimization. | Most apps are databases with code around them. |
| **Compilers** | Lexing, parsing, ASTs, semantic analysis, code generation. | You use these every day (linters, bundlers, TS). |
| **Distributed Systems** | Consensus, replication, partitioning, CAP, eventual consistency. | Every modern system is distributed. |
| **Computer Architecture** | CPU, cache, memory hierarchy, GPU, SIMD, ARM vs x86. | Performance optimizations make sense. |
| **Operating Systems — Linux** | Kernel, syscalls, signals, networking stack. | Where production runs. |
| **Security** | Cryptography (symmetric/asymmetric), hashing, threat models, common attacks. | Every system needs security. |
| **Software Engineering** | Version control, testing, code review, CI/CD, design patterns. | How teams ship. |
| **Math for CS** | Discrete math, linear algebra (for ML), probability. | The substrate. |

### Self-study resources

| Resource | Notes |
|----------|-------|
| **[Teach Yourself CS](https://teachyourselfcs.com/)** | The canonical reading list. |
| **[OSSU Computer Science](https://github.com/ossu/computer-science)** | Open-source CS degree path. |
| **[Coding Interview University](https://github.com/jwasham/coding-interview-university)** | Practical interview prep. |
| **[Missing Semester (MIT)](https://missing.csail.mit.edu/)** | The CS course MIT forgot to teach. |
| **[Crafting Interpreters](https://craftinginterpreters.com/)** | Best book on compiler implementation. |
| **CLRS (Cormen, Leiserson, Rivest, Stein)** | The algorithms bible. |
| **OSTEP (Operating Systems: Three Easy Pieces)** | Free; best modern OS book. |

## When To Use It

- **You're learning to be a senior engineer** — these are the foundations.
- **You're preparing for interviews** — especially at top companies.
- **You're debugging a performance issue** — knowing how CPUs / caches / networks work helps.
- **You're designing a system** — distributed systems knowledge is required.
- **You're choosing a database** — you need to understand indexing, query plans.
- **You're optimizing code** — algorithmic complexity + memory hierarchy matter.

## When NOT To Use It

- **You just want to ship a feature** — sometimes you just need to write the code.
- **The theory doesn't apply** — most CRUD doesn't need fancy algorithms.
- **You're in an unrelated role** — PM, designer, marketer — different foundations.
- **You can use a library** — most algorithms are in stdlib / well-known packages.
- **You're optimizing prematurely** — write clear code first; optimize after measuring.

## Why It Matters in 2026

Three forces:

1. **AI is changing what engineers do, not the foundations.** AI can write code; it cannot (yet) reason about algorithmic trade-offs, system-level performance, or design. CS fundamentals are the differentiator.
2. **The performance frontier is back.** With AI-generated code dominating the boilerplate, human value is in performance-critical work: hot paths, distributed systems, low-level optimizations.
3. **Interview filters still gate careers.** Top companies still test algorithms + systems. Knowing CS fundamentals opens doors.

Practitioner playbook in 2026:
1. **Cover the basics once** — Teach Yourself CS reading list.
2. **Deepen on your specialty** — distributed systems if you do backend; OS + networks if you do infra; ML math if you do AI.
3. **Read modern resources** — Missing Semester, ByteByteGo, williamfiset videos.
4. **Practice interviews** — LeetCode, Codemia, Hello Interview.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 70+ years of CS; the canon is settled. |
| Community | 100 | Massive; OSSU / Teach Yourself CS / every university. |
| Learning curve | 30 | Steep; many topics; years of study. |
| Performance | N/A | Knowledge. |
| Cost | 80 | Free resources available; some books cost money. |
| DX | N/A | Learning, not building. |
| Production readiness | N/A | Knowledge. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Bootcamp / no-CS-degree path** | You want to ship apps fast. | You want senior-level understanding. |
| **Just learn frameworks** | Junior roles; specific jobs. | Long-term engineering career. |
| **Specialized (ML / distributed)** | After you have the foundation. | Before. |

## Sources

- [Teach Yourself CS](https://teachyourselfcs.com/) — 2026
- [OSSU Computer Science](https://github.com/ossu/computer-science) — 2026
- [Coding Interview University (jwasham)](https://github.com/jwasham/coding-interview-university) — 2026
- [CompSciEdu](https://www.compsciedu.com/) — 2026
- [Wikipedia — Computer Science](https://en.wikipedia.org/wiki/Computer_science) — 2026
- [Wikipedia — Operating System](https://en.wikipedia.org/wiki/Operating_system) — 2026
- [Wikipedia — Computer Network](https://en.wikipedia.org/wiki/Computer_network) — 2026
- [Wikipedia — Database](https://en.wikipedia.org/wiki/Database) — 2026
- [Wikipedia — Compiler](https://en.wikipedia.org/wiki/Compiler) — 2026
- [Crafting Interpreters](https://craftinginterpreters.com/) — 2026
- [Missing Semester (MIT)](https://missing.csail.mit.edu/) — 2026
- [Computer Science Resources (ruppysuppy)](https://github.com/ruppysuppy/Computer-Science-Resources) — 2026
- [MIT OCW — Intro to CS and Programming](https://ocw.mit.edu/courses/6-0006-introduction-to-cs-and-programming-using-python-fall-2016/) — 2026
- [Coursera — Intro to Computer Science and Programming](https://www.coursera.org/specializations/introduction-to-computer-science-and-programming) — 2026