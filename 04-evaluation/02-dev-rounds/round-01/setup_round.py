"""Set up round 1: random answer codes, blinding keys, and the exact prompt for every answer and judge task.

Arms: A = no skill, C = skill v1 (skill-tested/). Answer models: opus (Claude Opus 5.5), haiku (Claude Haiku 4.5).
Judges: Claude Opus 5.5 for all comparisons. Comparisons are within one answer model (A vs C).
Outputs: blinding-key.json, tasks/answer-<model>-<case>-<arm>.txt, tasks/judge-<model>-<case>-<j>.txt
Usage:   python setup_round.py <seed>
"""
import json, random, re, string, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
B = HERE.as_posix()
MODELS = ['opus', 'haiku']
CASES = [f'U{i}' for i in range(1, 8)]

BASE = """You are an expert in reservoir operation under flood risk. Answer the question below.
- You do not need to run models or produce final results. Give a detailed plan of what you would do and why. Where the question asks for a judgment or recommendation, give your provisional one, with the reasons, the key assumptions, and what would confirm or change it.
- Do not invent facts beyond the question; state your assumptions.
- Answer every part the question asks. Organize the answer as you see fit. There is no length limit, but do not pad."""

SKILL = ("First read the skill at {B}/skill-tested/SKILL.md, follow it, and read the reference files it points to "
         "(in {B}/skill-tested/references/) when you work on a unit.")

ANSWER = """{skill}{base}

{scope}

Question:

{question}

Write only your answer (no preamble about these instructions) to {B}/answers/{model}/{file} with the Write tool. Then reply with the list of files you read, and "done"."""

JUDGE = """You are a senior expert in reservoir flood operation, judging two answers to the same question. You do not know how either answer was produced.

Base folder B = "{B}". The question is given below. Read only: Answer 1 = B/answers/{model}/{f1}, Answer 2 = B/answers/{model}/{f2}. Do not open any other file.

Question:

{question}

First work out yourself what an excellent answer must contain, including any calculation.

Score each answer from 1 to 10 on five criteria, using these anchors (3 / 6 / 9):
- KQ, key questions: 3 = misses the questions that decide the answer; 6 = finds most, settles some loosely; 9 = finds and correctly settles every deciding question.
- TC, technical correctness: 3 = a wrong formula, number or concept that changes the conclusion; 6 = minor slips that do not change the conclusion; 9 = no errors, arithmetic checked.
- ME, method: 3 = vague or not executable; 6 = executable with gaps; 9 = complete, ordered, executable, with verification.
- PR, practicality: 3 = ignores operation, regulation, approval; 6 = mentions them generically; 9 = specific operating, regulatory and fallback provisions.
- CA, calibration: 3 = overclaims or invents facts; 6 = some unsupported claims; 9 = conclusions scoped to the evidence, assumptions explicit.

Score the quality of reasoning and planning; do not expect computed results. Do not reward length, formatting or confident tone.

Write your judgment to B/judgments/{model}/{case}-{j}.md with the Write tool, with these parts:
1. Short reasoning per criterion for each answer.
2. "Notes for revision": for each answer, what was done well and what was missing or wrong, in concrete domain terms; then the specific points an expert answer must contain that neither answer had.
3. These exact final lines:
SCORES Answer 1: KQ=_ TC=_ ME=_ PR=_ CA=_
SCORES Answer 2: KQ=_ TC=_ ME=_ PR=_ CA=_
WINNER: Answer 1|Answer 2|tie, clear|slight

Then reply "done"."""


def questions():
    t = (HERE / 'questions-en.md').read_text(encoding='utf-8')
    parts = re.split(r'^## (U\d) — [^\n]*\n', t, flags=re.M)
    q = {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}
    assert list(q) == CASES, list(q)
    return q


def main():
    r = random.Random(int(sys.argv[1]))
    q = questions()
    code = lambda c: f'{c}-' + ''.join(r.choice(string.ascii_lowercase + string.digits) for _ in range(4)) + '.md'
    key = {}
    tasks = HERE / 'tasks'
    tasks.mkdir(exist_ok=True)
    for m in MODELS:
        key[m] = {}
        for c in CASES:
            arms = ['A', 'C']
            r.shuffle(arms)
            files = {a: code(c) for a in arms}
            key[m][c] = {'answer1': {'arm': arms[0], 'file': files[arms[0]]}, 'answer2': {'arm': arms[1], 'file': files[arms[1]]}}
            for a in arms:
                skill = SKILL.format(B=B) + '\n\n' if a == 'C' else ''
                scope = (f'Read only the skill files in {B}/skill-tested. Do not open any other file or folder.' if a == 'C'
                         else 'You do not need to read any file. Do not open any file or folder.')
                (tasks / f'answer-{m}-{c}-{a}.txt').write_text(
                    ANSWER.format(skill=skill, base=BASE, B=B, scope=scope, question=q[c], model=m, file=files[a]), encoding='utf-8')
            f1, f2 = files[arms[0]], files[arms[1]]
            for j, (x, y) in (('j1', (f1, f2)), ('j2', (f2, f1))):
                (tasks / f'judge-{m}-{c}-{j}.txt').write_text(
                    JUDGE.format(B=B, model=m, f1=x, f2=y, question=q[c], case=c, j=j), encoding='utf-8')
    (HERE / 'blinding-key.json').write_text(json.dumps(key, indent=1), encoding='utf-8')
    print(len(list(tasks.glob('answer-*'))), 'answer tasks,', len(list(tasks.glob('judge-*'))), 'judge tasks')


if __name__ == '__main__':
    main()
