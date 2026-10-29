"""Set up round 2: skill v2 (skill-tested/) answered by opus only; A answers reused from round 1.

Arms: A = no skill (round-1 opus answers, copied unchanged under new random names), C = skill v2.
Prompts are imported from round 1 so the answer and judge texts are identical apart from the base folder.
Outputs: blinding-key.json (with the round-1 source of each A answer), answers/opus/<A copies>,
         tasks/answer-opus-<case>-C.txt, tasks/judge-opus-<case>-<j>.txt
Usage:   python setup_round.py <seed>
"""
import json, random, shutil, string, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
R1 = HERE.parent / '05-round-01'
sys.path.insert(0, str(R1))
import setup_round as S1  # noqa: E402

B = HERE.as_posix()
M = 'opus'


def main():
    r = random.Random(int(sys.argv[1]))
    S1.HERE = HERE  # read questions-en.md from this round (a copy of round 1's)
    q = S1.questions()
    key1 = json.loads((R1 / 'blinding-key.json').read_text(encoding='utf-8'))[M]
    used = {v['file'] for k in key1.values() for v in (k['answer1'], k['answer2'])}

    def code(c):
        while True:
            f = f'{c}-' + ''.join(r.choice(string.ascii_lowercase + string.digits) for _ in range(4)) + '.md'
            if f not in used:
                used.add(f)
                return f

    tasks = HERE / 'tasks'
    tasks.mkdir(exist_ok=True)
    (HERE / 'answers' / M).mkdir(parents=True, exist_ok=True)
    (HERE / 'judgments' / M).mkdir(parents=True, exist_ok=True)
    key = {M: {}}
    for c in S1.CASES:
        a_src = next(v['file'] for v in (key1[c]['answer1'], key1[c]['answer2']) if v['arm'] == 'A')
        arms = ['A', 'C']
        r.shuffle(arms)
        files = {a: code(c) for a in arms}
        shutil.copyfile(R1 / 'answers' / M / a_src, HERE / 'answers' / M / files['A'])
        key[M][c] = {'answer1': {'arm': arms[0], 'file': files[arms[0]]},
                     'answer2': {'arm': arms[1], 'file': files[arms[1]]},
                     'A_source': f'05-round-01/answers/{M}/{a_src}'}
        skill = S1.SKILL.format(B=B) + '\n\n'
        scope = f'Read only the skill files in {B}/skill-tested. Do not open any other file or folder.'
        (tasks / f'answer-{M}-{c}-C.txt').write_text(
            S1.ANSWER.format(skill=skill, base=S1.BASE, B=B, scope=scope, question=q[c], model=M, file=files['C']), encoding='utf-8')
        f1, f2 = files[arms[0]], files[arms[1]]
        for j, (x, y) in (('j1', (f1, f2)), ('j2', (f2, f1))):
            (tasks / f'judge-{M}-{c}-{j}.txt').write_text(
                S1.JUDGE.format(B=B, model=M, f1=x, f2=y, question=q[c], case=c, j=j), encoding='utf-8')
    (HERE / 'blinding-key.json').write_text(json.dumps(key, indent=1), encoding='utf-8')
    print(len(list(tasks.glob('answer-*'))), 'answer tasks,', len(list(tasks.glob('judge-*'))), 'judge tasks')


if __name__ == '__main__':
    main()
