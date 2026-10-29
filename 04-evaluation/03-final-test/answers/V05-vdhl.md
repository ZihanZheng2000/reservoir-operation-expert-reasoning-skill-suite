# Stânca–Costești: Revised Design Floods and Outlet-Level Flood Operation — Study Design

## 0. Framing and provisional position

The question has two coupled parts:

1. **Hydrological:** what flood loads (peak, volume, hydrograph shape, and their joint probability) should the reservoir now be planned for?
2. **Operational:** given those loads, a 3-day warning, and several independently operated outlets, how should each outlet be operated to (a) never endanger the dam and (b) keep downstream flooding as low as possible?

They have to be studied together. The 2008 event shows that **volume**, not only peak, is the binding load: about 1100 mil. m³ arrived against a 665 mil. m³ flood-control volume. So the design floods must be described as hydrographs with a joint peak–volume probability, not as peaks alone. The operating rules must also be tested on those hydrographs, not on one design hydrograph.

**Provisional judgments (to be confirmed or revised by the study):**

- The original design floods are probably **non-conservative**. A single 43-year record that contains an event about 15% above the original design peak, with a volume of about 1.65 times the flood-control volume, strongly suggests that the original estimate of the upper tail was too low, or that the hydrological regime has changed. I expect the revised design peaks and especially the design volumes at the dam-safety return periods to go up. The size of the change is unknown until the rating-curve problem is resolved, because the high-flow values that drive the tail are exactly the uncertain ones.
- The design basis should have **two tiers**. (i) A *downstream-protection* tier: floods the reservoir should attenuate to a safe downstream release (order of a 1%-AEP event, to be set by the applicable Romanian/Moldovan standards and the downstream consequences). (ii) A *dam-safety* tier: floods the dam must pass without overtopping or structural distress (the design and check floods required for the dam's importance class, typically in the 0.1%–0.01% range, plus a PMF-type or stress-test check). The 2008 event should be a **mandatory stress test** whatever return period is assigned to it.
- Operationally, I expect the answer to be a **staged, forecast-informed rule**: pre-release during the 3-day lead time; a downstream-protection mode that holds the total release at or below the safe channel capacity while storage remains; and a dam-safety mode, triggered by reservoir level and inflow trend, that increases the release toward inflow. A firm constraint applies throughout: **outflow must not exceed inflow on the rising limb**, so the dam never makes the flood worse than it would have been without it. Each outlet then gets a sequence and opening schedule chosen by its hydraulic efficiency, its safe operating range, and the energy-dissipation limits.
- If, even with optimal operation, the revised dam-safety flood cannot be passed with adequate freeboard, the study must say so plainly. Better operation alone may not be enough, and **structural or allocation changes** may be needed: more discharge capacity, flap-gate or crest modifications, or a larger seasonal flood-control allocation. The study should be able to reach that conclusion rather than assume it away.

### Key assumptions (stated, not known)

- Reservoir level records, gate-opening logs and outlet discharge data exist for at least the 2008 event and ideally for other large events. Some reservoir operating data exist for 1978–2020.
- The dam's stage–storage curve and per-outlet rating/design data are available from the operator, although they may be outdated (sedimentation since 1979).
- Topography/bathymetry of the downstream Prut valley is available or can be obtained for hydraulic modelling.
- Both riparian states' operators and authorities (Romania and the Republic of Moldova) will take part. The operation of a border dam is a joint decision.
- Applicable dam-safety classification rules (Romanian norms and the joint commission's rules) set the required return periods. I do not assume specific numbers beyond the typical ranges above.
- The "upstream gauge" measures most of the reservoir inflow. If there is a significant ungauged lateral inflow between the gauge and the dam, it must be estimated (see §1.3).

---

## 1. Work Package 1 — Fix the data foundation (inflow series and rating-curve uncertainty)

Everything downstream depends on the high-flow values, so this comes first.

### 1.1 Re-examine the high-flow rating curve
- Gather all gaugings at the upstream station, the history of rating-curve changes, cross-section surveys, and any post-flood surveys (high-water marks, 2008 trash lines).
- Build a **hydraulically constrained rating curve with uncertainty** for the high-flow range, for example a Bayesian rating-curve approach that combines a hydraulic control model (section/channel control, overbank activation) with gaugings. Optionally add a local 1D/2D hydraulic model of the gauge reach, calibrated to measured gaugings and run to stage levels above the highest gauging. The result is a **set of plausible rating curves** (posterior samples), not one corrected curve.
- Look for rating shifts over time (bed changes) and for hysteresis on fast floods.

### 1.2 Independent check from the reservoir water balance
The dam itself is a second "gauge". For large events:

Inflow(t) ≈ Outflow(t) + ΔS(t)/Δt, where S comes from reservoir level through the stage–storage curve, and outflow comes from gate openings and the outlet ratings.

- Reconstruct inflow hydrographs for 2008 and other large events this way, with uncertainty from level noise, the storage curve (sedimentation), outlet ratings, wind setup, and evaporation (negligible during floods).
- Compare these with the gauge-derived hydrographs. **Volume** agreement is the strongest test of the rating curve's high-flow branch, because volumes are less sensitive to level noise than instantaneous values.
- Where the two disagree, use the reconciled series and carry the remaining disagreement into the uncertainty.

### 1.3 Lateral inflow and the travel time from gauge to reservoir
- Estimate the ungauged intermediate catchment contribution, for example with area/rainfall scaling or a calibrated rainfall–runoff model. It also shapes the inflow hydrograph that the operating rules see.
- Estimate the gauge-to-reservoir travel time. It adds to the effective warning time.

### 1.4 Extend information beyond 43 years
- Historical (pre-1978) flood information: documentary records, flood marks, and earlier gauge data on the Prut and its tributaries, if they exist. Even censored information of the form "exceeded level X in year Y" adds a great deal of tail information.
- Regional information: other Prut/Siret/Dniester-region gauges for a regional or index-flood analysis, and to check whether the 2008 event was regionally extreme.
- Upstream reservoirs or land-use changes in the basin (Ukrainian portion of the Prut): check whether the regime is homogeneous. I do not assume such changes exist; I only check.

**Deliverable WP1:** a reconciled inflow series at the dam, 1978–2020, with an ensemble or uncertainty bands at high flows, plus a documented set of large-event hydrographs.

---

## 2. Work Package 2 — Design flood estimation (peaks, volumes, hydrographs)

### 2.1 Event extraction
- Extract annual maxima and peaks-over-threshold events. For each, record the peak Q, the flood volume above a base (and volumes over fixed durations, e.g. 1, 3, 5, 10, 15 days), and the duration.
- Look at seasonality (spring snowmelt+rain versus summer convective/frontal events). The 2008 event was a summer event. If the flood types are distinct, analyse them separately (mixed populations), because they differ in volume–peak relationships and in forecastability.

### 2.2 Stationarity and trend checks
- Run Mann–Kendall/Pettitt tests on peaks and volumes. Given 43 years and one dominant event, these tests have little power, so treat them as diagnostics, not proof.
- Fit non-stationary variants only if they are justified physically (climate signal, land-use change). Otherwise represent climate change through sensitivity scenarios (§2.6).

### 2.3 Univariate frequency analysis with full uncertainty
- Fit candidate distributions (GEV, Pearson III/log-Pearson III, as conventional in the region) to peaks and to N-day volumes, using Bayesian or L-moment methods.
- **Propagate the rating-curve uncertainty.** Repeat the fit for each sample of the rating-curve ensemble (or fit jointly). Report quantiles with credible intervals that combine sampling, distribution choice and rating uncertainty.
- Include historical/censored information where available. Use regional priors on the shape parameter, because a 43-year at-site record cannot pin down the 0.1%–0.01% tail.
- Explicitly place 2008 in the fitted distribution, with its uncertainty. If it falls at an implausibly rare return period, that points to a distribution or regime problem, not to "a freak".

### 2.4 Joint peak–volume analysis
- Fit a bivariate model (copula) for peak and flood volume, or for peak and critical-duration volume.
- What matters for a reservoir is the **joint** exceedance. Many (peak, volume) combinations share the same "return period", and the most dangerous one for the dam is not necessarily the one with the highest peak. Use the **reservoir response** (maximum level, maximum release) to choose among them. In other words, define the design event by its consequence (a "structure-based" return period) rather than by a peak-only or volume-only return period.

### 2.5 Design hydrograph sets
- Build sets of synthetic hydrographs: scaled observed shapes (2008 and other large events), with shapes varied by flood type, and multi-peak sequences such as back-to-back events. The last matter because the reservoir may not empty between peaks.
- Alternative or complement: **continuous stochastic simulation**, i.e. a weather generator plus a calibrated rainfall–runoff model for the Prut upstream of the dam, producing thousands of years of synthetic inflow. These are routed through the reservoir, and the frequency of maximum reservoir level and maximum downstream release is derived directly. This avoids assuming the return period of the event equals the return period of the response, and it captures antecedent conditions and multi-peak events naturally. Resources permitting, this is the method I prefer for the dam-safety tier, cross-checked against the event-based approach.

### 2.6 Upper-bound and climate stress tests
- PMP/PMF-type estimate, or the extreme-flood estimate required by the national dam-safety norms.
- Climate-change scenarios: delta-change or scaled-precipitation sensitivity (e.g. +10/+20% extreme precipitation) to see whether the conclusions are robust, rather than to make one projection.
- A "2008 plus X%" scenario as an intuitive stress test for stakeholders.

### 2.7 Choosing the design floods (the judgment)
- Tier A (downstream protection): the AEP up to which the reservoir should keep the release at or below the safe downstream discharge. It is set from downstream damage and consequence analysis (WP4) and from the standards.
- Tier B (dam safety): design and check floods by dam class, characterised as a family of critical hydrographs with uncertainty. For a border dam with large populations downstream, use an **upper credible bound** of the quantile, not the median, at the dam-safety tier. The 2008 event's evidence of a heavier tail than assumed justifies this.
- Report how much the conclusion depends on the rating-curve choice. If the uncertainty band straddles a decision threshold (e.g. whether existing discharge capacity is adequate), say so and recommend measures that reduce it: gaugings at high flow, a new gauge section, or ADCP campaigns during the next flood.

**Deliverable WP2:** a set of design hydrographs (Tier A, Tier B, stress tests) with probabilities and uncertainty, and a short note comparing them with the original design values.

---

## 3. Work Package 3 — Reservoir and outlet system model

### 3.1 Storage and geometry
- Update the stage–storage(–area) curve with a new bathymetric survey if the last one is old. About 40+ years of Prut sediment can noticeably reduce the flood volume available.
- Fix the operating levels: normal retention level, flood-control band, flap-gate crest, maximum allowable flood level, dam crest, required freeboard (wind, waves, settlement).

### 3.2 Per-outlet hydraulics
For every bottom outlet, gated weir bay and flap gate:
- Discharge as a function of reservoir level and gate opening (orifice flow or free/controlled weir flow, and the transition between them), including tailwater effects.
- **Operating constraints:** minimum and maximum openings; ranges where cavitation, vibration or gate instability occur (often at small partial openings of high-head bottom outlets); opening and closing speeds; times to operate; power supply and backup; whether the gates can be operated once the reservoir is above the flap gates (2008 situation).
- Energy dissipation: capacity of the stilling basins per outlet group, the risk of scour, and asymmetric-release effects on the downstream channel and the dam toe (spreading flow across bays versus concentrating it).
- Turbine flow, if the hydropower units can contribute during floods, and when they must trip (high tailwater).
- **Reliability:** probability that a gate is unavailable (maintenance, mechanical/electrical failure, debris). Use an "n-1" (one largest outlet unavailable) test.

### 3.3 Verification against 2008
- Replay 2008 with the recorded gate openings and the reconstructed inflow. Check whether the model reproduces the observed reservoir levels and releases. This is the main validation of the outlet ratings and storage curve at extreme levels, including flow over the flap gates.

**Deliverable WP3:** a validated reservoir-routing model with per-outlet hydraulic and operational constraints.

---

## 4. Work Package 4 — Downstream consequence model

- Build a 1D/2D hydraulic model of the Prut downstream of the dam, as far as the relevant flood-prone reaches (on both banks; levees, settlements, infrastructure), including tributary inflows below the dam.
- Calibrate it to 2008 (observed levels and inundated areas) and to other events.
- Derive a **staged set of downstream thresholds**: the discharge at which flooding starts (bankfull or levee-safe capacity), discharges at which significant damage zones are activated, and the levee overtopping or breach threshold. These become the release targets and limits in the operating rules.
- Set the damage/consequence functions per discharge (economic damage, people exposed). Agree them with both countries' authorities, since the costs fall on both banks.
- Check the **rate of change** of releases (ramping) for bank stability and for the safety of people downstream.
- Check the coincidence of downstream tributary peaks with reservoir releases.

**Deliverable WP4:** a release-to-consequence mapping, and safe release limits as a function of the downstream tributary state.

---

## 5. Work Package 5 — Forecasts and the 3-day lead time

- Assess the skill of the forecasts actually available: hydrological forecasts for the gauge and inflow, meteorological ensembles. Use hindcasts or reforecasts over past events if they exist. Quantify volume and peak errors as a function of lead time (24/48/72 h).
- Add the gauge-to-dam travel time to find the true usable lead time.
- **Pre-release capacity calculation:** how much storage can be evacuated in 72 h through the available outlets while keeping the downstream release at or below the safe limit (minus tributary flows). This sets how much "extra" flood volume the forecast is worth. Given the 2008 volume deficit (about 435 mil. m³ above the flood-control volume), this number is central: if pre-release in 3 days can only free a small fraction of that, then operation alone cannot handle a 2008-type event without exceeding downstream limits, and the trade-off moves into the dam-safety mode.
- Build a **forecast-error model** (e.g. an ensemble of plausible forecasts conditioned on the actual future hydrograph) for testing the rules. Rules must not rely on perfect forecasts.
- Consider the cost of false alarms. Pre-release that turns out unnecessary costs water supply, irrigation and hydropower storage. Check the refill probability after pre-release.

---

## 6. Work Package 6 — Operating policy design and optimisation

### 6.1 Policy structure (proposed)
An operating regime with clear, auditable stages, driven by the reservoir level, the inflow and its trend, and the forecast:

| Stage | Trigger (to be calibrated) | Objective | Release logic |
|---|---|---|---|
| 0 Normal | No warning | Water uses | Conservation rule |
| 1 Pre-release | Forecast exceeds an inflow/volume threshold within 72 h | Create storage | Release up to the safe downstream limit (allowing for tributaries), ramp-limited, using the most efficient outlets |
| 2 Downstream protection | Flood arrives, level within the flood-control band | Minimise downstream damage | Hold total release at the downstream-safe target, or step it through damage thresholds; store the rest; outflow ≤ inflow |
| 3 Dam safety | Level, or projected level (from inflow trend and forecast volume), crosses the safety trigger | Protect the dam | Increase release progressively toward inflow; all outlets available; accept downstream damage; outflow still ≤ inflow on the rising limb |
| 4 Recession | Inflow falling | Evacuate flood volume for the next event | Release at the highest downstream-safe rate until the flood-control volume is restored |

Key design choices the study must resolve:
- **The dam-safety trigger level and its "look-ahead" form.** A purely level-based trigger reacts late. A trigger based on projected storage (current storage + forecast remaining volume − achievable release) acts earlier and so lowers the peak release. Its exact form must be optimised and checked for robustness to forecast error.
- **Graduated rather than abrupt transition** between Stage 2 and Stage 3. An abrupt switch from "hold safe release" to "release = inflow" creates a downstream surge that is worse than a gradual rise.

### 6.2 Outlet allocation (the "how should each outlet be operated" part)
Given the total target release Q*(t) from the policy, allocate it among the outlets by solving a small constrained problem at each step (which can then be turned into tables):
- Use outlets within their **safe opening ranges**, and avoid cavitation/vibration zones (e.g. open bottom outlets fully or keep them closed rather than holding small partial openings, if the hydraulics require it).
- **Sequence:** typically bottom outlets first for early pre-release (high discharge at low head, which is useful when the level is still low), then weir bays as the level rises and weir capacity grows. Keep reserve capacity in the gated weir bays so that a dam-safety increase is possible. Account for turbines where usable.
- **Symmetric and distributed** openings to protect the stilling basins and avoid concentrated jets and scour.
- **Respect gate-movement speed and staff/power constraints**, i.e. how many gate movements are physically feasible per hour.
- **Hold reserve against gate failure:** the rule must still work with the largest outlet out of service.
- **Flap gates:** define the operation explicitly (when they are lowered, and the status of the weir bays when the level exceeds them, as in 2008) so that they are not an improvised last resort.

The result is a set of **outlet operating tables**: for given reservoir level and target release, which outlets to use and at what openings, plus a gate-change sequence.

### 6.3 Optimisation and evaluation method
- **Simulation–optimisation:** parameterise the policy (trigger levels, pre-release thresholds, release targets per stage, ramp rates) and optimise with a multi-objective algorithm (e.g. NSGA-II/Borg) over the design hydrograph sets and the stochastic series. Objectives: minimise maximum reservoir level (or the probability of exceeding the safety level), minimise downstream damage or the peak release above thresholds, and minimise loss of conservation storage from false-alarm pre-release.
- **Benchmark with perfect-foresight optimisation** (deterministic DP/LP per event). This shows the theoretical best and how much of the gap is due to the rule structure versus forecast uncertainty.
- **Model predictive control (MPC)** as a real-time alternative: re-optimise the releases every few hours on the ensemble forecast. Compare it with the rule-based policy. If MPC is markedly better, recommend it as a decision-support tool, with the rule tables kept as fallback and default.
- **Robustness testing:** forecast errors, rating-curve uncertainty in the inflow, gate outages, back-to-back floods, starting levels (reservoir full at the start of the flood season versus normal), downstream tributary peaks, and climate scenarios. Pick the policy that performs acceptably across the scenarios (e.g. a regret or satisficing criterion), not the one optimal for a single scenario.
- **The 2008 replay** with the new policy and the realistic forecast available at the time, compared with the actual operation. This is the most convincing demonstration for operators.

### 6.4 Outcome categories the study must be able to report
- (a) The revised design floods can be handled with adequate freeboard by improved operation alone.
- (b) They can be handled only with forecast-based pre-release, so forecasting and communication become safety-critical.
- (c) They cannot be handled without exceeding dam-safety limits, so structural options (more spillway/outlet capacity, crest raising, flap-gate modification) or a larger seasonal flood-control allocation must be evaluated (at screening level), with their cost to water uses.

---

## 7. Work Package 7 — Institutional and implementation aspects

- The operating rules must be agreed by both countries (joint Romanian–Moldovan management). Define who decides each stage transition, the communication protocol to downstream authorities on both banks, and warning lead times for evacuation.
- Turn the results into an **operating manual**: stage triggers, outlet tables, gate sequences, ramp limits, and contingency procedures (loss of power, loss of communication, gate failure).
- Train operators and run a table-top exercise using a synthetic event bigger than 2008.
- Set a **monitoring programme**: high-flow gaugings at the upstream gauge, periodic bathymetry, gate condition testing, and post-event review with re-estimation of the design floods after each major flood.

---

## 8. What would confirm or change the provisional judgments

| Provisional judgment | Confirmed if | Changed if |
|---|---|---|
| Design floods should go up | Reconciled inflow (rating plus water balance) confirms the 2008 volume and peak; at-site and regional analysis puts the upper tail above the original design | Water balance shows the gauge strongly overestimated high flows, and the 2008 volume and peak shrink substantially; or historical/regional data show 2008 was consistent with the original design tail |
| Volume is the binding load | Reservoir response is more sensitive to volume than to peak across the hydrograph set | Short, sharp hydrographs drive maximum level due to limited discharge capacity at mid-levels |
| Staged forecast-informed rule with pre-release is worthwhile | Forecast skill at 48–72 h is adequate and pre-release capacity in 3 days frees a meaningful share of the volume deficit without exceeding downstream limits | Forecast skill is poor, or downstream limits are so low that pre-release frees little storage. Then the emphasis shifts to dam-safety triggers and structural or seasonal-allocation options |
| Operation alone may not suffice for the dam-safety tier | Simulated optimal operation still exceeds the safety level or freeboard for the Tier B flood | Optimal operation keeps adequate freeboard under the upper credible bound and n-1 gate availability |
| Outlet sequence (bottom outlets early, weir bays later, reserve held) | Hydraulic and structural constraints confirm the efficiency ordering and safe ranges | Cavitation/vibration, stilling-basin or scour limits make a different allocation safer |

---

## 9. Summary of outputs

1. A reconciled inflow series with high-flow uncertainty, and a revised rating curve.
2. A revised design-flood set (downstream-protection tier, dam-safety tier, stress tests including 2008 and climate scenarios), expressed as hydrograph families with joint peak–volume probabilities and uncertainty.
3. A validated reservoir and outlet model and a downstream consequence model.
4. A staged, forecast-informed flood-operating policy with per-outlet tables and contingency rules, tested for robustness to forecast error, rating uncertainty and gate failure.
5. A clear statement of whether operation alone is sufficient or whether structural or allocation changes must be considered.
6. An operating manual and monitoring programme for joint binational use.
