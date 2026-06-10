# Ultimate Skill Creator Workflow

## 1. Understand the Solved Problem

Capture:

- the user's original goal
- every hard constraint and non-negotiable instruction
- the environment and permissions
- the failure modes discovered
- the final working path
- validation evidence
- safety boundaries

Ask for clarification only when publication target, license, or sensitive details are ambiguous.

## 2. Extract Reusable Knowledge

Classify content:

- **SKILL.md**: short operational instructions that every future agent needs.
- **references/**: long case history, decision trees, language variants, API notes, troubleshooting.
- **scripts/**: deterministic helpers or templates that should not be rewritten from scratch.
- **assets/**: generated images, icons, diagrams, screenshots, templates.
- **repo README**: human-facing GitHub presentation, not part of the skill folder unless the skill is specifically about README generation.

## 3. Build the Candidate

Default structure:

```text
repo-candidate/
├── README.md
├── skills/
│   └── skill-name/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── references/
│       ├── scripts/
│       └── assets/
└── LICENSE
```

Keep each skill folder clean. Avoid extra `CHANGELOG.md`, `INSTALL.md`, or README files inside the skill folder unless required.

## 4. Add Language Switching

For Markdown, use anchor links:

```markdown
Language: [English](#english) | [繁體中文](#繁體中文) | [简体中文](#简体中文) | [Español](#español) | [日本語](#日本語)
```

Include at least English, Traditional Chinese, Simplified Chinese, Spanish, Japanese, Portuguese, Hindi, and Arabic for broad reach when the user requests popular languages.

## 5. Generate or Package Images

Use generated images for guide diagrams when useful. Always keep a self-contained fallback asset such as an SVG in `assets/` so the GitHub package remains portable.

Recommended diagram types:

- problem-to-solution flow
- keyboard shortcut / physical setup
- decision tree
- skill creation loop

## 6. Validate

Run:

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py /path/to/skill-folder
```

Also run representative script checks, for example `python3 script.py --help`, `clang` compile checks, or shell syntax checks.

## 7. Publish Safely

Publication is external. Create the candidate locally, summarize it, and ask the user to confirm:

- target GitHub account/repo
- new repo or existing repo
- visibility
- branch name
- commit message
- direct push or draft PR

Only push after explicit confirmation.

