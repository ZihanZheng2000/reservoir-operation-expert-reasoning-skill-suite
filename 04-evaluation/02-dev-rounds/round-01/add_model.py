"""Add one more answer model to round 1 without touching the existing ones.

Uses the same prompts and questions as setup_round.py; new random answer codes from a separate seed.
Appends the model to blinding-key.json and writes its answer and judge task files.
Usage: python add_model.py <model> <seed>      e.g. python add_model.py sonnet 20261029
"""
import json, random, string, sys
from pathlib import Path
import setup_round as S

HERE = Path(__file__).resolve().parent


def main():
    m, seed = sys.argv[1], int(sys.argv[2])
    key = json.loads((HERE / 'blinding-key.json').read_text(encoding='utf-8'))
    assert m not in key, f'{m} already in blinding key'
    r = random.Random(seed)
    q = S.questions()
    code = lambda c: f'{c}-' + ''.join(r.choice(string.ascii_lowercase + string.digits) for _ in range(4)) + '.md'
    tasks = HERE / 'tasks'
    (HERE / 'answers' / m).mkdir(parents=True, exist_ok=True)
    (HERE / 'judgments' / m).mkdir(parents=True, exist_ok=True)
    key[m] = {}
    for c in S.CASES:
        arms = ['A', 'C']
        r.shuffle(arms)
        files = {a: code(c) for a in arms}
        key[m][c] = {'answer1': {'arm': arms[0], 'file': files[arms[0]]}, 'answer2': {'arm': arms[1], 'file': files[arms[1]]}}
        for a in arms:
            skill = S.SKILL.format(B=S.B) + '\n\n' if a == 'C' else ''
            scope = (f'Read only the skill files in {S.B}/skill-tested. Do not open any other file or folder.' if a == 'C'
                     else 'You do not need to read any file. Do not open any file or folder.')
            (tasks / f'answer-{m}-{c}-{a}.txt').write_text(
                S.ANSWER.format(skill=skill, base=S.BASE, B=S.B, scope=scope, question=q[c], model=m, file=files[a]), encoding='utf-8')
        f1, f2 = files[arms[0]], files[arms[1]]
        for j, (x, y) in (('j1', (f1, f2)), ('j2', (f2, f1))):
            (tasks / f'judge-{m}-{c}-{j}.txt').write_text(
                S.JUDGE.format(B=S.B, model=m, f1=x, f2=y, question=q[c], case=c, j=j), encoding='utf-8')
    (HERE / 'blinding-key.json').write_text(json.dumps(key, indent=1), encoding='utf-8')
    print(m, 'added:', len(list(tasks.glob(f'answer-{m}-*'))), 'answer tasks,', len(list(tasks.glob(f'judge-{m}-*'))), 'judge tasks')


if __name__ == '__main__':
    main()
