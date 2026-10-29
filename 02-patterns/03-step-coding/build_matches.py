"""Build the step-pattern match tables from the per-step coding.

Inputs:  step-coding.csv (one row per step: primary pattern, secondary patterns, rationale)
         ../01-steps/step-inventory.csv, ../02-large-patterns/large-patterns.md (pattern names)
Outputs: step-pattern-matches.csv  one row per positive step-pattern match (primary or secondary)
         unmapped-steps.csv        steps with no pattern
         pattern-coverage.csv      papers and steps per pattern
Usage:   python build_matches.py
"""
import collections, csv, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def read(p):
    return list(csv.DictReader(p.open(encoding='utf-8-sig')))


def write(name, rows, fields):
    with (HERE / name).open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def main():
    steps = {r['step_key']: r for r in read(ROOT / '01-steps' / 'step-inventory.csv')}
    coding = read(HERE / 'step-coding.csv')
    assert {c['step_key'] for c in coding} == set(steps)
    names = dict(re.findall(r'^\| ([RE]P\d\d) \| ([^|]+?) \|', (ROOT / '02-large-patterns' / 'large-patterns.md').read_text(encoding='utf-8'), re.M))
    assert len(names) == 20
    matches, unmapped = [], []
    for c in coding:
        s = steps[c['step_key']]
        base = {k: s[k] for k in ('step_key', 'paper_id', 'layer', 'step_id', 'step_title')}
        if not c['primary']:
            unmapped.append(base | {'reason': c['rationale']})
            continue
        for pid, status in [(c['primary'], 'primary')] + [(x, 'secondary') for x in c['secondary'].split(';') if x]:
            matches.append(base | {'pattern_id': pid, 'pattern_name': names[pid], 'status': status, 'rationale': c['rationale']})
    write('step-pattern-matches.csv', matches, list(matches[0]))
    write('unmapped-steps.csv', unmapped, list(unmapped[0]))
    cov = collections.defaultdict(lambda: dict(pa=set(), pp=set(), steps=set(), prim=0, sec=0))
    for m in matches:
        c = cov[m['pattern_id']]
        c['pa'].add(m['paper_id']); c['steps'].add(m['step_key'])
        if m['status'] == 'primary':
            c['pp'].add(m['paper_id']); c['prim'] += 1
        else:
            c['sec'] += 1
    rows = [dict(pattern_id=k, layer='R' if k.startswith('RP') else 'E', pattern_name=names[k], papers_any_match=len(v['pa']),
                 papers_primary=len(v['pp']), steps_with_match=len(v['steps']), primary_matches=v['prim'], secondary_matches=v['sec'])
            for k, v in sorted(cov.items())]
    write('pattern-coverage.csv', rows, list(rows[0]))
    print(f'{len(matches)} matches ({sum(m["status"] == "primary" for m in matches)} primary), {len(unmapped)} unmapped steps, {len(rows)} patterns')


if __name__ == '__main__':
    main()
