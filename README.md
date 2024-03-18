# DES-SN5YR_DataRelease
Data Release for the DES Supernova 5yr Cosmological analysis. Extra documentation and tutorials available at https://desdrtest.readthedocs.io/en/main/

### Summary and Overview of this Github folder

**0_DATA**
The light curves are produced using the Scene Modelling Photometry pipeline described in Brout et al. 2019a and Sanchez et al. 2024 (in prep.).
The full set of light curves will be released with Sanchez et al. 2024 (in Collaboration Wide Review).

**1_SIMULATIONS:**
This folder includes the 25 DES mocks used for testing and validating the DES cosmological pipeline. We provide both simulated Ia and non-Ia DES light curves. Please take a look at the folder for further details.

**2_LCFIT_MODEL**:
This folder contains the SALT3 fitting models used (1) for our nominal analysis (SALT3.DES5YR) and (2) to incorporate SALT3-related systematics in our uncertainties (SALT3.DES5YR-SYS).

**3_CLASSIFICATION**:
The file contains classification probabilities for the 1635 DES SNe used in the DES-SN5YR cosmological analysis (see folder for info on the different classification algorithms used). 

**4_DISTANCES_COVMAT**:
This folder contains all the files to fully reproduce the cosmological contours presented in [DES Collaboration (2024)](https://arxiv.org/abs/2401.02929)
- Data vector with redshifts (zHD) and distance moduli (MU) for the 1829 SNe (194 low-z + 1635 DES) used in the DES-SN5YR cosmological analysis.
- STAT-only covariance matrix.
- STAT+SYST covariance matrix.
- Single systematic covariance matrices (see README therein).

**7_PIPPIN_FILES**:
This folder includes the pippin input files needed to reproduce DES simulations and cosmological analysis.
