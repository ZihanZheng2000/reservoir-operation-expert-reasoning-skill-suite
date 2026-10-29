"""Unblind round 3: winners per case, judgments per arm, mean score per criterion and arm, answer word counts,
and a check for skill vocabulary leaking into answers. Results per answer model (opus).
Usage: python tally.py   (writes results.md)
"""
import json, re
from pathlib import Path
from statistics import mean

HERE = Path(__file__).resolve().parent
CRIT = ['KQ', 'TC', 'ME', 'PR', 'CA']
LEAK = re.compile(r'\b(RP0\d|EP\d\d|RP\d\d-[A-H]|EP\d\d-[A-H]|J\d\d)\b|\bStage [1-4]\b|\bunit [1-4]\.\d\b|reservoir-flood-expert'
                  r'|\bthe papers\b|papers (show|report|found)', re.I)


def main():
    key = json.loads((HERE / 'blinding-key.json').read_text(encoding='utf-8'))
    out = ['# Round 3 results', '', 'Arms: A = no skill, C = skill v3. Judges: Claude Opus 5.5 (two per case, order reversed). '
           'A case is won only if both judges agree.', '']
    for m, cases in key.items():
        scores = {a: {c: [] for c in CRIT} for a in 'AC'}
        rows, ccount, wins = [], 0, {'A': 0, 'C': 0, 'split': 0, 'tie': 0}
        words = {'A': [], 'C': []}
        leaks = []
        for case, k in cases.items():
            arm_of = {1: k['answer1']['arm'], 2: k['answer2']['arm']}
            for n in (1, 2):
                f = HERE / 'answers' / m / k[f'answer{n}']['file']
                if f.exists():
                    t = f.read_text(encoding='utf-8')
                    words[arm_of[n]].append(len(t.split()))
                    hits = sorted(set(x.group(0) for x in LEAK.finditer(t)))
                    if hits:
                        leaks.append(f"{case}-{arm_of[n]}: {', '.join(hits)}")
            res = {}
            for j, order in (('j1', [arm_of[1], arm_of[2]]), ('j2', [arm_of[2], arm_of[1]])):
                f = HERE / 'judgments' / m / f'{case}-{j}.md'
                if not f.exists():
                    res[j] = 'missing'
                    continue
                t = f.read_text(encoding='utf-8')
                for n in (1, 2):
                    s = re.search(rf'SCORES Answer {n}:\s*' + r'\s+'.join(rf'{c}=(\d+)' for c in CRIT), t)
                    if s:
                        for c, v in zip(CRIT, s.groups()):
                            scores[order[n - 1]][c].append(int(v))
                w = re.findall(r'WINNER:\s*\**\s*(Answer 1|Answer 2|tie)[^,\n]*,?\s*(clear|slight)?', t, re.I)
                if not w:
                    res[j] = 'unparsed'
                    continue
                who, strength = w[-1]
                res[j] = 'tie' if who.lower() == 'tie' else f"{order[int(who[-1]) - 1]}, {strength.lower() or '?'}"
            arms = {r.split(',')[0] for r in res.values()}
            if len(arms) == 1 and next(iter(arms)) in ('A', 'C', 'tie'):
                result = next(iter(arms))
                result = 'tie' if result == 'tie' else f'{result} wins'
            else:
                result = 'split'
            wins[result.split()[0] if result != 'split' else 'split'] += 1
            ccount += sum(r.startswith('C') for r in res.values())
            rows.append(f"| {case} | {res.get('j1')} | {res.get('j2')} | {result} |")
        out += [f'## Answer model: {m}', '', '| Case | Judge 1 | Judge 2 | Result |', '|---|---|---|---|'] + rows
        out += ['', f"Cases: C {wins['C']}, A {wins['A']}, tie {wins['tie']}, split {wins['split']}. "
                    f"Judgments preferring C: {ccount} of {2 * len(cases)}.", '',
                '| Arm | ' + ' | '.join(CRIT) + ' | Mean | Mean words |', '|---|' + '---:|' * (len(CRIT) + 2)]
        for a in 'AC':
            if scores[a][CRIT[0]]:
                ms = [mean(scores[a][c]) for c in CRIT]
                out.append(f'| {a} | ' + ' | '.join(f'{x:.1f}' for x in ms) + f' | {mean(ms):.2f} | '
                           f"{mean(words[a]):.0f} |" if words[a] else ' | |')
        out += ['', 'Skill vocabulary found in answers: ' + ('; '.join(leaks) if leaks else 'none'), '']
    (HERE / 'results.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('\n'.join(out))


if __name__ == '__main__':
    main()
