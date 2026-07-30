#!/usr/bin/env python3
"""
research.py — Generate a new tech MD file from research data.
Implements the protocol in scripts/research-batch.md.

This is a scaffolder: the AI agent (or human) does the WebSearch + reasoning,
then fills the body fields. research.py creates the MD shell with proper frontmatter,
scoring matrix, and structure; then validates against templates/tech-md.md.

Usage:
    python scripts/research.py --interactive
    python scripts/research.py --name "Redis" --roadmap databases \\
        --sources "https://redis.io/,https://redis.io/docs/" \\
        --tags "cache,in-memory" \\
        --maturity 100 --community 100 --learning-curve 85 --performance 100 --cost 70 --dx 90 --production-readiness 100 \\
        --one-liner "In-memory data store used as cache, broker, leaderboard, and pub/sub." \\
        --when-to-use "Caching; sessions; leaderboards; pub/sub; rate limiting." \\
        --when-not "Durable storage; complex queries; huge data sets." \\
        --why-matters "Redis 8 license restored open source; Valkey is the OSS fork." \\
        --alternatives "| Memcached | Simpler cache | No data structures |" \\
        --body-paragraphs "Redis is the most popular in-memory store..."

If --interactive is set, prompts for each field.
"""
import argparse
import re
import sys
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent.parent

CORE_CRITERIA = ["maturity", "community", "learning_curve", "performance", "cost", "dx", "production_readiness"]


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def build_frontmatter(name, category, sources, tags=None):
    today = date.today().isoformat()
    sources_list = [s.strip() for s in sources.split(",") if s.strip()]
    sources_yaml = "\n".join(f"  - {s}" for s in sources_list) if sources_list else "  - TODO"
    tags_yaml = ""
    if tags:
        tags_list = [t.strip() for t in tags.split(",") if t.strip()]
        if tags_list:
            tags_yaml = "tags:\n" + "\n".join(f"  - {t}" for t in tags_list) + "\n"
    return f"""---
name: {name}
category: {category}
status: researched
last-updated: {today}
sources:
{sources_yaml}
{tags_yaml}---

"""


def build_scoring_matrix(scores):
    rows = []
    for c in CORE_CRITERIA:
        s = scores.get(c, 50)
        label = c.replace("_", " ").title()
        if c == "dx":
            label = "DX (developer experience)"
        rows.append(f"| {label} | {s} | TODO — add one-line evidence |")
    return "\n".join(rows)


def build_alternatives_table(alternatives_str):
    """Parse '| Alt | When | When |' lines into a markdown table."""
    if not alternatives_str:
        return "| Alternative | Better when | Worse when |\n| --- | --- | --- |\n| TODO | TODO | TODO |"
    lines = [l.strip() for l in alternatives_str.strip().split("\n") if l.strip()]
    out = ["| Alternative | Better when | Worse when |", "| --- | --- | --- |"]
    for line in lines:
        parts = [p.strip() for p in line.split("|")]
        if len(parts) == 3:
            out.append(f"| {parts[0]} | {parts[1]} | {parts[2]} |")
    return "\n".join(out)


def build_body(one_liner, when_to_use, when_not, why_matters, body_paragraphs, alternatives_table):
    paras = body_paragraphs.strip() if body_paragraphs else "TODO"
    return f"""# {one_liner.split('.')[0] if one_liner else 'TODO'}

## One-liner

{one_liner or "TODO"}

## What It Is

{paras}

## When To Use It

{chr(10).join('- ' + (line.strip() if line.strip() else 'TODO') for line in (when_to_use or 'TODO').split(chr(10)))}

## When NOT To Use It

{chr(10).join('- ' + (line.strip() if line.strip() else 'TODO') for line in (when_not or 'TODO').split(chr(10)))}

## Why It Matters in 2026

{why_matters or "TODO"}

## Scoring Matrix (0-100)

| Criterion | Score | Evidence |
|-----------|-------|----------|

## Comparison With Alternatives

{alternatives_table}

## Sources

"""


def build_sources_section(sources):
    today = date.today().strftime("%Y-%m")
    sources_list = [s.strip() for s in sources.split(",") if s.strip()]
    if not sources_list:
        return "TODO"
    lines = []
    for s in sources_list:
        # Try to give it a sensible name from the URL
        url = s.replace("https://", "").replace("http://", "")
        name = url.split("/")[0] if "/" in url else url
        lines.append(f"- [{name}]({s}) — {today}")
    return "\n".join(lines)


def write_tech_md(out_path, name, category, sources, tags, scores, one_liner, when_to_use, when_not, why_matters, body_paragraphs, alternatives):
    """Compose the full MD file and write to out_path."""
    content = build_frontmatter(name, category, sources, tags)
    body = build_body(one_liner, when_to_use, when_not, why_matters, body_paragraphs, build_alternatives_table(alternatives))
    # Replace the TODO scoring matrix placeholder with real rows
    scoring_lines = build_scoring_matrix(scores).split("\n")
    body_lines = body.split("\n")
    out_lines = []
    inserted = False
    for line in body_lines:
        if line.strip() == "| Criterion | Score | Evidence |" and not inserted:
            out_lines.extend(scoring_lines)
            inserted = True
        elif line.strip() == "| --- | --- | --- |" and inserted and len(out_lines) > 0 and "Maturity" in out_lines[-1]:
            out_lines.append(line)
            continue
        else:
            out_lines.append(line)
    content += "\n".join(out_lines)
    content += "\n\n" + build_sources_section(sources)
    content += "\n"
    out_path.write_text(content, encoding="utf-8")


def interactive_prompt(args):
    """Fill missing args interactively."""
    if not args.name:
        args.name = input("Tech name: ").strip()
    if not args.roadmap:
        args.roadmap = input("Roadmap folder (e.g. databases, ai-ml-llm): ").strip()
    if not args.sources:
        args.sources = input("Source URLs (comma-separated): ").strip()
    if not args.tags:
        args.tags = input("Tags (comma-separated, optional): ").strip()
    if not args.one_liner:
        args.one_liner = input("One-liner: ").strip()
    if not args.when_to_use:
        args.when_to_use = input("When to use (one per line, end with empty line):\n")
        while True:
            line = input()
            if not line:
                break
            args.when_to_use += line + "\n"
    if not args.when_not:
        args.when_not = input("When NOT to use (one per line, end with empty line):\n")
        while True:
            line = input()
            if not line:
                break
            args.when_not += line + "\n"
    if not args.why_matters:
        args.why_matters = input("Why it matters in 2026: ").strip()
    if not args.body_paragraphs:
        args.body_paragraphs = input("Body paragraphs (full description): ").strip()
    if not args.alternatives:
        args.alternatives = input("Alternatives (one per line, format: 'Alt | better | worse', empty line to end):\n")
        while True:
            line = input()
            if not line:
                break
            args.alternatives += line + "\n"
    # Scores
    for c in CORE_CRITERIA:
        key = c.replace("_", "-")
        current = getattr(args, key, None)
        if current is None:
            val = input(f"  Score for {c} (0-100, default 50): ").strip()
            setattr(args, key, int(val) if val else 50)
    return args


def main():
    ap = argparse.ArgumentParser(description="Generate a godmode tech MD file from research data.")
    ap.add_argument("--interactive", action="store_true", help="Prompt for any missing fields")
    ap.add_argument("--name", help="Tech name (e.g. 'Redis')")
    ap.add_argument("--roadmap", help="Roadmap folder (e.g. 'databases', 'ai-ml-llm')")
    ap.add_argument("--sources", help="Comma-separated source URLs")
    ap.add_argument("--tags", default="", help="Comma-separated tags")
    ap.add_argument("--one-liner", default="", help="Single-sentence summary")
    ap.add_argument("--when-to-use", default="", help="When to use (multi-line)")
    ap.add_argument("--when-not", default="", help="When NOT to use (multi-line)")
    ap.add_argument("--why-matters", default="", help="Why it matters in 2026")
    ap.add_argument("--body-paragraphs", default="", help="Full body paragraphs")
    ap.add_argument("--alternatives", default="", help="Alternatives table content")
    ap.add_argument("--maturity", type=int, help="Maturity score (0-100)")
    ap.add_argument("--community", type=int, help="Community score (0-100)")
    ap.add_argument("--learning-curve", type=int, help="Learning curve score (0-100)")
    ap.add_argument("--performance", type=int, help="Performance score (0-100)")
    ap.add_argument("--cost", type=int, help="Cost score (0-100)")
    ap.add_argument("--dx", type=int, help="DX score (0-100)")
    ap.add_argument("--production-readiness", type=int, help="Production readiness score (0-100)")
    args = ap.parse_args()

    if args.interactive:
        args = interactive_prompt(args)

    # Validate required fields
    missing = [f for f in ("name", "roadmap", "sources") if not getattr(args, f)]
    if missing:
        print(f"[error] Missing required: {', '.join(missing)}", file=sys.stderr)
        print(f"        Use --interactive to fill them in.", file=sys.stderr)
        sys.exit(1)

    scores = {
        c: getattr(args, c.replace("_", "-"), 50) or 50
        for c in CORE_CRITERIA
    }

    # Write file
    roadmap_dir = ROOT / "roadmaps" / args.roadmap
    roadmap_dir.mkdir(parents=True, exist_ok=True)
    out_path = roadmap_dir / f"{slugify(args.name)}.md"

    if out_path.exists():
        resp = input(f"[warn] {out_path} exists. Overwrite? [y/N]: ").strip().lower()
        if resp != "y":
            print("Aborted.")
            sys.exit(0)

    write_tech_md(
        out_path=out_path,
        name=args.name,
        category=args.roadmap,
        sources=args.sources,
        tags=args.tags,
        scores=scores,
        one_liner=args.one_liner,
        when_to_use=args.when_to_use,
        when_not=args.when_not,
        why_matters=args.why_matters,
        body_paragraphs=args.body_paragraphs,
        alternatives=args.alternatives,
    )

    print(f"\n[ok] Written: {out_path}")
    print(f"[next] Fill in TODO evidence notes in the scoring matrix.")
    print(f"[next] Run: python scripts/validate-md.py {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()