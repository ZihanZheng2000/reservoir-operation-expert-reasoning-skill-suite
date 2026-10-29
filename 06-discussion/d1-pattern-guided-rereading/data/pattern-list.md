# Pattern list for re-reading

Reasoning patterns (RP) are judgments a study makes: what it must understand, judge, or justify.
Execution patterns (EP) are concrete research activities a study carries out.

## RP01 Diagnose limitations of existing operating rules
Core question: Under what conditions does an existing reservoir operating rule fail to balance flood risk with other objectives, and which limitations indicate that it needs adjustment?
- RP01-A Fixed flood-control allocation causes a safety-benefit imbalance: A fixed flood-limited level, guide curve, or flood pool wastes water in small floods or under-protects in large floods
- RP01-B The rule cannot use available forecasts or their uncertainty: Forecasts exist, but the rule uses only the current state, treats forecasts as certain, or relies on a horizon that is too short
- RP01-C The rule boundary omits system objects: The rule covers only one reservoir and ignores cascade coupling or downstream control points
- RP01-D The basis of the rule is outdated or too narrow: The manual is decades old, the flood regime is assumed stationary, or parameters were calibrated on a few events

## RP02 Identify decision-relevant uncertainty
Core question: Which uncertainties can change releases, storage, risk, or rule selection and therefore must be represented?
- RP02-A Forecast uncertainty must enter the decision: Decisions rely on forecasts; treating them as certain causes over- or under-preparation
- RP02-B Uncertainty does not come only from forecasts: Initial level, hydrograph shape, discharge capacity, storage curves, and wind also change outcomes
- RP02-C Keep only decision-relevant sources and state exclusions: Too many sources exist; screen by importance and tractability and state what was excluded
- RP02-D Error structure is not a single fixed distribution: Errors vary with lead time, flow, and season, or are non-normal, multimodal, or fuzzy
- RP02-E Errors are dependent: Errors correlate across times, sites, variables, or ensemble members; assuming independence understates joint risk
- RP02-F Derive a distribution from accuracy metrics or deterministic forecasts: With limited data, infer the error distribution from qualified rate, NSE, or a point forecast
- RP02-G Trace how uncertainty reaches levels, releases, and risk: State the propagation path, where it is amplified, and when new information resolves it
- RP02-H The size of uncertainty changes the optimal decision: A threshold exists beyond which the optimal storage or release strategy switches

## RP03 Judge forecast reliability and timing
Core question: Which forecast horizons and flood stages can support which operating actions?
- RP03-A Reliability varies with lead time; use forecasts by stage: Near-term forecasts are accurate and long-lead ones coarse; different lead times support different actions
- RP03-B Forecasts must arrive early enough, with the right indicator: The lead time must cover the time needed to draw down; choose variables that signal floods earlier
- RP03-C Verify forecast quality before use: Whether the forecast meets requirements is a precondition for using it
- RP03-D Forecast accuracy is not operational value: High skill does not guarantee better operation; bound the value with no-forecast and perfect-forecast references
- RP03-E Derive the required forecast accuracy from acceptable risk: Beyond some error the forecast stops being useful; or a risk target implies a minimum accuracy
- RP03-F Beyond the forecast horizon and unequal horizons across reservoirs: Risk continues after the lead time; upstream and downstream reservoirs have different lead times
- RP03-G How to use a forecast that may be wrong: Choose a conservative quantile, correct when wrong, or fall back to measurement-based rules

## RP04 Define flood risk and acceptable safety
Core question: What counts as unsafe, which measures should quantify risk, and how much risk is acceptable?
- RP04-A Define reservoir-side failure events: Define unsafe as maximum level or required flood pool exceeding a safety threshold
- RP04-B Define downstream and engineering consequences: Levee failure, release above safe channel capacity, dam-break losses, shortage and lost generation
- RP04-C One exceedance probability is not enough; add other measures: Add loss, tail (CVaR), entropy, duration, or resilience
- RP04-D Set an acceptable-risk benchmark: Use current-rule risk, design or protection standards, or a stationary benchmark as the pass line
- RP04-E Derive operating bounds from acceptable risk: Convert the risk limit into a safety margin, level ceiling, or the inflow quantile that must be accommodated
- RP04-F Several safety objects or thresholds at once: Dam versus downstream, multiple reservoirs, or several thresholds interact and need an explicit combination rule
- RP04-G Aggregate risk over time: Distinguish point and whole-process risk, within and beyond the lead time, and weight by flood occurrence probability

## RP05 Judge physical and operational feasibility
Core question: Can the proposed prerelease, target level, or release adjustment actually be carried out in time, space, facilities, and institutions?
- RP05-A Hard limits of facilities and operation: Level, storage, outlet capacity, release change, and ramping limits exclude impossible actions
- RP05-B Is there enough time: Can drawdown or prerelease finish within the lead time; longer lead time permits a higher ceiling
- RP05-C Is there enough storage space: Can remaining storage absorb the design flood, and can released water be refilled
- RP05-D Downstream and system conditions limit local action: Travel time, channel storage, and uncontrolled local inflow mean locally feasible is not system-feasible
- RP05-E Model feasibility is not implementability: Regulations, authority, standard tools, data, computing time, and departmental approval

## RP06 Frame trade-offs and selection principles
Core question: When flood safety, supply, storage, and hydropower cannot all be optimized, what principle governs the choice?
- RP06-A Identify conflicting objectives: Safety and benefits trade against each other, or dam safety trades against downstream safety
- RP06-B Allocate limited resources over time or across the system: Store now or keep for later; upstream reservoirs take over downstream tasks
- RP06-C Safety first: define the safe domain, then optimize benefits: Safety is a non-compensable constraint; benefits are pursued only once it is met
- RP06-D No single optimum: keep a noninferior set: Do not collapse to one score too early; aggregate only when objectives are commensurable
- RP06-E The final choice depends on preferences and ranking rules: Weights, TOPSIS, fuzzy optimum, or multi-agency consultation, made transparent and testable
- RP06-F Formulate objectives to fit the problem: Flood scale, site purpose, and operating stage decide what the objective function contains

## RP07 Define adaptive logic across the flood event
Core question: As a flood develops, when should an action be started, changed, suspended, or reversed?
- RP07-A Different flood stages need different actions: Prerelease, rising-limb detention, peak, recession, and refill each follow their own rules
- RP07-B Switch actions by thresholds: When a forecast value, risk, or available water crosses a threshold, switch to another branch
- RP07-C Rolling update: execute only the next step: Plan over the whole horizon, execute only the current period, and recompute when new information arrives
- RP07-D Share current decisions; let future decisions branch with information: Two-stage or scenario-tree structure: one action until uncertainty resolves, then branch
- RP07-E Correction and fallback when the forecast is wrong: Correct by error sign, adjust gradually, or fall back to measurement-based rules
- RP07-F Seasonal staging and multi-year adjustment: Split the flood season into stages, or adjust bounds period by period under nonstationarity

## RP08 Select model representation and solution methods
Core question: How should the operating problem be turned into a model that is computable and credible enough, and which representation and method are chosen for what reason?
- RP08-A Reservoir system representation and computational trade-offs: Reservoir aggregation, channel storage, local linearization, routing-model fidelity, scenario-tree size, compact rules
- RP08-B Analytical derivation route: Derive optimal rules via KKT or equal marginal utility and state when they hold
- RP08-C Choice of solution and search algorithm: Genetic and evolutionary algorithms, global solvers, Monte Carlo search
- RP08-D Methods for computing uncertainty and risk: SDE, Bayesian networks, maximum-entropy densities, mixture distributions, continuous integration
- RP08-E Construction choices for data-driven forecast models: Event clustering, MIC input selection, LSTM, model combination
- RP08-F Methods for handling evaluation criteria: Network weights, sensitivity, PCA, entropy weights

## RP09 Judge evidence strength and applicability
Core question: What does the evidence establish, under which conditions, and where does the claim stop?
- RP09-A Improvement must be compared with the right baseline: Use current rule, no-forecast, and perfect-forecast comparators to isolate the true contribution
- RP09-B Robustness: sensitivity, stress, and holdout tests: Does the result depend on one flood, one parameter set, one record, or the number of scenarios
- RP09-C Data and models must be credible first: Check synthetic forecasts, error models, and risk estimators before use
- RP09-D Applicability depends on site, event, and institutions: Results from one reservoir, period, or basin do not transfer automatically
- RP09-E Explain why the result occurs: Attribute improvements or failures to specific mechanisms rather than only reporting numbers

## EP01 Prepare data and baseline rules
Core task: Before modeling or comparison, how should a reproducible and fair case baseline be established?
- EP01-A Assemble hydrologic, forecast, and operating data: Collect inflow, rainfall, forecast hindcasts, and operating records, aligned in time and space
- EP01-B Describe the physical system and safety thresholds: Storage curves, discharge capacity, characteristic levels, downstream control points, multi-reservoir links
- EP01-C Encode current or tested rules in executable form: The current rule as comparator, or the forecast rule under test as explicit parameters
- EP01-D Set initial state, events, and experiment boundaries: Initial level, design floods, time window, lead time, and deliberate simplifying assumptions

## EP02 Build and verify forecasts
Core task: How should inflow or flood forecasts be produced for reservoir decisions, and how should their reliability be demonstrated?
- EP02-A Build or train a forecast model: Hydrologic or data-driven models, probabilistic forecasts, or precursor indicators
- EP02-B Prepare and correct forecast inputs: Bias correction, downscaling, assimilation, naturalized flows, assembling hindcasts
- EP02-C Quantify forecast error and skill by lead time: Compare historical forecasts with observations to get error samples, qualified rate, reliable horizon
- EP02-D Verify operational usability of forecasts: Coverage, extremes, comparison with reference forecasts, site monitoring capability

## EP03 Model uncertainty and generate scenarios
Core task: How should decision-relevant uncertainty be converted into scenarios usable for simulation and optimization?
- EP03-A Specify or fit error and variable distributions: Normal, maximum-entropy, mixture, fuzzy membership, seasonal fitting, or derived from accuracy metrics
- EP03-B Preserve dependence when generating: Copulas, VAR, Schaake shuffle, generation conditional on the previous day
- EP03-C Generate forecast scenarios and ensembles: Monte Carlo perturbation, LHS, MMFE, synthetic ensembles, quantile paths
- EP03-D Generate or scale design floods and stochastic flood events: Floods beyond the historical range for stress testing and risk estimation
- EP03-E Reduce ensembles to scenario trees: Keep representative branches so current decisions are shared
- EP03-F Write non-forecast uncertainty into the water balance: Initial storage, discharge coefficient, storage curve, wind; stochastic-differential state
- EP03-G Check that generated scenarios are faithful: Statistics, coverage, dependence structure, extreme-event attributes

## EP04 Simulate reservoir and downstream responses
Core task: How should inflow scenarios and operating actions be converted into levels, storage, flows, and downstream consequences?
- EP04-A Build a reservoir water-balance simulator and compute trajectories: Advance storage, level, and release per period for single or cascade reservoirs; check against history when possible
- EP04-B Simulate basin, channel, and downstream processes: Channel routing, local inflow, naturalized flow, channel storage, downstream station levels
- EP04-C Propagate uncertainty to levels and flows: Route many scenarios, SDEs, or moment recursions; collect maxima and other outputs
- EP04-D Replace full simulation with surrogate or probabilistic models: Bayesian networks, simplified state-space models, precomputed risk relationships

## EP05 Calculate safety bounds and check feasibility
Core task: How should safety, physical, and operating requirements become explicit checks on candidate actions?
- EP05-A Calculate feasible level or storage ceilings: From release capacity, lead time, and refill, compute how high the level can be raised
- EP05-B Derive bounds from risk or safety requirements and screen: Convert acceptable risk into release intervals or margins, then check each candidate
- EP05-C Impose facility constraints in simulation or optimization: Release, change, storage, and ramping limits; handle candidates that violate them
- EP05-D Check implementation readiness: Are monitoring, data, and tools sufficient to support operation

## EP06 Generate candidate plans and rule parameters
Core task: How should objectives, constraints, and scenarios become release schedules, target levels, or rule parameters?
- EP06-A Derive analytical or piecewise rules: Use KKT, equal marginal utility, or heuristic steps to obtain piecewise hedging rules directly
- EP06-B Formulate and solve deterministic or multiobjective optimization: Write objectives and constraints, solve with GA, NSGA, MILP, etc., to obtain schedules or noninferior sets
- EP06-C Scenario-based stochastic optimization and rolling MPC: Optimize expected objectives over scenarios or trees; MPC re-optimizes each step
- EP06-D Search or calibrate rule parameters: With the rule form fixed, search or calibrate thresholds, coefficients, and boundary levels
- EP06-E Enumerate structurally different alternatives: Keep several structurally different plans for later evaluation and selection

## EP09 Translate plans into staged, rolling actions
Core task: How should a technical plan become release or level instructions that can be executed now and updated later?
- EP09-A Convert plan results into the current release: From target storage, safety margins, or member schedules, compute this period's release
- EP09-B Execute staged or branching rules: Prerelease, normal, peak, recession, and refill branches switched by thresholds
- EP09-C Rolling update and closed-loop recomputation: Execute only the first step, update state and forecast, recompute; correct when forecast bias is detected
- EP09-D Multi-reservoir and multi-agency coordination and emergency branches: Cascade peak staggering, power and navigation coordination, emergency plans for failures or extreme floods

## EP07 Calculate risks, losses, and benefits
Core task: How should the safety consequences and other benefits of each candidate plan be quantified consistently?
- EP07-A Calculate threshold-exceedance risk: Count or integrate the probability that maximum level, release, or required flood pool exceeds a threshold
- EP07-B Calculate losses, tail, and composite risk: Expected loss, CVaR, entropy, duration, loss ratios
- EP07-C Calculate benefits and non-safety indicators: Storage, refill rate, generation, spill, curtailment, downstream flow frequency
- EP07-D Combine risk across objects and hazards: Union/intersection of thresholds, weighted multi-reservoir aggregation, criteria matrices
- EP07-E Combine risk across time and stages: Within and beyond the lead time, point versus whole process, weighted by flood occurrence probability

## EP08 Organize criteria and select alternatives
Core task: When feasible alternatives have no single optimum, how should a transparent choice be made?
- EP08-A Build the criteria system and decision matrix: List criteria and directions; screen, decorrelate, and weight criteria when needed
- EP08-B Rank and test ranking stability: Check whether rankings change with weights, methods, flood types, or deleted criteria
- EP08-C Select a compromise from the noninferior set: Use TOPSIS, fuzzy optimum, or minimum composite risk to choose one plan
- EP08-D Staged screening and multi-agency consultation: Coarse screening before detailed evaluation; final scheme decided by consultation

## EP10 Compare and test operating policies
Core task: How should an adjustment be compared with a suitable baseline and tested without introducing unacceptable failure modes?
- EP10-A Compare with baselines under identical conditions: Against the current rule, conventional operation, deterministic plans, or historical operation
- EP10-B Test with historical events and trajectories: Look beyond aggregates at typical events and simulator agreement with history
- EP10-C Compare information conditions: No forecast, deterministic, ensemble, synthetic, and perfect forecasts
- EP10-D Sensitivity, stress, and extreme tests: Parameters, error levels, scenario count, lead time, scaled floods
- EP10-E Holdout, transfer, and generalization tests: Leave-one-year-out, held-out events, cross-reservoir thresholds, random seeds
- EP10-F Verify the method itself: Use independent samples or another method to check risk estimates or evaluation results

## EP11 Consult, pilot, and revise rules
Core task: How should a technically feasible adjustment pass institutional review, pilot learning, and formal rule revision?
- EP11-A Organize cross-agency review and staged screening: Steering committee, workplan, staged viability assessment, rounds of consultation
- EP11-B Controlled pilot: Temporarily modify the operating manual and observe the effects
- EP11-C Disposition and rule revision: Defer, research, fully assess, or update the manual; review after the event and revise
