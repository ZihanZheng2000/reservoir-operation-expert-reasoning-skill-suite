# V05 Reference Route (judges only)

Source: Hydrology 2024, 11, 147, "Adaptive Operating Rules for Flood Control of a Multi-Purpose Reservoir" (Stânca–Costești, Prut River).

## (a) Key questions the authors had to settle
- Is the gauge record reliable enough to use? The rating curve above 500 m³/s was extrapolated, and the volumes at the gauge and at the dam did not match.
- How should the design flood be defined? Peak alone is not enough: volume, duration and shape matter because the flood volume (up to 2,400 mil. m³) far exceeds the control volume (665 mil. m³).
- Which flood shape is critical?
- How should rules be set per outlet and adapted in real time when the flood's AEP is unknown at warning time?

## (b) Methods and steps
1. Built a MIKE FLOOD unsteady routing model of the 159.74 km reach from Rădăuți–Prut to below the dam (360 cross-sections, 13 structures). They re-evaluated the rating curve iteratively and calibrated roughness (0.032 channel, 0.085 floodplain).
2. Ran univariate frequency analysis on the 1978–2020 record. Peaks used block maxima (BM) and peaks over threshold (POT) with several distributions. Volumes used two-threshold POT (400/190 m³/s). Johnson SB was chosen. The spread across distributions was reported as an epistemic uncertainty band (about 37% at 0.1%). Climate-change (CC) values were added. They discussed bivariate AND/OR isolines and maximum-discharge flood (MDF) vs maximum-volume flood (MVF) cases.
3. Built design hydrographs on the 2008 flood shape, which had the highest compactness coefficient γ = V/(D(Qmax−Qb)). Duration was derived from γ.
4. Built a simulation-optimization model: reservoir continuity plus outlet equivalence classes. The decision variables are the open and close levels (H′, H″) for each outlet class. The model used Nelder–Mead with a penalized objective: keep outflow near qmax, stay under the level limit, smooth successive releases, and meet the end volume.
5. Derived rules for 10%, 5%, 1% and 0.1% floods, with and without CC. This gave an adaptive framework with forecast-based decision points at 91.00 and 95.50 MASL and volume sub-classes. They also added a 10-day rainfall lookup table.

## (c) Validation
- Water balances for 2008 and 2010 closed within 54 and 62 mil. m³. Simulated reservoir levels and outflows matched the 2008 records.
- Compared the optimized rules against the original design-phase rules (1969-shape 0.1% flood) and the operators' actual 2008 rules.
- Tested the rules on the multi-peak 2010 shape.

## (d) Main findings
- Optimized rules cut the peak outflow for the design flood from 2,300 to 1,400 m³/s and use fewer gate manoeuvres.
- 10% CC flood: 94.17 MASL / 581 m³/s. 5% CC: 96.85 / 600. The same rules hold for floods up to about 2,000 m³/s.
- 2008 flood: 98.52 / 890 m³/s. 1%: 98.70 / 1,350. 1% CC: 98.74 / 2,440. 0.1%: 99.84 / 3,095. 0.1% CC: 100.74 / 3,650 (under 2 m of freeboard). The multi-peak 0.1% CC case: 100.04 / 3,225, easier to manage.
- Flood volume matters as much as peak. Bottom outlets must open early.
- Floods smaller than 1% stay within the riverbed's carrying capacity. Larger floods flood the downstream area, but the dam stays safe.

## (e) Limitations
- Short forecast horizon: 3 days, while volume classes need 5–10 days.
- Outlets are assumed never to fail (one gate jammed in 2008).
- Large distribution uncertainty at low AEPs. Uncertain CC uplift.
- Adaptive operation underperforms the perfect-foresight optimum.
- Univariate quantiles were used for the design hydrographs.
- Data are restricted.
- Future work: a decision support system (DSS) for blocked outlets and an extra spillway.
