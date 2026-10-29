"""Check the reference files against their evidence bundles.

For each unit: (1) every small pattern of the unit has a section; (2) every bullet cites at least one step ID;
(3) every cited step ID appears in the unit's evidence bundle (no step from outside the bundle).
Usage: python check_references.py
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEP = re.compile(r'\bE\d\d-[RE]\d+\b')


def main():
    ok_all = True
    for ev in sorted((HERE / 'evidence').glob('*.md')):
        unit = ev.stem
        ref = HERE / 'reservoir-flood-expert' / 'references' / f'{unit}.md'
        if not ref.exists():
            print(f'{unit}: MISSING')
            ok_all = False
            continue
        et, rt = ev.read_text(encoding='utf-8'), ref.read_text(encoding='utf-8')
        fams = re.findall(r'^## ([RE]P\d\d-[A-H]) ', et, re.M)
        secs = re.findall(r'^## ([RE]P\d\d-[A-H]) ', rt, re.M)
        allowed = set(re.findall(r'^### (E\d\d-[RE]\d+):', et, re.M))
        cited = set(STEP.findall(rt))
        bullets = [l for l in rt.splitlines() if l.lstrip().startswith('- ')]
        uncited = [l.strip()[:80] for l in bullets if not STEP.search(l) and 'unclear' not in l.lower()]
        missing = [f for f in fams if f not in secs]
        outside = sorted(cited - allowed)
        unused = len(allowed - cited)
        ok = not missing and not outside
        ok_all &= ok
        print(f'{unit}: {len(secs)}/{len(fams)} sections, {len(cited)} step IDs cited '
              f'({unused} of {len(allowed)} evidence steps not cited), {len(rt.split()):,} words'
              + ('' if ok else f'  MISSING={missing} OUTSIDE={outside[:10]}'))
        if uncited:
            print(f'   bullets without a step ID: {len(uncited)}', uncited[:3])
    print('ALL OK' if ok_all else 'PROBLEMS FOUND')


if __name__ == '__main__':
    main()
