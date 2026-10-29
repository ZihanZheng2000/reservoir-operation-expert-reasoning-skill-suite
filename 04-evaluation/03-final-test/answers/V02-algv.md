# Study design: real-time hourly release scheduling for long floods at Daecheong Reservoir

## 1. How I read the problem

The brief has four features that drive the design:

1. **Very small flood-control storage.** It fills in about 6.5 hours at the 200-year inflow. Mistakes cannot be absorbed, and the main lever is when releases start and how high they go *before* storage is needed, not storage alone.
2. **Forecast horizon (6 h) much shorter than the event (more than 8 days, 1 to 3 peaks).** The 6-hour forecast is about as long as the time needed to fill the flood pool. It can guide the next step but cannot tell you whether a second or third peak is coming. A long flood is a sequence of decisions: how much to draw down between peaks so that space is ready for the next one, without releasing more than downstream can take and without ending the event with an empty conservation pool.
3. **Operators already use a receding-horizon practice.** Every hour they issue a multi-hour schedule and carry out only its first step. That is model predictive control (MPC) done by hand. So the natural formal tool is MPC, and it matches how operators already think.
4. **Acceptance matters as much as performance.** Operators rarely use optimisation tools. Schedules that jump around, change every hour, or reverse direction will not be used, however good their objective values. Acceptance has to be designed in, as constraints and as an evaluation outcome, not added afterwards.

So the research question breaks into three sub-questions:
- **RQ1 (control):** Which real-time scheduling scheme controls long multi-peak floods best, given only 6 h of rainfall forecast?
- **RQ2 (acceptability):** Which properties of a schedule make operators accept it, and how much flood-control performance does it cost to impose them?
- **RQ3 (robustness):** How do the schemes hold up under forecast error and under floods larger than the three in the record, up to the 200-year design level?

## 2. Assumptions (to be confirmed with the operator and data owner)

- Hourly storage, outflow and derived inflow exist for the 2016, 2018 and 2020 floods, as the brief states. I assume archived rainfall observations exist for the same periods. Whether archived 6-hour rainfall forecasts exist is **unknown**, and the design handles both cases (Section 4.3).
- Operating limits can be obtained from the operator: normal high water level, flood-season limited level, design or maximum flood level, safe downstream discharge(s), gate and turbine capacities, allowed ramp rates, and any notification rules for release increases. I do not assume any values.
- Downstream flood risk can be represented by a few control points (the dam outflow itself, plus any downstream gauges the operator uses). If there are significant local tributary inflows below the dam, I would need a simple routing to those points. Whether this is needed is a scoping question for the operator.
- Upstream regulation, if any, enters as part of the observed inflow. I would not model other dams explicitly unless the operator coordinates with them hourly.
- The study gives decision support. Final decisions stay with the operator.

## 3. Phase 0: Elicit objectives and acceptability criteria from operators (before any modelling)

This step matters most for the "acceptance" half of the question, and it should come first.

- **Structured interviews and a workshop** with duty operators and supervisors (target 5 to 10 people). Use the three historical floods as prompts: "At hour X you held the release at Y. Why? What would have made you change it?"
- Elicit and rank:
  - **Hard constraints:** dam safety level, maximum release, ramp limits, minimum release for in-stream flow.
  - **Priorities:** dam safety, then downstream flood damage, then refill for water supply, then hydropower. Confirm this order rather than assume it.
  - **Acceptability properties.** Candidates to test: how often the release changes; minimum hold time between changes; size of steps (gate increments); rate of increase versus rate of decrease; no up-down-up oscillation; schedule stability (how much the hour-t+1 schedule differs from the hour-t schedule over the overlapping hours); advance notice before releases rise downstream; and whether the logic can be explained to supervisors and the public afterwards.
- **Reconstruct the implicit historical policy.** Code the observed release decisions against the state (level, inflow, inflow trend, forecast rain, time of day). This gives (a) the baseline, and (b) evidence of what operators actually do, as opposed to what the manuals say.

**Output:** a written objective hierarchy, a list of hard and soft constraints, and a quantitative acceptability specification (for example, at most N changes per 24 h, ramp of at most R m³/s per hour, a minimum hold of H hours). The operators sign this off before algorithm development starts. Without it, "acceptance" cannot be tested.

## 4. Phase 1: Data and simulation testbed

### 4.1 Data preparation
- **Quality-check the derived inflow.** Inflow back-calculated from storage changes is noisy at hourly resolution: level-sensor noise, wind set-up, and errors in the level-storage curve can produce spurious spikes or negative inflows. Check the mass balance, apply a light smoothing that conserves volume, and record every correction. Keep raw and cleaned series separate.
- Check that the outflow series covers all pathways: spillway, turbines and any intake withdrawals.
- Characterise each event: duration, number of peaks, peak and volume, time between peaks, and the antecedent storage at the start.

### 4.2 Reservoir and downstream model
- An hourly mass-balance model using the official level-storage-area relation and the gate and turbine discharge capacities as functions of level.
- If downstream control points are needed (Section 2), add a simple routing such as Muskingum or a lag with attenuation, calibrated on the historical events.
- Check: replaying the historical releases through the model must reproduce the observed levels within a stated tolerance.

### 4.3 Forecast scenarios: the central methodological problem
I would build the inflow information available at each hour t in three tiers:
1. **0 to 6 h:** rainfall forecast fed through a rainfall-runoff model. Use the operator's model if one exists; otherwise calibrate a parsimonious event model on the three floods. If archived forecasts exist, use them in hindcast. If not, perturb the observed rainfall with errors that grow with lead time and come from published or operator-reported skill statistics. Label these as synthetic.
2. **Catchment memory beyond 6 h:** rain that has already fallen keeps generating runoff after the forecast window ends. This is real information past 6 h and is often the largest part of the inflow for the next 12 to 24 h.
3. **Beyond what is predictable:** a small set of scenarios, for example (a) no further rain, (b) rain persisting at the recent rate, and (c) a climatological or "design-like" further burst. These can be organised as a scenario tree, or the operator can set a "plan-for" scenario.

Also run **perfect foresight** as an upper bound and **no forecast** (persistence of the current inflow) as a lower bound. The gap between them shows how much better forecasts would be worth.

### 4.4 Scenario set for testing
Three events are too few for both tuning and validation, so:
- **Historical replays:** 2016, 2018 and 2020, using leave-one-event-out when tuning weights.
- **Scaled and perturbed versions:** inflows scaled up to the 100- and 200-year peak and volume; peaks shifted in time or merged; different antecedent storage.
- If the scope allows, **stochastically generated** multi-peak hydrographs (for example by resampling and recombining observed peaks) to test generality.

## 5. Phase 2: Candidate scheduling schemes

All schemes run in the same **closed loop**. Every hour: observe the state, update the forecast, compute a schedule over a horizon H, apply the first hour, and repeat. This copies the operators' practice.

| ID | Scheme | Why include it |
|---|---|---|
| B0 | Historical operation (observed) | Reality baseline |
| B1 | Existing rule or manual procedure, simulated | Fair "status quo" under the same inflows |
| S1 | Deterministic MPC, single best-estimate forecast | Simplest formal tool |
| S2 | Scenario-based (robust or multi-scenario) MPC with a shared first step | Handles uncertainty beyond 6 h |
| S3 | S1 or S2 with **acceptability constraints built in** | Main candidate |
| S4 | **Simplified rule distilled from S3**, e.g. a lookup chart or decision tree on (level, inflow, inflow trend, forecast volume) | For operators who will not run an optimiser |

### Formulation (S1 to S3)
- **Decision:** hourly release (or the release in blocks of k hours, see below) over the horizon H. H is longer than 6 h: try 12, 24, 48 and 72 h, because what matters is the volume over the coming days. The forecast tiers above supply the inflows.
- **Hard constraints:** mass balance; level not above the dam-safety limit; release within capacity limits that depend on level; ramp-up and ramp-down limits; minimum release.
- **Objective (weighted or lexicographic):**
  1. penalise exceeding critical levels, with steep penalties near the safety limit;
  2. penalise release above the safe downstream discharge, piecewise and convex in the excess;
  3. **terminal-storage term:** penalise end-of-horizon storage above a target that keeps space free for an unseen next peak. This term substitutes for knowledge beyond the forecast, and the drawdown strategy between peaks depends on it;
  4. penalise falling short of the refill target near the end of the event (water supply);
  5. smoothness terms (see S3);
  6. hydropower as a minor term.
- **Solver:** keep it convex (LP or QP with piecewise-linear penalties) so a solution takes seconds and the result is deterministic and reproducible. This avoids black-box behaviour. With a 1-hour decision cycle, solve time is not a binding constraint, but the solution must always be feasible. Add slack variables with large penalties so the solver never returns "infeasible" during an event.

### Acceptability built into S3
- **Move blocking:** the release may change only at block boundaries (e.g. every 3 or 6 h), or the number of changes in 24 h is limited. A cardinality limit needs integer variables, so test whether a convex L1 penalty on changes is a good enough proxy.
- **Ramp limits and quantised steps** that match gate increments.
- **No-reversal rule:** after starting to increase, no decrease within H_min hours unless the inflow forecast changes by more than a threshold.
- **Schedule-stability penalty:** penalise deviation from the previous hour's schedule over the overlapping hours. This directly targets "the plan keeps changing", which is likely the main source of distrust.
- **Notification:** release increases above a downstream warning threshold must be scheduled at least L hours ahead, as a constraint on the first L steps.

### S4: distilled rules
Using the S3 closed-loop runs over the large synthetic scenario set, fit a shallow decision tree or a small parametric rule (e.g. release as a function of level band and forecast inflow volume) that reproduces S3's first-step decisions. Report how faithful it is and how much performance it loses. This serves operators who want a chart they can follow and check by hand. It also shows whether S3's behaviour can be explained.

## 6. Phase 3: Evaluation

### 6.1 Flood-control performance (RQ1)
For each scheme × event × forecast condition:
- peak level and margin to the safety limit; hours above critical levels;
- peak release and hours above the safe downstream discharge, and volume above it; flows at downstream control points if modelled;
- **multi-peak behaviour:** storage available at the onset of each later peak (is space recovered between peaks?);
- end-of-event storage relative to the refill target (water supply cost of over-drawdown);
- spill and hydropower as secondary measures.

### 6.2 Acceptability metrics (RQ2)
- number of release changes per day, largest ramp, total variation of the release;
- reversals (sign changes in the release trend);
- **schedule revision index:** average absolute difference between successive issued schedules over the overlapping horizon;
- lead time given before downstream-relevant increases.

Plot **Pareto fronts** of flood-control performance against acceptability as the smoothness and stability weights vary. The price of acceptability is a main result: if strong smoothing costs little flood performance, the practical case is clear. If it costs a lot near the safety limit, report that and let the operator choose the trade-off.

### 6.3 Robustness (RQ3)
- Degrade forecasts: increase error, add bias, and shorten the horizon to 0 h.
- Run the 100- and 200-year scaled events, with different antecedent storage and peaks moved closer together.
- Mis-specify the horizon and terminal targets.
- Report worst-case as well as average outcomes. With a 6.5-hour fill time, the tail is what matters for dam safety.

### 6.4 Operator evaluation (acceptance in practice)
- **Blind comparison:** show operators side-by-side schedules (historical, S1, S3, S4) for the same flood moments, without labels. Collect ratings for "would you issue this?" and the reasons.
- **Hour-by-hour replay exercise:** operators work through a historical or synthetic flood in simulated real time. Information is revealed hour by hour, and the tool's recommended schedule is shown. Record whether they adopt, modify or reject it, and why. Compare the outcomes with and without the tool.
- Use the reasons for rejection to revise the acceptability constraints, at most one or two iterations, and document the changes.
- Be honest about the limit: this shows *stated and simulated* acceptance, not acceptance during a real event. A shadow-mode trial during a real flood season is the natural follow-on and is out of scope for the main study.

### 6.5 Statistical and claim discipline
- With three historical events, results are case studies, not statistics. Make general claims only from the synthetic ensembles, and label them as such.
- Tune on two events and test on the third (rotating). Do not tune on all three and then report on the same three.
- Separate the effect of forecast information from the effect of the scheduling algorithm (perfect-foresight versus realistic runs for each scheme).

## 7. Provisional recommendation

**Recommended approach:** a **scenario-based MPC (S2/S3)** that
- re-solves every hour over a 24 to 72 h horizon,
- uses the 6 h rainfall forecast plus catchment-memory runoff plus a small set of scenarios for what is unknown beyond 6 h,
- includes a **terminal free-storage target** to protect capacity for the next peak,
- builds the acceptability rules into the optimisation as hard limits and penalties: move blocking, ramp and step limits, no reversals, schedule-stability penalty and notification lead time,
- and comes with a **distilled rule chart (S4)** for transparency, training and fallback.

**Reasons**
- It matches the operators' existing receding-horizon practice, so it formalises what they already do rather than replacing it.
- The terminal-storage and scenario elements address the core difficulty: deciding drawdown between peaks when the next peak lies beyond the 6 h forecast.
- Building acceptability in turns "would operators use it" into a design property that can be measured and traded off against performance.
- A convex formulation is fast, reproducible and explainable. The distilled rules give a check that can be done without software.

**Key assumptions behind it**
- Runoff from rain that has already fallen is a large, predictable share of inflow over the next 12 to 24 h, so information beyond 6 h is not zero.
- Operators can and will state their acceptability criteria numerically.
- Downstream safe discharge and dam safety limits are known and stable.
- The model reproduces historical levels well enough that differences between schemes are not artefacts of model error.

**What would confirm it:** S3 matches or beats historical operation on peak level and downstream exceedance in all three replays and in the scaled 200-year runs. Its acceptability metrics are equal to or better than historical operation. Operators choose its schedules in blind comparison and adopt most of its recommendations in the replay exercise.

**What would change it:**
- *If forecasts beyond 6 h add almost nothing* (scenario MPC is no better than persistence MPC), simplify to a short-horizon MPC or a rule-based scheme with a fixed free-storage target that depends on level and season. A simpler tool would then be easier to justify.
- *If the price of acceptability is high near the safety limit,* adopt a two-mode scheme: smooth, constrained operation in normal flood conditions, and an emergency mode with relaxed smoothness above a level trigger. The operator approves the switch.
- *If operators reject optimiser output whatever its quality,* make the distilled rule chart (S4) the main deliverable, and use MPC offline only to design and stress-test it.
- *If derived-inflow noise or model mismatch is large,* the comparison is unreliable. Invest first in inflow reconstruction and model calibration, and narrow the claims.

## 8. Deliverables and limits
- A closed-loop simulation testbed and documented formulation.
- Operator-signed objectives and acceptability specification.
- Comparative results: performance, acceptability and robustness, including Pareto fronts.
- Operator evaluation results.
- A prototype decision-support schedule generator plus the rule chart.

**Main limits to state openly:** three historical events only; forecast errors may be synthetic if archived forecasts are unavailable; acceptance is measured in simulation, not in live operation; downstream damage is represented by discharge thresholds rather than a damage model unless the operator supplies one.
