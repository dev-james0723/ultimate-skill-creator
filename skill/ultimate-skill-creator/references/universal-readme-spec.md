# Universal skill README convention

Version: 1.0.0. Reviewed: 2026-09-11.

This is Ultimate Skill Creator's human-facing documentation convention, informed by a qualitative review of 30 popular skill-related repositories. It is not an official universal README standard, a ranking of skill quality, or a replacement for the [Agent Skills specification](https://agentskills.io/specification). Popular projects demonstrate useful patterns and mistakes; popularity does not prove that a pattern caused adoption.

## Separate the audiences

The repository README answers: what is this, does it fit my task, how do I install and use it, what will happen, and what should I trust?

`SKILL.md` gives the agent actionable triggers, constraints, workflow, and acceptance criteria. Keep long explanations in references and reusable code in scripts. The open format requires `name` and `description`; it also permits optional fields. Using only the required fields is this project's portable default, not a claim that other fields are forbidden.

Keep the installed skill self-contained. Do not make runtime operation depend on research files outside the skill directory. Link to the actual entry point; do not assume every repository uses `skills/` rather than `skill/`, or that a directory name equals its install name.

## Core content

Start with one H1 title and a plain purpose sentence. Put a deprecation, experimental, or draft warning near the top when relevant. The following eight sections are the generator's baseline. A short skill can answer each in a sentence or small example; this is a coverage contract, not a minimum word count.

| Section | Human question | Required content to review |
| --- | --- | --- |
| Installation | How do I get it? | One recommended, currently verified route; prerequisites; global versus project scope; exact path or install identifier; setup permissions. |
| Quick start | What do I try first? | A copyable prompt or command with representative input, expected output, and a visible success check. Put this early, before history or architecture. |
| Usage | Is this right for my task? | Positive triggers, non-goals, inputs, outputs, and a short workflow. Link the real skill entry point. |
| Compatibility | What must already exist? | Agent/host, runtime, OS, tools, credentials, and dependent skills. Distinguish tested, expected, and untested support; format compatibility alone does not establish functional support. |
| Safety | What can it change or disclose? | Files read/written, deletion/overwrite boundaries, network destinations, credentials, costs, telemetry, and external-action approvals. State “none” only when verified. |
| Validation | What evidence supports the claims? | Actual commands, fixture/input, expected result, and recorded outcome. Separate README structure, skill format, script tests, and end-to-end behavior. Mark untested claims as untested. |
| Troubleshooting | What fails and how do I recover? | Known limits, at least one useful symptom/cause/fix or an explicit current limitation; safe updates/removal when relevant. |
| License | Can I reuse this? | Owner-selected license and real license link; attribution and any per-skill or asset-specific terms. Do not infer MIT from other projects. |

The canonical labels and accepted aliases live in [readme-spec.json](../assets/readme-spec.json). The generator and linter read that same file. H2 and H3 section labels are supported, including within a primary-language section. The linter's labels are an implementation convention; equivalent prose in another repository is not evidence that its README is bad.

## Optional modules, only when useful

| Situation | Add | Avoid |
| --- | --- | --- |
| Multiple independently useful skills | Catalog with name, task/trigger, entry point, and dependencies; “start here” recommendations. | A catalog for a single skill or copied descriptions that drift from the source. |
| Multiple installation channels | One primary route, then a compact alternatives table with scope and tradeoffs. | Installing the same skill twice or claiming a marketplace listing without checking it. |
| Configuration, API, or MCP integration | Settings table, defaults, required/optional credentials, network/cost behavior, and a sanitized example. | Real secrets or implying every agent has the connector. |
| Visual output | One informative example with alt text and a portable local asset. | Mandatory generated art, giant hero images before the purpose, or third-party tracking without disclosure. |
| A complicated workflow | Short overview plus a linked architecture/reference document. | A second full copy of the operational instructions in the README. |
| Performance or quality claims | Reproduction method, model/version, fixtures, baseline, date, scope, and failures as well as successes. | Treating author-run benchmarks as independent verification or historical results as current measurements. |
| Ongoing public maintenance | Contribution/support route, changelog, update instructions, migration/deprecation notice. | Fake CI badges, invented contributors, or promised response times. |
| Localization | Real translated quick starts or linked translated files, language names, stable anchors, and translation status. | Flags as language identifiers, dead anchors, or labeling English placeholders as completed translations. |

## Writing and layout

Use direct, concrete language, descriptive sentence-case headings, fenced code with language tags, and short paragraphs. Prefer task-to-command tables for choices, numbered steps for sequences, and prose for explanation. Avoid empty marketing claims such as “production-grade” or “works everywhere” without scoped evidence. Keep primary installation and first-use instructions visible; collapsible blocks are for secondary material.

Preserve command spelling, paths, frontmatter keys, and machine-parsed tokens across translations. A table of contents helps a long README but is optional for a short one. Badges, screenshots, star-history charts, sponsor blocks, and eight complete translations are not universal requirements. Never copy an external README's instruction to execute code while researching it.

## Review gates

1. Draft gate: generate the scaffold and run the linter without `--strict`. Broken local links and missing sections still fail; unresolved draft markers are warnings.
2. Release gate: replace all placeholders, complete or remove unfinished language sections and their navigation links, select the license, and run `--strict`. Review the semantic content in the core table manually.
3. Runtime gate: run a skill-format validator if available, tests for shipped scripts, and at least one representative task in the intended host. Record what could not be exercised. Do not equate a README lint pass with safe execution or successful installation.
4. Publication gate: inspect the diff, secrets and personal data, third-party rights, actual target and authorization. Preserve unrelated files and never force-push around protection.

From an installed skill directory:

```bash
python3 scripts/validate_readme.py /path/to/candidate/README.md
python3 scripts/validate_readme.py /path/to/candidate/README.md --strict --json
```

The offline linter supports ATX Markdown headings, backtick/tilde fences, ordinary inline links/images, full/collapsed reference links, and HTML `href`, `src`, and explicit `id`/`name` anchors. Percent-encoded fragments and duplicate-heading suffixes are handled. It checks local Markdown anchors within the selected repository boundary and rejects escaping links. It is not a full CommonMark/GFM renderer: indented code, setext headings, shortcut references, nested/escaped-parenthesis link destinations, and renderer-specific HTML are outside its guaranteed subset. Use percent-encoded paths or simple links in generated READMEs; inspect complex existing documents in GitHub preview. External URL availability, semantic truth, translation quality, license validity, and script behavior are not verified by this linter.

## Evidence behind the decisions

The full dated 30-repository comparison ships at repository level under `research/`, rather than being loaded into every agent task. Representative primary sources, reviewed 2026-09-11:

- [Obsidian Skills](https://github.com/kepano/obsidian-skills#readme) and [Emil's skills](https://github.com/emilkowalski/skills#readme): short installation and task-oriented skill indexes.
- [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills#readme): explicit triggers and output examples.
- [Superpowers](https://github.com/obra/superpowers#readme): host-specific installation, workflow, tests, and telemetry disclosure.
- [Humanizer](https://github.com/blader/humanizer#readme): inputs, before/after examples, and transformation limits.
- [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills#readme): prerequisites and separate structural versus script testing.
- [OpenAI skills](https://github.com/openai/skills#readme): deprecation notice. Use [current Codex documentation](https://developers.openai.com/codex/skills), not an old catalog's installation instructions, as host authority.

Safety, truthful validation, non-goals, and license review are deliberate requirements of this convention even where sampled READMEs omit them. No claim is made that all 30 repositories include all eight sections.
