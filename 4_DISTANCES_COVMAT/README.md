### Hubble diagrams
We provide two Hubble diagrams, one including only the essential information for cosmology (DES-SN5YR_HD.csv) and one including additional metadata (DES-SN5YR_HD+MetaData.csv). 

Using the metadata, SN distances are calculated as:

`MU` $`=`$ -2.5log$`_{10}`$(x0) $`~+~\alpha`$x1 $`~-~\beta`$c$`~\pm~\gamma/2~-~`$biasCor_mu$`~-~M_{0~\mathrm{avg}}`$

**DES-SN5YR_HD.csv**

- `CID` - Candidate ID
- `IDSURVEY` - {10:'DES', 61:'CFA1', 62:'CFA2', 63:'CFA3S', 64:'CFA3K' ,65:'CFA4p2', 66:'CFA4p3', 150:'FOUND'}
- `zHD` - Hubble Diagram Redshift (with CMB and VPEC corrections)
- `zCMB` - CMB Corrected Redshift
- `zHEL` - Heliocentric Redshift
- `MU` - SN distances (assuming H0 of 70)
- `MUERR_FINAL` - SN distance uncertainties (renormalized for BEAMS prob of being core-collapse, also referred to as MUERR_RENORM)

**DES-SN5YR_HD+MetaData.csv**

- `CID` - Candidate ID
- `IDSURVEY` - {10:'DES', 61:'CFA1', 62:'CFA2', 63:'CFA3S', 64:'CFA3K' ,65:'CFA4p2', 66:'CFA4p3', 150:'FOUND'}
- `zHD` - Hubble Diagram Redshift (with CMB and VPEC corrections)
- `zHDERR` - Hubble Diagram Redshift Uncertainty
- `zCMB` - CMB Corrected Redshift
- `zCMBERR` - CMB Corrected Redshift Uncertainty
- `zHEL` - Heliocentric Redshift
- `zHELERR` - Heliocentric Redshift Uncertainty
- `MU` - SN distances (assuming H0 of 70)
- `MUERR_RENORM` - SN distance uncertainties (renormalized for BEAMS prob of being core-collapse, also referred to as MUERR_RENORM)
- `PROB_SNNV19` - Prob of being Ia from SuperNNova trained on sims generated using core-collapse templates from Vincenzi et al 2019 (Nominal)
- `PROB_SNNDESCC` - Prob of being Ia from SuperNNova trained on sims generated using core-collapse templates from Jones et al 2017
- `PROB_SNNJ17` - Prob of being Ia from SuperNNova trained on sims generated using core-collapse templates from DES data
- `PROB_SCONE` - Prob of being Ia from SCONE trained on sims generated using core-collapse templates Vincenzi et al 2019
- `PROB_SNIRFV19` - Prob of being Ia from SNIRF trained on sims generated using core-collapse templates from Vincenzi et al 2019
- `PROBCC_BEAMS` - BEAMS Prob of being core-collapse (see eq. 6 in Vincenzi et al 2024)
- `c` - SALT2 color
- `cERR` - SALT2 color uncertainty
- `x1` - SALT2 stretch
- `x1ERR` - SALT2 stretch uncertainty
- `mB` - SALT2 uncorrected brightness
- `mBERR` - SALT2 uncorrected brightness uncertainty
- `x0` - SALT2 light curve amplitude where $m_x = -2.5\mathrm{log}_{10}(x0)$ used in the modified Tripp equation
- `x0ERR` - SALT2 light curve amplitude uncertainty
- `COV_x1_c` - SALT2 fit covariance between x1 and c
- `COV_x1_x0` - SALT2 fit covariance between x1 and x0
- `COV_c_x0` - - SALT2 fit covariance between c and x0
- `HOST_RA` - Host Galaxy RA
- `HOST_DEC` - Host Galaxy DEC
- `HOST_ANGSEP` - Angular separation between SN and host (arcsec)
- `HOST_DDLR` - directional light radius distance between SN and host (dimentionless)
- `VPEC` - Peculiar velocity (km/s)
- `VPECERR` - Peculiar velocity uncertainty (km/s)
- `MWEBV` - Milky Way E(B-V)
- `HOST_LOGMASS` - Host Galaxy Log Stellar Mass
- `HOST_COLOR` - Host Galaxy rest-frame u-r color
- `PKMJD` - Fit Peak Date
- `PKMJDERR`  - Fit Peak Date Uncertainty
- `NDOF` - Number of degrees of freedom in SALT2 fit
- `FITCHI2` - SALT2 fit chi squared
- `FITPROB` - SNANA Fitprob
- `biasCor_mu` - Bias correction applied to brightness m_b
- `biasCorErr_mu`  - Uncertainty on bias correction applied to brightness m_b
- `biasCor_mu_COVSCALE` - Reduction in uncertainty due to selection effects (multiplicative)
- `biasCor_mu_COVADD`  - Uncertainty floor as given by the intrinsic scatter model (quadriture)

### Global Parameters ###
- $\alpha =  0.16087 \pm 0.00152$ 
- $\beta = 3.11780 \pm 0.03530$
- $\gamma = 0.03754 \pm 0.00798$
- $M_{0~\mathrm{avg}} = -29.95821$

Note, these global parameters are determined from the likelihood analysis of all the SNe on the Hubble diagram.


### Statistical and Stat+Systematic Covariance matrices
The Statistical and Stat+Systematic Covariance matrices (both 1829x1829 Matrix) are provided in
- STATONLY.txt.gz
- STAT+SYS.txt.gz (all systematics)

Single-syst cov matrix are also available in SingleSYS_CovMatrix.



