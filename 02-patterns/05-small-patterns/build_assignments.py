"""Build <PID>-assignment.csv for every large pattern from assign/<PID>.py.

assign/<PID>.py defines ASSIGN = {step_key: (small_pattern, secondary_small_pattern, rationale)}; RP01 also defines
SITUATION = {step_key: one-line situation}. The script checks that ASSIGN covers exactly the steps matched to that
large pattern in ../03-step-coding/step-pattern-matches.csv, writes reasoning/ or execution/<PID>-assignment.csv,
and prints step and paper counts per small pattern.
Usage: python build_assignments.py [PID ...]     (default: all 20)
"""
import csv, importlib.util, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MATCHES = HERE.parent / '03-step-coding' / 'step-pattern-matches.csv'


def build(pid, matches):
    spec = importlib.util.spec_from_file_location(pid, HERE / 'assign' / f'{pid}.py')
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    rows = [r for r in matches if r['pattern_id'] == pid]
    keys = {r['step_key'] for r in rows}
    assert keys == set(m.ASSIGN), (pid, sorted(keys - set(m.ASSIGN)), sorted(set(m.ASSIGN) - keys))
    situation = getattr(m, 'SITUATION', None)
    fields = ['step_key', 'paper_id', 'step_title', 'pattern_status', 'family', 'secondary_family']
    fields += ['situation_code'] if situation else []
    fields += ['assignment_rationale']
    out = HERE / ('reasoning' if pid.startswith('RP') else 'execution') / f'{pid}-assignment.csv'
    with out.open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            fam, sec, why = m.ASSIGN[r['step_key']]
            row = dict(step_key=r['step_key'], paper_id=r['paper_id'], step_title=r['step_title'], pattern_status=r['status'],
                       family=fam, secondary_family=sec, assignment_rationale=why)
            if situation:
                row['situation_code'] = situation[r['step_key']]
            w.writerow(row)
    fam = {}
    for r in rows:
        fam.setdefault(m.ASSIGN[r['step_key']][0], [0, set()])
        fam[m.ASSIGN[r['step_key']][0]][0] += 1
        fam[m.ASSIGN[r['step_key']][0]][1].add(r['paper_id'])
    print(pid, ', '.join(f'{k} {v[0]} steps/{len(v[1])} papers' for k, v in sorted(fam.items())))


def main():
    matches = list(csv.DictReader(MATCHES.open(encoding='utf-8-sig')))
    pids = sys.argv[1:] or sorted({r['pattern_id'] for r in matches})
    for pid in pids:
        build(pid, matches)


if __name__ == '__main__':
    main()
