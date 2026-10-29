# Can 154 m be the operating upper limit? Theoretical ceiling, judgment, margins, checks, missing information

## Bottom line

- The calculation does not rule out 154 m. Under the stated assumptions, the largest storage above 152 m that can be drawn down before the flood arrives is about 232 million m³. That is more than the 180 million m³ between 152 and 154 m.
- Slightly more than 154 m is therefore theoretically permissible. The storage curve above 154 m is not given, so a level for 232 million m³ cannot be stated.
- That figure is a best-case ceiling. It uses the full nominal lead time, assumes the inflow stays at 1,500 m³/s, and assumes the forecast is right.
- Once the real timing and forecast losses are included, the margin at 154 m shrinks to almost nothing. If a forecast update is missed, it is about zero at typical inflow. At higher inflow it is negative.
- **Provisional judgment:** do not adopt 154 m as the actual upper limit yet. Treat it as the theoretical ceiling and a candidate for the actual limit. Use roughly 153.0 m (up to about 153.5 m) as the provisional working ceiling until the checks below are done. These level figures rest on a linear interpolation of storage between 152 and 154 m (about 90 million m³ per metre), which must be replaced by the real storage curve.
- 154 m can be reached later, with conditions, if the verifications support it. It would be a conditional, forecast-gated ceiling, not a standing limit.

## 1. Theoretical maximum allowable level

**Principle.** The level can be held above 152 m only if the water above 152 m can be released, in the time that remains after the decision, before the flood arrives, without breaching the downstream safe discharge.

**Release limit while drawing down.**
- The town's safe discharge is 5,000 m³/s.
- The intervening catchment can add up to 1,200 m³/s during storms. It is ungauged, so I assume the worst case: it peaks while the reservoir is releasing.
- Allowable reservoir release is therefore 5,000 − 1,200 = **3,800 m³/s**.
- The 7,500 m³/s release capacity is a gate or structure limit, not an operating limit. Using it would overstate drawdown speed by a factor of about 2.6, because 7,500 would put 8,700 m³/s through the town.

**Net drawdown rate.** Release minus inflow is 3,800 − 1,500 = **2,300 m³/s**.

**Time available.**
- The forecast gives 36 h of lead time.
- Decision, warning, and gate adjustment take 8 h, so release cannot start earlier.
- Effective drawdown time is 36 − 8 = **28 h = 100,800 s**.

**Maximum drawable storage:** 2,300 × 100,800 ≈ **231.8 million m³**.

**Checks.**
- The 180 million m³ above 152 m is drawn down in 180e6 / 2,300 ≈ 78,300 s ≈ 21.7 h. That leaves about 6 h of nominal slack.
- Because 231.8 > 180, the theoretical ceiling is at or above 154 m.
- Under the unsupported assumption of roughly constant reservoir area, 231.8 million m³ would be about 154.6 m. Reservoir area normally grows with level, so the true figure is likely higher. I do not use this number as a result.

**Simplifications built into this calculation.** All of the following make the figure optimistic:
- Constant inflow of 1,500 m³/s throughout the drawdown.
- Constant release at 3,800 m³/s, with instant ramp-up.
- A perfect forecast.
- No flood arrival earlier than forecast.
- No gate unavailability.
- Evaporation, seepage, and storage-curve error ignored.

## 2. Why 154 m should not be adopted as the actual upper limit yet

### 2.1 The effective lead time is shorter than 28 h

- **Forecast update cycle (6 h).** A flood may first appear in a forecast one cycle late. That cuts the effective time to about 22 h.
- **Forecast timing error.** A flood that arrives a few hours earlier than forecast, or a rise that starts before the nominal arrival, cuts it further. A planning case of about 16 h is not unreasonable.
- **Forecast reliability at long lead.** The 36 h end of the forecast is the least reliable part. Whether the 36 h forecast can trigger a full drawdown is unverified. It may be too late or too uncertain at the moment it is needed.
- **Release ramp-up.** I assume gate and ramp time is inside the 8 h. If it is not, subtract it.

### 2.2 Inflow before the flood is not fixed at 1,500 m³/s

1,500 m³/s is "typical". Inflow can be higher in the wet season, or can already be rising when the flood is forecast. The break-even inflow is the largest inflow at which 180 million m³ can still be drawn down in time:

| Effective time | Drawable at 1,500 | Drawable at 2,000 | Drawable at 3,000 | Break-even inflow for 180 Mm³ |
|---|---|---|---|---|
| 28 h | 231.8 Mm³ | 181.4 Mm³ | 80.6 Mm³ | ≈ 2,010 m³/s |
| 22 h | 182.2 Mm³ | 142.6 Mm³ | 63.4 Mm³ | ≈ 1,530 m³/s |
| 16 h | 132.5 Mm³ | 103.7 Mm³ | 46.1 Mm³ | ≈ 690 m³/s |

Reading the table:
- At 28 h, 154 m passes only if inflow stays below about 2,000 m³/s.
- At 22 h, 154 m passes only if inflow is no higher than the typical value, which leaves essentially no margin.
- At 16 h, 154 m fails even at typical inflow. Only about 132 Mm³ can be drawn, which is about 153.5 m on the linear interpolation.

So 154 m holds in the nominal case and has essentially no margin in a realistic degraded case.

### 2.3 The failure case is a missed or late forecast, not a good forecast

If the reservoir sits at 154 m and the flood is not forecast, or is forecast late, the flood-control storage is 180 million m³ smaller than designed. The 152 m flood-limited level was set for the design flood, so this is where risk is created. The real test is the consequence of a late forecast, not a successful drawdown. The tail case is a late-forecast large flood, with possibly a gate failure on top.

### 2.4 Downstream limit is conservative but not exact

- Assuming the full 1,200 m³/s of intervening flow is coincident makes 3,800 m³/s conservative.
- The release peak and the intervening-catchment peak may not coincide. Travel time from dam to town is not given.
- Before the storm starts, the intervening catchment may contribute little. Releasing at up to 5,000 m³/s in the early part of the window could add drawdown.
- That credit cannot be claimed without knowing travel time, the baseline downstream flow, and the timing of intervening-catchment response. I do not count it in the base case.

### 2.5 The goal "hold 154 m when no flood is forecast" depends on "no flood forecast" being trustworthy

- A "no flood" call at lead 36 h needs a known miss rate.
- Southern China convective and typhoon events can develop faster than the forecast horizon.
- A fixed 154 m hold across the whole season is a different risk from a 154 m hold that is released as soon as a trigger fires.

### 2.6 Regulatory and implementation status

- A flood-limited level of 152 m is typically a regulated design value.
- Operating above it needs approval from the flood-control authority. It also needs demonstrated feasibility under the real tools, rules, and procedures, and an agreed fallback.
- Model feasibility is not implementability.

## 3. Safety margins to consider

1. **Lead-time margin.** Subtract the forecast update delay (up to 6 h) and the timing error of flood arrival from the 28 h. Reserve gate-ramp time if it is not in the 8 h. Use a conservative effective time, for example 16 to 22 h, as a design basis.
2. **Inflow margin.** Use a high quantile of pre-flood inflow in the season, not the typical 1,500 m³/s. Include the possibility that the rise has already begun.
3. **Release margin.** Use the actual release capacity at each level (it depends on head). Include gate availability (for example one gate out of service). Include discharge ramping or release-change limits and downstream warning requirements.
4. **Downstream margin.** Treat the 5,000 m³/s safe discharge as a limit with buffer, not a target. Treat the 1,200 m³/s as a maximum observed or assumed value. Check whether larger intervening inflow has occurred or is physically possible, since it is ungauged.
5. **Forecast-error margin.**
   - Use a conservative quantile or an ensemble upper bound, not the point forecast.
   - Add the effect of underforecast of volume and peak.
   - Use a lead-time-dependent tolerance: no tolerance for risk in short lead times, more in long ones.
6. **Storage margin.** Include storage-curve uncertainty, sedimentation or survey age, and wind setup or wave allowances where they matter for dam safety.
7. **Return-to-152 margin.** The level must be back at 152 m, not just close, when the flood arrives. A margin on arrival time is needed so that the reservoir does not meet the rising limb above 152 m.
8. **Refill and water-use margin.** The cost of a false alarm is water released that cannot be recovered before the dry season. This is not a safety margin, but it determines how often the drawdown is acceptable and so affects the choice of trigger.

## 4. Verifications to carry out

1. **Reproduce the calculation with the real physical data.**
   - Use the actual storage-elevation curve, the head-dependent discharge curve at each level, and the real gate configuration, not only the 152 m capacity.
   - Include gate operating speed and release ramp.
   - Run it as a time-stepped water balance, with the real inflow hydrograph rising during the drawdown, not as constant-rate arithmetic.
2. **Downstream routing.** Route reservoir release plus intervening-catchment hydrographs (with realistic timing, not coincident peaks only) to the town control section. Test against 5,000 m³/s. Calibrate or bound the intervening catchment with rainfall-runoff or the nearest gauged analogues, since it is ungauged.
3. **Hindcast of forecast timing and error.**
   - Collect historical forecast and observed inflow pairs by lead time.
   - Quantify error by lead time, in particular at 24 to 36 h, for peak, volume, and timing.
   - Estimate the missed-flood and late-alarm rate.
   - Check how often the first alarm appeared with less than 36 h of lead.
4. **Event replay.** Replay historical floods, especially fast-rising ones, with the 154 m rule against the 152 m rule. Check the level at flood arrival, peak release against the safe limit, maximum level, and the number of times the drawdown could not finish.
5. **Design and check flood routing from 154 m.** Route the design flood and check flood from 154 m as an initial level for the failure case (no forecast or late forecast, and with gate unavailability). Compare maximum level, outflow, and downstream flow against the dam safety level and against the risk of the current 152 m rule.
6. **Risk comparison.** Use the current rule (152 m) as the benchmark. The new limit should not raise reservoir-side or downstream risk above it. Distinguish risk within and beyond the forecast lead time. Weight by flood occurrence probability.
7. **Sensitivity and stress tests.** Vary inflow, effective lead time, release capacity, forecast bias, intervening inflow, and storage curve. Find the combination at which the chosen ceiling stops being safe. Include floods larger than the historical record.
8. **Operational value, not only safety.** Compare the 154 m rule against a no-forecast baseline (hold 152 m) and a perfect-forecast reference. Quantify the water or generation gain and the water lost to false alarms, so the extra 2 m is shown to be worth its risk.
9. **Fallback rule.** Test a measurement-based fallback when the forecast fails: a level-based or observed-inflow trigger that forces release or lowers the ceiling. Test it when a forecast update is missed or the data link fails.
10. **Implementation review.** Confirm the rule can be run with the available tools, communications, and decision authority within the 8 h. Run a drill or controlled pilot if approval allows.

## 5. Information still missing before the final limit can be set

- Storage-elevation curve above 154 m and the actual curve between 152 and 154 m.
- Discharge capacity at each level, gate number and configuration, gate operating speed and ramp limit, and an outage scenario.
- Whether the 8 h includes gate ramp-up, and whether the 8 h is fixed or varies by time of day or event.
- Travel time from dam to the town control section, channel storage, and the timing relation between reservoir release and the intervening-catchment peak.
- Whether the 1,200 m³/s is a record, a design value, or an estimate, and the downstream baseflow before storms.
- Distribution of pre-flood inflow by season and by typical event, not only the typical 1,500 m³/s.
- Historical forecast verification by lead time, in particular the false-negative rate and the timing error at 24 to 36 h, plus whether the 36 h forecast is a point or an ensemble forecast.
- Design flood and check flood hydrographs, the dam safety level, and the current rule's risk as the benchmark.
- Flood-season stages (pre-flood, main flood, typhoon season) and whether the ceiling should vary by stage.
- Downstream operating rules: ramp limits, warning requirements, any other reservoir or tributary contributing at the control section.
- Water-use value of the extra storage, and refill probability if the drawdown is a false alarm.
- The regulatory and approval route for operating above the design flood-limited level.

## 6. What would confirm or change the provisional judgment

- **Would support raising the ceiling toward 154 m (or higher):**
  - Verified 24 to 36 h forecast reliability, with a low miss rate.
  - A real storage curve that shows a smaller volume between 152 and 154 m than 180 million m³ of unrealistic margin, or a higher discharge capacity that allows a faster drawdown within the downstream limit.
  - Evidence that the intervening-catchment peak is delayed relative to release, so that higher release is allowed early in the window.
  - Design and check flood routing from 154 m that meets the current rule's risk benchmark even under a late-forecast scenario.
- **Would lower the ceiling:**
  - Pre-flood inflow above about 2,000 m³/s in the flood season.
  - A real effective lead time of 16 h or less.
  - Failure of the late-forecast routing test.
  - A gate outage scenario that cuts release below 3,800 m³/s.
  - A higher intervening inflow than 1,200 m³/s.

## 7. Recommended operating structure for now

- Keep 152 m as the default flood-season level until verification is complete.
- Allow a lower candidate ceiling, about 153.0 m, as a forecast-gated hold when no flood is forecast. This rests on a simple linear interpolation and must be redone with the real storage curve.
- Require a drawdown trigger at each 6-hourly update, with the plan recomputed each time. Do not decide once and wait.
- Tie the ceiling to current inflow, so the allowed level falls when inflow is high or rising.
- Keep a measurement-based fallback to 152 m when the forecast is unavailable or doubtful.
- After the checks, consider raising the ceiling stepwise toward 154 m, ideally through a pilot with review after each event.
