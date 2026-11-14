---
name: until-green
description: Own the post-push loop on a PR. Watch CI, triage review-bot comments, fix real issues, repeat until every blocking check is green. No check-ins.
argument-hint: "[pr-number] (defaults to the PR for the current branch)"
disable-model-invocation: true
---

Take the PR **$ARGUMENTS** (if empty, resolve it from the current branch with `gh pr view --json number`) to a landable state without involving me. Do not end your turn to report "CI is running" or "expect more bot comments" — that is the babysitting this skill exists to remove.

## Security pass

Before the loop, review the PR diff against its base once for security issues, with the `security-review` skill when you have it. Triage each finding like a bot comment: verify it in the code, then fix it as a fixup commit or note why it does not apply.

## Stack

A PR is stacked when its base is not the default branch, or when it is the base of another open PR. Move changes along the stack by merge, never by rebase.

- **Down, before the loop:** `git fetch origin`, then merge `origin/<baseRefName>` into the branch when it has commits the branch lacks, and push. When the base PR merged, GitHub retargets this PR to the default branch, so merge that.
- **Up, once the exit criteria hold:** for each open PR in `gh pr list --base <branch> --json number,headRefName`, merge this branch into its head and push, then repeat for the PRs based on that one. Work in the worktree that has the head checked out (`git worktree list`), or in a temporary one. Skip a worktree with uncommitted changes and report it.
- On a conflict the code does not settle, stop and ask me.

## Loop

Repeat until the exit criteria below hold:

1. Wait for CI on the latest commit. If your harness has a PR monitor that wakes you on CI changes, use it and do not poll. Otherwise poll `gh pr checks <n>` in the background, at most 30 times, 60 seconds apart, until none are pending. If checks are still pending after 30 polls, report that and stop. A check on a superseded commit stays `in_progress` forever, so never wait on one.
2. Read every new review comment since your last pass: `gh api repos/{owner}/{repo}/pulls/<n>/comments` plus `gh pr view <n> --comments`.
3. Triage each finding. Bot claims are often right about the location and wrong about the rationale — verify empirically (read the code, run the test, reproduce) before you touch anything.
   - **Real** → fix it.
   - **Wrong or out of scope** → do not change code. Draft a short reply saying why, and leave it pending (see **Pending replies**).
4. Fix every failing blocking check. Failures caused by your own commits are yours.
5. Validate locally before pushing: run the repo's type check, the affected tests, and the linter on touched code.
6. Commit as a fixup on the same branch and push. Never rebase or force-push a pushed PR. Go back to step 1.

## Blocking vs non-blocking

Blocking — must be green: type checks, lint, unit tests, builds, and any check the repo marks required.

Non-blocking — report the status, do not block on it, do not chase flakes: e2e checks, anything named `interactive`, anything `skipping`.

If a non-blocking failure is plainly caused by this PR's change, fix it. If it looks like an unrelated flake, say so with the evidence and move on.

## Exit criteria

Stop when all four hold:

- Every security finding is fixed or noted.
- Every blocking check passes on the latest commit.
- Every legitimate bot finding is either fixed or has a pending reply explaining the dismissal.
- No new comments have landed since your last pass.

## Pending replies

Put every reply in one pending review. Omitting `event` keeps it pending:

```bash
gh api -X POST repos/<owner>/<repo>/pulls/<n>/reviews --input - <<'JSON'
{"comments":[{"path":"src/file.ts","line":118,"side":"RIGHT","body":"..."}]}
JSON
```

Confirm the response says `"state": "PENDING"`. Never use `gh pr review`: it submits at once, and a submitted review cannot be made pending again.

## Boundaries

- **Never submit a review or a reply.** Everything stays pending — the author presses send.
- Never merge the PR.
- Do not expand scope: fix what CI and the reviewers flag, nothing adjacent.
- Stop and ask only if you are genuinely blocked — an infra failure you cannot act on, a finding that needs a product decision, or CI that will not run.

## Final report

One block: blocking checks status, each finding with fixed / dismissed-with-reason, commits pushed, the non-blocking failures worth a glance, and each stacked PR you merged into (each needs its own run).
