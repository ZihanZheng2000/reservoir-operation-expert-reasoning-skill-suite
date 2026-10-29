# V02 Reference Route (judges only)

**Paper.** Parameterised Dynamic MPC (PD-MPC) for real-time flood control at the Daecheong reservoir. Published in the Journal of Hydroinformatics, 27(4), 2025.

## (a) Key questions the authors had to settle
- Which "practical objectives" do operators actually use, and how can they be written mathematically? These rest on operator experience, not on regulations.
- How can a multi-objective, nonlinear (complementarity-type) problem be solved in real time without building a Pareto set at every step?
- Should objective weights and parameters (for example the highest tolerated level, SH) stay fixed, or change with the hydrological state?

## (b) Methods and steps
1. **Receding-horizon MPC.** The control inputs are the total and spillway outflow schedules. The state includes storage, predicted inflow, and the schedule from the previous step. Only the first outflow is carried out each hour.
2. **Eight practical objectives:**
   - peak spillway outflow;
   - total spillway outflow;
   - step-wise changes within the horizon;
   - changes between consecutive schedules;
   - water-level exceedance outside a target band [SL, SU] and above SH;
   - continuity of gate state;
   - peak outflow kept below the inflow peak so far;
   - turbines used before the spillway (soft constraint).
3. **Two-level split.** The first five objectives are linearised with slack variables and solved as a linear MPC (Pyomo/GLPK), with time-decaying change weights. A nonlinear "evaluator" holds all objectives, including the complementarity-type ones, and simulates with the nonlinear height-volume curve.
4. **Weight search.** A genetic algorithm (pyGAD) searches 8 integer weights plus SH (EL. 78.5, 79.0, or 79.5 m) at each time step, warm-started from the previous step. MAVE-based multipliers normalise the objectives.
5. **Experiment design:**
   - prediction horizons of 6, 12, 18, and 24 h;
   - start at NHWL, with turbine release 150 m3/s and spillway release 0 m3/s;
   - synthetic forecast error: Gaussian multiplicative noise (a=0.05, b=0.03 per step, floor c=0.1) plus a 3-h moving average;
   - three historical events: 2016, 2018, and 2020.

## (c) Validation
- PD-MPC was compared with two fixed-weight MPC baselines: Fixed-1 favours schedule stability and Fixed-2 favours peak-flow reduction. Both use SH = 79.0 m.
- Runs were done under both uncertain and perfect inflow.
- Sensitivity tests varied the evaluator weight on schedule changes ("Higher"/"Lower"). PD-MPC with fixed SH was compared with PD-MPC with dynamic SH.
- Penalty heatmaps over k=84-99 showed how the best weight shifts over time.

## (d) Main findings
- **All runs.** PD-MPC kept peak outflow below peak inflow in every run and never reached the evaluator's "large-penalty" conditions. Both fixed cases reached them many times.
- **Event 1 under uncertainty.** PD-MPC beat both fixed cases on every metric reported. Peak outflow and number of schedule changes:

| Horizon | PD-MPC | Fixed-1 | Fixed-2 |
|---|---|---|---|
| 6 h | 2,367 m3/s, 9 changes | 3,710 m3/s, 13 changes | 3,617 m3/s, 28 changes |
| 12 h | 2,005 m3/s, 9 changes | 3,267 m3/s, 10 changes | 2,759 m3/s, 37 changes |
| 24 h | 2,128 m3/s, 9 changes | - | -; peak level 77.13 m |

- **Fixed baselines.** Neither baseline reliably won even on the objective it was tuned for.
- **Uncertain vs perfect inflow.** Uncertain inflow raised peaks and the number of changes, for example 38 versus 18 changes for Event 3 at 24 h.
- **Dynamic SH.** Letting SH vary lowered both peak outflow and peak level. Spill started earlier, and storage between SH and FWL was used instead of sharp release jumps.
- **Weights over time.** The best weights changed from step to step. For example, the best weight on the level objective flipped at k=90 for the 18-h horizon.
- **Evaluator weight trade-off.** A higher evaluator weight on schedule changes gave fewer changes but higher peaks.

## (e) Limitations
- No terminal cost or end-of-event state; RL or policy-search is suggested.
- Uncertainty is handled only through receding-horizon feedback, not through stochastic or robust MPC.
- Synthetic forecast noise with arbitrary parameters.
- Only three historical events; there were no 200-year or PMF hydrographs.
- Downstream routing and the upstream reservoir were not modelled; Yongdam outflows were assumed known.
- The GA's computational cost and the fixed weight ratios and multipliers were chosen somewhat arbitrarily.
