# Round 01 judge evidence for opus and sonnet: C weaknesses and shared gaps

Produced on 2026-10-28 by a Claude Opus 5.5 subagent, which read only `05-round-01/blinding-key.json`, `05-round-01/questions-en.md` and the 28 files in `05-round-01/judgments/{opus,sonnet}/`. The main session saved its returned text here. The haiku results are excluded at the user's request.

C means the answer written with the skill; A means the answer written without it. Tags take the form [model-case-judge].

Error classes:
- E: technical or arithmetic error
- O: omission
- G: governance, approval, pilot or fallback
- S: overclaiming, an unsupported claim, citation or fabrication
- F: form

## Outcomes (from C's side; score = C total vs A total)

| Case | opus j1 | opus j2 | sonnet j1 | sonnet j2 |
|---|---|---|---|---|
| U1 | win clear (40/35) | win (41/37) | win (38/37) | win (38/36) |
| U2 | win (42/39) | win (44/40) | win clear (38/34) | win (40/34) |
| U3 | win (43/39) | win (39/36) | **loss (39/39)** | win (41/40) |
| U4 | win (40/38) | **tie (41/41)** | **loss (37/38)** | win (39/37) |
| U5 | **loss (38/40)** | win (38/37) | win (36/33) | **tie (35/35)** |
| U6 | **loss (42/43)** | win (42/40)\* | win (40/37) | win (40/39) |
| U7 | win (41/39) | win (42/39) | win (39/39) | win (37/36) |

\* The opus-U6-j2 judge cut C's TC score for the figure "48%", which is correct: 1 − 0.987^50 = 0.480.

## Part 1. Weaknesses attributed to C, and points where A was better

### opus

**[opus-U1-j1]**
- (O) Risk combination is right in direction but has no numbers. There is no numeric illustration such as 3 stages × 1% ≈ 3% (1-in-300 per stage), and no arithmetic to check.
- (O) The PMF and seasonal-PMP issue is not raised.
- (O) No named distributions, partition methods or stage-probability allocation rule.
- (G) Not India-specific: no CWC/BIS guideline, Dam Safety Act or rule-curve framing.
- (O) Monsoon onset and withdrawal variability is not treated, so transitions are not trigger-based.
- (O) No transition buffers.
- (O) No check on whether the daily inflow is back-calculated.
- A was better on: the seasonal-PMF and onset cautions, India-specific practice, transition buffers, a floor at the observed maximum, back-calculated inflow noise, decision delays, drawdown-rate limits and an explicit pre-release inequality.

**[opus-U1-j2]**
- (O) The PMF and seasonal-PMP point is weaker ("check flood" only).
- (O) No arithmetic for risk allocation or drawdown time.
- (E, disputed) "Effective lead time minus travel time" is debatable in direction. Judges disagree on this point.
- (G) No Indian regulatory names.
- (O) Transitions are not triggered by onset or withdrawal.

**[opus-U2-j1]**
- (G) No specific regulatory instrument is named; the framework is generic.
- (G) No abort or fallback dispatch rule for a flood that arrives early while drawdown is under way.
- (O/E) The ramp loss and the forecast-error allowance are not stacked.
- (O) The downstream protection standard is only implicit.
- A was better on: a separate downstream protection-standard margin, per-margin sizing guidance (lead-time percentile, N−1 gate), a dynamic control range, downstream users during a sustained release, and listing the design basis of the current level as missing information.

**[opus-U2-j2]**
- (O) The N−1 gate and protection-standard points are underdeveloped.
- (G) No pre-authorised decision protocol to shorten the 8 h chain.
- (O) False-alarm drawdown cost is only implied.
- A was better on: the margins table with a sizing method, sedimentation and ramp-rate limits, a pre-authorised protocol, and night-time and communication failures.

**[opus-U3-j1]**
- (O) The independence effect (3σ²(1+2ρ) vs 3σ²) is not quantified.
- (O) No numeric Monte Carlo standard error.
- (O) No expected annual damage or probability weighting across return periods.
- (O) Uncertainty in the 100-year estimate is omitted.
- (O) Ensembles are not considered as an alternative.
- (O) No arithmetic at all.

**[opus-U3-j2]**
- (O) No numbers at all; no prerelease-volume arithmetic against the 600 Mm³ storage.
- (O) No ensembles; no climate change.
- (G) No emergency action plan; prerelease caps are not named.
- A was better on: quantifying the √3 effect, dependence across issues, timing and shape errors, block resampling, caps, abort and refill, operator override, and EAP updates.

**[opus-U4-j1]**
- (O) No closed-loop simulation concept; no regime change in the training data.
- (O) No optimization or MPC benchmark; no storage-volume calculation.
- (G) Thin on cybersecurity, version control, operator training, EAP updates, downstream warning procedures and an after-action review of 2023.

**[opus-U4-j2]**
- (O) No closed-loop vs open-loop distinction; no regime change.
- (O) No storage-volume estimate; downstream routing is not set up explicitly.
- (O) No simple forecast-informed or MPC benchmark.
- (G) Operator training, EAP, version control, cybersecurity and after-action review are thin.
- A had PR 9 vs 8 for the most complete operating provisions: a hard-constraint layer, version freeze, regulatory mapping, decision rights and training. A also had MPC and perfect-foresight benchmarks and noted leakage through lagged features.

**[opus-U5-j1]**
- (E) Treats evacuating the lower reservoir as losing water "for good", although the occupied storage is flood-control storage that normally should be evacuated.
- (O/G) Does not frame the occupied storage as flood-pool water above the flood-limited level, which the rules require evacuating.
- (E) The catch-up rate is overstated (3,500–4,000 vs about 3,200–3,400 m³/s).
- (G) No readiness checks for gates, power or staff; no head-dependent capacity check; no decision log; no prohibition on drawing into conservation storage.
- (S) "Lower drawdown has a real water cost" is mildly unsupported.
- Note: opus-U5-j2 takes the opposite view of the lower reservoir's role.

**[opus-U5-j2]**
- (E) The catch-up release is overstated.
- (E) "Roughly 5,500 or less" is loose.
- (O/G) The flood-limited-level and rule-compliance angle is missing.
- (G) Less on gate, power and staff readiness and on head-dependent discharge capacity.

**[opus-U6-j1]**
- (O/F) No difference table and no statement that the four options are mutually non-dominated.
- (O) Needed sample size is not quantified.
- (O) No back-to-back floods or surcharge/spillway use.
- (O) Does not show how a contractual 90% irrigation minimum changes the picture.
- (G) No upstream stakeholders.
- (O) No sediment.
- (G) No statutory approval procedure for the flood-limited level; no example triggers.
- (S) The mechanism reading is speculative.

**[opus-U6-j2]**
- (E, wrong accusation) "48% should be 52%". The judge is wrong.
- (O/G) No back-to-back floods; no upstream backwater.
- (S/O) "Costs possibly within error" is stated without a calculation.

**[opus-U7-j1]**
- (O) Travel time is guessed ("about a day") rather than estimated.
- (O) Does not note that tributary inflow can reach the station before the release does.
- (E/O) The cost of the conservative terminal condition is untested.
- (O) The effect of tree reduction on CVaR from about 16 branches is not discussed.

**[opus-U7-j2]**
- (O) No reliability check of the tool's own risk statements.
- (O) Does not say that 20 years hold few extremes.
- (O) The pre-release bound is not written as a quantity.
- (O/G) No partial-gate-outage scenario; less on the operator what-if UI.

### sonnet

**[sonnet-U1-j1]**
- (O) Seasonal risks are not combined into the annual standard.
- (O) No worked drawdown-time calculation.
- (E/design) No stage may sit below today's FLWL, which rules out a lower core-season level.
- (G) No Indian regulatory bodies.
- (O) No degraded-gate test.

**[sonnet-U1-j2]**
- (O) The time ceiling is not turned into a drawdown formula; no ΔV/ΔQ expression.
- (F) A sentence is garbled.
- (E/design) Every stage stays at or above the current FLWL.
- (G/O) No Indian specifics, no gate-out test and no limit on release ramp rate.

**[sonnet-U2-j1]**
- (E) 690 should be about 675 m³/s.
- (E) The direction of the area–level relation is wrong.
- (F) A garbled item; a muddled sentence on risk tolerance.
- (S) The 16 h planning case is arbitrary.
- (O) Does not ask whether the 36 h lead refers to the peak or to the start of the rise.
- (O) No drawdown-rate limits for slopes and banks; no measurement or wave allowance.

**[sonnet-U2-j2]**
- (E) 690 should be about 675.
- (F) A garbled sentence.
- (O) The deadline when inflow exceeds the allowable release is not stated sharply.
- (O) No drawdown-rate limits; no measurement allowance.
- (S) The 16 h case is asserted, not derived.
- (G) Regulatory discussion is generic.

**[sonnet-U3-j1]** (C lost)
- (O) Independence is not quantified; no arithmetic.
- (O) Misses hindcast vs operational forecasts, in-sample tuning and forecast-system versions.
- (O) No event or year block bootstrap.
- (O) No timing-error component.
- (G) No pre-agreed acceptance criteria, shadow mode or revert triggers.
- (S) Vague "papers have reported".

**[sonnet-U3-j2]**
- (O) No hindcast vs operational distinction and no parameter uncertainty.
- (O) No in-sample tuning check.
- (O) Nothing is quantified.
- (S) Uncited "papers".
- (G) Less specific on revert triggers, criteria and shadow operation.

**[sonnet-U4-j1]** (C lost)
- (O) No storage-volume check; does not ask whether the 2023 peak was already within safe channel capacity; no calculation.
- (O) The training-label issue is hinted at but not settled.
- (O) No simple-heuristic or MPC baseline to isolate the ML contribution.
- (G) Generic pass/fail thresholds; less concrete exclusion conditions, deviation bands and in-season change control.
- (S) "Papers in this field show".

**[sonnet-U4-j2]**
- (S) Unsupported "papers in this field".
- (G) Less concrete in-season provisions (exclusion thresholds, no silent retraining).
- (O) No quantitative storage check.

**[sonnet-U5-j1]**
- (E) 47 should be about 56 M m³.
- (O) The coincidence check is only a rule of thumb.
- (G) Little on warning the city and emergency services.
- (E/logic) "Reduce or stagger upper release" is not reconciled with the upper reservoir's storage shortage.
- (O) No upper-dam safety check.

**[sonnet-U5-j2]** (tie)
- (E) The "shortfall" framing implies the upper reservoir must store the whole volume.
- (O) Peak routing is not settled.
- (E) 47 vs 56, and loose catch-up figures.
- (S) Assumes refill is possible in the flood season.
- (G) No public warning for raised releases; no interim forecast request.
- (O) No storage or routing verification at the lower dam.

**[sonnet-U6-j1]**
- (O) No return-period or horizon-risk computation; no binomial SE.
- (O) Less depth on parameter and tail uncertainty and on non-market valuation.
- (G) Thin public participation.
- (G) Formal approval of the flood-limited level is not named.

**[sonnet-U6-j2]**
- (O) No return-period conversion or cumulative risk; B is not tested against the design standard.
- (O) No tolerance test (upper bound of the difference).
- (G) Less on formal approval and override authority.
- (O) No dry-year or seasonal timing metrics.
- (F) Carries both A and B forward without saying which to prioritise.

**[sonnet-U7-j1]**
- (S) Twice cites "papers" with no source.
- (E/O) The convexity condition is imprecise.
- (G) No automatic envelope-rejection rule.
- (O) No numeric travel-time bound.

**[sonnet-U7-j2]**
- (O) No travel-time, LP-size or cycle-count estimate.
- (O) Does not note that the residual tributary estimate absorbs routing and rating error.
- (G) No per-cycle audit log.
- (S) Uncited "papers".
- (O/G) No "do-no-harm" limit on pre-release.

## Part 2. Points neither answer had (summary)

- **Worked numbers:**
  - 1−(1−p)^n for stages or years
  - drawdown volume and time
  - travel time (distance / celerity)
  - MC SE ≈ 0.003 at n = 5,000
  - binomial SE ≈ 1.6 pp in 40 years, with one failure year = 2.5 pp
  - horizon risk (39% vs 48%)
  - storage cost of a claimed peak reduction (ΔV ≈ ∫ΔQ dt)
  - LP size and cycle count
  - prerelease scale against total storage
- **Approval:**
  - the named authority and instrument (India: CWC/BIS/NDSA/Dam Safety Act; China: annual flood-control dispatch plan, dynamic FLWL procedure, demonstration report)
  - the current rule stays the legal basis until approval
  - the competent authority alone can change the standard
  - liability for false pre-releases
- **Safeguards:**
  - explicit fallback and abort, with reversion triggers
  - a pre-authorised decision protocol
  - warnings for man-made rises
  - ramp-down and reversal criteria
  - audit
- **Dam safety:**
  - route the design, check and PMF floods from the raised level
  - release capacity above the current level
  - characteristic levels
  - the upper reservoir's surcharge as a hard trigger
- **Prerelease harm:**
  - false-alarm economics
  - cap prerelease at what can be refilled under a low-side forecast
  - "do not exceed the natural peak" (no induced flood)
  - asymmetric consequences
- **Rare events:**
  - few independent extremes in short records
  - pooled or regional tails
  - minimum detectable difference
  - detection power of triggers
- **Forecast:**
  - hindcast ensemble size and configuration that match the operational system
  - PIT/CRPS verification at high flows
  - an interim forecast request
  - two forecast updates as a decision tree with a point of no return
- **Cascade (U5):**
  - flood-pool storage above the FLWL is normally required to be evacuated, and refill does not apply in flood season
  - coincidence of upper and tributary storms from the same source
  - upper-dam safety
- **Baseline (U4):** whether the operators' 2023 peak was forced; whether it exceeded the safe discharge; the starting level.

## Part 3. Recurring themes (count = model-case combos out of 14)

| # | Theme | Count |
|---|---|---|
| 1 | No back-of-envelope number where the data allowed one (missing only in U2) | 12 |
| 2 | Formal approval route not named | 13 |
| 3 | Operating safeguards (fallback, abort, shadow, pre-agreed criteria, readiness, audit, warnings) not concrete | 13 |
| 4 | Downstream timing and coincidence (travel time, tributary or local inflow, control-point check) not worked out | 9 |
| 5 | Statistical resolution of rare events ignored | 8 |
| 6 | Dam-safety or design-flood checks from the raised level missing | 8 |
| 7 | Harm from the prerelease itself not costed | 7 |
| 8 | Verification design incomplete (benchmarks, out-of-sample, closed-loop, tolerance or worst-case test) | 6 |
| 9 | Hardware and operating constraints thin (N−1, ramp and drawdown rate, gated rating, readiness, measurement) | 6 |
| 10 | Arithmetic slips (opus-U5, sonnet-U2, sonnet-U5), plus 1 false accusation (opus-U6-j2) | 3 |
| 11 | Conceptual or framing errors (opus-U1-j2 disputed, opus-U5-j1, sonnet-U1, sonnet-U5) | 4 |
| 12 | Forecast-skill characterisation missing (hindcast vs operational, ensemble size, probabilistic verification) | 5 |
| 13 | Staged or dynamic seasonal limits not proposed as an option | 5 |
| 14 | Assertions without derivation | 4 |
| 15 | Uncited "papers" (all sonnet) | 3 |
| 16 | Counterfactual baseline or benefit mechanism not explained (initial level, forced operator action, head vs volume) | 3 |
| 17 | Form: garbled sentences, no difference or non-dominance table, decision not prioritised | 4 |

No judge flagged leaked labels, a generic checklist, a buried answer or excessive length for opus or sonnet.

## Part 4. Why C lost or tied on U3–U6

- **opus-U3:** C won both judgments. Its remaining gaps were no quantification, no MC SE and no storage arithmetic.
- **sonnet-U3:** 39/39 in j1, where A won on concrete governance (criteria, shadow, revert triggers) and on hindcast vs operational, timing errors, in-sample tuning and block bootstrap. C was marked down for uncited "papers". C won j2. Effectively a coin flip.
- **opus-U4:** C won j1 and tied j2. A matched C on governance breadth, closed-loop simulation, regime change and an MPC benchmark. Neither answer computed the storage volume.
- **sonnet-U4:** In j1, A won KQ and PR with an MPC baseline, exclusion conditions, deviation bands and no silent retraining. C had generic thresholds, no storage check and "papers". C won j2.
- **opus-U5:**
  - Both judges flagged the overstated catch-up rate.
  - j1 penalised treating the lower reservoir's flood-pool water as kept, which conflicts with the rule-mandated evacuation, and also penalised missing readiness checks.
  - j2 took the opposite view. The judges contradict each other on the central point.
- **sonnet-U5:** In j2, C had the "shortfall" framing, the 47 vs 56 slip, assumed refill, no public warning, no interim forecast and no storage check, which led to a tie.
- **opus-U6:** In j1, A won KQ and CA with a difference table, non-dominance, back-to-back floods, surcharge, the contract edge case, upstream residents and sediment. In j2, C won even though its correct figure was wrongly penalised.
- **sonnet-U6:** C won both. Its remaining gaps were no return-period or horizon risk, no binomial SE, no test against the standard, formal approval less explicit, and both A and B carried forward without saying which to prioritise.
