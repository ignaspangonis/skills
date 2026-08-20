# skills

Claude Code skills I created and use daily, packaged as a plugin marketplace.

## Install

```
/plugin marketplace add ignaspangonis/skills
/plugin install <name>@ignaspangonis-skills
```

Or copy any `skills/<name>` folder into `~/.claude/skills/`.

## Skills

| Skill | Invoke | What it does |
|---|---|---|
| `save-tokens` | `/save-tokens` | Runs the session on a small token budget. Delegates legwork to subagents on cheaper models and keeps interfaces between agents small. |
| `unslop` | `/unslop` or auto | Cuts AI tells from writing: puffery, filler, em dash overuse, chatbot phrases. Then adds voice back. |
| `grilling` | `/grilling` or auto | Interviews you relentlessly about a plan or decision, one question at a time, until you reach shared understanding. |
| `until-green` | `/until-green [pr]` | Owns the post-push loop on a PR: watches CI, triages review-bot comments, fixes real issues, repeats until every blocking check is green. Drafts replies but never submits them, never merges. |

## License

MIT
