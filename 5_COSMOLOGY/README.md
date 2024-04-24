## SN likelihood and chains

### Likelihood
The Likelihood file is `dessn5yr.py`
In the Likelihood provided, we analytically marginalize over M (SN absolute brightness) and H0 (See Sec. 3 in DES Collaboration 2024).
M and H0 are unconstrained by our data (do not use this sample to measure H0).

Use this likelihood with distances and cov matrixes in folder 4_DISTANCES_COVMAT.

### Chains
The chain folder includes all the cosmosis/emcee chains (see file header) for the four cosmological models tested in our analysis:
- Flat $`\Lambda`$CDM (flcdm sub-folder)
- $`\Lambda`$CDM (lcdm sub-folder)
- Flat $`w`$CDM (wlcdm sub-folder)
- Flat $`w_0 w_a`$CDM (w0wacdm sub-folder)
  
And for the different probes combination
- DES-SN only
- DES-SN + CMB (from Planck Collaboration et al. 2020)
- DES-SN + BAO and 3x2pt
- DES-SN + BAO and 3x2pt + CMB


