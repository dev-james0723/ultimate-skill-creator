#!/usr/bin/env python3
"""Create a lightweight GitHub-ready skill candidate skeleton."""

import argparse
import pathlib
import re
import textwrap


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9-]+", "-", value.lower()).strip("-")
    slug = re.sub(r"-+", "-", slug)
    return slug[:63] or "new-skill"


def write(path: pathlib.Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True, help="Skill name or title")
    parser.add_argument("--out", required=True, help="Output candidate directory")
    parser.add_argument("--title", help="Human title")
    parser.add_argument("--languages", default="en,zh-Hant,zh-Hans,es,ja")
    args = parser.parse_args()

    skill_name = slugify(args.name)
    title = args.title or skill_name.replace("-", " ").title()
    root = pathlib.Path(args.out).expanduser().resolve()
    skill = root / "skills" / skill_name
    languages = [item.strip() for item in args.languages.split(",") if item.strip()]

    write(skill / "SKILL.md", f"""
    ---
    name: {skill_name}
    description: "TODO - Describe what this skill does and exactly when to use it."
    ---

    # {title}

    ## Quick Start

    1. TODO: State the first action.
    2. TODO: State the main workflow.
    3. TODO: State validation.

    ## Workflow

    - Capture the user's goal and constraints.
    - Use references for long case history.
    - Use scripts for repeatable commands.
    - Validate before publishing.
    """)

    write(skill / "references" / "case-study.md", """
    # Case Study

    ## Original Goal

    TODO

    ## Instructions and Constraints

    TODO

    ## Failed Attempts

    TODO

    ## Final Working Path

    TODO
    """)

    write(skill / "assets" / "flow.svg", f"""
    <svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675">
      <rect width="1200" height="675" fill="#0f172a"/>
      <text x="60" y="90" font-family="Arial" font-size="48" fill="#f8fafc">{title}</text>
      <g font-family="Arial" font-size="28" fill="#e2e8f0">
        <rect x="80" y="180" width="260" height="140" rx="18" fill="#1d4ed8"/>
        <text x="115" y="260">Problem</text>
        <rect x="470" y="180" width="260" height="140" rx="18" fill="#0f766e"/>
        <text x="520" y="260">Solution</text>
        <rect x="860" y="180" width="260" height="140" rx="18" fill="#7c3aed"/>
        <text x="910" y="260">Skill</text>
      </g>
      <path d="M350 250 H455 M740 250 H845" stroke="#fbbf24" stroke-width="10" stroke-linecap="round"/>
    </svg>
    """)

    lang_links = " | ".join(f"[{code}](#{code.lower().replace('-', '')})" for code in languages)
    write(root / "README.md", f"""
    # {title}

    Language: {lang_links}

    This repository is a candidate package for `{skill_name}`.

    ## Quick Start

    - Read `skills/{skill_name}/SKILL.md`.
    - Fill in `references/case-study.md`.
    - Run the skill validator.
    - Confirm before publishing to GitHub.
    """)

    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
