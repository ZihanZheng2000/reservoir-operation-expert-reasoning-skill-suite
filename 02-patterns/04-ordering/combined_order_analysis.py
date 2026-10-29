"""Combined ordering of reasoning and execution patterns on one timeline, plus the reasoning-execution pairing table.

Each card's section 4 ("Functional abstraction and paper-specific realization") pairs reasoning steps with the
execution steps they drive, for example "R3 / E4" or "R4 / E5–E6". These pairs put both layers on one timeline:
- execution step Ek sits at position k;
- a paired reasoning step sits just before the first execution step it is paired with (position min(k) - 0.5);
- an unpaired reasoning step is placed by linear interpolation between the neighbouring paired reasoning steps
  in reasoning order (or 0.5 before / after the first / last one).
Then: per paper, each pattern's position is the mean position of its primary steps;
pairwise precedence over papers containing both; exact Kemeny ranking of all 20 patterns (subset dynamic
programming, vectorized by subset size); 300 paper bootstrap resamples (seed 1).

Inputs:  ../../01-corpus/development-50/cards/Exx-card.md (section 4), ../03-step-coding/step-coding.csv
Outputs: combined-order-results.md, rp-ep-pairing.csv (papers in which an RP step and an EP step are paired)
Usage:   python combined_order_analysis.py
"""
import collections, csv, itertools, random, re, statistics as st
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
V3 = HERE.parents[1]
CARDS = V3 / '01-corpus' / 'development-50' / 'cards'
RP = [f'RP0{i}' for i in range(1, 10)]
EP = [f'EP{i:02d}' for i in range(1, 12)]


def expand(cell, layer):
    out = set()
    for a, b in re.findall(rf'{layer}(\d+)(?:\s*[–-]\s*{layer}?(\d+))?', cell):
        a = int(a); b = int(b) if b else a
        out |= set(range(a, b + 1))
    return out


def load():
    coding = list(csv.DictReader((HERE.parent / '03-step-coding' / 'step-coding.csv').open(encoding='utf-8-sig')))
    prim = {c['step_key']: c['primary'] for c in coding if c['primary']}
    nsteps = collections.defaultdict(lambda: {'R': 0, 'E': 0})
    for c in coding:
        p, s = c['step_key'].split('-')
        nsteps[p][s[0]] = max(nsteps[p][s[0]], int(s[1:]))
    links, pairing = {}, collections.defaultdict(set)
    for f in sorted(CARDS.glob('E??-card.md')):
        pid = f.name[:3]
        sec = re.search(r'## 4\..*?\n(.*?)\n## 5\.', f.read_text(encoding='utf-8'), re.S).group(1)
        lk = collections.defaultdict(set)
        for line in sec.splitlines():
            if not line.startswith('|') or line.startswith('|---') or 'Important step' in line:
                continue
            cell = line.split('|')[1]
            rs, es = expand(cell, 'R'), expand(cell, 'E')
            for r in rs:
                lk[r] |= es
            for r in rs:
                for e in es:
                    a, b = prim.get(f'{pid}-R{r}'), prim.get(f'{pid}-E{e}')
                    if a and b:
                        pairing[(a, b)].add(pid)
        links[pid] = lk
    return prim, nsteps, links, pairing


def positions(prim, nsteps, links):
    pos = collections.defaultdict(lambda: collections.defaultdict(list))   # paper -> pattern -> positions
    for pid, n in nsteps.items():
        rpos = {r: min(links[pid][r]) - 0.5 for r in range(1, n['R'] + 1) if links[pid].get(r)}
        known = sorted(rpos)
        for r in range(1, n['R'] + 1):
            if r in rpos:
                continue
            lo = max((k for k in known if k < r), default=None)
            hi = min((k for k in known if k > r), default=None)
            if lo and hi:
                rpos[r] = rpos[lo] + (rpos[hi] - rpos[lo]) * (r - lo) / (hi - lo)
            elif lo:
                rpos[r] = rpos[lo] + 0.5 * (r - lo)
            elif hi:
                rpos[r] = rpos[hi] - 0.5 * (hi - r)
        for r, x in rpos.items():
            if prim.get(f'{pid}-R{r}'):
                pos[pid][prim[f'{pid}-R{r}']].append(x)
        for e in range(1, n['E'] + 1):
            if prim.get(f'{pid}-E{e}'):
                pos[pid][prim[f'{pid}-E{e}']].append(e)
    return {p: {k: st.mean(v) for k, v in d.items()} for p, d in pos.items()}


def prec(papers, pos, items):
    idx = {a: i for i, a in enumerate(items)}
    win = np.zeros((len(items), len(items)), dtype=np.int64)
    tot = np.zeros_like(win)
    for p in papers:
        m = pos[p]
        for a, b in itertools.combinations(sorted(m), 2):
            if m[a] == m[b]:
                continue
            i, j = idx[a], idx[b]
            tot[i, j] += 1; tot[j, i] += 1
            if m[a] < m[b]:
                win[i, j] += 1
            else:
                win[j, i] += 1
    return win, tot


def kemeny(win):
    """Exact Kemeny order maximizing sum of win[i, j] over pairs with i placed before j.
    best[S] = best score of ordering set S first; adding i after S gains sum_{j in S} win[j, i]."""
    n = win.shape[0]
    N = 1 << n
    masks = np.arange(N, dtype=np.int64)
    pop = np.zeros(N, dtype=np.int8)
    for b in range(n):
        pop += ((masks >> b) & 1).astype(np.int8)
    colsum = np.zeros((N, n), dtype=np.int32)          # colsum[S, i] = sum_{j in S} win[j, i]
    for b in range(n):
        has = (masks >> b) & 1 == 1
        colsum[has] += win[b].astype(np.int32)
    best = np.full(N, -1, dtype=np.int64)
    best[0] = 0
    choice = np.zeros(N, dtype=np.int8)
    for k in range(1, n + 1):
        layer = masks[pop == k]
        for i in range(n):
            sel = layer[(layer >> i) & 1 == 1]
            prev = sel ^ (1 << i)
            cand = best[prev] + colsum[prev, i]
            upd = cand > best[sel]
            best[sel[upd]] = cand[upd]
            choice[sel[upd]] = i
    order, m = [], N - 1
    while m:
        i = int(choice[m]); order.append(i); m ^= 1 << i
    return order[::-1]


def main():
    prim, nsteps, links, pairing = load()
    pos = positions(prim, nsteps, links)
    papers = sorted(pos)
    items = RP + EP
    win, tot = prec(papers, pos, items)
    order = [items[i] for i in kemeny(win)]
    random.seed(1)
    boots = []
    for b in range(300):
        smp = [random.choice(papers) for _ in papers]
        w, _ = prec(smp, pos, items)
        boots.append([items[i] for i in kemeny(w)])
    rank = {a: sorted(bo.index(a) + 1 for bo in boots) for a in items}
    idx = {a: i for i, a in enumerate(items)}
    out = ['# Combined ordering of reasoning and execution patterns', '',
           'Generated by `combined_order_analysis.py`. Reasoning steps are placed on the execution timeline through the '
           'R/E pairs in section 4 of each card; see the script docstring for the placement rule.', '',
           '## Consensus order (exact Kemeny)', '', ' > '.join(order), '',
           '| Rank | Pattern | Layer | Bootstrap rank range (5-95%) |', '|---:|---|---|---|']
    out += [f'| {i} | {a} | {"reasoning" if a.startswith("RP") else "execution"} | {rank[a][15]}-{rank[a][284]} |'
            for i, a in enumerate(order, 1)]
    out += ['', '## Adjacent pairs', '', '| Pair | P(before) | n papers | Bootstrap share keeping this order |', '|---|---:|---:|---:|']
    for a, b in zip(order, order[1:]):
        n = tot[idx[a], idx[b]]
        p = win[idx[a], idx[b]] / n if n else float('nan')
        keep = sum(bo.index(a) < bo.index(b) for bo in boots) / len(boots)
        out.append(f'| {a} > {b} | {p:.2f} | {n} | {keep:.0%} |')
    out += ['', '## Reasoning-execution pairing', '',
            'Number of papers in which a step coded to the reasoning pattern (row) is paired in section 4 with a step '
            'coded to the execution pattern (column); primary codes only. Full table in `rp-ep-pairing.csv`.', '',
            '| | ' + ' | '.join(EP) + ' | Main pair |', '|---|' + '---:|' * len(EP) + '---|']
    for r in RP:
        cnt = [len(pairing[(r, e)]) for e in EP]
        mx = max(cnt)
        main = ', '.join(e for e, c in zip(EP, cnt) if c == mx)
        out.append(f'| {r} | ' + ' | '.join(str(c) for c in cnt) + f' | {main} ({mx}) |')
    (HERE / 'combined-order-results.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    with (HERE / 'rp-ep-pairing.csv').open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['reasoning_pattern', 'execution_pattern', 'papers', 'paper_ids'])
        for r in RP:
            for e in EP:
                if pairing[(r, e)]:
                    w.writerow([r, e, len(pairing[(r, e)]), ' '.join(sorted(pairing[(r, e)]))])
    print('\n'.join(out[:40]))


if __name__ == '__main__':
    main()
