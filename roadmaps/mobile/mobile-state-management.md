---
name: Mobile State Management
category: mobile
status: researched
last-updated: 2026-07-30
sources:
  - https://zustand.docs.pmnd.rs/
  - https://github.com/pmndrs/zustand
  - https://redux-toolkit.js.org/
  - https://github.com/reduxjs/redux-toolkit
  - https://jotai.org/
  - https://github.com/pmndrs/jotai
  - https://tanstack.com/query/latest
  - https://github.com/TanStack/query
  - https://react.dev/reference/react/useState
  - https://docs.expo.dev/router/introduction/
  - https://docs.swmansion.com/react-native-async-storage/
  - https://github.com/mrousavy/react-native-mmkv
  - https://op-sqlite.org/
  - https://expo.dev/versions/latest/sdk/sqlite
  - https://www.notion.so/blog/how-we-sped-up-notion-mobile-by-50-with-react-native
tags: [state-management, mobile, react-native, zustand, redux, jotai, mmkv, sqlite, offline]
---

# Mobile State Management

## One-liner

How React Native / Flutter / native apps organize in-memory state, persistent storage, and server sync — with mobile-specific concerns (offline, persistence, performance).

## What It Is

Mobile state management has more layers than web because of **persistence** and **offline-first** requirements:

| Layer | Question | Mobile-specific concerns |
|-------|----------|--------------------------|
| **In-memory state** | Current screen state? Form values? | Ephemeral; lost on app close. |
| **Local persistence** | What stays across app restarts? | Settings, drafts, cached data, auth tokens. |
| **Server state cache** | API data, shared with backend. | Stale-while-revalidate; offline fallback. |
| **Offline queue** | Pending mutations to sync later. | Critical for mobile (network drops). |
| **Optimistic UI** | Show change instantly, roll back on error. | Mobile users expect instant feedback. |

### React Native state (JS / TS)

Same options as web (Zustand, Redux Toolkit, Jotai) — but with mobile-tuned storage:

| Tool | Notes |
|------|-------|
| **[Zustand](https://zustand.docs.pmnd.rs/)** | Same API as web; pairs with MMKV for persistence. |
| **[Redux Toolkit](https://redux-toolkit.js.org/)** | RTK + RTK Query; great for large apps + offline-first. |
| **[Jotai](https://jotai.org/)** | Atomic; great for derived state. |
| **[TanStack Query](https://tanstack.com/query/latest)** | Server cache + offline; pair with MMKV / AsyncStorage persistence. |

### Mobile persistence (React Native)

| Storage | Use case |
|---------|----------|
| **AsyncStorage** (deprecated for performance) | Key-value; deprecated for new code. |
| **[MMKV](https://github.com/mrousavy/react-native-mmkv)** | 10× faster than AsyncStorage; encrypted option; default in 2026. |
| **[op-sqlite](https://op-sqlite.org/) / [Expo SQLite](https://expo.dev/versions/latest/sdk/sqlite)** | SQLite for relational data; huge data sets. |
| **WatermelonDB** | Reactive database for offline-first. |
| **Realm / MongoDB Realm** | Object database; sync to Atlas. |
| **SecureStore (Expo)** | Encrypted key-value (Keychain on iOS, Keystore on Android). |

### Flutter state (Dart)

| Tool | Notes |
|------|-------|
| **`setState` + `InheritedWidget`** | Built-in. |
| **[Riverpod 2.x](https://riverpod.dev/)** | The default for new Flutter projects in 2026. |
| **[Bloc](https://bloclibrary.dev/)** | Event-driven; loved by enterprise. |
| **Provider** | Older; Riverpod is the evolution. |
| **GetX** | All-in-one (state + nav + DI); popular but controversial. |

Flutter persistence:
- **`shared_preferences`** — key-value.
- **`sqflite` / `drift`** — SQLite.
- **`hive`** / **`isar`** — fast NoSQL.
- **`flutter_secure_storage`** — Keychain / Keystore.

### Native state (Swift / Kotlin)

- **Swift**: `@State` / `@Observable` (SwiftUI); `UserDefaults`; Core Data; SwiftData (2023+); Combine.
- **Kotlin**: `StateFlow` / `MutableState` (Compose); DataStore; Room; Coroutines + Flow.

## When To Use It

### React Native
- **Default**: Zustand for client state + TanStack Query for server state + MMKV for persistence.
- **Large app**: Redux Toolkit + RTK Query + MMKV.
- **Atomic / derived**: Jotai.
- **Offline-first**: WatermelonDB or PowerSync + Zustand/Jotai for UI state.

### Flutter
- **Default**: Riverpod 2.x + Drift (SQLite) + `shared_preferences` for small settings.
- **Enterprise**: Bloc + Drift + `flutter_secure_storage`.

### Native
- **iOS**: SwiftUI `@State` / `@Observable` + SwiftData + `@AppStorage`.
- **Android**: Compose `StateFlow` + DataStore + Room.

## When NOT To Use It

### AsyncStorage (deprecated for performance)
- **New code in 2026.** MMKV is the replacement.

### GetX (Flutter)
- **Most projects.** Couples state + nav + DI; hard to test; community has moved to Riverpod / Bloc.

### Realm
- **Small projects.** Heavy; sync requires Atlas; overkill for most.

### Redux Toolkit (RN)
- **Tiny apps.** Use Zustand.

### Provider (Flutter)
- **New projects.** Riverpod is the modern evolution.

## Why It Matters in 2026

Three forces:

1. **MMKV replaced AsyncStorage** as the default React Native persistence. 10× faster; encrypted option; built-in TypeScript types.
2. **Offline-first went mainstream.** Apps are expected to work on planes, subways, low connectivity. WatermelonDB, PowerSync, RxDB, and Drift made reactive sync real.
3. **SQLite replaced NoSQL** for most mobile local storage. op-sqlite (JSI-powered) is faster than any NoSQL for most workloads; SQLite is just better-engineered.

Practitioner defaults in 2026:
- **React Native**: Zustand + TanStack Query + MMKV.
- **Flutter**: Riverpod 2.x + Drift.
- **iOS**: SwiftUI + SwiftData.
- **Android**: Compose + DataStore + Room.
- **Offline-first RN**: WatermelonDB or PowerSync + Zustand.

## Scoring Matrix (0–100)

### React Native stack (Zustand + TanStack Query + MMKV)
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 85 | All three are battle-tested; MMKV is the 2024+ default. |
| Community | 95 | Zustand and TanStack Query have huge communities; MMKV growing fast. |
| Learning curve | 80 | Familiar patterns from web; MMKV API is dead simple. |
| Performance | 90 | MMKV is fastest key-value; TanStack Query caches are fast; SQLite via op-sqlite is excellent. |
| Cost | 95 | All free OSS. |
| DX | 90 | Excellent; minor friction integrating the three. |
| Production readiness | 95 | Used at scale in many apps. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **MMKV** | Any RN persistence in 2026. | Tiny scripts. |
| **op-sqlite** | Relational data; large datasets; offline-first. | Simple key-value (use MMKV). |
| **WatermelonDB** | Offline-first sync; reactive. | Non-sync use cases. |
| **Realm** | MongoDB sync; complex schemas. | Most apps — overkill. |
| **AsyncStorage** | Legacy code only. | New code — MMKV. |
| **Zustand vs Redux Toolkit** | Zustand = simple; Redux Toolkit = large teams + strict actions. | Pick by team size. |

## Sources

- [Zustand Docs](https://zustand.docs.pmnd.rs/) — 2026
- [Zustand GitHub (pmndrs/zustand)](https://github.com/pmndrs/zustand) — 2026
- [Redux Toolkit Docs](https://redux-toolkit.js.org/) — 2026
- [Redux Toolkit GitHub](https://github.com/reduxjs/redux-toolkit) — 2026
- [Jotai](https://jotai.org/) — 2026
- [Jotai GitHub](https://github.com/pmndrs/jotai) — 2026
- [TanStack Query](https://tanstack.com/query/latest) — 2026
- [TanStack Query GitHub](https://github.com/TanStack/query) — 2026
- [React useState Reference](https://react.dev/reference/react/useState) — 2026
- [Expo Router](https://docs.expo.dev/router/introduction/) — 2026
- [Async Storage (swmansion)](https://docs.swmansion.com/react-native-async-storage/) — 2026
- [React Native MMKV](https://github.com/mrousavy/react-native-mmkv) — 2026
- [op-sqlite](https://op-sqlite.org/) — 2026
- [Expo SQLite](https://expo.dev/versions/latest/sdk/sqlite) — 2026
- [Notion — How We Sped Up Notion Mobile by 50% with React Native](https://www.notion.so/blog/how-we-sped-up-notion-mobile-by-50-with-react-native) — 2025