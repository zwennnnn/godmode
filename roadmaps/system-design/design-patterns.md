---
name: Design Patterns
category: system-design
status: researched
last-updated: 2026-07-30
sources:
  - https://refactoring.guru/design-patterns
  - https://en.wikipedia.org/wiki/Design_Patterns
  - https://www.oodesign.com/
  - https://sourcemaking.com/design_patterns
  - https://github.com/RefactoringGuru/design-patterns-php
  - https://www.martinfowler.com/eaaCatalog/
  - https://martinfowler.com/
  - https://en.wikipedia.org/wiki/GRASP_(object-oriented_design)
  - https://en.wikipedia.org/wiki/SOLID
  - https://www.thoughtworks.com/radar
  - https://refactoring.guru/design-patterns/behavioral-patterns
  - https://refactoring.guru/design-patterns/structural-patterns
  - https://refactoring.guru/design-patterns/creational-patterns
tags: [design-patterns, gang-of-four, solid, grasp, oop, architecture, refactoring]
---

# Design Patterns

## One-liner

The reusable, named solutions to recurring problems in object-oriented software design — the Gang of Four classics (1994) plus modern variants, codified so teams can communicate and reason about design.

## What It Is

Design patterns are **named, abstracted solutions** to problems you see over and over in software. They aren't libraries or frameworks; they're templates for how to structure code. The original catalog (Gang of Four, 1994) classified 23 patterns into three families; modern practice extends with concurrency, architectural, and reactive variants.

### Creational patterns
How objects are created — decoupling instantiation from use.

| Pattern | Intent | When |
|---------|--------|------|
| **Factory Method** | Defer instantiation to subclasses. | Multiple object types from one creator. |
| **Abstract Factory** | Family of related objects. | UI themes; cross-platform widgets. |
| **Builder** | Step-by-step construction of complex objects. | Many optional fields; readable construction. |
| **Prototype** | Clone existing objects. | Object creation is expensive. |
| **Singleton** | One instance globally. | Config, loggers — use sparingly. |

### Structural patterns
How classes and objects are composed.

| Pattern | Intent | When |
|---------|--------|------|
| **Adapter** | Convert interface to one clients expect. | Integrate third-party with mismatched API. |
| **Bridge** | Decouple abstraction from implementation. | Multiple implementations × multiple abstractions. |
| **Composite** | Tree of objects; treat uniformly. | Hierarchies (UI tree, org chart). |
| **Decorator** | Add behavior dynamically. | Middleware, HOCs, React HOCs. |
| **Facade** | Simple interface to complex subsystem. | Hide library complexity. |
| **Flyweight** | Share state to support many fine-grained objects. | Game particles, character glyphs. |
| **Proxy** | Surrogate controlling access. | Lazy loading, protection, caching, remote. |

### Behavioral patterns
How objects communicate.

| Pattern | Intent | When |
|---------|--------|------|
| **Chain of Responsibility** | Pass request along handlers. | Middleware; event bubbling. |
| **Command** | Encapsulate request as object. | Undo/redo; queueing. |
| **Iterator** | Sequential access without exposing internals. | Custom collections; `for...of`. |
| **Mediator** | Central coordinator for many objects. | UI components; chat rooms. |
| **Memento** | Capture + restore object state. | Undo; snapshots. |
| **Observer** | Notify dependents of state changes. | Event systems; reactive streams. |
| **State** | Behavior changes with internal state. | State machines; connection states. |
| **Strategy** | Family of interchangeable algorithms. | Sorting strategies; pricing rules. |
| **Template Method** | Skeleton with overridable steps. | Frameworks; pipelines. |
| **Visitor** | Add operations to object structure without modifying. | Compilers; ASTs; serializers. |

### Modern / beyond GoF

| Pattern | Intent | Notes |
|---------|--------|-------|
| **Repository** | Abstract data access. | DDD / Clean Architecture. |
| **Unit of Work** | Track object changes for batch commit. | DDD; ORM coordination. |
| **Specification** | Composable business rules. | DDD; query objects. |
| **Null Object** | Default no-op behavior. | Avoid null checks. |
| **Circuit Breaker** | Fail fast on downstream failure. | Resilience. |
| **Bulkhead** | Isolate resources per tenant. | Resilience. |
| **Sidecar** | Co-located helper process. | Service mesh (Envoy); Dapr. |
| **Saga** | Distributed transaction via local txs. | Microservices. |
| **Outbox** | Reliable message publishing. | Event-driven. |
| **CQRS** | Separate read + write models. | Architecture. |
| **Event Sourcing** | State = sequence of events. | Architecture. |

### SOLID principles (object-oriented design)
| Letter | Principle | Meaning |
|--------|-----------|---------|
| **S** | Single Responsibility | One class, one reason to change. |
| **O** | Open/Closed | Open to extension, closed to modification. |
| **L** | Liskov Substitution | Subtypes must be substitutable for base types. |
| **I** | Interface Segregation | Many specific interfaces > one general. |
| **D** | Dependency Inversion | Depend on abstractions, not concretions. |

### GRASP (General Responsibility Assignment Software Patterns)
- Information Expert, Creator, Controller, Low Coupling, High Cohesion, Polymorphism, Pure Fabrication, Indirection, Protected Variations.

## When To Use It

- **You see the same problem over and over** — patterns give names + solutions.
- **You want to communicate with teammates** — "let's use a Strategy here" is precise.
- **You're designing libraries / frameworks** — patterns are how you structure the API.
- **You're reviewing code** — recognizing patterns helps spot missing abstractions.
- **You're interviewing** — patterns are classic interview topics (though modern interviews weight them less).

## When NOT To Use It

- **The pattern is overkill** — a simple if/else beats a Strategy.
- **You're pattern-matching without understanding** — cargo-culting patterns makes code worse.
- **You don't have the problem yet** — premature abstraction.
- **Modern alternatives are better** — e.g. reactive streams may replace Observer + Iterator.
- **You're writing throwaway code** — patterns add structure overhead.

## Why It Matters in 2026

Three forces:

1. **Patterns are still the lingua franca of senior engineering conversations.** "Let's use a Repository + Unit of Work" still means something specific.
2. **Modern patterns matter more than GoF.** Saga, Outbox, CQRS, Circuit Breaker, Bulkhead, Sidecar are what production microservices use. GoF is the foundation; modern patterns are the practice.
3. **SOLID is still the baseline for OO design.** Even with functional / reactive paradigms, the principles (single responsibility, dependency inversion) remain valid.

Practitioner playbook in 2026:
1. **Learn the GoF 23** — even if you don't use all, recognize them.
2. **Add modern patterns**: Saga, Outbox, CQRS, Event Sourcing, Circuit Breaker, Bulkhead, Sidecar.
3. **SOLID** as your default OO design checklist.
4. **Recognize when NOT to apply** — patterns are tools, not laws.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | 30+ years old (1994); the canon is settled. |
| Community | 95 | Massive; patterns are taught in every CS program. |
| Learning curve | 70 | Concepts are learnable; applying them well takes years. |
| Performance | N/A | Design knowledge. |
| Cost | N/A | Knowledge. |
| DX | 80 | Patterns improve code readability when used right. |
| Production readiness | 100 | Every production codebase uses these. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **No patterns** | Throwaway code. | Anything in production. |
| **Functional patterns (Functor, Monad)** | Pure functional code. | OOP code. |
| **Reactive patterns (Observable, Subject)** | Event streams. | Sync CRUD. |
| **Architectural patterns (see software-architecture.md)** | System-level design. | Class-level. |

## Sources

- [Refactoring Guru — Design Patterns](https://refactoring.guru/design-patterns) — 2026
- [Wikipedia — Design Patterns](https://en.wikipedia.org/wiki/Design_Patterns) — 2026
- [OODesign.com](https://www.oodesign.com/) — 2026
- [SourceMaking — Design Patterns](https://sourcemaking.com/design_patterns) — 2026
- [Refactoring Guru Patterns — PHP Examples](https://github.com/RefactoringGuru/design-patterns-php) — 2026
- [Martin Fowler — EAA Catalog](https://www.martinfowler.com/eaaCatalog/) — 2002+
- [Martin Fowler](https://martinfowler.com/) — 2026
- [Wikipedia — GRASP](https://en.wikipedia.org/wiki/GRASP_(object-oriented_design)) — 2026
- [Wikipedia — SOLID](https://en.wikipedia.org/wiki/SOLID) — 2026
- [ThoughtWorks Technology Radar](https://www.thoughtworks.com/radar) — 2026
- [Refactoring Guru — Behavioral Patterns](https://refactoring.guru/design-patterns/behavioral-patterns) — 2026
- [Refactoring Guru — Structural Patterns](https://refactoring.guru/design-patterns/structural-patterns) — 2026
- [Refactoring Guru — Creational Patterns](https://refactoring.guru/design-patterns/creational-patterns) — 2026