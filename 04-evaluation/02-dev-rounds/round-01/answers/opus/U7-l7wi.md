# Real-time release decision tool: representation, method, verification

## 1. Provisional recommendation in brief

I would build the tool as a **rolling-horizon, scenario-tree stochastic model predictive controller (MPC)**. It would have:

- a **convex internal model**: an exact-in-mass reservoir balance, a conservative piecewise-linear discharge-capacity constraint, and a reduced linear routing model identified from the calibrated channel model;
- a **joint ensemble of reservoir inflow and ungauged-tributary inflow**, reduced each cycle to a small scenario tree. All branches share the release for the next 6 h, and the branches split later as the forecasts diverge;
- **priority-ordered objectives** in place of opaque weights: (1) dam-safety limits are hard on every branch; (2) minimise exceedance of the safe flow at the downstream control station, with a tail (CVaR-type) term; (3) return to the target or flood-limited level after the event; (4) keep releases smooth and the number of changes small;
- a **full-fidelity check outside the optimiser**. The recommended release is re-simulated with the exact nonlinear level–storage and capacity curves and the calibrated routing model, against all 51 members and the tributary scenarios, before it is shown to the operator;
- a **pre-agreed fallback**: the current operating rule, or a simple rule based on measured level and inflow. It is used whenever data, solver or check fail.

What the tool executes is only the next 6-h release, rounded to an operable gate setting. Everything else in the plan (the trajectory envelope, the risk numbers, the binding constraint) is explanation.

This choice is provisional. During verification I would compare it against a much simpler alternative: an **offline-calibrated ensemble risk-tolerance rule**. That rule checks what fraction of members exceed a threshold and compares it with a tolerance that depends on lead time, then releases the smallest amount that brings the risk back within tolerance. If closed-loop hindcast replay shows the MPC is not materially better than that rule on downstream exceedance, maximum level and false pre-releases, I would recommend the rule. It is easier to explain and to write into an operating manual. The MPC must earn its added complexity.

## 2. How I would represent the reservoir–river system

### 2.1 Reservoir

- **State:** storage S (level Z = f(S) from the level–storage curve). The internal time step is 1 h. Decisions are taken every 6 h, aligned with forecast issue, and the release is held constant within each 6-h block (or a shorter block if gate practice allows).
- **Balance:** S(t+1) = S(t) + [I(t) − R(t)]·Δt. It is linear in storage, so it stays exact inside the optimiser. The nonlinearity sits only in the curves.
- **Level–storage:** a piecewise-linear fit over the operating range. Level limits (flood-limited level, design flood level, check flood level, any upper safety level) are converted into storage limits, so constraints are written in storage, which is linear.
- **Discharge capacity:** because capacity varies strongly with level, this is the most important nonlinearity. It matters most at the moment pre-release is needed: at lower levels the reservoir cannot release as much, so pre-release must start earlier. I would write it as R(t) ≤ Rmax(S(t)) and approximate Rmax(S) by a **concave piecewise-linear inner (under-)approximation**. Any release the optimiser plans is then truly feasible. If the true curve is not concave over the range, I would use sequential local linearisation around the previous cycle's trajectory, re-linearise once or twice per cycle, and always tighten the result to the lower envelope. Linearisation error is reported each cycle.
- **Other release limits:** minimum release, maximum rate of release change per block (to protect the channel and respect gate practice), spillway or outlet operating rules (for example gate opening sequences), and any restriction on releasing more than inflow during the rising limb. These will be confirmed later. Until then they are configurable constraints.

### 2.2 River reach (dam → control station, 120 km)

- The calibrated routing model is too slow to sit inside a repeated optimisation and is hard to differentiate. It stays as the **reference model**, used to verify every recommendation and to generate training data.
- Inside the optimiser I would use a **reduced linear routing model** identified from the calibrated model: a Muskingum cascade, integrator-delay, or linear transfer function, possibly with separate parameters for low, medium and high flow bands, since travel time and attenuation change with discharge. I would screen candidates by bias, RMSE, NSE and peak-timing error against the calibrated model over the 20-year record and over synthetic high-flow events. I would also check specifically that the reduced model **does not underestimate the station peak** at the flows that matter. Where it does, I would add a calibrated safety margin to the station constraint.
- **Station flow:** Q_station(t) = routed release + routed tributary 1 + routed tributary 2 (+ any residual local inflow). The safe-flow constraint is written at the station, and at any intermediate point with a lower safe capacity if one exists.
- **Horizon:** 10 days is much longer than the reach travel time (likely about a day; to be confirmed from the calibrated model), so releases take effect at the station within the horizon. The 6-h decision step must still resolve the travel time, and the first block's release must be judged by its station effect 1–2 blocks later.

### 2.3 Ungauged tributaries (main structural uncertainty downstream)

The tributaries enter between the dam and the control point. The reservoir can only control its own release, so it has to **leave room for them** in the station flow. I would represent them as follows:

1. **Historical back-calculation.** Over 20 years, observed station flow minus routed observed release gives the combined lateral inflow series. This assumes station and release records exist and are consistent; I would verify that. Its uncertainty includes routing error and should be described as such.
2. **Real-time estimate.** Use a rainfall–runoff model driven by the same meteorological forcing as the inflow ensemble, if that forcing covers the tributary catchments. Otherwise transfer flows from the reservoir inflow forecast by area or regression. Then **update by assimilating the latest station observation**: the station is effectively a lagged sensor for the tributaries.
3. **Joint scenarios with the main inflow.** The same storms drive both, so tributary errors are likely positively correlated with reservoir inflow errors. Treating them as independent would understate joint risk at the station. I would build tributary scenarios conditionally on each inflow member, for example with a copula fitted to the back-calculated lateral errors against the inflow-forecast errors, or by using the same meteorological member. I would then test whether the dependence is significant.
4. **In the constraint:** use a conservative quantile of tributary flow, or the tributary scenarios on the branches themselves, plus the routing margin.

If the back-calculated lateral series turns out to be too noisy to support any model, I would design the station constraint around an upper quantile of lateral flow conditioned on observed rainfall and state that limit to the regulator.

### 2.4 Inflow forecast representation

- **Before use**, verify the 51-member hindcasts against observations for each lead time and flow magnitude: bias, CRPS against climatology and against persistence, rank histograms and spread–error for under-dispersion, Brier score for exceeding operationally meaningful inflow and volume thresholds, and separate statistics for the largest events. This gives the lead time up to which the ensemble adds skill and shows whether it can be trusted in the extremes.
- **Post-process** where needed: bias correction and spread adjustment for each lead time, keeping temporal structure, for example by reordering corrected members with a Schaake shuffle.
- **Ensemble to tree:** reduce the 51 members (each joined with tributary scenarios) to roughly 8–20 branches. Use a mass-preserving reduction, with distances weighted toward volume over the next 1–3 days and toward peak. Branch points are placed where the members actually diverge. The first block is shared by all branches (non-anticipativity), so the tool gives **one** release now, while the later controls may differ by branch. This sits between two failure modes. One common release sequence across all members can be infeasible or overly conservative in a storage-limited reservoir. Fully separate per-member plans cannot be implemented.
- **Beyond 10 days**, add a terminal condition: the end-of-horizon storage must allow a design-standard flood arriving after the horizon to be routed without exceeding dam-safety levels. This prevents the tool from filling the reservoir at the end of the window.

## 3. Modelling and solution method, and why

### 3.1 Formulation

At each 6-h update:

1. Ingest observed level, release and station flow, and estimate current inflow and lateral flow, with the state-estimation uncertainty noted.
2. Build the post-processed joint scenario tree.
3. Solve the tree-based optimisation with the convex internal model:
   - **Hard constraints on every branch:** reservoir balance, storage bounds (maximum level ≤ the applicable dam-safety level), R ≤ conservative Rmax(S), ramping, minimum release, terminal storage condition.
   - **Downstream:** station flow above the safe flow is penalised on every branch. Penalties are tiered (larger above levee-critical stage), and a CVaR term over branches limits the tail rather than only the average. If the regulator works with a probability limit, I would implement it as a scenario-count limit on exceedance and report the achieved probability.
   - **Priority (lexicographic) solve:** first minimise downstream exceedance subject to dam safety. Then, holding that within a small tolerance, minimise deviation from the target level at event end. Then minimise release changes. Each stage is an LP or QP. This avoids arbitrary weights between dam, downstream and conservation goals, and lets the operator be told "this release is the smallest change that keeps the station below X in all but Y% of scenarios".
4. Take the first-block release and round it to an operable gate setting. Re-check that setting against the full nonlinear simulator on all 51 members with tributary scenarios, and against the calibrated routing model. If it fails, tighten the margin and re-solve once. If it still fails, or the solver times out, issue the fallback rule's release and flag it.
5. Produce the explanation package (section 4.4).

**Size:** 240 hourly steps × about 16 branches, with routing states, comes to roughly 10⁴ variables and constraints. An LP or QP of that size with a warm start typically solves in seconds to a minute. Even with two re-linearisations and three lexicographic stages, the optimisation should take well under the 30-minute budget. That leaves most of the budget for data handling and the full-fidelity check.

### 3.2 Why this rather than the main alternatives

| Alternative | What it offers | Why not the primary choice | Role kept |
|---|---|---|---|
| Current operating rule / guide curve | Transparent, approved, familiar | Uses only current state or a short forecast. Cannot exploit the 10-day ensemble or allow for tributary uncertainty. Wastes storage in small floods or pre-releases too late in large ones | Baseline comparator and fallback |
| Deterministic optimisation on ensemble mean or median | Simple, fast | Treats the forecast as certain. Hides the upper tail that drives downstream exceedance, and under-prepares for big events | Benchmark; shows what the ensemble adds |
| Per-member optimisation, then take e.g. the maximum first-block release over risky members | Explainable ("we prepare for the bad members") | No coordination between members. Can be overly conservative and produce false pre-releases. Ad hoc in how it handles tributaries and capacity at low level | Comparator; its logic is reused in the explanation |
| Offline-calibrated ensemble risk-tolerance rule (fraction of members over threshold vs lead-time tolerance curve) | Very explainable, easy to write into a manual, trivial compute | Thresholds are tuned on 20 years and may overfit. Handles downstream tributary coincidence only implicitly. Less flexible in unusual events | **Main competitor**; adopted instead if the MPC's gain is small |
| (Stochastic) dynamic programming | Optimal feedback policy under its assumptions | Curse of dimensionality: routing states plus a 10-day forecast state cannot be carried. Forecast information has to be compressed heavily | Not used; possibly an offline cross-check of the rule |
| Evolutionary multi-objective search on the full nonlinear simulator in real time | Handles nonlinearity directly; gives a Pareto set | Convergence within 30 min not guaranteed. Results vary between runs (hard to defend to a regulator). No optimality certificate | Offline tuning of rule parameters and margins |
| Full hydrodynamic model inside the optimiser | Highest physical fidelity | Too slow; no gradients | Reference model for verification only |
| Analytical rules (KKT, equal marginal value) | Closed form, insightful | Need strong simplifications (normal errors, no lateral inflow, simple capacity) that do not hold here | Interpretation aid only |

The core reasons are as follows. The convex internal model gives reproducible, certifiable solutions in seconds. The scenario tree uses the ensemble without pretending a single trace is right, while still producing one release now. The full-model check outside the loop catches the simplifications.

## 4. How I would verify the method

All tests are run as a **closed-loop hindcast replay**. The tool runs every 6 h through the 20-year record using only the hindcast available at each time. The true inflow is the observed series, and the system is advanced with the full nonlinear simulator and the calibrated routing model. A tool that is never tested in closed loop has not been tested.

### 4.1 Computational efficiency

- Time each step (ingest, post-processing, tributary update, tree building, each solve, re-linearisation, full check, report) over all flood-season decisions in the replay, not just averages. Report the 95th, 99th and maximum percentile times, and check the largest events specifically, since trees and active constraints grow there.
- Target: the whole cycle comfortably below 30 min (say ≤ 10–15 min at the 99th percentile), leaving margin for data delays and an operator re-run.
- Run the 51-member full checks in parallel. Give the solver a time limit and warm start from the last cycle. Define the timeout behaviour (fallback release plus flag) and test it by forcing timeouts.
- Find the tree size at which results stop changing: compare the first-block release and the risk metrics for 4, 8, 16, 32 branches and for 1-h against 3-h internal steps, and keep the smallest size that gives the same decisions within tolerance.

### 4.2 Physical constraints

- For every recommended release in the replay, the full simulator must show zero violations of level limits, capacity Rmax(Z), ramping and minimum flow. Any violation is a design failure, not a statistic.
- Record the linearisation gap (planned against simulated level and capacity) and the reduced-model routing gap (station peak and timing against the calibrated model), especially at high flows, and confirm that the margins cover them.
- Test pre-release feasibility directly. In events where pre-release was needed, could it be completed in time given the lower capacity at lower levels? Compare the required drawdown time with the lead time at which the ensemble first signalled the event.
- Check water balance closure and units at the interfaces (forecast volumes against hourly flows, storage curve units).

### 4.3 Decision reliability

- **Comparators under identical conditions** (same initial states, same events, same constraints): current rule; no-forecast operation; deterministic-mean MPC; per-member heuristic; calibrated risk-tolerance rule; and **perfect-forecast MPC** as the non-deployable upper bound. Placing the ensemble MPC between no-forecast and perfect shows how much of the available forecast value it captures.
- **Metrics:**
  - maximum reservoir level and margin to each safety level;
  - station flow above safe flow: number of events, duration, excess volume, peak;
  - tail metrics over events;
  - false pre-releases (water released for floods that did not come) and missed pre-releases;
  - end-of-event storage and refill;
  - number and size of release changes;
  - **decision stability**: how often the recommendation reverses between consecutive 6-h updates. Operators will not trust flip-flopping.
- **Event trajectories:** review the largest events and the false alarms as time series with operators, not only aggregate scores. The goal is to see why the tool did what it did.
- **Robustness:**
  - leave-one-year-out (or leave-one-event-out) for anything tuned: margins, CVaR level, tree settings, the competitor's tolerance curve;
  - sensitivity to forecast skill (degrade or inflate spread), tributary uncertainty (larger errors, stronger correlation with main inflow), initial level, and capacity-curve error;
  - stress tests with floods scaled beyond the record (e.g. up to the design flood) with matching synthetic forecasts, and consecutive floods;
  - failure modes: forecast missing or late, a member set badly under-dispersed, station data missing.
- **Credibility of components before results:** forecast verification (section 2.4), tributary back-calculation and error model, reduced routing model, scenario-tree fidelity. Check that the reduced tree keeps ensemble means, spread and upper quantiles of 1–3-day volume.
- **Interpretation:** a fall in downstream exceedance should be explained by a mechanism, for example earlier pre-release because the ensemble's upper members signalled the flood 2 days ahead. If the gain comes mainly from one or two events, or only from a higher operating level, I would say so.

### 4.4 Practical implementability

- **Operable output:** releases as discrete gate settings, held for whole blocks, within agreed rates of change. No recommendation that requires gate moves faster than crews can make them.
- **Explanation package each cycle:**
  - recommended release and its hold period;
  - the binding reason (dam level, station capacity in branch k, or the tributary allowance);
  - the probability or fraction of scenarios exceeding the station safe flow and the dam thresholds, with and without the recommended action;
  - the projected level and station-flow envelope (median and upper quantiles);
  - comparison with what the current rule would do;
  - what change in the next forecast would alter the decision.
- **Regulator view:** the priority order (dam safety, then downstream, then conservation) is stated in plain words. Margins and risk levels are written as parameters that the regulator can review. The fallback rule is the approved manual rule.
- **Operator control:** operators can override with a logged reason. Every input, version and output is archived for post-event review.
- **Staged adoption:** shadow-mode running for at least one flood season, with the tool's recommendations recorded alongside actual decisions. Then review with operators and the regulator. Then, if supported, a controlled pilot under a temporary, documented modification of the operating rules. Then decide whether to defer, research further, or update the manual. Post-event reanalysis after each significant flood.
- **Engineering readiness:** data latency (does the 6-h forecast arrive in time?), real-time inflow estimation from level changes (noisy, needs filtering), and redundancy of station data.

## 5. Handling unclear data and engineering constraints in the preliminary design

Several items that shape the design are not given. I would not invent values for them. I would make each one an explicit, configurable assumption with a conservative default, test sensitivity to it, and list it for confirmation.

| Unclear item | Why it matters | Preliminary handling | What would settle it |
|---|---|---|---|
| Safe flow / stage thresholds at the control station (and any weaker reach section) | Defines downstream failure; directly sets releases | Use the officially stated value if one exists, else a range; tiered penalties; sensitivity runs | Flood-defence authority data, levee assessments |
| Dam-safety levels and the acceptable risk the regulator accepts | Hard constraints and the CVaR or probability level | Default to the current rule's achieved risk as the benchmark ("no worse than now"); show results for several risk levels | Regulator agreement |
| Ramping limits, gate rules, minimum flows, release blocks | Determine operability | Take from the operating manual; if absent, adopt conservative values from operating records and confirm with operators | Operating manual, operators |
| Accuracy of level–discharge capacity curve | Pre-release feasibility at low levels | Use the lower envelope; sensitivity to ±x% capacity | Spillway tests, gate calibration |
| Reach travel time and routing validity at extreme flows | Station constraint timing and peak | Flow-banded reduced model, margin calibrated on synthetic high-flow runs with the calibrated model | Calibrated model documentation, flood marks from large events |
| Ungauged tributary areas, forecast coverage, dependence on main inflow | Size of downstream allowance | Back-calculated lateral series; conditional scenarios; upper quantile in constraint | Temporary gauging, rainfall–runoff model for the tributaries, radar rainfall |
| Whether hindcasts were produced with the same forecast system as the operational one | Validity of all verification | Check versions; if they differ, test on the period with the operational version and widen margins | Forecast provider |
| Other objectives (supply, hydropower, environment) and authority to draw below or rise above normal levels | Lower-priority objectives and terminal condition | Treat as the third priority with a target level; do not trade them against safety | Owner and regulator |
| Real-time data latency and quality | Whether 30 min is achievable in practice | Design with a time budget for late data; fallback | IT/operations test |

To prioritise which unknowns to settle first, I would run the replay across the plausible range of each item and see which ones change the recommended releases or the risk numbers. Those come first: most likely the station safe flow, the tributary allowance and the capacity curve. The architecture keeps these as separate modules (tributary estimator, reduced routing, constraint set, risk level), so a better gauge, a revised curve or a regulator decision can be added without redesigning the solver.

## 6. Key assumptions and what would change the recommendation

- **Assumed:** the reservoir operates mainly for flood control with other uses secondary; the inflow ensemble covers reservoir inflow but not the tributaries; observed release and station-flow records exist for back-calculation; the reach travel time is much shorter than 10 days; operators can adjust releases at least every 6 h.
- **Would favour the simpler risk-tolerance rule:** replay shows small MPC gains, unstable recommendations, or the regulator requires rule-based language.
- **Would require a richer model:**
  - if the reduced routing misses station peaks badly in extreme events, use flow-dependent or nonlinear routing with more re-linearisation;
  - if the tributaries dominate station floods, the problem becomes mainly about forecasting the tributaries, and gauging or modelling them is worth more than refining the reservoir optimiser;
  - if the ensemble is unreliable beyond a few days, shorten the effective horizon, rely on the terminal condition, and give more weight to measurement-based rules.
- **Would confirm the design:** in out-of-sample closed-loop replay, the MPC has zero physical violations, finishes within budget at the 99th percentile, gives less downstream exceedance than the current rule with no rise in dam-level risk, has an acceptable false-pre-release rate and stable decisions, and operators judge its explanations usable in shadow mode.
