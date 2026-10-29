"""Evidence check of the recovered patterns (project coder, 2026-10-02) and summary tables."""
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
sample = json.load(open(HERE / 'sample.json'))
onepass = {k: set(v) for k, v in json.load(open(HERE / 'onepass.json')).items()}
reread = {p: {k for k, v in json.load(open(HERE / 'reread' / f'{p}.json', encoding='utf-8'))['patterns'].items() if v.get('present')}
          for p in sample}

# Recoveries judged NOT supported by the quoted evidence (all others supported)
NOT_SUPPORTED = {
    ('E10', 'RP05'): 'Quote lists model constraints; no feasibility judgment by the study.',
    ('E11', 'EP07'): 'Statement about a probability; no risk calculation shown in the quote.',
    ('E23', 'RP05'): 'Describes optimizer behaviour, not a judgment about downstream/system limits.',
    ('E26', 'EP04'): 'States a distribution; does not show propagation through a reservoir simulation.',
    ('E35', 'RP01'): 'Evaluates the deterministic method, not a limitation of the current operating rule.',
}

rows = []
recovered_ok = Counter()
for p in sample:
    rec = reread[p] - onepass[p]
    ok = {k for k in rec if (p, k) not in NOT_SUPPORTED}
    for k in ok:
        recovered_ok[k] += 1
    union = onepass[p] | ok
    rows.append(dict(paper=p, onepass=len(onepass[p]), recovered=len(ok), rejected=len(rec) - len(ok),
                     onepass_only=len(onepass[p] - reread[p]), union=len(union)))

tot = {k: sum(r[k] for r in rows) for k in ['onepass', 'recovered', 'rejected', 'onepass_only', 'union']}
out = ['# Pattern-guided re-reading: results', '',
       'Sample: 10 random development papers. A = one-pass extraction + mapping; B = re-reading with the pattern list.', '',
       '| Paper | One-pass patterns | Recovered (supported) | Rejected recoveries | Found only in one-pass | Patterns after re-reading |',
       '|---|---:|---:|---:|---:|---:|']
for r in rows:
    out.append(f"| {r['paper']} | {r['onepass']} | {r['recovered']} | {r['rejected']} | {r['onepass_only']} | {r['union']} |")
out.append(f"| Total | {tot['onepass']} | {tot['recovered']} | {tot['rejected']} | {tot['onepass_only']} | {tot['union']} |")
out += ['', f"One-pass found {tot['onepass']} of {tot['union']} pattern occurrences ({100 * tot['onepass'] / tot['union']:.0f}%); "
        f"re-reading added {tot['recovered']} supported occurrences (+{100 * tot['recovered'] / tot['onepass']:.0f}%).", '',
        '## Most often recovered patterns', '']
out += [f'- {k}: {v} papers' for k, v in recovered_ok.most_common()]
out += ['', '## Rejected recoveries', ''] + [f'- {p} {k}: {why}' for (p, k), why in NOT_SUPPORTED.items()]

# corpus-level: patterns present in the 10-paper sample before and after
before = set().union(*onepass.values())
after = before | {k for k in recovered_ok}
ALL = [f'RP0{i}' for i in range(1, 10)] + [f'EP{i:02d}' for i in range(1, 12)]
out += ['', '## Corpus level', '',
        f'Distinct large patterns present in the 10 papers: one-pass {len(before)}, after re-reading {len(after)}.',
        f'Patterns absent in both: {", ".join(p for p in ALL if p not in after) or "none"}.',
        'Every recovered pattern was already present in other papers in the one-pass results, so no new pattern was discovered.']
per = []
for k in ALL:
    a = sum(k in onepass[p] for p in sample)
    b = sum(k in (onepass[p] | {x for x in reread[p] - onepass[p] if (p, x) not in NOT_SUPPORTED}) for p in sample)
    per.append((k, a, b))
out += ['', '| Pattern | Papers (one-pass) | Papers (after re-reading) |', '|---|---:|---:|'] + [f'| {k} | {a} | {b} |' for k, a, b in per]
(HERE / 'results.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
json.dump(dict(rows=rows, total=tot, per_pattern=per, recovered=recovered_ok, before=len(before), after=len(after)),
          open(HERE / 'results.json', 'w'), indent=1)
print('\n'.join(out))
