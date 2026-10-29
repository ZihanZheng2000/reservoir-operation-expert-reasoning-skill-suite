# Raising the flood-season operating level from 152 m to 154 m: feasibility check

## 1. Theoretical maximum allowable level

### 1.1 What limits the pre-release

The plan only works if, once a flood shows up in the forecast, the 180 million m³ stored between 152 m and 154 m can be released before the flood arrives. Releasing it must not push the town's control section above its safe discharge.

- **Usable release is set by the town, not by the dam.** The gates can pass 7,500 m³/s at 152 m, which is more than the downstream channel can take. The intervening catchment can add up to 1,200 m³/s during storms. If I assume that inflow coincides with the pre-release (the conservative case, because pre-release happens when a storm system is approaching), the reservoir can release at most
  Q_rel,max = 5,000 − 1,200 = **3,800 m³/s**.
- **Net drawdown rate.** Before the flood, inflow is about 1,500 m³/s, so
  ΔQ = 3,800 − 1,500 = **2,300 m³/s**, which is about 8.28 million m³/h.
- **Usable time.** The forecast gives 36 h of lead time. Decision, warning and gate adjustment take 8 h, which leaves **28 h** of effective drawdown time.
  The forecast is updated every 6 h, so in the worst case the flood first appears in a forecast issued up to 6 h after it became forecastable. That leaves only **22 h**.

### 1.2 Volume that can be evacuated

| Case | Effective time | Volume released = 2,300 × t × 3,600 | Compared with 180 million m³ |
|---|---|---|---|
| Ideal: flood detected at full 36 h lead | 28 h | **231.8 million m³** | +51.8 (+29 %) |
| Worst-case update timing | 22 h | **182.2 million m³** | +2.2 (+1.2 %) |

Time needed to evacuate exactly 180 million m³: 180×10⁶ / 2,300 = 78,261 s, which is **21.7 h**. Adding the 8 h of operational delay gives 29.7 h, so the flood must be seen at least about **30 h** before it arrives.

### 1.3 Converting volume to level

Storage above 154 m is not given. Assume, only to get a number, that storage is linear at 180 / 2 = 90 million m³ per metre. Then:

- In the 28 h case, 231.8 million m³ corresponds to 2.58 m, so the **theoretical upper limit is about 154.6 m**.
- In the 22 h case, 182.2 million m³ corresponds to 2.02 m, so the **theoretical upper limit is about 154.0 m**.

The reservoir usually widens as it rises, so each metre above 154 m holds more water than each metre below it. The true level for the same volume is therefore probably a little lower than 154.6 m. **Theoretical maximum: about 154.0–154.5 m.** In the idealised case 154 m is just inside it. Under the realistic worst case on forecast timing it sits right at the limit.

## 2. Can 154 m be the actual operating upper limit?

**Provisional judgment: No, not as a fixed limit for the whole flood season.** Under the current information 154 m is the edge of feasibility, not a level with a safety margin. The result in Section 1 depends on several optimistic simplifications, and each of them works against the plan:

1. **Inflow will not stay at 1,500 m³/s.** During the 36 h before a flood, inflow is rising. If it averages 2,000 m³/s, the net rate falls to 1,800 m³/s. That evacuates 181 million m³ in 28 h (zero margin) and only **143 million m³ in 22 h**, which brings the level down to about 152.4 m and not to 152 m.
2. **Releases cannot jump instantly to 3,800 m³/s.** Gates must be opened in steps, downstream warnings must be acted on, and channel ramp-rate limits apply. Ramping from 1,500 to 3,800 m³/s over a few hours costs several million m³ of evacuation.
3. **Forecast error.** A 36 h forecast of timing and volume has real uncertainty. A flood that arrives a few hours early, or rain that falls over the intervening catchment and the reservoir at the same time, wipes out a 1–2 % margin at once.
4. **Travel time and timing of the intervening flow.** The release takes time to reach the town and adds to the local 1,200 m³/s on a time-shifted basis. If the local catchment peaks while the pre-release wave is passing, the 3,800 m³/s figure itself becomes optimistic.
5. **Consequence of failure.** If pre-release fails, the design flood starts from up to 154 m. The 180 million m³ that the flood-control design assumed was empty is already used. This lowers the protection standard for the town and can raise peak reservoir levels toward the design or check flood levels, which affects dam safety. That is an asymmetric risk, so it needs a margin, not a break-even calculation.

**Provisional recommendation:**
- Treat 152–154 m as a *dynamic control range*, not a fixed new limit.
- Set the routine operating upper limit lower, provisionally about **153.0–153.5 m**. With 22 h, a net rate of about 1,800 m³/s and some ramping loss, roughly 110–140 million m³ can be evacuated, which corresponds to about 1.2–1.5 m above 152 m.
- Allow 154 m only under explicit conditions: a high-confidence no-rain forecast covering both the upstream and the intervening catchment, stages of the flood season with lower flood risk (for example the post-main-flood period), and a demonstrated forecast skill record.

**Key assumptions behind this judgment:**
- The full 1,200 m³/s of intervening flow coincides with the pre-release.
- Storage above 154 m is roughly linear.
- The 36 h lead time is lead to the start of significant flood inflow, not lead to the peak.

**What would change it:**
- **Toward accepting 154 m:** verified evidence that intervening-catchment flow is small during the pre-release window, reliable forecasts with effective lead time well beyond 30 h, or a shorter operational chain (for example a pre-authorised decision protocol).
- **Toward a lower limit than 153 m:** larger forecast errors, a short travel time, or frequent fast-rising floods.

## 3. Safety margins to consider

| Margin | What it covers | How to size it |
|---|---|---|
| Forecast lead-time margin | The 6 h update interval, early arrival, false or late detection | Use the hindcast distribution of detection lead time, for example the 90–95 % lower bound, not the nominal 36 h |
| Forecast volume and magnitude margin | Underestimated inflow and rising pre-flood inflow | Use a rising inflow hydrograph during pre-release, not a constant 1,500 m³/s, and add percentile error bands |
| Intervening-catchment margin | The ungauged 1,200 m³/s, its timing, and possible exceedance | Regional or rainfall-runoff estimate with uncertainty, checked against coincidence with mainstem flow |
| Operational margin | Decision delay beyond 8 h, gate failure, power loss, stuck gates, communication failure | Allow extra hours, and check with one gate unavailable (N-1) |
| Ramp-rate and downstream-safety margin | Rate-of-rise limits, people in the river, evacuation time after warning | Use the realistic release trajectory, not a step change |
| Storage or level margin | Stage-storage curve error, sedimentation, wind setup and waves | Updated bathymetric survey, plus freeboard checks |
| Dam-safety margin | Flood routing that starts from the higher level | Check that the design and check floods routed from the raised level stay within the design flood level, check flood level and freeboard |
| Downstream protection-standard margin | Whether the town still gets its design protection frequency if pre-release fails | Route the town's design flood starting from the proposed upper limit |

## 4. Verifications to carry out

1. **Hindcast and simulation of historical floods.**
   - Replay every significant historical flood, with the forecasts that were actually available or reconstructed, under the proposed rule.
   - Check that the level reaches 152 m, or a safe level, before the flood.
   - Check that the town never exceeds 5,000 m³/s.
   - Count failures and near-misses.
2. **Design-flood routing.** Route the design floods (reservoir and downstream protection standards) and the check flood starting from 154 m and from the candidate lower limits. Compare the peak levels and peak releases with those of the original design that starts from 152 m.
3. **Forecast-skill assessment.**
   - Statistics of lead time, peak, volume and timing errors.
   - Hit, miss and false-alarm rates for "flood or no flood" at the decision threshold.
   - Performance of the 6 h updates.
4. **Downstream hydraulic routing.**
   - Combine the pre-release with the intervening inflow, including travel time and attenuation.
   - Use an unsteady model or Muskingum-type routing to confirm the actual peak at the control section.
5. **Rising-inflow and ramping scenarios.** Calculate how much can be evacuated with a realistic gate-opening schedule and a rising inflow hydrograph.
6. **Stress tests.**
   - Back-to-back floods, where the second flood arrives before the reservoir has recovered.
   - Rain falling on the reservoir and the intervening catchment at the same time.
   - A forecast that misses entirely.
   - One gate unavailable.
7. **Risk quantification.** Compare the probability that the rule fails, and the expected flood damage or extra downstream risk, with the benefit gained (hydropower, water supply).
8. **Seasonal staging.** Check whether different limits suit different sub-periods (pre-flood, main flood season, post-flood season), based on seasonal flood statistics.

## 5. Information still missing

- **Stage-storage curve above 154 m and near the design and check flood levels**, together with the dam's characteristic levels and freeboard requirements.
- **Release capacity at each level**, gate configuration, the number of gates and their reliability, the permitted gate-operation speed, and downstream ramp-rate limits.
- **Intervening catchment:** area, rainfall-runoff behaviour, the statistical basis for 1,200 m³/s and its exceedance probability, its correlation with mainstem floods, and the flood travel time from the dam to the town.
- **Forecast performance record:** hindcast errors in timing and volume, what "36 h lead" actually refers to (onset or peak), rainfall-forecast skill, and false-alarm and miss rates.
- **Flood hydrograph characteristics:** typical rise time, how fast inflow increases before the peak, the design flood hydrographs, and the frequency of multi-peak floods.
- **Flood-control design basis:** the protection standard for the town, the original flood-control rule curve, and how the 152 m limit and the flood-control storage were derived.
- **Operational procedures:** who authorises a pre-release, whether the 8 h figure can be guaranteed (including at night or during communication failures), and how warning and evacuation work downstream.
- **Downstream constraints during pre-release:** river users, construction, navigation, and any limits on sustained high releases of about 3,800 m³/s for around 22 h.
- **Regulatory and approval requirements:** dynamic flood-limited water-level control normally requires approval from the flood-control authority, and that process should be confirmed.
- **Sedimentation status:** whether the storage figures reflect a recent survey.

Only when this information is in hand can the margins be quantified and a final operating upper limit (or a conditional, staged range between 152 and 154 m) be set.
