---
name: godproject
description: Scaffold the actual code (package.json, src/, .env.example) for an existing projects/<slug>/ (typically created by /godhunt). Auto-detects framework from README.md or accepts --framework override. Fully autonomous.
---

# /godproject — Scaffold Code for an Existing Project

> **Invocation:** in Claude Code, type `/godproject <slug>` (e.g. `/godproject turkce-ai-destek`). Or type `/skill godproject <slug>`. Or just describe the request in natural language.
> **Argument** (required): the project name / folder name under `projects/`.
> **Behavior:** scaffold the actual code (package.json, src/, .env.example) for an existing `projects/<slug>/` (typically created by `/godhunt` or hand-written). Fully autonomous — no user input.

## Protocol (agent must follow exactly)

1. **Verify `projects/<slug>/` exists** and has a `README.md` (from `/godhunt` or hand-written).
   - If missing, stop and tell the user to run `/godhunt` first.

2. **Read the tech stack** from the README's `## Tech stack` table.

3. **Optionally re-score** via `python scripts/score.py --stage mvp-speed` to confirm.

4. **Generate the scaffold:**
   ```bash
   python scripts/project.py init --name <slug> --framework <nextjs|fastapi|express|react-vite|django|go-gin>
   ```
   Auto-detects framework from README.md if `--framework` not given.

5. **Scaffold includes:**
   - `package.json` (or `requirements.txt` / `go.mod`) with deps
   - Minimal `src/app/page.tsx` (Next.js) or `src/main.py` (FastAPI) or `src/server.js` (Express)
   - `.gitignore`
   - `.env.example` with `MINIMAX_API_KEY=your-key-here`

6. **Log** to `godmode.md` under `## Recent Decisions`.

7. **Tell the user:**
   > "Code scaffolded in `projects/<slug>/`. `cd projects/<slug> && pnpm install && pnpm dev` to start."

## Rules

- ❌ **Never** ask the user clarifying questions.
- ✅ **Always** detect framework from README or use the explicit argument.
- ✅ **Always** log to `godmode.md`.
- ✅ **Always** print the run command.

## Example

```
> /godproject turkce-ai-destek

[agent detects Next.js from README tech stack, runs scripts/project.py init]

Scaffolded code in projects/turkce-ai-destek/ (nextjs):
  package.json
  tsconfig.json
  src/app/page.tsx
  src/lib/minimax.ts
  .env.example
  .gitignore

Next: cd projects/turkce-ai-destek && pnpm install && pnpm dev
```
