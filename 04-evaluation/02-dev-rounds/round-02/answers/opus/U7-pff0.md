# Real-time release decision tool for a large flood-control reservoir: representation, method, and verification

## Recommendation in brief

Use a **rolling, scenario-tree stochastic model predictive control (MPC)** with a **linear, convex internal model**:

- reservoir water balance on storage, with the level-dependent discharge capacity written as conservative piecewise-linear constraints;
- a linear routing surrogate (Muskingum-type or integrator-delay) for the 120 km reach, fitted to the calibrated routing model;
- the two ungauged tributaries as uncertain lateral inflows, estimated in real time from the residual at the downstream control station and made consistent with each inflow ensemble member.

The solver re-optimizes every 6 hours over the 10-day horizon, and only the next block of releases is put into effect. Dam safety is a hard constraint on every scenario. Downstream exceedance is minimized in strict priority order, not traded against benefits through weights.

The optimizer works inside an explainable wrapper:

1. The objectives are lexicographic and stated in operating language.
2. Each run reports which scenario and which constraint drives the recommendation.
3. Each proposed release is checked offline against the full calibrated routing model for all 51 members.
4. The output is turned into gate steps the operators can actually set, with hold times.
5. A simple, transparent ensemble-risk rule runs beside the MPC every cycle. It serves as a cross-check and as the fallback.

The tool advises within the approved operating manual. It does not replace that manual.

Four alternatives were considered and rejected as the main engine:

- **Deterministic MPC on the ensemble mean:** it hides the tail that matters.
- **Stochastic dynamic programming:** the state dimension explodes once channel routing and lag states are included.
- **Evolutionary multi-objective search at each update:** it is too slow, gives non-reproducible results, and is hard to defend to a regulator.
- **A pure parameterized rule or learned policy:** it is transparent or fast, but less adaptive, or it is a black box.

The parameterized rule is kept as the fallback and benchmark.

## The deciding questions

These three questions would change the design if answered differently. They are treated first and in the most depth.

1. **Where does the controllable lead time run out?** The release travel time to the station is compared with the tributary response time and the 6-hour update cycle.
2. **Can the ensemble support a risk-based decision at the probability levels that matter?** This covers the reliability of the 51 members and of the uncertain tributary inflow.
3. **Can a method that handles 1 to 3 inside 30 minutes still produce recommendations that are physically feasible, can be set at the gates, and can be explained?**

### 1. Travel time and the point of no return

- **Assumption:** the flood wave speed in the reach is 1.5 to 3 m/s. This is typical for a large lowland-to-mid-gradient channel. It must be replaced by the value from the calibrated routing model.
- **Travel time over 120 km:** 120,000 m ÷ (1.5 to 3 m/s) = 40,000 to 80,000 s, or **about 11 to 22 hours**.

This sets up three consequences.

- **Releases made now are already committed for the next half to one day of station flow.** A release cut decided now cannot help the station before about 11 to 22 hours from now.
- **The tributaries enter part-way down the reach, so their water reaches the station sooner than water released from the dam.** If a tributary peak will reach the station within the release travel time, cutting the release is already too late to offset it.
- **The point of no return for a release cut is therefore "tributary peak arrival at the station minus release travel time".** The tool must forecast the tributary contribution at least one release travel time ahead. Today it is ungauged, so this is the weakest link in the system.

Two design choices follow.

- **Model time step:** an hourly step for the first 48 hours, so that a lag of 11 to 22 hours is resolved by at least 11 steps, and a 6-hour step from day 3 to day 10.
- **Decision structure:** the 6-hour update is shorter than the travel time, so each update can still correct releases before they reach the station. The first 6-hour block, however, is committed and must be shared across all scenarios.

### 2. Is the uncertainty usable at the probability levels that matter?

**Member resolution.** With 51 equally likely members, the smallest non-zero exceedance probability that can be counted is 1/51 ≈ 2%. If the acceptable downstream exceedance probability per decision is near or below 2%, member counting cannot resolve it. Three options follow:

- add a calibrated tail, for example post-processing the ensemble with a fitted error distribution by lead time;
- impose the constraint on the worst member plus a margin;
- use both.

The choice depends on a risk level that has not been set (see "Unresolved items" below).

**How finely the hindcasts can resolve things.** Twenty years of hindcasts every 6 hours give about 29,000 forecast issues, but these are not independent.

- **Assumption:** about 3 to 5 flood events per year, so about 60 to 100 independent events, of which only perhaps 10 to 20 exceed downstream safe capacity.
- **Example:** an exceedance rate of 5% estimated from 60 events has a binomial standard error of √(0.05 × 0.95 / 60) ≈ 0.028.
- **Consequence:** the hindcast replay cannot distinguish two policies whose exceedance rates differ by less than about 5 percentage points. Statements about rare outcomes need scaled or synthetic floods (see "Verification plan" below).

**The two tributaries are probably strongly correlated with each other and with the reservoir inflow, because the same storms drive all three.** For two tributary error terms of equal spread σ and correlation ρ, the variance of their sum is 2σ²(1 + ρ).

- **Example:** with ρ = 0.8 this is 3.6σ², against 2σ² if they are treated as independent. The standard deviation of the combined lateral inflow is about √1.8 ≈ 1.34 times larger.
- **Consequence:** a safety margin built on independence would be about 25% too thin. Tributary scenarios must therefore be generated conditional on each reservoir-inflow member, not drawn independently.

### 3. Speed, feasibility, explainability

Only a convex, linear or linearized formulation solved by a deterministic solver (LP or QP) meets all three requirements together. Section C below explains why.

## A. How the reservoir–river system is represented

| Component | Representation in the optimizer | Representation for verification | Why |
|---|---|---|---|
| Reservoir | Storage water balance S(t+1) = S(t) + (I − R)Δt; level from the level–storage curve as a piecewise-linear function | Full curves, with hourly iteration | Storage is linear in the decision variables; level is only needed at thresholds |
| Discharge capacity | R(t) ≤ Q_cap(S(t)), written as piecewise-linear constraints (chords) | Exact level–capacity relationship at the actual head | Capacity varies strongly with level. If Q_cap is concave in storage, the chords lie below the curve, so the constraint is conservative and stays convex. If it is not concave (for example a change from gate control to free overflow), use a small mixed-integer program or successive linearization around the previous trajectory, and test which is fast enough |
| Gates and operation | Release-change (ramping) limits and a minimum hold time per release block; one gate assumed out of service as a conservative capacity case | Release converted to gate openings; the resulting release is checked against the recommendation | Recommendations must be settable |
| River reach (120 km) | Linear routing surrogate (Muskingum or integrator-delay) with sub-reaches, and tributary junctions at their true locations; parameters fitted to the calibrated routing model over the relevant flow range, possibly as two flow-range parameter sets | The calibrated routing model itself | Embedding the full model in repeated optimization is too slow, and the full model has no gradients. A linear surrogate keeps the problem convex. Its error is measured, not assumed |
| Ungauged tributaries | Uncertain lateral inflows at their junctions, one scenario per tree branch, conditioned on the reservoir-inflow member | The same scenarios, plus stress cases | See "Tributary estimation" below |
| Downstream control station | Station flow or stage = routed release + routed lateral inflow; safe threshold with a buffer below the danger level | Same, using the calibrated model's rating | This is the main downstream constraint |
| Forecast | 51 members, reduced to a scenario tree of about 8 to 16 branches with mass-conservative reduction; branch points placed where the hindcasts show that the spread actually resolves | All 51 members | The current decision is shared; later decisions adapt to information as it arrives |

**Tributary estimation (the uncertain input).**

1. **Real-time state.** Combined lateral inflow ≈ observed station flow − routed observed dam release. This assumes the station is gauged and gives a lagged real-time estimate, using a gauge that already exists. A split between the two tributaries by catchment area, or by a rainfall-runoff model if rainfall data exist, is an assumption to be checked.
2. **Forecast.** Rebuild 20 years of this residual series from history. Fit its relationship to the reservoir-inflow observations and hindcasts, for example as a conditional distribution or copula by season and lead time. Each tree branch then carries a reservoir inflow and a consistent lateral inflow.
3. **If a meteorological ensemble for the tributary catchments exists,** driving a simple rainfall-runoff model with it is better. The question does not state that such an ensemble exists, so this is an option, not part of the base design.

**Objectives, in priority order.** The objectives are lexicographic, with no weighted sum across priority levels.

1. Dam safety: the maximum level stays below the safety threshold on every branch, with a margin. This is a hard constraint.
2. Downstream: minimize the volume of station flow above the safe threshold, expected over branches, with a constraint on the worst branch or on the exceedance probability once the acceptable risk is set.
3. Do not create a man-made flood: the release must not raise station flow above what the natural, unregulated flood would have produced.
4. Flood-control zone: outside a flood, empty the zone back to the flood-limited level as soon as downstream limits allow; at the end of the event, reach the target level for refill or the next flood.
5. Smoothness: few release changes, and changes in gate-settable steps.

A strict priority order is easier to explain to a regulator than tuned weights. Each lower objective is optimized only among solutions that are equally good on the higher ones.

## B. Why this method rather than the main alternatives

| Alternative | What it does well | Why not the main engine here |
|---|---|---|
| Deterministic MPC on the ensemble mean or a single forecast | Fast, simple | Averaging the members smooths away exactly the high-flow members that drive flood risk. With a 1 to 10 day horizon and 11 to 22 h travel time, under-preparation is the failure mode. Kept as a benchmark |
| Two-stage stochastic program, full ensemble (shared first action, independent member recourse) | Fast with a linear model, uses all members | Assumes each member's future is known right after the first step, which is too optimistic and under-prepares. Kept as a sensitivity check on the tree |
| Stochastic dynamic programming | Gives a feedback policy, which is attractive for explanation | State = storage + routing lag states + forecast state. Dimensionality makes it infeasible with an explicit 120 km reach |
| Evolutionary / genetic multi-objective search at each update | Handles nonlinearity and gives Pareto fronts | Hundreds of runs per update. A similar setup elsewhere took several hours per event, far beyond 30 minutes. Results are stochastic and not reproducible run to run, which is a problem for a regulator. Constraint handling by penalty is opaque |
| Fixed or parameterized rule (for example an ensemble exceedance fraction against a risk-tolerance curve; release thresholds tuned offline) | Transparent, instant, easy to approve | Fixed structure; cannot exploit the details of a particular event (tributary timing, multi-peak events). **Kept as fallback and cross-check** |
| Analytical rules (optimality conditions for two-stage allocation) | Clear explanation of hedging | Rely on simplifications (Gaussian errors, little or no intermediate inflow) that the ungauged tributaries break |
| Learned policies (for example reinforcement learning) | Fast online | Black box; training data contain few extreme floods; hard to certify |

**Why a tree rather than independent recourse or a single sequence.** A single release sequence common to all members can be infeasible for some members or very conservative. Fully independent per-member releases cannot be carried out, because only one release exists now. A tree shares the decision until the forecast resolves and then adapts, which mirrors what operators actually do.

**Size estimate.**

- Each branch has about 48 hourly steps and 32 six-hour steps, about 80 steps in total.
- With about 16 branches and about 10 variables per step (storage, release, routed flows at sub-reaches, station flow, slack), the problem has on the order of 10⁴ variables.
- A linear or quadratic program of that size typically solves in seconds to tens of seconds. This must be benchmarked on the target hardware.

## C. Verification plan

### C1. Computational efficiency (30-minute budget)

**The budget is allocated to steps and measured.** Run times are targets until measured.

| Step | Target |
|---|---|
| Ingest forecast, observed level and release, station flow; update states | ≤ 5 min |
| Tributary residual estimate, conditioned lateral scenarios, tree reduction | ≤ 3 min |
| Optimization | ≤ 5 min |
| Check of the proposed releases against the full routing model, 51 members, run in parallel | ≤ 7 min |
| Report generation | ≤ 2 min |
| Margin for retries and operator review | ≥ 8 min |

**Tests.**

- **Timing distribution:** replay every 6-hour issue of the 20-year hindcast through the full chain and record the run time. The criterion is the 99th percentile and the maximum, not the mean. The worst cases cluster in large floods, when the mixed-integer branch or successive linearization may be triggered.
- **Size sweep:** sweep tree size (1, 4, 8, 16, 32 branches) and hourly-horizon length. Record closed-loop peak station flow and dam level against run time, and keep the smallest tree beyond which the results stop changing.
- **Fallback guarantee:** if the optimizer fails or runs past a hard time limit (for example 15 minutes), the tool issues the fallback rule's release automatically, logged as such. A recommendation is always available within 30 minutes.

### C2. Physical constraints

**Every recommendation is checked a second time, outside the optimizer, against the exact relationships:**

- The level–capacity relationship at the actual level over the whole release block. Capacity falls as the level falls, so a drawdown slows down. The check uses the capacity at the lowest level reached in the block, not at the starting level.
- Ramping limits for the channel, and drawdown-rate limits for the reservoir banks and dam slopes. These are to be confirmed.
- The full routing model's station flow for all 51 members, compared with the surrogate's prediction.

**Surrogate fidelity.** Over the hindcast floods, measure the error of the linear surrogate against the calibrated routing model at the station: peak flow, peak timing, and volume above the threshold. Add the 95th-percentile surrogate error to the station-threshold margin. If the peak error exceeds an agreed tolerance, two remedies apply in order:

1. use flow-range-dependent parameter sets;
2. if that is not enough, iterate: optimize, check with the full model, tighten the margin, and re-optimize. One extra loop fits the time budget.

**Mass-balance plausibility of each recommendation.**

- The volume needed to cut the station peak by ΔQ for T hours is ΔQ·T. Example: 1,000 m³/s for 24 h = 86.4 × 10⁶ m³.
- Compare this with the free flood-control storage. If the volume exceeds the storage, the recommendation cannot deliver the stated benefit.
- Apply the same check to pre-releases: (release − inflow) × available time must fit within the lead time and the capacity at the falling level, and must be refillable under a low-side inflow forecast.

**Design-flood check.** When the tool's plans leave the reservoir above the flood-limited level at any time, route the design flood and the check flood from that level, including two floods in close succession. This shows that dam safety is not eroded.

**Equipment cases.** Re-run the constraint checks with one gate out of service and with level-measurement error, for example ± a few tenths of a metre, to be set from the instrument specification.

### C3. Decision reliability

**Forecast verification first.**

- On the 20-year hindcasts, by lead time, season, and flow stratum: rank histograms, CRPS, and Brier scores for exceedance of the station-relevant inflow thresholds.
- Check bias and under-dispersion. If the ensemble is under-dispersed, add a post-processor and verify it out of sample.
- **Confirm that the hindcasts come from the same forecast system version, ensemble size, and issue times as the operational feed.** If they do not, the reliability statistics do not transfer.

**Tributary-scenario faithfulness.**

- Coverage of the reconstructed residual series by the conditional lateral scenarios. For example, the 90% band should hold about 90% of observations, checked separately for high flows.
- The correlation with reservoir inflow is preserved.

**Closed-loop hindcast replay.** Over 20 years, every 6 hours, the tool's own releases feed back into the state. Only the first block is applied, then the system is advanced with observed inflows and the reconstructed lateral flows.

The tool is compared under identical starting levels and inflows with five benchmarks:

1. the current operating rule as encoded from the manual;
2. a no-forecast rule;
3. deterministic MPC on the ensemble mean;
4. the simple ensemble-risk rule;
5. perfect-foresight MPC, as an upper bound that cannot be deployed.

The metrics are:

- maximum dam level and its margin to the safety threshold;
- hours and volume above the station threshold;
- man-made exceedances (release above the natural-flow counterfactual);
- end-of-event level and refill;
- number of release changes;
- **stability between successive updates**: how often and how much the recommended current release flips from one 6-hour run to the next. This matters for operator trust.

**Out of sample.** Any tuned items, such as the tree size, margins, and the fallback rule's thresholds, are fitted with leave-one-year-out cross-validation. The test events must not have been used for tuning.

**Stress.**

- The largest historical events scaled to rarer magnitudes, with their forecasts.
- Tributary flows at the upper scenario bound arriving at the worst timing, just inside the release travel time.
- Forecast failure cases, where a flood arrives earlier or larger than every member.

**Honest resolution.** Report the uncertainty of each difference, using the binomial standard error from the number of independent events. Do not claim a reduction in exceedance that the event count cannot resolve. Explain gains by mechanism, using trajectory plots of representative floods, not only aggregate numbers.

### C4. Practical implementability and explainability

**What a recommendation contains.**

- The release, or gate setting, for the next 6-hour block.
- The planned envelope for the next 24 to 48 hours.
- The 51-member fan of dam level and station flow under that plan.
- The binding constraint and binding scenario, in words. Example: "Release held at X because member group B would bring the station above the safe flow at hour 18 once tributary inflow arrives."
- The fallback rule's release for comparison, and the reason for any difference.
- The point of no return for the next change: the latest update at which a cut or increase still affects the station before the forecast peak.
- The triggers that would change the action at the next update.

**Settable actions.** Releases are converted to discrete gate steps, with minimum hold times, and to the existing release-scheduling and notification format.

**Mandatory checks before deployment.**

- The tool cannot recommend anything outside the operating manual's limits. Where the manual itself is the binding constraint, the tool reports this instead of proposing a deviation.
- A complete audit log records the inputs, forecast version, tree, solver status, the recommendation, and the operator's action.
- Solver runs are deterministic, so the same inputs give the same output and any decision can be reproduced for the regulator.

**Adoption path.**

1. Agree the acceptance criteria with the dam-safety authority and the operating agency before the trial: the dam-safety margin, the station exceedance criterion, the maximum run time, and the update-stability limit.
2. Run in shadow mode beside the current rule for at least one flood season. Operators decide as now. The tool's recommendations are logged and compared after each event.
3. Then use the tool as decision support within the current manual.
4. Only later, if the evidence supports it, revise the manual through the normal approval procedure.

The current rule remains the legal basis throughout.

**Reversion triggers.** These are written down in advance, with a named person who decides:

- the forecast is missing, late, or diverging from observed inflow beyond a set tolerance;
- the tributary residual is implausible, for example negative beyond the gauge's measurement error, which signals a gauge or rating problem at the station;
- the optimizer fails or times out;
- the equipment state differs from the model.

On any of these, the tool falls back to the fallback rule or the current manual and logs the reversion.

**Warnings and people.** Downstream authorities and emergency services are notified of planned release increases, including pre-releases, within the release travel time. Operators are trained on reading the outputs. The tool and its parameters are under version control. Each event has an after-event review.

## D. Unresolved items and how the preliminary design handles them

| Unresolved item | How the preliminary design handles it | What would confirm it or change the design |
|---|---|---|
| Wave speed and travel time in the reach | Take them from the calibrated model; test 11 h and 22 h as bounds | If the travel time exceeds about 24 h, hourly resolution beyond 48 h is needed and the shared first-stage period lengthens |
| Concavity of discharge capacity in storage, gate count, and capacity with one gate out | Conservative chords; one-gate-out case as default; mixed-integer fallback coded but switched on only if needed | Inspection of the curves; the dam owner's equipment data |
| Safe flow and danger level at the station; ramping and drawdown limits | Configurable parameters with conservative placeholder values, flagged "to be confirmed" in every output; sensitivity runs at ± a range | Values from the river authority and the dam-safety documentation. Tighter limits shrink the feasible set and may make the tree size or margins binding |
| Acceptable risk (probability of station exceedance, dam-safety margin) | Dam safety enforced as a hard constraint on all branches. Downstream handled as minimum exceedance volume plus a worst-branch report until the regulator sets a probability | A set probability at or below about 2% requires tail post-processing of the ensemble, because member counting cannot resolve it |
| Tributary flows | Residual reconstruction plus conditional scenarios; a margin covering correlated error; a stress case at the upper bound | Coverage tests. If coverage is poor, install temporary gauges on the tributaries. This is likely the cheapest improvement in decision reliability, because it attacks the input that limits the point of no return |
| Whether the hindcasts match the operational forecast version | Verify the version before using any reliability statistic | If they do not match, re-run hindcasts or widen the margins until operational verification data accumulate |
| Authority to pre-release or to hold above the flood-limited level | The tool stays within the current manual; any flexibility beyond it is reported as "would require approval" | The regulator's position; the outcome of the shadow trial |
| Surrogate routing error at extreme flows beyond the calibration range | Measured error margin; full-model check every cycle | If the error grows sharply at high flow, use flow-range parameter sets or the iteration described in C2 |

## E. Summary of the provisional judgment

- **Recommended choice:** tree-based stochastic MPC with a linear surrogate model, a conservative capacity representation, tributary scenarios conditioned on each inflow member, lexicographic objectives, and a full-model check plus a transparent fallback rule every cycle.
- **Why:**
  - It is the only option among those considered that handles the forecast uncertainty and the 11 to 22 hour committed-release lag together.
  - It respects a strongly level-dependent capacity.
  - It solves in minutes.
  - It produces reproducible, explainable, gate-settable advice.
- **Key assumptions:**
  - The capacity relationship can be represented conservatively in convex form.
  - A linear routing surrogate stays within an agreed error of the calibrated model.
  - The downstream station is gauged, so the tributary residual can be reconstructed.
- **What would change the choice:**
  - Closed-loop replay showing no material gain over the simple ensemble-risk rule beyond what the event count can resolve. The simpler rule would then be easier to approve and should be adopted, with the MPC kept as an analysis tool.
  - Run times that cannot be held under the budget in large floods.
  - Surrogate errors that cannot be bounded at high flows.
