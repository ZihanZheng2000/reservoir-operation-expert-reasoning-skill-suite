"""Build one evidence bundle per skill unit, as input for writing the unit's reference file.

A unit pairs a reasoning pattern with its execution pattern (see README.md). For every small pattern of the unit,
the bundle lists the paper steps assigned to it (primary small-pattern assignment) with the step's full card text:
description, retained details (trigger, inputs, procedure, branches, output, checks), and evidence boundary.

Inputs:  v3/02-patterns/01-steps/step-inventory.csv
         v3/02-patterns/05-small-patterns/*/<PID>-assignment.csv (small-pattern assignment of each step)
         v3/02-patterns/06-taxonomy/pattern-taxonomy-en.md (small-pattern names and descriptions)
Output:  evidence/<unit>.md
Usage:   python build_unit_evidence.py [unit ...]     (default: all 11 units)
"""
import csv, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
V3 = HERE.parent / '02-patterns'
UNITS = {
    '1.1-current-rule-and-baseline': ['RP01', 'EP01'],
    '2.1-decision-relevant-uncertainty': ['RP02', 'EP03'],
    '2.2-forecast-reliability-and-timing': ['RP03', 'EP02'],
    '2.3-simulate-response': ['EP04'],
    '3.1-risk-and-acceptable-safety': ['RP04', 'EP07'],
    '3.2-feasibility': ['RP05', 'EP05'],
    '3.3-adaptive-logic': ['RP07', 'EP09'],
    '3.4-trade-offs-and-selection': ['RP06', 'EP08'],
    '3.5-model-and-method-choice': ['RP08', 'EP06'],
    '4.1-evidence-and-applicability': ['RP09', 'EP10'],
    '4.2-adoption': ['EP11'],
}


def main():
    steps = {r['step_key']: r for r in csv.DictReader((V3 / '01-steps' / 'step-inventory.csv').open(encoding='utf-8-sig'))}
    tax = (V3 / '06-taxonomy' / 'pattern-taxonomy-en.md').read_text(encoding='utf-8')
    small = {}
    for m in re.finditer(r'^\| \*\*([RE]P\d\d-[A-H])\*\* ([^|]+?) \|(.*)\|\s*$', tax, re.M):
        cells = [c.strip() for c in m.group(3).split('|')]
        small[m.group(1)] = (m.group(2).strip(), cells[-4] if m.group(1).startswith('RP08') else cells[0], cells[-1])
    out = HERE / 'evidence'
    out.mkdir(exist_ok=True)
    for unit in sys.argv[1:] or UNITS:
        lines = [f'# Evidence for unit {unit}', '',
                 'Paper steps assigned to each small pattern of this unit, with their full card text. '
                 'Step IDs: Exx = paper, Rn = reasoning step, En = execution step.', '']
        total = 0
        for pid in UNITS[unit]:
            layer = 'reasoning' if pid.startswith('RP') else 'execution'
            rows = list(csv.DictReader((V3 / '05-small-patterns' / layer / f'{pid}-assignment.csv').open(encoding='utf-8-sig')))
            for fam in sorted({r['family'] for r in rows}):
                name, desc, strength = small[fam]
                members = [r for r in rows if r['family'] == fam]
                papers = {r['paper_id'] for r in members}
                lines += [f'## {fam} {name}', '', f'{desc}. Strength: {strength}. {len(members)} steps, {len(papers)} papers.', '']
                for r in members:
                    s = steps[r['step_key']]
                    lines += [f"### {s['paper_id']}-{s['step_id']}: {s['step_title']}", '',
                              f"**Description:** {s['step_description']}", '',
                              f"**Retained details:** {s['retained_details']}", '',
                              f"**Evidence boundary:** {s['evidence_boundary']}", '']
                total += len(members)
        (out / f'{unit}.md').write_text('\n'.join(lines), encoding='utf-8')
        print(f'{unit}: {total} steps, {sum(len(l.split()) for l in lines):,} words')


if __name__ == '__main__':
    main()
