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
  - **Phase 19** complete (TOOLING + PUBLISH):
    - `scripts/score.py` — weighted-scoring engine (working, tested).
    - `scripts/research.py` — scaffolder for new tech MDs.
    - `SKILL.md` (root) — Agent Skills manifest.
    - **🟢 Published to GitHub**: `https://github.com/zwennnnn/godmode`.
  - **Phase 20** complete (SKILLS.SH INTEGRATION):
    - `npx skills use zwennnnn/godmode@godmode` **works** — SKILL.md fetched + parsed.
    - SKILL.md enriched with: keywords/author/version/license/homepage.
    - README.md has install badge + primary `npx skills add` path.
    - Subagent research: no public submit form; back-channel issue may be needed.
  - **Phase 21** complete (CONTRIBUTOR ONBOARDING):
    - Created `.github/CONTRIBUTING.md` — full contributor guide.
    - Created `CONTRIBUTORS.md` — credits + first-external-contributor table.
    - Added **`@birkansiser`** as the first external contributor.
    - README.md has a Contributors section + badge.
- **Decisions made**:
  - **Phase 21 scope**: User asked to add `birkansiser` as a contributor — created proper contribution infrastructure so future contributors have a clear path.
  - All files validated 0 errors.
- **Next**: User pushes Phase 20 + Phase 21 commits to GitHub. Optionally opens the back-channel issue on `vercel-labs/skills` for indexing.

---

## 🏆 STATUS — 2026-07-30

# 🟢 GODMODE v1.0.1 — LIVE + CONTRIBUTOR-READY

**GitHub:** [https://github.com/zwennnnn/godmode](https://github.com/zwennnnn/godmode)

| Component | Status |
|-----------|--------|
| Knowledge base | ✅ 17 roadmaps / 117 tech MDs |
| Scoring engine | ✅ `scripts/score.py` (working) |
| Research scaffolder | ✅ `scripts/research.py` |
| Schema validator | ✅ `scripts/validate-md.py` (0 errors) |
| Roadmaps scraper | ✅ `scripts/scrape-roadmap.py` |
| Agent Skills manifest | ✅ `SKILL.md` (root, enriched) |
| skills.sh guide | ✅ `skills.md` (root) |
| **Install test** | ✅ `npx skills use zwennnnn/godmode@godmode` works |
| **Contributor system** | ✅ `.github/CONTRIBUTING.md` + `CONTRIBUTORS.md` |
| **First external contributor** | ✅ `@birkansiser` |
| **Discoverability** | ⏳ Awaiting `npx skills find` indexing |
| **GitHub repo** | ✅ `zwennnnn/godmode` (public) |

**Install as a skill (works today):**
```bash
npx skills add zwennnnn/godmode
```

**Contribute:**
- See [`.github/CONTRIBUTING.md`](.github/CONTRIBUTING.md) for guidelines.
- See [CONTRIBUTORS.md](CONTRIBUTORS.md) for the contributor list.

---

### Phase 21 (CONTRIBUTOR ONBOARDING) *(COMPLETE 2026-07-30)*

- [x] Created `.github/CONTRIBUTING.md` — full contributor guide (ways to contribute, quick start, add tech, new category, reporting bugs, code of conduct)
- [x] Created `CONTRIBUTORS.md` — credits + first-external-contributor table
- [x] Added `@birkansiser` as first external contributor
- [x] README.md — Contributors section + "Contributors welcome" badge
- [ ] **Pending user action**: commit + push via GitHub Desktop

---

### Phase 20 (SKILLS.SH INTEGRATION) *(COMPLETE 2026-07-30)*

- [x] Audited `SKILL.md` per Vercel Agent Skills spec — required fields present
- [x] Added keywords/author/version/license/homepage/install to SKILL.md frontmatter
- [x] Added skills.sh install badge + `npx skills add` instructions to README
- [x] Tested `npx skills use zwennnnn/godmode@godmode` → SKILL.md fetched + parsed correctly ✅
- [x] Tested `npx skills find godmode --owner zwennnnn` → "No skills found" (known indexing gap, issue #705)
- [x] Subagent research: no public submit form; install telemetry + Vercel Labs curation drive indexing
- [ ] **Pending user action**: file back-channel issue on `vercel-labs/skills` requesting indexing for `zwennnnn/godmode` (only known escalation path)
- [ ] **Pending user action**: commit + push updated SKILL.md + README

---

### Phase 19 (TOOLING + PUBLISH) *(COMPLETE 2026-07-30)*

- [x] `scripts/score.py` — weighted-scoring engine (working)
- [x] `scripts/research.py` — scaffolder for new tech MDs
- [x] `SKILL.md` (root) — Agent Skills manifest
- [x] `README.md` (root) — comprehensive
- [x] `.gitignore` — added
- [x] `git init` + initial commit (158 files, 20,197 lines)
- [x] **Published to GitHub**: `https://github.com/zwennnnn/godmode` (via GitHub Desktop)
- [x] Verified: `main` tracking `origin/main`; commit `b3b5e85` pushed

---

## 🟢 GODMODE v1.0 — LIVE ON GITHUB

- **URL**: https://github.com/zwennnnn/godmode
- **Public repo**, MIT license
- **158 files, 20,197 insertions**
- **17 roadmaps, 117 tech MDs, working scoring engine**

---

## Recent Decisions

- 2026-07-30 — **🏆 CONTRIBUTOR ONBOARDING COMPLETE**: `.github/CONTRIBUTING.md` + `CONTRIBUTORS.md` created. `@birkansiser` added as first external contributor. README has Contributors section + badge.
- 2026-07-30 — **🏆 SKILLS.SH INTEGRATION COMPLETE**: SKILL.md enriched with keywords/author/version; README has install badge; `npx skills use zwennnnn/godmode` works. Awaiting back-channel indexing issue on `vercel-labs/skills` (issue #705 known gap).
- 2026-07-30 — **🏆 GODMODE v1.0 PUBLISHED to GitHub**: `https://github.com/zwennnnn/godmode`. 158 files / 20,197 lines. Tools + skill package all working.
- 2026-07-30 — **TOOLING SHIPPED**: `scripts/score.py` (weighted-scoring engine — working), `scripts/research.py` (scaffolder), `SKILL.md` (Agent Skills manifest). godmode is now functional + installable.
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