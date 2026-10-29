"""Per-question and per-criterion analysis of round 2 (C minus A, averaged over the two judges).
Usage: python analyze.py   (writes analysis-tables.md)
"""
import json, re
from pathlib import Path
from statistics import mean

HERE = Path(__file__).resolve().parent
CRIT = ['KQ', 'TC', 'ME', 'PR', 'CA']
MODELS = ['opus']


def scores():
    key = json.loads((HERE / 'blinding-key.json').read_text(encoding='utf-8'))
    S = {}  # (model, case, arm) -> list of {crit: score} per judge
    W = {}  # (model, case, arm) -> words
    for m in MODELS:
        for case, k in key[m].items():
            arm_of = {1: k['answer1']['arm'], 2: k['answer2']['arm']}
            for n in (1, 2):
                W[(m, case, arm_of[n])] = len((HERE / 'answers' / m / k[f'answer{n}']['file']).read_text(encoding='utf-8').split())
            for j, order in (('j1', [arm_of[1], arm_of[2]]), ('j2', [arm_of[2], arm_of[1]])):
                t = (HERE / 'judgments' / m / f'{case}-{j}.md').read_text(encoding='utf-8')
                for n in (1, 2):
                    s = re.search(rf'SCORES Answer {n}:\s*' + r'\s+'.join(rf'{c}=(\d+)' for c in CRIT), t)
                    S.setdefault((m, case, order[n - 1]), []).append(dict(zip(CRIT, map(int, s.groups()))))
    return S, W


def main():
    S, W = scores()
    cases = [f'U{i}' for i in range(1, 8)]
    out = ['# Round 2 analysis tables', '', 'Values are skill arm (C) minus no-skill arm (A), averaged over the two judges and the five criteria unless stated.', '']
    out += ['## Mean score difference per question (C − A)', '', '| Question | ' + ' | '.join(MODELS) + ' |', '|---|' + '---:|' * len(MODELS)]
    for c in cases:
        row = []
        for m in MODELS:
            d = mean(mean(s.values()) for s in S[(m, c, 'C')]) - mean(mean(s.values()) for s in S[(m, c, 'A')])
            row.append(f'{d:+.1f}')
        out.append(f'| {c} | ' + ' | '.join(row) + ' |')
    out += ['', '## Mean criterion difference per model (C − A), over all questions', '', '| Model | ' + ' | '.join(CRIT) + ' |', '|---|' + '---:|' * len(CRIT)]
    for m in MODELS:
        ds = [mean(s[k] for c in cases for s in S[(m, c, 'C')]) - mean(s[k] for c in cases for s in S[(m, c, 'A')]) for k in CRIT]
        out.append(f'| {m} | ' + ' | '.join(f'{d:+.1f}' for d in ds) + ' |')
    out += ['', '## Calibration (CA) difference per question (C − A)', '', '| Question | ' + ' | '.join(MODELS) + ' |', '|---|' + '---:|' * len(MODELS)]
    for c in cases:
        out.append(f'| {c} | ' + ' | '.join(f"{mean(s['CA'] for s in S[(m, c, 'C')]) - mean(s['CA'] for s in S[(m, c, 'A')]):+.1f}" for m in MODELS) + ' |')
    out += ['', '## Answer length per question (words, A / C)', '', '| Question | ' + ' | '.join(MODELS) + ' |', '|---|' + '---|' * len(MODELS)]
    for c in cases:
        out.append(f'| {c} | ' + ' | '.join(f"{W[(m, c, 'A')]} / {W[(m, c, 'C')]}" for m in MODELS) + ' |')
    # length vs score difference
    pairs = [(W[(m, c, 'C')] - W[(m, c, 'A')], mean(mean(s.values()) for s in S[(m, c, 'C')]) - mean(mean(s.values()) for s in S[(m, c, 'A')])) for m in MODELS for c in cases]
    xs, ys = zip(*pairs)
    mx, my = mean(xs), mean(ys)
    cov = sum((x - mx) * (y - my) for x, y in pairs)
    r = cov / (sum((x - mx) ** 2 for x in xs) ** 0.5 * sum((y - my) ** 2 for y in ys) ** 0.5)
    out += ['', f'Correlation between length difference (C − A words) and score difference across the 7 questions: r = {r:.2f}.', '']
    # judge agreement
    agree = []
    for m in MODELS:
        for c in cases:
            d = [mean(S[(m, c, 'C')][j].values()) - mean(S[(m, c, 'A')][j].values()) for j in (0, 1)]
            agree.append((m, c, d))
    same_sign = sum((a > 0) == (b > 0) or (a == 0 and b == 0) for _, _, (a, b) in agree)
    out += [f'Judges agree on the sign of the score difference in {same_sign} of 7 question-model pairs.', '']
    (HERE / 'analysis-tables.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('\n'.join(out))


if __name__ == '__main__':
    main()
