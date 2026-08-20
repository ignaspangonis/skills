---
name: until-green
description: Own the post-push loop on a PR. Watch CI, triage review-bot comments, fix real issues, repeat until every blocking check is green. No check-ins.
argument-hint: "[pr-number] (defaults to the PR for the current branch)"
disable-model-invocation: true
---

Take the PR **$ARGUMENTS** (if empty, resolve it from the current branch with `gh pr view --json number`) to a landable state without involving me. Do not end your turn to report "CI is running" or "expect more bot comments" — that is the babysitting this skill exists to remove.

## Loop

Repeat until the exit criteria below hold:

1. `gh pr checks <n> --watch --interval 60` in the background. Wait for it. Always watch the latest commit — a check on a superseded commit stays `in_progress` forever.
2. Read every new review comment since your last pass: `gh api repos/{owner}/{repo}/pulls/<n>/comments` plus `gh pr view <n> --comments`.
3. Triage each finding. Bot claims are often right about the location and wrong about the rationale — verify empirically (read the code, run the test, reproduce) before you touch anything.
   - **Real** → fix it.
   - **Wrong or out of scope** → do not change code. Draft a short reply saying why, and leave it pending.
4. Fix every failing blocking check. Failures caused by your own commits are yours.
5. Validate locally before pushing: run the repo's type check, the affected tests, and the linter on touched code.
6. Commit as a fixup on the same branch and push. Never rebase or force-push a pushed PR. Go back to step 1.

## Blocking vs non-blocking

Blocking — must be green: type checks, lint, unit tests, builds, and any check the repo marks required.

Non-blocking — report the status, do not block on it, do not chase flakes: e2e checks, anything named `interactive`, anything `skipping`.

If a non-blocking failure is plainly caused by this PR's change, fix it. If it looks like an unrelated flake, say so with the evidence and move on.

## Exit criteria

Stop when all three hold:

- Every blocking check passes on the latest commit.
- Every legitimate bot finding is either fixed or has a pending reply explaining the dismissal.
- No new comments have landed since your last pass.

## Boundaries

- **Never submit a review or a reply.** Everything stays pending — the author presses send.
- Never merge the PR.
- Do not expand scope: fix what CI and the reviewers flag, nothing adjacent.
- Stop and ask only if you are genuinely blocked — an infra failure you cannot act on, a finding that needs a product decision, or CI that will not run.

## Final report

One block: blocking checks status, each finding with fixed / dismissed-with-reason, commits pushed, and the non-blocking failures worth a glance.
