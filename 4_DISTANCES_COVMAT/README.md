### Hubble diagrams
We provide two Hubble diagrams, one including only the essential information for cosmology (`DES-SN5YR_HD.csv`) and one including additional metadata (`DES-SN5YR_HD+MetaData.csv`).

Using the metadata, SN distances are calculated as:

`MU` $`=`$ -2.5log$`_{10}`$(x0) $`~+~\alpha`$x1 $`~-~\beta`$c$`~\pm~\gamma/2~-~`$biasCor_mu$`~-~M_{0~\mathrm{avg}}`$

**DES-SN5YR_HD.csv**

- `CID` - Candidate ID
- `IDSURVEY` - {10:'DES', 61:'CFA1', 62:'CFA2', 63:'CFA3S', 64:'CFA3K' ,65:'CFA4p2', 66:'CFA4p3', 150:'FOUND'}
- `zHD` - Hubble Diagram Redshift (with CMB and VPEC corrections)
- `zCMB` - CMB Corrected Redshift
- `zHEL` - Heliocentric Redshift
- `MU` - SN distances (assuming H0 of 70)
- `MUERR_FINAL` - SN distance uncertainties (renormalized for BEAMS prob of being core-collapse)

**DES-SN5YR_HD+MetaData.csv**

- `CID` - Candidate ID
- `CIDint` - Candidate ID integer (same as CID except for those starting with letters e.g. sn2000aa)
- `IDSURVEY` - {10:'DES', 61:'CFA1', 62:'CFA2', 63:'CFA3S', 64:'CFA3K' ,65:'CFA4p2', 66:'CFA4p3', 150:'FOUND'}
- `TYPE` - Type of supernova, 1=Type Ia (everything in this file is 1)
- `zHEL` - Heliocentric Redshift
- `zHELERR` - Heliocentric Redshift Uncertainty
- `zCMB` - CMB Corrected Redshift
- `zCMBERR` - CMB Corrected Redshift Uncertainty
- `zHD` - Hubble Diagram Redshift (with CMB and VPEC corrections)
- `zHDERR` - Hubble Diagram Redshift Uncertainty
- `VPEC` - Peculiar velocity (km/s)
- `VPECERR` - Peculiar velocity uncertainty (km/s)
- `MWEBV` - Milky Way E(B-V)
- `HOST_ZSPEC` - Host spectroscopic redshift (heliocentric frame, same as zHEL).
- `HOST_ZSPECERR` - Uncertainty in host spectroscopic redshift.
- `HOST_RA` - Host Galaxy RA
- `HOST_DEC` - Host Galaxy DEC
- `HOST_ANGSEP` - Angular separation between SN and host (arcsec)
- `HOST_DDLR` - directional light radius distance between SN and host (dimentionless)
- `HOST_LOGMASS` - Host Galaxy Log Stellar Mass
- `HOST_LOGMASS_ERR` - Uncertainty in Host Galaxy Log Stellar Mass
- `HOST_COLOR` - Host Galaxy rest-frame u-r color
- `HOST_COLOR_ERR` - Uncertainty in Host Galaxy rest-frame u-r color
- `PKMJD` - Fit Peak Date
- `PKMJDERR`  - Fit Peak Date Uncertainty
- `x1` - SALT3 stretch
- `x1ERR` - SALT3 stretch uncertainty
- `c` - SALT3 color
- `cERR` - SALT3 color uncertainty
- `mB` - SALT3 uncorrected brightness
- `mBERR` - SALT3 uncorrected brightness uncertainty
- `mB_corr` - Tripp1998 corrected/standardized mB magnitudes
- `x0` - SALT3 light curve amplitude where $m_x = -2.5\mathrm{log}_{10}(x0)$ used in the modified Tripp equation
- `x0ERR` - SALT3 light curve amplitude uncertainty
- `COV_x1_c` - SALT3 fit covariance between x1 and c
- `COV_x1_x0` - SALT3 fit covariance between x1 and x0
- `COV_c_x0` - - SALT3 fit covariance between c and x0
- `NDOF` - Number of degrees of freedom in SALT3 fit
- `FITPROB` - SNANA Fitprob
- `PROB_SCONE` - Prob of being Ia from SCONE trained on sims generated using core-collapse templates Vincenzi et al 2019
- `PROB_SNIRFV19` - Prob of being Ia from SNIRF trained on sims generated using core-collapse templates from Vincenzi et al 2019
- `PROB_SNNDESCC` - Prob of being Ia from SuperNNova trained on sims generated using core-collapse templates from Jones et al 2017
- `PROB_SNNJ17` - Prob of being Ia from SuperNNova trained on sims generated using core-collapse templates from DES data
- `PROB_SNNV19` - Prob of being Ia from SuperNNova trained on sims generated using core-collapse templates from Vincenzi et al 2019 (Nominal)
- `MU` - SN distance moduli 
- `MUERR_FINAL` - SN distance uncertainties (renormalized for BEAMS prob of being core-collapse, also referred to as MUERR_FINAL)
- `PROBCC_BEAMS` - BEAMS Prob of being core-collapse (see eq. 6 in Vincenzi et al 2024)
- `biasCor_mu` - Bias correction applied to brightness m_b
- `biasCor_mu_COVSCALE` - Reduction in uncertainty due to selection effects (multiplicative)
- `biasCor_mu_COVADD`  - Uncertainty floor as given by the intrinsic scatter model (added in quadrature)

### Global Parameters ###
- $\alpha =  0.16087 \pm 0.00152$
- $\beta = 3.11780 \pm 0.03530$
- $\gamma = 0.03754 \pm 0.00798$
- $M_{0~\mathrm{avg}} = -29.95821$

Note, these global parameters are determined from the likelihood analysis of all the SNe on the Hubble diagram.


### Statistical and Stat+Systematic Covariance matrices
The Statistical and Stat+Systematic Covariance matrices (both 1829x1829 Matrix) are provided in
- `STATONLY.txt.gz`
- `STAT+SYS.txt.gz` (all systematics)

Note that `STATONLY.txt.gz` is actually an 1829x1829 matrix filled with zeros because the statistical uncertainties are included in the `MUERR_FINAL` in the DES-SN5YR_HD.csv file. STAT+SYS.txt.gz contains the additional systematic uncertainties.
See the likelihood function in folder 5_COSMOLOGY to see how the likelihood is built using SN distances (MU in `DES-SN5YR_HD.csv`), statistical SN uncertainties (`MUERR_FINAL` in `DES-SN5YR_HD.csv`) and these covariance matrices.

Single-syst cov matrices are also available in SingleSYS_CovMatrix.
