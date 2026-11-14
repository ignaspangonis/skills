# skills

Skills I created and use daily, packaged as a plugin marketplace.

## Install

In Claude Code:
```
/plugin marketplace add ignaspangonis/skills
/plugin install <name>@ignaspangonis-skills
```

Or copy any `<name>/skills/<name>` folder into `~/.agents/skills/` or `~/.claude/skills/`.

## Skills

| Skill | Invoke | What it does |
|---|---|---|
| `save-tokens` | `/save-tokens` | Runs the session on a small token budget. Delegates legwork to subagents on cheaper models and keeps interfaces between agents small. |
| `unslop` | `/unslop` or auto | Cuts AI tells from writing: puffery, filler, em dash overuse, chatbot phrases. Then adds voice back. |
| `grilling` | `/grilling` or auto | Interviews you relentlessly about a plan or decision, one question at a time, until you reach shared understanding. |
| `tech-writing` | `/tech-writing` or auto | Writes and edits docs by Google's technical writing rules: says each idea once, cuts empty words, swaps vague terms for concrete ones, keeps commands safe to paste. |
| `until-green` | `/until-green [pr]` | Owns the post-push loop on a PR: runs a security pass, keeps stacked PRs in sync by merge, watches CI, triages review-bot comments, fixes real issues, repeats until every blocking check is green. Drafts replies but never submits them, never merges. |
| `writing-prs` | auto | Holds a PR description to a budget: two sentences of context, three of change, no narrating the diff. Leaves author comments as a pending review. |
| `wayfind` | `/wayfind` | Turns a foggy idea into a plan. Names the destination, lists the decisions in the way, and resolves them one at a time in a single markdown doc. |
| `grill-board` | `/grill-board [board url]` | Moves grilling onto a shared claude.ai decision board. The team answers each round of questions as tickets; the next run folds the decisions in and posts the next round. Needs Claude's Artifact tools. |
| `listen` | `/listen [show] \| again \| stop` | Reads the current problem or open question aloud: where we are, the options, the pick, the question. `show` renders it as a page with diagrams instead. **macOS only**: it uses `say` and `afplay`. |
| `git-conventions` | auto | An example, not a standard: my branch prefixes, numbered stacked branches, and PR-title format. Fork it and put in your own rules. |

## License

MIT
