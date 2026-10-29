# Stânca–Costești: revised design floods and per-outlet flood operating rules

## 1. Provisional answer

**Design floods.** The rules should be designed and checked against a *set* of floods, not against one peak-scaled hydrograph. The set is defined by flood **volume** over 1 to 30 days as well as by peak:

| Design case | Basis | Climate allowance | Criterion the rules must meet |
|---|---|---|---|
| 1% flood (single-peak shapes) | Re-estimated joint peak–volume frequency at the dam, after the rating curve above 500 m³/s has been repaired | **+20% on peak and on volume as the design case**; 0% and +10% reported as well | Outflow ≤ 550 m³/s (riverbed), max level ≤ 98.20 m |
| 1% multi-peak / long-duration flood (2010 type) | 2010 sequence scaled to the 1% 15–30-day volume | Same +20% | Same as above, starting from the level left by the previous peak |
| 0.1% flood (several shapes, not only 1969) | Re-estimated peak and volume | **None for design**, as the guidance says; +10% and +20% run as a stress test | Max level ≤ 99.50 m, outflow never above inflow, no overtopping, freeboard kept |
| Check / safety-evaluation flood, if the dam's class requires one | Romanian dam-class norms | None | Level stays below dam crest 102.50 m with wave freeboard |
| Historical events 2005, 2008 (both peak estimates), 2010, 2020 | Reconstructed inflow at the dam | None | Must do no worse than the current rule on each event |

Why +20% and why volume. Section 2 shows that this reservoir is limited by volume, not by peak. Volume uncertainty from the rating extrapolation (2008: 3300 vs 4240 m³/s, about ±25%) is the same size as the uplift. Four large floods in 15 years also make the low end of the allowance hard to defend. The cost of the conservative choice is small, because it mostly moves non-damaging releases earlier. The guidance speaks of *flows*. Applying the uplift to volume is my interpretation, and the water authority must confirm it. If +20% makes the 1% riverbed criterion physically impossible (see the mass-balance test in Section 2), the study should not quietly weaken the rule. It should report how large the shortfall is and ask the authority to choose between (a) +10%, or (b) allowing up to 700 m³/s (flow between the dikes) for the uplifted 1% flood.

**Operating rules.** I recommend a two-tier, staged rule that operators can apply without knowing the flood size:

- **Tier 1, non-damaging release.** On a credible warning, raise outflow early to the riverbed capacity (550 m³/s minus local inflow at the downstream control point), including pre-release of up to about 100 mil. m³. At worst this costs water and refill risk. It never causes damage, and every m³ released early is storage kept for later.
- **Tier 2, damaging release (above 550, then above 700 m³/s).** This is triggered by the **reservoir state**: current level, current inflow and the inflow trend, read off a level–inflow release chart. It is never triggered by the forecast alone. The chart gives the minimum release that keeps the projected maximum level below the governing limit if the flood turns out to be at the upper end of the design set.
- **Fixed opening order:** power galleries → central bottom outlets → lateral bottom outlets → lowering of the flap gates bay by bay. **Closing runs in reverse order**, with hysteresis. Outflow never exceeds inflow on the rising limb, so the dam never adds a man-made peak.
- **The recession is part of the rule.** Storage above 90.80 m is emptied at the highest non-damaging rate as soon as the peak has passed, because the next peak (2010) is the most likely way to fail.

The thresholds in that table are what the study must calibrate. Starting values are in Section 4.

## 2. The deciding questions and order-of-magnitude answers

Three questions decide the outcome. The rest of the study supports them.

**Q1. Can a 1% flood, with uplift, be held within 550 m³/s at all, even with perfect operation?** If not, the "within riverbed up to 1%" objective is infeasible and the authority must decide the trade-off before rules are tuned.

**Q2. How much does the rating-curve problem change the design volume, and therefore the answer to Q1?**

**Q3. What can operators observe early enough to start Tier 1 without knowing the flood size, and what state variable safely triggers Tier 2?**

### Storage zones (from the given table)

| Zone | Levels (m) | Volume (mil. m³) | ≈ mil. m³ per m |
|---|---|---|---|
| Conservation to spillway crest | 90.80–95.50 | 325 | 69 |
| Spillway crest to raised flap crest (1% level) | 95.50–98.20 | 225 | 83 |
| Flap crest to 0.1% level | 98.20–99.50 | 115 | 88 |
| 0.1% level to dam crest | 99.50–102.50 | 309 | 103 |

- Storage available for a 1% flood: 550 mil. m³. With pre-release of 100 it becomes about **650**. For a 0.1% flood: 665, or about **765** with pre-release.
- Flap gates are 2.70 m high on the 95.50 m crest, so 95.50 + 2.70 = 98.20 m. The 0.5 m overflow limit therefore caps the level at **≈98.70 m with gates raised** (about 594 mil. m³ above conservation). Reaching the 0.1% level of 99.50 m therefore requires the flaps to be lowered. I am assuming the 0.5 m limit is a structural limit on raised gates, so "lower flaps before 98.70 m" becomes a hard rule. This must be confirmed with the dam owner.

### Release arithmetic

- 550 m³/s for one day = 47.5 mil. m³. 700 m³/s for one day = 60.5 mil. m³.
- Pre-release of 100 mil. m³ in 3 days = 386 m³/s of net release above inflow. That is roughly "release at 550 while inflow is about 150–200 for three days". The full 100 can only be reached if pre-release starts about 3 days before inflow reaches 550. Once inflow exceeds 550, no more volume can be gained without damage. **The point of no return for pre-release is therefore the moment inflow reaches the release cap, not the peak.**

### Q1 test: excess volume above the release cap

With ideal operation, the storage a flood needs is its volume above the release cap. For a triangular hydrograph this is V·(1 − q/Qp)².

- **2008** (V ≈ 1100, Qp = 3300): base length ≈ 2V/Qp ≈ 7.7 days. Excess above 550 ≈ 1100 × (0.833)² ≈ **764 mil. m³**. Excess above 700 ≈ 683. Both exceed the ≈650 available up to 98.20 m, even with full pre-release and a start at 90.80 m. With Qp = 4240, excess above 550 ≈ 833.
  - So even a perfect operator may not have been able to keep 2008 within the riverbed and below the flap crest, if its shape was this compact. A longer tail would lower the excess. The 2008 outcome may have been **largely forced by the flood**, not only by the 200 m³/s / 600 m³/s trigger. The 2008 starting level and gate log must settle this before "the rule failed in 2008" is used as a premise.
- **2010** (1600–1700 mil. m³ over "a few weeks"): over 21 days the mean inflow is ≈ 910 m³/s, so releasing 550 throughout still stores ≈ 650. Over 30 days the mean is ≈ 640 m³/s and ≈ 225 is stored. **The mean inflow over the whole event is near or above the riverbed capacity**, so storage can hardly be recovered between peaks. Emptying 550 mil. m³ at a net 300 m³/s (550 out, about 250 in) takes ≈ 21 days. At a net 450 m³/s (700 out) it takes ≈ 14 days. Both are longer than the gap between 2010 peaks. **Long-duration volume, not peak, is the governing design quantity.**
- **0.1% illustration.** If the 0.1% volume scaled with the 2008 ratio (4300/3300 × 1100 ≈ 1430, an illustrative assumption only), holding it within 765 mil. m³ needs a constant outflow q with (1 − q/4300)² = 765/1430, giving **q ≈ 1150 m³/s**. With a level-dependent outflow the peak outflow would be higher. This is plausible against the outlet capacity estimated below, but it must be checked with the real rating curves.

**Conclusion for Q1 (provisional).** At +20%, keeping the 1% flood within 550 m³/s is probably at or beyond the physical limit for compact single peaks and for 2010-type sequences. The study must compute this exactly. The best statistic to compute is the **annual maximum excess volume above 550 and above 700 m³/s**, frequency-analysed directly. It gives the probability that even ideal operation exceeds 98.20 m.

### Outlet capacity (illustrative; real rating curves needed)

- **Weir** (6 × 16 m = 96 m, Q ≈ 2.0·L·H^1.5, assumed coefficient):
  - Flaps down: at 98.20 m (H = 2.7) ≈ 850 m³/s; at 99.50 m (H = 4.0) ≈ 1540 m³/s.
  - Flaps up with 0.5 m overflow: only ≈ 70 m³/s.
- **Bottom outlets** (total area 49.5 m², Cd ≈ 0.8, and an *assumed* head of 25 m): ≈ 880 m³/s. Each 9 m² outlet gives about 160, each 15.76 m² outlet about 280.
- **Power galleries:** limited by the turbines (not given).

Implications:
- The 550–700 m³/s tier can probably be delivered by power galleries plus bottom outlets alone. **Lowering the flaps is the dam-safety tool.**
- Total capacity at 99.50 m is probably 2500–3000 m³/s, below the 4300 m³/s inflow peak, so the 0.1% flood is always attenuated by storage.

### Q3: timing

- **Travel time** Rădăuți–Prut → dam: about 160 km of winding reach at a wave speed of 1–3 m/s gives **15–45 h**, so roughly 1–3 steps of 12 h. This is the only observed lead time. It is shorter than the 3 days pre-release needs, so **full pre-release depends on the 3-day forecast**.
- **Local inflow:** 12,212 − 9,296 = 2,916 km², or 24% of the dam catchment and steeper. It can arrive before the routed upstream wave. The rule therefore needs a reservoir-inflow estimate from the water balance, I = O + ΔS/Δt, and not only the upstream gauge.
  - Accuracy check: a level error of 1 cm × ~80 mil. m³/m ≈ 0.8 mil. m³, or ≈ 19 m³/s over 12 h. This is usable if smoothed over 12–24 h. The outflow rating error (likely around ±10%) dominates.

### Q2: how far the record can resolve this

- 43 annual maxima support a 1% estimate only weakly and a 0.1% estimate barely at all.
  - P(at least one 1% flood in 43 years) = 1 − 0.99⁴³ ≈ 35%.
  - P(at least one 1% flood in a 10-year revision period) ≈ 9.6%. For a 0.1% flood: ≈ 1%. Over 50 years: 1 − 0.999⁵⁰ ≈ 4.9%.
- Four large floods (2005, 2008, 2010, 2020) are too few to separate a trend from clustering.
- **The confidence band, not the central estimate, should be carried into the rule check.**

## 3. Design-flood work plan

1. **Repair the high-flow rating at Rădăuți–Prut first.**
   - Build a hydraulic model of the gauge reach (surveyed sections, roughness calibrated below 500 m³/s, checked against 2008 high-water marks if any exist). Use slope–area checks.
   - Produce two or three alternative ratings that bracket the uncertainty. Do not pick one silently.
   - **Independent check:** reconstruct 2008 inflow at the dam by water balance from the recorded levels, outflows and gate operations. Route the gauge hydrograph (with each rating) to the dam, add local inflow by area or rainfall–runoff, and compare peak and volume. This also explains the gauge–dam volume mismatch: rating error, local inflow, or storage-curve error (resurvey if sedimentation has changed it).
2. **Transfer gauge → dam.**
   - Area ratio 1.31. Peaks scale less than linearly, volumes closer to linearly.
   - Calibrate on 2008, the only event with reservoir records. State that the transfer rests on one event, and test sensitivity with ratios from 1.15 to 1.31.
3. **Frequency analysis of peak *and* volume.**
   - Annual maxima of peak and of 1-, 3-, 5-, 10-, 15- and 30-day volume, plus the excess volume above 550 and 700 m³/s.
   - Fit candidate distributions with confidence intervals (bootstrap). Use the 1969 flood and any other documented pre-1978 floods as historical information to lengthen the record.
   - Fit a peak–volume copula, because volume governs and peak and volume are not perfectly correlated.
   - Run trend and change-point tests, interpreted cautiously.
4. **Design hydrographs.**
   - For 1% and 0.1%, choose peak–volume pairs on the joint-probability contour, including the high-volume, moderate-peak end.
   - Shape them with several observed shapes (1969, 2005, 2008, 2010, 2020), scaled consistently to peak and volume.
   - Add a 2010-type multi-peak sequence and a "1% peak arriving 7–10 days after a large flood" sequence.
   - Find the **critical duration**: the one that maximises volume minus cap × duration.
5. **Climate allowance.** Apply 0/+10/+20% to the 1% set and +10/+20% to the 0.1% set as a stress test only. Check the ordering: the uplifted 1% must not exceed the 0.1% in peak or critical volume. If it does, the 0.1% estimate needs revisiting.
6. **Synthetic ensemble for risk.** Generate thousands of events by sampling the joint peak–volume distribution with the observed shapes. Weight them by probability to compute exceedance probabilities of 98.20 / 98.70 / 99.50 m and of 550 / 700 m³/s under each rule. Report the Monte Carlo standard error, √(p(1−p)/N). For p ≈ 0.001 this needs N of the order of 10⁵ to get ±10%.

## 4. Operating rule: structure and per-outlet table

### Inputs operators can read in real time

- Z: reservoir level.
- I: reservoir inflow from water balance, averaged over 12 h, and its 12-h change.
- Q_R: Rădăuți–Prut flow and its trend.
- F3: 3-day forecast maximum and volume.
- P10: 10-day areal rainfall outlook.
- Q_d: downstream gauge flow, or local inflow below the dam.

### Hard constraints in every mode

- Total outflow O ≤ max(I, 550 − local downstream inflow) unless dam-safety mode applies.
- On the rising limb, O ≤ I. This applies even in dam-safety mode, except at a level where the rating forces more.
- Lower the flaps before Z reaches 98.70 m.
- Release changes are limited per 6 h (rate to be agreed for bank stability and downstream warning).
- Minimum 12 h between successive gate steps unless Z crosses a safety level (hysteresis against gate hunting).

### Modes and per-outlet actions (thresholds are starting values to be calibrated)

| Mode | Enter when | Outlets | Leave when |
|---|---|---|---|
| **0 Normal** | — | Power galleries for generation and water use; Z ≤ 90.80 m | — |
| **1 Alert** | Q_R ≥ 200 m³/s and rising, **or** F3 ≥ ~400 m³/s, **or** P10 above a calibrated threshold | Galleries at full capacity; gates tested; staff, power and downstream liaison on standby; no extra release unless Z > 90.80 | No trigger for 24 h → Mode 0 |
| **2 Pre-release (Tier 1)** | F3 ≥ ~600 m³/s (current trigger, to be recalibrated) **or** Q_R ≥ X₁ rising for two 12-h steps | Add **central bottom outlet 1**, then **2**, then lateral outlets if needed, until O ≈ 550 − local inflow. Stop at 100 mil. m³ below conservation or at the pre-release floor level | Forecast revised below the trigger and Q_R falling → close in reverse order and hold level. **Abort** (go to Mode 3 cap) if Q_d nears 550 because local inflow arrives early |
| **3 Detention at riverbed capacity** | I ≥ 550 | Hold O = 550 − local inflow. As head rises, keep O constant by trimming galleries or one outlet. Do not let O exceed the cap | Z or (Z, I) reaches the chart boundary → Mode 4; peak passed → Mode 6 |
| **4 Dike capacity (Tier 2a)** | (Z, I, dI/dt) above the "550 curve" of the release chart, starting from about Z ≥ 95.5–96.5 m with I still rising | All bottom outlets, raising O stepwise to 700 | Point above the "700 curve" → Mode 5; peak passed → Mode 6 |
| **5 Dam safety (Tier 2b)** | Point above the "700 curve", **or** Z ≥ 98.20 m and rising, **or** the projected maximum level > 98.70 m | All bottom outlets fully open; **lower flaps bay by bay** (symmetric order agreed with the dam owner) so O follows the chart; O ≤ I on the rising limb. Above 99.50 m everything is open | Peak passed and Z falling → Mode 6 |
| **6 Recession / evacuation** | I falling for two 12-h steps and F3 not rising | **Close in reverse:** raise flaps first (stop spillway flow), then reduce to 700, then 550. Keep O at the highest non-damaging rate until Z ≤ 90.80 m. If F3 or P10 shows another peak, evacuate at 700 where the dikes allow | Z ≤ 90.80 m and no forecast flood → Mode 7 |
| **7 Refill / normal** | — | Recover any pre-release deficit from the recession limb; return to Mode 0 | — |

### The release chart (the Tier 2 tool)

The chart is one figure. For each current level Z and inflow I (and its trend), it gives the minimum total release that keeps the maximum level ≤ 98.20 m (1% curve) or ≤ 99.50 m (0.1% curve), assuming the remaining flood is the *upper envelope* of design hydrographs consistent with the current Z and I.

- It is computed offline by routing the design set from every (Z, I) state.
- It lets operators act correctly without knowing the flood size: a small flood never reaches the curve, and a large flood crosses it early.
- A per-outlet table converts the required O into a gate combination at the current head, using outlet ratings by level.

### Forecast use and fallback

- The 3-day forecast drives Modes 1–2 only.
- Tier 2 is driven by state, so a missed or late forecast costs at most the pre-release volume. It does not compromise dam safety.
- If forecast hindcasts are available, calibrate the Mode 2 trigger as a quantile chosen from hit and false-alarm rates.
  - **Cost of a false alarm:** ≤ 100 mil. m³ of water. Refill time = 100 mil. m³ / (inflow − minimum release); at a 50 m³/s surplus that is ≈ 23 days.
  - **Benefit of a hit:** about 100 mil. m³ of flood space, ≈ 1.2 m of level near the flap crest.
- If the forecast is missing, late, or diverging from Q_R for two steps, operators fall back to state-only triggers. In that case Q_R ≥ X₁ and rising starts pre-release.

## 5. Calibration and testing

1. **Simulator.**
   - 12-h step for routing (as data allow), with a 6-h or finer step inside flood events.
   - Storage curve (resurveyed), per-outlet ratings by level, flap-gate logic, gauge-to-dam routing with lag and attenuation, local inflow, and downstream control point.
   - **Validate on 2008:** feed the reconstructed inflow and the logged gate operations and reproduce the recorded levels.
2. **Baseline.**
   - Encode the current rule (200 m³/s + forecast ≥ 600; hold level for 200–600) and run it on all events.
   - Reconstruct 2008 explicitly: starting level, when outlets opened, and whether downstream flooding came from release above 550 or from local inflow. This separates operating failure from forced outcome.
3. **Parameter search.** Search the triggers (X₁, F3 threshold), the Mode 3→4→5 boundaries and the recession rates by grid or evolutionary search over the design set plus historical events.
   - **Safety is a hard constraint.** The 0.1% set (upper rating band) must stay ≤ 99.50 m. The uplifted 1% set must stay ≤ 98.20 m with O ≤ 550; if infeasible, report the minimum relaxation needed.
   - Only then trade off: duration and volume above 550 and 700, number of gate operations, pre-release water lost, refill probability, energy.
   - Keep the non-dominated set and present it as a short table of three to five candidate threshold sets with their differences.
4. **Tests.**
   - Closed loop: the rule's own releases update the state.
   - Information conditions: no forecast, the actual forecast (hindcast or synthetic errors derived from verification statistics), and perfect forecast as an upper bound.
   - Leave-one-event-out, so the rule is not tuned to 2008.
   - Initial levels above 90.80 m (summer storage).
   - Stress tests:
     - One lateral bottom outlet out of service.
     - One flap gate stuck raised.
     - Loss of power at the galleries.
     - 2010 sequence followed by a 1% peak.
     - 0.1% × 1.2.
     - Both 2008 ratings.
     - Local inflow peaking before, with, and after the routed upstream wave.
5. **Correlated errors.** If forecast errors at successive 12-h steps are correlated (likely), the error of a 3-day volume is understated by assuming independence. For n = 6 steps and ρ = 0.6, the variance is 6σ²(1 + 5×0.6) = 24σ² rather than 6σ², so the SD is twice as large. Use this when setting the Mode 2 trigger quantile.

## 6. Adoption

- **Legal basis.** As far as I know, the operating regulation is issued for the Romanian side by the water administration: Apele Române, through the Prut–Bârlad basin administration that operates the dam. Dam-safety matters go to the national dam-safety commission (CONSIB) and the ministry responsible for waters. Because the dam is shared, the revision also needs agreement with Moldova (Apele Moldovei and the joint Romanian–Moldovan Prut commission). The national hydrology institute (INHGA) and the Moldovan hydrometeorological service supply forecasts. Upstream data come partly from Ukraine. Please confirm these names and the approval route. **The current rule stays the legal basis until the revised rule is approved.**
- **Agree in advance** with the safety authority:
  - The acceptance criteria (the design-case table in Section 1).
  - The climate-allowance interpretation for volume.
  - The decision on the 1% riverbed criterion if it proves infeasible.
- **Trial.** Run the new rule in shadow mode beside the current one for one or two flood seasons, logging what each would have done, before switching.
- **Reversion triggers.** Return to the state-only rule if forecasts are missing or diverging, gates fail, or level or flow measurements are lost. The duty dispatcher decides and the basin flood committee confirms. Log every gate move, its time and its reason.
- **Warnings.** Pre-release and any release above 550 m³/s are man-made flow increases. Romanian and Moldovan emergency services and downstream municipalities must be warned with a fixed lead time before each step. Operators need training on the release chart. Hold an after-event review after every Mode 4–5 event and a formal re-check at the next 10-year revision.

## 7. Key assumptions and what would change the recommendations

- **Outlet ratings and dam head** are assumed (Section 2). If the bottom outlets deliver much less than ~700 m³/s at mid-levels, Tier 2 must start earlier and the flaps carry more of the load.
- **The 0.5 m flap-overflow limit** is assumed to apply to raised gates. If it means something else, for example a limit on any flow over lowered flaps, the dam-safety mode must be redesigned.
- **2008 hydrograph shape and starting level.** If 2008 was long-tailed and started near 90.80 m, the current trigger timing is the main culprit and Tier 1 alone gives most of the gain. If it was compact, the outcome was forced and the debate moves to the 1% criterion and the allowance.
- **Rating outcome.** If repaired ratings support the 4240 m³/s peak, 2008 approaches the old 0.1% peak, and the 0.1% estimate must probably rise beyond the original 4300 m³/s.
- **Forecast skill.** If 3-day hindcasts show high false-alarm rates at 600 m³/s, keep pre-release tied to the observed upstream rise and use the forecast only for alerting.
- **Downstream capacity.** If the riverbed capacity is lower in places, or local inflow below the dam is significant, the 550 m³/s cap must be reduced at the control point and the feasibility test in Section 2 tightens.
