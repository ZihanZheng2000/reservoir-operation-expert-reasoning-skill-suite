# Round 1 protocol

Written 2026-10-28, before any run. Decisions agreed with the user are recorded in `../04-dev-questions/answer-and-judge-prompts.md`.

## What is tested

- **Skill:** skill v1, frozen in `skill-tested/` (copied from `../03-skill-v1/reservoir-flood-expert/`; SHA256 in `skill-tested.sha256`).
- **Questions:** the 7 development questions U1–U7, English version `questions-en.md` (copied from `../04-dev-questions/`).
- **Arms:** A = no skill; C = reads the skill first. The answer prompt is otherwise identical (`setup_round.py`).
- **Answer models:** Claude Opus 5.5 (`opus`) and Claude Haiku 4.5 (`haiku`), each answering all 7 questions in both arms (28 answers). Comparisons are only within one answer model.
- **Added after the first results (user request, 2026-10-28):** Claude Sonnet 5.5 (`sonnet`) as a middle-tier answer model, same skill v1, questions, prompts and judges; answer codes from seed 20261029 (`add_model.py`). 14 answers, 14 judgments.
- **Judges:** Claude Opus 5.5, two per comparison, the second sees the answers in reversed order (28 judgments). Judge prompt: the original development judge prompt with one added line ("Score the quality of reasoning and planning; do not expect computed results.") and updated paths.
- **Blinding:** random answer codes, seed 20261028 (`blinding-key.json`). Judges read only the question and the two answers.

## Rules

- No fixed sections, no length limit; a detailed plan is required, final computed results are not; questions that ask for a judgment get a provisional one.
- A case is a win only if both judges agree. Report judgments per arm, mean score per criterion and arm, and mean answer length per arm.
- After the round, check skill-arm answers for skill vocabulary (stage or unit names, pattern codes).
- Skill revisions after this round come only from the judges' "Notes for revision" and the user's comments; each revision records its source.

## Known limitations

- Judges and Opus answerers are the same model.
- The project folder name in the answer path contains "skill-suite", visible to both arms.
- The development questions were drafted by the skill builder and revised by the user.
- One answer per question and arm; no repetitions.

## Run log

| Batch | Tasks | Model | Status |
|---|---|---|---|
| 1 | answers, opus, U1–U5 × A/C | Claude Opus 5.5 (`opus`) | done, 10/10 |
| 2 | answers, opus U6–U7 × A/C; haiku U1–U3 × A/C | Opus 5.5 / Claude Haiku 4.5 (`haiku`) | done, 10/10 |
| 3 | answers, haiku U4–U7 × A/C | Claude Haiku 4.5 (`haiku`) | done, 8/8 |
| 4 | judges, opus U1–U7 and haiku U1–U7 × j1/j2 | Claude Opus 5.5 (`opus`) | done, 28/28; results in `results.md` |
| 5 | answers, sonnet U1–U7 × A/C | Claude Sonnet 5.5 (`sonnet`) | done, 14/14 (first launch hit the session limit after 8 answers were written; the 8 written files were checked complete; the other 6 were rerun) |
| 6 | judges, sonnet U1–U7 × j1/j2 | Claude Opus 5.5 (`opus`) | done, 14/14 |
