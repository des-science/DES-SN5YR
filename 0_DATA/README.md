## Data Format

### The full set of DES light-curves will be release after acceptance of Sanchez et al. 2024, currently in Collaboration Wide Review

Data and simulations are in SNANA FITs Format (see also Sec. 4.36.1 FITS Format in SNANA manual on Github)
You will find two sets of files `XXX.HEAD.FITS` files and `XXX.PHOT.FITS`.
The HEAD files are tables and each row contains summary info for each SN. The summary info includes the SNID, sky coordinates, redshift, Galactic extinction, host-galaxy information, and many other quantities. Each HEAD file also contains the name of the second “PHOT” file which contains the photometric light curves. All of the light curves are written sequentially to the PHOT-tables, and pointers in the HEAD file (see PTROBS_MIN and PTROBS_MAX) are used to select the appropriate rows from the PHOT table. To help catch pointer mistakes, MJD = -777 is written after each light curve to clearly indicate the end of the light curve.


### HEAD file:
Variable name                : Description
* `SNID`                       : integer or character ID
* `FAKE`                       : 0=real data, 1=fake overlaid on image, 2=SNANA sim,
* `RA`,DEC                     : sky coordinates (degrees)
* `SNTYPE`                     : integer type assigned by survey (e.g., SPEC type)
* `NOBS`                       : number of obs (all bands)
* `PTROBS_MIN`                 : pointer to 1st light curve obs in PHOT file
* `PTROBS_MAX`                 : pointer to last light curve obs
* `MWEBV[_ERR]`                : E(B-V) for Milky way
* `REDSHIFT_HELIO[_ERR]`       : best heliocentric redshift; zSpec if available; else zPhot; else -9
* `REDSHIFT_FINAL[_ERR]`       : best CMB redshift (no VPEC correction)
* `VPEC_[ERR]`                 : pec velocity (km/sec) and error on correction
* `PEAKMJD`                    : approx PEAKMJD; useful to init light curve fit
* `MJD_TRIGGER`                : MJD when survey trigger is satisfied
* `MJD_DETECT_FIRST`           : MJD of first detection
* `MJD_DETECT_LAST`            : MJD of last detection
* `HOSTGAL_SB_FLUXCAL_[band]`  : Surface brightness mag at SN location
* `HOSTGAL_NMATCH`             : number of host matches with DDLR < 4
* `HOSTGAL_NMATCH2`            : number of host matches with DDLR < 7
* `HOSTGAL_OBJID`              : integer id of host (long long int)
* `HOSTGAL_RA`                 : R.A. (deg) for center of host
* `HOSTGAL_DEC`                : declination (deg) for center of host
* `HOSTGAL_SNSEP`              : transient-host separation, arcsec
* `HOSTGAL_DDLR`               : SN-host sep in distance-light-radii (d_DLR)
* `HOSTGAL_SPECZ[_ERR]`        : zSpec of host (-9 -> not available)
* `HOSTGAL_PHOTOZ[_ERR]`       : zphot (mean of PDF); -9 -> not available
* `HOSTGAL_ZPHOT_Q[PPP]`       : redshift containing PPP percent of zPDF prob
* `HOSTGAL_LOGMASS[_ERR]`      : logmass and error
* `HOSTGAL_LOGSFR[_ERR]`       : log(star formation rate) and error
* `HOSTGAL_MAG_[band]`         : host mags for band=u,g,r,i,z,Y
* `HOSTGAL_MAGERR_[band]`      : uncertainty on above mags [Each hostgal_xxx has hostgal2_xxx for 2nd host-match;
                                 -999 indicates no 2nd host; else values are filled.
                                 First listed host has smallest DDLR and may not be the true host]

Additional variables for simulated data:
* `SIM_TYPE_INDEX`             true integer transient type (e.g., 1 for SNIa)
* `SIM_[SSS]`                  true sim property SSS


### PHOT file:
* `MJD`           :modified Julian date (-777 -> end of light curve)
* `BAND`          :e.g.,  ’u’, ’g’, ’r’ etc ...
* `CCDNUM`        :CCD or detector number
* `IMGNUM`        :image number; e.g. exposure number, visit id ...
* `FIELD`         :name of field; e.g., SHALLOW, DEEP, etc ...
* `PHOTFLAG`      :bit-mask of information (check data README)
* `PHOTPROB`      :float metric; e.g, RealBogus score, chi2, ...
* `FLUXCAL`       :calibrated flux : mag = 27.5 - 2.5*log10(FLUXCAL)
* `FLUXCALERR`    :Poisson uncertainty on FLUXCAL; sky+galaxy+source image properties
* `PSF_SIG1`      :PSF Gauss sigma, pixels
* `SKY_SIG`       :sky noise (ADU/pixel)
* `SKY_SIG_T`     :template sky noise (for DIFFIMG, not for SMP)
* `ZEROPT`        :image zero point
* `GAIN`          :N_photoelectron/ADU
* `XPIX`          :x-locaton on CCD (pixels)
* `YPIX`          :y-locaton on CCD (pixels)

Additional variables for simulated data:
* `SIM_MAGOBS`    :true model mag
  



