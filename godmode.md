# Godmode — Session Memory

> **Auto-managed by the model.** Updated after every major decision, phase advance, or roadmap completion.
> Source of truth for cross-session continuity. If this file is wrong, the next session will be wrong.

---

## Current User Profile

- **technical_level**: unknown *(set on first interaction — see CLAUDE.md Step 2)*
- **preferred_language**: tr *(user writes in Turkish; replies may match, but `.md` files stay English per rules.md)*
- **primary_domain**: undecided

---

## Active Roadmap

`roadmaps/ai-ml-llm/` — first category to fill (planned 12 technologies)

---

## Progress Tracker

### Phase 1 — Skeleton *(COMPLETE 2026-07-30)*
- [x] Directory structure
- [x] `CLAUDE.md`
- [x] `README.md`
- [x] `rules.md`
- [x] `godmode.md` (this file, initial state)
- [x] `decision-engine.md`
- [x] `scoring/weights.json`
- [x] `scoring/rubric.md`
- [x] `templates/tech-md.md`
- [x] `templates/roadmap-index.md`
- [x] `templates/decision-card.md`
- [x] `templates/session-summary.md`
- [x] `scripts/scrape-roadmap.py`
- [x] `scripts/research-batch.md`
- [x] `scripts/validate-md.py`
- [x] `roadmaps/ai-ml-llm/README.md` (placeholder, will be filled in Phase 2)
- [x] `roadmaps/frontend-backend/.gitkeep`
- [x] `roadmaps/devops-cloud/.gitkeep`
- [x] `roadmaps/mobile/.gitkeep`

### Phase 2 — `roadmaps/ai-ml-llm/` *(COMPLETE 2026-07-30)*
- [x] `prompt-engineering.md`
- [x] `rag-architectures.md`
- [x] `vector-databases.md`
- [x] `embeddings.md`
- [x] `ai-frameworks.md`
- [x] `agent-design.md`
- [x] `fine-tuning-llms.md`
- [x] `model-evaluation.md`
- [x] `llm-ops.md`
- [x] `multimodal-models.md`
- [x] `speech-and-vision.md`
- [x] `ai-safety-alignment.md`
- [x] `roadmaps/ai-ml-llm/README.md` — quick decision guide written (MVP / production / research paths)

### Phase 3 — `roadmaps/frontend-backend/` *(COMPLETE 2026-07-30)*
- [x] `typescript.md`
- [x] `react.md`
- [x] `nextjs.md`
- [x] `nodejs-bun.md`
- [x] `api-design.md`
- [x] `postgresql.md`
- [x] `authentication.md`
- [x] `state-management.md`
- [x] `css-architecture.md`
- [x] `build-tooling.md`
- [x] `roadmaps/frontend-backend/README.md` — quick decision guide written (MVP / custom backend / enterprise paths)

### Phase 4 — `roadmaps/devops-cloud/` *(COMPLETE 2026-07-30)*
- [x] `docker-containers.md`
- [x] `kubernetes.md`
- [x] `infrastructure-as-code.md`
- [x] `cloud-providers.md`
- [x] `ci-cd.md`
- [x] `observability.md`
- [x] `serverless.md`
- [x] `secrets-management.md`
- [x] `cdn-edge.md`
- [x] `logging-incident.md`
- [x] `roadmaps/devops-cloud/README.md` — quick decision guide written (MVP / production / scale paths)

### Phase 5 — `roadmaps/mobile/` *(COMPLETE 2026-07-30)*
- [x] `react-native.md`
- [x] `expo.md`
- [x] `flutter.md`
- [x] `swift-ios.md`
- [x] `kotlin-android.md`
- [x] `mobile-state-management.md`
- [x] `offline-sync.md`
- [x] `push-notifications.md`
- [x] `mobile-ci-cd.md`
- [x] `mobile-analytics.md`
- [x] `roadmaps/mobile/README.md` — quick decision guide written (JS team / Flutter / iOS / Android / KMP paths)

---

## 🏆 ALL PHASES COMPLETE — 2026-07-30

All 4 roadmaps researched, written, and validated. 42 tech files total. Godmode is operational.

---

## Last Session

- **Date**: 2026-07-30
- **Worked on**:
  - **Phases 1–18** complete (17 roadmaps, 117 tech MDs + skills.md).
  - **Phase 19** complete (TOOLING): built the actual godmode runtime:
    - `scripts/score.py` — weighted-scoring engine (decision-engine.md implemented); parses tech MDs + applies stage weights from `scoring/weights.json`; tested across 3 roadmaps × 3 stages with sensible results (Build Tooling 86.2, Express 92.2, Kotlin 93.8, etc.).
    - `scripts/research.py` — scaffolder for new tech MD files; supports `--interactive` mode + CLI flags.
    - `SKILL.md` (root) — skills.sh / Claude Code / Cursor skill manifest with full boot sequence + scoring usage + install instructions.
  - Validated score.py works: `score.py --roadmap frontend-backend --stage mvp-speed --top 3` returns valid weighted scores.
- **Decisions made**:
  - **Phase 19 scope**: User asked to build actual tools (score.py + research.py) and publish to GitHub as a godmode skill.
  - **score.py** implements decision-engine.md's weighted formula `Σ weight[stage][criterion] × tech.score[criterion]`.
  - **research.py** is a scaffolder — the AI agent (or human) does the WebSearch, fills the prompts, and the script generates the validated MD file.
  - **SKILL.md** makes godmode installable as a Claude Code / Cursor / skills.sh agent skill.
- **Next**: Push to GitHub as a public repo; finalize v1.0 release.

---

## 🏆 STATUS — 2026-07-30

**17 roadmaps + 117 tech MDs + scoring engine + research scaffolder + SKILL.md.**

**Godmode is now functional.** The knowledge base + scoring algorithm + installable skill package are all in place.

**Tools available:**
- `python scripts/score.py` — weighted-scoring engine
- `python scripts/research.py` — tech MD scaffolder
- `python scripts/validate-md.py` — schema validator
- `python scripts/scrape-roadmap.py` — roadmap.sh scraper

**Special files (root level):**
- `SKILL.md` — Agent Skills manifest (skills.sh / Claude Code / Cursor)
- `skills.md` — skills.sh + Claude Agent Skills guide

**Validation**: All 117 tech files + 17 roadmap indexes pass `scripts/validate-md.py --all` cleanly. 134 total files validated.

---

## Recent Decisions

- 2026-07-30 — **🏆 TOOLING SHIPPED**: `scripts/score.py` (weighted-scoring engine — working), `scripts/research.py` (scaffolder), `SKILL.md` (Agent Skills manifest). godmode is now functional + installable.
- 2026-07-30 — **Phase 18 (People + Process roadmap) COMPLETE**: 6 tech MDs researched, written, and validated.
- 2026-07-30 — **Phase 17 (QA + Testing roadmap) COMPLETE**: 5 tech MDs researched, written, and validated.
- 2026-07-30 — **Phase 16 (Infrastructure Tools roadmap) COMPLETE**: 6 tech MDs researched, written, and validated.
- 2026-07-30 — **Phase 15 (Modern AI Meta roadmap) COMPLETE**: 5 tech MDs researched, written, and validated.
- 2026-07-30 — **Phase 14 (Frontend Frameworks roadmap) COMPLETE**: 6 tech MDs researched, written, and validated.
- 2026-07-30 — **Phase 13 (Backend Frameworks roadmap) COMPLETE**: 8 tech MDs researched, written, and validated.
- 2026-07-30 — **`skills.md`** at root — skills.sh + Claude Agent Skills + godmode-as-skill.
- 2026-07-30 — **Phase 12 (Cyber Security roadmap) COMPLETE**: 6 tech MDs researched, written, and validated.
- 2026-07-30 — **Phase 11 (Game Development roadmap) COMPLETE**: 6 tech MDs researched, written, and validated.
- 2026-07-30 — **Phase 10 (Design + UX roadmap) COMPLETE**: 6 tech MDs researched, written, and validated.
- 2026-07-30 — **Phase 9 (Databases roadmap) COMPLETE**: 6 tech MDs researched, written, and validated.
- 2026-07-30 — **Phase 8 (Data Engineering, Analytics & MLOps roadmap) COMPLETE**: 4 tech MDs researched, written, and validated.
- 2026-07-30 — **Phase 7 (System Design roadmap) COMPLETE**: 5 tech MDs researched, written, and validated.
- 2026-07-30 — **Phase 6 (Programming Languages roadmap) COMPLETE**: 6 tech MDs researched, written, and validated.
- 2026-07-30 — **Phase 5 (Mobile roadmap) COMPLETE**: 10 tech MDs researched, written, and validated.
- 2026-07-30 — **Phase 4 (DevOps + Cloud roadmap) COMPLETE**: 10 tech MDs researched, written, and validated.
- 2026-07-30 — **Phase 3 (Frontend + Backend roadmap) COMPLETE**: 10 tech MDs researched, written, and validated.
- 2026-07-30 — **Phase 2 (AI/ML roadmap) COMPLETE**: 12 tech MDs researched, written, and validated. All scoring matrices filled, all sources dated.
- 2026-07-30 — **Phase 1 (Skeleton) COMPLETE**: 17 files written. Decision engine, scoring rubric, templates, scripts, and roadmap placeholders are all in place.
- 2026-07-30 — **Architecture finalized**: weighted-scoring decision engine, English `.md`, auto-managed session memory. See [`decision-engine.md`](decision-engine.md).
- 2026-07-30 — **User-profile question protocol established**: ask once on first interaction, persist to this file.

---

## Known Gaps (to address later)

- `scripts/scrape-roadmap.py` depends on roadmap.sh's HTML/JSON structure; if their layout has changed since writing, the scraper will need a small patch. Fallback: hand-create stubs from the visual roadmap and skip the scraper.
- Scoring rubric weights are rough first-pass values; will be calibrated after Phase 2 produces real data.
- No example decision-card outputs yet — first one comes after Phase 2 first decision.