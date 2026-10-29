"""Result figures for the reservoir flood-operation skill study (English labels, light theme).

Reads the blinding keys and judgments in ../05-round-01, ../07-round-02, ../09-round-03 and ../10-final-test,
and the reference-coverage codes transcribed from ../10-final-test/rc-analysis-zh.md (section 1).
Writes PNG (220 dpi) and SVG to out/.
Usage: python make_figures.py
"""
import json, re
from pathlib import Path
from statistics import mean

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm
from matplotlib.patches import Patch, Rectangle

HERE = Path(__file__).resolve().parent
W = HERE.parent
OUT = HERE / 'out'
OUT.mkdir(exist_ok=True)

# ---- style -------------------------------------------------------------------------------------------------
SURF, INK, INK2, MUTED, GRID = '#ffffff', '#0b0b0b', '#52514e', '#8a8984', '#e7e6e2'
BLUE, BLUE_L, BLUE_D, GRAY = '#2a78d6', '#9ec5f4', '#184f95', '#9a9993'
RED, RED_L = '#d64545', '#f2b8b5'
ORANGE, AQUA = '#eb6834', '#1baf7a'
plt.rcParams.update({
    'font.family': 'Arial', 'font.size': 10, 'text.color': INK, 'axes.labelcolor': INK2,
    'axes.edgecolor': GRID, 'xtick.color': INK2, 'ytick.color': INK2, 'axes.titlesize': 12,
    'axes.titleweight': 'bold', 'axes.titlelocation': 'left', 'figure.facecolor': SURF, 'axes.facecolor': SURF,
    'savefig.facecolor': SURF, 'svg.fonttype': 'none', 'axes.spines.top': False, 'axes.spines.right': False,
})


def save(fig, name):
    for ext, kw in (('png', {'dpi': 220}), ('svg', {})):
        fig.savefig(OUT / f'{name}.{ext}', bbox_inches='tight', pad_inches=0.25, **kw)
    plt.close(fig)


def title(fig, text, sub):
    fig.text(0.0, 1.0, text, ha='left', va='bottom', fontsize=14, fontweight='bold', color=INK, transform=fig.transFigure)
    fig.text(0.0, 0.985, sub, ha='left', va='top', fontsize=10, color=INK2, transform=fig.transFigure)


# ---- data --------------------------------------------------------------------------------------------------
def load(folder, crit, nested_model=None):
    """Return {case: {'A': [judge dicts], 'C': [...], 'win': [arm or 'tie' per judge], 'strength': [...]}}."""
    key = json.loads((folder / 'blinding-key.json').read_text(encoding='utf-8'))
    if nested_model:
        key = key[nested_model]
    jdir = folder / 'judgments' / nested_model if nested_model else folder / 'judgments'
    res = {}
    for case, k in key.items():
        a1, a2 = k['answer1']['arm'], k['answer2']['arm']
        r = {'A': [], 'C': [], 'win': [], 'strength': []}
        for j, order in (('j1', [a1, a2]), ('j2', [a2, a1])):
            t = (jdir / f'{case}-{j}.md').read_text(encoding='utf-8')
            for n in (1, 2):
                s = re.search(rf'SCORES Answer {n}:\s*' + r'\s+'.join(rf'{c}=(\d+)' for c in crit), t)
                r[order[n - 1]].append(dict(zip(crit, map(int, s.groups()))))
            who, st = re.findall(r'WINNER:\s*\**\s*(Answer 1|Answer 2|tie)[^,\n]*,?\s*(clear|slight)?', t, re.I)[-1]
            r['win'].append('tie' if who.lower() == 'tie' else order[int(who[-1]) - 1])
            r['strength'].append((st or 'slight').lower())
        res[case] = r
    return res


C5 = ['KQ', 'TC', 'ME', 'PR', 'CA']
C6 = C5 + ['RC']
R1 = {m: load(W / '05-round-01', C5, m) for m in ('opus', 'sonnet', 'haiku')}
R2 = load(W / '07-round-02', C5, 'opus')
R3 = load(W / '09-round-03', C5, 'opus')
FT = load(W / '10-final-test', C6)


def avg(r, arm, crit=None):
    return mean(mean(d.values()) if crit is None else d[crit] for d in r[arm])


def result(r):
    w = set(r['win'])
    return next(iter(w)) if len(w) == 1 else 'split'


# ---- Figure 1: final test by case --------------------------------------------------------------------------
def fig_final_by_case():
    cases = list(FT)
    fig, ax = plt.subplots(figsize=(11.2, 5.8))
    ys = []
    y = 0
    for i, c in enumerate(cases):
        if i and c[:3] != cases[i - 1][:3]:
            y += 0.6
        ys.append(y)
        y += 1
    chip = {('C', 'clear'): ('C · clear', BLUE_D, SURF), ('C', 'slight'): ('C · slight', '#cde2fb', INK),
            ('tie', 'slight'): ('tie', '#e7e6e2', INK), ('tie', 'clear'): ('tie', '#e7e6e2', INK),
            ('A', 'slight'): ('A · slight', RED_L, INK), ('A', 'clear'): ('A · clear', RED, SURF)}
    tr = ax.get_yaxis_transform()          # x in axes fraction, y in data
    cols = (1.10, 1.25, 1.42)
    for x, h in zip(cols, ('Judge 1', 'Judge 2', 'Result')):
        ax.text(x, -0.95, h, transform=tr, ha='center', va='center', fontsize=9.5, color=INK2, fontweight='bold')
    for c, y in zip(cases, ys):
        a, cc = avg(FT[c], 'A'), avg(FT[c], 'C')
        ax.plot([a, cc], [y, y], color=GRID, lw=3, solid_capstyle='round', zorder=1)
        ax.scatter([a], [y], s=70, color=GRAY, zorder=3, edgecolor=SURF, linewidth=1.5)
        ax.scatter([cc], [y], s=70, color=BLUE, zorder=3, edgecolor=SURF, linewidth=1.5)
        for x, w, st in zip(cols, FT[c]['win'], FT[c]['strength']):
            t, bg, fg = chip[(w, st)]
            ax.text(x, y, t, transform=tr, ha='center', va='center', fontsize=9, color=fg,
                    bbox=dict(boxstyle='round,pad=0.35,rounding_size=0.6', fc=bg, ec='none'))
        res = result(FT[c])
        lab = {'C': 'skill wins', 'A': 'no-skill wins', 'split': 'judges split', 'tie': 'tie'}[res]
        ax.text(cols[2], y, lab, transform=tr, ha='center', va='center', fontsize=9.5,
                color=INK if res == 'C' else MUTED, fontweight='bold' if res == 'C' else 'normal')
    ax.set_yticks(ys, [f"{c[:3]}  {'simple' if c.endswith('S') else 'detailed'}" for c in cases])
    ax.invert_yaxis()
    ax.set_xlim(6.9, 8.75)
    ax.set_xticks([7.0, 7.5, 8.0, 8.5])
    ax.set_xlabel('Mean judge score (6 criteria, 2 judges, 1–10)')
    ax.grid(axis='x', color=GRID, lw=0.8)
    ax.set_axisbelow(True)
    ax.spines['left'].set_visible(False)
    ax.tick_params(axis='y', length=0)
    ax.legend(handles=[plt.Line2D([], [], marker='o', ls='', color=GRAY, ms=8, label='No skill (A)'),
                       plt.Line2D([], [], marker='o', ls='', color=BLUE, ms=8, label='With skill (C)')],
              loc='lower left', bbox_to_anchor=(0, 1.0), ncol=2, frameon=False, fontsize=9.5)
    title(fig, 'Held-out papers: the skill wins 8 of 10 cases and loses none',
          'Five papers not used to build the skill, each posed as a simple and a detailed brief. Claude Opus 5.5 answers; '
          'two blind judges per case (judge 2 saw the answers in reverse order).')
    fig.subplots_adjust(top=0.86, right=0.72)
    save(fig, 'fig1-final-test-by-case')


# ---- Figure 2: final test by criterion ---------------------------------------------------------------------
def fig_final_by_criterion():
    names = {'KQ': 'Key questions', 'TC': 'Technical correctness', 'ME': 'Method', 'PR': 'Practicality',
             'CA': 'Calibration', 'RC': 'Coverage of the\npaper’s own route'}
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.6), sharey=True)
    for ax, (ver, lab) in zip(axes, (('S', 'Simple brief'), ('D', 'Detailed brief'))):
        rs = [r for c, r in FT.items() if c.endswith(ver)]
        for i, k in enumerate(C6):
            a = mean(d[k] for r in rs for d in r['A'])
            c = mean(d[k] for r in rs for d in r['C'])
            col = BLUE if c - a >= 0.3 else (RED if c - a <= -0.3 else MUTED)
            ax.plot([a, c], [i, i], color=GRID, lw=3, solid_capstyle='round', zorder=1)
            ax.scatter([a], [i], s=70, color=GRAY, zorder=3, edgecolor=SURF, linewidth=1.5)
            ax.scatter([c], [i], s=70, color=BLUE, zorder=3, edgecolor=SURF, linewidth=1.5)
            ax.text(9.45, i, f'{c - a:+.1f}', va='center', ha='right', fontsize=10, color=col, fontweight='bold')
        ax.set_title(lab, fontsize=11, pad=8)
        ax.set_xlim(5.6, 9.5)
        ax.set_xticks([6, 7, 8, 9])
        ax.grid(axis='x', color=GRID, lw=0.8)
        ax.set_axisbelow(True)
        ax.spines['left'].set_visible(False)
        ax.tick_params(axis='y', length=0)
        ax.axhspan(4.5, 5.5, color='#f6f5f2', zorder=0)
        ax.set_xlabel('Mean score (1–10)')
    axes[0].set_yticks(range(6), [names[k] for k in C6])
    axes[0].invert_yaxis()
    axes[1].text(9.45, -0.75, 'C − A', ha='right', fontsize=9, color=MUTED)
    axes[0].legend(handles=[plt.Line2D([], [], marker='o', ls='', color=GRAY, ms=8, label='No skill (A)'),
                            plt.Line2D([], [], marker='o', ls='', color=BLUE, ms=8, label='With skill (C)')],
                   loc='lower left', bbox_to_anchor=(0, 1.08), ncol=2, frameon=False, fontsize=9.5)
    title(fig, 'The skill improves practicality most; coverage of the paper’s route does not improve',
          'Held-out test, mean over 5 papers × 2 judges. Shaded row: reference coverage (RC).')
    fig.subplots_adjust(top=0.78, wspace=0.08)
    save(fig, 'fig2-final-test-by-criterion')


# ---- Figure 3: development rounds heatmap ------------------------------------------------------------------
def fig_dev_heatmap():
    qs = [f'U{i}' for i in range(1, 8)]
    qname = {'U1': 'U1  Study design', 'U2': 'U2  Calculation', 'U3': 'U3  Review of a claim',
             'U4': 'U4  Judging an ML result', 'U5': 'U5  Cascade real-time decision',
             'U6': 'U6  Scheme choice', 'U7': 'U7  Method choice'}
    cols = ['Round 1\nskill v1', 'Round 2\nskill v2', 'Round 3\nskill v3']
    vals, labs = [], []
    for q in qs:
        row, lr = [], []
        for rnd in (R1['opus'], R2):
            r = rnd[q]
            row.append(avg(r, 'C') - avg(r, 'A'))
            lr.append(result(r))
        if q == 'U5':
            rr = [R3[f'U5-r{i}'] for i in (1, 2, 3)]
            row.append(mean(avg(r, 'C') - avg(r, 'A') for r in rr))
            lr.append('C wins 3/3')
        else:
            row.append(None)
            lr.append(None)
        vals.append(row)
        labs.append(lr)
    cmap = LinearSegmentedColormap.from_list('div', [RED, '#f6d6d4', '#f0efec', '#cde2fb', '#5598e7', BLUE_D])
    norm = TwoSlopeNorm(vmin=-1.0, vcenter=0, vmax=2.0)
    fig, ax = plt.subplots(figsize=(7.6, 5.0))
    for i, row in enumerate(vals):
        for j, v in enumerate(row):
            if v is None:
                ax.add_patch(Rectangle((j, i), 1, 1, facecolor='#f7f6f3', edgecolor=SURF, lw=2, hatch='////'))
                ax.text(j + 0.5, i + 0.5, 'not rerun', ha='center', va='center', fontsize=8, color=MUTED)
                continue
            ax.add_patch(Rectangle((j, i), 1, 1, facecolor=cmap(norm(v)), edgecolor=SURF, lw=2))
            dark = norm(v) > 0.78 or norm(v) < 0.12
            res = labs[i][j]
            tag = {'C': 'C wins', 'A': 'A wins', 'split': 'split', 'tie': 'tie'}.get(res, res)
            ax.text(j + 0.5, i + 0.42, f'{v:+.1f}', ha='center', va='center', fontsize=11, fontweight='bold',
                    color=SURF if dark else INK)
            ax.text(j + 0.5, i + 0.72, tag, ha='center', va='center', fontsize=8, color=SURF if dark else INK2)
    plt.rcParams['hatch.color'] = GRID
    ax.set_xlim(0, 3)
    ax.set_ylim(len(qs), 0)
    ax.set_xticks([0.5, 1.5, 2.5], cols)
    ax.set_yticks([i + 0.5 for i in range(len(qs))], [qname[q] for q in qs])
    ax.tick_params(length=0)
    ax.xaxis.tick_top()
    for s in ax.spines.values():
        s.set_visible(False)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    cb = fig.colorbar(sm, ax=ax, fraction=0.04, pad=0.03, ticks=[-1, 0, 1, 2])
    cb.outline.set_visible(False)
    cb.ax.tick_params(length=0, labelsize=8.5)
    cb.set_label('Score difference, skill − no skill', fontsize=9, color=INK2)
    title(fig, 'Judge and human feedback closed the gaps question by question',
          'Development questions, Claude Opus 5.5. Round 3 reran only U5 (three independent skill answers).')
    fig.subplots_adjust(top=0.80, left=0.30)
    save(fig, 'fig3-dev-rounds-heatmap')


# ---- Figure 4: judgment outcomes across tests --------------------------------------------------------------
def fig_outcomes():
    tests = [('Round 1 · v1', R1['opus']), ('Round 2 · v2', R2), ('Round 3 · v3 (U5 ×3)', R3), ('Held-out test · v3', FT)]
    cats = [('Skill, clear', BLUE_D), ('Skill, slight', '#6da7ec'), ('Tie', '#d9d8d3'), ('No skill, slight', RED_L),
            ('No skill, clear', RED)]
    fig, ax = plt.subplots(figsize=(9.0, 3.4))
    for i, (name, rs) in enumerate(tests):
        cnt = dict.fromkeys([c for c, _ in cats], 0)
        for r in rs.values():
            for w, s in zip(r['win'], r['strength']):
                k = 'Tie' if w == 'tie' else ('Skill' if w == 'C' else 'No skill') + f', {s}'
                cnt[k] += 1
        n = sum(cnt.values())
        left = 0
        for c, col in cats:
            v = cnt[c] / n
            if v:
                ax.barh(i, v, left=left, color=col, height=0.62, edgecolor=SURF, linewidth=2)
                if v >= 0.03:
                    ax.text(left + v / 2, i, str(cnt[c]), ha='center', va='center', fontsize=9.5,
                            color=SURF if col in (BLUE_D, RED) else INK, fontweight='bold')
            left += v
        ax.text(1.01, i, f'{cnt["Skill, clear"] + cnt["Skill, slight"]}/{n} prefer skill', va='center', fontsize=9,
                color=INK2)
    ax.set_yticks(range(len(tests)), [t for t, _ in tests])
    ax.invert_yaxis()
    ax.set_xlim(0, 1)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1], ['0%', '25%', '50%', '75%', '100%'])
    ax.tick_params(axis='y', length=0)
    ax.spines['left'].set_visible(False)
    ax.legend(handles=[Patch(color=col, label=c) for c, col in cats], loc='lower left', bbox_to_anchor=(0, 1.0),
              ncol=5, frameon=False, fontsize=9, handlelength=1.2, columnspacing=1.2)
    title(fig, 'The skill was preferred in 79–100% of judgments in every test',
          'Share of individual judgments, Claude Opus 5.5 answers; numbers in bars are counts. Clear wins peaked in round 2 '
          'on the development questions.')
    fig.subplots_adjust(top=0.72)
    save(fig, 'fig4-judgment-outcomes')


# ---- Figure 5: answer models in round 1 (absolute scores) ---------------------------------------------------
def fig_models():
    models = [('opus', 'Opus 5.5'), ('sonnet', 'Sonnet 5.5'), ('haiku', 'Haiku 4.5')]
    names = {'KQ': 'Key questions', 'TC': 'Technical correctness', 'ME': 'Method', 'PR': 'Practicality',
             'CA': 'Calibration', 'ALL': 'Mean of five'}
    rows = ['ALL'] + C5
    fig, axes = plt.subplots(1, 3, figsize=(11.5, 4.6), sharey=True)
    for ax, (m, lab) in zip(axes, models):
        rs = list(R1[m].values())
        for i, k in enumerate(rows):
            if k == 'ALL':
                a_, c_ = mean(avg(r, 'A') for r in rs), mean(avg(r, 'C') for r in rs)
            else:
                a_ = mean(x[k] for r in rs for x in r['A'])
                c_ = mean(x[k] for r in rs for x in r['C'])
            big = k == 'ALL'
            ax.plot([a_, c_], [i, i], color=GRID, lw=4 if big else 3, solid_capstyle='round', zorder=1)
            same = abs(c_ - a_) < 0.05
            ax.scatter([a_], [i], s=(150 if same else 95) if big else (120 if same else 60), color=GRAY, zorder=3,
                       edgecolor=SURF, linewidth=1.5)
            ax.scatter([c_], [i], s=(50 if same else 95) if big else (38 if same else 60),
                       color=BLUE if c_ >= a_ else RED, zorder=4, edgecolor=SURF, linewidth=1.0 if same else 1.5)
            ax.text(max(a_, c_) + 0.25, i, f'{a_:.1f} → {c_:.1f}', va='center', fontsize=9.5 if big else 8.8,
                    color=INK if big else INK2, fontweight='bold' if big else 'normal')
        rc = sum(r['win'].count('C') for r in rs)
        ax.set_title(f'{lab}', fontsize=12, pad=24)
        ax.text(0, 1.015, f'{rc}/14 judgments prefer the skill', transform=ax.transAxes, fontsize=9, color=INK2,
                va='bottom')
        ax.axhspan(-0.5, 0.5, color='#f6f5f2', zorder=0)
        ax.set_xlim(3.5, 10)
        ax.set_xticks([4, 6, 8, 10])
        ax.grid(axis='x', color=GRID, lw=0.8)
        ax.set_axisbelow(True)
        ax.spines['left'].set_visible(False)
        ax.tick_params(axis='y', length=0)
        ax.set_xlabel('Mean score (1–10)')
    axes[0].set_yticks(range(len(rows)), [names[k] for k in rows])
    axes[0].invert_yaxis()
    axes[0].legend(handles=[plt.Line2D([], [], marker='o', ls='', color=GRAY, ms=8, label='No skill (A)'),
                            plt.Line2D([], [], marker='o', ls='', color=BLUE, ms=8, label='With skill (C)'),
                            plt.Line2D([], [], marker='o', ls='', color=RED, ms=8, label='With skill, lower than A')],
                   loc='lower left', bbox_to_anchor=(0, 1.2), ncol=3, frameon=False, fontsize=9.5)
    title(fig, 'Model capability sets the level; the skill adds a smaller step on top',
          'Development round 1 (skill v1), 7 questions × 2 judges per model. The gap between models is larger than '
          'the gain from the skill.')
    fig.subplots_adjust(top=0.70, wspace=0.12)
    save(fig, 'fig5-answer-models-round1')


# ---- Figure 6: reference-coverage matrix -------------------------------------------------------------------
# Codes per reference element for (simple-A, simple-C, detailed-A, detailed-C), from rc-analysis-zh.md section 1:
# Y covered, E justified equivalent, P partial, N not covered, X judges disagree, U not judged.
RC = {
    'V01  Three Gorges: forecast-based flood-season level': [
        ('Forecast error by lead time, Monte Carlo', 'YYEE'), ('Pre-release cap per lead time', 'PPYY'),
        ('Three-module rule (pre-release / rule / refill)', 'PPYY'), ('Error domain of graded release rules', 'NNNN'),
        ('Daily choice of trusted lead time', 'NNEE'), ('Upstream and downstream risk', 'YYYY'),
        ('Option set incl. relaxed accuracy', 'PPPP'), ('Sensitivity to risk threshold', 'PPEE'),
        ('Rolling 2019 simulation', 'YYYY')],
    'V02  Daecheong: operator-acceptable hourly releases': [
        ('Objectives from operator experience', 'YYYY'), ('Receding-horizon control', 'YYYY'),
        ('Eight practical objectives', 'PPYY'), ('Soft target level band', 'PNNN'),
        ('Linear MPC + nonlinear evaluator', 'NNXX'), ('Weights that change with flood state', 'NNNN'),
        ('Normalising objective scales', 'NNNN'), ('Fixed-weight baselines', 'PNNP'),
        ('Experiment design (horizons, noise, events)', 'YYYP'), ('Weight sensitivity', 'NXPP')],
    'V03  Lishimen: releases under forecast uncertainty': [
        ('Rainfall-driven inflow forecast', 'EYYY'), ('Multi-model ensemble (stacking)', 'NNNN'),
        ('Forecast scenarios', 'EEEE'), ('Whole-event storage-use index', 'NNPE'),
        ('Scenario risk objectives', 'YYYY'), ('Scenario aggregation (regret)', 'PNYN'),
        ('Multi-objective Pareto search', 'NNYN'), ('Choosing a compromise plan', 'EPEE'),
        ('Deterministic vs robust comparison', 'YPYP'), ('Ablation of the new index', 'NNNN'),
        ('Event-wise cross-validation', 'EEEE')],
    'V04  Yiluo: two reservoirs under forecast error': [
        ('Flow-dependent residual model', 'EPYY'), ('Normalising transform and checks', 'PPPX'),
        ('Residual autocorrelation', 'EEEE'), ('Ladder of error assumptions', 'NNYY'),
        ('Prediction-interval coverage', 'YYNY'), ('Monte Carlo inflow scenarios', 'YYYY'),
        ('Three-objective optimisation + routing', 'YPYY'), ('Encoding against saw-tooth releases', 'NNNN'),
        ('Plan choice under fuzzy preferences', 'NNEE'), ('End-level repair', 'NNYU'),
        ('Robust vs deterministic comparison', 'YYYP'), ('Limits: storage metric, compute cost', 'NNNN')],
    'V05  Stânca–Costești: design floods and outlet rules': [
        ('Rating-curve reliability check', 'YYYY'), ('Long-reach unsteady routing model', 'NNYY'),
        ('Design flood by volume and shape', 'YYYY'), ('Spread across distributions', 'PPPP'),
        ('Climate-change uplift', 'YXYY'), ('Critical hydrograph shape', 'PNNP'),
        ('Open/close levels per outlet', 'PPPP'), ('Rule sets by flood class + decision points', 'NXYE'),
        ('10-day rainfall lookup', 'NNYY'), ('2008 water-balance check', 'YYYY'),
        ('Comparison with original design rule', 'NNNN'), ('Comparison with current rule', 'YYNY'),
        ('Limit: forecast shorter than needed', 'PPNN')],
}
LEVEL = {'Y': ('Covered', BLUE_D), 'E': ('Justified equivalent', '#5598e7'), 'P': ('Partly', '#b7d3f6'),
         'N': ('Not covered', '#ecebe7'), 'X': ('Judges disagree', None), 'U': ('Not judged', None)}


def fig_rc_matrix():
    fig = plt.figure(figsize=(14.5, 10.2))
    gs = fig.add_gridspec(2, 3, hspace=0.28, wspace=1.15)
    slots = [gs[0, 0], gs[0, 1], gs[0, 2], gs[1, 0], gs[1, 1]]
    for slot, (paper, items) in zip(slots, RC.items()):
        ax = fig.add_subplot(slot)
        for i, (_, code) in enumerate(items):
            for j, ch in enumerate(code):
                lab, col = LEVEL[ch]
                if col:
                    ax.add_patch(Rectangle((j, i), 1, 1, facecolor=col, edgecolor=SURF, lw=2))
                else:
                    ax.add_patch(Rectangle((j, i), 1, 1, facecolor=SURF, edgecolor=SURF, lw=2))
                    ax.add_patch(Rectangle((j + 0.08, i + 0.08), 0.84, 0.84, facecolor=SURF, edgecolor=MUTED, lw=0.8,
                                           hatch='////' if ch == 'X' else None))
        n = len(items)
        cov = lambda j: sum(c[1][j] in 'YE' for c in items)
        for j in range(4):
            ax.text(j + 0.5, n + 0.55, f'{cov(j)}/{n}', ha='center', va='top', fontsize=8.5, color=INK2)
        ax.set_xlim(0, 4)
        ax.set_ylim(n + 1.1, 0)
        ax.set_xticks([0.5, 1.5, 2.5, 3.5], ['A', 'C', 'A', 'C'])
        ax.xaxis.tick_top()
        ax.text(1, -1.25, 'simple', ha='center', fontsize=8.5, color=MUTED)
        ax.text(3, -1.25, 'detailed', ha='center', fontsize=8.5, color=MUTED)
        ax.axvline(2, color=INK2, lw=1)
        ax.set_yticks([i + 0.5 for i in range(n)], [t for t, _ in items], fontsize=8.6)
        ax.tick_params(length=0)
        for s in ax.spines.values():
            s.set_visible(False)
        ax.set_title(paper, fontsize=10.5, pad=40, loc='right')
    lax = fig.add_subplot(gs[1, 2])
    lax.axis('off')
    hand = [Patch(facecolor=LEVEL[k][1], edgecolor='none', label=LEVEL[k][0]) for k in 'YEPN']
    hand += [Patch(facecolor=SURF, edgecolor=MUTED, hatch='////', label='Judges disagree'),
             Patch(facecolor=SURF, edgecolor=MUTED, label='Not judged')]
    lax.legend(handles=hand, loc='upper left', frameon=False, fontsize=10, title='Coverage of each reference step',
               title_fontproperties={'weight': 'bold', 'size': 10}, alignment='left', handlelength=1.4,
               handleheight=1.2)
    lax.text(0.0, 0.42, 'A = no skill, C = with skill.\nNumbers under each column: steps covered\nor replaced by a '
             'justified equivalent.\n\nSteps that no answer reached are mostly\nthe paper’s own inventions; the '
             'detailed\nbrief raises coverage more than the skill.', transform=lax.transAxes, va='top', fontsize=9.5,
             color=INK2, linespacing=1.5)
    title(fig, 'Which steps of each paper’s own route did the answers reach?',
          'Held-out test. Coverage as stated in the two judges’ notes; a cell is “covered” only if the judges say so.')
    fig.subplots_adjust(top=0.86)
    save(fig, 'fig6-reference-coverage-matrix')


if __name__ == '__main__':
    fig_final_by_case()
    fig_final_by_criterion()
    fig_dev_heatmap()
    fig_outcomes()
    fig_models()
    fig_rc_matrix()
    print('written:', sorted(p.name for p in OUT.iterdir()))
