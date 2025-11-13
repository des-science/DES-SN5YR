## SN likelihood and chains

### Likelihood
The Likelihood file is `Dovekie_cosmosis_likelihood.py`
In the Likelihood provided, we analytically marginalize over M (SN absolute brightness) and H0 (See Sec. 3 in DES Collaboration 2024).
M and H0 are _unconstrained_ by our data (_do **not** use this sample to measure H0_). When you run SN only chains using our likelihood, you can vary or fix H0 and M, it doesn't matter cause in both cases, these parameters are marginalized over.

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

