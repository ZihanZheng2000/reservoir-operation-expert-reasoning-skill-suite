"""Split the 50 development cards into steps.

Input:  ../../01-corpus/development-50/cards/Exx-card.md (reasoning rows R1..Rn and execution rows E1..En)
Output: step-inventory.csv, reasoning-steps.md, execution-steps.md
Usage:  python build_steps.py
"""
import csv, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
V3 = HERE.parents[1]
CARDS = V3 / '01-corpus' / 'development-50' / 'cards'
STEP = re.compile(r'^\|\s*([RE])(\d+)\.\s*([^|]+)\|', re.ASCII)
FIELDS = ['step_key', 'paper_id', 'layer', 'step_id', 'step_title', 'source_file', 'source_line',
          'step_description', 'retained_details', 'evidence_boundary', 'raw_row']


def cells(row):
    """Split a card step row into its 4 cells: step | description | retained details | evidence.
    Formulas inside cells can contain '|' (absolute values, conditional probabilities), so the cell
    separators are found from the row structure: separators are '|' with whitespace on both sides;
    the first is the first such '|', the second is the one right before '**Trigger:**' (retained details
    always start with it), and the third is the last one. Falls back to a plain split if that fails."""
    body = row.rstrip('\n\r')[1:-1]
    seps = [m.start() for m in re.finditer(r'(?<=\s)\|(?=\s)', body)]
    trig = [p for p in seps if body[p + 1:].lstrip().startswith('**Trigger')]
    if len(seps) >= 3 and len(trig) == 1 and seps[0] < trig[0] < seps[-1]:
        a, b, c = seps[0], trig[0], seps[-1]
        return [body[:a].strip(), body[a + 1:b].strip(), body[b + 1:c].strip(), body[c + 1:].strip()]
    return [c.strip() for c in re.split(r'(?<!\\)\|', row.rstrip('\n\r'))[1:-1]]


def main():
    rows = []
    for path in sorted(CARDS.glob('E??-card.md')):
        pid = path.stem.split('-')[0]
        for n, line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(), 1):
            m = STEP.match(line)
            if not m:
                continue
            layer, num, title = m.groups()
            c = cells(line)
            rows.append({'step_key': f'{pid}-{layer}{num}', 'paper_id': pid, 'layer': layer, 'step_id': f'{layer}{num}',
                         'step_title': title.strip(), 'source_file': path.relative_to(V3).as_posix(), 'source_line': n,
                         'step_description': c[1] if len(c) > 1 else '', 'retained_details': c[2] if len(c) > 2 else '',
                         'evidence_boundary': c[3] if len(c) > 3 else '', 'raw_row': line})
    with (HERE / 'step-inventory.csv').open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    for layer, name, title in (('R', 'reasoning-steps.md', 'Reasoning'), ('E', 'execution-steps.md', 'Execution')):
        out = [f'# E01–E50 {title} Steps', '']
        for pid in sorted({r['paper_id'] for r in rows}):
            out += [f'## {pid}', '', '| Step |', '|---|']
            out += [f"| {r['step_id']}. {r['step_title']} |" for r in rows if r['paper_id'] == pid and r['layer'] == layer]
            out.append('')
        (HERE / name).write_text('\n'.join(out), encoding='utf-8')
    print(f"{len(rows)} steps: {sum(r['layer'] == 'R' for r in rows)} reasoning, {sum(r['layer'] == 'E' for r in rows)} execution")


if __name__ == '__main__':
    main()
