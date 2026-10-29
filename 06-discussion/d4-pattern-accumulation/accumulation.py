"""Pattern accumulation curves (discussion D4): how many distinct large and small patterns appear in n papers.

For n = 1..50, draw 2,000 random subsets of n development papers (seed 20261029) and count the distinct large patterns
(RP/EP) and small patterns (e.g. RP02-E) whose steps occur in those papers. A step counts for a small pattern if the
small pattern is its family or its secondary family; a paper counts for a large pattern if any of its steps is
assigned to that pattern (primary or secondary match), as in v3/02-patterns/03-step-coding/pattern-coverage.csv.
Also reports papers per small pattern and the Chao1 estimate of how many small patterns a larger corpus might hold.
Input:  v3/02-patterns/05-small-patterns/{reasoning,execution}/*-assignment.csv
Usage:  python accumulation.py <v3 folder> <output folder>
"""
import csv, json, random, sys
from collections import defaultdict
from pathlib import Path
from statistics import mean

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

V3, OUT = Path(sys.argv[1]), Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)
SURF, INK, INK2, MUTED, GRID = '#ffffff', '#0b0b0b', '#52514e', '#8a8984', '#e7e6e2'
BLUE, ORANGE = '#2a78d6', '#eb6834'
plt.rcParams.update({
    'font.family': 'Arial', 'font.size': 10, 'text.color': INK, 'axes.labelcolor': INK2, 'axes.edgecolor': GRID,
    'xtick.color': INK2, 'ytick.color': INK2, 'figure.facecolor': SURF, 'axes.facecolor': SURF,
    'savefig.facecolor': SURF, 'svg.fonttype': 'none', 'axes.spines.top': False, 'axes.spines.right': False,
})

large, small = defaultdict(set), defaultdict(set)
for f in sorted((V3 / '02-patterns' / '05-small-patterns').glob('*/*-assignment.csv')):
    pid = f.name[:4]
    with f.open(encoding='utf-8-sig') as fh:
        for r in csv.DictReader(fh):
            large[r['paper_id']].add(pid)
            for fam in (r['family'], r['secondary_family']):
                if fam:
                    small[r['paper_id']].add(fam)
papers = sorted(large)
N, R = len(papers), 2000
all_small = set().union(*small.values())
rng = random.Random(20261029)
curve = {}
for n in range(1, N + 1):
    L, S = [], []
    for _ in range(R):
        sub = rng.sample(papers, n)
        L.append(len(set().union(*(large[p] for p in sub))))
        S.append(len(set().union(*(small[p] for p in sub))))
    L.sort(); S.sort()
    q = lambda xs, a: xs[int(a * (R - 1))]
    curve[n] = dict(large=mean(L), large_lo=q(L, 0.05), large_hi=q(L, 0.95),
                    small=mean(S), small_lo=q(S, 0.05), small_hi=q(S, 0.95))

# papers per small pattern, singletons and Chao1
freq = {s: sum(s in small[p] for p in papers) for s in all_small}
f1 = sum(v == 1 for v in freq.values())
f2 = sum(v == 2 for v in freq.values())
chao1 = len(all_small) + (f1 * f1 / (2 * f2) if f2 else f1 * (f1 - 1) / 2)
summary = dict(papers=N, large_total=len(set().union(*large.values())), small_total=len(all_small),
               per_paper_large=mean(len(large[p]) for p in papers), per_paper_small=mean(len(small[p]) for p in papers),
               small_in_1_paper=f1, small_in_2_papers=f2, chao1_small=round(chao1, 1),
               curve={n: {k: round(v, 2) for k, v in c.items()} for n, c in curve.items()})
(OUT / 'accumulation.json').write_text(json.dumps(summary, indent=1), encoding='utf-8')

rows = [1, 2, 3, 5, 10, 15, 20, 30, 40, 50]
md = ['| Papers | Large patterns (of 20): mean [5–95%] | Small patterns (of 104): mean [5–95%] |', '|---:|---|---|']
for n in rows:
    c = curve[n]
    md.append(f"| {n} | {c['large']:.1f} [{c['large_lo']}–{c['large_hi']}] | {c['small']:.1f} [{c['small_lo']}–{c['small_hi']}] |")
(OUT / 'accumulation-table.md').write_text('\n'.join(md) + '\n', encoding='utf-8')

# figure
fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.6))
for ax, key, tot, col, lab in ((axes[0], 'large', 20, BLUE, 'Large patterns (20 in total)'),
                               (axes[1], 'small', len(all_small), ORANGE, f'Small patterns ({len(all_small)} in total)')):
    xs = list(curve)
    ax.fill_between(xs, [curve[n][f'{key}_lo'] for n in xs], [curve[n][f'{key}_hi'] for n in xs], color=col, alpha=0.15,
                    lw=0)
    ax.plot(xs, [curve[n][key] for n in xs], color=col, lw=2.2)
    ax.axhline(tot, color=MUTED, lw=1, ls=(0, (3, 3)))
    for n in (1, 5, 20):
        v = curve[n][key]
        ax.scatter([n], [v], s=40, color=col, edgecolor=SURF, linewidth=1.5, zorder=3)
        ax.annotate(f'{n} paper{"s" if n > 1 else ""}: {v:.1f}' if key == 'large' else f'{n} paper{"s" if n > 1 else ""}: {v:.0f}', (n, v), textcoords='offset points', xytext=(8, -14),
                    fontsize=9.5, color=INK)
    ax.set_title(lab, fontsize=11.5, fontweight='bold', loc='left', pad=8)
    ax.set_xlim(0, 51)
    ax.set_ylim(0, tot * 1.08)
    if key == 'large':
        ax.set_yticks([0, 5, 10, 15, 20])
    ax.set_xlabel('Number of papers (random subsets of the 50 development papers)')
    ax.grid(color=GRID, lw=0.8)
    ax.set_axisbelow(True)
axes[0].set_ylabel('Distinct patterns found')
fig.text(0.0, 1.0, 'Five papers show nearly all large patterns; small patterns need about 30 papers',
         ha='left', va='bottom', fontsize=14, fontweight='bold')
fig.text(0.0, 0.985, f'Mean over 2,000 random subsets per size; band = 5–95% range. One paper shows '
         f"{summary['per_paper_large']:.1f} large and {summary['per_paper_small']:.1f} small patterns on average. "
         f'{f1} small patterns occur in only one paper.', ha='left', va='top', fontsize=10, color=INK2)
fig.subplots_adjust(top=0.80, wspace=0.18)
for ext, kw in (('png', {'dpi': 220}), ('svg', {})):
    fig.savefig(OUT / f'd4-pattern-accumulation.{ext}', bbox_inches='tight', pad_inches=0.25, **kw)
print(json.dumps({k: v for k, v in summary.items() if k != 'curve'}, indent=1))
print('\n'.join(md))
