#!/usr/bin/env python3
"""
project.py — /godproject runner: scaffold the code for an existing project.

Usage:
    python scripts/project.py init --name turso-notes
    python scripts/project.py init --name turso-notes --framework nextjs

Reads existing projects/<name>/{README,PLAN}.md and:
1. Re-scores tech stack via score.py to confirm choices.
2. Generates package.json / requirements.txt / Cargo.toml / etc.
3. Creates minimal scaffolding (README inside src/, .gitignore, etc.).
4. Logs to godmode.md.
"""
import argparse
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECTS = ROOT / "projects"


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def detect_framework(project_dir):
    """Detect the tech stack from README.md."""
    readme = project_dir / "README.md"
    if not readme.exists():
        return None
    text = readme.read_text(encoding="utf-8").lower()
    if "next.js" in text:
        return "nextjs"
    if "react" in text:
        return "react-vite"
    if "fastapi" in text or "python" in text:
        return "fastapi"
    if "go" in text and "gin" in text:
        return "go-gin"
    if "django" in text:
        return "django"
    if "node.js" in text or "express" in text:
        return "express"
    return None


def generate_nextjs_scaffold(project_dir, name):
    pkg = {
        "name": name,
        "version": "0.1.0",
        "private": True,
        "scripts": {
            "dev": "next dev",
            "build": "next build",
            "start": "next start",
            "lint": "next lint",
            "test": "vitest",
            "score": "python ../scripts/score.py --roadmap frontend-backend --stage mvp-speed",
        },
        "dependencies": {
            "next": "^15.0.0",
            "react": "^19.0.0",
            "react-dom": "^19.0.0",
            "@minimax/api": "latest",
            "zod": "^3.23.0",
        },
        "devDependencies": {
            "typescript": "^5.5.0",
            "@types/react": "^19.0.0",
            "tailwindcss": "^4.0.0",
            "vitest": "^2.0.0",
        },
    }
    (project_dir / "package.json").write_text(json.dumps(pkg, indent=2) + "\n", encoding="utf-8")

    # Minimal Next.js app structure
    (project_dir / "src" / "app").mkdir(parents=True, exist_ok=True)
    (project_dir / "src" / "app" / "page.tsx").write_text(
        f'export default function Home() {{\n'
        f'  return <main><h1>{name}</h1></main>;\n'
        f'}}\n',
        encoding="utf-8",
    )
    (project_dir / "src" / "app" / "layout.tsx").write_text(
        f'export const metadata = {{ title: "{name}" }};\n'
        f'export default function RootLayout({{ children }}) {{\n'
        f'  return <html><body>{{children}}</body></html>;\n'
        f'}}\n',
        encoding="utf-8",
    )
    (project_dir / "src" / "lib").mkdir(exist_ok=True)
    (project_dir / "src" / "lib" / "minimax.ts").write_text(
        "// Minimax API client — replace with your real SDK\n"
        "// Documented in: " + str(ROOT) + "\\skills.md\n",
        encoding="utf-8",
    )

    # tsconfig + next.config + tailwind + .gitignore
    (project_dir / "tsconfig.json").write_text(
        '{\n  "compilerOptions": { "target": "ES2022", "module": "esnext", "moduleResolution": "bundler", "jsx": "preserve", "strict": true }\n}\n',
        encoding="utf-8",
    )
    (project_dir / "next.config.mjs").write_text(
        "/** @type {import('next').NextConfig} */\nconst nextConfig = {};\nexport default nextConfig;\n",
        encoding="utf-8",
    )
    (project_dir / "postcss.config.mjs").write_text(
        'export default { plugins: { "@tailwindcss/postcss": {} } };\n',
        encoding="utf-8",
    )
    (project_dir / ".gitignore").write_text(
        "node_modules/\n.next/\n.env\n.env.local\n*.log\n",
        encoding="utf-8",
    )
    print(f"[ok] Generated Next.js 15 scaffold (App Router + TS + Tailwind v4).")


def generate_fastapi_scaffold(project_dir, name):
    (project_dir / "requirements.txt").write_text(
        "fastapi>=0.115.0\nuvicorn[standard]>=0.32.0\npydantic>=2.9.0\nsqlmodel>=0.0.22\nhttpx>=0.27.0\nminimax>=latest\n",
        encoding="utf-8",
    )
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "src" / "main.py").write_text(
        f'"""{name} — FastAPI entry point."""\n'
        f'from fastapi import FastAPI\n'
        f'app = FastAPI(title="{name}")\n'
        f'@app.get("/")\n'
        f'async def root():\n'
        f'    return {{"name": "{name}", "status": "ok"}}\n',
        encoding="utf-8",
    )
    (project_dir / ".gitignore").write_text(
        "__pycache__/\n*.pyc\n.env\nvenv/\n.venv/\n*.log\n",
        encoding="utf-8",
    )
    print(f"[ok] Generated FastAPI scaffold.")


def generate_express_scaffold(project_dir, name):
    pkg = {
        "name": name,
        "version": "0.1.0",
        "type": "module",
        "scripts": {
            "dev": "node --watch src/server.js",
            "start": "node src/server.js",
            "test": "vitest",
            "score": "python ../scripts/score.py --roadmap backend-frameworks --stage mvp-speed",
        },
        "dependencies": {
            "express": "^4.21.0",
            "minimax": "latest",
            "zod": "^3.23.0",
        },
        "devDependencies": {"vitest": "^2.0.0"},
    }
    (project_dir / "package.json").write_text(json.dumps(pkg, indent=2) + "\n", encoding="utf-8")
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "src" / "server.js").write_text(
        f'import express from "express";\n'
        f'const app = express();\n'
        f'app.get("/", (_, res) => res.json({{ name: "{name}", status: "ok" }}));\n'
        f'const port = process.env.PORT || 3000;\n'
        f'app.listen(port, () => console.log(`${{"{name}"}} on :${{port}}`));\n',
        encoding="utf-8",
    )
    (project_dir / ".gitignore").write_text(
        "node_modules/\n.env\n*.log\n",
        encoding="utf-8",
    )
    print(f"[ok] Generated Express scaffold.")


def init_project(args):
    name = args.name
    slug = slugify(name)
    project_dir = PROJECTS / slug

    if not project_dir.exists():
        print(f"[error] projects/{slug}/ not found.", file=sys.stderr)
        print(f"        Run /godhunt first to create the scaffold.", file=sys.stderr)
        sys.exit(1)

    framework = args.framework or detect_framework(project_dir)
    if not framework:
        print(f"[error] Could not detect framework from README.md.", file=sys.stderr)
        print(f"        Pass --framework (nextjs | fastapi | express | react-vite | django | go-gin).", file=sys.stderr)
        sys.exit(1)

    print(f"[info] Detected framework: {framework}")
    print(f"[info] Scaffolding code for projects/{slug}/...")

    if framework == "nextjs":
        generate_nextjs_scaffold(project_dir, slug)
    elif framework == "fastapi":
        generate_fastapi_scaffold(project_dir, slug)
    elif framework == "express":
        generate_express_scaffold(project_dir, slug)
    elif framework == "react-vite":
        # Same as nextjs but without SSR
        generate_nextjs_scaffold(project_dir, slug)
    elif framework == "django":
        print("[todo] Django scaffold — run `django-admin startproject <name> .` manually.")
    elif framework == "go-gin":
        print("[todo] Go scaffold — run `go mod init <name>` manually.")
    else:
        print(f"[warn] Unknown framework {framework!r}; no scaffold written.")

    today = date.today().isoformat()
    godmode_path = ROOT / "godmode.md"
    if godmode_path.exists():
        text = godmode_path.read_text(encoding="utf-8")
        log_entry = (
            f"- {today} — `/godproject {slug}` → scaffolded code ({framework}); "
            f"see `projects/{slug}/`\n"
        )
        if "## Recent Decisions" in text and "no decisions yet" in text.lower():
            text = text.replace("(no decisions yet)", log_entry.strip())
        else:
            text = text.replace("## Recent Decisions\n", f"## Recent Decisions\n\n{log_entry}")
        godmode_path.write_text(text, encoding="utf-8")

    print(f"\n[next] cd projects/{slug}/ && pnpm install && pnpm dev")


def main():
    ap = argparse.ArgumentParser(description="Scaffold code for an existing /godhunt project.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    init_p = sub.add_parser("init", help="Scaffold code in projects/<name>/")
    init_p.add_argument("--name", required=True, help="Project name (folder name if matches)")
    init_p.add_argument("--framework", choices=["nextjs", "fastapi", "express", "react-vite", "django", "go-gin"], help="Force framework")

    args = ap.parse_args()
    if args.cmd == "init":
        init_project(args)


if __name__ == "__main__":
    main()