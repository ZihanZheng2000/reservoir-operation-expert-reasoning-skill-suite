"""Compare one-pass (A) and pattern-guided re-reading (B); list recoveries for evidence checking."""
import json
from pathlib import Path

HERE = Path(__file__).parent
sample = json.load(open(HERE / 'sample.json'))
onepass = {k: set(v) for k, v in json.load(open(HERE / 'onepass.json')).items()}
ALL = [f'RP0{i}' for i in range(1, 10)] + [f'EP{i:02d}' for i in range(1, 12)]

rows, recov = [], []
for p in sample:
    d = json.load(open(HERE / 'reread' / f'{p}.json', encoding='utf-8'))['patterns']
    assert set(d) == set(ALL), (p, set(ALL) ^ set(d))
    b = {k for k, v in d.items() if v.get('present')}
    a = onepass[p]
    rec = sorted(b - a)
    rows.append((p, len(a), len(b), len(a & b), len(rec), len(a - b), sorted(a - b)))
    for k in rec:
        recov.append((p, k, d[k].get('small'), d[k].get('quote'), d[k].get('where')))

out = ['| Paper | One-pass | Re-read | Both | Recovered (B only) | One-pass only | One-pass only patterns |', '|---|---:|---:|---:|---:|---:|---|']
for r in rows:
    out.append(f'| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {", ".join(r[6]) or "-"} |')
tot = [sum(r[i] for r in rows) for i in range(1, 6)]
out.append(f'| Total | {tot[0]} | {tot[1]} | {tot[2]} | {tot[3]} | {tot[4]} | |')
out += ['', '## Recoveries to check', '']
for p, k, sm, q, w in recov:
    out.append(f'- **{p} {k}** {sm} ({w}): "{q}"')
(HERE / 'comparison-raw.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print('\n'.join(out))
