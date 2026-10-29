# Research Skill Development — Development Questions (English test version)

Translation of `questions-zh.md` (the user-approved Chinese version, 2026-10-28). These are the 7 fixed development questions for internal skill iteration, not the final held-out test.

## U1 — Research Design

A PhD student wants to study whether staged (seasonal) flood-limited water levels could replace the single fixed flood-limited water level at a multipurpose reservoir (mainly for irrigation and hydropower) in a monsoon basin in India, so as to improve water-use efficiency while keeping flood control safe.

A town 40 km downstream is protected by the reservoir.

The data currently available are:

- 45 years of daily reservoir inflow records.
- The reservoir's level–storage and level–discharge-capacity relationships.
- 8 recent years of archived inflow forecasts with concurrent observations; forecast lead times are 1–5 days, updated daily.
- The current reservoir operating rule.

It is not yet confirmed whether any other data can be obtained.

Draft a study design, including: the research question, the data and methods needed, how to assess the effect of adjusting the flood-limited level on flood safety and on the other operating objectives, and what research results would be sufficient to support recommending a change to the current rule.

## U2 — Feasible Design Calculation

A reservoir in southern China has a design flood-limited water level of 152.0 m. Storage between 152 m and 154 m is 180 million m³.

The safe discharge at the downstream town's control section is 5,000 m³/s; the reservoir's maximum release capacity at 152 m is 7,500 m³/s. Between the dam and the town there is an ungauged intervening catchment that can add up to 1,200 m³/s during storms.

The inflow forecast has a lead time of 36 hours and is updated every 6 hours. Making the decision, issuing the downstream warning, and adjusting the gates take 8 hours in total. Before a flood, inflow is typically about 1,500 m³/s.

The operator wants to hold the level at 154 m when the forecast shows no flood, and to bring it down to 152 m before a flood arrives.

First calculate the theoretical maximum allowable level under these assumptions, then judge whether 154 m can serve as the actual operating upper limit. Explain which safety margins need to be considered, which verifications should be carried out, and what information is still missing before the final operating upper limit can be set.

## U3 — Critical Review of an Analysis

A consulting firm evaluated a new prerelease rule for a reservoir with a total storage of 600 million m³.

They used 12 years of 3-day inflow forecasts and fitted a normal distribution to the daily forecast errors. The fit did not distinguish season, flow magnitude, or forecast lead time; all errors were pooled.

They then generated 5,000 synthetic forecasts for each design flood, sampling each day's forecast error independently.

The firm's conclusion is that, in the 100-year design flood scenario, the new rule lowers the maximum outflow by 18% compared with the current rule, and it claims "95% confidence" in this conclusion.

The owner wants to adopt the new rule.

Review this analysis, identify the possible methodological problems and uncertainties, and state which additional analyses, verifications, or evidence you would require before recommending adoption of the new rule.

## U4 — Recommendation for Operational Adoption

A conference paper reports that, had a large reservoir used a machine-learning release model during the 2023 flood, its maximum outflow could have been 30% lower than under the release decisions the operators actually made.

The model was trained on historical data from 2010–2022. The paper demonstrates the model's effect mainly through a retrospective simulation of the 2023 flood event.

The head of the basin management agency wants to know whether the model should be adopted directly for the next flood season, replacing the current operating rule.

Advise the head of the agency: explain what conclusions the current evidence can support, which questions remain unresolved, and which evaluations and preparations should be carried out before actual adoption.

## U5 — Time-Critical Operational Decision

Two reservoirs in series jointly protect a city. The city is 10 hours of flow travel time downstream of the lower dam; water takes 18 hours to travel from the upper dam to the lower dam. An uncontrolled tributary between the two dams currently carries about 300 m³/s and can add up to 1,500 m³/s during storms.

The current situation of the two reservoirs:

| Item | Upper reservoir | Lower reservoir |
|---|---:|---:|
| Flood-control storage | 300 million m³ | 500 million m³ |
| Currently free share of flood-control storage | 40% | 85% |
| Maximum release capacity | 8,000 m³/s | 8,000 m³/s |
| Current inflow | 1,200 m³/s | — |
| Current release | 1,500 m³/s | 2,500 m³/s |

The safe flow at the city's control section is 6,000 m³/s.

The latest forecast is updated every 12 hours. It shows that the flood will begin to enter the upper reservoir in about 30 hours, with a cumulative inflow volume over the following 72 hours expected to be 250 million m³, within a possible range of 150–400 million m³.

The complete inflow hydrograph and a detailed forecast for the tributary between the dams are not yet available.

The operators propose three alternatives:

**(a)** Both reservoirs start prereleasing now.

**(b)** Only the lower reservoir starts prereleasing now.

**(c)** Take no prerelease action for now, and decide after the next forecast in 12 hours.

The flood-control headquarters needs a recommendation within one hour.

Based on the information available, give a conditional preferred alternative, and explain your main reasons, key assumptions, and the actions to take immediately. Also state which new information or risk thresholds would make you change the current recommendation. If the available information is not sufficient to support a single choice, state clearly the most important missing information and its effect.

## U6 — Multi-objective Trade-offs and Governance

A multipurpose reservoir serves downstream city flood control, hydropower, irrigation supply, and navigation.

The hydropower company proposes raising the flood-season operating level to increase generation revenue; the city's flood-control department and the irrigation district are concerned.

A study based on 40 years of historical data, combining probabilistic models and simulated scenarios, evaluated the current rule and three alternatives. The table gives the estimated indicators; no uncertainty intervals for the estimates have been provided yet.

| Scheme | Mean annual generation | Annual probability that city flow exceeds the safe threshold | End-of-flood-season irrigation storage reliability | Mean days per year with insufficient navigation flow |
|---|---:|---:|---:|---:|
| Current rule | 10.0 billion kWh | 1.0% | 92% | 12 days |
| A | 10.3 billion kWh | 1.0% | 90% | 14 days |
| B | 10.5 billion kWh | 1.3% | 95% | 9 days |
| C | 10.2 billion kWh | 0.9% | 85% | 18 days |

The basin commission must decide whether to adopt one of the new schemes or keep the current rule.

Advise the commission, answering the following:

1. How should the schemes be compared, and how should the trade-offs between the different operating objectives be handled?
2. Which scheme do you recommend taking forward, or should the current rule be kept? On what basis? Are conditions needed?
3. Which agencies and stakeholders should take part in the decision, and how should they take part?

## U7 — Model and Method Selection

A research team is developing a real-time release decision tool for a large flood-control reservoir.

The following data and conditions are available:

- 51-member ensemble inflow forecasts with a 10-day lead time, updated every 6 hours, with 20 years of hindcasts and the corresponding observations.
- The reservoir's level–storage and level–discharge-capacity relationships; the discharge capacity varies strongly with the level.
- A calibrated channel routing model covering the 120 km reach from the dam to the downstream control station.
- Two ungauged tributaries also enter this reach, and their real-time flows are uncertain.
- Each real-time decision must be computed within 30 minutes.

The operators want release recommendations that they can understand, actually carry out, and explain clearly to the regulator.

Propose how you would represent this reservoir–river system, which modelling and solution method you would choose, and why you would choose it rather than the main alternatives.

Also explain how you would verify that the chosen method meets the requirements for computational efficiency, physical constraints, decision reliability, and practical implementability. If some key data or engineering constraints are not yet clear, explain how you would handle these uncertainties in the preliminary design.
