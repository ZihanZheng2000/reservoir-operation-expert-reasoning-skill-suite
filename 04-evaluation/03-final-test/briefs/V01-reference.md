# V01 Reference Route (judges only)

Source: dynamic control of the flood limited water level (DC-FLWL) at the Three Gorges Reservoir, with the forecast error domain taken into account (Water Resources Management, 2025).

## (a) Key questions the authors had to settle
- How to describe forecast error at each lead time from 1 to 7 days.
- How to set the upper limit of the dynamic FLWL range for each lead time.
- How to account for the fact that graded, threshold-based release rules tolerate some forecast error. As long as the forecast and the observed inflow fall in the same rule grade, the decision does not change.
- How to choose, in real time, which lead time to trust, and how to combine forecasts from several lead times.
- How to define upstream risk and downstream risk.

## (b) Methods and steps
1. **Forecast error.** Relative forecast error was computed for each lead time from historical forecasts and observed inflows. Normal distributions were fitted by maximum likelihood and passed a chi-square test at the 0.9 level. Monte Carlo sampling then produced 1,000 inflow scenarios per lead time (actual inflow x (1 + error)).
2. **Upper limit of the dynamic range (pre-release capacity constraint).** The storage that can be released during the effective lead time was calculated. The effective lead time is the forecast lead time minus 2 h. Releases were capped at 35,000 m3/s less lateral inflow, and inflow was set to the average flood-season inflow of 25,500 m3/s. The lower limit of the range is 145 m.
3. **Three-module DC-FLWL model.**
   - Rising stage: pre-release down to 145 m.
   - Flood stage: follow the original flood rules.
   - Falling stage: pre-refill up to the upper limit, while keeping power output.
4. **Error domain.** The error domain is the relative gap between the forecast maximum inflow and the release-rule thresholds, giving bounds [θL, θU]. Only the pre-release threshold of 35,000 m3/s was used.
5. **Probability of a correct decision.** For each lead time, this is the probability that the observed inflow falls inside the error domain. Starting from the longest lead time, lead times were dropped until this probability reached a threshold Pθ, set to 0.9995 in the base case. If no lead time passes, operation uses real-time inflow only.
6. **Risk measures.** Upstream risk RP is the share of scenarios in which the end-of-rising-stage level is above 145 m. Downstream risk RL is the share of time in which outflow exceeds 35,000 m3/s.

## (c) Validation
- A rolling daily simulation was run from 1 June to 23 July 2019, focused on the rising flood stage ending 24 July 2019.
- Five options were compared over 1,000 scenarios each:
  1. 3-day lead time (design practice)
  2. 6-day lead time (longest that meets the accuracy requirement)
  3. 6-day lead time with accuracy relaxed by 20%
  4. 6-day lead time with errors enlarged by 20%
  5. coupled lead times selected through the error domain
- A sensitivity sweep tested 10,000 values of Pθ, with 1,000 simulations each.

## (d) Main findings
- **Forecast accuracy.** The share of forecasts within 20% relative error fell with lead time: 99.2, 97.0, 93.1, 88.9, 85.4, 80.8 and 76.9% for 1 to 7 days.
- **Upper limit of the dynamic range.** It rose from 146.48 m (1-day lead time) to 153.72 m (7-day lead time).
- **Results by option** (energy in 10^8 kWh):

| Option | Energy | Upstream risk | Downstream risk |
|---|---|---|---|
| 1 | 186.74 | 0.435 | 0.066 |
| 2 | 187.89 | 0.966 | 0.082 |
| 3 | 192.38 | 1.000 | 0.027 |
| 4 | 181.56 | 0.573 | 0.121 |
| 5 | 189.09 | 0.020 | 0.058 |

- **Option 5 against Option 1.** Energy rose by 2.83 x 10^8 kWh (1.5%), as reported in the paper. Upstream risk fell by 0.415 (95.4%) and downstream risk by 0.005 (7.6%).
- **Reading the comparison.** The usable lead time adapts to conditions: longer lead times are used when inflows are low, shorter ones as inflows near the threshold. The value of Pθ trades risk against benefit, and the authors recommend Pθ > 0.998 for the TGR.

## (e) Limitations
- The study covers a single reservoir. Cascade or parallel reservoir systems with hydraulic links are left for future work.
- Only the pre-release rule threshold was used to build the error domain.
- Forecast errors were assumed to be normal and independent for each lead time.
- Validation covers one flood season and one rising stage in 2019.
- Refill failure was assumed not to occur, which the authors justify by the water-rich south China setting.
- The paper's own figures do not fully agree. Table 2 gives 189.09 for Option 5 against 186.74 for Option 1, a gain of about 2.35, while the text claims 2.83 and also cites 189.20.
