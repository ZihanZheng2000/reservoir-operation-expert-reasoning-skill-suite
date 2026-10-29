"""Set up the final held-out test: five papers x two brief versions (S simple, D detailed) x two arms (A no skill, C skill v3).

Answer prompt: the development-round prompt (imported from 05-round-01), with the brief as the question.
Judge prompt: the earlier held-out judge prompt (six criteria incl. RC, reference route for judges only), plus one line
used in the development rounds: "Score the quality of reasoning and planning; do not expect computed results."
Outputs: blinding-key.json, tasks/answer-<case>-<arm>.txt, tasks/judge-<case>-<j>.txt   (case = V01-S, V01-D, ...)
Usage:   python setup_final.py <seed>
"""
import json, random, string, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / '05-round-01'))
import setup_round as S1  # noqa: E402

B = HERE.as_posix()
PAPERS = [f'V0{i}' for i in range(1, 6)]
VERSIONS = {'S': 'simple', 'D': 'detailed'}

JUDGE = """You are a senior researcher in reservoir flood operation, judging two study designs written for the same problem. You do not know how either was produced.

Base folder B = "{B}". Read only: the problem brief B/briefs/{paper}-brief-{version}.md, the reference route B/briefs/{paper}-reference.md, Answer 1 = B/answers/{f1}, Answer 2 = B/answers/{f2}. Do not open any other file.

The reference describes how one published study approached this problem. It is one expert solution, not the only correct one: a design that departs from it with a sound, justified approach deserves full credit. The answers did not see the reference; they saw only the brief.

Score each answer from 1 to 10 on six criteria (anchors 3 / 6 / 9):
- KQ, key questions: 3 = misses the questions that decide the study; 6 = finds most, settles some loosely; 9 = finds and correctly settles every deciding question.
- TC, technical correctness: 3 = a wrong formula, number or concept that changes the design; 6 = minor slips; 9 = no errors.
- ME, method: 3 = vague or not executable; 6 = executable with gaps; 9 = complete, ordered, executable, with verification.
- PR, practicality: 3 = ignores data limits, operation, regulation; 6 = mentions them generically; 9 = specific and realistic.
- CA, calibration: 3 = overclaims or invents facts; 6 = some unsupported claims; 9 = scoped to the brief, assumptions explicit.
- RC, reference coverage: 3 = covers few of the reference's essential questions and steps; 6 = about half, or weaker substitutes; 9 = nearly all, or justified equivalents.

Score the quality of reasoning and planning; do not expect computed results. Do not reward length, formatting or confident tone.

Write your judgment to B/judgments/{case}-{j}.md with the Write tool:
1. Short reasoning per criterion for each answer.
2. Notes: for each answer, what was good and what was missing or wrong, in concrete domain terms; then the reference's essential questions or steps that neither answer covered.
3. These exact final lines:
SCORES Answer 1: KQ=_ TC=_ ME=_ PR=_ CA=_ RC=_
SCORES Answer 2: KQ=_ TC=_ ME=_ PR=_ CA=_ RC=_
WINNER: Answer 1|Answer 2|tie, clear|slight

Then reply "done"."""


def main():
    r = random.Random(int(sys.argv[1]))
    used = set()

    def code(p):
        while True:
            f = f'{p}-' + ''.join(r.choice(string.ascii_lowercase + string.digits) for _ in range(4)) + '.md'
            if f not in used:
                used.add(f)
                return f

    tasks = HERE / 'tasks'
    tasks.mkdir(exist_ok=True)
    (HERE / 'answers').mkdir(exist_ok=True)
    (HERE / 'judgments').mkdir(exist_ok=True)
    key = {}
    for p in PAPERS:
        for v, version in VERSIONS.items():
            case = f'{p}-{v}'
            brief = (HERE / 'briefs' / f'{p}-brief-{version}.md').read_text(encoding='utf-8').strip()
            arms = ['A', 'C']
            r.shuffle(arms)
            files = {a: code(p) for a in arms}
            key[case] = {'answer1': {'arm': arms[0], 'file': files[arms[0]]}, 'answer2': {'arm': arms[1], 'file': files[arms[1]]}}
            for a in arms:
                skill = S1.SKILL.format(B=B) + '\n\n' if a == 'C' else ''
                scope = (f'Read only the skill files in {B}/skill-tested. Do not open any other file or folder.' if a == 'C'
                         else 'You do not need to read any file. Do not open any file or folder.')
                text = S1.ANSWER.format(skill=skill, base=S1.BASE, B=B, scope=scope, question=brief, model='X', file=files[a])
                text = text.replace(f'{B}/answers/X/', f'{B}/answers/')
                (tasks / f'answer-{case}-{a}.txt').write_text(text, encoding='utf-8')
            f1, f2 = files[arms[0]], files[arms[1]]
            for j, (x, y) in (('j1', (f1, f2)), ('j2', (f2, f1))):
                (tasks / f'judge-{case}-{j}.txt').write_text(
                    JUDGE.format(B=B, paper=p, version=version, f1=x, f2=y, case=case, j=j), encoding='utf-8')
    (HERE / 'blinding-key.json').write_text(json.dumps(key, indent=1), encoding='utf-8')
    print(len(list(tasks.glob('answer-*'))), 'answer tasks,', len(list(tasks.glob('judge-*'))), 'judge tasks')


if __name__ == '__main__':
    main()
