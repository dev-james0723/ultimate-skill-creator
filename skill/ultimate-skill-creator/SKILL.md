---
name: ultimate-skill-creator
description: Convert a solved user-agent workflow into a reusable, validated, GitHub-ready Codex skill. Use when the user wants to package a conversation, troubleshooting session, automation, research workflow, or hard-won solution into SKILL.md with references, scripts, assets, multilingual quick starts, generated images, README content, validation, and optional GitHub publication.
---

# Ultimate Skill Creator

## Quick Start

Use this skill when a user says: “turn what we just solved into a skill”, “make this reusable”, “package this as SKILL.md”, or “upload this skill to GitHub”.

1. Extract the solved workflow from the conversation.
2. Separate durable knowledge from one-off details.
3. Create a skill folder with `SKILL.md`, optional `references/`, `scripts/`, `assets/`, and `agents/openai.yaml`.
4. Add multilingual quick starts and self-contained visual assets when useful.
5. Validate the skill locally.
6. Create a GitHub publication candidate.
7. Ask for explicit confirmation before pushing or changing external repositories.

For the full repeatable workflow, read `references/workflow.md`.
For language and README patterns, read `references/language-and-readme.md`.
For GitHub publication safety, read `references/github-publication.md`.
For user-facing explainers, use `assets/ultimate-skill-creator-guide.png` or the portable fallback `assets/skill-creation-loop.svg`.

## What To Capture

Capture only reusable material:

- original user goal and non-negotiable constraints
- exact environment assumptions and permissions
- failed attempts and why they failed
- final working sequence and validation evidence
- safety boundaries and conditions where the skill should refuse or warn
- scripts, templates, or commands that improve repeatability

Move detailed transcripts and long histories into `references/`; keep `SKILL.md` action-oriented.

## Skill Packaging Rules

- Use lowercase hyphen-case skill names under 64 characters.
- Keep YAML frontmatter to `name` and `description`.
- Put detailed documentation in `references/`.
- Put deterministic helper code in `scripts/`.
- Put generated images, diagrams, icons, and templates in `assets/`.
- Do not put README files inside the skill folder unless the target skill specifically works with README files; create repository-level README content outside the skill.

## Automation

Use `scripts/create_skill_candidate.py` when a fast skeleton is useful:

```bash
python3 scripts/create_skill_candidate.py \
  --name my-skill \
  --out ./candidate \
  --title "My Skill" \
  --languages "en,zh-Hant,zh-Hans,es,ja"
```

Then replace placeholders with the actual solved workflow and run the validator from the system `skill-creator` skill when available.

## GitHub Publication

Publication is an external action. Always create a candidate first and ask before pushing.

Minimum pre-push checks:

- skill validator passes
- generated assets exist
- README has language navigation
- `git status` scope is clean and intentional
- target repo, visibility, branch, commit message, and PR/direct-push strategy are confirmed

Default to creating a new repository or draft PR only after the user approves.
