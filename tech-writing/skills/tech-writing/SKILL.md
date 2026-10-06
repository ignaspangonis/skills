---
name: tech-writing
description: Write or edit text by Google's technical writing rules. Use for docs, READMEs, design docs, RFCs, guides, runbooks, specs, skills, AGENTS.md or CLAUDE.md files, and any request to make text clearer, shorter, or easier to read.
---

# Tech writing

Every sentence tells the reader something new they need.

- **Once.** Say each idea in one place. When a new sentence restates an earlier one, merge them. Skip intros that preview the body and summaries that repeat it.
- **Short.** Cut words that carry no meaning: "in order to" → "to", "is able to" → "can", "it is important to note that" → cut. Pick one plain word over a phrase.
- **Concrete.** Name the exact thing: a number, command, file, role, or example. Swap vague nouns ("legwork", "things", "issues", "handling") and vague modifiers ("fast", "robust", "significantly", "various") for the specific one the source gives. Define a needed term in one clause at first use.
- **Point first.** The first sentence of each section and paragraph states its point.
- **Faithful.** Keep every fact and example from the source. Add none.
- **Runnable.** Every command works exactly as pasted. Quote shell metacharacters (`<`, `>`, `|`, `$`), even when the source leaves them bare. Write placeholders as `<like-this>` and say what replaces them.
- **Branches.** In steps, each check says what to do for every outcome: pass, fail, or none found.

## Self-edit

Reread twice. First pass: find every sentence that repeats an earlier one, and merge. Second pass: cut every empty word, and swap every vague term for a concrete one. Cut words, not content.
