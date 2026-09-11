# Ultimate Skill Creator workflow

## 1. Understand the solved problem

Capture the original goal, constraints, environment, permissions, failed attempts and their causes, working steps, validation evidence, and safety boundaries. Separate observed results from assumptions. Ask only for genuinely missing decisions, such as an unspecified publication target or license; reuse the user's existing explicit instructions.

## 2. Extract reusable knowledge

| Destination | Contents |
| --- | --- |
| SKILL.md | Triggers, non-goals, actionable workflow, acceptance criteria, and safety rules. |
| references/ | Detailed evidence, case histories, decisions, API notes, and troubleshooting, loaded when needed. |
| scripts/ | Deterministic helpers with documented dependencies and regression tests. |
| assets/ | Optional diagrams, images, templates, and shared specification data. |
| agents/openai.yaml | Optional Codex presentation/invocation adapter. |
| Repository README | Human purpose, installation, examples, expected outputs, compatibility, trust boundaries, verification, and license. |

Do not dump a transcript into the runtime skill. Do not move an existing skill simply to match a preferred directory name.

## 3. Build the candidate

A new candidate uses `README.md` beside `skills/<name>/SKILL.md`, with optional references, scripts, assets, and adapters. Existing Ultimate Skill Creator installations retain this repository's `skill/ultimate-skill-creator/` path. Add a license file only after the owner selects the license; do not silently inherit this repository's MIT terms for a new user's material.

Run `scripts/create_skill_candidate.py` from the installed skill for a scaffold. All original CLI flags remain available. The output directory must not already exist. Replace every placeholder with the actual solved workflow; generation alone is not validation.

## 4. Write human documentation

Read [the universal README convention](universal-readme-spec.md). Use its eight core content areas and only relevant optional modules. Verify the selected host's current installation documentation; a generic skill format does not imply that plugins, hooks, tools, or permissions are portable.

Follow [language guidance](language-and-readme.md). Advertise only real sections or translated files. Generated untranslated sections remain visibly marked as drafts until completed or removed. Keep required commands and machine-readable tokens literal across languages.

## 5. Package visuals when useful

Use a visual to clarify output or a workflow, not as a required decoration. Keep a portable local fallback, useful alt text, and provenance. Inspect screenshots for personal information. The existing guide PNG and fallback SVG remain available in `assets/`.

## 6. Validate at separate levels

Run `python3 scripts/validate_readme.py /path/to/candidate/README.md --strict --json` from the installed skill directory. Resolve findings and manually review each section's truth and usefulness. The linter does not certify functionality or contact external URLs.

Run the system skill-creator's `quick_validate.py` against the skill directory when available. Otherwise report that tool as not run, inspect frontmatter and relative references, and avoid claiming equivalent full validation. Test shipped scripts, including `--help`, happy paths, invalid input, and file-safety cases. Exercise at least one actual task in the intended host when available. Record environment, input, command, result, and untested areas.

For this repository's generator/linter regression suite, run `python3 -m unittest discover -s tests -v` from the repository root.

## 7. Publish within authorization

Read [publication safety](github-publication.md). Inspect the diff, secrets, rights, tests, target, visibility, and intended branch. Current explicit authorization can cover a scoped update without asking the user to approve the same change again. Ask before actions outside that scope. Preserve unrelated files, respect branch protection, use a non-forced update, and verify the resulting remote commit. Report a draft PR as a PR, not as a change already live on the default branch.
