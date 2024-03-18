## PIPPIN Input Files 
Pippin code available at https://github.com/dessn/Pippin
See SNANA library for additional auxiliary files: https://zenodo.org/records/4015340

These are the pippin input file (and additional auxiliary files) to reproduce the DES-SN5YR analysis..

D5yr_biascor.yml: produce biasCor simulations for low-z samples and DES sample
D5yr_sim_nominal.yml: produce 10 DES-like and low-z-like simulated samples 
                      (for validation)
D5yr_analysis.yml: run the full cosmological analysis both on data 
                   and on the 10 simulations

**Order of operations:**
1) Look at the top of the three files D5yr_biascor.yml, D5yr_sim_nominal.yml, D5yr_analysis.yml 
 and check the keys that require to be changes (marked with **CHANGE**). Check also that the OUTPUT path is correct.

2) 
  - Run D5yr_biascor.yml     to produce biasCor sims
  - Run D5yr_sim_nominal.yml to produce 10 data-like samples

3) Run D5yr_analysis.yml: full analysis on data and sim-data.


(Last modified: March 2024 by M.Vincenzi)  
