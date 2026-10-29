"""Figures for the pattern-guided re-reading back-test (discussion D1), in the style of v3/05-results.

Inputs (copied unchanged into v3/06-discussion/d1-pattern-guided-rereading/data/):
  onepass.json  - large patterns found per paper by one-pass extraction + step coding (same as v3 step coding, any match)
  reread/*.json - large patterns found by pattern-guided re-reading, with quotes
  Recoveries judged not supported by their quote (project coder, 2026-10-02) are listed in NOT_SUPPORTED below,
  copied from judge_and_summarize.py.
Usage: python rereading_figures.py <data folder> <output folder>
"""
import json, sys
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

DATA, OUT = Path(sys.argv[1]), Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)
SURF, INK, INK2, MUTED, GRID = '#ffffff', '#0b0b0b', '#52514e', '#8a8984', '#e7e6e2'
BLUE, GRAY = '#2a78d6', '#c9c8c3'
plt.rcParams.update({
    'font.family': 'Arial', 'font.size': 10, 'text.color': INK, 'axes.labelcolor': INK2, 'axes.edgecolor': GRID,
    'xtick.color': INK2, 'ytick.color': INK2, 'figure.facecolor': SURF, 'axes.facecolor': SURF,
    'savefig.facecolor': SURF, 'svg.fonttype': 'none', 'axes.spines.top': False, 'axes.spines.right': False,
})
NOT_SUPPORTED = {('E10', 'RP05'), ('E11', 'EP07'), ('E23', 'RP05'), ('E26', 'EP04'), ('E35', 'RP01')}
PATTERNS = [f'RP0{i}' for i in range(1, 10)] + [f'EP{i:02d}' for i in range(1, 12)]

sample = json.loads((DATA / 'sample.json').read_text(encoding='utf-8'))
onepass = {k: set(v) for k, v in json.loads((DATA / 'onepass.json').read_text(encoding='utf-8')).items()}
reread = {p: {k for k, v in json.loads((DATA / 'reread' / f'{p}.json').read_text(encoding='utf-8'))['patterns'].items()
              if v.get('present')} for p in sample}
recovered = {p: {k for k in reread[p] - onepass[p] if (p, k) not in NOT_SUPPORTED} for p in sample}


def title(fig, text, sub):
    fig.text(0.0, 1.0, text, ha='left', va='bottom', fontsize=14, fontweight='bold', color=INK)
    fig.text(0.0, 0.985, sub, ha='left', va='top', fontsize=10, color=INK2)


def save(fig, name):
    for ext, kw in (('png', {'dpi': 220}), ('svg', {})):
        fig.savefig(OUT / f'{name}.{ext}', bbox_inches='tight', pad_inches=0.25, **kw)
    plt.close(fig)


def stacked(ax, labels, base, add, ymax, ylabel):
    x = range(len(labels))
    ax.bar(x, base, color=GRAY, width=0.68, edgecolor=SURF, linewidth=1.5)
    ax.bar(x, add, bottom=base, color=BLUE, width=0.68, edgecolor=SURF, linewidth=1.5)
    for i, (b, a) in enumerate(zip(base, add)):
        if a:
            ax.text(i, b + a + 0.15, f'+{a}', ha='center', va='bottom', fontsize=9.5, color=BLUE, fontweight='bold')
    ax.set_xticks(list(x), labels)
    ax.set_ylim(0, ymax)
    ax.set_ylabel(ylabel)
    ax.grid(axis='y', color=GRID, lw=0.8)
    ax.set_axisbelow(True)
    ax.tick_params(length=0)


# per paper
fig, ax = plt.subplots(figsize=(9, 4.3))
base = [len(onepass[p]) for p in sample]
add = [len(recovered[p]) for p in sample]
stacked(ax, sample, base, add, 21, 'Large patterns found in the paper (of 20)')
ax.set_yticks([0, 5, 10, 15, 20])
tot_b, tot_a = sum(base), sum(add)
ax.legend(handles=[Patch(color=GRAY, label=f'One-pass extraction ({tot_b})'),
                   Patch(color=BLUE, label=f'Added by pattern-guided re-reading (+{tot_a})')],
          loc='lower left', bbox_to_anchor=(0, 1.0), ncol=2, frameon=False, fontsize=9.5)
title(fig, f'Reading a paper once misses about one in five patterns it uses',
      f'10 random development papers. One-pass extraction found {tot_b} of {tot_b + tot_a} pattern occurrences '
      f'({tot_b / (tot_b + tot_a):.0%}).\nRe-reading the full text with the pattern list in hand added {tot_a} more '
      f'(+{tot_a / tot_b:.0%}), '
      'each backed by a verbatim quote.')
fig.subplots_adjust(top=0.76)
save(fig, 'd1-rereading-by-paper')

print('one-pass', tot_b, 'recovered', tot_a, 'union', tot_b + tot_a)
