# Final held-out test: protocol

Written 2026-10-28, before any run. The user agreed the design in this session (Claude Code as researcher by session role override).

## What is tested

- **Skill:** v3, frozen in `skill-tested/` (`skill-tested.sha256`). It is not revised from these results.
- **Papers:** V01–V05. They were not among the 50 papers used to build the patterns and the skill.
- **Arms:**
  - **A:** no skill.
  - **C:** reads `skill-tested/SKILL.md`, follows it, and uses its references.
- **Answer model:** Claude Opus 5.5 for both arms, generated fresh. Earlier final-test answers used a different format and an unrecorded model, so they are not reused.

## Briefs (two versions per paper)

| Version | Content |
|---|---|
| **S (simple)** | Two paragraphs: background and research question, about 150 words. No sub-questions, no risk definitions, few numbers. |
| **D (detailed)** | Five fixed sections, about 550 words: background, system characteristics table, current operation and constraints, data, research question. |

- **How V01 was written:** the main session wrote it from the paper. The user reviewed it and set the level of detail: simple in two paragraphs, detailed in five fixed sections, not longer.
- **How V02–V05 were written:** one subagent per paper, following `briefs-draft/brief-writer-instructions.md`. Each subagent read the paper, the old brief, the old reference and the approved V01 examples. None of them saw the skill. The main session reviewed the drafts.
- **Edit by the main session:** the V05 detailed brief had a research-question bullet asking whether the gauge record can be relied on for large floods. It was removed because it pointed to the paper's water-balance check.
- **Content carried over from the old briefs:**
  - V03: the statement that forecast errors are largest for big floods.
  - V04: the sub-question on whether simple error assumptions understate risk.
- **References:** the judge-only routes in `briefs/Vxx-reference.md`, copied unchanged from the earlier final test.

## Prompts

- **Answer:** the development-round answer prompt, imported from `05-round-01/setup_round.py`, with the brief as the question.
- **Judge:** the earlier final-test judge prompt, with these changes:
  - It keeps the six criteria KQ, TC, ME, PR, CA and RC, the 3/6/9 anchors, and the note that the reference is one solution among others.
  - Added, as in the development rounds: "Score the quality of reasoning and planning; do not expect computed results."
  - The notes now also ask for the reference's essential questions that neither answer covered.
- **What judges read:** the brief version the answers saw, the reference, and the two answers. They do not read the paper.

## Design

- **Cases:** 10 (5 papers × 2 versions).
- **Answers:** 20 (each case × 2 arms).
- **Judges:** two blind judges per case, the second seeing the answers in reversed order, so 20 judgments.
- **Blinding:** file names are a paper prefix plus a random code; the key is in `blinding-key.json` (seed 20261101).

## Reporting

- **Per case:** a win requires both judges to agree.
- **Overall:**
  - the number of judgments preferring C;
  - mean scores per criterion and arm, overall and separately for S and D.
- **Main questions:**
  1. Does the skill beat no skill on held-out papers?
  2. Is its advantage larger on simple briefs?
  3. Does RC (coverage of the paper's own route) improve with the skill, especially on simple briefs?
- **No changes after results:** the design is not changed once results are seen.
