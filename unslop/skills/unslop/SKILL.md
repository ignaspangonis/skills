---
name: unslop
description: Cut AI tells from any writing. Must always apply.
---

# Unslop

Remove AI patterns, add human voice. Keep every fact from the source; cut wording, not information. Preserve intended tone. Finish with a self-audit: "What makes this obviously AI generated?" Fix what's left.

## Add soul

Sterile writing is as obvious as sloppy writing. Have opinions instead of neutrally listing pros and cons. Vary sentence length. Use "I" when it fits. Be specific: not "this is concerning" but "agents churning away at 3am". Perfect structure looks machine-made, so let some mess in.

Specificity comes from the source, never from you. If the source has no concrete detail, cut the vague sentence instead of inventing a concrete one. Never add facts, dates, history, or commitments the original doesn't contain.

Uniform certainty is as machine-made as stacked hedging. Mark claims the author inferred rather than verified ("as I understand", "as I can see", "if so") and let verified facts stand plain. One hedge per claim.

## Cut these words

- Puffery and AI vocabulary: pivotal, testament, delve, crucial, showcase, underscore, tapestry, landscape (abstract), vibrant, breathtaking, groundbreaking, renowned, nestled, stunning, fostering, intricate, enduring, garner, interplay, enhance, additionally, must-visit. State what happened in plain words.
- Abstract metaphor nouns: substrate, wedge, vector, nexus, locus, primitive, harness, bedrock, scaffolding, modality, paradigm, flywheel, north star, endgame, ratchet, gold-plating. Use the concrete word: "substrate" is "base", "wedge in" is "add".
- Coined category nouns ("every layout shape we have", "the surface area of the change"). Use the plain word: "everywhere", "what changed".
- Coined shorthand ("fresh-mount nav") and generic stand-ins ("the transition", "placeholders"). Name the artifact with the reader's word, the file, flag, or team term ("loading.tsx", "skeletons"), even when longer.
- Fancy synonyms: utilize is "use", leverage is "use", facilitate is "help", numerous is "many". "Serves as", "stands as", "boasts", "features" are "is" or "has".
- Filler: "in order to" is "to", "due to the fact that" is "because", "it is important to note that" gets deleted.

## Cut these constructions

- "Not just X, but Y". State the point directly.
- Rule of three. Use the natural number of items.
- False ranges ("from X to Y" with no real scale). List the topics.
- Synonym cycling. Pick one word and repeat it.
- Vague attribution ("experts believe", "reports suggest"). Name the source or delete.
- Name-dropping media outlets without context. Pick one, say what it said.
- Superficial -ing tails ("...highlighting the importance of"). Delete or expand with facts.
- Formulaic arcs ("despite challenges... continues to thrive", "the future looks bright"). Specific facts only.
- Stacked hedging ("could potentially possibly"). One "may" is enough.
- Argument meta-narration ("My point is...", "To be clear...", "In other words..."). Make the point with a plain connective: "but", "still".
- Adverbs propping up weak verbs ("significantly improves"). Stronger verb or the measured number.
- Passive voice. Name the actor ("the compiler validates queries") unless the actor truly doesn't matter.
- Dense sentences. If the reader backtracks to parse it, split it. One idea per sentence.

## Style

- No em dashes or en dashes as clause glue. End the sentence or use a comma.
- Parentheses only for a short aside that adds standing or a cross-reference ("(from the other thread)"), never as a dash substitute grafting a clause.
- Arrows only as domain notation ("item page → catalog"), never as a prose connective ("A → B → fails").
- Colons only before a list or example, never as mid-sentence connectors.
- Sentence case headings. No decorative emojis. Straight quotes.
- Don't bold every proper noun. A bold label that restates its line ("**Performance:** performance improved...") becomes prose; a bold lead-in followed by genuinely new detail is fine.

## Replies in threads

- State your standing first when it changes how the reply lands ("I approved the RFC, so this is not blocking").
- Quote the line you answer with ">" instead of paraphrasing it.
- No numbered question lists. Fold the ask into one hedged sentence: "Not sure which layout.tsx you plan to test, perhaps worth noting in the RFC."
- One point per message. Don't pre-answer follow-ups with metrics, options, or contingencies. "Worth its own measurement later" leaves the door open; the details wait for the question.

## Communication artifacts

- No chatbot phrases ("Hope this helps!", "Great question!", "Certainly!"). Respond directly.
- No cutoff disclaimers ("while specific details are limited..."). Find sources or cut.

## Plain speech

Say what it does, not how it feels. "SQL you can read" names a feeling; the fix names the mechanism or a number. If a sentence can't be restated as a concrete instruction, fact, or number, or could appear unchanged in another project's docs, cut it.
