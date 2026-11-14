---
name: writing-prs
description: Must read before writing or editing a PR description.
---

A length gate for PR descriptions. Prose rules alone do not keep a body short; a budget you count against does.

Budget the body:

- `## Context` — at most 2 sentences, covering why the change is needed.
- `## This PR` — prose, at most 3 sentences. Use prose when the changes are related, even when the PR does several things; use bullets only when they are not related. For a refactor or a change in which component owns what, a `diff` block of the component or call tree, at most 8 lines, may replace sentences. It shows the shape, not a file list.
- `**Risk:**` — one line after `## This PR`, only for a one-way door (a data or storage format change, a removed API field, tracking event or flag) or a blast radius beyond the pages the diff renders. Name the door and what could break. Most PRs have none.
- `## Screenshots` — only when the screenshots rule below applies.
- On a bug fix, `## Problem` and `## Solution` replace `## Context` and `## This PR`, with the same budgets.
- Team mention on the last line, when the repo uses one.
- No other headings, and nothing after the mention.

## Screenshots

When the diff changes what a page renders, add `## Screenshots` with a Before | After table: same page, state and viewport in each pair.

When the diff renders nothing different (types, test ids, a pure move), make `## Screenshots` the single line `No visual change: <reason>`.

## Author comments

Once the PR exists, leave a pending line comment wherever a reviewer would stop: unclear logic, a choice over an obvious alternative, a workaround. At most 5, one or two sentences each. None is fine.

Post them as one pending review. Omitting `event` keeps it pending, so nothing is sent until you submit it in the GitHub UI:

```bash
gh api -X POST repos/<owner>/<repo>/pulls/<n>/reviews --input - <<'JSON'
{"comments":[{"path":"src/file.ts","line":118,"side":"RIGHT","body":"..."}]}
JSON
```

Never use `gh pr review`: it submits at once.

## Body rules

Bullets are the exception, not the format. Use them only when the changes are not related and cannot be read as one story — then at most 3. A list of 4 bullets is the signal you narrated the diff.

Collapse a bullet list by picking the change that matters and folding the rest in as clauses:

```
Bad — one bullet per diff area:
- Adds the `natural_language_search` flag and reads it in `SearchBar`.
- Swaps the item placeholder to "Describe what you're looking for".
- Adds `NaturalLanguageSearchTooltip`, shown once per calendar day per browser.
- Tooltip closes on typing, blur, submit, outside click or a tap on itself.

Good — lead change, rest as clauses:
Adds `NaturalLanguageSearchTooltip`, shown once per calendar day per browser.
Gated behind a `natural_language_search` flag. Also swaps the item
placeholder to "Describe what you're looking for".
```

The dismissal triggers went because they are diff contents. The flag went from its own bullet to three words.

Cut before submitting. Delete any line that is:

- Contents of the diff — file paths, the rules or options a new file adds, names of things added. The reviewer opens the diff for that. The tree sketch above is the one exception.
- Rationale for a decision nobody challenged, including why this approach beat an alternative discussed in chat.
- Verification you ran — tests, checks, regenerated output matching. That belongs in the chat reply.
- An answer to something the user asked you. The PR has a different audience than the conversation.

Re-read this file when you compose the body, not only at task start. Reading it early and writing many steps later is how the budget gets missed.

Count sentences and bullets against the budget immediately before `gh pr create` or `gh pr edit`. Over budget means cut, not reword.
