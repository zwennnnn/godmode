#!/usr/bin/env python3
"""
scrape-roadmap.py — Extract technology list from a roadmap.sh page and generate
stub MD files for each technology, following templates/tech-md.md.

Usage:
    python scripts/scrape-roadmap.py <roadmap-slug> [--output <dir>] [--template <path>]

Example:
    python scripts/scrape-roadmap.py ai-ml-llm-engineer --output roadmaps/ai-ml-llm

What it does:
1. Fetches https://roadmap.sh/<slug>
2. Parses the embedded JSON topic list (roadmap.sh exposes its roadmap data as JSON).
3. For each topic, generates a stub MD using the tech-md.md template.
4. Writes stubs to <output>/<topic-slug>.md with frontmatter pre-filled, body empty.

This is intentionally a *stub generator*, not a content writer. Filling the bodies
is the model's job (see scripts/research-batch.md), because that requires WebSearch
+ reasoning.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError

ROADMAP_SH_BASE = "https://roadmap.sh"
USER_AGENT = "godmode-scraper/0.1 (+https://github.com/local/godmode)"


def fetch_roadmap_json(slug: str) -> dict:
    """Fetch the JSON representation of a roadmap.sh page."""
    # roadmap.sh embeds the topic graph as JSON in a <script id="__NEXT_DATA__"> tag.
    # We fetch the HTML and extract it.
    url = f"{ROADMAP_SH_BASE}/{slug}"
    req = Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", errors="replace")
    except URLError as e:
        print(f"[error] Failed to fetch {url}: {e}", file=sys.stderr)
        sys.exit(1)

    # Try to find the JSON blob
    # roadmap.sh may have changed layout over time; try several patterns.
    patterns = [
        r'<script[^>]+id="__NEXT_DATA__"[^>]*>(.*?)</script>',
        r'<script[^>]+type="application/json"[^>]*>(.*?)</script>',
        r'"topics"\s*:\s*(\[[^\]]*\])',
    ]
    for pat in patterns:
        m = re.search(pat, html, re.DOTALL)
        if m:
            blob = m.group(1)
            try:
                return json.loads(blob)
            except json.JSONDecodeError:
                continue

    # Fallback: try the public JSON endpoint (if roadmap.sh exposes one).
    # As of 2026-07, roadmap.sh has a JSON endpoint at /<slug>.json
    for endpoint in (f"{ROADMAP_SH_BASE}/{slug}.json", f"{ROADMAP_SH_BASE}/api/{slug}"):
        try:
            req = Request(endpoint, headers={"User-Agent": USER_AGENT})
            with urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (URLError, json.JSONDecodeError):
            continue

    print(f"[error] Could not extract topic data from {url}.", file=sys.stderr)
    print("[hint] Open the page in a browser and inspect the HTML; the roadmap is", file=sys.stderr)
    print("       usually embedded as JSON in a <script> tag.", file=sys.stderr)
    sys.exit(2)


def slugify(text: str) -> str:
    """Convert 'Prompt Engineering' -> 'prompt-engineering'."""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def extract_topics(data: dict) -> list[dict]:
    """Walk the roadmap JSON tree and pull out topic nodes.

    Roadmap.sh topics typically have a 'title' or 'label' field and may have
    nested children. We flatten the tree.
    """
    topics = []

    def walk(node, parent_path=""):
        if isinstance(node, dict):
            title = node.get("title") or node.get("label") or node.get("name")
            if title and not node.get("isGroup", False) and not node.get("isMilestone", False):
                topics.append({
                    "title": title,
                    "slug": slugify(title),
                    "parent": parent_path,
                    "url": node.get("url") or node.get("link"),
                    "description": node.get("description", ""),
                })
            for child in node.get("children", []) or []:
                walk(child, parent_path=parent_path + " > " + (title or ""))
        elif isinstance(node, list):
            for item in node:
                walk(item, parent_path=parent_path)

    # Try common keys
    for key in ("topics", "nodes", "items", "roadmap"):
        if key in data:
            walk(data[key])
            return topics

    # If the data is a flat list
    if isinstance(data, list):
        walk(data)
        return topics

    # Otherwise, walk the whole object
    walk(data)
    return topics


STUB_TEMPLATE = """---
name: {title}
category: {category}
status: placeholder
last-updated: {date}
sources: []
tags: []
---

# {title}

> **Status:** placeholder. Body to be filled by research protocol (see `scripts/research-batch.md`).
> **Parent context:** {parent}

## One-liner

*TODO*

## What It Is

*TODO — 2–3 short paragraphs from official docs + 1–2 third-party sources.*

## When To Use It

*TODO*

## When NOT To Use It

*TODO*

## Why It Matters in 2026

*TODO — cite 2025–2026 sources.*

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 50 | *TODO — placeholder, replace with researched value* |
| Community | 50 | *TODO* |
| Learning curve | 50 | *TODO* |
| Performance | 50 | *TODO* |
| Cost | 50 | *TODO* |
| DX | 50 | *TODO* |
| Production readiness | 50 | *TODO* |

## Comparison With Alternatives

*TODO*

## Sources

*TODO — at least 3 sources, each with `YYYY-MM` date.*
"""


def write_stub(topic: dict, category: str, output_dir: Path) -> Path:
    """Write one stub MD file."""
    today = "2026-07-30"  # fixed during skeleton phase; replace with date.today() later
    body = STUB_TEMPLATE.format(
        title=topic["title"],
        category=category,
        parent=topic["parent"] or "(root)",
        date=today,
    )
    out_path = output_dir / f"{topic['slug']}.md"
    out_path.write_text(body, encoding="utf-8")
    return out_path


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", help="roadmap.sh slug (e.g. 'ai-ml-llm-engineer')")
    ap.add_argument("--output", "-o", required=True, help="Output directory for stubs")
    ap.add_argument("--category", "-c", default=None, help="Category folder name (default: <slug>)")
    args = ap.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    category = args.category or args.slug

    print(f"[info] Fetching roadmap.sh/{args.slug} ...")
    data = fetch_roadmap_json(args.slug)

    topics = extract_topics(data)
    if not topics:
        print("[warn] No topics extracted. Inspect the HTML manually.", file=sys.stderr)
        sys.exit(3)

    print(f"[info] Found {len(topics)} topics.")
    written = []
    for topic in topics:
        path = write_stub(topic, category, output_dir)
        written.append(path)
        print(f"  [stub] {path.name}")

    print(f"\n[done] Wrote {len(written)} stub files to {output_dir}/")
    print("[next] For each stub, follow scripts/research-batch.md to fill the body.")


if __name__ == "__main__":
    main()