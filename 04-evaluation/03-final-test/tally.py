"""Unblind the final held-out test: winner per case, judgments preferring C, mean scores (six criteria) per arm,
overall and per brief version (S simple, D detailed), answer lengths, and a check for skill vocabulary in answers.
Usage: python tally.py   (writes results.md)
"""
import json, re
from pathlib import Path
from statistics import mean

HERE = Path(__file__).resolve().parent
CRIT = ['KQ', 'TC', 'ME', 'PR', 'CA', 'RC']
LEAK = re.compile(r'\b(RP0\d|EP\d\d|RP\d\d-[A-H]|EP\d\d-[A-H]|J\d\d)\b|\bStage [1-4]\b|\bunit [1-4]\.\d\b|reservoir-flood-expert'
                  r'|\bthe papers\b|papers (show|report|found)', re.I)


def main():
    key = json.loads((HERE / 'blinding-key.json').read_text(encoding='utf-8'))
    rows, leaks = [], []
    scores = {v: {a: {c: [] for c in CRIT} for a in 'AC'} for v in 'SD'}
    words = {v: {'A': [], 'C': []} for v in 'SD'}
    wins = {v: {'C': 0, 'A': 0, 'tie': 0, 'split': 0} for v in 'SD'}
    ccount = {v: 0 for v in 'SD'}
    for case, k in key.items():
        v = case[-1]
        arm_of = {1: k['answer1']['arm'], 2: k['answer2']['arm']}
        for n in (1, 2):
            t = (HERE / 'answers' / k[f'answer{n}']['file']).read_text(encoding='utf-8')
            words[v][arm_of[n]].append(len(t.split()))
            hits = sorted(set(x.group(0) for x in LEAK.finditer(t)))
            if hits:
                leaks.append(f"{case}-{arm_of[n]}: {', '.join(hits)}")
        res = {}
        for j, order in (('j1', [arm_of[1], arm_of[2]]), ('j2', [arm_of[2], arm_of[1]])):
            t = (HERE / 'judgments' / f'{case}-{j}.md').read_text(encoding='utf-8')
            for n in (1, 2):
                s = re.search(rf'SCORES Answer {n}:\s*' + r'\s+'.join(rf'{c}=(\d+)' for c in CRIT), t)
                for c, x in zip(CRIT, s.groups()):
                    scores[v][order[n - 1]][c].append(int(x))
            who, strength = re.findall(r'WINNER:\s*\**\s*(Answer 1|Answer 2|tie)[^,\n]*,?\s*(clear|slight)?', t, re.I)[-1]
            res[j] = 'tie' if who.lower() == 'tie' else f"{order[int(who[-1]) - 1]}, {strength.lower() or '?'}"
        arms = {r.split(',')[0] for r in res.values()}
        result = next(iter(arms)) if len(arms) == 1 else 'split'
        wins[v][result] += 1
        ccount[v] += sum(r.startswith('C') for r in res.values())
        rows.append(f"| {case} | {res['j1']} | {res['j2']} | {result if result in ('tie', 'split') else result + ' wins'} |")
    out = ['# Final held-out test: results', '', 'A = no skill, C = skill v3; answers by Claude Opus 5.5; two Opus 5.5 judges per case '
           '(order reversed). A case is won only if both judges agree. S = simple brief, D = detailed brief.', '',
           '| Case | Judge 1 | Judge 2 | Result |', '|---|---|---|---|'] + rows + ['']
    for label, vs in (('All', 'SD'), ('Simple (S)', 'S'), ('Detailed (D)', 'D')):
        w = {r: sum(wins[v][r] for v in vs) for r in ('C', 'A', 'tie', 'split')}
        out += [f'## {label}', '', f"Cases: C {w['C']}, A {w['A']}, tie {w['tie']}, split {w['split']}. "
                f"Judgments preferring C: {sum(ccount[v] for v in vs)} of {10 * len(vs)}.", '',
                '| Arm | ' + ' | '.join(CRIT) + ' | Mean | Mean words |', '|---|' + '---:|' * (len(CRIT) + 2)]
        for a in 'AC':
            ms = [mean(x for v in vs for x in scores[v][a][c]) for c in CRIT]
            out.append(f'| {a} | ' + ' | '.join(f'{x:.1f}' for x in ms) + f' | {mean(ms):.2f} | {mean(x for v in vs for x in words[v][a]):.0f} |')
        out.append('')
    out += ['Skill vocabulary found in answers: ' + ('; '.join(leaks) if leaks else 'none'), '']
    (HERE / 'results.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('\n'.join(out))


if __name__ == '__main__':
    main()
