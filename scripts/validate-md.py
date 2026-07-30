#!/usr/bin/env python3
"""
validate-md.py — Validate that a tech MD file conforms to the Godmode schema.

Checks:
1. Has YAML frontmatter with required fields: name, category, status, last-updated, sources.
2. `status` is one of: researched, outdated, experimental, placeholder.
3. `last-updated` matches YYYY-MM-DD.
4. `sources` is a list with >= 3 entries (when status == 'researched').
5. Has all required sections: One-liner, What It Is, When To Use It, When NOT To Use It,
   Why It Matters in 2026, Scoring Matrix, Comparison With Alternatives, Sources.
6. Scoring Matrix has the core 7 criteria (maturity, community, learning_curve,
   performance, cost, dx, production_readiness).
7. Every scoring cell has evidence (non-empty after the `|`).
8. No leftover `*TODO*` markers.

Usage:
    python scripts/validate-md.py roadmaps/<category>/<tech>.md
    python scripts/validate-md.py roadmaps/<category>/  # validates all .md in dir
    python scripts/validate-md.py --all  # validates everything under roadmaps/
"""

import argparse
import re
import sys
from pathlib import Path

REQUIRED_FRONTMATTER = ["name", "category", "status", "last-updated", "sources"]
ALLOWED_STATUS = {"researched", "outdated", "experimental", "placeholder"}
REQUIRED_SECTIONS = [
    "## One-liner",
    "## What It Is",
    "## When To Use It",
    "## When NOT To Use It",
    "## Why It Matters in 2026",
    "## Scoring Matrix",
    "## Comparison With Alternatives",
    "## Sources",
]
CORE_CRITERIA = [
    "maturity",
    "community",
    "learning_curve",
    "performance",
    "cost",
    "dx",
    "production_readiness",
]
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body). Expects --- delimiters."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_block = text[3:end].strip()
    body = text[end + 4 :].lstrip("\n")
    # Naive YAML parser — handles the simple key: value and key: [a, b] cases.
    fm = {}
    current_key = None
    for line in fm_block.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if line.startswith("  ") and current_key:
            # Continuation of a list
            stripped = line.strip().rstrip(",")
            if stripped.startswith("- "):
                fm[current_key].append(stripped[2:].strip().strip('"').strip("'"))
            continue
        m = re.match(r"^([a-zA-Z_][a-zA-Z0-9_-]*)\s*:\s*(.*)$", line)
        if not m:
            continue
        key, value = m.group(1), m.group(2).strip()
        current_key = key
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1]
            items = []
            for piece in inner.split(","):
                piece = piece.strip().strip('"').strip("'")
                if piece:
                    items.append(piece)
            fm[key] = items
        elif value == "":
            fm[key] = []
        else:
            fm[key] = value.strip('"').strip("'")
    return fm, body


def validate_file(path: Path) -> list[str]:
    errors = []
    text = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)

    # 1. Frontmatter fields
    for field in REQUIRED_FRONTMATTER:
        if field not in fm:
            errors.append(f"Missing frontmatter field: {field}")

    # 2. status
    if fm.get("status") not in ALLOWED_STATUS:
        errors.append(f"Invalid status: {fm.get('status')!r}. Must be one of {ALLOWED_STATUS}.")

    # 3. last-updated format
    if "last-updated" in fm and not DATE_RE.match(fm["last-updated"]):
        errors.append(f"Invalid last-updated: {fm['last-updated']!r}. Must be YYYY-MM-DD.")

    # 4. sources >= 3 if researched
    if fm.get("status") == "researched":
        sources = fm.get("sources", [])
        if not isinstance(sources, list) or len(sources) < 3:
            errors.append(f"status=researched requires >= 3 sources; found {len(sources) if isinstance(sources, list) else 0}.")

    # 5. Required sections
    for section in REQUIRED_SECTIONS:
        if section not in body:
            errors.append(f"Missing section: {section}")

    # 6. Scoring matrix criteria
    scoring_section = ""
    in_scoring = False
    for line in body.splitlines():
        if line.startswith("## Scoring Matrix"):
            in_scoring = True
            continue
        if in_scoring:
            if line.startswith("## "):
                break
            scoring_section += line + "\n"
    for crit in CORE_CRITERIA:
        # Accept snake_case, spaced form, or with parens (e.g. "Learning curve")
        crit_spaced = crit.replace("_", " ")
        crit_pat = re.compile(rf"\b{re.escape(crit)}\b|\b{re.escape(crit_spaced)}\b", re.IGNORECASE)
        if not crit_pat.search(scoring_section):
            errors.append(f"Scoring matrix missing core criterion: {crit}")

    # 7. No empty evidence cells (look for rows with only `| X |` after the score column)
    for line in scoring_section.splitlines():
        if line.startswith("|") and not line.startswith("|---") and not line.startswith("| Criterion"):
            cells = [c.strip() for c in line.split("|")]
            # Expect: ['', 'Criterion', 'Score', 'Evidence', '']
            if len(cells) >= 4:
                evidence = cells[3]
                if evidence in ("", "*TODO*", "TODO"):
                    errors.append(f"Scoring row missing evidence: {line.strip()}")

    # 8. No leftover TODO markers
    for marker in ("*TODO*", "TODO — placeholder"):
        if marker in body:
            errors.append(f"Leftover placeholder marker: {marker!r}")

    return errors


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*", help="MD file(s) or directories to validate")
    ap.add_argument("--all", action="store_true", help="Validate every .md under roadmaps/")
    args = ap.parse_args()

    targets: list[Path] = []
    if args.all:
        root = Path(__file__).resolve().parent.parent
        targets.extend(root.glob("roadmaps/**/*.md"))
    else:
        for p in args.paths:
            path = Path(p)
            if path.is_dir():
                targets.extend(path.glob("*.md"))
            else:
                targets.append(path)

    if not targets:
        print("[error] No targets. Pass file paths, a directory, or --all.", file=sys.stderr)
        sys.exit(1)

    total_errors = 0
    for path in sorted(targets):
        if not path.exists():
            print(f"[skip] {path} (not found)")
            continue
        # README.md files are roadmap index files, not tech MDs — skip them.
        if path.name.lower() == "readme.md":
            print(f"[skip] {path} (roadmap index, not a tech file)")
            continue
        errors = validate_file(path)
        if errors:
            print(f"[FAIL] {path}")
            for e in errors:
                print(f"   - {e}")
            total_errors += len(errors)
        else:
            print(f"[ OK ] {path}")

    print(f"\n{'PASS' if total_errors == 0 else 'FAIL'}: {total_errors} error(s) across {len(targets)} file(s).")
    sys.exit(0 if total_errors == 0 else 1)


if __name__ == "__main__":
    main()