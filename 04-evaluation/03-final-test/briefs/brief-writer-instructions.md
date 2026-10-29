# Instructions for writing a simple and a detailed problem brief

You write two problem briefs for one published study of reservoir flood operation. Experts will write a study design from each brief without seeing the paper. Judges compare their designs with the paper's own route. A brief must therefore give the setting, system, data and problem, but never the paper's method, findings or result values.

Base folder B = "D:/Auto Research/human-gated-ai-research-framework/research/reservoir-operation-expert-reasoning-skill-suite/artifacts/run-20261028-v3-rebuild/work/10-final-test".
Paper text folder P = "D:/Auto Research/human-gated-ai-research-framework/research/reservoir-operation-expert-reasoning-skill-suite/artifacts/run-20260914-0925-50paper-patterns/01-corpus/heldout-5/text".

## Read only these files

1. `P/{paper}.txt`, the full paper text.
2. `B/briefs-old/{paper}-brief.md`, the existing brief (about 320 words).
3. `B/briefs-old/{paper}-reference.md`, the paper's route. Read it only to know what you must NOT reveal.
4. The approved examples for paper V01, which set the format and level of detail:
   - `B/briefs-draft/V01-brief-simple.md`
   - `B/briefs-draft/V01-brief-detailed.md`

Do not open any other file or folder.

## Simple brief: `B/briefs-draft/{paper}-brief-simple.md`

- Title line: `# Problem Brief {paper}: <system name>`.
- Exactly two paragraphs, about 120–150 words in total:
  - **Background.** The system and its purposes, the one or two facts that define the problem, and what data are available, including the period.
  - **Research question.** One or two questions stating what the study must find out, then one sentence asking for a study design.
- Leave out sub-questions, risk definitions, objectives lists, and most numbers. The expert should have to work out for themselves what must be settled, and state assumptions where values are missing.

## Detailed brief: `B/briefs-draft/{paper}-brief-detailed.md`

- Use the same five numbered sections as the V01 example:
  1. Background
  2. System characteristics (a table)
  3. Current operation and constraints
  4. Data available
  5. Research question
- Length: about 450–550 words, about as long as the V01 example. Do not make it longer.
- Include everything in the existing brief. Add setting facts from the paper's description of the study area, the system, the current operation and the data, if an expert designing the study would want them.
- The research question may contain the sub-questions and requirements stated in the existing brief.

## Rules for both briefs

- Never state the paper's method, model or algorithm. Never state its findings, result values, or which option performed best.
- Do not state forecast accuracy statistics, fitted distributions or optimized values that the paper produced.
- Only state facts that are in the paper or the existing brief. Write numbers exactly as the paper gives them. If the paper's sources disagree, say so, as the existing brief does.
- Use plain English. Keep units as in the paper.

When done, reply with:
- the two file paths;
- one line for each fact you added to the detailed brief beyond the existing brief, with where it comes from in the paper (section or page);
- any facts you deliberately left out because they would reveal the method.
