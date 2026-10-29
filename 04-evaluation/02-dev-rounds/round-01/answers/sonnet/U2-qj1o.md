# Answer: Upper operating level for a reservoir with a 152 m flood-limited level

## 1. Verdict

- The theoretical calculation shows that 154 m is not safe as the actual operating upper limit. It is borderline at best.
- The theoretical maximum depends on how the 36 h lead time is counted:
  - Nominal lead time: about 231.8 million m³ above 152 m, which is above 154 m.
  - Worst-case lead time with the update cycle: about 182 million m³, which is just 154 m, with a margin of about 1%.
- 154 m is therefore the theoretical ceiling under optimistic, zero-error assumptions. It is not a defensible operating limit.
- Provisional recommendation:
  - Treat 154 m as the absolute upper bound.
  - Set the working limit to a level holding roughly 110–140 million m³ above 152 m. Under the linear-storage assumption below, that is about 153.2–153.5 m.
  - Fix the number only after the verifications in section 5 are done.
  - Because the intervening catchment is ungauged, make any value above 152 m conditional on a rule that falls back to 152 m when forecast confidence is low.

## 2. Theoretical maximum allowable level

### 2.1 Release constraint

- Downstream safe discharge at the town is 5,000 m³/s.
- The ungauged intervening catchment may add up to 1,200 m³/s.
- Because the intervening flow cannot be measured, the release must be planned for the worst case.
- Maximum safe release = 5,000 − 1,200 = **3,800 m³/s**.
- The 7,500 m³/s gate capacity at 152 m is irrelevant here. Capacity is not the binding constraint. The downstream limit is.
- Net drawdown rate = release − inflow = 3,800 − 1,500 = **2,300 m³/s**.
  - This assumes inflow stays at the typical pre-flood value of 1,500 m³/s.

### 2.2 Time available

The decision and gate-adjustment chain takes 8 h. Releases start only after that.

| Case | Lead time seen | Drawdown time | Storage that can be removed |
|---|---|---|---|
| A: nominal | 36 h | 36 − 8 = 28 h | 2,300 × 28 × 3,600 = **231.8 Mm³** |
| B: forecast-cycle worst case | 30 h | 30 − 8 = 22 h | 2,300 × 22 × 3,600 = **182.2 Mm³** |

- Case B reflects the 6 h update interval.
  - A flood entering the 36 h horizon just after an update is first seen at the next update.
  - It is then seen with only 30–36 h of lead time remaining, so 30 h is the worst case.
- The 180 Mm³ between 152 m and 154 m is almost exactly what Case B can remove.
  - Margin: 182.2 − 180 = 2.2 Mm³, which is about 1%.

### 2.3 Maximum level

- Under Case A the theoretical level exceeds 154 m. The extra storage is 231.8 − 180 = 51.8 Mm³ above 154 m.
  - The storage curve above 154 m is not given, so I cannot convert that to a level.
  - I will not invent it.
- Under Case B the theoretical maximum is about 154.0 m. It is slightly above only if the curve is gentle.
- If storage is roughly linear at 90 Mm³/m (assumed from 180 Mm³ over 2 m), then the limits are:
  - Case A: about 154.6 m.
  - Case B: about 154.0 m.

This is a theoretical ceiling. It assumes:

- the release is at the full 3,800 m³/s the moment the 8 h is up;
- inflow is constant;
- the flood does not begin to rise before the lead time expires;
- the forecast is perfect;
- no other restriction applies.

None of these holds in reality.

## 3. Is 154 m acceptable as the actual upper limit?

**No.** Reasons:

1. **No margin in the worst case.** The margin in Case B is about 1%. Any small loss of time or a small rise in inflow breaks the case. The 8 h chain is also an estimate, and real delays are longer.
2. **The drawdown deadline is earlier than the lead time.**
   - The reservoir must be at 152 m when inflow rises above the allowable release, not when the peak arrives.
   - Inflow starts rising before the peak, so the real available time is shorter than 22–28 h.
   - The reservoir cannot keep releasing 3,800 m³/s once inflow exceeds it.
3. **Gate ramp-up is not instantaneous.** Gates are not opened to 3,800 m³/s on the first minute, and downstream warning and evacuation may require a staged increase.
4. **Inflow is not constant.**
   - If inflow averages 2,000 m³/s during the drawdown, the net rate falls to 1,800 m³/s.
   - Removable storage then falls to about 143 Mm³ in 22 h, and about 130 Mm³ with 20 h effective.
5. **Forecast error.** A 36 h inflow forecast has error in timing, volume and peak, especially for typhoons and convective storms in southern China. The forecast may also miss events completely.
6. **The 1,200 m³/s intervening flow is a maximum.** It may be larger in an extreme storm. It also may coincide with the dam's flood flows.
7. **Loss of flood-control capacity.** Holding at 154 m permanently removes 180 Mm³ from the flood-control storage. If the forecast misses or the flood arrives faster than forecast, the reservoir starts the flood at 154 m instead of 152 m. The design flood routing and dam safety checks must then be satisfied from the higher starting level.
8. **Regulatory.** 152 m is the design flood-limited level. Operating above it during the flood season usually needs formal approval from the flood-control authority. This is a institutional issue, not only a technical one.

## 4. Safety margins to consider

| Margin | What it covers | Treatment |
|---|---|---|
| Forecast update delay | Up to 6 h between updates | Use 30 h, not 36 h |
| Decision and gate chain | 8 h is nominal | Use the longest observed time, plus a buffer |
| Gate ramp rate and downstream warning | Release cannot reach 3,800 m³/s at once | Model the ramp, and time-lag to the town |
| Travel time dam to town | Not given | Use it to time releases against the intervening peak |
| Inflow rise during drawdown | Inflow is not constant | Use the forecast hydrograph, not the 1,500 m³/s mean |
| Forecast error | Volume, peak, timing, missed events | Use an error envelope or ensembles, e.g. P90 |
| Intervening catchment uncertainty | Ungauged, up to 1,200 m³/s, may be more | Keep the 3,800 cap, and add a margin on 1,200 |
| Downstream control-section uncertainty | Rating curve, channel changes, backwater | Check that 5,000 m³/s is still safe |
| Drawdown-rate limits | Dam slope stability, bank erosion, and levee safety | Check the limits for falling level and for sudden releases |
| Equipment reliability | Gate failure or power loss | Assume one gate or unit unavailable |
| Operator and communication reliability | Human delay and failed warnings | Use a drill-validated time |
| Level measurement error and wave allowance | A level of 154 m is not exact | Add an allowance |
| Structural margin | Dam safety at higher levels | Check against the design and check-flood levels |

A practical way to apply them is to run a time-stepping drawdown calculation with the reduced time, a ramp, a rising inflow and a reduced release. The working limit is the level where the storage above 152 m can still be removed with a reserve, for example 15–25%.

Illustration, with assumptions only:

- 20 h effective drawdown.
- Average net rate of 1,800 m³/s.
- Removable volume = 1,800 × 20 × 3,600 ≈ 130 Mm³.
- Subtract a 15–20% reserve to get about 105–110 Mm³.
- That is roughly 153.2 m under the linear assumption.

This is an illustration, not a result.

## 5. Verifications to carry out

1. **Storage–level curve above 152 m.** Verify the table, and check the accuracy of the 180 Mm³ between 152 and 154 m.
2. **Time-stepping drawdown simulation.** Use the observed gate ramp, a rising inflow and release limits.
3. **Historical replay.**
   - Take past floods, including typhoon events.
   - Replay the forecast at each 6 h update, with the real forecast and the real errors.
   - Count the cases where the reservoir could not return to 152 m before the inflow rose.
4. **Forecast skill assessment.**
   - Check the lead time and the error of the forecast against observed events.
   - Check the missed-event rate and the false-alarm rate.
   - Establish the confidence level for the "no flood" statement.
5. **Intervening catchment check.**
   - Estimate the 1,200 m³/s value and its uncertainty.
   - Test whether it can exceed that value, and how often it coincides with the dam inflow.
6. **Downstream routing.**
   - Route reservoir release plus intervening flow to the town.
   - Verify the 5,000 m³/s with travel time and attenuation.
7. **Design and check-flood routing from the proposed starting level.** Verify that the reservoir and the dam remain safe for design and check floods starting from 154 m or from the working limit. Include the case of a missed forecast.
8. **Gate and release capacity test.** Check capacity at levels above 152 m, and with one gate out of service.
9. **Operational drill.** Measure the actual time of decision, warning and gate adjustment.
10. **Sensitivity and risk analysis.**
    - Vary lead time, inflow, intervening flow and release ramp.
    - Estimate the probability of breaching 5,000 m³/s downstream and of exceeding the dam limit.
11. **Regulatory check.** Confirm what the approved scheduling rules allow above the flood-limited level.

## 6. Missing information

- The storage–level curve above 154 m, and below 154 m in detail.
- Travel time from dam to the town, and channel attenuation.
- Real gate ramp rates, the staged release rules, and the downstream warning requirements.
- Forecast skill: error statistics, rate of missed events, and whether the "36 h" lead is for the flood start or the peak.
- The meaning of "typically 1,500 m³/s" (mean, base flow, or median), and its variability.
- The design flood hydrographs, rise rates, and typical time between the first rise and the peak.
- Basis of the 1,200 m³/s: its return period, uncertainty, and any gauges.
- Whether there is an upstream or downstream reservoir, and other flood-control works.
- Dam and downstream safety limits: drawdown-rate limits, structural levels, levee conditions.
- Regulatory limits: whether the flood-limited level can be exceeded and who approves it.
- Season: whether the pre-flood and main flood seasons have different limits.
- The purpose of holding 154 m: water supply, hydropower or ecology. This sets the benefit to weigh against the risk.
- Operational reliability: equipment, power supply, and communications.

## 7. What would change the provisional judgment

- **Raise the limit towards 154 m** if:
  - the real forecast skill is shown to be high with no missed events;
  - the real chain time is much shorter than 8 h;
  - the intervening flow is better measured, so that more than 3,800 m³/s can be released;
  - the storage curve above 154 m is steep or the verified inflow is low;
  - the flood-control authority approves.
- **Lower the limit** if:
  - the historical replay shows failures;
  - the drawdown rate is limited by dam or bank safety;
  - the gate ramp is slow;
  - typhoon floods rise quickly;
  - the intervening flow can exceed 1,200 m³/s;
  - the travel time to the town is short.
- The key judgment: **the nominal calculation (154 m or slightly above) is a ceiling, and the working limit should be set below it by verified margins. Until verification is done, 154 m should not be the standing upper limit.**
