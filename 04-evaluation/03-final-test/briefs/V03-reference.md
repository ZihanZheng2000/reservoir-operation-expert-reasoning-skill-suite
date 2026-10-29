# V03 Reference Route (judges only)

Source: J. Hydrol. 620 (2023) 129421. The paper is a multi-objective robust optimization of real-time reservoir flood control under forecast uncertainty, with Lishimen Reservoir as the case study.

## (a) Questions the authors had to settle
- How to produce short-term inflow forecasts, and how to represent their uncertainty as an input to operations.
- How to combine several forecast models into one deterministic forecast.
- How to measure flood-storage use across the whole event, rather than in each time step or by peak reduction alone. This includes avoiding operation that is "too risky" or "too conservative".
- How to define upstream and downstream risk objectives over many forecast scenarios.
- How to collapse each candidate solution's performance across scenarios into one value so the optimizer can rank it.
- How to pick one final operating plan from the Pareto set.

## (b) Methods, in order
1. Built three ML inflow forecasters: BP, LSTM and ELM. Inputs were hourly rainfall from six gauges at lags 0-18 h (114 inputs, chosen by cross-correlation). Inputs were min-max normalized, Adam was the optimizer and NSE was the loss.
2. Used 22 floods: 16 for training with 4-fold cross-validation split by whole events (12 train, 4 validation per fold) and 6 for testing.
3. Combined the three base models with a stacking ensemble (SEM) using a linear-regression meta-model on out-of-fold predictions.
4. Generated stochastic forecast scenarios for the 2004 Rananim flood (48 h) by perturbing hyperparameters (hidden nodes, batch size, dropout). Scenarios below an NSE threshold were dropped; the text gives both 0.75 and 0.85. They then took 100 scenarios per model at equal NSE intervals, 300 in total.
5. Defined a new index, RRCA: the time-average over the event of normalized inflow divided by normalized remaining flood storage. The target is 1.
6. Built a deterministic 3-objective model (minimize the sum of squared releases, minimize the peak level, minimize |1-RRCA|). It was run with the SEM forecast (MOSEM) or with observed inflow (MOOB).
7. Built the robust model MOROU with 5 objectives:
   - maximum probability of exceeding the level limit;
   - maximum probability of exceeding the release limit;
   - fraction of hours above the level limit;
   - fraction of hours above the release limit;
   - probability that RRCA is below 0.8 or above 1.
   Constraints covered mass balance, level and release bounds, ramping limits, and the stage-storage and stage-discharge curves.
8. Proposed the scenario-to-point (STP) method: compute a regret value per scenario and use the minimax-regret (worst-case) value as the individual's fitness. They report a "worst-case" set and an "optimal-case" (minimum-regret) set.
9. Solved with NSGA-III (population 100, 500 generations, parallelized).
10. Chose a compromise solution using combined AHP and entropy weights (50/50).

## (c) Validation
- Forecasts were scored with NSE, RMSE, MAE and R2 across folds and on the test set.
- Operations were compared across MOROU, MOSEM and MOOB (the observed-inflow control).
- An ablation, MOROU-noF5, dropped the RRCA objective.
- All results come from a single flood event at a single reservoir.

## (d) Main findings
- BP gave test NSE of 0.87-0.91, LSTM 0.84-0.87 and ELM 0.87-0.88. SEM reached NSE 0.900 and R2 0.912. SEM beat the worst base model, not the best.
- Under MOROU's worst case, upstream exceedance probability was 0.77-0.917 and downstream 0.027-0.043. The optimal case gave much lower and narrower risks.
- Maximum release ranges: MOROU 876-1006 m3/s, MOSEM 341-1218 m3/s, MOOB 677-1303 m3/s.
- Maximum level ranges: MOROU 176.93-180.85 m, MOSEM 176.74-184.29 m, MOOB 177.68-182.74 m.
- MOROU's peak level was 1.87% lower than MOSEM and 1.03% lower than MOOB (the abstract says "about 1.5%").
- The compromise solution kept release below 1000 m3/s, cutting the peak by 22.78% vs MOOB and 17.34% vs MOSEM.
- Adding RRCA lowered the mean maximum release from 941.2 to 898.6 m3/s (-4.52%) with a similar mean peak level (180.03 vs 180.14 m). The mean RRCA was 1.138 vs 1.140, with a maximum of 1.723 without RRCA.

## (e) Limitations
- Only forecast uncertainty is modelled. Measurement error, routing and decision-delay uncertainty are not.
- No parameter sensitivity analysis was done, and hyperparameters were tuned by trial.
- The flood sample is small (22 events), and the test covers one large flood at one reservoir.
- Only one ensemble method and one optimizer were tried.
- The scenarios come from hyperparameter perturbation, not a calibrated error model.
- The data are confidential.
- The paper has internal inconsistencies: flood capacity is given as 35.7 vs 31.4 million m3, the NSE screening threshold as 0.75 vs 0.85, and the peak-level reduction as 1.5% in the abstract.
