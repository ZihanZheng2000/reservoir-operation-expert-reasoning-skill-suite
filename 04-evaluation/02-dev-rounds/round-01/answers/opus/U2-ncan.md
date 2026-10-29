# Can 154 m serve as the operating upper limit above the 152 m flood-limited level?

## Short answer

- **The theoretical maximum.** Under the stated assumptions, the reservoir can evacuate about **232 million m³** above 152 m before a forecast flood arrives. That is about 52 million m³ (29%) more than the 180 million m³ between 152 and 154 m. The matching theoretical maximum level is roughly **154.5 m**. The exact figure needs the storage curve above 154 m. A linear extrapolation of 90 million m³/m gives 154.58 m, and a curve whose storage per metre grows with level would give a little less.
- **Judgment.** 154 m sits close to the edge of what the forecast and the downstream channel can support. It should **not yet be adopted as the operating upper limit**. The 29% surplus holds only under best-case timing. Two realistic effects, each on its own, cut it to about 1%:
  - the 6-hour forecast update cycle;
  - inflow rising above 1,500 m³/s during the drawdown.
  
  Together they make 154 m infeasible. My provisional view: plan on a limit of about **153.3–153.6 m** for now, or allow 154 m only under extra conditions (listed below). Fix the final value only after the verifications described here, against a risk benchmark no worse than the current 152 m rule.

## 1. Theoretical maximum allowable level

**Logic.** A level above 152 m is allowed only if the extra storage can be released back to 152 m before the flood arrives. Two limits apply during that drawdown:
- the release must not push flow at the town above its safe discharge;
- the release cannot start until the decision and gate adjustment are complete.

**Inputs and assumptions**

| Item | Value | Note |
|---|---|---|
| Forecast lead time | 36 h | Assumed to be lead time to the start of the flood rise at the dam. If it is lead time to the peak, the usable window is shorter. |
| Decision + warning + gate adjustment | 8 h | No net drawdown during this time (release ≈ inflow). |
| Effective drawdown time T_e | 36 − 8 = **28 h** | |
| Safe discharge at the town | 5,000 m³/s | |
| Intervening inflow (worst case) | 1,200 m³/s | Assumed to coincide with the drawdown, because the same storm drives both and the catchment is ungauged. |
| Maximum allowable reservoir release | 5,000 − 1,200 = **3,800 m³/s** | Below the 7,500 m³/s outlet capacity. The downstream limit binds, not the outlets. |
| Inflow during drawdown | 1,500 m³/s | Pre-flood value, held constant. |
| Net drawdown rate | 3,800 − 1,500 = **2,300 m³/s** | |
| Travel time, attenuation, release ramping | Ignored | All are checked later. |

**Calculation**

ΔV_max = (Q_safe − Q_int − Q_in) × T_e = 2,300 m³/s × 28 h × 3,600 s/h ≈ **231.8 million m³**

- **Level.** 152 m + 231.8 / 90 ≈ 154.6 m with a linear storage curve. A real curve would probably give about 154.5 m. This is an illustrative figure only: the storage curve above 154 m is not given.
- **Time needed to empty 152–154 m.** 180 × 10⁶ / 2,300 ≈ 78,300 s ≈ **21.7 h**. That leaves about 6.3 h of slack in the 28 h window.
- **Equivalent condition.** 154 m is feasible only if the net drawdown rate over the effective window stays at or above 180 × 10⁶ / (28 × 3,600) ≈ **1,790 m³/s**.

**Two calculations to avoid**
- Ignoring the intervening inflow (release up to 5,000 m³/s) gives 352.8 million m³. This overstates capacity by about 50% and would flood the town if the storm also falls on the intervening catchment.
- Ignoring the 8 h delay gives 298 million m³. This counts time in which no drawdown actually happens.

## 2. Why 154 m is not yet a safe operating limit

The 232 million m³ figure assumes everything happens at the best possible moment. The table shows how realistic effects shrink the evacuable volume, using the same formula.

| Case | Effective time | Net rate | Evacuable volume | 154 m feasible? |
|---|---|---|---|---|
| Baseline (above) | 28 h | 2,300 | 231.8 Mm³ | Yes, 29% margin |
| Flood first seen one update late (36 − 6 − 8) | 22 h | 2,300 | 182.2 Mm³ | Barely (about 1%) |
| Inflow averages about 2,000 m³/s during drawdown | 28 h | 1,800 | 181.4 Mm³ | Barely (about 1%) |
| Both of the above | 22 h | 1,800 | 142.6 Mm³ | **No** (≈153.6 m) |
| Forecast reliable enough to act on only at 24 h | 16 h | 2,300 | 132.5 Mm³ | **No** (≈153.5 m) |
| Release ramp from 1,500 to 3,800 m³/s over about 4 h | loses ≈16.6 Mm³ | | ≈215 Mm³ (baseline) | Yes, but margin shrinks |

How each effect arises:
- **Update cycle.** A flood that starts just beyond the 36 h horizon is first seen at the next update. In the worst case, the usable lead time at detection is about 30 h, not 36 h.
- **Rising inflow.** Inflow begins to rise before the "flood" in forecast terms arrives.
- **Trustworthy lead time.** The 36 h is the nominal horizon. The lead time at which the forecast is reliable enough to trigger a costly drawdown is usually shorter. Operators often wait for a second update to confirm.
- **Ramping.** Release cannot jump instantly from 1,500 to 3,800 m³/s, either for safety in the channel or because of gate sequencing.

These effects are likely to occur together. 154 m is therefore an optimistic bound, not a limit with a safety margin.

**Provisional recommendation**
- **Planning value.** About **153.3–153.6 m**, i.e. roughly 120–145 million m³ above 152 m. This is what the combined adverse cases support with a modest margin. It assumes the curve is close to linear.
- **Conditional use of 154 m.** Possible only if:
  1. drawdown is triggered at a lower forecast threshold or from longer-range rainfall forecasts (e.g. 2–3-day quantitative precipitation forecasts), so it starts before the 36 h streamflow forecast confirms the flood;
  2. the forecast hindcast shows the lead time is reliably close to 36 h for floods large enough to matter;
  3. the design-flood check in section 4 passes from 154 m even when the drawdown fails.
- **What would raise it toward 154 m:** a reliable lead time demonstrated in hindcasts, an intervening-inflow bound shown to be lower than 1,200 m³/s or not coincident with the drawdown, and a pre-agreed early-drawdown trigger.
- **What would lower it further:** frequent missed or late forecasts, sharp rising limbs, sediment loss of storage, or a design-flood check that fails from 154 m.

## 3. Safety margins to consider

1. **Downstream flow margin.**
   - Is 5,000 m³/s a true safe discharge, or a bankfull or warning value?
   - Is a buffer below it needed for channel changes, backwater, or bridge constraints?
   - Should the operating release target be set below 3,800 m³/s?
2. **Intervening-inflow margin.**
   - 1,200 m³/s is an estimate for an ungauged catchment. Its basis, exceedance probability and timing relative to the reservoir flood are unknown.
   - Local rain may peak before the reservoir inflow peak, i.e. during the drawdown. That is when the margin matters most.
3. **Time margin.**
   - The 6 h update interval.
   - The decision, warning and gate time: 8 h may be optimistic at night or under poor communications.
   - Release ramping limits.
   - Travel time from the dam to the town, which delays when the release meets the local flow.
   - Waiting for a confirming forecast.
4. **Forecast-error margin.**
   - Timing errors (the flood arrives earlier than forecast).
   - Volume and peak errors.
   - Missed floods (false negatives).
   - All should be quantified by lead time from hindcasts, not assumed.
5. **Inflow-during-drawdown margin.** The rising limb, rather than a constant 1,500 m³/s.
6. **Storage and level margin.**
   - Storage-curve accuracy above 152 m, including sediment loss.
   - Level-gauge accuracy.
   - Wind set-up and waves near the dam, which matter for the design-flood check.
7. **Facility margin.**
   - Gate availability, e.g. one gate out of service.
   - Discharge-coefficient uncertainty.
   - Power supply and backup operation of the gates.
8. **Successive-flood margin.** After one flood, the reservoir must be back at 152 m, or have a recovery plan, before the next forecast flood. Refill to 154 m should only be allowed when the forecast shows no further flood.
9. **Forecast-failure (residual) margin.** If the drawdown does not happen at all (flood not forecast, or a gate failure), the reservoir starting at 154 m must still pass the design and check floods safely. This margin is separate from the drawdown arithmetic and is often the binding one.

## 4. Verifications to carry out

1. **Design and check flood routing from 154 m.**
   - Route the design and check floods from 154 m under two cases: no prerelease (forecast failure) and partial prerelease.
   - Confirm three things: the peak level does not exceed the design flood level, check flood level and crest constraints; the design flood level is not raised relative to routing from 152 m; and the downstream protection standard is still met.
   - This is the decisive dam-safety check.
2. **Lead-time mass-balance check under realistic conditions.**
   - Repeat section 1 with observed rising-limb hydrographs, the update cycle, ramping limits and travel time.
   - Use a time-stepped water-balance simulation, not a constant-rate formula.
   - Find the highest level from which the reservoir reaches 152 m before the flood under each condition.
3. **Forecast verification.**
   - Use a hindcast of the 36 h forecasts, issued every 6 h, against observed floods.
   - Measure error in timing, volume and peak by lead time; hit, miss and false-alarm rates for the flood trigger; and the lead time actually available at the first trigger.
4. **Risk assessment against a benchmark.**
   - Generate many forecast-error and intervening-inflow scenarios, preserving the dependence between local and upstream inflow, and route them.
   - Estimate two probabilities: the reservoir exceeding its safety levels, and the town exceeding 5,000 m³/s.
   - Accept a candidate upper limit only if both risks are no greater than those of the current fixed 152 m rule, or within the official protection standard.
   - Scan candidate levels (e.g. 152.5–154.5 m in 0.1–0.25 m steps) and take the highest one that passes.
5. **Downstream hydraulic check.**
   - Route the release plus intervening inflow to the town with a channel model that includes travel time and attenuation.
   - Confirm that a 3,800 m³/s release combined with the local peak really stays below the safe discharge.
6. **Historical replay.** Replay past flood seasons under the proposed rule and under the 152 m rule. Include multi-peak floods, typhoon-type floods and front-type floods, since these differ in southern China. Compare peak levels, downstream peaks, spills and extra stored water.
7. **Stress tests.**
   - Lead time shortened (e.g. 24 h, 18 h).
   - Intervening inflow above 1,200 m³/s.
   - Gate unavailability.
   - Back-to-back floods.
   - Floods scaled beyond the historical record.
8. **Benefit check.** Quantify what the extra water is worth: hydropower, water supply, and refill at the end of the season. This shows whether the added risk is justified, and whether a slightly lower limit gives most of the benefit.
9. **Operational and institutional check.**
   - Drawdown trigger rules, warning procedures and staffing for the 8 h chain.
   - Approval of dynamic flood-limited-level control by the competent flood-control authority. A model-feasible level is not an authorized one.
   - Ideally, a monitored trial period with review after each flood.

## 5. Information still missing

- **Storage curve** above 152 m beyond 154 m, and its current accuracy (sedimentation).
- **Characteristic levels and dam-safety thresholds:** design flood level, check flood level, crest level, and the flood standards they correspond to.
- **Design and check flood hydrographs**, including rising-limb shape and flood volume, for each flood season if the season is split.
- **Discharge capacity curve** by level and gate, gate operating rules, ramping limits, and gate reliability.
- **Downstream information:**
  - what 5,000 m³/s represents and the protection standard;
  - travel time from the dam to the town;
  - channel attenuation;
  - any other downstream control points or constraints.
- **Intervening catchment:**
  - the basis of the 1,200 m³/s figure;
  - its response time;
  - its timing relative to the reservoir flood;
  - any rainfall gauges that could be used to estimate it in real time.
- **Forecast performance:**
  - the exact meaning of the 36 h lead time (to onset or to peak);
  - error statistics by lead time;
  - hit, miss and false-alarm rates;
  - the flood definition and threshold that triggers drawdown;
  - availability of longer-range rainfall forecasts.
- **Seasonality:** whether different upper limits should apply in the pre-flood season and the main (typhoon) flood season.
- **Operating constraints and benefits:** minimum flows, navigation, hydropower, water supply, and the value of the extra storage.
- **Acceptable risk:** which benchmark the authority will accept (the current-rule risk or a prescribed standard), and who decides.

## Key assumptions behind this answer

- The 36 h lead time is to flood onset at the dam.
- No net drawdown occurs during the 8 h decision and gate period.
- The intervening inflow peak of 1,200 m³/s can coincide with the drawdown.
- Inflow stays at about 1,500 m³/s until the flood arrives.
- The storage curve is roughly linear near 152–154 m (90 million m³/m).
- Release changes and travel time are neglected in the theoretical figure.

If any of these is corrected, redo the calculation in section 1 and the scenario table in section 2.
