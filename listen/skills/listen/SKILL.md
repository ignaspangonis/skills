---
name: listen
description: Use when the user runs /listen to hear the current problem or open question read aloud.
disable-model-invocation: true
argument-hint: '[show] [focus] | again | stop'
---

- `<base>` below is this skill's base directory. Use its absolute path in every command.
- If `$ARGUMENTS` is `stop`, run `<base>/speak.sh --stop` and end the turn.
- If `$ARGUMENTS` is `again`, run `<base>/speak.sh --again` and end the turn.
- If `$ARGUMENTS` starts with `show`, follow **Show it**. Otherwise follow **Speak it**.
- Cover the latest open problem or question in this conversation. If `$ARGUMENTS` names a focus, cover only that.
- Do **not** run any other tool or change any file. This turn only explains.

## Script content

Follow this order. Each part is one to three sentences.

1. Where we are: the task and the step we reached.
2. The problem: what blocks us or what is unclear, and why it matters.
3. The options: at most three. For each, say what happens if we pick it.
4. My pick and the one reason for it.
5. The question: the exact thing the user must answer. Start with "So, my question is".

If there is no open question, replace parts 3 to 5 with what happens next and whether the user needs to do anything.

## Script style

- Keep the whole script between 80 and 220 words.
- Write for the ear: short sentences, one idea per sentence, plain everyday words.
- Use the words the user already uses for things. Explain any new term in the same sentence.
- Do **not** read code, file paths, URLs, commit hashes, flags, or symbols. Name things by what they do: "the item page test file", "the sold-out flag".
- Do **not** use markdown, lists, brackets, quotes, or emoji. Write numbers and acronyms the way a person says them.
- Use ordinal words to signal structure: "First option", "Second option".

## Speak it

- Pipe the script through a quoted heredoc:

```bash
<base>/speak.sh <<'EOF'
<script>
EOF
```

- After the command returns, print the same script as plain text so the user can read along, then one line: `Say /listen again to replay, /listen stop to stop.`

## Show it

- Split the script into one section per part. Give each section a `kind`: `context`, `problem`, `options`, `pick`, `question`, or `next`.
- Put the spoken part in `say`, following **Script style**.
- Put the visual part in `show` as markdown. Show what is hard to hear: exact names, paths, short code, numbers.
- Do **not** repeat `say` word for word in `show`. Keep each `show` under 12 lines.
- For `options`, use a table: one row per option, columns for what changes, cost, and risk.
- When a flow, call chain, or before/after helps, add one ` ```mermaid ` diagram in the section where it helps most. Keep it under 10 nodes.
- Pipe the JSON through a quoted heredoc. The command opens the page in the browser and prints its path:

```bash
/usr/bin/python3 <base>/render.py <<'EOF'
{"title": "<short title>", "sections": [{"kind": "context", "say": "<spoken>", "show": "<markdown>"}]}
EOF
```

- After the command returns, print the page path and one line: `Press space on the page to play or pause.`
