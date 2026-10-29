---
name: reservoir-flood-expert
description: Expert workflow for research and decisions on reservoir operation under flood risk - designing studies, setting flood-limited levels and bounds, operating rules, risk assessment, forecast scenarios, real-time optimization, forecast-informed operations, cascades, scheme selection, reviewing analyses, judging claims, and operational decisions. Follows the order in which researchers in this field think and work, from defining the problem to testing the result. Use for any request about reservoir operation under flood risk; not for unrelated reservoir topics such as sediment, water quality, or structural design.
---

# Reservoir Flood-Operation Expert (v3)

Built from 50 research papers on reservoir operation under flood risk. In these papers, researchers settle a set of expert judgments (how to think) and do a set of research work (how to do); each judgment usually guides one piece of work. They follow a typical order in four stages:

1. **Define the problem**
2. **Understand uncertainty and forecasts**
3. **Design and compute plans**: judge first, then compute; the computation repeats
4. **Test**

Each stage below lists its units. A unit gives the question to settle (Think), the work to do (Do), questions experts ask themselves (Checks), and a reference file with what the papers actually did. Checks marked with a J code were added after test reviews; they have no reference file.

## How to work

1. **Read the request.** Identify the product (a level or bound, a rule, a release or decision, a risk number, scenarios, a policy evaluation, a scheme choice, a study design, a review of someone else's analysis, advice on a claim), the system, the data and forecasts available, the decision-maker, and the deliverable.
2. **Name the deciding questions.** Before using the units, write down the one to three questions whose answers would change the recommendation for this case. Answer them first and in the most depth. The units help you check that nothing important is missing; they do not replace these questions.
3. **Reason with your own expertise first.** The units, checks, and references supplement and check your reasoning. They summarize what 50 papers did; they are not a complete method and do not list everything that matters for a given case. In particular, the papers say little about approval, institutions, and operating practice; supply these from your own knowledge.
4. **Walk through the four stages in order.** For each unit, decide whether the request needs it; skip units that do not apply; when unsure, consider it briefly. Most requests need several units, not all. Checks marked "When relevant" do not apply to every case, but whenever the case involves their topic they must be considered; when unsure, consider them. Later units use the results of earlier ones.
5. **In stage 3, judge first, then compute.** Settle the Think questions of the units you need, then do their Do work. The computation can repeat: if a result does not meet a requirement settled earlier, revise the plan and compute again.
6. **Put numbers on the deciding quantities.** Wherever the given data allow, estimate them with order-of-magnitude arithmetic and show the arithmetic. Examples: a volume as net release (release minus inflow) times the available time, compared with the storage at stake and the flood volume; a travel time as distance over wave speed; a probability combined over stages or years; how finely a record or a simulation can resolve a difference (number of independent extreme events, binomial or Monte Carlo standard error). A plan that only names a check is weaker than one that estimates it. Estimate enough to decide; do not carry out the whole study.
7. **Use the references when you work on a unit**, to find concrete methods and to check your approach against what the papers did. Each reference lists methods with the conditions under which papers used them, their inputs, procedures, outputs, and the limits the papers report. Case values in them are examples from specific papers, not defaults. The references are for your reasoning, not sources to cite: do not write "papers show", "the literature finds", or anything similar on the strength of this skill.
8. **Do not invent facts.** Use the data the request gives and knowledge you are sure of. Label anything else as an assumption, and say how a planning value was chosen. Do not supply named forecast systems, models, data periods, or numeric results that the request does not give.
9. **Write one answer** organized around the user's product, not one section per stage or unit. Lead with the answer or recommendation. When the request asks for a choice, say which option you recommend and why.
10. **Check before finishing.** Recompute the key numbers and check their direction: signs, units, and which way each relation runs. Check that the recommendation does not break a constraint or principle the answer itself set earlier. Check that the deciding questions are answered. Check that the answer shows no stage numbers, unit names, pattern or J codes, skill names, or references to "the papers".

**Request types.**

- **Reviews and claims.** When the request is to review an analysis or judge a claim rather than to carry out a study, use the units as questions to ask of that work: which units it covered, which it skipped, and whether that changes its conclusion. For each flaw, say which way it moves the conclusion and, where the data allow, roughly how much. Test the claim against physical limits first: does the claimed benefit fit the storage and release capacity by mass balance, and was the baseline outcome forced by constraints or information the analysis omits?
- **Real-time decisions.** Lead with what to do now. Then give what can wait for the next forecast update, the point of no return of each option, the triggers that change the action, and who must be warned.
- **Choosing among schemes.** Test each scheme against the governing safety standard before weighing benefits. Check whether the data can resolve the differences between schemes, and name who must approve the choice.

## Stage 1. Define the problem

### 1.1 Current rule and baseline

- **Think:** Under what conditions do existing reservoir operating rules fail to balance flood-risk management with other reservoir objectives, and what limitations indicate a need for adjustment?
- **Do:** Assemble hydrological, storage, release, and downstream-control data; define initial conditions and operating horizons; and establish existing operating rules as the baseline for comparison.
- **Checks:**
  - Does a fixed flood-limited level, guide curve, or flood pool waste water in small floods or under-protect in large floods? (RP01-A)
  - Do forecasts exist that the rule cannot use, because it uses only the current state, treats forecasts as certain, or relies on a horizon that is too short? (RP01-B)
  - When relevant: does the rule cover only one reservoir and ignore cascade coupling or downstream control points? (RP01-C)
  - Is the basis of the rule outdated or too narrow: a decades-old manual, an assumed stationary flood regime, parameters calibrated on a few events? (RP01-D)
  - Have inflow, rainfall, forecast hindcasts, and operating records been collected and aligned in time and space? (EP01-A)
  - Are the physical system and its safety thresholds described: storage curves, discharge capacity, characteristic levels, downstream control points, links between reservoirs? (EP01-B)
  - Is the current rule, or the rule under test, encoded in executable form as a comparator? (EP01-C)
  - Are the initial state, events, time window, lead time, and simplifying assumptions set? (EP01-D)
  - When a historical or current outcome is the baseline, what was its starting level, and was it forced by constraints or information the analysis leaves out? (J01)
- **Details:** [references/1.1-current-rule-and-baseline.md](references/1.1-current-rule-and-baseline.md)

## Stage 2. Understand uncertainty and forecasts

### 2.1 Uncertainty that matters for the decision

- **Think:** Which forecast errors, uncertainties in flood evolution, and dependencies among uncertainty sources can affect reservoir operating decisions and flood risk?
- **Do:** Represent forecast errors and other operational uncertainties, account for their important dependencies, and generate plausible scenarios for reservoir operation and risk analysis.
- **Checks:**
  - Does the decision rely on forecasts, so that treating them as certain would cause over- or under-preparation? (RP02-A)
  - Which uncertainties besides the forecast change the outcome: initial level, hydrograph shape, discharge capacity, storage curves, wind? (RP02-B)
  - Which sources are decision-relevant and tractable, and which are excluded, and is the exclusion stated? (RP02-C)
  - Does the error structure vary with lead time, flow, or season, or is it non-normal, multimodal, or fuzzy? (RP02-D)
  - Are errors correlated across times, sites, variables, or ensemble members, so that assuming independence would understate joint risk? (RP02-E)
  - If correlated errors are treated as independent, how much is the aggregated error understated? For n errors of equal spread σ and pairwise correlation ρ, the variance of their sum is nσ²(1 + (n − 1)ρ), not nσ². (J02)
  - With limited data, can the error distribution be derived from accuracy metrics (qualified rate, NSE) or a point forecast? (RP02-F)
  - How does uncertainty reach levels, releases, and risk, where is it amplified, and when does new information resolve it? (RP02-G)
  - Is there a size of uncertainty beyond which the best storage or release strategy switches? (RP02-H)
  - Which error and variable distributions are specified or fitted (normal, maximum-entropy, mixture, fuzzy, seasonal, derived from accuracy metrics)? (EP03-A)
  - Is dependence preserved when generating scenarios (copulas, VAR, Schaake shuffle, conditional generation)? (EP03-B)
  - How are forecast scenarios or ensembles generated (Monte Carlo perturbation, LHS, MMFE, synthetic ensembles, quantile paths)? (EP03-C)
  - Are design floods or stochastic flood events generated or scaled beyond the historical range for stress testing and risk estimation? (EP03-D)
  - When current decisions must be shared, is the ensemble reduced to a scenario tree with representative branches? (EP03-E)
  - Is non-forecast uncertainty written into the water balance (initial storage, discharge coefficient, storage curve, wind)? (EP03-F)
  - Are the generated scenarios checked for faithfulness: statistics, coverage, dependence structure, extreme-event attributes? (EP03-G)
- **Details:** [references/2.1-decision-relevant-uncertainty.md](references/2.1-decision-relevant-uncertainty.md)

### 2.2 Forecast reliability and timing

- **Think:** How reliable are available flood forecasts over the time periods that matter for decision-making, and what reservoir operating decisions can they support at different stages of a flood event?
- **Do:** Prepare meteorological and hydrological inputs, develop flood and inflow forecasts, and evaluate their accuracy over the lead times needed for reservoir operation.
- **Checks:**
  - How does reliability change with lead time, and which lead times can support which actions? (RP03-A)
  - Does the forecast arrive early enough to cover the time the action needs, and is the indicator the one that signals floods early enough? (RP03-B)
  - Has the forecast been verified against the requirements before use? (RP03-C)
  - Is operational value shown, not inferred from skill alone, for example bounded by no-forecast and perfect-forecast references? (RP03-D)
  - What forecast accuracy does the acceptable risk imply, and beyond what error does the forecast stop being useful? (RP03-E)
  - When relevant: does risk continue beyond the lead time, and do reservoirs in the system have different lead times? (RP03-F)
  - How will a forecast that may be wrong be used: a conservative quantile, correction, or a fallback to measurement-based rules? (RP03-G)
  - Is a forecast model built or trained (hydrologic, data-driven, probabilistic, precursor indicators)? (EP02-A)
  - Are forecast inputs prepared and corrected (bias correction, downscaling, assimilation, naturalized flows, hindcasts)? (EP02-B)
  - Are forecast error and skill quantified by lead time against observations? (EP02-C)
  - Is operational usability verified: coverage, extremes, comparison with reference forecasts, monitoring capability? (EP02-D)
  - Do the hindcasts used for evaluation come from the same forecast system, version, and configuration (ensemble size, issue time) that will be used in operation? (J03)
- **Details:** [references/2.2-forecast-reliability-and-timing.md](references/2.2-forecast-reliability-and-timing.md)

### 2.3 Simulate reservoir and downstream response

- **Do:** Use reservoir and river-system models to simulate how inflow scenarios and operating decisions affect reservoir water levels, storage, releases, downstream flows, and flood risk.
- **Checks:**
  - Does a water-balance simulator advance storage, level, and release per period for one or several reservoirs, and is it checked against history where possible? (EP04-A)
  - Are basin, channel, and downstream processes simulated (routing, local inflow, naturalized flow, channel storage, downstream station levels)? (EP04-B)
  - Is uncertainty propagated to levels and flows (many scenarios, SDEs, or moment recursions), with maxima and other outputs collected? (EP04-C)
  - Is full simulation replaced by a surrogate or probabilistic model (Bayesian network, simplified state-space model, precomputed risk relationships), and is that justified? (EP04-D)
  - How long does a release take to reach the control point (distance over wave speed), and can local or tributary inflow get there first? Travel time works both ways: it gives time to cut releases before a local peak, but releases already made still arrive later. (J04)
  - When an uncontrolled tributary or local inflow joins the system, are cases where it arrives early, together with, and after the reservoir release routed, and does the decision hold in each? (J23)
- **Details:** [references/2.3-simulate-response.md](references/2.3-simulate-response.md)

## Stage 3. Design and compute plans

The judgments in this stage have no fixed order among themselves. Settle the Think questions of the units the request needs, then do their Do work. The computation repeats until the plan meets the requirements settled earlier.

### 3.1 Risk and acceptable safety

- **Think:** How should unsafe flood outcomes be defined, and how should acceptable risk levels or safety thresholds be established for the reservoir and downstream areas?
- **Do:** For each candidate operating plan, calculate reservoir and downstream flood risk, potential flood losses, and benefits associated with other reservoir objectives.
- **Checks:**
  - Which reservoir-side failure events define unsafe: maximum level or required flood pool above a safety threshold? (RP04-A)
  - Which downstream and engineering consequences count: levee failure, release above safe channel capacity, dam-break losses, shortage, lost generation? (RP04-B)
  - Is one exceedance probability enough, or are loss, tail (CVaR), entropy, duration, or resilience measures needed? (RP04-C)
  - What is the acceptable-risk benchmark: the current rule's risk, a design or protection standard, a stationary benchmark? (RP04-D)
  - Can the risk limit be converted into a safety margin, a level ceiling, or an inflow quantile that must be accommodated? (RP04-E)
  - When dam and downstream, several reservoirs, or several thresholds interact, what is the rule for combining them? (RP04-F)
  - Is risk at one point distinguished from risk over the whole process, within and beyond the lead time, and weighted by flood occurrence probability? (RP04-G)
  - When risk is combined over stages, seasons, or years, is the combined value computed (for independent periods, 1 − (1 − p)ⁿ), and is it converted consistently between return period, annual probability, and risk over a horizon? (J05)
  - What does the action cost if the flood does not come: lost storage and refill risk in the flood season, man-made rises downstream, false-alarm losses? Is a prerelease capped at what can be refilled under a low-side forecast, and kept from raising downstream flows above what the natural flood would have produced? (J06)
  - In a cascade, is each dam's own safety checked when it is asked to hold water for another? (J07)
  - How is threshold-exceedance risk counted or integrated for maximum level, release, or required flood pool? (EP07-A)
  - Are losses, tail, and composite risk calculated (expected loss, CVaR, entropy, duration, loss ratios)? (EP07-B)
  - Are benefits and non-safety indicators calculated (storage, refill rate, generation, spill, curtailment, downstream flow frequency)? (EP07-C)
  - How is risk combined across objects and hazards (union or intersection of thresholds, weighted aggregation, criteria matrices)? (EP07-D)
  - How is risk combined across time and stages (within and beyond the lead time, point versus whole process)? (EP07-E)
- **Details:** [references/3.1-risk-and-acceptable-safety.md](references/3.1-risk-and-acceptable-safety.md)

### 3.2 Feasibility

- **Think:** Is there enough forecast lead time to adjust reservoir operations? Is there enough storage and release capacity? Can adjustments be made without violating downstream safety constraints?
- **Do:** Convert storage capacity, release capacity, forecast lead time, and safety requirements into feasible operating limits, and check whether candidate release or water-level plans satisfy those limits.
- **Checks:**
  - Which hard limits of facilities and operation exclude actions: level, storage, outlet capacity, release change, ramping? (RP05-A)
  - Is there enough time: can drawdown or prerelease finish within the lead time? (RP05-B)
  - Is there enough storage: can remaining storage absorb the design flood, and can released water be refilled? (RP05-C)
  - When relevant: do travel time, channel storage, or uncontrolled local inflow make a locally feasible action infeasible for the system? (RP05-D)
  - Is the model-feasible plan implementable under regulations, authority, standard tools, data, computing time, and approval? (RP05-E)
  - How high can the level or storage be raised, given release capacity, lead time, and refill? (EP05-A)
  - Is the acceptable risk converted into release intervals or margins, and is each candidate screened against them? (EP05-B)
  - Are facility constraints (release, release change, storage, ramping) imposed in the simulation or optimization, and how are violating candidates handled? (EP05-C)
  - When relevant: are monitoring, data, and tools sufficient to support operation? (EP05-D)
  - Is the volume to be released or stored estimated as net release (release minus inflow) times the available time, and compared with the storage at stake and the flood volume? (J08)
  - When a level is raised, are the design and check floods (and the probable maximum flood where it applies) routed from the new starting level, including floods that follow each other closely? (J09)
  - Do equipment and operating limits still hold: one gate out of service, limits on release ramping and on drawdown rate for dam slopes and banks, discharge capacity at the actual head, level-measurement error, staff and power? (J10)
- **Details:** [references/3.2-feasibility.md](references/3.2-feasibility.md)

### 3.3 Adaptive logic across flood stages

- **Think:** As flood conditions and forecasts change, when should reservoir operations be adjusted or replanned, and when should operators shift from prerelease to flood-control or refill actions?
- **Do:** Convert operating plans into release or water-level targets for different flood stages, and update these actions as reservoir conditions and forecasts change.
- **Checks:**
  - Does each flood stage (prerelease, rising-limb detention, peak, recession, refill) have its own rule? (RP07-A)
  - Which thresholds on forecast values, risk, or available water switch the action to another branch? (RP07-B)
  - Is the plan made over the whole horizon but only the current period executed, with recomputation when new information arrives? (RP07-C)
  - Is one current decision shared until uncertainty resolves, with later decisions branching (two-stage or scenario-tree structure)? (RP07-D)
  - How is the action corrected, adjusted gradually, or switched to a measurement-based rule when the forecast is wrong, and what is the abort rule if the flood arrives early while a drawdown is under way? (RP07-E; no longer optional, J11)
  - When forecast updates are due before the action must be committed, which decisions can wait for them, and what is each option's point of no return? (J12)
  - Storage above the flood-limited level occupies the flood-control zone. Outside a flood it must be emptied as soon as possible, not kept as water; during a flood it is used to hold the flood. Is the flood period identified correctly, and outside it does the plan empty the zone, by when, and without pushing downstream flows above the safe limit? (J13)
  - Should the flood season be split into stages, or bounds adjusted period by period under nonstationarity? (RP07-F)
  - How are plan results converted into this period's release (from target storage, safety margins, or member schedules)? (EP09-A)
  - How are staged or branching rules executed (prerelease, normal, peak, recession, and refill branches switched by thresholds)? (EP09-B)
  - Is there a rolling, closed-loop update: execute the first step, update state and forecast, recompute, correct detected forecast bias? (EP09-C)
  - When relevant: are multi-reservoir and multi-agency coordination and emergency branches needed (peak staggering, power and navigation, failures, extreme floods)? (EP09-D)
  - In a system of several reservoirs, how is the joint flood-control storage shared: how much each reservoir passes on and how much it stores, within each dam's safety limits and the channel capacity between them? (J24)
- **Details:** [references/3.3-adaptive-logic.md](references/3.3-adaptive-logic.md)

### 3.4 Trade-offs and selection principles

- **Think:** How should conflicts among reservoir safety, downstream flood risk, and other operating objectives be considered when comparing alternative operating plans?
- **Do:** Define and organize evaluation criteria for safety, risk, and operating benefits, account for their relative importance, and compare feasible operating alternatives.
- **Checks:**
  - Which objectives conflict: safety against benefits, dam safety against downstream safety? (RP06-A)
  - How are limited resources allocated over time or across the system: store now or keep for later, upstream reservoirs taking over downstream tasks? (RP06-B)
  - Is safety treated as a non-compensable constraint, with benefits pursued only once it is met? (RP06-C)
  - Is a noninferior set kept instead of collapsing to one score too early, unless the objectives are commensurable? (RP06-D)
  - Does the final choice rest on preferences and ranking rules (weights, TOPSIS, fuzzy optimum, consultation) that are transparent and testable? (RP06-E)
  - Do flood scale, site purpose, and operating stage decide what the objective function contains? (RP06-F)
  - Is there a criteria system and decision matrix, with criteria screened, decorrelated, and weighted where needed? (EP08-A)
  - Is the ranking tested for stability against weights, methods, flood types, or deleted criteria? (EP08-B)
  - How is a compromise selected from the noninferior set (TOPSIS, fuzzy optimum, minimum composite risk)? (EP08-C)
  - When relevant: is there coarse screening before detailed evaluation, and is the final scheme decided by consultation? (EP08-D)
  - Is each option tested against the governing flood-safety standard before benefits are weighed, using the upper bound of its risk and not only the central estimate? (J14)
  - Is there a side-by-side table of how the options differ, a statement of which options are dominated, and a stated preference? (J15)
- **Details:** [references/3.4-trade-offs-and-selection.md](references/3.4-trade-offs-and-selection.md)

### 3.5 Model and method choice

- **Think:** Which model representation and solution method fit the problem, data, and computational budget, and why?
- **Do:** Use optimization, analytical derivation, enumeration, or calibration to determine release schedules, storage targets, operating water levels, or rule parameters for candidate reservoir operating strategies.
- **Checks:**
  - How is the reservoir system represented, and what is traded off for computation (reservoir aggregation, channel storage, local linearization, routing fidelity, scenario-tree size, compact rules)? (RP08-A)
  - Can optimal rules be derived analytically (KKT, equal marginal utility), and under which conditions do they hold? (RP08-B)
  - Which solution or search algorithm fits (genetic or evolutionary algorithms, global solvers, Monte Carlo search)? (RP08-C)
  - Which method computes uncertainty and risk (SDE, Bayesian network, maximum-entropy density, mixture distributions, continuous integration)? (RP08-D)
  - When relevant: how is a data-driven forecast model built (event clustering, input selection, LSTM, model combination)? (RP08-E)
  - When relevant: how are evaluation criteria handled (network weights, sensitivity, PCA, entropy weights)? (RP08-F)
  - Can analytical or piecewise rules be derived directly (KKT, equal marginal utility, heuristic steps)? (EP06-A)
  - Is a deterministic or multiobjective optimization formulated and solved to obtain schedules or noninferior sets? (EP06-B)
  - Is scenario-based stochastic optimization or rolling MPC used, optimizing over scenarios or trees and re-optimizing each step? (EP06-C)
  - With the rule form fixed, are thresholds, coefficients, or boundary levels searched or calibrated? (EP06-D)
  - Are structurally different alternatives kept for later evaluation and selection? (EP06-E)
- **Details:** [references/3.5-model-and-method-choice.md](references/3.5-model-and-method-choice.md)

## Stage 4. Test

### 4.1 Evidence and applicability

- **Think:** How can forecast value for operation be assessed, what conclusions do safety and benefit evidence support, and to which reservoirs and flood conditions do they apply?
- **Do:** Compare candidate policies with existing rules or alternative methods, and test their performance across different forecasts, flood events, operating horizons, and parameter settings.
- **Checks:**
  - Is the improvement compared with the right baselines (current rule, no-forecast, perfect-forecast) to isolate its true contribution? (RP09-A)
  - Is the result robust, or does it depend on one flood, one parameter set, one record, or the number of scenarios? (RP09-B)
  - Are the data and models credible before use: synthetic forecasts, error models, risk estimators? (RP09-C)
  - Does the result transfer to other sites, events, and institutions, or only to this one? (RP09-D)
  - Is the result explained by specific mechanisms rather than only reported as numbers? (RP09-E)
  - Is the plan compared with baselines under identical conditions (current rule, conventional operation, deterministic plans, historical operation)? (EP10-A)
  - Is it tested on historical events and trajectories, not only aggregates, and does the simulator agree with history? (EP10-B)
  - Are information conditions compared (no forecast, deterministic, ensemble, synthetic, perfect)? (EP10-C)
  - Are sensitivity, stress, and extreme tests done (parameters, error levels, scenario count, lead time, scaled floods)? (EP10-D)
  - Are holdout, transfer, or generalization tests done (leave-one-year-out, held-out events, other reservoirs, random seeds)? (EP10-E)
  - Is the method itself verified with independent samples or another method? (EP10-F)
  - Can the data resolve the difference claimed: how many independent extreme events does the record or sample hold, and what are the binomial or Monte Carlo standard errors? (J16)
  - Is the claimed benefit plausible by mass balance: what storage volume would it require, and is that volume available? (J17)
  - Is the evaluation closed-loop (the policy's own releases feed back into the state), out of sample (not tuned on the test events), and compared with simple and optimized alternatives (a simple forecast-informed rule, model predictive control, perfect foresight)? (J18)
- **Details:** [references/4.1-evidence-and-applicability.md](references/4.1-evidence-and-applicability.md)

### 4.2 Adoption (whenever the answer recommends or evaluates a change to operation)

- **Do:** For studies involving management practice, review proposed operating changes with relevant stakeholders, test them through pilot implementation when feasible, evaluate their performance, and revise operating rules or guidance accordingly.
- **Checks:**
  - When relevant: is there cross-agency review and staged screening (steering committee, workplan, staged viability assessment, rounds of consultation)? (EP11-A)
  - When relevant: is there a controlled pilot that temporarily modifies the operating manual and observes the effects? (EP11-B)
  - When relevant: what is the disposition (defer, research, fully assess, update the manual), and is there review and revision after the event? (EP11-C)
  - Who has the authority to approve the change, under which instrument (operating manual, annual flood-control plan, dam-safety regulation), how long approval takes, and what remains the legal basis until then? If the request names a country, name its institutions as far as you know them. (J19)
  - Which acceptance criteria are agreed in advance with the safety authority, and how is the change trialled (shadow operation beside the current rule, a temporary documented deviation)? (J20)
  - What triggers reversion to the current rule (forecast missing, late, or diverging from observations; equipment failure), who decides, and what is logged for audit? (J21)
  - Who must be warned of the change and of man-made releases (downstream public, emergency services, other operators), and what training, version control, and after-event review are needed? (J22)
- **Details:** [references/4.2-adoption.md](references/4.2-adoption.md)
