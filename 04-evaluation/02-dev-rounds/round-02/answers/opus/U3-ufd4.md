# Review of the prerelease-rule evaluation

## Bottom line (provisional)

I would not recommend adopting the new rule on the basis of this analysis. The rule may well be beneficial, but the evidence as presented does not show it. The "18% lower maximum outflow with 95% confidence" result depends on an error model that is probably too optimistic for exactly the conditions that matter (large floods). It covers one scenario and one metric. And the "95% confidence" most likely describes the spread inside the firm's own assumptions, not real-world confidence. My expectation is that a corrected analysis would show a smaller and more uncertain benefit for the 100-year event. It might also show new risks: higher peak storage when the forecast under-predicts, and lost storage or downstream harm when the forecast over-predicts. Whether the rule is still worth adopting after that is an open question that the additional work below should answer.

Assumptions I am making, because the question does not specify them:
- The prerelease rule uses the 3-day forecast to release water before the flood arrives, so it creates flood-storage space in advance.
- The "current rule" uses either no forecast or a simpler trigger.
- "Maximum outflow" means the peak release from the dam.
- The 12-year forecast archive comes from an operational (or reforecast) deterministic forecast system.
- The 100-year design flood is a synthetic design hydrograph, not an observed event.

---

## 1. Problems with the forecast-error model

### 1.1 Pooling all errors into one normal distribution
- **Heteroscedasticity.** Forecast errors almost always grow with flow magnitude, roughly in proportion to it, and often by more. Pooling 12 years of mostly ordinary flows produces an error variance dominated by small, low-error days. Applied to a 100-year flood, which lies at or beyond the top of the calibration range, this understates the absolute error at the flood peak, possibly by a large factor.
- **Seasonality.** Flood-season errors (convective storms, snowmelt, typhoons) usually differ in size and sign from dry-season errors. A pooled fit mixes regimes that should not be mixed.
- **Lead-time dependence.** Errors at day 3 are normally much larger than at day 1. One distribution for all lead times gives day 1 too much error and day 3 too little. Day 3 is what drives how much water gets prereleased, so its skill is what matters for this rule.
- **Distribution shape.** Streamflow forecast errors are typically skewed and heavy-tailed. Large floods are often under-forecast because rainfall forecasts miss extremes. A symmetric normal with zero mean (or a mean fitted to pooled data) misses this systematic peak bias and gives near-zero probability to the large misses that cause failures.
- **Nonstationarity of the forecast system.** Over 12 years the forecast model, its inputs and the gauge network have probably changed. If skill improved, the early years may not represent current skill, and vice versa. The fit treats all years as one sample.

### 1.2 Sampling each day's error independently
This is probably the most consequential flaw.
- **Autocorrelation within a forecast.** Real errors for day 1, 2 and 3 of one forecast are strongly positively correlated: if the rainfall is under-predicted, all three days are under-predicted together. Independent sampling makes errors partly cancel. The variance of the 3-day forecast *volume*, which is what a prerelease decision uses, is then badly understated. For a sum of three errors with correlation ρ, the variance is larger than the independent case by a factor of up to (1 + 2·2ρ/3 + …), roughly 3x at ρ near 1. A volume-error standard deviation that should be about √3 times larger looks much smaller.
- **Correlation between successive forecasts.** Forecasts issued on consecutive days for the same target day are also correlated. A real operator may see the same bias persist for several issuances. Independent sampling instead gives a "self-correcting" forecast stream, which flatters any forecast-based rule.
- **Timing and shape errors.** Real forecasts often get the peak *timing* or hydrograph *shape* wrong, not just the daily magnitude. An additive daily error cannot reproduce a peak forecast one day late, which is a classic failure mode for prerelease: water released too late, or the reservoir refilling at the wrong time.

**Net effect.** The synthetic forecasts are probably more accurate and better behaved than real forecasts during a 100-year flood. This biases the result in favour of the new rule.

### 1.3 Representativeness of the 12-year record for extremes
Twelve years probably contains few or no events near the 100-year magnitude. Using errors from that record for the 100-year event is an extrapolation, and the analysis should state it as one. Extreme events are often where forecast skill is lowest.

---

## 2. Problems with the scenario design

- **One design flood, one hydrograph.** The result is for a single 100-year hydrograph. The benefit of prerelease depends heavily on hydrograph shape (peaky vs. long-volume), duration, multi-peak sequences, and the volume–peak combination. A "100-year" event can be defined by peak, by 3-day volume, or by longer-duration volume, and the definitions give different hydrographs. I would want several plausible 100-year hydrographs (different shapes, durations, historical-event-scaled patterns), not one.
- **Initial conditions.** The starting reservoir level strongly controls both rules' performance. Was it set at a fixed flood-control level, or sampled from realistic seasonal levels? If it was fixed at a favourable level, the result may not generalize.
- **Only the 100-year event is reported.** Adoption needs performance across the full frequency range:
  - *Frequent and moderate floods* (2–20-year). Prerelease can cause *harm* here: unnecessary releases, downstream nuisance flooding, loss of water-supply or hydropower storage when the flood under-materializes.
  - *Above-design floods* (500-, 1,000-year, PMF, or the dam-safety design flood). Peak storage and freeboard are what matter for these, and a rule that depletes or mis-times storage could change dam-safety margins.
  - *False alarms.* Forecast floods that do not occur: how much storage is lost, and can it be refilled?
  - *Missed events.* Floods that were not forecast, where the rule gives no benefit and may behave worse than the current rule.
- **Probability weighting.** A rule that helps at 100-year but slightly hurts at 10-year may be worse overall in expected-damage terms, because frequent events carry most of the expected annual damage.

---

## 3. Problems with the metric and the comparison

- **Single metric.** Peak outflow alone is not enough. I would also want:
  - maximum reservoir water level, minimum freeboard, and the probability of reaching spillway or emergency levels (dam safety);
  - peak flow and stage at downstream control points (after routing and tributary inflows), duration above channel capacity or damage thresholds, and expected flood damage;
  - prerelease rates against downstream channel capacity and rate-of-change (ramping) limits, plus whether the prerelease itself causes flooding or creates hazards for people downstream;
  - end-of-event storage and refill probability; water-supply reliability and hydropower and environmental-flow impacts over the following months.
- **Which statistic is the 18%?** Is it a reduction in the mean, the median, a deterministic run, or each of the 5,000 paired runs? Averages hide tails. I would want the full distribution of outcomes: the worst 5% and 1% of cases, and the probability that the new rule produces a *higher* peak outflow or *higher* peak water level than the current rule.
- **Fair comparison.** Were both rules run on the same synthetic forecasts and inflows (common random numbers)? Was the current rule modelled the way the reservoir is actually operated, including operator discretion and existing forecast use, or as an idealized rule that is easy to beat? Was the new rule tuned on the same data used to evaluate it (in-sample optimism)?
- **Operational realism.** Does the simulation respect gate capacities and outlet rating curves, gate operation constraints, decision intervals (forecasts arrive at a fixed time; actions lag), communication and warning lead times, and legal or permit release limits?

---

## 4. What "95% confidence" actually means here

The claim is ambiguous and almost certainly overstated.
- It most likely means "in about 95% of the 5,000 synthetic runs the new rule's peak outflow was lower", or that a Monte Carlo confidence interval on the mean reduction excludes zero. With 5,000 samples the Monte Carlo *sampling* uncertainty is tiny, so this mainly shows the simulation was long enough. It does not show the conclusion is correct.
- That confidence is **conditional on** the assumed error model (pooled, normal, independent), the single design hydrograph, the initial condition, and the reservoir model. None of these structural (epistemic) uncertainties is in the 95%. Errors in these assumptions probably dominate the true uncertainty, and as argued above they lean toward overstating the benefit.
- It is also unclear whether the confidence is about the *sign* of the effect (new rule is better) or the *size* (18%). These are very different claims.
- The design flood's own uncertainty (the 100-year estimate from a finite record) is not carried through.

I would ask the firm to restate the claim precisely and to separate (a) Monte Carlo sampling uncertainty, (b) forecast-error-model uncertainty, (c) design-flood and hydrograph uncertainty, and (d) model and parameter uncertainty.

---

## 5. Additional analyses, verifications and evidence I would require

### A. Re-do the forecast-error model
1. Characterize errors by **lead time, season and flow magnitude**. Fit a heteroscedastic model (e.g., errors proportional to flow, or modelled in log or normal-quantile-transformed space), or a conditional distribution. Test for bias at high flows.
2. Model **dependence**: cross-lead-time correlation within each forecast and persistence across successive issuances. Use, for example, a multivariate or AR error model in transformed space, or block-resample whole observed forecast-error trajectories rather than independent daily draws.
3. Include **timing and shape errors** (e.g., peak shift), or use historical forecast trajectories scaled to design magnitudes.
4. Check for skill changes over the 12 years, and use the error characteristics of the *current* forecast system.
5. Validate the error model: compare simulated and observed error statistics (variance by lead time, autocorrelation, 3-day volume error, tail quantiles, error during the largest observed events).
6. If ensemble forecasts are available, consider using them directly. Their spread carries the right dependence structure.

### B. Hindcast on real events
7. Run both rules on the **actual 12-year forecast archive with actual inflows** (a real-forecast hindcast). This is the most direct evidence and uses no synthetic error model. Report every event in which the rule triggered: benefits, false alarms, misses and storage losses.
8. Look closely at the largest observed floods, and at any regional historical events with available forecasts, to see how the rule behaves under real large-event forecast failures.

### C. Broaden the scenarios
9. Multiple design hydrographs per return period (shape, duration, multi-peak), and a range of return periods from about 2-year to the dam-safety design flood or PMF.
10. Realistic initial-storage distributions (seasonal), not a single starting level.
11. Propagate design-flood uncertainty, e.g., the confidence band on the 100-year flood estimate.
12. Stress tests: a forecast that badly under-predicts; peak timing off by one day or more; a forecast outage; gate failure or partial outlet capacity; a second flood arriving while the reservoir is still drawn down or refilling; and consideration of climate-change-adjusted floods.

### D. Broaden the metrics and the decision criteria
13. Report peak water level and freeboard, downstream peak flows and stages (with routing), damage or exceedance-duration measures, prerelease-induced downstream impacts, and refill and water-supply reliability.
14. Report full distributions and tails, the probability that the new rule is worse, and expected annual damage across all events, not just the mean reduction at one return period.
15. Sensitivity and robustness analysis: how the result changes as error variance, correlation and bias vary. Identify the error level at which the new rule stops beating the current rule (a break-even analysis). If realistic errors sit near that threshold, the benefit is fragile.

### E. Verify the model and the process
16. Verify the reservoir simulation model (storage–elevation curve, outlet ratings, operating constraints) against observed operations.
17. Confirm that the current rule is represented the way it is actually operated, and that the new rule's parameters were not tuned on the evaluation set. Use split-sample or out-of-sample evaluation.
18. Independent technical review of the analysis, with code and data provided.
19. Institutional and legal checks: compatibility with dam-safety regulations, downstream release limits and water-rights or supply commitments, plus coordination with downstream authorities and warning systems. Prerelease affects downstream communities and needs clear communication protocols.

### F. Adoption pathway, if the evidence holds up
20. If the corrected analyses still show a robust benefit with acceptable dam-safety and downstream-risk outcomes, I would recommend **staged or conditional adoption**:
    - clear trigger thresholds tied to forecast confidence (e.g., ensemble probability);
    - conservative caps on prerelease volume and rate;
    - a refill or abort protocol;
    - operator override rules;
    - a trial period with monitoring and logging of every activation;
    - a scheduled re-evaluation as forecast skill and the observed record evolve.
    The emergency action plan and operating manual would need updating accordingly.

---

## What would confirm or change my judgment

- **Confirm benefit:** a real-forecast hindcast showing consistent peak reductions without harmful false-alarm releases; a heteroscedastic, autocorrelated error model reproducing observed error statistics and still showing a clear reduction (even if smaller than 18%); no increase in peak water level or dam-safety risk in the tails; acceptable performance at frequent floods and refill reliability.
- **Change toward rejection or redesign:** the benefit vanishes or reverses once errors are realistic; a meaningful probability of higher peak storage or reduced freeboard; frequent damaging or unnecessary prereleases; refill failures that harm water supply; or a break-even error level close to the actual forecast error at high flows.
