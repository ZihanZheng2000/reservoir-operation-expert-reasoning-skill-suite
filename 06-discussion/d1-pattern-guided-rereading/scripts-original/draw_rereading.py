"""Figure: papers (of 10) containing each pattern, one-pass vs after pattern-guided re-reading."""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).parent
res = json.load(open(HERE / 'results.json'))
per = res['per_pattern']
plt.rcParams['font.family'] = ['Arial', 'DejaVu Sans', 'sans-serif']
fig, ax = plt.subplots(figsize=(12, 5.2), dpi=200)
x = range(len(per))
a = [r[1] for r in per]
b = [r[2] for r in per]
ax.bar([i - 0.2 for i in x], a, width=0.4, color='#9bb7d4', label='one-pass extraction')
ax.bar([i + 0.2 for i in x], b, width=0.4, color='#287eb5', label='after pattern-guided re-reading')
for i, (va, vb) in enumerate(zip(a, b)):
    if vb > va:
        ax.text(i + 0.2, vb + 0.15, f'+{vb - va}', ha='center', fontsize=11, color='#c0392b', weight='bold')
ax.set_xticks(list(x))
ax.set_xticklabels([r[0] for r in per], fontsize=11, rotation=45)
ax.set_ylim(0, 11.5)
ax.set_yticks(range(0, 11, 2))
ax.tick_params(axis='y', labelsize=11)
ax.set_ylabel('Papers containing the pattern (of 10)', fontsize=12)
ax.legend(fontsize=11, frameon=False, loc='upper center', ncol=2, bbox_to_anchor=(0.5, 1.12))
ax.spines[['top', 'right']].set_visible(False)
fig.savefig(HERE / 'rereading-per-pattern.png', bbox_inches='tight', facecolor='white')
print('saved')
