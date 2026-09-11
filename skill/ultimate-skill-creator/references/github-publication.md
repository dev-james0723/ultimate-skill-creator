# GitHub publication safety

## Candidate-first rule

Prepare and validate the proposed files before external publication. Publication needs explicit user authorization. A current request to implement scoped changes directly in a named repository is authorization for those changes; do not ask the user to repeat it. It is not authorization to create another repository, change visibility, delete unrelated files, install software, or publish private source material.

## Pre-push checks

Confirm the connected account and target repository, current branch/commit, visibility, and relevant protection. Inspect the complete diff and preserve unrelated work. Remove secrets, tokens, private conversation material, serial numbers, and accidental personal data. Verify third-party rights and the owner's license choice. Run README lint, skill-format checks when available, script tests, and relevant behavioral checks; report skipped checks.

## New repositories

Confirm owner, name, visibility, license, and publication strategy before creation. Default to private when visibility is not specified; do not create it until the missing decision is resolved. Add only inspected files, not an unreviewed working directory. Do not invent a license just to make a checklist pass.

## Existing repositories

Fetch the latest state first. Use a branch and draft PR by default unless the user explicitly requests a direct update and branch policy permits it. Do not bypass protections or force-push. Prefer an atomic multi-file commit so the schema, generator, tests, and docs change together. Recheck the parent commit before updating the branch; if it changed, reconcile instead of overwriting the newer work.

No automatic deletion, broad cleanup, reset, or rollback is authorized by a failed validation or push. Preserve the candidate for inspection and report the actual failure. Verify the remote commit and distinguish local tests, remote CI results, PR creation, and default-branch publication in the completion report.
