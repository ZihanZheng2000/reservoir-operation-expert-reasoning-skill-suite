# Prompt: generate the large patterns in one pass

Give this whole file to one agent, with `[V3]` and `[OUTPUT]` filled in. It produces large-pattern definitions in the format of `large-patterns.md` in one pass. It was reconstructed from the version history (`history/`): the grouping method follows the AI draft, the writing rules in section 4 encode the user's rewrite of that draft, and the rule on method choice (section 2, item 5) covers the pattern the user added later (RP08).

---

You are a researcher in reservoir operation for flood risk management, building a taxonomy of how researchers in this field reason and work.

## 1. Inputs

- `[V3]/02-patterns/01-steps/reasoning-steps.md`: titles of the 344 reasoning steps (R1, R2, … per paper) from 50 papers (E01–E50).
- `[V3]/02-patterns/01-steps/execution-steps.md`: titles of the 416 execution steps (E1, E2, … per paper).
- `[V3]/02-patterns/01-steps/step-inventory.csv`: every step with its full description (`step_description`, `retained_details`, `evidence_boundary`).

Topic of the corpus: **Reservoir operation adjustment for flood risk management.** Reasoning steps record the judgments that motivate the authors' choices; execution steps record the concrete work they did.

Read only these files. Do not read other folders, earlier pattern versions, skills, or papers V01–V05.

## 2. Task

Group the steps into cross-paper **large patterns**, separately for reasoning and for execution.

1. Read all step titles of one layer first. Group them by the **function** the step serves in the study, not by method name, paper section, or wording. Two steps with different methods (for example a copula and a scenario tree) belong together if they do the same job.
2. When a title is method-specific, ambiguous, or does several things, read its description in `step-inventory.csv` before placing it.
3. A pattern must recur across papers. Keep a pattern that appears in only a few papers when it is a distinct, recognizable part of practice (for example operational consultation and pilot implementation).
4. Choose the granularity at which each **reasoning** pattern is one distinct expert judgment (one question an expert must settle) and each **execution** pattern is one distinct work package (one deliverable). Do not split a judgment by method, and do not merge two judgments because they often co-occur. In this corpus this usually gives about 9 reasoning and 11 execution patterns.
5. **Method choice is its own reasoning pattern.** Steps that justify why a particular model representation or solution method is used (for example an analytical derivation, a stochastic differential equation, a Bayesian network, a genetic algorithm, an aggregated reservoir, a scenario tree of a given size) are a distinct judgment. Do not fold them into uncertainty, trade-off, or evidence patterns.
6. Order the patterns by their typical position in a study: for reasoning, from diagnosing the problem with the current rule, through uncertainty, forecasts, risk, feasibility, trade-offs, adaptive logic and method choice, to judging the evidence; for execution, from data and baseline, through forecasts, uncertainty, simulation, bounds, solving, risk calculation and selection, to staged actions, testing and adoption. Adjust the order if the steps show otherwise.
7. Patterns do not have to appear in every paper and do not form a fixed sequence.

## 3. Output

Write `[OUTPUT]` in English with exactly this structure:

```
# Large patterns: N reasoning and M execution patterns

<one paragraph: 50 papers analyzed; per paper, the research problem, the reasoning behind the authors' choices,
and the execution workflow were extracted; average reasoning and execution steps per paper (computed from the
inputs); similar functions grouped into N reasoning and M execution patterns>

## Reasoning patterns

| ID | Candidate category | Shared question |
| --- | --- | --- |
| RP01 | ... | ... |

## Execution patterns

| ID | Candidate category | Shared task |
| --- | --- | --- |
| EP01 | ... | ... |

## Example steps

<for each pattern, 3–5 step IDs with titles that show its range, for example "E01 R3: Use lead time and release
capacity to define an admissible upper level">
```

## 4. Writing rules

**Names (Candidate category)**

- Start with a verb that fits the function.
  - Reasoning: verbs of expert judgment, such as *Diagnose*, *Identify*, *Judge*, *Justify*, *Frame*, *Consider*, *Select*. Use *Judge* when the expert decides whether something holds (is the forecast reliable enough, is the adjustment feasible, what does the evidence support); use *Justify* when the expert must set and defend a standard (what counts as unsafe, what risk is acceptable).
  - Execution: verbs of work, such as *Prepare*, *Develop and verify*, *Model*, *Calculate*, *Solve for*, *Organize … and select*, *Translate*, *Compare and test*, *Conduct*.
- Anchor every name in the domain. Say where the judgment or work sits in reservoir flood operation: "under flooding risk", "for reservoir flood-operation decisions", "across flood-event stages", "of candidate operating plans". A name that would fit any research field is not acceptable (method choice is the one exception, since it is about representation and solution).
- No method names (Monte Carlo, copula, MPC, TOPSIS) in names.

**Shared question (reasoning)**

- Write the question a reservoir operator or flood hydrologist would actually ask, in plain language.
- When the judgment has several concrete parts, split it into short sub-questions.
- Name the concrete quantities involved (lead time, storage, release capacity, downstream thresholds, flood stage).

**Shared task (execution)**

- One verb-led sentence (or two short clauses) saying what is done and what it produces.
- Name the concrete objects: water levels, storage, releases, downstream flows, release schedules, rule parameters, flood risk, losses, benefits.
- Write it per candidate operating plan or per study where relevant ("For each candidate operating plan, calculate …").
- Methods may appear only as a short list of alternatives ("optimization, analytical derivation, enumeration, or calibration").

**What not to write in the tables**

- No coding instructions or methodological caveats (for example "keep each metric's definition", "do not merge risk indicators with real losses", "check the description before coding").
- No step examples inside the tables (they go in the example-steps section).
- No claims of frequency or validation.

**Style examples** (one row each; follow the style, not the content):

| ID | Candidate category | Shared question |
| --- | --- | --- |
| RPxx | Judge physical and operational feasibility of reservoir adjustments | Is there enough forecast lead time to adjust reservoir operations? Is there enough storage and release capacity? Can adjustments be made without violating downstream safety constraints? |

| ID | Candidate category | Shared task |
| --- | --- | --- |
| EPxx | Calculate risks, losses, and benefits of candidate operating plans | For each candidate operating plan, calculate reservoir and downstream flood risk, potential flood losses, and benefits associated with other reservoir objectives. |

## 5. Self-check before saving

- Every pattern groups steps from several papers by function; no pattern is a single method.
- Reasoning and execution patterns are kept separate; a reasoning pattern is a judgment, an execution pattern is work.
- Method-choice reasoning has its own pattern.
- Every name starts with a fitting verb and is anchored in reservoir flood operation.
- Questions are plain and concrete; tasks name what is produced.
- The tables contain no caveats, coding instructions, or step examples.
- The step averages in the opening paragraph are computed from the inputs.

Save as UTF-8 and reply with the output path and the number of reasoning and execution patterns.
