# Review of the proposed prerelease rule (600 million m³ reservoir)

## Bottom line

**Provisional recommendation: do not adopt the new rule on this evidence.** That does not mean the rule is bad. It may well be better than the current rule. The problem is that the analysis cannot show it, and the "18% lower maximum outflow with 95% confidence" claim is much stronger than the method allows.

Three weaknesses carry most of the weight:

1. **The forecast-error model is probably too optimistic for exactly the case that matters.** The errors were pooled into one normal distribution and sampled independently day by day. A prerelease rule depends on the forecast 3-day flood volume and on the timing of the peak. Independent daily errors largely cancel over three days, so the model understates volume and timing errors. A pooled fit also understates how large errors get in large floods and at longer lead times.
2. **The "95% confidence" covers only Monte Carlo sampling noise inside an assumed error model.** It does not cover whether that model is right, the uncertainty in its parameters, the shape of the design flood, the starting water level, or how the reservoir simulator is built. With 5,000 samples, almost any mean difference looks "significant."
3. **One outcome for one flood is not enough to adopt an operating rule.** A lower peak outflow in the 100-year flood says nothing about the maximum reservoir level (dam safety), about flows the prerelease itself sends downstream, about failing to refill after a false alarm, or about how the rule behaves in smaller and larger floods.

The rule could still be adopted, through a staged and reversible process, once the evidence below is in place.

## 1. Problems with the forecast-error model

**Pooling across season, flow size and lead time**
- Forecast errors almost always grow with lead time. The day-3 error is typically several times the day-1 error. A single pooled distribution gives day 3 too little spread and day 1 too much. Prerelease decisions lean most on the longer leads, which are the ones understated.
- Errors usually grow with flow, so the spread scales roughly with the flow itself. A pooled sample is dominated by ordinary, low-to-moderate flow days. Its spread is therefore too small for the flows of a 100-year flood, especially if the errors were added as absolute values in m³/s. If the errors were relative rather than absolute, the pooled spread may still be wrong for high flows. Either way, the high-flow subset needs to be checked separately.
- Error behaviour can differ by season (different storm types, snowmelt against rain). One distribution for all seasons hides this.
- **Normality, zero mean and symmetry are assumptions, not findings.** Flood forecasts are often biased, typically underforecasting peaks on the rising limb. Their errors are often skewed and heavy-tailed. A normal fit to pooled data mostly reflects the many small errors of normal days and says little about the tails, which decide whether prerelease is enough.

**Independence between days**
- Real errors are strongly correlated. If a storm is missed or underforecast, the error persists across lead times and across successive forecasts. Sampling each day independently:
  - makes errors cancel over the 3-day window, so the forecast flood volume looks more reliable than it is;
  - almost never produces the dangerous cases: a sustained underforecast (prerelease too small or too late) or a sustained overforecast (water released for nothing);
  - produces forecasts that are inconsistent from one issue to the next, which a real forecasting system does not;
  - leaves out errors in peak timing, which matter for when prerelease must start.
- This bias most likely favours the new rule, because a forecast-using rule looks best when the forecasts look reliable. I can't be certain of the direction without redoing the analysis, but the likely direction is optimistic.

**Extrapolating from 12 years**
- Twelve years of forecasts will rarely include a flood anywhere near the 100-year event. The error model is fitted on events far smaller than the one it is applied to. Forecast skill in extreme events is often worse, and different in kind, from skill in ordinary floods.
- Over 12 years the forecasting system has probably changed (model upgrades, new data, new procedures). Errors from older versions may not describe the forecasts the rule will actually use. The reverse also holds: if the current system is better, the old errors may be too pessimistic.
- The fitted parameters themselves are uncertain, given the short record and serially correlated data. This uncertainty does not appear anywhere in the "95% confidence."

**Other uncertainties left out**
- Starting water level when the flood arrives, design-flood hydrograph shape (single or multiple peaks, peak timing, volume against peak), the storage–level curve, real outlet capacity, and local inflow between the dam and the downstream control points. Any of these can change the result as much as forecast error does. The study should either include them or state that it excludes them.

## 2. Problems with the design-flood scenario

- **One design hydrograph shape is a single point of failure.** The benefit of prerelease depends strongly on flood volume, how early the volume arrives relative to the peak, and whether a second peak follows. A rule tuned to one shape can do worse on another. It is not stated how many shapes were used.
- **Only the 100-year flood is reported.**
  - Smaller floods (5- to 50-year): prerelease may release water that is never needed, cause flows downstream that would not otherwise have occurred, or leave the reservoir unable to refill.
  - Larger floods (the dam's design and check floods, up to the probable maximum flood): this is where dam-safety risk sits. A rule that lowers peak outflow by storing more water can raise the maximum reservoir level.
  - An adoption decision needs results across return periods, not at one point.
- **Successive floods.** If a second flood arrives before the reservoir is drawn back down or refilled, the outcome can be very different. A single design flood does not test this.
- **Daily time step.** For a 600 million m³ reservoir the peak outflow may occur within a day. With daily forecasts and a daily simulation, the peak outflow and its timing may be smoothed out. Check that the 18% holds at the operational time step (for example hourly or 6-hourly).

## 3. Problems with the outcome measure and the "95% confidence" claim

- **What exactly is 18%?** The mean of the peak outflow, the median, a high percentile, or the outflow under the forecast with no error? And what is the 95% statement: a confidence interval on the mean reduction, the share of runs in which the new rule is better, or something else? These mean very different things for a safety decision.
- **Was the comparison paired?** Both rules should be run on the same 5,000 synthetic forecasts, the same flood and the same starting level, and the difference computed run by run. The study should report:
  - the full distribution of that difference;
  - the share of runs in which the new rule is worse;
  - how much worse it is in those runs (the tail, for example the expected value of the worst 5% or 1%).

  An average gain of 18% can hide a small share of runs where the new rule fails badly. Usually that happens when a missed or late forecast means prerelease did not happen. For a flood-safety decision, those runs matter more than the average.
- **The confidence is conditional on the model.** "95%" holds only if the pooled, independent normal error model, the single design hydrograph and the simulator are all correct. It is not 95% confidence that the rule will lower outflow in reality. Presenting it that way to the owner overstates the evidence.
- **Peak outflow is only one measure.** At minimum, I would also need:
  - maximum reservoir level, and the probability of exceeding key levels (flood-control level, design flood level, dam crest margin);
  - peak flow and stage at downstream control points, including local inflow and travel time, not just the release at the dam;
  - flows caused by the prerelease itself: the release rate, how long it lasts, and whether it already exceeds safe channel capacity;
  - false-alarm cost: water released for floods that did not come, refill probability at the end of the flood season, and lost water supply or hydropower;
  - limits on release changes and ramping, and how often gates must move.

## 4. Problems with the baseline, the simulator and feasibility

- **Is the current rule encoded faithfully?** It should be checked against historical operating records (levels and releases) before it serves as the comparator. If the simulated current rule performs worse than real operators do, the gain is inflated.
- **Is the simulator validated?** The water-balance model should reproduce observed levels and releases for historical floods, with the correct storage–level curve and outlet capacities.
- **Reference bounds are missing.** The same flood should also be run with no forecast and with a perfect forecast. That shows how much of the 18% comes from the rule's logic, how much from forecast information, and how close the rule is to the best that perfect information allows. If the new rule comes close to the perfect-forecast result under the assumed errors, the errors are probably too optimistic.
- **Physical feasibility of prerelease.** Check that the forecast volume calls for a drawdown that can actually be done within the effective lead time, given:
  - outlet capacity at the lower levels reached during drawdown;
  - limits on release changes;
  - the safe downstream discharge.

  This must hold under real lead times, after allowing for when forecasts are issued, how long decisions take, and how long releases take to reach downstream. A rule that works on paper with a 3-day lead may have only 1.5–2 days of usable lead in practice.

## 5. Additional analyses and evidence I would require

In rough order of priority.

**A. Rebuild and verify the forecast-error model**
1. Split the errors by lead time (day 1, 2, 3), by flow size (at least a high-flow subset above a flood threshold) and by season where the data allow. Test for bias, skewness and heavy tails (Q–Q plots, goodness-of-fit tests). Consider relative errors, errors whose spread grows with flow, or a mixture or other non-normal distribution.
2. Model the dependence between lead times and between successive forecasts, for example with a copula over lead times or a model of how forecasts evolve from one issue to the next. Make sure the generated forecasts stay consistent from one issue to the next.
3. **Check that the generated forecasts are faithful.** They should reproduce the observed distribution of 3-day volume errors, peak-timing errors, autocorrelation and spread, and they should cover the largest observed floods. They must do this for the high-flow events, not just on average.
4. Quantify parameter uncertainty, for example by bootstrapping whole years or whole flood events from the 12-year record. Carry it into the outflow results.
5. Confirm that the 12-year hindcast represents the forecast system in use now. If it does not, use recent years or reforecasts from the current system.

**B. Test with real forecasts on real floods**
6. Run both rules on every significant flood in the 12-year record using the archived real forecasts (a hindcast), and compare paired results event by event. Real errors carry their real dependence and bias, so this is the most direct check of the synthetic results.
7. Hold out years or events (for example leave one year out) if any rule parameters were tuned on the same record.
8. Scale the largest historical floods up to 100-year (and larger) magnitude while keeping their real forecast-error patterns. This gives an alternative to the synthetic design-flood experiment.

**C. Stress and sensitivity tests**
9. Inflate the error spread (for example ×1.5 and ×2), add systematic underforecast bias at the peak, shift the peak timing, and simulate a missed forecast, a false alarm and a forecast outage. Find the error level at which the new rule stops beating the current rule, and compare it with the error level actually seen in large floods.
10. Vary the design flood: several hydrograph shapes (single and multiple peaks, early and late volume), successive floods, and the full range of return periods from frequent floods up to the dam's design and check floods.
11. Vary the starting level within its realistic range at the start of a flood.
12. Repeat at a finer time step if peak timing within a day matters.

**D. Report a decision-relevant result**
13. For each return period, report:
    - the paired distribution of the change in peak outflow;
    - the probability that the new rule is worse, and the tail of its losses;
    - maximum reservoir level and exceedance probabilities at key levels;
    - downstream peak flows and stages at the control points;
    - refill and water-supply or hydropower effects, including false alarms.
14. Replace "95% confidence" with ranges that also include uncertainty in the error model, the design flood and the starting level, for example the spread of results across the different error models and scenario sets.
15. Set an explicit acceptance criterion with the owner and the dam-safety authority before looking at results. For example:
    - the new rule must not raise the probability of exceeding any dam-safety level compared with the current rule, at any return period;
    - it must not create downstream flows above safe capacity through prerelease;
    - it must reduce downstream peaks in most floods.

**E. Baselines and model credibility**
16. Validate the simulator and the encoded current rule against historical operation.
17. Add the no-forecast and perfect-forecast runs to bound the benefit.
18. Check prerelease feasibility against outlet capacity, release-change limits, safe channel capacity and the effective lead time.

**F. Operational readiness (if the evidence above supports the rule)**
19. Define how the rule handles a wrong forecast:
    - how releases are adjusted as forecasts are updated, re-deciding each time a new forecast is issued;
    - when it falls back to the current, measurement-based rule (for example when the forecast is missing, late, or clearly diverging from observed inflow).
20. Confirm institutional feasibility: authority to release ahead of the flood, downstream warning procedures, liability for releases caused by false alarms, and staff ability to apply the rule in real time.
21. Have the analysis reviewed independently, ideally with access to the code and data.
22. Adopt in stages, keeping it reversible:
    - first a trial run in parallel without changing actual operations (operators record what the new rule would have done, alongside actual operation);
    - then, if justified, a temporary, documented change to the operating manual, with a review after each significant flood and clear triggers for reverting.

## 6. What would confirm or change my recommendation

- **Toward adoption:** the new rule still meets the agreed acceptance criteria when the following all hold:
  - errors that depend on lead time and flow, with realistic dependence;
  - inflated and biased errors;
  - several flood shapes and return periods;
  - real hindcast floods;
  - and it never meaningfully raises dam-safety or downstream risk relative to the current rule.

  Then I would recommend staged adoption with a fallback rule, even if the gain turns out smaller than 18%.
- **Toward rejection or redesign:** any of the following.
  - The benefit disappears once errors are realistically correlated or inflated to the size seen in large floods.
  - The rule raises the maximum reservoir level or prerelease flows above safe limits in some floods.
  - Prerelease cannot physically be completed within the usable lead time.
  - False alarms cost too much water.

  In that case the rule would need redesign, for example more conservative triggers, a cap on how much water it pre-releases, or a shorter lead time it relies on, and a new evaluation.

**Key assumptions in this review:** I have not seen the firm's report. I assume the 18% is a summary of peak outflow at the dam from the synthetic runs. I assume the "95% confidence" comes from those runs. I assume only one 100-year design hydrograph and one starting condition were used. If the firm did any of the checks above and did not report them, some of these concerns fall away. They should be asked to show that work.
