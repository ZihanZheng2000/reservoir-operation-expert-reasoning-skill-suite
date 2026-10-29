# Daecheong Reservoir: decision support for hourly flood release schedules

## 1. Recommendation in brief

Build a **rolling-horizon (model predictive control) scheduler with a scenario-based mixed-integer program**. It runs every hour on a horizon longer than the 6-hour forecast, carries out only the first hour, and is re-solved when new storage, outflow, Yongdam plans and rainfall forecasts arrive. Operator preferences go into it as follows:

- **Hard constraints, ranked in a stated order:** levels between LWL and FWL minus a safety margin; the minimum release; turbine capacity; spillway capacity at the current head; turbines at full capacity before any spill.
- **"No man-made flood" constraint:** outflow must not exceed the peak inflow observed so far. This is a strong soft constraint that may be relaxed **only** when the dam-safety constraint would otherwise be broken.
- **Penalty terms:** spillway volume, peak outflow, hour-to-hour release changes, deviation from the schedule announced in the previous hour, and gate open/close switches. A minimum gate-open time and an explicit "flood clearly ending" condition set when gates may close.
- **Soft but heavily weighted terminal-storage target:** keeps enough water for supply after the event.

Forecast uncertainty is handled with a small set of inflow scenarios. All scenarios share one release decision for the next hour (the hour that gets executed and announced), and later hours may differ by scenario.

Demonstrate it in **closed-loop hindcasts** of the 2016, 2018 and 2020 events, using the actual starting levels. Compare it with historical operation, a deterministic-forecast version of the same controller, a simple rule, and a perfect-foresight optimum (a bound that cannot be deployed). Then stress-test it with scaled events, because no 200-year or PMF hydrographs exist.

**Why this route:**

- The sponsor's goals are mostly about **shape and stability** of the schedule (gate states, announced-schedule revisions, turbines first, peak not above inflow so far). These are naturally logical and integer conditions, and a mixed-integer program over a short hourly horizon handles them exactly and quickly.
- The problem is small enough to solve within the hourly cycle. Evolutionary search or dynamic programming would be slower or less transparent. A fixed rule cannot use the forecast or the announced schedule.
- **The main risk is not computation. It is whether operators accept the schedules.** For that reason, eliciting and checking operator preferences is built into the design.

## 2. The questions that decide the design

1. **What can the storage actually do?**
   - At the 200-year inflow (10,700 m³/s) the flood-control storage fills in about 6.5 h. With little release, that implies a usable flood volume of about 10,700 × 6.5 × 3,600 ≈ **250 × 10⁶ m³**.
   - **Assumption:** this is roughly the NHWL–FWL band (3.5 m). That implies a mean surface area near 250/3.5 ≈ **70 km²**, or about **0.7 × 10⁶ m³ per 10 cm** of level. Confirm with the level–storage table.
   - **2020 peak** (4,468 m³/s) with only turbines running (264 m³/s): the net gain is about 4,200 m³/s ≈ 15 × 10⁶ m³/h ≈ 0.22 m/h. The band would fill in about 16 h of peak-level inflow.
   - **Event volume:** the events last 200–310 h. Even at an assumed average inflow of 1,000 m³/s, a 269-h event carries about 970 × 10⁶ m³, roughly four times the flood storage.
   - **Consequence:** the storage cannot hold these events. It can only **shift and smooth** releases over hours to about a day. If excess inflow above the release must be held for about 24 h, the storage can lower the peak release by about 250 × 10⁶ / 86,400 ≈ **2,900 m³/s**, but only if the band starts empty.
   - **So the deciding operational quantity is how much of the band is free when each peak arrives.** In multi-peak events, that depends on how far the reservoir was drawn down between peaks.
2. **How should the next hours be scheduled when the forecast covers only 6 h of a 200–300-h, multi-peak event?**
   - The horizon must reach past the forecast, so a scenario extension is needed beyond 6 h.
   - The main risk is **between peaks**: closing gates to save water leaves the band full if a second peak follows. Keeping them open too long empties water needed after the event.
   - This is the trade-off on which the 2016 and 2018 demonstrations should focus.
3. **What makes a schedule acceptable to operators?** The preferences are unwritten. Their ranking (for example, schedule stability against a lower peak outflow) cannot be taken from regulations. It must be elicited and then checked against what operators actually did, allowing for the conditions they faced.

## 3. Baseline and data preparation

- **Reconstruct historical operation** for each event: hourly level, storage, turbine and spillway release, gate states (if K-water can supply gate logs), Yongdam releases, and the announced schedules (if archived).
  - The historical run is the main comparator. It is context rather than a controlled counterfactual, because operators reacted to information (forecasts they saw, requests from downstream agencies) that the model will not have.
  - Ask K-water for those records and for any downstream requests made during each event.
- **Fix the initial state.** Every comparison of an event starts from the **historical starting level**. A tool that starts lower would look better for no real reason.
- **Clean the derived inflow.**
  - Inflow is back-calculated from storage change. With 1-cm level resolution (**assumption**) and about 70 km² of area, one hour's storage change is uncertain by about 0.7 × 10⁶ m³, which is about **±200 m³/s** of apparent inflow. That is close to the full turbine capacity.
  - Hourly derived inflow is therefore noisy, and negative values are possible. Smooth it (for example, a centred 3-h moving average, or a filter that conserves volume) and check it against event volumes.
  - The "peak inflow observed so far" must use the **smoothed** series. Otherwise noise spikes raise the cap and allow larger releases.
- **Separate the inflow into the planned Yongdam release and the local basin inflow.** Only the local part is forecast. Yongdam's plan is treated as known, as the brief allows. Estimate the Yongdam-to-Daecheong travel time from the records (lagged correlation of Yongdam release with derived inflow) and shift the Yongdam term by it.
- **Encode the physics as piecewise-linear relations:**
  - the level–storage relation;
  - the spillway rating (maximum discharge as a function of level; more than 6,000 m³/s at NHWL, 11,680 m³/s at FWL);
  - turbine capacity (264 m³/s; check whether it falls at low head, which matters little in floods).
- **Collect what the brief does not list.** Request from K-water and the Korea Meteorological Administration:
  - the archived 6-h quantitative rainfall forecasts for the three events, as issued;
  - basin-average observed rainfall;
  - the minimum-release amounts (contracted plus in-stream);
  - the post-event supply storage requirement;
  - gate opening and ramping limits.

  If the forecast archive is not available, synthetic forecasts must be used (Section 5), and the results must be labelled as such.

## 4. Formulation

**Decision variables, hourly over horizon H** (provisionally 48 h; justified in Section 6):

- turbine release T_t ≤ 264 m³/s;
- spill S_t ≤ S_max(level_t);
- gate state g_t ∈ {0, 1};
- auxiliary peak and change variables.

**Hard constraints:**

1. Mass balance: storage_{t+1} = storage_t + (local inflow_t + Yongdam_t − T_t − S_t) × 3,600.
2. LWL ≤ level ≤ FWL − m in **every** scenario. The margin m covers level-measurement error, wave set-up and gate-response time. **Planning value:** 0.3–0.5 m, about 20–35 × 10⁶ m³, or about 1.5–2.5 h of storage at the 2020 peak with only turbines running. Agree m with K-water dam-safety staff.
3. T_t + S_t ≥ the downstream requirement (contracted users plus in-stream flow).
4. Turbines first: S_t ≤ M·z_t and T_t ≥ 264·z_t. Spill is allowed only when turbines are at full capacity, unless turbines are unavailable.
5. Spill only when gates are open (S_t ≤ M·g_t). Minimum gate-open duration: once g switches to 1, it stays 1 until the **end-of-flood condition** is true. Proposed end-of-flood condition, to be set with operators: smoothed inflow falling for k consecutive hours, below a threshold, no significant rain in the 6-h forecast, and level at or below the target band.
6. Hourly ramp limit |Q_t − Q_{t−1}| ≤ ΔQ_max (value from gate practice and downstream agencies).

**No man-made flood constraint:** Q_t ≤ Q_in,max-so-far (smoothed). Treat it as hard with a slack variable that carries a very high penalty and may be used **only** if constraint 2 would otherwise be broken. This states the priority **dam safety > no amplification** explicitly, rather than leaving it to weights.

**Objective:** a weighted sum with weights in clearly separated magnitude tiers, so it behaves close to lexicographically. The tiers below are provisional and must be confirmed with operators:

- **Tier 1, terminal storage:** shortfall below the end-of-horizon storage band. The lower edge is the supply requirement. The upper edge is the level that still leaves enough buffer for a plausible next peak (Section 6). This is tier 1 because water after the event is a stated requirement.
- **Tier 2, stability:**
  - deviation from the schedule announced last hour over the overlapping hours, weighted most heavily for the nearest hours;
  - the number of gate switches;
  - the sum of |ΔQ|.
- **Tier 3, peak outflow over the horizon:** a minimax term through an auxiliary variable.
- **Tier 4, spillway volume.**

**Two cautions:**

- Peak outflow and spill volume can pull in **opposite** directions. Minimizing the peak favours releasing early to spread the flood, while minimizing spill favours holding water. With 6-h forecasts, early release is justified only when the forecast and the scenario set support it. The tiers decide which goal wins, so their order is a question for operators, not for the modeller.
- An optional "freeze" can fix the first 1–2 hours of an announced schedule unless a trigger fires (level projected above FWL − m in the upper scenario, or inflow beyond the scenario envelope). This directly addresses the downstream agencies' need for predictable schedules.

**Size:** 48 h × about 20 scenarios × about 8 variables gives roughly 8,000 variables and up to about 1,000 binaries. A standard mixed-integer solver should handle this in seconds to a few minutes. Confirm that solve time stays within, say, 10 minutes of the hourly cycle, with a fallback (the deterministic version) if it does not.

## 5. Forecast uncertainty and scenarios

- **Inflow forecast model (hours 1–6):**
  - Use a simple, transparent model of local inflow driven by recent smoothed inflow and the 6-h rainfall forecast, plus observed rainfall if obtained. A linear transfer-function or autoregressive model with exogenous input is a reasonable first choice.
  - Data-driven models fitted on three events would overfit. With only three events, calibrate on non-event and minor-flood periods as well, and check the events out of sample.
  - The model must reproduce the basin response lag. Estimate it from rainfall–inflow cross-correlation. The usable inflow lead time is roughly the 6-h forecast plus that lag.
- **Error model by lead time:**
  - Fit relative errors for leads 1–6 h, separately for rising and falling limbs if the data support it, including bias. The error grows with lead time.
  - Keep the **correlation across lead times**. For n = 6 hourly errors of equal spread σ and correlation ρ = 0.8 (**assumed** for illustration), the variance of the 6-h volume error is 6σ²(1 + 5 × 0.8) = 30σ², not 6σ². The standard deviation is about 2.2 times larger than an independence assumption gives. Independent errors would therefore badly understate the risk of a volume surge, which is what fills the band.
  - Generate correlated paths, for example an autoregressive process on relative errors or a Gaussian copula across leads, and check their coverage against hindcast errors.
- **Hours 7–H (no forecast):** extend each scenario with conditioned continuations:
  - recession;
  - persistence of current inflow;
  - renewed rise, built by drawing hydrograph segments that follow similar states in the three events and other flood-season periods in the record.

  Weight these by rough frequency, and keep at least one deliberately adverse branch so the safety constraint is checked against an upper case.
- **Structure:** reduce to about 10–30 scenarios. All of them share the next-hour release (non-anticipative). They may share the first few hours if a freeze is used, and branch afterwards. A single "average" scenario is not acceptable, because the deciding risk lies in the upper tail.
- **Hindcast forecasts:**
  - Use the archived real 6-h rainfall forecasts if available, so the evaluation uses the same forecast product that will be used in operation.
  - If they are not available, build synthetic forecasts by perturbing the observed inflow with the fitted error model. Run several error levels (0 %, i.e. perfect; the fitted level; double the fitted level) and **label results by forecast condition**.

## 6. Adaptive logic across the event

The hourly re-optimization does most of the adapting. Four event phases still need explicit handling, so that schedules make sense to operators.

- **Before and early in the rise (gates closed):**
  - Release turbines at up to 264 m³/s and store the rest. The no-amplification cap is binding early, because the observed peak is still small.
  - Open the gates when the upper scenario projects the level above a gate-opening trigger within the horizon. The trigger is set by the time needed to evacuate safely.
  - Example: at 0.22 m/h (2020-scale peak, turbines only), 1 m of band lasts about 4.5 h. Opening must be decided several hours before the band is used up, which is **within** the 6-h forecast window.
- **Peaks:** hold outflow at or below the observed inflow peak, smooth it, and keep the gates open.
- **Between peaks (the deciding phase for 2016 and 2018):**
  - The question is how far to draw down before a second peak that the 6-h forecast cannot yet see.
  - **Proposed rule, to be computed and tested:** the end-of-horizon storage band's upper edge is set so that a repeat of the largest peak seen so far, using its observed volume above the current release cap, could be absorbed without breaking the cap or FWL − m. Its lower edge is the post-event supply requirement.
  - **Example arithmetic:** with inflow at 1,500 m³/s and outflow at 2,500 m³/s (net 1,000 m³/s), freeing 1 m of level (about 70 × 10⁶ m³) takes about 19 h. Freeing the full band would take most of four days at that rate. Large drawdown between peaks is therefore slow, and the band edge matters.
  - Whether storing more between peaks would have caused problems in 2016 or 2018 is an empirical question for the hindcasts.
- **Recession and closing:**
  - Close the gates only when the end-of-flood condition holds.
  - Bring the level into the supply band without pushing outflow above the event's observed inflow peak.
  - Do not keep water in the flood band longer than the supply requirement needs. Outside an active flood, the band is buffer, not storage.
- **Fallbacks:**
  - If the forecast is missing or late, or observed inflow leaves the scenario envelope for two consecutive hours, switch to the deterministic or measurement-based version (current inflow and its trend, no forecast term), and flag the switch to the operator.
  - If Yongdam must depart from its plan (for example, its own spill), replace the Yongdam input immediately and re-solve.
  - If the inflow approaches the scale of the 200-year flood, hand over to the existing emergency procedure. The tool is not validated for that range.

## 7. Evaluation and demonstration

**Comparators,** all run from the same initial level with the same inflows and Yongdam releases:

1. historical operation;
2. a simple rule (for example, turbines first, spill to keep a level target, outflow capped at inflow-so-far);
3. deterministic-forecast MPC with the same objective;
4. scenario MPC (the proposed tool);
5. perfect-foresight optimization of the whole event (an upper bound, not deployable).

The difference between 3 and 4 measures what handling uncertainty is worth. The difference between 4 and 5 measures what better forecasts could add.

**Closed-loop protocol:** at every hour, the tool sees only information available at that time. It executes hour 1, and the state is advanced with the *actual* derived inflow. The tool's own releases feed back into the state. Record every announced schedule.

**Metrics per event:**

- peak outflow, and its ratio to the peak inflow so far;
- spillway volume and spill hours;
- turbine use while spilling (should be 100 %);
- maximum level and minimum margin to FWL;
- end-of-event storage against the supply requirement;
- gate switches;
- maximum |ΔQ|;
- **schedule revision**: mean absolute change, from one issue to the next, of the release planned for the same hour, by lead.

Show trajectories, not only totals, so operators can see why the schedule acts as it does.

**What the evidence can and cannot show:**

- Three events cannot support probabilities or general superiority. They are demonstrations of behaviour.
- Use **leave-one-event-out** tuning: set weights and triggers on two events and test on the third.
- Report sensitivity to weights, forecast-error level, horizon (24, 48 and 72 h) and scenario count (5, 10, 20, 30), with run time.

**Stress tests:**

- Scale the observed hydrographs up to the 200-year peak (×2.4 for 2020, since 10,700/4,468 ≈ 2.4), with shape fixed.
- Shift peak timing in the multi-peak events, for example bringing the second peak closer.
- Raise starting levels to NHWL.
- Add a forecast bias (systematic under-forecast).

These tests show where the tool's dam-safety relaxation activates and whether it fails safe. They do **not** certify dam safety, which still rests on the design-flood routing.

**Acceptability test:**

- Show operators, blind, pairs of schedules from the tool and from history for the same hours. Ask which they would issue and why.
- Use their answers to re-rank the objective tiers.
- Check whether historical decisions that differ from the tool's were forced by things the model omits, such as downstream requests or information not in the record.

**What would change the recommendation:**

- If deterministic MPC matches the scenario version on the hindcasts and stress tests, the simpler version is preferable for transparency.
- If the integer program cannot be solved reliably within the hour, simplify. Fix gate state by rule, and leave only the continuous release to optimize.
- If operators consistently reject schedules that move away from the previous announcement, schedule stability should become tier 1, and the cost in peak outflow should be shown to them explicitly.

## 8. Adoption

- **Approval:** the tool advises; it does not replace the operating procedures. My understanding is that K-water operates the dam, and that flood-season release plans are coordinated with or approved by the regional flood-control authority for the Geum River. Confirm the approving body and the instrument with K-water. The current procedures remain the legal basis until a change is approved.
- **Trial:** run the tool in **shadow mode** for at least one flood season. It issues schedules beside the operators, who record whether each schedule was acceptable and why not. Agree acceptance criteria with K-water dam-safety staff in advance, for example:
  - no projected level above FWL − m;
  - no outflow above the inflow-so-far peak;
  - revision and switch counts no worse than historical.
- **Logs and reversion:** log every run (inputs, scenarios, solution, operator choice) for after-event review. Reversion triggers are those in Section 6. The duty operator decides on reversion, and every override is logged.
- **Communication:**
  - Downstream flood-control agencies need to know how announced schedules are built and when the freeze may be broken.
  - Water users need the end-of-event storage target.
  - Operators need training on reading scenario outputs, and the model and its parameters need version control.
