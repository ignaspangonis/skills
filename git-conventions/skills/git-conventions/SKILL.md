---
name: git-conventions
description: Must read before creating or naming a branch, stacking branches, or writing a PR title.
---

My personal naming conventions. These apply in every repo. If a repo's own committed
git skill says something different about naming, this file wins — it is my preference,
not the repo's.

For git mechanics (how to branch off mainline, commit, push, resolve conflicts), use the
repo's own git skill. This file only covers names.

## Branch prefixes

Two prefixes, no others:

- `fix/` — bugfixes and hotfixes only. Correcting behaviour that is already wrong.
- `feature/` — everything else: new product work, refactors, migrations, modularisation,
  one-off technical work.

Do not invent `refactor/`, `chore/`, `docs/`, or `test/`. Refactors are `feature/`.

Use kebab-case after the prefix: `fix/checkout-double-submit`, `feature/complaints-assets`.

## Chained branches (stacked PRs)

When branches stack, they share one base name and get a numeric suffix instead of each
having its own name. The numbers show the order, which is what makes a chain readable:

```
feature/item-details-svc-1
feature/item-details-svc-2
feature/item-details-svc-3
```

- Number from the bottom of the stack up. `-1` sits on mainline, `-2` on `-1`, `-3` on `-2`.
- Do not give each link a separate descriptive name. `feature/item-details-svc-experiment-gate`
  followed by `feature/item-details-svc-section` hides the order — that is the thing this
  rule exists to prevent.
- Only number when a chain actually exists. A standalone branch keeps a plain name, no suffix.
- Adding a link later: take the next number and branch off the current top of the stack.

## PR titles

`<Sentence-case description> [TICKET-123]`

Example: `Add item_id details to favourite click events [IE-112]`

No conventional-commit prefixes — not `feat(scope):`, not `fix:`.

Each PR in a chain gets a title describing its own change. Do not put the branch's
number in the title.
