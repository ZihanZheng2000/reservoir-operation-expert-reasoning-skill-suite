"""Prepare the pattern-guided re-reading back-test.

1. Build pattern-list.md (20 large patterns + small patterns) from the frozen English taxonomy.
2. Draw a random sample of 10 development papers (seed 20261002).
3. Record, for each sampled paper, which large patterns the one-pass extraction + mapping found (data-v2),
   kept in onepass.json and NOT given to the re-reading agents.
"""
import csv, json, random, re
from pathlib import Path

HERE = Path(__file__).parent
RUN = HERE.parents[1]
tax = (RUN / '02-pattern-extraction' / '04-integrated-pattern-taxonomy' / 'pattern-taxonomy-v2.0-en.md').read_text(encoding='utf-8')

lines = ['# Pattern list for re-reading', '',
         'Reasoning patterns (RP) are judgments a study makes: what it must understand, judge, or justify.',
         'Execution patterns (EP) are concrete research activities a study carries out.', '']
for block in re.split(r'\n### ', tax)[1:]:
    head = block.split('\n', 1)[0]
    m = re.match(r'((RP|EP)\d\d) (.*)', head)
    if not m:
        continue
    pid, name = m.group(1), m.group(3).replace(' (new)', '').replace(' (former RP08)', '')
    core = re.search(r'\*\*Core (question|task):\*\* (.*)', block).group(2)
    lines.append(f'## {pid} {name}')
    lines.append(f'Core {"question" if pid.startswith("RP") else "task"}: {core}')
    for row in block.split('\n'):
        sm = re.match(r'^\| \*\*((?:RP|EP)\d\d-[A-H])\*\* ([^|]*)\|', row)
        if not sm:
            continue
        cells = [c.strip() for c in row.strip().strip('|').split('|')]
        # columns: name, [label,] description, steps, papers, strength
        desc = cells[-4]
        lines.append(f'- {sm.group(1)} {sm.group(2).strip()}: {desc}')
    lines.append('')
(HERE / 'pattern-list.md').write_text('\n'.join(lines), encoding='utf-8')

random.seed(20261002)
sample = sorted(random.sample([f'E{i:02d}' for i in range(1, 51)], 10))

found = {p: set() for p in sample}
for r in csv.DictReader(open(RUN / '04-development-50-backtest' / 'semantic-map' / 'data-v2' / 'final-positive-matches-v2.csv', encoding='utf-8-sig')):
    if r['paper_id'] in found:
        found[r['paper_id']].add(r['pattern_id'])
json.dump({p: sorted(v) for p, v in found.items()}, open(HERE / 'onepass.json', 'w'), indent=1)
json.dump(sample, open(HERE / 'sample.json', 'w'))
print('sample', sample)
print({p: len(v) for p, v in found.items()})
print('pattern-list lines', len(lines), 'small entries', sum(1 for l in lines if l.startswith('- ')))
