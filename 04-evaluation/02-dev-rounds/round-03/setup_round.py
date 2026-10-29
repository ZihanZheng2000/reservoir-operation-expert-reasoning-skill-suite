"""Set up round 3: skill v3 (skill-tested/), question U5 only, opus only, three independent C answers.

Each C answer is paired with the round-1 opus A answer for U5 (copied unchanged under a new random name per pair).
Pairs are named U5-r1, U5-r2, U5-r3 in the blinding key; answer files carry only "U5-" plus a random code.
Prompts are imported from round 1 so the answer and judge texts are identical apart from the base folder.
Usage: python setup_round.py <seed>
"""
import json, random, shutil, string, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
R1 = HERE.parent / '05-round-01'
sys.path.insert(0, str(R1))
import setup_round as S1  # noqa: E402

B = HERE.as_posix()
M, CASE, RUNS = 'opus', 'U5', 3


def main():
    r = random.Random(int(sys.argv[1]))
    S1.HERE = HERE
    q = S1.questions()[CASE]
    key1 = json.loads((R1 / 'blinding-key.json').read_text(encoding='utf-8'))[M][CASE]
    a_src = next(v['file'] for v in (key1['answer1'], key1['answer2']) if v['arm'] == 'A')
    used = {key1['answer1']['file'], key1['answer2']['file']}

    def code():
        while True:
            f = f'{CASE}-' + ''.join(r.choice(string.ascii_lowercase + string.digits) for _ in range(4)) + '.md'
            if f not in used:
                used.add(f)
                return f

    tasks = HERE / 'tasks'
    tasks.mkdir(exist_ok=True)
    (HERE / 'answers' / M).mkdir(parents=True, exist_ok=True)
    (HERE / 'judgments' / M).mkdir(parents=True, exist_ok=True)
    key = {M: {}}
    for i in range(1, RUNS + 1):
        pair = f'{CASE}-r{i}'
        arms = ['A', 'C']
        r.shuffle(arms)
        files = {a: code() for a in arms}
        shutil.copyfile(R1 / 'answers' / M / a_src, HERE / 'answers' / M / files['A'])
        key[M][pair] = {'answer1': {'arm': arms[0], 'file': files[arms[0]]},
                        'answer2': {'arm': arms[1], 'file': files[arms[1]]},
                        'A_source': f'05-round-01/answers/{M}/{a_src}'}
        scope = f'Read only the skill files in {B}/skill-tested. Do not open any other file or folder.'
        (tasks / f'answer-{M}-{pair}-C.txt').write_text(
            S1.ANSWER.format(skill=S1.SKILL.format(B=B) + '\n\n', base=S1.BASE, B=B, scope=scope, question=q, model=M,
                             file=files['C']), encoding='utf-8')
        f1, f2 = files[arms[0]], files[arms[1]]
        for j, (x, y) in (('j1', (f1, f2)), ('j2', (f2, f1))):
            (tasks / f'judge-{M}-{pair}-{j}.txt').write_text(
                S1.JUDGE.format(B=B, model=M, f1=x, f2=y, question=q, case=pair, j=j), encoding='utf-8')
    (HERE / 'blinding-key.json').write_text(json.dumps(key, indent=1), encoding='utf-8')
    print(len(list(tasks.glob('answer-*'))), 'answer tasks,', len(list(tasks.glob('judge-*'))), 'judge tasks')


if __name__ == '__main__':
    main()
