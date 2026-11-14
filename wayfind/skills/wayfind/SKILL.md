---
name: wayfind
description: Turn a loose, foggy idea into a plan by naming the destination and resolving the open decisions one at a time, recording everything in a single markdown doc. Use when the way from here to the goal is not visible yet and the work is too big to just start.
disable-model-invocation: true
---

An idea has arrived, too big and too foggy to start on: the way from here to the **destination** is not visible yet. Wayfinding finds that way. It does not charge at the destination.

The whole effort lives in **one markdown doc**. You name the destination, list the decisions standing between here and there, then resolve them one at a time until nothing is left to decide.

## Plan, don't do

Every open question resolves into a **decision**, not a deliverable. The doc is done when the way is clear — someone can pick it up and build without asking anything.

The pull to just start coding is the signal you have reached the edge of the plan and it is time to hand off. The user can override this in **Notes**; absent that, produce decisions.

## The doc

One markdown file. Ask the user where it goes; default to `docs/plans/<slug>.md`, or `PLAN.md` in the working directory if there is no `docs/`.

```markdown
# <name of the effort>

## Destination

<what the end of this plan looks like — the spec, decision, or change this is finding its way to. One or two lines. Re-read it before choosing what to work on next.>

## Notes

<domain context; skills to consult each session; standing preferences for this effort>

## Open questions

- [ ] **<sharp question>** — <type> — <one line of why it matters>
- [ ] **<sharp question>** — <type> — blocked by: <other question>

## Decisions

- **<the question>** — <the answer, in a line or three. Enough that nobody has to re-derive it.>

## Not yet clear

- <a question you can tell is coming but cannot phrase sharply yet>

## Out of scope

- <thing ruled out> — <why it sits past the destination>
```

Open questions carry a type: `research`, `prototype`, `conversation`, or `task` (see below). Blocked questions say what blocks them; a question is takeable when everything blocking it has moved to **Decisions**.

Keep answers in **Decisions**, not scattered. If resolving a question produces an artifact — a prototype, a spike branch, a doc — link it from the decision rather than pasting it in.

## Question types

- **Research** — read docs, third-party APIs, or the codebase to surface a fact a decision waits on. The agent does this alone. Spin up a subagent when the reading is wide.
- **Prototype** — make something cheap and concrete to react to: an outline, a stub, a rough UI. Use when "how should it look" or "how should it behave" is the real question. Needs the human in the loop.
- **Conversation** — talk it through with the user, one question at a time, via `/grilling`. The default. Needs the human in the loop; never answer on their behalf.
- **Task** — manual work that has to happen before a decision is possible: signing up for a service so its API can be judged, provisioning access, moving data so its shape is visible. The one type that *does* rather than decides, and it earns that by unblocking a decision. Do it yourself where you can; otherwise hand the user a precise checklist. Record what was done and any facts later questions depend on.

## Fog

The plan is deliberately incomplete. Do not chart what you cannot see yet. Beyond the open questions sits fog: decisions you can tell are coming but cannot pin down, because they hang on questions still open. Resolving a question clears the fog ahead of it.

**Open question or fog?** The test is whether you can state the question precisely *now* — not whether you can answer it now.

- **Open question** when it is already sharp, even if it is blocked.
- **Not yet clear** when you cannot phrase it that sharply. Do not pre-slice fog into question-sized pieces; one patch may become three questions later, or none.

## Out of scope

The destination fixes the scope. Work past it is not fog — it never becomes clear enough to take, because the frontier stops at the destination.

When something already on the list turns out to sit past the destination, delete it from **Open questions** and leave one line in **Out of scope** with the reason. It does not go in **Decisions** — that section records the route actually walked, and a scope boundary is not a step on it.

Out-of-scope work comes back only if the destination is redrawn, and then as a fresh effort.

## How to run it

### Chart

The user arrives with a loose idea.

1. **Name the destination.** Use `/grilling` to pin down what this is finding its way to. Scope is settled first, because it shapes every question after it.
2. **Map the frontier.** Grill again, **breadth-first** — fan out across the whole space instead of going deep on one thread. Surface the open decisions and what is takeable right now.
3. **If nothing is foggy, stop.** The way is already clear and the effort fits in one sitting. Say so and ask how the user wants to proceed instead of writing a plan nobody needs.
4. **Write the doc.** Destination and Notes filled in, Decisions empty, sharp questions listed with types and blockers, everything blurrier written into **Not yet clear**.
5. **Run the research questions now** if there are any — they are the cheap ones, and their answers usually sharpen the fog. Everything else waits.
6. **Stop.** Charting is its own piece of work. It resolves nothing by hand.

### Work through it

The user arrives with the doc, and maybe a specific question.

1. Read the doc. Re-read the **Destination**.
2. Pick the question. If the user named one, take that. Otherwise take the first unblocked open question.
3. Resolve it. Invoke whatever the **Notes** section names. When in doubt, `/grilling`.
4. Update the doc: move the question into **Decisions** with its answer, add any newly sharp questions, and clear graduated patches out of **Not yet clear** so each lives in exactly one place. If the answer put something past the destination, move it to **Out of scope**. If it invalidated other questions, rewrite or delete them.
5. Say what is now takeable and ask whether to keep going. Resolve one question at a time — research questions are the exception, since they are cheap and non-committal.
