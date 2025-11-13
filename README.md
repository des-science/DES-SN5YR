# DES-SN 5YR Data Release

[![Documentation Status](https://readthedocs.org/projects/des-sn-dr/badge/?version=latest)](https://des-sn-dr.readthedocs.io/en/latest/?badge=latest)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.12720778.svg)](https://doi.org/10.5281/zenodo.12720778)

> This github page supercedes the original DES-SN5YR results from Vincenzi et al. 2024, which is still available on [Zenodo](https://doi.org/10.5281/zenodo.12720778) and [this tagged version](https://github.com/des-science/DES-SN5YR/releases/tag/1.3).

## The Dark Energy Survey Supernova DES-Dovekie Results

This repo contains the data, simulations, pipeline inputs and results from the Dark Energy Survey Supernova Program Dovekie cosmology results.

Please check our [ReadTheDocs](https://des-sn-dr.readthedocs.org) for all details on contents and ancillary data description.

### Summary and Overview of this Github folder

**0_DATA**
The light curves are produced using the Scene Modelling Photometry pipeline described in [Brout et al. 2019a](https://ui.adsabs.harvard.edu/link_gateway/2019ApJ...874..106B/doi:10.3847/1538-4357/ab06c1) and [Sánchez et al. (2024)](https://ui.adsabs.harvard.edu/link_gateway/2024ApJ...975....5S/doi:10.3847/1538-4357/ad739a).
The full set of light curves is released with [Sánchez et al. (2024)](https://ui.adsabs.harvard.edu/link_gateway/2024ApJ...975....5S/doi:10.3847/1538-4357/ad739a).

**1_SIMULATIONS:**
This folder includes the 25 DES mocks used for testing and validating the DES cosmological pipeline. We provide both simulated Ia and non-Ia DES light curves. Please take a look at the folder for further details.

**2_LCFIT_MODEL**:
This folder contains the SALT3 fitting models used
- (1) for our nominal analysis (SALT3.DOVEKIE)
- (2) to incorporate SALT3-related systematics in our uncertainties (SALT3.DOVEKIE-SYS).

**3_CLASSIFICATION**:
The file contains classification probabilities for the 1635 DES SNe used in the DES-Dovekie cosmological analysis (see folder for info on the different classification algorithms used).

**4_DISTANCES_COVMAT**:
This folder contains all the files to fully reproduce the cosmological contours presented in [Popovic et al. 2026](https://arxiv.org/abs/2511.07517)
- Data vector with redshifts (zHD) and distance moduli (MU) for the 1820 SNe used in the DES-Dovekie cosmological analysis.
- STAT-only covariance matrix.
- STAT+SYST covariance matrix.
- Single systematic covariance matrices (see README therein).

**5_COSMOLOGY**:
SN likelihood and chains for the different cosmological models and data used in the [Popovic et al. 2026](https://arxiv.org/abs/2511.07517) paper.

**6_DCR_CORRECTIONS**
Wavelength dependent corrections implemented for SMP 5YR, that depend on the airmass and color of the observed events.

**7_PIPPIN_FILES**:
This folder includes the pippin input files needed to reproduce DES simulations and cosmological analysis.


## References and citing this work

> The Dark Energy Survey Supernova Program: A Reanalysis Of Cosmology Results And Evidence For Evolving Dark Energy With An Updated Type Ia Supernova Calibration. Monthly Notices of the Royal Astronomical Society. [Popovic et al. 2026.](https://ui.adsabs.harvard.edu/abs/2025arXiv251107517P/abstract)

> The Dark Energy Survey Supernova Program: Cosmological Analysis and Systematic Uncertainties. The Astrophysical Journal, Volume 975, Issue 1, id.86, 31 pp. [Vincenzi et al (2024).](https://ui.adsabs.harvard.edu/link_gateway/2024ApJ...975...86V/doi:10.3847/1538-4357/ad5e6c)

> Light curve and ancillary data release for the full Dark Energy Survey Supernova Program. The Astrophysical Journal, Volume 975, Issue 1, id.5, 12 pp [Sánchez et al. (2024)](https://ui.adsabs.harvard.edu/link_gateway/2024ApJ...975....5S/doi:10.3847/1538-4357/ad739a)

#### The legacy DES-SN5YR cosmological results can be found at:

> The Dark Energy Survey: Cosmology Results With ~1500 New High-redshift Type Ia Supernovae Using The Full 5-year Dataset. The Astrophysical Journal Letters, Volume 973, Issue 1, id.L14, 20 pp. [DES Collaboration (2024).](https://ui.adsabs.harvard.edu/link_gateway/2024ApJ...973L..14D/doi:10.3847/2041-8213/ad6f9f)

**Please, for the full documentation refer to [ReadTheDocs](https://des-sn-dr.readthedocs.org).**
