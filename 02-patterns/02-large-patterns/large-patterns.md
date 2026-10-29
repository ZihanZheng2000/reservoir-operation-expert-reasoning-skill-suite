# Large patterns: nine reasoning and eleven execution patterns

Final definitions (2026-10-01). Names and shared questions/tasks are the user's rewrite of the AI draft (`history/2-human-revised/patterns-en.md`); RP08 was added by user decision after step coding found 38 method-choice reasoning steps (26 papers) that no other pattern covered. These definitions are the basis of the step coding in `../03-step-coding/`. Small patterns are in `../05-small-patterns/`; the integrated version is `../06-taxonomy/`.

## Reasoning patterns

| ID | Candidate category | Shared question |
| --- | --- | --- |
| RP01 | Diagnose limitations of existing reservoir operating rules under flooding risk | Under what conditions do existing reservoir operating rules fail to balance flood-risk management with other reservoir objectives, and what limitations indicate a need for adjustment? |
| RP02 | Identify uncertainties that affect flood risk and reservoir operation decisions | Which forecast errors, uncertainties in flood evolution, and dependencies among uncertainty sources can affect reservoir operating decisions and flood risk? |
| RP03 | Judge forecast reliability and timing for reservoir flood-operation decisions | How reliable are available flood forecasts over the time periods that matter for decision-making, and what reservoir operating decisions can they support at different stages of a flood event? |
| RP04 | Justify reservoir and downstream flood risk and acceptable safety limits | How should unsafe flood outcomes be defined, and how should acceptable risk levels or safety thresholds be established for the reservoir and downstream areas? |
| RP05 | Judge physical and operational feasibility of reservoir adjustments | Is there enough forecast lead time to adjust reservoir operations? Is there enough storage and release capacity? Can adjustments be made without violating downstream safety constraints? |
| RP06 | Frame reservoir operating trade-offs and selection principles | How should conflicts among reservoir safety, downstream flood risk, and other operating objectives be considered when comparing alternative operating plans? |
| RP07 | Consider adaptive reservoir operation across flood-event stages | As flood conditions and forecasts change, when should reservoir operations be adjusted or replanned, and when should operators shift from prerelease to flood-control or refill actions? |
| RP08 | Select model representation and solution methods | Which model representation and solution method fit the problem, data, and computational budget, and why? |
| RP09 | Judge evidence and applicability for reservoir operation adjustments | How can forecast value for operation be assessed, what conclusions do safety and benefit evidence support, and to which reservoirs and flood conditions do they apply? |

## Execution patterns

| ID | Candidate category | Shared task |
| --- | --- | --- |
| EP01 | Prepare reservoir-operation data and baseline rules | Assemble hydrological, storage, release, and downstream-control data; define initial conditions and operating horizons; and establish existing operating rules as the baseline for comparison. |
| EP02 | Develop and verify flood and reservoir inflow forecasts | Prepare meteorological and hydrological inputs, develop flood and inflow forecasts, and evaluate their accuracy over the lead times needed for reservoir operation. |
| EP03 | Model operational uncertainty and generate possible scenarios | Represent forecast errors and other operational uncertainties, account for their important dependencies, and generate plausible scenarios for reservoir operation and risk analysis. |
| EP04 | Model reservoir and downstream flood responses under uncertainty | Use reservoir and river-system models to simulate how inflow scenarios and operating decisions affect reservoir water levels, storage, releases, downstream flows, and flood risk. |
| EP05 | Calculate operating safety bounds and check feasibility | Convert storage capacity, release capacity, forecast lead time, and safety requirements into feasible operating limits, and check whether candidate release or water-level plans satisfy those limits. |
| EP06 | Solve for candidate operating plans and rule parameters | Use optimization, analytical derivation, enumeration, or calibration to determine release schedules, storage targets, operating water levels, or rule parameters for candidate reservoir operating strategies. |
| EP07 | Calculate risks, losses, and benefits of candidate operating plans | For each candidate operating plan, calculate reservoir and downstream flood risk, potential flood losses, and benefits associated with other reservoir objectives. |
| EP08 | Organize evaluation criteria and select operating alternatives | Define and organize evaluation criteria for safety, risk, and operating benefits, account for their relative importance, and compare feasible operating alternatives. |
| EP09 | Translate operating results into staged actions and rolling updates | Convert operating plans into release or water-level targets for different flood stages, and update these actions as reservoir conditions and forecasts change. |
| EP10 | Compare and test reservoir operating policies | Compare candidate policies with existing rules or alternative methods, and test their performance across different forecasts, flood events, operating horizons, and parameter settings. |
| EP11 | Conduct operational consultation, pilot implementation, and rule revision | For studies involving management practice, review proposed operating changes with relevant stakeholders, test them through pilot implementation when feasible, evaluate their performance, and revise operating rules or guidance accordingly. |

## RP08 boundaries

- **RP08 vs RP02:** RP02 decides which uncertainties matter for the decision; RP08 decides how to represent them computationally (for example copula, SDE, mixture, fuzzy, scenario tree).
- **RP08 vs RP06:** RP06 decides which objectives and selection principles govern the choice among plans; RP08 decides which formulation, derivation, or algorithm is used to obtain or evaluate plans.
- **RP08 vs RP09:** RP09 judges what results establish after testing; RP08 judges whether a method or representation is suitable before results are produced. In all 18 papers containing both, RP08 appears before RP09.
- **RP08 vs EP02/EP03/EP04/EP06/EP08:** those execution patterns build and run the chosen forecast, uncertainty, simulation, solution, or evaluation method; RP08 is the reasoning about why that method or representation was chosen.
- **Domain-specific vs general:** families inside RP08 will be tagged as reservoir-specific (system representation and computational trade-offs) or general method choice, so that later skill comparisons can separate domain skill content from general research skill content.
