---
name: save-tokens
description: Run this session on a small token budget. Delegate legwork to subagents on cheaper models like Sonnet and keep the interfaces between agents small.
disable-model-invocation: true
---

The main session runs an expensive model. Don't spend its tokens on work a cheaper model does just as well.

Delegate to a `model: sonnet` subagent any step whose output would flood this context: reading many files, broad searches, investigating, running tests and digesting output, mechanical multi-file edits. Use `haiku` for trivial steps. Keep here only what needs the full conversation or top-model judgment: choosing direction, weighing tradeoffs, refining, final synthesis.

Keep interfaces small. Brief in: exact scope, paths, what done means, the shape of answer you want. Answer out: conclusions with `file:line` pointers, not transcripts. Send independent briefs in one message so they run in parallel. When a result is thin, continue the same agent with a tighter brief instead of redoing the work here.
