"""Draw one combined diagram of reasoning (how to think) and execution (how to do) patterns.
Order, stages and arrow percentages come from combined-order-results.md (combined_order_analysis.py);
pairing counts from rp-ep-pairing.csv; paper counts from ../03-step-coding/pattern-coverage.csv.
Usage: python draw_combined_order.py        (Chinese: combined-order.png/svg)
       python draw_combined_order.py --en   (English: combined-order-en.png/svg)"""
import csv, sys
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

EN = '--en' in sys.argv
plt.rcParams['font.family'] = (['Arial', 'DejaVu Sans', 'sans-serif'] if EN
                               else ['Microsoft YaHei', 'SimHei', 'sans-serif'])
plt.rcParams['axes.unicode_minus'] = False
SURF, INK, INK2, MUTED = '#fcfcfb', '#0b0b0b', '#52514e', '#9a9893'
ACC, NODE, ZONE, PAIR = '#2a78d6', '#ffffff', '#eef3fb', '#c06a2b'
OUT = Path(__file__).parent
COMMON, CONDITIONAL = 30, 15
with (OUT.parent / '03-step-coding' / 'pattern-coverage.csv').open(encoding='utf-8-sig') as f:
    PAPERS = {r['pattern_id']: int(r['papers_any_match']) for r in csv.DictReader(f)}
with (OUT / 'rp-ep-pairing.csv').open(encoding='utf-8-sig') as f:
    PAIRN = {(r['reasoning_pattern'], r['execution_pattern']): int(r['papers']) for r in csv.DictReader(f)}

NAME = {
    'RP01': '诊断现有规则局限', 'RP02': '识别决策相关不确定性', 'RP03': '预报可靠性与时机', 'RP04': '风险与可接受安全',
    'RP05': '物理与运行可行性', 'RP06': '目标权衡与选择原则', 'RP07': '洪水阶段自适应逻辑', 'RP08': '模型表示与方法选择',
    'RP09': '判断证据强度与适用性',
    'EP01': '准备数据与基线规则', 'EP02': '构建并检验预报', 'EP03': '不确定性建模与情景', 'EP04': '模拟水库与下游响应',
    'EP05': '安全边界与可行性', 'EP06': '生成候选方案与参数', 'EP07': '风险、损失与效益', 'EP08': '组织准则并选择方案',
    'EP09': '分阶段滚动动作', 'EP10': '比较与检验调度策略', 'EP11': '协商、试点与修订',
}
NAME_EN = {
    'RP01': 'Diagnose rule limitations', 'RP02': 'Decision-relevant uncertainty', 'RP03': 'Forecast reliability and timing',
    'RP04': 'Risk and acceptable safety', 'RP05': 'Operational feasibility', 'RP06': 'Trade-offs and selection',
    'RP07': 'Adaptive flood-stage logic', 'RP08': 'Model and method choice', 'RP09': 'Evidence and applicability',
    'EP01': 'Data and baseline rules', 'EP02': 'Build and verify forecasts', 'EP03': 'Uncertainty and scenarios',
    'EP04': 'Simulate reservoir response', 'EP05': 'Safety bounds', 'EP06': 'Candidate plans',
    'EP07': 'Risk, losses and benefits', 'EP08': 'Criteria and selection', 'EP09': 'Staged rolling actions',
    'EP10': 'Compare and test policies', 'EP11': 'Consult, pilot and revise',
}
TXT = {   # (Chinese, English)
    'papers': ('篇', 'papers'),
    'title': ('怎么想 ↔ 怎么做：推理与执行 pattern 合在一条时间线上',
              'How to think ↔ how to do: reasoning and execution patterns on one timeline'),
    'source': ('来源：50 篇开发集论文；推理步骤按 card 中"推理 / 执行"配对放到执行时间线上，再做成对先后统计 + 精确 Kemeny 排序（300 次 bootstrap）',
               'Source: 50 development papers. Reasoning steps are placed on the execution timeline through the reasoning/execution '
               'pairs in each paper card; pairwise precedence + exact Kemeny ranking (300 bootstrap resamples).'),
    'think': ('怎\n么\n想', 'How to\nthink'),
    'do': ('怎\n么\n做', 'How to\ndo'),
    's1': ('① 界定问题', '① Define the problem'),
    's1n': ('稳定：总在最前', 'Stable: always first'),
    's2': ('② 认识不确定性与预报', '② Understand uncertainty and forecasts'),
    's2n': ('较稳定', 'Mostly stable'),
    's3': ('③ 设计并计算方案', '③ Design and compute plans'),
    's3n': ('内部没有固定顺序；先判断（上），再计算（下），计算可反复',
            'No fixed order inside; judge first (top), then compute (bottom); computing repeats'),
    's4': ('④ 检验', '④ Test'),
    's4n': ('稳定：总在最后', 'Stable: always last'),
    'jfirst': ('先判断后计算 95%', 'judge before\ncomputing 95%'),
    'loop': ('不满足要求 → 修改方案再算（可反复）', 'Requirements not met → revise the plan and recompute'),
    'adopt': ('仅在走向实际采用时', 'only when moving to adoption'),
    'leg1': ('稳定先后（bootstrap ≥80% 且 n ≥5），% = 300 次重抽样中保持该顺序的比例',
             'Stable order (bootstrap ≥80% and n ≥5); % = share of 300 resamples keeping the order'),
    'leg2': ('推理与执行的主要配对，数字 = 在 card 中被配成一对的论文篇数',
             'Main reasoning–execution pair; number = papers in which the two are paired in the card'),
    'common': ('常见：≥{} 篇出现', 'Common: ≥{} papers'),
    'cond': ('条件性：{}–{} 篇', 'Conditional: {}–{} papers'),
    'spec': ('专门：<{} 篇', 'Specialized: <{} papers'),
}
T = {k: v[1 if EN else 0] for k, v in TXT.items()}
if EN:
    NAME = NAME_EN
TOP, BOT = 7.2, 3.0          # lane centres: how to think / how to do
W, H = 2.15, 0.95

# x, y for every pattern; order follows the exact Kemeny ranking in combined-order-results.md
P = {
    'RP01': (2.4, TOP), 'EP01': (4.2, BOT),
    'RP02': (6.9, TOP), 'RP03': (9.5, TOP), 'EP02': (8.2, BOT), 'EP03': (10.8, BOT), 'EP04': (13.4, BOT),
    'RP04': (16.0, TOP + 0.6), 'RP06': (18.6, TOP + 0.6), 'RP05': (21.2, TOP + 0.6),
    'RP07': (17.3, TOP - 0.65), 'RP08': (19.9, TOP - 0.65),
    'EP07': (16.0, BOT + 0.6), 'EP06': (18.6, BOT + 0.6), 'EP05': (21.2, BOT + 0.6),
    'EP09': (17.3, BOT - 0.65), 'EP08': (19.9, BOT - 0.65),
    'RP09': (24.9, TOP), 'EP10': (24.9, BOT), 'EP11': (24.9, BOT - 1.55),
}
PAIRS = [('RP01', 'EP01'), ('RP02', 'EP03'), ('RP03', 'EP02'), ('RP04', 'EP07'), ('RP05', 'EP05'),
         ('RP06', 'EP06'), ('RP07', 'EP09'), ('RP08', 'EP06'), ('RP09', 'EP10')]
# stable adjacent orders (bootstrap >= 80% and n >= 5), with the share keeping the order
STABLE = [('RP01', 'EP01', '99%'), ('EP01', 'RP02', '92%'), ('RP02', 'RP03', '88%'), ('EP02', 'EP03', '88%'),
          ('EP03', 'EP04', '99%'), ('RP09', 'EP10', '100%')]


def border(n):
    if n >= COMMON:
        return dict(ec=INK, lw=1.8, ls='-')
    if n >= CONDITIONAL:
        return dict(ec=INK2, lw=1.3, ls=(0, (5, 3)))
    return dict(ec=MUTED, lw=1.3, ls=(0, (1, 2.5)))


def node(ax, pid):
    x, y = P[pid]
    n = PAPERS[pid]
    ax.add_patch(FancyBboxPatch((x - W / 2, y - H / 2), W, H, boxstyle='round,pad=0.02,rounding_size=0.12',
                                fc=NODE, zorder=3, **border(n)))
    ax.text(x, y + 0.2, f"{pid} · {n} {T['papers']}", ha='center', va='center', fontsize=9.5, weight='bold', color=INK, zorder=4)
    ax.text(x, y - 0.17, NAME[pid], ha='center', va='center', fontsize=8.5, color=INK, zorder=4)


def side(pid, s):
    x, y = P[pid]
    return {'r': (x + W / 2, y), 'l': (x - W / 2, y), 't': (x, y + H / 2), 'b': (x, y - H / 2)}[s]


def arrow(ax, p, q, label='', color=ACC, lw=2.0, ls='-', style='-|>', lpos=(0, 0.12), rad=0.0):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=13, lw=lw, color=color, ls=ls,
                                 shrinkA=2, shrinkB=2, zorder=2, connectionstyle=f'arc3,rad={rad}'))
    if label:
        ax.text((p[0] + q[0]) / 2 + lpos[0], (p[1] + q[1]) / 2 + lpos[1], label, ha='center', va='bottom',
                fontsize=7.5, color=INK2, zorder=5, bbox=dict(fc=SURF, ec='none', pad=0.4))


def zone(ax, x0, x1, title, note):
    ax.add_patch(FancyBboxPatch((x0, 0.3), x1 - x0, 8.65, boxstyle='round,pad=0.02,rounding_size=0.25',
                                fc=ZONE, ec=ACC, lw=1.0, ls=(0, (4, 3)), zorder=1))
    ax.text((x0 + x1) / 2, 9.55, title, ha='center', va='center', fontsize=11, weight='bold', color=INK, zorder=2)
    ax.text((x0 + x1) / 2, 9.13, note, ha='center', va='center', fontsize=8, color=INK2, zorder=2)


fig, ax = plt.subplots(figsize=(27.5, 11.2), dpi=200)
fig.patch.set_facecolor(SURF)
ax.set_facecolor(SURF)
ax.set_xlim(0, 27.5)
ax.set_ylim(-1.6, 11.2)
ax.axis('off')

ax.text(0.3, 10.75, T['title'], fontsize=15, weight='bold', color=INK)
ax.text(0.3, 10.3, T['source'],
        fontsize=9, color=INK2)
ax.text(0.45, TOP, T['think'], ha='center', va='center', fontsize=10 if EN else 12, weight='bold', color=INK)
ax.text(0.45, BOT, T['do'], ha='center', va='center', fontsize=10 if EN else 12, weight='bold', color=INK)

zone(ax, 1.0, 5.55, T['s1'], T['s1n'])
zone(ax, 5.8, 14.75, T['s2'], T['s2n'])
zone(ax, 15.0, 22.55, T['s3'], T['s3n'])
zone(ax, 23.7, 26.1, T['s4'], T['s4n'])

for a, b in PAIRS:
    pa, pb = side(a, 'b'), side(b, 't')
    ax.plot([pa[0], pb[0]], [pa[1], pb[1]], color=PAIR, lw=1.2, ls=(0, (2, 2)), zorder=1.5)
    f = 0.38 if a == 'RP07' else 0.72   # keep labels clear of the boxes
    lx, ly = pa[0] + (pb[0] - pa[0]) * f, pa[1] + (pb[1] - pa[1]) * f
    ax.text(lx + 0.08, ly, f'{PAIRN[(a, b)]}', ha='left', va='center', fontsize=7.5,
            color=PAIR, zorder=5, bbox=dict(fc=ZONE, ec='none', pad=0.3))
for pid in P:
    node(ax, pid)

for a, b, pct in STABLE:
    pa, pb = P[a], P[b]
    if pa[1] == pb[1]:
        arrow(ax, side(a, 'r'), side(b, 'l'), pct)
    else:
        arrow(ax, side(a, 'b' if pa[1] > pb[1] else 't'), side(b, 'l'), pct, lpos=(0.25, 0.0))
# stage transitions
arrow(ax, (14.55, BOT), (14.95, BOT), lw=2.4)
arrow(ax, (14.55, TOP), (14.95, TOP), lw=2.4)
arrow(ax, (22.35, TOP), (23.75, TOP), '97%', lw=2.4)
arrow(ax, (22.35, BOT), (23.75, BOT), lw=2.4)
# within stage 3: judgments before computation (RP08 > EP06, 95%), and the iteration loop
arrow(ax, side('RP08', 'b'), side('EP06', 't'), '', color=ACC, lw=1.6)
ax.text(19.55, 5.05, T['jfirst'], ha='left', va='center', fontsize=7.5, color=ACC, zorder=5,
        bbox=dict(fc=ZONE, ec='none', pad=0.3))
arrow(ax, (21.2, BOT + 0.6 - H / 2), (16.0, BOT + 0.6 - H / 2), color=ACC, lw=1.4, rad=-0.62)
ax.text(18.6, 0.62, T['loop'], ha='center', va='center', fontsize=8.5, color=ACC, zorder=5,
        bbox=dict(fc=ZONE, ec='none', pad=0.3))
ax.text(24.9, 0.55, T['adopt'], ha='center', va='center', fontsize=7.5, color=MUTED)

# legend
lx, ly = 1.0, -0.35
ax.plot([lx, lx + 0.7], [ly, ly], color=ACC, lw=2)
ax.text(lx + 0.85, ly, T['leg1'], va='center', fontsize=8, color=INK2)
ax.plot([lx, lx + 0.7], [ly - 0.45, ly - 0.45], color=PAIR, lw=1.2, ls=(0, (2, 2)))
ax.text(lx + 0.85, ly - 0.45, T['leg2'], va='center', fontsize=8, color=INK2)
bx = 12.5
for i, (n, txt) in enumerate([(COMMON, T['common'].format(COMMON)), (CONDITIONAL, T['cond'].format(CONDITIONAL, COMMON - 1)),
                              (0, T['spec'].format(CONDITIONAL))]):
    xx = bx + 3.6 * i
    ax.add_patch(FancyBboxPatch((xx, ly - 0.11), 0.6, 0.22, boxstyle='round,pad=0.01,rounding_size=0.05', fc=NODE, **border(n)))
    ax.text(xx + 0.75, ly, txt, va='center', fontsize=8, color=INK2)

for ext in ('png', 'svg'):
    fig.savefig(OUT / f"combined-order{'-en' if EN else ''}.{ext}", bbox_inches='tight', facecolor=SURF)
print('saved')
