# Decision Engine — Weighted Scoring

> The root decision mechanism for Godmode. Every technology recommendation must flow through this.

---

## When This File Is Read

Every time a user describes a project (or asks "which X should I use?"), the model:

1. Reads this file to refresh the flow.
2. Reads [`scoring/weights.json`](scoring/weights.json) and [`scoring/rubric.md`](scoring/rubric.md).
3. Reads the relevant `roadmaps/<category>/README.md` to get the candidate list.
4. For each candidate, reads its `roadmaps/<category>/<tech>.md` to get the scoring matrix.
5. Applies the formula below.
6. Outputs a decision card from [`templates/decision-card.md`](templates/decision-card.md).

---

## The Formula

```
score(tech, stage) = Σ criterion ∈ C   weight[stage][criterion] × tech.score[criterion]
```

Where:

- `C` is the set of criteria defined in [`scoring/rubric.md`](scoring/rubric.md).
- `weight[stage][criterion]` is loaded from [`scoring/weights.json`](scoring/weights.json) — they sum to 1.0 for each stage.
- `tech.score[criterion]` is read from the tech's `.md` file scoring matrix.

**Result interpretation**:

| Score | Verdict |
|-------|---------|
| 80–100 | Strong fit — top recommendation. |
| 65–79 | Solid fit — worth presenting as a top-3 option. |
| 50–64 | Marginal — present only if user constraints demand it. |
| < 50 | Poor fit — don't recommend unless user explicitly insists. |

---

## The Flow (step by step)

### Step 1 — Project profile extraction
From the user's request (after the clarifying questions in CLAUDE.md Step 1), extract:

- **Domain**: `ai-ml`, `frontend-backend`, `devops-cloud`, `mobile`, or `mixed`.
- **Stage**: `mvp-speed`, `production-scale`, `research-experimental`, or `enterprise-compliance`.
- **Constraints** (free-form): team size, budget, existing stack, deployment target, timeline, regulatory needs.
- **Success criteria**: latency, cost, DX, scale, accuracy, etc.

If the user didn't supply enough info, **ask more questions** — never guess.

### Step 2 — Roadmap selection
Open the relevant `roadmaps/<category>/README.md` (or multiple, if `mixed`). For each:
- Note the candidate technologies listed.
- Note the recommended sequencing for the user's stage.

### Step 3 — Load scoring inputs
- Read [`scoring/weights.json`](scoring/weights.json) → pick the `weight[stage]` profile.
- For each candidate, read its `roadmaps/<category>/<tech>.md` → extract the scoring matrix.

### Step 4 — Compute weighted scores
Apply the formula. Round to the nearest integer.

### Step 5 — Filter + rank
- Drop candidates with `score < 50` (unless user constraints force it).
- Sort descending.
- Take top 3.

### Step 6 — Build decision cards
For each top-3 tech, fill [`templates/decision-card.md`](templates/decision-card.md):
- Weighted score + the math behind it
- Why it fits the user's profile (specific constraints → specific reasons)
- Trade-offs (cost, complexity, learning curve, when NOT to use)
- Source links (from the `.md` file's sources section)

### Step 7 — Surface questions
If any of the top 3 are within 5 points of each other, **ask one more question** to break the tie — usually a constraint the user hasn't mentioned yet.

### Step 8 — Wait for user decision
Do NOT auto-pick. Present, then wait.

### Step 9 — Log to `godmode.md`
After the user chooses (or rejects all and asks for new candidates), append to `godmode.md`:
- `## Recent Decisions` → dated entry with tech chosen + brief why.
- `## Last Session` → refresh date, what was decided, what the next concrete step is.

---

## Edge Cases

### Tech not in `roadmaps/` yet
If the user asks about a technology that has no `.md` file:
- **Say so honestly.** Don't fake a score.
- Offer two paths:
  - *"I can research it now using the protocol in `scripts/research-batch.md` and add it to `roadmaps/`, then score it."*
  - *"Or I can give you an unverified gut-feel answer with a clear caveat — your call."*

### User wants a quick gut-feel
If the user explicitly says *"just tell me, don't make me wait for the formula"*:
- Give the recommendation.
- **Still** state the score and the criterion breakdown briefly (one line per criterion).
- Never drop the transparency.

### Two technologies score within 3 points
Tiebreaker rules (in order):
1. Better fit on the user's most-weighted constraint.
2. Better fit on team-experience (if known).
3. Lower total cost of ownership.
4. If still tied → ask the user.

### User picks something below the threshold
The model must **respect the choice** but also **document the warning**:
- Add a note to `godmode.md` Recent Decisions: *"User chose <X> despite score <Y>. Reason: <user's reason>. Risk: <...>"*.

---

## Anti-patterns (do NOT do these)

- ❌ Picking a tech before computing scores.
- ❌ Recommending the same tech for every project ("LangChain is always good").
- ❌ Hiding the math — the user should see the score and weights.
- ❌ Skipping the clarifying questions because "the user knows what they want".
- ❌ Inventing scores for techs not yet covered.
- ❌ Citing sources without their dates.

---

## Self-test

After every Phase completion (a roadmap category finishes), run a self-test:

1. Pick a sample scenario from `godmode.md` (or invent one).
2. Run the full flow end-to-end.
3. Verify the output makes sense.
4. If the top-3 all score above 80 with no clear winner, the weights need rebalancing → update [`scoring/weights.json`](scoring/weights.json) and re-run.

---

## Versioning

This file is owned by the model (with user approval). Major rewrites should be logged in `godmode.md`.