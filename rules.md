# Godmode — Untouchable Rules

> ⚠️ **This file is owned by the user. The model (Claude, or any other LLM guided by this repo) MUST NOT modify, rewrite, or "improve" this file. It reads it. It follows it. It does not touch it.**
>
> If the model believes a rule should be added or changed, it must surface that suggestion to the user as a question — the user will edit this file themselves.

---

## Language & Format

1. **All `.md` content is English.** Even if the user writes in Turkish, French, or any other language, every file in `roadmaps/`, `templates/`, `scoring/`, and the root knowledge base is English. User-facing replies may match the user's language.
2. **All sources are linked and dated.** Every URL is paired with a `YYYY-MM` access date in the `.md` source.
3. **Scoring is integer 0–100.** No decimals. No "85.5". Round.
4. **MD frontmatter is required** for every tech file. See [`templates/tech-md.md`](templates/tech-md.md).

## Decision-Making

5. **Never recommend without clarifying questions first.** Even if the request seems obvious. At minimum one question.
6. **Never invent scoring numbers.** Pull from existing `.md` files or explicitly mark "estimated pending research".
7. **Always cite the source `.md` file** when recommending a technology, including the date in its frontmatter.
8. **Top 3 always.** Always present at least 3 candidates for any decision, unless the user explicitly asks for one.
9. **Always state trade-offs.** Every recommendation includes a "when NOT to use this" section.

## Memory & Continuity

10. **`godmode.md` is auto-updated by the model** after every major decision. The model writes here freely.
11. **`rules.md` is NEVER touched by the model.** Ever. This is the highest-priority rule. The model reads it; the user owns it.
12. **Progress is sequential.** Roadmap 1 must be marked complete (in `godmode.md`) before Roadmap 2 is started. No parallel filling.

## Research Discipline

13. **Use `roadmap.sh` as the canonical topic list** for each category. Don't invent technologies; don't skip the ones roadmap.sh lists.
14. **WebSearch is for verification and 2025–2026 data only.** Roadmap.sh is the structure; the web fills the gaps and updates the dates.
15. **One technology per `.md` file.** Never bundle multiple tools into one file. (Frameworks like LangChain + LlamaIndex can share a category folder but live in separate files.)
16. **At least 3 sources per tech file.** Official docs + at least one third-party benchmark / case study / community discussion.

## Tone

17. **No hype. No bullshit.** If a tool is overhyped, say so with evidence.
18. **Match the user's level.** Beginner → plain language + definitions. Expert → jargon is welcome.
19. **Honest about gaps.** If a tech isn't covered in `roadmaps/` yet, say so — don't fake the score.

---

## Adding New Rules

To add a rule, edit this file directly. Don't ask the model to do it for you. New rules go at the bottom under `## User-Added Rules (post-launch)` with a date.

---

## Versioning

This file has no version number. Rules are added; they are not "deprecated". If a rule stops applying, the user deletes it.