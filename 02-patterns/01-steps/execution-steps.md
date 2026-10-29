# E01–E50 Execution Steps

## E01

| Step |
|---|
| E1. Assemble the TGR case and current-rule baseline |
| E2. Calibrate and validate the TGR inflow forecast |
| E3. Check forecast accuracy and derive forecast-error realizations |
| E4. Calculate the candidate upper bound from capacity-constrained pre-release |
| E5. Execute the refill branch during flood recession |
| E6. Apply threshold-based TGR decision logic and safety constraints |
| E7. Quantify risk for each candidate decision/level |
| E8. Search for a converged Monte Carlo dynamic bound |
| E9. Compare simulated schemes with the current rule |

## E02

| Step |
|---|
| E1. Configure the case study and horizon |
| E2. Generate synthetic ensemble inflow forecasts |
| E3. Build and solve the scenario-based stochastic program |
| E4. Trace the uncertain Pareto front |
| E5. Calculate alternative-specific exceedance risks |
| E6. Assemble the stochastic MCDM decision matrix |
| E7. Sample uncertain preferences and rank alternatives |
| E8. Apply the current-period release and update the state |
| E9. Evaluate update value and uncertainty effects |

## E03

| Step |
|---|
| E1. Set the flood-season state, boundaries, and targets |
| E2. Describe the real-time DC-FLWL operational trigger |
| E3. Build the rolling two-stage water balance |
| E4. Represent Stage-2 forecast error and release uncertainty |
| E5. Convert downstream risk and water-supply requirements into bounds |
| E6. Test the reduced DC-FLWL feasibility conditions |
| E7. Optimize carryover storage and safety margin |
| E8. Select the piecewise analytical hedging branch |
| E9. Convert optimal storage to Stage-1 release and enforce the release floor |
| E10. Roll the horizon and update decisions |
| E11. Estimate the case-study forecast and error model |
| E12. Derive case rules and parameter scenarios |
| E13. Compare three operation policies |
| E14. Evaluate water conservation and modelled flood risk |

## E04

| Step |
|---|
| E1. Assemble the TGR forecast-operation data |
| E2. Compute rolling relative-error reductions |
| E3. Split reductions by season |
| E4. Fit and screen marginal distributions |
| E5. Check serial dependence and fit joint copulas |
| E6. Generate single-period reduction samples and check moments |
| E7. Reconstruct forecast uncertainty at each lead time |
| E8. Generate synthetic daily flows and predicted inflows |
| E9. Apply forecast-informed pre-release and routing rules |
| E10. Estimate and compare extreme flood risk |

## E05

| Step |
|---|
| E1. Set up the two-stage reservoir representation |
| E2. Construct losses, risk, and constraints |
| E3. Reduce stage-2 mass balance to an allocation problem |
| E4. Generate the feasible zone and endpoint conditions |
| E5. Derive and classify preference-dependent hedging rules |
| E6. Calculate the mass-balance uncertainty threshold |
| E7. Select the active constraint branch for (r_{max}) |
| E8. Evaluate preference–uncertainty interaction |
| E9. Illustrate the procedure with Nierji Reservoir |

## E06

| Step |
|---|
| E1. Configure TGR case and operating thresholds |
| E2. Fit three-day forecast-error model |
| E3. Generate dependent forecast-error vectors |
| E4. Generate synthetic daily flood hydrographs |
| E5. Fit distributions for hydraulic/storage/wind uncertainty |
| E6. Construct LHS uncertainty samples |
| E7. Route each simulated flood with pre-release and sampled uncertainties |
| E8. Calculate traditional threshold exceedance risk |
| E9. Calculate component and system entropy |
| E10. Check simulations and interpret risk results |

## E07

| Step |
|---|
| E1. Build the LMO water-balance simulator |
| E2. Assemble hindcast and common operational inputs |
| E3. Test model assumptions against historical operations |
| E4. Configure the EFO risk test |
| E5. Simulate member trajectories under no release and detect risky horizons |
| E6. Construct and constrain member release schedules |
| E7. Select the current release across risky members and horizons |
| E8. Combine releases, update state, and roll forward |
| E9. Run the EO and PFO comparison branches |
| E10. Evaluate storage, releases, and downstream flood indicators |

## E08

| Step |
|---|
| E1. Compute uncertain initial conditions |
| E2. Specify uncertain routing inputs |
| E3. Generate feasible operation samples |
| E4. Build and fit BN |
| E5. Perform prior risk inference |
| E6. Perform posterior prediction or diagnosis |
| E7. Compare and interpret risk |

## E09

| Step |
|---|
| E1. Fit dry-period distribution |
| E2. Estimate effective forecast lead time |
| E3. Calculate two-period over-FLWL volume |
| E4. Run worst-case release calculation |
| E5. Check historical event behavior |

## E10

| Step |
|---|
| E1. Define RFH and uncertainty |
| E2. Solve outer allocation |
| E3. Solve inner allocation |
| E4. Route and update |
| E5. Compare operation rules |
| E6. Stress forecast and horizon choices |

## E11

| Step |
|---|
| E1. Estimate forecast skill/error |
| E2. Build flood-volume scenarios |
| E3. Calculate candidate and selected D-PSL |
| E4. Simulate operation under D-PSL |
| E5. Compare scenarios and current practice |

## E12

| Step |
|---|
| E1. Fit forecast-error distribution |
| E2. Calculate early pre-release |
| E3. Optimize flood-regulating trajectories |
| E4. Select preferred rules |
| E5. Simulate and compare |

## E13

| Step |
|---|
| E1. Assemble case data and operating context |
| E2. Represent EFO storage and release decisions |
| E3. Construct multivariate forecast-error records |
| E4. Model conditional bias and heteroscedasticity |
| E5. Remove dependence and fit residual distributions |
| E6. Reimpose dependence by Schaake shuffle and kNN |
| E7. Reconstruct syn-HEFS forecasts |
| E8. Reconstruct syn-GEFS and force HEFS |
| E9. Verify synthetic forecast ensembles |
| E10. Validate rare-event forecast attributes |
| E11. Run hindcast EFO operational validation |
| E12. Extend EFO testing to pre-hindcast events |

## E14

| Step |
|---|
| E1. Assemble and classify the case data |
| E2. Select inputs and train base forecasters |
| E3. Build Cloud deterministic forecasts |
| E4. Fit error marginals and adjacent copula |
| E5. Generate SE-Cloud scenarios with Gibbs sampling |
| E6. Create comparator forecast scenarios |
| E7. Simulate constrained reservoir operation |
| E8. Run deterministic forecast-value experiment |
| E9. Run TSO ensemble-versus-deterministic comparison |
| E10. Run MRO for large-flood trade-offs |
| E11. Post-assess under actual and noisy inflows |
| E12. Test confidence/scenario sensitivity and limitations |

## E15

| Step |
|---|
| E1. Generate multi-step probabilistic forecasts |
| E2. Apply two-stage water-balance constraints |
| E3. Execute HPFOR branch logic |
| E4. Encode rule parameters and cascade constraints |
| E5. Evaluate five objectives under cascade dynamics |
| E6. Repair/rank constraint violations |
| E7. Run RSEA and comparator algorithms |
| E8. Summarize final HPFOR solutions |
| E9. Inspect representative operational traces |
| E10. Compare with HFOR and state limits |

## E16

| Step |
|---|
| E1. Assemble Oroville forecasts, inflows, and constraints |
| E2. Define storage objective and shared constraints |
| E3. Train EFO risk-curve policies |
| E4. Run daily MPC |
| E5. Run cumulative guide-curve policy |
| E6. Run baseline and perfect MPC benchmarks |
| E7. Construct event and training designs |
| E8. Evaluate flood-pool robustness |
| E9. Assess water-supply refill and forecast diagnostics |

## E17

| Step |
|---|
| E1. Assemble six-site event and forecast inputs |
| E2. Form scenario-based MPC state forecasts |
| E3. Enforce release and ramp constraints; roll forward |
| E4. Define required flood pool and performance |
| E5. Define forecast-policy branches |
| E6. Enumerate global parameter combinations |
| E7. Train and evaluate individual DT classifiers |
| E8. Extract cross-reservoir thresholds |
| E9. Diagnose interactions and event dependence |

## E18

| Step |
|---|
| E1. Organize a FIRO pilot and workplan |
| E2. Establish site baseline and operating constraints |
| E3. Assemble forecasts and monitoring capability |
| E4. Define site-specific FIRO alternatives |
| E5. Simulate/evaluate candidate scenarios with required decision tools |
| E6. Compare outcomes across multiple site metrics |
| E7. Check physical, data, and implementation adequacy |
| E8. Temporarily implement and observe a pilot modification |
| E9. Route candidates through the FIRO Screening Process |
| E10. Branch to defer, research, assess, or update |
| E11. Update WCM/WCP and preserve future adaptability |

## E19

| Step |
|---|
| E1. Define the reservoir and seasonal operating context |
| E2. Assemble atmospheric, hydrologic, and reservoir data |
| E3. Set idealized forecast horizons for scheme comparison |
| E4. Compute PP from atmospheric water balance |
| E5. Transform PP into floodwater volume |
| E6. Derive VCWL under a prerelease sequence |
| E7. Establish the common FIRO upper bound |
| E8. Execute VPS-FIRO's three-line operating sequence |
| E9. Run the PS-FIRO and historical comparator scenarios |
| E10. Inspect representative Typhoon In-Fa and Muifa/Hinnamnor events |
| E11. Compute 50-event statistics and interpret indexes |
| E12. Validate hydrological and vapor-data components |

## E20

| Step |
|---|
| E1. Define case reservoir and risk thresholds |
| E2. Generate a stochastic flash-flood ensemble |
| E3. Set model inputs and initial state |
| E4. Encode and run the per-event MILP RFCM |
| E5. Define and enumerate candidate RFCM parameters |
| E6. Extract maximum release and storage per event |
| E7. Estimate empirical distributions and release/storage risk indices |
| E8. Aggregate risk and select the balanced parameter set |
| E9. Construct and inspect the Pareto front |
| E10. Compare cases, sensitivity, and calibrated versus non-calibrated behavior |
| E11. Record limitations before operational transfer |

## E21

| Step |
|---|
| E1. Acquire and manage basin data |
| E2. Simulate upstream reservoir effects and naturalized flows |
| E3. Forecast precipitation/floods at multiple lead times |
| E4. Generate candidate cooperation schemes |
| E5. Submit schemes for multi-department consultation |
| E6. Pre-discharge TGR using long-lead warning |
| E7. Release upstream reserved capacity to stagger peaks |
| E8. Adjust generation, shipping, and levels during execution |
| E9. Reanalyze performance and maintain crisis branches |

## E22

| Step |
|---|
| E1. Set the Dez Dam case and operation data |
| E2. Assemble and bias-correct NWP precipitation ensembles |
| E3. Train the sequential LSTM inflow forecaster |
| E4. Evaluate forecast skill and uncertainty representation |
| E5. Formulate multiobjective flood-operation functions |
| E6. Apply water-balance, release, storage, and fluctuation constraints |
| E7. Grid-search objective weights and run GA |
| E8. Run the deterministic/no-forecast policy |
| E9. Run ensemble-member and ensemble-mean policies |
| E10. Compare release, storage, and safety outcomes |
| E11. Document limitations and future operating route |

## E23

| Step |
|---|
| E1. Assimilate observations and generate hydrological disturbances |
| E2. Verify forecast products before optimization use |
| E3. Reduce ensemble to a scenario tree |
| E4. Choose and embed downstream routing model |
| E5. Solve multi-stage stochastic MPC |
| E6. Compare event trajectories and constraint behavior |

## E24

| Step |
|---|
| E1. Specify two-stage water balance and forecast variables |
| E2. Compute uncertainty and expected damage |
| E3. Compute total EFSM and critical thresholds |
| E4. Select and solve the EFSM allocation rule |
| E5. Convert EFSM to release and storage decisions |
| E6. Enforce storage capacity and extreme-flood response |
| E7. Demonstrate three cases |

## E25

| Step |
|---|
| E1. Parameterize forecast ensemble and reservoir state |
| E2. Compute candidate storm releases |
| E3. Evaluate failure and expected damage |
| E4. Categorize storms and simplify cost |
| E5. Search feasible Qh and identify optimum |
| E6. Run sensitivity and comparison branches |

## E26

| Step |
|---|
| E1. Build phase-wise inputs and benchmark rules |
| E2. Prepare uncertainty and risk functions |
| E3. Calculate feasible V1 and solve the analytical HR |
| E4. Generate and apply three-zone rule |
| E5. Run event and rolling-horizon simulations |
| E6. Compare rule performance and forecast-precision sensitivity |

## E27

| Step |
|---|
| E1. Define routing and operating-rule inputs |
| E2. Estimate lead-time error statistics |
| E3. Select and parameterize forecast rule |
| E4. Generate random inflow scenarios |
| E5. Route Monte Carlo floods and record MWL |
| E6. Magnify return-period floods and estimate exceedance risk |
| E7. Summarize thresholds and interpret risk |

## E28

| Step |
|---|
| E1. Calibrate and verify the inflow forecast |
| E2. Estimate relative forecast-error scale |
| E3. Specify flood input and operating rules |
| E4. Transfer error to stochastic routing |
| E5. Convert and summarize level paths |
| E6. Compute design/check operation risk |
| E7. Run sensitivity and threshold analyses |

## E29

| Step |
|---|
| E1. Fit and validate the BFS |
| E2. Generate candidate inflow paths |
| E3. Instantiate dynamic FLWL bounds |
| E4. Execute the forecast-triggered control step |
| E5. Evaluate downstream safety |
| E6. Evaluate water-use and energy benefits |
| E7. Compare schemes and paired forecast runs |

## E30

| Step |
|---|
| E1. Set uncertainty model and case data |
| E2. Obtain deterministic mean routing |
| E3. Fit local discharge/storage coefficients |
| E4. Recursively calculate level-error moments |
| E5. Calculate temporal covariance and risk |
| E6. Run case sensitivity and action examples |

## E31

| Step |
|---|
| E1. Parameterize uncertainty sources |
| E2. Obtain mean routing and local curve coefficients |
| E3. Recursively calculate level-error moments |
| E4. Recursively calculate level-error dependence and risks |
| E5. Run Experiments 1–4 |
| E6. Isolate factors and compare combined models |
| E7. Produce decision-support interpretations |

## E32

| Step |
|---|
| E1. Define the multi-reservoir case and variables |
| E2. Generate physically consistent training samples |
| E3. Build the DBN structure |
| E4. Discretize and learn parameters |
| E5. Run prediction inference and threshold risks |
| E6. Run diagnosis inference |
| E7. Test uncertainty level, comparators, and limitations |

## E33

| Step |
|---|
| E1. Specify state and routing equations |
| E2. Build lead-time forecast scenarios |
| E3. Evaluate stage-1 scenario failures |
| E4. Construct aligned stage-2 design-event inputs |
| E5. Precompute the stage-2 risk relationship |
| E6. Combine the two risk stages |
| E7. Generate Monte Carlo verification samples |
| E8. Verify risk against the reference statistic |
| E9. Solve the constrained rolling-horizon operation |
| E10. Compare regular and optimized case operation |

## E34

| Step |
|---|
| E1. Define forecast-error variables and system links |
| E2. Calibrate a correlated t-copula |
| E3. Sample discretized inflow scenarios |
| E4. Build the deterministic benchmark |
| E5. Formulate MOSP scenario objectives and constraints |
| E6. Generate and select noninferior solutions |
| E7. Solve nonlinear models |
| E8. Run rolling-horizon recourse |
| E9. Diagnose scenario coverage and forecast behavior |
| E10. Compare solutions and historical events |

## E35

| Step |
|---|
| E1. Define the design event and hindcast frame |
| E2. Generate deterministic forecast scenarios |
| E3. Generate evolving probabilistic forecast ensembles |
| E4. Assess forecast ensemble behavior |
| E5. Build the reservoir dynamic/constraint model |
| E6. Define and solve MPC objective |
| E7. Reduce PSF ensemble to a mass-conservative tree |
| E8. Run closed-loop deterministic or tree MPC |
| E9. Sweep branch counts and horizons |
| E10. Evaluate flood-control and supply outcomes |

## E36

| Step |
|---|
| E1. Estimate forecast quality |
| E2. Convert quality metric to error σ |
| E3. Generate and structure inflow scenarios |
| E4. Formulate scenario-wise operation |
| E5. Minimize expected highest level |
| E6. Extract scenario maximum levels |
| E7. Fit POME density and check its form |
| E8. Integrate risk and conduct sensitivity sweeps |

## E37

| Step |
|---|
| E1. Inventory operation modes and risk factors |
| E2. Fit and test forecast net-rainfall error |
| E3. Apply the FBO rule to forecast input |
| E4. Construct CO comparison operation |
| E5. Generate CO Monte Carlo floods and route them |
| E6. Generate FBO Monte Carlo forecasts and route actual inflow |
| E7. Scale counts to risk rates and compare modes |
| E8. Probe forecast-error remedies |

## E38

| Step |
|---|
| E1. Generate feasible joint-operation schemes |
| E2. Define forecast-error samples |
| E3. Represent discharge and storage uncertainty |
| E4. Jointly sample uncertainty realizations |
| E5. Run uncertain operation simulations |
| E6. Calculate complementary risk indicators |
| E7. Aggregate reservoir indicators with AHP weights |
| E8. Rank schemes with weighted TOPSIS |
| E9. Repeat and compare across flood hydrographs |

## E39

| Step |
|---|
| E1. Establish case thresholds and operating rules |
| E2. Fit the forecast-error density |
| E3. Derive cumulative-rainfall density |
| E4. Construct the hazard surface and single-hazard boundary |
| E5. Form UHE and IHE domains |
| E6. Calculate joint density and integrate risk |
| E7. Compare AMIT with MLTP |
| E8. Sweep FLWL and report operational implication |

## E40

| Step |
|---|
| E1. Build ensemble inflow forecasts |
| E2. Simulate reservoir with scenario inputs |
| E3. Count forecast-horizon failures |
| E4. Estimate post-horizon risk conditionally |
| E5. Combine the two risk stages |
| E6. Define scenario-optimized operation |
| E7. Compare historical and optimized schemes |

## E41

| Step |
|---|
| E1. Divide the flood season and prepare design floods |
| E2. Quantify forecast error as a fuzzy variable |
| E3. Generate candidate IOWLs |
| E4. Run fuzzy simulation for each IOWL/frequency |
| E5. Form K and test feasibility |
| E6. Select stage bounds |
| E7. Verify with extreme-risk rate |

## E42

| Step |
|---|
| E1. Construct lead-time-specific error samples |
| E2. Fit and select IGMD |
| E3. Validate error-model fit |
| E4. Sample uncertainty and construct ensembles |
| E5. Assess ensemble coverage |
| E6. Count design-flood exceedance risk |
| E7. Optimize generation for each inflow input |
| E8. Calculate curtailment and compare periods |

## E43

| Step |
|---|
| E1. Assemble hydrologic and hydraulic inputs |
| E2. Calibrate rainfall-runoff prediction |
| E3. Build the internal control model |
| E4. Formulate and solve each MPC problem |
| E5. Advance the closed-loop simulation |
| E6. Compare operation scenarios and inspect bottlenecks |

## E44

| Step |
|---|
| E1. Form aggregation reservoirs |
| E2. Calculate CSR and aggregate storage |
| E3. Run pre-discharge operation |
| E4. Compute two-stage flood risk |
| E5. Optimize and decompose WLFS boundaries |
| E6. Compare and verify candidate operations |

## E45

| Step |
|---|
| E1. Define probability and loss measures |
| E2. Aggregate CVaR over the planning horizon |
| E3. Establish Scheme A |
| E4. Build and route nonstationary scenarios |
| E5. Solve B1 risk-constrained adaptation |
| E6. Solve B2 with CVaR protection |
| E7. Compare metrics and infer operating implication |

## E46

| Step |
|---|
| E1. Simulate reservoir continuity |
| E2. Execute pre-release rule |
| E3. Execute peak-stage rule |
| E4. Execute post-peak release reduction |
| E5. Estimate recession inflow |
| E6. Calibrate rules sequentially with BOBYQA |
| E7. Validate and benchmark |

## E47

| Step |
|---|
| E1. Generate non-dominated operating alternatives |
| E2. Define the original criteria system |
| E3. Construct BP training samples |
| E4. Train and verify BP network |
| E5. Calculate importance and sensitivity |
| E6. Apply comprehensive discrimination threshold |
| E7. Compare MCDM rankings before and after selection |

## E48

| Step |
|---|
| E1. Define the cascade case and flood inputs |
| E2. Enumerate and route six alternatives |
| E3. Calculate the criterion matrix |
| E4. Diagnose correlation and transform criteria |
| E5. Compute improved entropy weights |
| E6. Score alternatives using three MCDM methods |
| E7. Compare rankings and inspect selected policy |
| E8. Record omitted uncertainty and deployment checks |

## E49

| Step |
|---|
| E1. Define forecast error and case data |
| E2. Fit marginals and construct dependent uncertainty scenarios |
| E3. Set XHD operation parameters and thresholds |
| E4. Calculate the six RMOO objectives |
| E5. Enforce physical and boundary constraints |
| E6. Solve RMOO and CCP and evaluate search quality |
| E7. Compare objective distributions and select compromises |
| E8. Diagnose the selected mechanism in adverse scenarios |
| E9. Test event-scale behavior and document limitations |

## E50

| Step |
|---|
| E1. Set the multireservoir case and daily baseline data |
| E2. Implement baseline release rules and constraints |
| E3. Specify infrastructure and hydrologic inputs |
| E4. Add FIRO risk tolerance and TOCS multiplier |
| E5. Evaluate forecast skill and form forecast inputs |
| E6. Simulate four policy variants |
| E7. Optimize Forecast and Perfect parameters |
| E8. Compare storage and flood-control outcomes |
| E9. Analyze site attributes and policy equifinality |
| E10. Perform LOOCV and restrict the TOCS bound after failures |
