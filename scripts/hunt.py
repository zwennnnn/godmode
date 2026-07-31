#!/usr/bin/env python3
"""
hunt.py — /godhunt runner: scaffold a project from a ProductHunt candidate.

This script is called by the agent (in CLAUDE.md / SKILL.md protocol) AFTER the agent has:
1. Fetched ProductHunt's daily/weekly top products (via WebSearch / WebFetch).
2. Filtered by user market (read from godmode.md or default to "global").
3. Scored each (market fit + build feasibility + quality) using godmode's scoring engine.
4. Picked a single best candidate.

The agent then invokes this script with the product's metadata to scaffold the project.

Usage:
    python scripts/hunt.py create \\
        --name "Turso Notes" \\
        --slug "turso-notes" \\
        --ph-url "https://www.producthunt.com/posts/turso-notes" \\
        --market "Turkey" \\
        --mode customize \\
        --market-score 88 \\
        --feasibility-score 92 \\
        --quality-score 80 \\
        --short-description "Lightweight collaborative notes with offline-first sync" \\
        --market-justification "Remote teams in Turkey need offline-first notes; local data-residency" \\
        --mvp-scope "Markdown editor; realtime sync; offline-first; multi-device" \\
        --features "Markdown editor,Real-time collaboration,Offline-first sync,Mobile PWA" \\
        --frontend "Next.js 15 (App Router)" \\
        --backend "Next.js API routes" \\
        --db "SQLite + Drizzle (Turso for prod)" \\
        --auth "Auth.js" \\
        --deploy "Vercel" \\
        --customizations "Türkçe dil desteği, KVKK uyumlu veri saklama, TL fiyatlandırma" \\
        --ph-description "Original PH tagline..."
"""
import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "templates"


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def render_template(template_path, **kwargs):
    text = template_path.read_text(encoding="utf-8")
    for key, value in kwargs.items():
        text = text.replace("{" + key + "}", str(value))
    return text


def create_project(args):
    """Create projects/<slug>/ with README.md, PLAN.md, and an empty structure."""
    projects_root = ROOT / "projects"
    projects_root.mkdir(exist_ok=True)
    project_dir = projects_root / args.slug
    if project_dir.exists():
        print(f"[warn] {project_dir} already exists. Overwriting?", file=sys.stderr)
        resp = input("[warn] Overwrite? [y/N]: ").strip().lower()
        if resp != "y":
            print("Aborted.")
            sys.exit(0)
    project_dir.mkdir(parents=True, exist_ok=True)

    today = date.today().isoformat()

    # Render README.md
    readme_path = project_dir / "README.md"
    readme_path.write_text(render_template(
        TEMPLATES / "project-readme.md",
        name=args.name,
        slug=args.slug,
        ph_url=args.ph_url,
        market=args.market,
        date=today,
        mode=args.mode,
        market_score=args.market_score,
        feasibility_score=args.feasibility_score,
        quality_score=args.quality_score,
        short_description=args.short_description,
        market_justification=args.market_justification,
        mvp_scope=args.mvp_scope,
        features_list="\n".join(f"- {f.strip()}" for f in args.features.split(",")),
        frontend=args.frontend,
        f_score=args.f_score or "?",
        f_why=args.f_why or "auto-scored",
        backend=args.backend,
        b_score=args.b_score or "?",
        b_why=args.b_why or "auto-scored",
        db=args.db,
        d_score=args.d_score or "?",
        d_why=args.d_why or "auto-scored",
        auth=args.auth,
        a_score=args.a_score or "?",
        a_why=args.a_why or "auto-scored",
        deploy=args.deploy,
        dep_score=args.dep_score or "?",
        dep_why=args.dep_why or "auto-scored",
        customizations=args.customizations or "(no customizations — building as-is)",
        ph_description=args.ph_description or "(see PH link)",
    ), encoding="utf-8")

    # Render PLAN.md
    plan_path = project_dir / "PLAN.md"
    plan_path.write_text(render_template(
        TEMPLATES / "project-plan.md",
        name=args.name,
        slug=args.slug,
        date=today,
        market=args.market,
    ), encoding="utf-8")

    # Empty structure markers (agent / user fills these in)
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "tests").mkdir(exist_ok=True)
    (project_dir / ".env.example").write_text(
        f"# Minimax API\n"
        f"MINIMAX_API_KEY=your-minimax-api-key\n\n"
        f"# Database\n"
        f"DATABASE_URL=your-database-url\n\n"
        f"# Auth\n"
        f"AUTH_SECRET=your-auth-secret\n",
        encoding="utf-8",
    )

    # Log to godmode.md
    godmode_path = ROOT / "godmode.md"
    if godmode_path.exists():
        text = godmode_path.read_text(encoding="utf-8")
        log_entry = (
            f"- {today} — `/godhunt` → created `projects/{args.slug}/` "
            f"(market={args.market}, scores=market:{args.market_score}/feasibility:{args.feasibility_score}/quality:{args.quality_score})\n"
        )
        if "## Recent Decisions" in text and "no decisions yet" in text.lower():
            text = text.replace("(no decisions yet)", log_entry.strip())
        else:
            text = text.replace("## Recent Decisions\n", f"## Recent Decisions\n\n{log_entry}")
        godmode_path.write_text(text, encoding="utf-8")

    print(f"\n[ok] Created project: {project_dir}")
    print(f"     README.md      ({args.name} overview + tech stack)")
    print(f"     PLAN.md        (6-phase build plan)")
    print(f"     src/, tests/   (empty — for /godproject <name>)")
    print(f"     .env.example   (Minimax API + secrets)")
    print(f"\n[next] Run `/godproject {args.slug}` to scaffold the code.")


def main():
    ap = argparse.ArgumentParser(description="Create a projects/<slug>/ scaffold from a /godhunt candidate.")
    ap.add_argument("--name", required=True)
    ap.add_argument("--slug", required=True)
    ap.add_argument("--ph-url", default="")
    ap.add_argument("--market", required=True)
    ap.add_argument("--mode", choices=["customize", "as-is"], default="customize")
    ap.add_argument("--market-score", type=int, default=0)
    ap.add_argument("--feasibility-score", type=int, default=0)
    ap.add_argument("--quality-score", type=int, default=0)
    ap.add_argument("--short-description", default="")
    ap.add_argument("--market-justification", default="")
    ap.add_argument("--mvp-scope", default="")
    ap.add_argument("--features", default="")
    ap.add_argument("--frontend", default="")
    ap.add_argument("--f-score", default="")
    ap.add_argument("--f-why", default="")
    ap.add_argument("--backend", default="")
    ap.add_argument("--b-score", default="")
    ap.add_argument("--b-why", default="")
    ap.add_argument("--db", default="")
    ap.add_argument("--d-score", default="")
    ap.add_argument("--d-why", default="")
    ap.add_argument("--auth", default="")
    ap.add_argument("--a-score", default="")
    ap.add_argument("--a-why", default="")
    ap.add_argument("--deploy", default="")
    ap.add_argument("--dep-score", default="")
    ap.add_argument("--dep-why", default="")
    ap.add_argument("--customizations", default="")
    ap.add_argument("--ph-description", default="")
    args = ap.parse_args()
    create_project(args)


if __name__ == "__main__":
    main()