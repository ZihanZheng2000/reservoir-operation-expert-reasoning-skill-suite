# Prompt: write the reference file for one skill unit

Give this whole file to one agent per unit, with `[UNIT]`, `[EVIDENCE]` and `[OUTPUT]` filled in. One agent per unit; agents do not share context.

---

You are writing one reference file of a skill for expert work on reservoir operation under flood risk. The skill is organized in units; each unit pairs an expert judgment with a piece of research work, and lists one check question per small pattern. This reference file is what an agent reads when it works on unit `[UNIT]`: it gives the concrete methods that research papers used for each small pattern.

The agent using the skill reasons with its own expertise first. This file **supplements and checks** that reasoning: it shows what the papers did, under which conditions, and with which limits. It is not a recipe to follow.

## Input

`[EVIDENCE]`: for every small pattern of this unit, the paper steps assigned to it, each with its full card text (description, retained details, evidence boundary). Step IDs look like `E05-R3` (paper E05, reasoning step 3) or `E05-E4` (execution step 4).

Read only this file. Read all of it before writing. Do not read papers, other evidence files, other skill files, or earlier skill versions.

## Task

For each small pattern, in the order of the input, write a section with:

1. **When papers did this**: the triggers or conditions under which the papers took this step (from the triggers and descriptions).
2. **How**: the concrete methods, procedures, and formulas the papers used, each followed by the step IDs that support it. Group papers that did the same thing; keep different approaches apart.
3. **Choosing between approaches**: when papers took different approaches, the conditions under which each was used, as far as the evidence shows. Leave this out if there is only one approach.
4. **Limits and gaps**: what the papers report as limits, assumptions, or things not done, and what the cards mark as unreported or unclear (from the evidence boundaries).
5. **Example values** (only when useful): concrete numbers from a paper, each labelled with its step ID, as examples of scale, not as defaults.

## Rules

- **Only the evidence.** Every statement must come from the input and carry at least one step ID. Do not add methods, checks, standards, formulas, or advice from your own knowledge, even if you are sure they are correct. If something important seems missing, do not fill it in.
- **Keep each paper's own definitions and notation.** Papers differ in sign conventions, units, definitions of risk, and names of levels. Do not merge different definitions into one; when papers differ, say so and show each version with its step IDs.
- **No generalization beyond the evidence.** Say "E12 and E30 did X", not "X is standard practice". Counts of papers are fine.
- **Formulas** only as reported in the cards, with their variables defined as the cards define them. If a card mentions an equation without giving it, say that the equation is in the paper (for example "Eq. (5) in E01") rather than reconstructing it.
- **Unclear evidence** stays unclear: mark it as such.
- Plain, concise English. Use bullet lists. About 100–400 words per small pattern, depending on how much evidence there is; do not pad thin patterns.
- Do not copy whole card passages; summarize them.

## Output

Write `[OUTPUT]` in English with this structure:

```
# Reference for unit [UNIT]: what the papers did

<two sentences: what this file covers, and that it summarizes N steps from M papers; use it to find concrete
methods and to check an approach; values are examples from specific papers, not defaults>

## <small-pattern ID> <small-pattern name>

**When papers did this** ...
**How** ...
**Choosing between approaches** ...   (only if several approaches)
**Limits and gaps** ...
**Example values** ...                 (only if useful)

## <next small pattern> ...
```

Before saving, check: every bullet has a step ID; no statement comes from outside the input; every small pattern of the input has a section; differing definitions are kept apart.

Save as UTF-8 and reply with the output path and any evidence you found contradictory or unclear.
