# Pattern-guided re-reading back-test (Test 1, pilot)

Written 2026-10-02 before any run.

**Question.** One-pass, open-ended extraction does not guarantee that every pattern a paper uses is extracted. If a reader re-reads the full text with the pattern list in hand, how many additional pattern occurrences are found, and does this change corpus-level coverage?

**Sample.** 10 of the 50 development papers, drawn at random (seed 20261002): E06, E10, E11, E23, E24, E26, E32, E35, E42, E44 (`sample.json`).

**Condition A (one-pass).** Large patterns found in each paper by the existing extraction + recoded mapping (`onepass.json`). Re-reading agents do not see this file, the extractions, or the mapping.

**Condition B (pattern-guided).** One fresh subagent per paper reads the full text (`01-corpus/development-50/text/Exx.txt`) and `pattern-list.md`, and judges each of the 20 large patterns as present or absent. A pattern is present only if the study itself performs that judgment or activity (not if it appears only in the literature review or as future work), and each "present" needs a verbatim quote of 40 words or fewer as evidence. Output: `reread/Exx.json`.

**Comparison.** For each paper:
- **Recovered:** patterns found in B but not in A.
- **Confirmed:** patterns found in both A and B.
- **Missed by B:** patterns found in A but not in B.

Then corpus level: whether any pattern absent from the corpus is newly discovered.

**Check.** The project coder reads the evidence for every recovered pattern and labels it supported or not supported. Only supported recoveries are reported as recovered.

**Limits.** Small sample; AI readers and AI checker; the re-reader sees a pattern list, which may also encourage over-detection, so evidence checking is required.
