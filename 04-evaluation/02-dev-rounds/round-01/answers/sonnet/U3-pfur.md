# Review of the consulting firm's prerelease-rule evaluation

## Bottom line (provisional)

I would not recommend adoption on the basis of this analysis. The finding that the new rule lowers maximum outflow by 18% in the 100-year design flood is a model-conditional result. It rests on an error model that is probably too benign for exactly the situation that matters (a rare, large flood), and it covers only one outcome measure and one flood. The phrase "95% confidence" is not a statement about reality.

The 18% may well be roughly right. The package gives no way to tell, because the evidence cannot separate a real rule benefit from an artifact of the synthetic forecasts. My position would change if the analyses below show that (a) the benefit survives realistic, dependent, flow-dependent and heavier-tailed errors, (b) reservoir safety (maximum level, spill) and downstream safety are not worsened in the failure cases, (c) the rule can physically and institutionally be executed within the 3-day lead time, and (d) a backtest on real historical forecasts and events agrees.

Assumptions I make, since the question does not say:
- The new rule uses the forecast to start prerelease early.
- "Maximum outflow" is the peak release or peak downstream flow in a simulation of a single design hydrograph.
- The 5,000 runs differ only in the sampled forecast errors.
- The "current rule" is a rule that either ignores forecasts or uses them in a simple way.
- The 600 million m³ is the total storage, so the flood-control pool is only a part of it, and its size is unknown.

I flag each of these as something to confirm with the firm.

## 1. What "95% confidence" can and cannot mean here

The firm drew 5,000 random forecasts from a fitted error model. That gives sampling precision of a Monte Carlo estimate, and conditional on the model being right, nothing more. It does not give confidence about the real reservoir, because:

- Model uncertainty is not in the interval. The error distribution was fitted on 12 years, and its form, parameters, dependence and applicability to a 100-year flood are all uncertain. None of that is represented.
- The design flood is a single assumed scenario. Real 100-year floods differ in volume, peak, shape, timing, number of peaks and antecedent state. The 5,000 runs vary only the forecast error, so the spread covers only part of the uncertainty.
- The statistic is undefined. It is not stated whether 18% is the mean, the median or a percentile of the peak outflow difference. It is also not stated whether the 95% refers to a confidence interval on that mean, to a share of runs in which the new rule is better, or to something else.
- More runs shrink the Monte Carlo interval without limit, so a "95%" figure can be made arbitrarily tight and says nothing about how right the model is.

What I would ask for:
- The full distribution of outcomes under each rule, not only the mean.
- The paired differences, with the same sampled error series fed to both rules.
- The share of runs in which the new rule is worse. The key operational question is the tail: in the runs with the worst forecast failures, is the new rule worse than the current rule, and by how much?
- Convergence evidence for the number of runs, using different seeds and a bootstrap interval.

## 2. Problems with the forecast-error model

**Pooling all seasons, flows and lead times.**
- Forecast error in this field generally depends on lead time (it grows with it), on flow magnitude (floods differ from low flows) and on season. Papers have reported error structure that is biased, non-Gaussian, heavy-tailed, seasonally nonstationary, and different between low flow and flood regimes. Some used a stationary Gaussian only in the high-flow regime because it did not hold elsewhere.
- Pooling mixes a large number of small, low-flow days with a few flood days. Whether this makes the pooled spread too small or too large for a flood depends on whether errors are relative or absolute. The firm does not say. If errors are relative, low-flow days can inflate the spread. If absolute, flood-day errors are diluted. I do not assume either direction, but the pooled fit is not shown to represent the flood regime in which the 18% claim is made.
- A single normal distribution cannot be right at all lead times. Within a 3-day forecast, day 3 is less accurate than day 1, and the benefit of prerelease depends on exactly those later days.
- A normal distribution of relative error also allows impossible values (a forecast below zero) and has thin tails. Flood-peak forecasts commonly show systematic underforecast of the largest events and heavy tails. A thin-tailed model understates the chance and size of a large miss, which is where a forecast-based prerelease rule is most vulnerable.

**Extrapolation to a 100-year flood.** Twelve years of data contain perhaps a few moderate floods and no 100-year event. The error behavior at that magnitude is not observed, only assumed. Papers that needed this either scaled floods up while explicitly keeping the error attributes as an assumption, or tested several error levels, and reported the extrapolation as a limit.

**Independence across days.**
- The firm sampled each day's error independently. Real forecast errors are strongly correlated across consecutive days and across lead times of the same forecast, because they arise from a shared cause (a misplaced storm, a bias in rainfall forecast, a timing shift). An entire event is typically over- or under-forecast together.
- Independent daily errors partly cancel when the hydrograph is built, so the simulated forecasts are smoother and more reliable than real ones. This understates the probability and severity of persistent whole-event bias, such as a prerelease that is too small or too large for the whole event. It biases results in favor of any rule that depends on forecast accuracy.
- Dependence across successive forecast issues (forecast updates), and between forecast error and other uncertain quantities, also matters.
- It is also unclear what "daily forecast error" means: the error of the 1-day, 2-day and 3-day forecasts issued on a given day are jointly distributed, and a rule may use all three. A rolling set of updated forecasts, with its own error evolution, is not what independent daily sampling produces.

**Faithfulness of the synthetic forecasts.** No check is reported that the 5,000 synthetic forecasts reproduce the historical error statistics, coverage, autocorrelation, flow-dependence or extreme-event behavior. This needs to be demonstrated, including for the largest historical events separately.

## 3. Problems with the design-flood scenario

- How was the 100-year flood built? From frequency analysis of peak or volume, scaling of a historical event, or a synthetic hydrograph? The reservoir response depends on the 1-, 3-, 5- and 7-day volumes and on the hydrograph shape, not only on peak flow. A rule that helps for one shape may not for another (single peak versus multi-peak, fast versus slow rise, a pre-flood small peak that triggers early prerelease).
- Each design flood is probably one fixed hydrograph. Hydrograph-shape and volume uncertainty can be as important as forecast error. Papers that compared sources found shape to dominate in some cases.
- The uncertainty of the 100-year estimate itself, and nonstationarity of flood regime, are not mentioned.
- Other uncertainties are not in the model: initial reservoir level at the start of the event, outlet or discharge capacity, storage-elevation curve, and whether other floods follow soon after.
- The firm reports only the 100-year flood. The decision cannot be made on one return period. Behavior needs to be examined across a range of return periods, from frequent events (where early prerelease may waste water and lose refill) to rarer than the 100-year (a check or extreme event, where dam safety, not outflow, governs).

## 4. Problems with the outcome measure and the comparison

**"Maximum outflow" alone is not the safety measure.**
- Lower peak outflow can be achieved by holding more water, which raises the maximum reservoir level. The outcome that determines dam safety is the maximum level (and the required flood pool, or overtopping margin), not only the release peak. An 18% lower outflow peak is not evidence of safety unless the maximum level stays within limits across the error distribution.
- Downstream consequences are not stated. What matters is whether release exceeds the safe channel capacity, the duration above thresholds, and whether the early prerelease itself causes downstream flooding or conflicts with other control points and local inflow.
- A single exceedance probability or a mean is insufficient. I would ask for the tail (the worst few percent of runs, expected shortfall), the duration, and the maximum level, together with probability of exceeding each safety threshold.
- The cost side is missing: water lost to false alarms, failed refill after prerelease, hydropower, supply and navigation. If the new rule lowers outflow in the design flood but wastes water in smaller floods and fails to refill, the net benefit is not shown. Safety should be treated as a constraint met first, with benefits judged after.

**The baseline and the comparison.**
- Confirm that the current rule is encoded as the real operating rule and run under identical conditions: same hydrographs, same initial state, same error sequences (paired), same release and ramping constraints, same outlet capacity.
- Show the information bounds. Compare the new rule against no-forecast operation, against perfect-forecast operation, and against the current rule with the same forecast. The gap between no-forecast and perfect forecast shows the most that forecast use can give, and how much of the 18% is captured by the forecast at all. Without that, it is unclear whether the gain comes from using forecasts, from simply releasing earlier, or from a more conservative threshold that any rule could adopt.
- Do the same comparison for a rule that prereleases by a fixed margin without using forecasts, to isolate the contribution of forecast information.
- Check whether the benefit is explained by a mechanism (for instance, release spread before the peak and earlier start), rather than being only a number. If the mechanism depends on the forecast being right, it is exactly the part that needs stress testing.

## 5. Evidence I would require before recommending adoption

Listed roughly in order of importance.

1. **Backtest on real data.** Run both rules over the actual historical events and the actual forecasts available in the 12 years, not only synthetic ones. Compare simulated levels and flows to the recorded operation, and check the simulator against history. Do this with held-out events (for example leave-one-year-out), and examine the largest floods separately. Include events where the forecast failed.

2. **Rebuild the error model, then test whether the conclusion survives it.**
   - Stratify by season, flow regime (or event size) and lead time. Where data are sparse, say so and show alternative models: heteroscedastic (spread growing with flow), heavy-tailed or skewed distributions, a mixture, and a model including bias for large events.
   - Preserve dependence across lead times and consecutive days (for example by copula, vector autoregression, or by resampling whole historical error trajectories).
   - Test goodness of fit and show coverage, autocorrelation and extreme-event behavior of the synthetic forecasts against the 12 years.
   - Check whether the data are enough to support any of this. If not, run the stress tests below and present results as a range.

3. **Sensitivity and stress tests on forecast quality.** Vary error magnitude, bias (systematic underforecast of peaks), heavy tails, correlation across days, lead time, and number of runs and seeds. Find the error level at which the benefit disappears or reverses, the "breakeven" forecast accuracy. Then ask whether that level is within what the real forecasts show, especially in large floods. Include a deliberate forecast-failure case (a large miss early in the event) and a false-alarm case.

4. **Safety outcomes in addition to outflow.** Maximum reservoir level, required flood pool, probability of exceeding each critical level, downstream peak and exceedance duration, and tail measures, for both rules, under the full set of error models. Safety should be non-compensable: the new rule should be no worse than the current rule on dam safety in failure cases before benefits count.

5. **Wider flood coverage.** Several return periods (smaller and larger than 100-year), multiple hydrograph shapes and volumes, uncertain initial level, successive floods, and uncertain discharge capacity and storage curve. State which uncertainties are excluded and why.

6. **Feasibility and implementability.**
   - Can prerelease finish within the 3-day lead time given outlet capacity, release-change limits and ramping, with the reservoir at its realistic starting level?
   - Is there enough remaining storage to absorb the flood if the forecast is wrong, and can the released water be refilled afterward?
   - Do travel time, channel storage and local uncontrolled inflow downstream turn a locally feasible release into a downstream problem?
   - Is it permitted by the operating manual, regulation and the authority responsible; can operators execute it with available tools, data and computing time?
   - What is the rule's fallback when the forecast is wrong or unavailable, for example reverting to a measurement-based rule, or correcting gradually?

7. **Trade-off evidence.** Frequent-flood behavior, water lost, refill reliability, hydropower and supply effects, to show the rule does not buy a design-flood benefit at an unacceptable operational cost. If the choice is between several rule versions, test the ranking's stability against weights and assumptions.

8. **Independent verification of the analysis itself.** Re-run the simulation with an independent implementation or a second method, and share code, parameters and seeds. Confirm simulation settings (time step, routing) and that the 5,000-run result is stable.

9. **Adoption process, if evidence is favorable.** Review with the operating agency and stakeholders, a staged or pilot approach (for example a trial prerelease limited to forecasts of high reliability, with observation and post-event review), and a plan to revise after real events.

## 6. How I would present the finding to the owner

- The 18% figure is conditional: it holds if future forecast errors for a 100-year flood behave like the pooled, independent, normal errors the firm assumed. That assumption is untested for large floods and is likely favorable to a forecast-dependent rule.
- "95% confidence" should be dropped or replaced by a clear statement of what is being estimated and which uncertainty it covers (Monte Carlo sampling only).
- Adoption is more defensible as a staged decision: first the backtest and stress tests above (modest effort, using existing data); if those support the rule, a limited pilot with a safe fallback. If the breakeven forecast accuracy turns out to be close to real forecast skill in large floods, the rule should not be adopted in this form, or should be limited to cases when forecast reliability is verified.

## What would change my view

- Supports adoption: a backtest on real events agreeing with the simulation; the benefit persisting (with maximum level and downstream safety no worse) under dependent, flow-dependent, heavy-tailed errors and the forecast-failure cases; breakeven forecast accuracy well below observed large-flood forecast skill; the rule shown feasible within the lead time and refill-safe; acceptance by the operating authority.
- Against adoption: the benefit disappearing or reversing under persistent whole-event bias or heavy tails; higher maximum level or worse tail in forecast-failure runs; the gain explained by a more conservative threshold rather than by forecast use; infeasible prerelease within the lead time; losses in frequent floods or refill.
