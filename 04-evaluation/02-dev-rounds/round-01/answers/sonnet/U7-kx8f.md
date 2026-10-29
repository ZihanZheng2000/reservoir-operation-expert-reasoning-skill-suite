# Real-time flood release tool: representation, method, verification

## 1. Provisional recommendation

Build the tool as a **rolling-horizon, scenario-tree stochastic model-predictive control (MPC) optimizer**. It sits inside a transparent, operator-facing layer of hard rules, risk checks and fallbacks.

- **Inside the optimizer**, use a simplified reservoir–channel model (a convex or near-convex program, solved by LP/QP).
- **Outside the optimizer**, use the full calibrated routing model and the exact level–capacity relations. They check every candidate release and update the state each cycle.
- **Each cycle** (every 6 h, within 30 min):
  1. Ingest the latest state and the 51-member forecast.
  2. Reduce the ensemble to a small scenario tree.
  3. Optimize one current release shared by all branches. Later releases may branch as information arrives.
  4. Re-simulate the result with the full model.
  5. Apply risk checks and constraint checks.
  6. Present a recommended release and a permissible band to the operator.
  7. Apply only the first step, then recompute at the next update.

This is a provisional choice. Section 6 lists what would confirm or change it.

Key assumptions, to be confirmed:
- The hindcasts represent the current operational forecast system.
- The decision step is 6 h, matching the forecast update.
- Safety is defined by a maximum reservoir level and a downstream control-station flow or stage threshold.
- Releases go through outlets or gates with a known level-dependent capacity.
- The tool advises operators. It does not control gates automatically.

## 2. How to represent the system

**Reservoir**
- Use a single mass balance per step: storage(t+1) = storage(t) + (inflow − release − losses)·Δt. Take Δt = 6 h as the base step. Test 3 h if the hindcasts show sub-6-h inflow rise matters.
- Use the level–storage curve as a piecewise-linear table.
- The discharge capacity depends strongly on level, so it is a key part of the representation.
  - **It creates a time-feasibility problem.** At low level the outlet cannot release much, so a late decision cannot undo an early mistake. The planner must therefore look ahead: drawdown has to start early enough to be physically possible.
  - **Treatment in the optimizer.** Impose release ≤ capacity(level) with a piecewise-linear, conservative inner approximation. Evaluate capacity at the lowest level the step can reach. This never promises more release than the real outlet can deliver.
  - **Exact check outside the optimizer.** Forward-simulate with the true curve.
  - **If the conservative version is too restrictive,** use a sequential linearization around the current plan with a trust region, or a mixed-integer formulation if gates or spillway regimes switch discretely. Decide this from the real curve shape and gate layout, which I do not yet know.
- Release constraints: minimum and maximum release, ramp (change per step) limits, and the gate or outlet configuration. All of these are configuration inputs, because they are not yet confirmed.

**River reach (120 km, dam to control station)**
- Inside the optimizer, use a **reduced routing model**: a pure delay plus attenuation (an integrator-delay or Muskingum-type form), or a linearized state-space form.
- Keep the **full calibrated routing model** as the verifier and state estimator. It runs once per cycle on the chosen plan and on selected scenarios.
- Why reduce: the full model is likely too slow and not differentiable enough to sit in a repeated optimization. Papers using detailed hydraulics inside control loops usually kept them outside the loop for exactly this reason.
- Calibrate the reduced model against the full model over the realistic range of flows, especially high flows. Report the discrepancy, and add a safety margin equal to the high-flow discrepancy where it matters.

**Ungauged tributaries (two, uncertain real-time flows)**
- Represent them as an **additive lateral inflow with its own uncertainty**, entering the reach at their confluence positions and routed to the control station. They are not forecast-driven state variables.
- Real-time estimate: take the control-station observation minus the routed dam release (inverse mass balance). Where rainfall or a rainfall–runoff relation is available, blend the two. Update each cycle from the residual between the observed and predicted control flow.
- Uncertainty: fit an error model from the history of that residual, by flow regime and by season if the data allow. Treat the error as correlated with rainfall and with the dam-inflow forecast error. Preserve this dependence when generating scenarios, for example with a copula or a shuffle method, rather than assuming independence. Independence would understate joint risk because the same storm drives all three.
- In the optimizer, the downstream constraint is: dam release routed + tributary inflow ≤ safe control-station flow, enforced in a risk sense (Section 3). Because the tributaries cannot be forecast well, a conservative tributary quantile reduces the release room available to the dam. This is a large explainable lever. If tributary uncertainty turns out to dominate, the practical decision rule becomes margin-based, not optimization-based.
- The tributaries reduce the dam's useful lead time. The release you decide now affects the control station only after the travel time. Pick a horizon that covers at least the dam-to-station travel time plus the time to recover storage. The travel time is not given, so it is an assumption to confirm.

**Forecast uncertainty**
- Use the 51 members as the primary uncertainty description, after checking them against the 20-year hindcasts:
  - Bias, spread and reliability by lead time and by flow level (rank histograms, spread–error, a probabilistic score), with separate attention to large events.
  - Whether the ensemble is under-dispersed at long lead times.
  - Whether errors vary with lead time, season or flow (they usually do).
- Apply bias correction and spread inflation where the hindcasts justify them. Keep the member-to-member time dependence. Do not resample members independently across time.
- The hindcasts contain few large floods in 20 years. For rare, extreme events, generate **scaled or synthetic stress events** (for example, scale the largest observed floods with their forecasts to larger return periods, keeping hydrograph shape and error attributes). State these are stress tests, not observations.
- Other uncertainties that move the outcome: initial level and storage error, the level–discharge capacity relation (gate behavior), and tributary flows. List which are included and which are excluded by scope, and state the exclusions. I would include the initial state, tributaries and capacity error as small perturbations, and exclude wind, backwater and storage-curve error unless a sensitivity test shows they matter.

## 3. Objective and constraints (what the optimizer is told)

Treat safety as a priority ordering, not a weighted score.

1. **Hard limits (never violated in the planned trajectory):** maximum reservoir level, release ≤ capacity(level), ramp limits, minimum release.
2. **Safety risk limits (chance or tail constraints on the tree):**
   - Reservoir level above its safety threshold.
   - Control-station flow or stage above its safe value (including the tributary contribution).
   - Each is bounded by an acceptable probability, optionally with a tail measure (CVaR) so that a rare but severe branch is not hidden by a mean.
   - The acceptable-risk benchmark should be the current rule's risk or a regulatory standard. I do not know which applies, so I treat it as a parameter to be agreed with the regulator.
   - With 51 members, tail probabilities below about 2% cannot be resolved from the ensemble alone. The synthetic stress events and conservative margins cover the rarer end.
3. **Then minimize** expected peak downstream flow and expected maximum reservoir level, and finally recover storage by the end of the horizon (a soft terminal condition, because the exact end level can conflict with safety) and keep release changes smooth.

Using a priority ordering with an explicit safety constraint avoids hiding a safety trade-off inside a weight that the regulator cannot inspect. If other objectives (such as generation or supply) are required, add them only below safety, and keep a Pareto view rather than collapsing them into one number too early. These objectives are not specified in the question.

## 4. Why this method, and why not the alternatives

**Chosen: scenario-tree stochastic MPC with a shared current release.**
- It uses the ensemble directly, which matters because the forecast is the main information source and it is probabilistic.
- The tree keeps one common current release. Later releases may branch, because information resolves later. A fully independent release per member would not be implementable, and one fully shared control sequence for all members can be infeasible in a storage-limited reservoir.
- Re-optimizing every 6 h gives a feedback loop that corrects for forecast error without needing a perfect model.
- With the reduced reach model and piecewise-linear curves, the program is an LP or QP of a size that solves quickly. Computation can be bounded.
- Its outputs are explainable: planned trajectories, binding constraints and their shadow prices, and a risk statement per branch.

**Alternatives and why I would not make them the main method:**

| Alternative | Why not the primary choice |
|---|---|
| Stochastic dynamic programming (SDP/SSDP) | The state would need reservoir storage, forecast information, tributary flow and channel states. This is high-dimensional, and the forecast-update dynamics are hard to encode. It does give an offline policy, but fitting it to the 51-member, 10-day, 6-h updating forecast is impractical. I would use it at most as a simplified check. |
| Deterministic MPC on the ensemble mean or a single forecast | Cheapest, but it hides forecast uncertainty and is likely to under-prepare for large events or over-release for small ones. Keep it as a baseline, not the product. |
| Independent optimization per ensemble member | Gives a release per member, but there is no single implementable current release. It needs an ad hoc aggregation step. It is also not a verifiable decision rule. |
| Evolutionary or direct policy search | Slow to run each cycle, and constraint handling is weak. It suits offline calibration of rule parameters (for example, risk-tolerance curve parameters) but not 30-min real-time optimization. I would use it offline for tuning, not in the loop. |
| Nonconvex global solvers | Risk of exceeding the 30-min window, and optimality is hard to verify independently. Keep for benchmarking small cases only. |
| Pure rule-based or ensemble-risk rules (no optimizer) | Easy to explain and fast, but they do not coordinate with the downstream reach and tributary margin, or adapt to a strongly level-dependent capacity. I would keep a simple risk-tolerance rule as the **fallback** and as the explanation layer. |
| Analytical (KKT) rules | They give clear rule forms, but they need convex loss functions and distribution assumptions that do not hold for the full system. Use them only to understand and sanity-check behavior (for example, a hedging pattern). |
| Full hydraulic model inside the optimization | Too costly for the 30-min budget and not suitable for repeated gradient-based optimization. Kept outside the loop as the verifier. |

## 5. How the 51-member ensemble is made tractable

- Reduce 51 members to a scenario tree of roughly 8–16 branches. Branch so that scenarios share history until uncertainty can be resolved, and preserve the probability-weighted ensemble mass.
- Always keep the high-risk tail members, or add one or two explicitly chosen conservative scenarios, so that reduction cannot drop the flood that matters. Check the reduced tree's risk estimates against the full ensemble.
- Choose the tree size and horizon by a sweep: closed-loop performance versus solve time over, for example, 1–32 branches and 3–10 day horizons. Papers that did this found performance flattened beyond a moderate tree size while cost rose. Select the smallest tree and horizon beyond which results stop changing. Do not assume 10 days is useful: forecast skill at the far end may be too low to support an action, so weight or limit later lead times accordingly, based on the hindcast skill by lead time.
- A compact time grid (finer first 1–2 days, coarser later) reduces size without losing the near-term detail that matters for the current release.

## 6. How I would verify the method meets each requirement

Run all tests as a closed-loop hindcast: at each forecast cycle, use only information available then, apply the first release, advance the simulation with the observed inflow and the full model, and repeat. This is about 20 years × 4 cycles/day. Use all flood events above a threshold plus a random sample of non-flood periods, and add stress events.

### 6.1 Computational efficiency (30-minute limit)
- Time every cycle on the intended production hardware, including data ingestion, scenario reduction, solve, full-model re-simulation and reporting. Report the median, the 95th and 99th percentiles and the worst case, especially during major floods, where the level-dependent capacity makes the problem hardest.
- Allocate the budget explicitly: for example, a few minutes for ingestion and reduction, a capped solve (with warm start from the previous plan), and time reserved for the full-model check and reporting.
- Build an **anytime fallback**: if the solver has not converged by the cap, use the best feasible solution found. If that is not available, fall back to the simple rule-based recommendation and flag it. Measure how often the fallback triggers.
- Test scaling with tree size, horizon and step to know how much margin exists.
- Pass criterion: all cycles, including the worst, finish well within 30 min with a stated margin. The margin value is a design choice I would set with the team.

### 6.2 Physical constraints
- Re-simulate every recommended release with the **full** routing model and the **exact** level–capacity curve, not only the reduced model. Check at every step across all branches:
  - Mass balance closes.
  - Level stays within limits.
  - Release ≤ capacity at the actual level.
  - Ramp and minimum release limits hold.
  - Gate or outlet settings are physically realizable after rounding.
- Report the discrepancy between the reduced and the full model, especially at high flows and at the capacity transitions. Add a margin if the discrepancy is not negligible.
- Run a historical check: simulate historical operations from the same initial conditions and compare with observed levels and flows. This tests the simulator and the reach model, not the tool.
- Pass criterion: zero hard-constraint violations in the re-simulation. Any violation is a defect, not a trade-off.

### 6.3 Decision reliability
- **Baselines under identical conditions:** the current rule, no-forecast operation, a deterministic-forecast MPC, and a perfect-forecast bound (non-deployable). The perfect-forecast bound separates forecast limitations from method limitations.
- **Metrics:** peak and exceedance of reservoir level and control-station flow, frequency of threshold exceedance, tail loss (CVaR) of the worst events, spill, refill success, release variability, and **stability between consecutive cycles** (so that recommendations do not oscillate as the forecast updates).
- **Risk-estimate checks:** verify the tool's predicted risk against realized hindcast outcomes (calibration). Verify with independent samples or an alternative method that the reduced-tree risk matches full-ensemble or Monte Carlo risk.
- **Robustness and stress:**
  - Forecast error inflated or biased.
  - A missed event (a forecast that fails right after a prerelease, with the next flood arriving immediately).
  - Tributary uncertainty scaled up.
  - Initial-level error.
  - Capacity-curve error.
  - Missing or late data.
  - Scaled floods beyond the record.
  - Ensemble size and tree size.
- **Out-of-sample:** any tuned parameter (risk tolerance curve, tributary margin, spread inflation) is chosen using leave-one-year-out or held-out events. Do not tune and score on the same events.
- **Caveats to report:** with 20 years there are few large floods. Results on rare floods rest on synthetic scaling and carry a generator bias. Perfect and no-forecast comparators are benchmarks, not controlled counterfactuals. Say plainly what the evidence supports and what it does not.
- Pass criterion: no worse than the current rule on safety metrics at the agreed risk benchmark across events and stress tests, with demonstrated benefit or neutrality on other objectives. If the tool is better on average but worse on a severe event, treat that as a finding to resolve, not an average to accept.

### 6.4 Practical implementability and explainability
- **Operator-facing outputs:** a recommended release for the next step, a permissible band, the plan for the next 24–72 h, the share of ensemble branches that exceed each threshold under the recommendation, which constraint is binding, and a comparison with what the current rule would do.
- **Regulator-facing explanation:** a documented priority order (hard limits, then risk limits, then secondary goals), the risk benchmark and who agreed it, and a worked example for a past flood showing each cycle's decision. Distilling the optimizer's behavior into simple threshold rules (for example, with a shallow decision tree) can support an audit, but only as an explanation, not as a replacement.
- **Execution:** respect gate operating limits, minimum hold times and the number of gate changes, and round to realizable settings. Test the rounded schedule in the full model.
- **Failure handling:** data outage, late forecast, solver failure, or forecast clearly wrong against observation. In these cases move to a measurement-based rule (using current level, inflow and rainfall) or a conservative gradual correction. Define the trigger conditions before use.
- **Human role:** the operator accepts, adjusts or overrides, and the override and the reason are logged. This is an advisory tool until the regulator agrees otherwise.
- **Adoption path:**
  1. Offline hindcast.
  2. Shadow-mode operation through at least one flood season, comparing recommendations with actual operator decisions (without acting).
  3. Review with the operators and the regulator.
  4. A controlled pilot if the manual allows it.
  5. Post-event review and revision.
- I have no evidence from the question about the regulator's approval process or legal limits, so I list these as items to confirm rather than assume.

## 7. Handling key unknowns in the preliminary design

For each unknown, use a stated provisional value or conservative default, make it a configuration input, and test how much it matters.

| Unknown | Provisional handling | What would change the design |
|---|---|---|
| Downstream safe flow or stage and the acceptable-risk level | Use a conservative threshold with a buffer below the danger level. Take the current rule's risk as the provisional benchmark. Ask the regulator to confirm. | A stricter or looser standard moves the risk limit and the margin. |
| Channel travel time and attenuation | Estimate from the calibrated routing model. Cover it in the horizon. | If it is long, the horizon and tributary margin grow. If it is short, a finer time step may be needed. |
| Tributary flow magnitude and uncertainty | Estimate by inverse mass balance. Use a conservative quantile. Run a sensitivity test with scaled uncertainty. | If tributaries dominate downstream flow, move toward a margin-based rule and invest in gauging or rainfall data. |
| Outlet and gate configuration, ramp limits, minimum hold | Treat as configuration inputs with conservative values. Check realizability by re-simulation. | Discrete gate logic would push the formulation to a mixed-integer or a rounding post-step. |
| Shape of the level–capacity curve | Use a conservative piecewise-linear inner approximation, then verify with the exact curve. | A strongly nonconvex curve needs sequential linearization or discrete modeling. |
| Forecast skill at long lead times, and whether hindcasts match the operational system | Quantify skill by lead time and flow level from the hindcasts. Limit or down-weight later lead times. | If skill is poor beyond a few days, shorten the horizon or lean on the rule-based risk layer. |
| Rare extreme floods | Use synthetic scaled floods as stress tests, labeled as such. Add conservative scenarios to the tree. | Risk estimates for the rarest events remain uncertain, so state them as bounds. |
| Regulatory and institutional constraints | Keep the tool advisory, inside current rule-curve practice, and keep logs. Ask early about approval requirements. | Requirements may force simpler outputs or staged adoption. |
| Initial level and measurement quality | Include small state perturbations and a data-quality check. | If measurement error is large, increase the safety margin. |

## 8. Order of work

1. Assemble and align the data: forecasts, hindcasts, observations, rating and capacity curves, operating rules and records. Encode the current rule as an executable baseline.
2. Verify the forecasts by lead time and flow level. Decide what lead times can support which actions.
3. Build and check the simulator: reservoir balance, full routing, tributary estimator. Check against history.
4. Build the reduced internal model and quantify its discrepancy with the full model.
5. Generate scenarios (with dependence), reduce to a tree, and check the reduction.
6. Formulate and solve the rolling optimization. Run the size and horizon sweep for computing time and performance.
7. Run the closed-loop hindcast, baselines, stress tests and out-of-sample tests.
8. Run shadow-mode operation, then operator and regulator review. Revise and repeat where a result fails an earlier requirement.
