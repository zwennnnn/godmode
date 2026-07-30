---
name: TypeScript
category: frontend-backend
status: researched
last-updated: 2026-07-30
sources:
  - https://www.typescriptlang.org/docs/
  - https://devblogs.microsoft.com/typescript/typescript-5-7/
  - https://github.com/microsoft/TypeScript
  - https://survey.stackoverflow.co/2024/technology/
  - https://stateofjs.com/
  - https://www.typescriptlang.org/docs/handbook/intro.html
  - https://www.typescriptlang.org/docs/handbook/2/type-checking.html
  - https://www.typescriptlang.org/docs/handbook/tsconfig-json.html
  - https://www.typescriptlang.org/play/
  - https://basarat.gitbook.io/typescript/
  - https://github.com/DefinitelyTyped/DefinitelyTyped
tags: [typescript, javascript, types, compiler, dx]
---

# TypeScript

## One-liner

A statically-typed superset of JavaScript that compiles to plain JS — the default language of professional web development in 2026.

## What It Is

TypeScript is Microsoft's open-source language that adds **optional static typing**, **structural interfaces**, **generics**, **enums**, **decorators**, and a powerful type system on top of JavaScript. It compiles (`tsc`) to plain JavaScript that runs anywhere JS runs (browsers, Node, Bun, Deno, edge runtimes). The type system is **structural** (duck-typed) and **gradual** — you can adopt it incrementally file by file.

The 2026 baseline (`TypeScript 5.7+`) ships:

- **Faster compiler** — `tsc` rewritten in Go for the native port (`tsgo`) shipping in beta; 10× faster type-check on large codebases.
- **Strict mode by default** in new templates (`strict: true` is the new norm).
- **`isolatedDeclarations`** for fast, parallel declaration emit.
- **Improved inference** for `const` type parameters, narrowed return types.
- **Native ESM support** mature; Node.js ESM interop is no longer painful.
- **JSDoc-type-only adoption path** for `.js` files — you can get TypeScript-style types without writing `.ts`.
- **Biome / oxc** as drop-in replacements for `tsc` in many workflows (10–100× faster lint/format).

TypeScript adoption (per [Stack Overflow Developer Survey 2024](https://survey.stackoverflow.co/2024/technology/) and [State of JS](https://stateofjs.com/)):
- TypeScript has been the **#2 most-used language** in Stack Overflow surveys since 2022.
- ~70–80% of professional JS developers use TypeScript for new projects (State of JS 2024).
- The Node.js ecosystem ([npm](https://www.npmjs.com/)) has >85% of new packages shipping with TypeScript types.
- React, Vue, Angular, Next.js, NestJS, all ship first-class TypeScript support.

## When To Use It

- **Any non-trivial JS/TS project** (frontend, backend, full-stack, scripts, libs). The cost of `tsc --noEmit` in CI is trivial; the runtime cost is zero.
- **Any code shared by 2+ people.** Types are documentation + compile-time checks.
- **Any public API** (REST, GraphQL, library). Types are a contract.
- **Any team that has ever debugged "undefined is not a function".** Strict null checks alone prevent hundreds of bug classes.
- **Greenfield React, Next.js, Node.js, Bun, Deno, etc.** — all defaults are TS now.

## When NOT To Use It

- **Throwaway scripts under ~50 lines.** The setup tax isn't worth it.
- **Prototypes where you don't yet know the shape.** Use plain JS or JSDoc-typed JS to defer the type design.
- **Tight performance-critical hot paths** in Node.js — `tsc` adds no runtime cost, but type-heavy libraries have a tiny startup cost. Usually negligible.
- **You're shipping pure WebAssembly.** TS doesn't help there.
- **You're using a JS framework that doesn't yet support TS well.** Increasingly rare in 2026.
- **Your team refuses to learn types.** The friction of forcing TS on unwilling engineers > the benefit. (Try JSDoc instead.)

## Why It Matters in 2026

Three forces keep TypeScript dominant:

1. **The AI-coding era makes types more valuable, not less.** Cursor / Copilot / Claude Code generate JS-shaped code; without types, errors compound across generated chunks. With strict TS, the model gets instant feedback. The dev experience with AI is *measurably better* in TS codebases.
2. **Type ecosystem maturity.** [DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped) has >80,000 typed packages; nearly every npm package ships its own types. The "I can't find types for X" excuse is dead.
3. **Native port + faster toolchain.** `tsc` got slow; the native Go port (`tsgo`) + Biome + oxc reset the bar. In 2026, TS is as fast to type-check as it ever was, even on million-line monorepos.

Practitioner defaults in 2026:
- `"strict": true` + `"noUncheckedIndexedAccess": true` + `"exactOptionalPropertyTypes": true` for new projects.
- `verbatimModuleSyntax` for clean ESM/CJS interop.
- ESLint + `@typescript-eslint` (or Biome as a drop-in).
- Vitest for tests (TS-first).
- Use `tsc --noEmit` in CI as a type-check gate.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 95 | 12+ years old (Microsoft, 2012); v5.x in 2026; the default for serious JS development. |
| Community | 95 | #2 most-used language in Stack Overflow 2024; >80K typed packages on DefinitelyTyped; native toolchain support in every major editor. |
| Learning curve | 65 | Easy to start (add types to vars); mastery (conditional types, mapped types, infer, satisfies) takes months. |
| Performance | 85 | `tsc` historically slow on large projects (mitigated by `tsgo`/Biome/oxc in 2026); runtime cost = 0. |
| Cost | 95 | Free; open source; runs on any dev machine. |
| DX (developer experience) | 95 | Best-in-class autocomplete in VS Code / Cursor; instant feedback on save; refactor tools are unmatched. |
| Production readiness | 95 | Used by Microsoft, Google, Stripe, Airbnb, Slack, Shopify, every serious startup. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Plain JavaScript + JSDoc types** | You want TS-like safety without the build step; you ship ES modules directly. | You need rich type system (generics, conditional types); tooling is less integrated. |
| **Flow** | You're on the Facebook/Instagram stack (mostly irrelevant in 2026). | Almost everything — Flow lost the ecosystem battle. |
| **Zod / Valibot for runtime validation** | You need to validate data at the boundary (API, user input). Combine with TS; they don't replace it. | You want compile-time type checking of internal code. |
| **ReScript / PureScript / Elm** | You want a stronger functional-typed language that compiles to JS. | Ecosystem is small; hiring pool is tiny; learning curve is steeper. |
| **Rust → wasm** | You need type safety + performance in the browser. | You're building UI components — overkill. |
| **Python with type hints** | You're in a Python shop. | Your stack is web/JS; the ecosystem doesn't overlap. |

## Sources

- [TypeScript Official Docs](https://www.typescriptlang.org/docs/) — 2026
- [Microsoft DevBlog — TypeScript 5.7](https://devblogs.microsoft.com/typescript/typescript-5-7/) — 2025+
- [TypeScript GitHub (microsoft/TypeScript)](https://github.com/microsoft/TypeScript) — 2026
- [Stack Overflow Developer Survey 2024](https://survey.stackoverflow.co/2024/technology/) — 2024
- [State of JS](https://stateofjs.com/) — 2024+
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) — 2026
- [TypeScript Type Checking Handbook](https://www.typescriptlang.org/docs/handbook/2/type-checking.html) — 2026
- [tsconfig.json Reference](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html) — 2026
- [TypeScript Playground](https://www.typescriptlang.org/play/) — 2026
- [Basarat's TypeScript Deep Dive (GitBook)](https://basarat.gitbook.io/typescript/) — 2026
- [DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped) — 2026