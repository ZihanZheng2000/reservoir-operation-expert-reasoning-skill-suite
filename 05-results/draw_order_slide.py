"""Slide version of the combined reasoning/execution order diagram (English): compact layout, large fonts.

Same content as v3/02-patterns/04-ordering/draw_combined_order.py --en (order, stages, arrow percentages, pairing
counts, paper counts); only the layout and type sizes change. Coordinates are in inches (1 unit = 1 inch).
Writes out/fig0-expert-research-order.{png,svg} (no figure title; lanes labelled Reason / Execute).
Usage: python draw_order_slide.py
"""
import csv
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

HERE = Path(__file__).resolve().parent
V3P = HERE.parents[3] / 'v3' / '02-patterns'
OUT = HERE / 'out'
plt.rcParams.update({'font.family': ['Arial', 'Segoe UI Symbol', 'DejaVu Sans'], 'svg.fonttype': 'none'})
SURF, INK, INK2, MUTED = '#ffffff', '#0b0b0b', '#52514e', '#9a9893'
ACC, NODE, ZONE, PAIR = '#2a78d6', '#ffffff', '#eef3fb', '#c06a2b'
COMMON, CONDITIONAL = 30, 15
with (V3P / '03-step-coding' / 'pattern-coverage.csv').open(encoding='utf-8-sig') as f:
    PAPERS = {r['pattern_id']: int(r['papers_any_match']) for r in csv.DictReader(f)}
with (V3P / '04-ordering' / 'rp-ep-pairing.csv').open(encoding='utf-8-sig') as f:
    PAIRN = {(r['reasoning_pattern'], r['execution_pattern']): int(r['papers']) for r in csv.DictReader(f)}

NAME = {
    'RP01': 'Diagnose rule\nlimitations', 'RP02': 'Decision-relevant\nuncertainty', 'RP03': 'Forecast reliability\nand timing',
    'RP04': 'Risk and\nacceptable safety', 'RP05': 'Operational\nfeasibility', 'RP06': 'Trade-offs and\nselection',
    'RP07': 'Adaptive\nflood-stage logic', 'RP08': 'Model and\nmethod choice', 'RP09': 'Evidence and\napplicability',
    'EP01': 'Data and\nbaseline rules', 'EP02': 'Build and verify\nforecasts', 'EP03': 'Uncertainty and\nscenarios',
    'EP04': 'Simulate reservoir\nresponse', 'EP05': 'Safety bounds', 'EP06': 'Candidate plans',
    'EP07': 'Risk, losses\nand benefits', 'EP08': 'Criteria and\nselection', 'EP09': 'Staged rolling\nactions',
    'EP10': 'Compare and\ntest policies', 'EP11': 'Consult, pilot\nand revise',
}

# ---- geometry (inches) -------------------------------------------------------------------------------------
W, H = 2.1, 1.25            # box
G_COL, PAD, G_ZONE = 0.45, 0.14, 0.62
TOP, TOP2, BOT, BOT2 = 6.2, 4.75, 2.6, 0.92
X0 = 0.95                    # left edge of the first zone (lane labels sit left of it)


def zone_span(x0, ncol):
    return x0, x0 + 2 * PAD + ncol * W + (ncol - 1) * G_COL


Z = []
x = X0
for ncol in (1, 2, 3, 1):
    a, b = zone_span(x, ncol)
    Z.append((a, b))
    x = b + G_ZONE
col = lambda z, i: Z[z][0] + PAD + W / 2 + i * (W + G_COL)

P = {
    'RP01': (col(0, 0), TOP), 'EP01': (col(0, 0), BOT),
    'RP02': (col(1, 0), TOP), 'RP03': (col(1, 1), TOP),
    'EP02': (col(1, 0), BOT), 'EP03': (col(1, 1), BOT), 'EP04': (col(1, 1), BOT2),
    'RP04': (col(2, 0), TOP), 'RP06': (col(2, 1), TOP), 'RP05': (col(2, 2), TOP),
    'RP07': (col(2, 0.5), TOP2), 'RP08': (col(2, 1.5), TOP2),
    'EP07': (col(2, 0), BOT), 'EP06': (col(2, 1), BOT), 'EP05': (col(2, 2), BOT),
    'EP09': (col(2, 0.5), BOT2), 'EP08': (col(2, 1.5), BOT2),
    'RP09': (col(3, 0), TOP), 'EP10': (col(3, 0), BOT), 'EP11': (col(3, 0), BOT2),
}
WIDTH = Z[-1][1] + 0.15
YMIN, YMAX = -1.55, 8.75


def border(n):
    if n >= COMMON:
        return dict(ec=INK, lw=2.2, ls='-')
    if n >= CONDITIONAL:
        return dict(ec=INK2, lw=1.7, ls=(0, (5, 3)))
    return dict(ec=MUTED, lw=1.7, ls=(0, (1, 2.2)))


def side(pid, s, dx=0.0):
    x, y = P[pid]
    return {'r': (x + W / 2, y), 'l': (x - W / 2, y), 't': (x + dx, y + H / 2), 'b': (x + dx, y - H / 2)}[s]


def label(ax, x, y, text, color=INK2, size=12, bg=ZONE, **kw):
    ax.text(x, y, text, ha=kw.pop('ha', 'center'), va=kw.pop('va', 'center'), fontsize=size, color=color, zorder=6,
            bbox=dict(fc=bg, ec='none', pad=0.5), **kw)


def arrow(ax, p, q, color=ACC, lw=2.6, rad=0.0, ls='-'):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle='-|>', mutation_scale=18, lw=lw, color=color, ls=ls, shrinkA=1,
                                 shrinkB=1, zorder=3, connectionstyle=f'arc3,rad={rad}'))


def pair_line(ax, p, q):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=PAIR, lw=1.8, ls=(0, (2, 2)), zorder=2)


def draw():
    ymax, ymin = 7.85, -1.75
    fig = plt.figure(figsize=(WIDTH, ymax - ymin))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(ymin, ymax)
    ax.axis('off')
    fig.patch.set_facecolor(SURF)

    stages = [('① Define the problem', 'Stable: always first'),
              ('② Understand uncertainty and forecasts', 'Mostly stable'),
              ('③ Design and compute plans', 'No fixed order inside · judge (top) before compute (bottom) · repeats'),
              ('④ Test', 'Stable: always last')]
    for (a, b), (t, n) in zip(Z, stages):
        ax.add_patch(FancyBboxPatch((a, -0.42), b - a, 7.42, boxstyle='round,pad=0,rounding_size=0.18', fc=ZONE, ec=ACC,
                                    lw=1.3, ls=(0, (4, 3)), zorder=1))
        ax.text((a + b) / 2, 7.55, t, ha='center', va='center', fontsize=17, weight='bold', color=INK)
        ax.text((a + b) / 2, 7.2, n, ha='center', va='center', fontsize=12, color=INK2)
    for y, t in ((TOP, 'Reason'), (BOT, 'Execute')):
        ax.text(0.5, y, t, ha='center', va='center', fontsize=18, weight='bold', color=INK, rotation=90)

    # reasoning-execution pairs (dotted) with paper counts
    vert = {('RP04', 'EP07'), ('RP05', 'EP05'), ('RP06', 'EP06'), ('RP07', 'EP09')}
    for a, b in vert:
        p, q = side(a, 'b'), side(b, 't')
        pair_line(ax, p, q)
        ymid = (TOP2 - H / 2 + BOT + H / 2) / 2
        label(ax, p[0], ymid, str(PAIRN[(a, b)]), color=PAIR, size=12.5)
    for a, b, f in (('RP02', 'EP03', 0.78), ('RP03', 'EP02', 0.78)):
        p, q = side(a, 'b'), side(b, 't')
        pair_line(ax, p, q)
        label(ax, p[0] + (q[0] - p[0]) * f, p[1] + (q[1] - p[1]) * f, str(PAIRN[(a, b)]), color=PAIR, size=12.5)
    for a, b in (('RP01', 'EP01'), ('RP09', 'EP10')):     # pair and stable order share the same two boxes
        p, q = side(a, 'b', 0.45), side(b, 't', 0.45)
        pair_line(ax, p, q)
        label(ax, p[0], (p[1] + q[1]) / 2, str(PAIRN[(a, b)]), color=PAIR, size=12.5)

    for pid in P:
        x, y = P[pid]
        n = PAPERS[pid]
        ax.add_patch(FancyBboxPatch((x - W / 2, y - H / 2), W, H, boxstyle='round,pad=0,rounding_size=0.14', fc=NODE,
                                    zorder=4, **border(n)))
        ax.text(x, y + 0.36, f'{pid} · {n} papers', ha='center', va='center', fontsize=15, weight='bold', color=INK,
                zorder=5)
        ax.text(x, y - 0.17, NAME[pid], ha='center', va='center', fontsize=13.5, color=INK, zorder=5, linespacing=1.12)

    # stable orders (bootstrap >= 80% and n >= 5); every arrow carries its share of resamples
    for a, b, pct in (('RP01', 'EP01', '99%'), ('RP09', 'EP10', '100%')):
        p, q = side(a, 'b', -0.45), side(b, 't', -0.45)
        arrow(ax, p, q)
        label(ax, p[0], (p[1] + q[1]) / 2, pct)
    for a, b, pct in (('RP02', 'RP03', '88%'), ('EP02', 'EP03', '88%')):
        p, q = side(a, 'r'), side(b, 'l')
        arrow(ax, p, q)
        label(ax, (p[0] + q[0]) / 2, p[1] + 0.3, pct, size=11.5, bg=ZONE)
    p, q = side('EP03', 'b'), side('EP04', 't')
    arrow(ax, p, q)
    label(ax, p[0] + 0.12, (p[1] + q[1]) / 2, '99%', size=11.5, ha='left')
    # stage boundaries: one arrow each, between the two lanes
    ymid = (-0.42 + 7.0) / 2                                                          # vertical centre of the stage panels
    arrow(ax, (Z[0][1] - 0.02, ymid), (Z[1][0] + 0.02, ymid), lw=3.0)                   # EP01 > RP02, 92%
    label(ax, (Z[0][1] + Z[1][0]) / 2, ymid + 0.32, '92%', size=11.5, bg=SURF)
    arrow(ax, (Z[1][1] - 0.02, ymid), (Z[2][0] + 0.02, ymid), color=MUTED, lw=3.0)      # EP04 > RP05, 69%: not stable
    label(ax, (Z[1][1] + Z[2][0]) / 2, ymid + 0.32, '69%', color=MUTED, size=11.5, bg=SURF)
    arrow(ax, (Z[2][1] - 0.02, ymid), (Z[3][0] + 0.02, ymid), lw=3.0)                   # EP08 > RP09, 97%
    label(ax, (Z[2][1] + Z[3][0]) / 2, ymid + 0.32, '97%', size=11.5, bg=SURF)
    # stage 3: judge before compute, and the iteration loop
    p, q = side('RP08', 'b'), side('EP06', 't', 0.35)
    arrow(ax, p, q, lw=2.2)
    label(ax, (p[0] + q[0]) / 2 + 0.16, (p[1] + q[1]) / 2 - 0.05, 'judge first: 95%\n(paired in 9)', color=ACC,
          size=11.5, ha='left')
    arrow(ax, side('EP08', 'b'), side('EP09', 'b'), lw=2.0, rad=-0.3)
    label(ax, P['RP06'][0], -0.27, 'Requirements not met → revise the plan and recompute', color=ACC, size=12.5)
    label(ax, P['EP11'][0], 0.0, 'only when moving to adoption', color=MUTED, size=11)

    # legend, two rows
    fs = 14.5
    r1, r2 = -0.95, -1.45
    ax.plot([X0, X0 + 0.7], [r1, r1], color=ACC, lw=2.8)
    ax.text(X0 + 0.85, r1, 'Stable order (bootstrap ≥80%, n ≥5); % = share of 300 resamples keeping it', va='center',
            fontsize=fs, color=INK2)
    ax.plot([X0, X0 + 0.7], [r2, r2], color=MUTED, lw=2.8)
    ax.text(X0 + 0.85, r2, 'Less stable order between stages (<80%)', va='center', fontsize=fs, color=INK2)
    lx2 = X0 + 10.6
    ax.plot([lx2, lx2 + 0.7], [r1, r1], color=PAIR, lw=2.0, ls=(0, (2, 2)))
    ax.text(lx2 + 0.85, r1, 'Reason–execute pair; number = papers', va='center', fontsize=fs, color=INK2)
    for i, (n, t) in enumerate([(COMMON, '≥30 papers'), (CONDITIONAL, '15–29 papers'), (0, '<15 papers')]):
        xx = lx2 + i * 2.75
        ax.add_patch(FancyBboxPatch((xx, r2 - 0.16), 0.65, 0.32, boxstyle='round,pad=0,rounding_size=0.06', fc=NODE,
                                    **border(n)))
        ax.text(xx + 0.8, r2, t, va='center', fontsize=fs, color=INK2)

    for ext, kw in (('png', {'dpi': 200}), ('svg', {})):
        fig.savefig(OUT / f'fig0-expert-research-order.{ext}', facecolor=SURF, bbox_inches='tight', pad_inches=0.15, **kw)
    plt.close(fig)


if __name__ == '__main__':
    draw()
    print('saved')
