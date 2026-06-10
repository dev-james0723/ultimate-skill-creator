# GitHub Publication Safety

## Candidate-First Rule

Always create a local publication candidate before pushing. GitHub upload is an external publication action and needs explicit confirmation.

## Pre-Push Checklist

- `gh auth status` confirms the target account.
- `git status --short` is understood.
- The candidate contains no secrets, tokens, serial numbers, or accidental personal data.
- Skill validators pass.
- The target repo and visibility are confirmed.
- The user approves push.

## New Repository Flow

```bash
git init
git add README.md LICENSE skills/
git commit -m "Add skill pack"
gh repo create OWNER/REPO --private --source . --push
```

Use `--public` only after explicit confirmation.

## Existing Repository Flow

```bash
git remote add origin https://github.com/OWNER/REPO.git
git checkout -b codex/add-skill-pack
git add README.md LICENSE skills/
git commit -m "Add skill pack"
git push -u origin codex/add-skill-pack
gh pr create --draft --fill
```

Use a draft PR by default.

