### Hubble diagrams
We provide the Hubble diagram including only the essential information for cosmology (`DES-Dovekie_HD.csv`).

Using the metadata, SN distances are calculated as:

`MU` $`=`$ -2.5log$`_{10}`$(x0) $`~+~\alpha`$x1 $`~-~\beta`$c$`~\pm~\gamma/2~-~`$biasCor_mu$`~-~M_{0~\mathrm{avg}}`$

**DES-SN5YR_HD.csv**

- `CID` - Candidate ID
- `IDSURVEY` - {10:'DES', 61:'CFA1', 62:'CFA2', 63:'CFA3S', 64:'CFA3K' ,65:'CFA4p2', 66:'CFA4p3', 150:'FOUND'}
- `zHD` - Hubble Diagram Redshift (with CMB and VPEC corrections)
- `zHEL` - Heliocentric Redshift
- `MU` - SN distances (assuming H0 of 70)
- `MUERR` - SN distance uncertainties (renormalized for BEAMS prob of being core-collapse)


### Global Parameters ###
- $\alpha =  0.169 \pm 0.0003$
- $\beta = 3.14 \pm 0.04$
- $\gamma = 0.033 \pm 0.008$
- $M_{0~\mathrm{avg}} = -29.96210$

Note, these global parameters are determined from the likelihood analysis of all the SNe on the Hubble diagram.


### Statistical and Stat+Systematic Covariance matrices
The Statistical and Stat+Systematic Covariance matrices (both 1820x1820 Matrix) are provided in
- `STATONLY.npz`
- `STAT+SYS.npz` (all systematics)


Single-syst cov matrices are also available in SingleSYS_CovMatrix.
