#!/usr/bin/env python3
"""
score.py — Weighted scoring engine for godmode technology decisions.
Implements the algorithm documented in decision-engine.md.

Usage:
    python scripts/score.py --roadmap ai-ml-llm --stage mvp-speed --top 3
    python scripts/score.py --roadmap frontend-backend --stage production-scale
    python scripts/score.py --roadmap all --stage mvp-speed --top 5
    python scripts/score.py --stage mvp-speed --query "vector database"   # free-text search
"""
import argparse
import json
import re
import sys
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent.parent
WEIGHTS_FILE = ROOT / "scoring" / "weights.json"

CORE_CRITERIA = [
    "maturity", "community", "learning_curve", "performance",
    "cost", "dx", "production_readiness",
]


def parse_frontmatter(text):
    """Minimal YAML frontmatter parser."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_block = text[3:end].strip()
    body = text[end + 4:].lstrip("\n")
    fm = {}
    for line in fm_block.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, _, value = line.partition(":")
            fm[key.strip()] = value.strip().strip('"').strip("'")
    return fm, body


def parse_scoring_matrix(text):
    """Extract criterion -> score from the Scoring Matrix table."""
    # Match the section header (allow either – or -)
    pattern = r"## Scoring Matrix \(0[–-]100\)\s*\n(.*?)(?=\n## |\Z)"
    match = re.search(pattern, text, re.DOTALL)
    if not match:
        return {}
    section = match.group(1)
    matrix = {}
    for line in section.splitlines():
        m = re.match(r"\|\s*([a-z_][a-z0-9 _]*?)\s*\|\s*(\d+)\s*\|", line.strip(), re.IGNORECASE)
        if not m:
            continue
        # Normalize criterion name
        crit_raw = m.group(1).strip().lower()
        crit = crit_raw.replace(" ", "_").replace("(", "").replace(")", "")
        # Handle "learning curve" -> "learning_curve"
        if crit == "learning_curve":
            crit = "learning_curve"
        try:
            score = int(m.group(2))
            matrix[crit] = score
        except (ValueError, IndexError):
            continue
    return matrix


def load_tech(roadmap_dir):
    """Load all researched tech MD files in a roadmap directory."""
    techs = []
    if not roadmap_dir.exists():
        return techs
    for path in sorted(roadmap_dir.glob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"  Warning: could not read {path.name}: {e}", file=sys.stderr)
            continue
        fm, body = parse_frontmatter(text)
        if fm.get("status") != "researched":
            continue
        matrix = parse_scoring_matrix(body)
        if not matrix:
            continue
        techs.append({
            "name": fm.get("name", path.stem),
            "file": path.name,
            "roadmap": roadmap_dir.name,
            "category": fm.get("category", ""),
            "matrix": matrix,
        })
    return techs


def load_weights():
    """Load weights.json; strip metadata keys (starting with _)."""
    with open(WEIGHTS_FILE, encoding="utf-8") as f:
        data = json.load(f)
    stages = {}
    for stage, weights in data.items():
        if stage.startswith("_"):
            continue
        stages[stage] = {
            k: float(v) for k, v in weights.items()
            if not k.startswith("_")
        }
    return stages


def score_tech(tech, stage_weights):
    """Compute weighted score + per-criterion breakdown."""
    total = 0.0
    breakdown = {}
    for criterion, weight in stage_weights.items():
        score = tech["matrix"].get(criterion, 0)
        contribution = weight * score
        total += contribution
        breakdown[criterion] = (weight, score, contribution)
    return round(total, 1), breakdown


def format_output(i, tech, score, breakdown, verbose=True):
    out = []
    out.append(f"#{i}  {tech['name']} ({tech['roadmap']}/)")
    out.append(f"    File: {tech['file']}")
    out.append(f"    Score: {score}")
    if verbose:
        out.append("    Breakdown (top contributors):")
        contribs = sorted(breakdown.items(), key=lambda x: -x[1][2])[:5]
        for crit, (w, s, c) in contribs:
            out.append(f"      {crit:<22} weight={w:.2f}  score={s:>3}  contrib={c:>6.1f}")
    out.append("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(
        description="Weighted scoring engine for godmode technology decisions.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("--roadmap", default="all", help="Roadmap folder (e.g. 'ai-ml-llm', 'frontend-backend') or 'all'")
    ap.add_argument("--stage", default="mvp-speed",
                    help="Stage profile: mvp-speed, production-scale, research-experimental, enterprise-compliance")
    ap.add_argument("--top", type=int, default=3, help="Number of top recommendations (default: 3)")
    ap.add_argument("--min-score", type=int, default=0, help="Minimum weighted score (default: 0)")
    ap.add_argument("--query", default=None, help="Free-text filter on tech names")
    ap.add_argument("--verbose", action="store_true", help="Show full breakdown")
    ap.add_argument("--json", action="store_true", help="Output as JSON")
    args = ap.parse_args()

    stages = load_weights()
    if args.stage not in stages:
        print(f"[error] Unknown stage: {args.stage}", file=sys.stderr)
        print(f"        Available: {', '.join(stages)}", file=sys.stderr)
        sys.exit(1)
    stage_weights = stages[args.stage]

    roadmaps_dir = ROOT / "roadmaps"
    if args.roadmap == "all":
        all_techs = []
        for rd in sorted(roadmaps_dir.iterdir()):
            if rd.is_dir():
                all_techs.extend(load_tech(rd))
    else:
        all_techs = load_tech(roadmaps_dir / args.roadmap)
        if not all_techs:
            print(f"[error] No techs found in {args.roadmap}", file=sys.stderr)
            sys.exit(1)

    if args.query:
        q = args.query.lower()
        all_techs = [t for t in all_techs if q in t["name"].lower() or q in t["roadmap"].lower()]

    if not all_techs:
        print(f"[error] No techs matched filters", file=sys.stderr)
        sys.exit(1)

    scored = []
    for tech in all_techs:
        score, breakdown = score_tech(tech, stage_weights)
        if score >= args.min_score:
            tech["score"] = score
            tech["breakdown"] = breakdown
            scored.append(tech)

    scored.sort(key=lambda t: t["score"], reverse=True)
    top = scored[:args.top]

    if args.json:
        output = {
            "stage": args.stage,
            "roadmap": args.roadmap,
            "evaluated": len(all_techs),
            "recommendations": [
                {
                    "rank": i,
                    "name": t["name"],
                    "roadmap": t["roadmap"],
                    "file": t["file"],
                    "score": t["score"],
                    "breakdown": {
                        c: {"weight": w, "score": s, "contribution": round(c2, 2)}
                        for c, (w, s, c2) in t["breakdown"].items()
                    },
                }
                for i, t in enumerate(top, 1)
            ],
        }
        print(json.dumps(output, indent=2))
        return

    print()
    print(f"=== godmode scoring ===")
    print(f"Stage:     {args.stage}")
    print(f"Roadmap:   {args.roadmap}")
    print(f"Evaluated: {len(all_techs)} techs")
    print(f"Showing:   top {len(top)}")
    print()

    for i, tech in enumerate(top, 1):
        print(format_output(i, tech, tech["score"], tech["breakdown"], args.verbose))


if __name__ == "__main__":
    main()