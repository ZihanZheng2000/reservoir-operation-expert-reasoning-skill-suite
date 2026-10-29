# Real-time release decision tool for a flood-control reservoir: representation, method, verification

## 0. Provisional recommendation

**Recommendation:** I would use an **ensemble-based multi-stage stochastic model predictive control (tree-based MPC)**. It rolls forward every 6 hours on the 51-member forecast after post-processing. It has four parts:

- a **reservoir mass balance** that includes the nonlinear, level-dependent discharge capacity;
- a **fast, linear surrogate of the calibrated channel routing model** for the 120 km reach, used inside the optimizer;
- **probabilistic lateral inflows** for the two ungauged tributaries, estimated from the downstream control station's residuals;
- **operating constraints** written the way operators think: gate steps, ramp rates and hold times.

Only the first-stage release (the next 6–12 h) is implemented. Every recommendation is then checked again with the full routing model and the exact level–capacity curve. A transparent rule-based fallback is always computed alongside it.

**Why this approach:**

- It is the only class of method that does all of the following within 30 minutes:
  - uses the full forecast ensemble rather than just its mean;
  - respects hard physical constraints exactly;
  - gives a single, actionable decision that does not anticipate which member will verify;
  - produces explanations that the regulator can audit: binding constraints, risk numbers, and a comparison with the rule-based release.

**Key assumptions and what would change this choice:**

- **Assumptions:**
  - The flood objectives can be stated as stage or discharge limits at the control station and the dam, plus levels that must not be exceeded.
  - The routing in the reach is close enough to linear over the operating range that a surrogate stays within an acceptable error.
- **What would change it:** strong hysteresis or backwater in the reach, or a regulator who requires a fixed, codified rule. See Section 6.

---

## 1. Representing the reservoir–river system

### 1.1 Spatial and temporal structure

- **Nodes:**
  1. reservoir (inflow node);
  2. dam outlet works;
  3. routing reach from the dam to the control station, split into sub-reaches at the two tributary confluences;
  4. tributary A lateral inflow;
  5. tributary B lateral inflow;
  6. downstream control station, the point where flood performance is judged.
- **Time step:** 6 h decision step, to match the forecast update. Internal routing is computed at 1–3 h, depending on the reach travel time.
- **Horizon:** the full 10-day forecast lead. Beyond day 10, a terminal condition is added (see 1.4). This matters because a 10-day forecast on a large reservoir carries real information about flood volume, not only about the peak.

### 1.2 Reservoir

- **State:** storage S_t, converted to level h_t through the level–storage curve.
- **Mass balance:** S_{t+1} = S_t + Δt·(I_t − R_t − spill_t − losses).
  - Losses are negligible at flood time scales, but this assumption should be checked.
- **Release:** R_t = Σ over outlets (gates, bottom outlets, spillway). Each outlet is bounded by a level-dependent capacity: 0 ≤ R_t ≤ Q_max(h_t).
  - This is the key nonlinearity. At low level the reservoir **physically cannot** release what an optimizer would like, so this constraint is what stops "pre-release" plans from being infeasible.
- **Representing Q_max inside the optimizer:**
  - Q_max(h(S)) is typically monotone and concave in S over the operating range. I would use a **piecewise-linear inner approximation** of it in storage space, which keeps the problem LP/QP-convex while staying conservative.
  - If it is not concave, I would use either sequential linearization around the previous solution (2–3 iterations) or a small MILP with SOS2 breakpoints.
- **Level bounds:**
  - the operating band;
  - flood-control pool limits;
  - dam-safety level (hard);
  - surcharge level (hard or heavily penalized, as the safety case requires).
- **Operational constraints:**
  - ramp rate |R_t − R_{t−1}| ≤ ΔR_max;
  - minimum environmental or navigation flow;
  - discrete gate increments, if they apply (see 1.5).

### 1.3 Downstream reach and ungauged tributaries

**Routing inside the optimizer.** The calibrated channel routing model (probably hydrodynamic or a nonlinear hydrologic model) is too slow and too nonlinear to embed in an optimization over 51 members and 40 time steps. I would:

1. Build a **linear surrogate**, as follows:
   - Use a multi-segment Muskingum or Muskingum-Cunge cascade, or equivalently a set of discrete impulse-response kernels (one per input point: dam, tributary A, tributary B) to the control station.
   - Identify the surrogate by running the calibrated model over a designed set of release and lateral-inflow sequences that span the operating range.
2. Where the response depends on flow level (for example overbank flow), fit **2–3 flow-regime-dependent kernels**. Choose the kernel by the forecast flow level in the current solve, or by the previous solution.
3. Quantify the surrogate error against the full model, especially for peak magnitude and peak timing at the control station. Carry that error into the constraints as a safety margin (back-off).
4. Run the **full calibrated model as an after-the-fact check** on every recommended release schedule (Section 4.2).

**Ungauged tributaries.** These are the largest structural uncertainty downstream. I would represent them as **ensemble lateral inflows with a calibrated error model**, not as single values:

- **Back-calculation:** historical combined lateral inflow can be estimated as observed flow at the control station minus routed dam release (from the calibrated model). This uses the 20 years of observations.
  - It gives a time series of combined tributary contribution, and it also reveals the routing model's error.
  - Splitting the total between the two tributaries is not identifiable from this alone. Area ratios or regionalized rainfall–runoff parameters give a prior split. The split matters mainly if the confluences are far apart in travel time.
- **Real-time estimate:** the same residual, computed in real time with the appropriate lag, acts as **data assimilation**. It updates the current tributary state, for example through an error-correction or state-updating step in a simple rainfall–runoff or regression model of the tributaries.
- **Forecast:**
  - If the forecasting system also gives precipitation or tributary flows, I would drive a simple tributary model with them, member by member. This keeps the reservoir inflow and the tributary flows from the same storm consistent.
  - If only reservoir-inflow ensembles exist, I would build a conditional model from the hindcast period that relates tributary flow to reservoir inflow (with lag), and keep its residual spread.
  - In both cases, the **correlation between reservoir inflow and tributary flow** must be preserved. Treating them as independent would understate the joint flood risk.
- **Optimizer input:** a joint ensemble (reservoir inflow, tributary A, tributary B) for each scenario.

### 1.4 Objectives and the end of the horizon

**Hierarchy of objectives**, best handled as hard constraints where safety demands it and as prioritized penalties otherwise:

1. Dam safety: never exceed the safety level. This is a hard constraint.
2. Downstream flood protection: keep control-station flow or stage below the safe channel capacity Q_safe.
   - Penalize exceedance, with risk control through CVaR or chance constraints over the scenarios.
3. Keep storage within the flood-control allocation, and avoid upstream inundation, if relevant.
4. Return to the target storage after the event, so as not to lose flood space for the next event or water for supply.
5. Smoothness and operational simplicity: penalize changes in release and the number of gate moves.

**Terminal condition:** a target storage band at the end of the horizon, or a value-of-storage function. Without it, the optimizer will "spend" flood space at the end of the 10-day window.

### 1.5 Operational realism built into the representation

- Releases are defined in **operator units**: gate openings and number of gates, mapped to discharge through the level–discharge relationship. Alternatively, releases are discharge targets that are then translated to gate settings.
- **Minimum hold time** for a release decision, for example 6–12 h. This matches how the reservoir is actually run and how decisions are documented.
- Constraints on the **rate of change of downstream flow**, for bank stability and warning time, if these apply.

---

## 2. Modelling and solution method

### 2.1 Chosen method: tree-based (multi-stage stochastic) MPC with risk control

**Scenario tree:**

- Start from the 51 post-processed members.
- Reduce them to a tree with about 10–25 leaves, using forward or backward scenario reduction (Kantorovich distance) on the **joint** reservoir and tributary series.
- Branch at the times when ensemble spread grows enough to matter for decisions, for example at day 1, day 3 and day 5.
- Where the budget allows, use all 51 leaves: with an LP formulation this is often affordable.

**Non-anticipativity:** decisions are shared across all scenarios until their paths split. In particular, the **first-stage release is a single value**, and that is what the operator carries out.

**Formulation:**

- Use an LP, or a convex QP if quadratic smoothing is used. The surrogate routing and the piecewise-linear capacity keep it convex.
- Use CVaR at level α, for example α = 0.9–0.95, on downstream exceedance and on the reservoir-level exceedance volume. Alternatively, use chance constraints made workable by scenario approximation.
- **Size:** about 25 scenarios × 40 steps × (storage, release, several outlets, routed flow) gives on the order of 10⁴ variables. Commercial or open-source LP/QP solvers handle this in seconds to a minute.

**Rolling cycle (every 6 h):**

1. Ingest the new forecast and post-process it. Update the tributary state from the residual at the control station.
2. Build the scenario tree.
3. Solve.
4. Run the full-model check and the exact-capacity check.
5. Run the fallback rule.
6. Show the result to the operator.

**Forecast post-processing using the 20-year hindcasts:**

- Correct bias and spread by lead time and by flow regime, for example with quantile mapping plus an EMOS- or BMA-type spread correction.
- Pay particular attention to **high-flow tails**, which is where under-dispersion usually hurts most.
- Verify with rank histograms, reliability diagrams for exceedance of key thresholds, CRPS and Brier skill by lead time.
- This also sets the **useful lead time** for decisions: if skill beyond, say, day 6 is weak, branching after day 6 is coarse and the terminal condition carries more of the weight.

### 2.2 Why this instead of the main alternatives

| Alternative | Strength | Why not chosen as the core |
|---|---|---|
| **Fixed rule curves / operating rules** (status quo) | Fully transparent, already accepted by the regulator | Ignore the forecast, so they cannot pre-release ahead of a forecast flood or hold back when tributaries peak. Typically conservative or reactive. **Kept as a fallback and as a benchmark.** |
| **Deterministic MPC on the ensemble mean or median** | Simple and fast | The mean smooths out peaks and gives no risk information. It systematically under-protects against the upper-tail members that drive flood damage. It cannot state "probability of exceeding Q_safe". |
| **Multi-scenario MPC with one release path shared by all members** (no branching) | Robust, simple | Too conservative: it ignores that the operator will receive new forecasts every 6 h. It may trigger unnecessary large pre-releases and lose storage. |
| **Stochastic dynamic programming (SDP / SSDP)** | Gives a policy, handles uncertainty properly | Curse of dimensionality: the routing reach and tributaries add many states. It is hard to condition on a 51-member, 10-day ensemble, and 30-min re-solves at fine resolution are impractical. More suited to designing seasonal policies offline. |
| **Direct policy search / evolutionary multi-objective optimization (e.g. NSGA-II with the full simulator)** | Handles nonlinearity, shows Pareto trade-offs | Too slow for 30-min real-time use with 51 members and full routing. No guarantee of feasibility or optimality, and results vary from run to run, which is hard to defend to a regulator. **Useful offline** to tune objective weights or CVaR level and to study trade-offs. |
| **Deep reinforcement learning / ML surrogates of the whole decision** | Very fast at runtime | Rare extreme floods are short in 20 years of data. No guarantees on hard constraints. Explanation and audit are weak. Hard to certify for dam safety. **Possibly useful** as an ML emulator of the routing model, if the linear surrogate turns out inadequate. |
| **Full nonlinear MPC with the hydrodynamic model in the loop** | Most physically faithful | Nonconvex. Solve times with an ensemble are uncertain and may break the 30-min limit. Convergence to a local optimum is hard to explain. **Kept as the verification layer**, not the optimizer. |

**Why tree-based MPC fits these particular requirements:**

- **It fits the data:** it uses a 51-member, 10-day ensemble updated every 6 h, with hindcasts that let us calibrate both the ensemble and the risk level.
- **It fits the physics:** the level-dependent capacity and the routing enter as explicit constraints, not as soft guesses.
- **It fits the time budget:** a convex problem solves in minutes or less.
- **It is understandable and auditable:**
  - it gives one first-stage release plus a fan of planned futures;
  - the binding constraints can be stated in plain language (for example, "release is limited by gate capacity at current level", or "downstream flow constraint binds at hour 54 when tributary A peaks");
  - risk metrics are stated directly ("P(Q_control > Q_safe) = 3 % under this plan vs 18 % under the rule curve").

---

## 3. Explainability and operator interface (part of the design, not an afterthought)

For each 6-h cycle, the tool would show the following.

- **The recommendation:**
  - the recommended release for the next 6–12 h, in gate settings and in m³/s;
  - its feasibility status from the full-model check.
- **Forecast fans:**
  - ensemble fans of reservoir level and control-station flow under the recommended plan;
  - the same fans under the rule-curve fallback.
- **Risk numbers:**
  - probability of exceeding Q_safe at the control station;
  - probability of exceeding key reservoir levels;
  - expected exceedance volume.
- **Why this release:** which constraints are binding, and which scenarios drive the decision (for example, "the upper 10 % of members, which show a second storm on day 4").
- **Change log** against the previous recommendation, and the reason (for example, "new forecast raised day-3 inflow peak by 20 %").
- **What-if tools:** the operator can enter an alternative release and immediately see its risk numbers, from a fast simulation using the same tree.

All inputs, the solver version, the parameters, the outputs and the operator's actual decision are stored, giving an **audit trail for the regulator**.

---

## 4. Verification plan

### 4.1 Computational efficiency (≤ 30 min per decision)

- **Time budget:** split the 30 min into data ingest and post-processing, tree construction, solve, full-model check, fallback and reporting. Target **≤ 10 min end-to-end** under normal conditions, so there is room for a re-solve if the full-model check fails.
- **Benchmark on the hardest cases:**
  - the largest historical floods and synthetic scaled floods, where constraints bind most and the solver works hardest;
  - for each, report solve time (median, 95th percentile, maximum), iteration counts and worst-case behaviour of the sequential-linearization loop.
- **Scaling study:** solve time against the number of tree leaves (10, 25, 51) and the time step (6 h vs 3 h), together with the solution quality lost at each level. Choose the largest tree that comfortably fits.
- **Failure handling:**
  - a hard solver time limit;
  - a warm start from the previous solution;
  - if the solve fails or exceeds the limit, automatically fall back to the reduced tree, then to the rule-curve release, with a clear flag to the operator.
- **Test environment:** the target operational hardware with realistic data latency, not only a development workstation.

### 4.2 Physical constraints

- **Exact-capacity check:** for every recommended schedule, recompute the release limit with the exact level–discharge curve over every scenario. Confirm the planned releases are achievable, and report any infeasibility caused by the piecewise approximation (expected to be zero with an inner approximation).
- **Full routing check:** run the calibrated routing model with the recommended schedule plus the tributary ensemble. Compare control-station peak and timing with the surrogate.
  - If the full model shows exceedance that the surrogate missed, raise the margin (back-off) and re-solve.
  - Track surrogate error statistics over all hindcast replays.
- **Mass-balance closure:** check level–storage consistency and mass-balance closure every time step.
- **Rule checks:** ramp rates, minimum flows, gate increments and hold times, for every output.
- **Unit and limit tests:**
  - releases are never negative and never exceed capacity;
  - releases are never above inflow when the level is below the minimum level;
  - behaviour at the curve boundaries (outside the tabulated range).

### 4.3 Decision reliability

The main evidence is a **closed-loop hindcast replay** over the 20-year record:

1. Every 6 h, give the tool only the information that was available at that time: the hindcast ensemble, and observations up to that time with a realistic delay.
2. Carry out the first-stage decision.
3. Simulate the "true" system response using **observed** inflows and back-calculated tributary flows with the full routing model.
4. Move forward 6 h and repeat.

**Comparators:**

- historical operation, if records exist;
- the rule-curve policy;
- deterministic MPC on the ensemble mean;
- tree MPC without forecast post-processing;
- **perfect-forecast MPC**, as an upper bound, to measure how much of the achievable benefit is captured.

**Metrics:**

- downstream: number of events, hours and volume above Q_safe at the control station; peak reduction;
- dam: maximum reservoir level reached and margin to the safety level;
- false alarms: unnecessary pre-releases, and storage not recovered after the event;
- regret against perfect information;
- operational burden: number of gate changes, frequency of reversals;
- risk calibration: does the stated "P(exceed) = x %" match observed frequencies over many decisions? This is a reliability diagram for the tool's own risk statements.

**Robustness tests:**

- **Event-based stratification:** single-peak vs multi-peak floods; floods driven by the tributaries vs by reservoir inflow; floods arriving while storage is high.
- **Stress tests:**
  - synthetic floods scaled to design-flood magnitudes;
  - deliberately degraded forecasts (missed event, timing error, under-dispersion);
  - tributary flows set to the upper tail, or tributaries assumed fully correlated with reservoir inflow;
  - partial gate unavailability.
- **Sensitivity:** to CVaR level α, objective weights, tree size and terminal storage target. Show the regulator how sensitive outcomes are to these choices.
- **Statistical caution:**
  - 20 years contain few extreme events, so rank comparisons on major floods have wide uncertainty. Report results by event, with confidence intervals where possible, and lean on synthetic stress tests for the extremes.
  - Use leave-years-out cross-validation for forecast post-processing, so that the replay is not tested on the same data used to calibrate it.

### 4.4 Practical implementability

- **Shadow mode:** run in real time for at least one flood season, side by side with current practice. Compare recommendations with actual operator decisions and record the reasons for any differences.
- **Operator workshops:** walk through past events with operators and test whether they can interpret the outputs. Adjust the presentation and the constraints, for example hold times, preferred gate sequences and night-time limits.
- **Regulator review:**
  - documentation of the formulation, assumptions, fallback logic and verification results;
  - agreement on which constraints are hard, which risk level is acceptable, and how decisions are documented;
  - a demonstration that the tool never recommends releases that break existing regulations, unless an explicit deviation procedure is followed.
- **Robustness to missing data:** forecast delivery fails; control-station data are missing; one ensemble member is corrupted. Each case needs a defined degraded mode.
- **Maintainability:**
  - re-identify the routing surrogate after channel changes;
  - recalibrate forecast post-processing annually;
  - version control all parameters.

---

## 5. Handling unclear data and engineering constraints in the preliminary design

Several important items are not given in the question. I would **not** fix them silently. Instead I would make them **explicit, configurable parameters** with conservative defaults, test sensitivity to each one, and resolve them with the owners.

| Unclear item | Preliminary handling | How to resolve |
|---|---|---|
| Downstream safe discharge or stage at the control station, and whether other points (towns, levees) between dam and station also need protection | Use the regulator's current value as the hard target. Add intermediate checkpoints as configurable nodes in the routing surrogate. | Elicit from the regulator and flood agency. Check against levee and flood-map data. |
| Dam-safety and surcharge rules, flood-control pool limits, required drawdown/refill rules | Treat as hard constraints at the current approved values. Flag any that conflict with forecast-based pre-release. | Review of the operating manual and the regulator; a formal deviation process if forecast-based operation needs flexibility. |
| Gate operation limits: ramp rates, hold times, gate sequence, number of available gates, response time | Use conservative assumptions, for example a minimum hold of 6 h and modest ramp rates. Test sensitivity. | Interviews with the operations team; the gate manufacturer's and maintenance records. |
| Accuracy of the discharge-capacity curve, especially at high heads | Use an inner (conservative) approximation. Treat curve uncertainty as a margin at high levels. | Compare with any measured releases. Commission a hydraulic check if gaps are large. |
| Tributary areas, response times and flood magnitudes | Back-calculated residual from the control station, prior split by area. Wide uncertainty bands. Stress tests with upper-tail and fully correlated tributary flows. | Install temporary gauges, or use radar-rainfall-based estimates. Update the error model as data accumulate. |
| Whether precipitation or tributary forecasts exist in the ensemble system | Design both paths (precipitation-driven tributary model vs conditional regression on reservoir inflow). | Check with the forecasting provider. |
| Validity range of the calibrated routing model (e.g. overbank flows, backwater from the tributaries) | Regime-dependent surrogate kernels. Margins from full-model comparison. Full-model check of every decision. | Review calibration events. If large floods are outside the calibration range, flag this as a limitation and test with synthetic events. |
| Relative weights of objectives (downstream vs reservoir level vs storage recovery) and the acceptable risk level | Fix the hierarchy: dam safety > downstream protection > storage. Show trade-off curves for α and the weights from offline multi-objective runs. | Decided with the regulator and stakeholders, not by the modelling team. |
| Other uses (water supply, hydropower, environmental flows) after the flood | Represent them through the terminal storage target and minimum flows. | Confirm with the owner and the allocation rules. |
| Computing environment and data latency | Assume a moderate server. Design to finish in ≤ 10 min. | Test on the target infrastructure. |

**General principles:**

1. Separate **hard constraints** (safety, legal) from **soft preferences**, and keep the classification visible and configurable.
2. Wherever information is missing, choose the conservative option, then **quantify the cost of that conservatism** in the replay. This shows which missing data are most worth collecting.
3. Design the code so that new data (gauges, better curves, a revised Q_safe) can be added without changing the method.
4. Record every assumption in a register that the regulator can see.

---

## 6. What would confirm or change the recommendation

**What would confirm it:**

- Closed-loop replay shows clear reductions in exceedance at the control station compared with the rule curve and deterministic MPC, with no extra dam-safety risk.
- False-alarm releases are limited.
- The tool's stated risks are well calibrated.
- Typical solve times are well under 30 min.
- Surrogate errors are small compared with the safety margins.
- Operators accept the recommendations during shadow mode.

**What would change it:**

- **The surrogate routing does not work:** strong nonlinearity, hysteresis, or tributary backwater that the linear kernels cannot capture. I would then switch to an ML or reduced-order emulator inside the MPC, or to a sequential nonlinear MPC on a smaller tree. Both need the 30-min budget checked again.
- **The forecast adds little value:** if, after post-processing, hindcast skill beyond 1–2 days at high flows is poor, a long tree gives little benefit. A simpler **forecast-informed rule** (for example, pre-release triggered when the forecast exceedance probability passes a threshold, tuned offline by policy search) might perform almost as well and be easier to approve.
- **The regulator needs a fixed codified rule:** I would use the MPC offline to **design and tune a forecast-based operating rule** (a decision table or simple decision tree). The online tool would then provide decision support and check that rule, rather than produce optimized releases directly.
- **Tributary uncertainty dominates downstream risk:** the priority then becomes measurement (gauging), and the reservoir's ability to reduce downstream risk may be smaller than expected. This should be communicated to the regulator as a real limitation, not hidden by the optimizer.
