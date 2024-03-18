## SALT3 models
This folder includes the differen SED time-series models used to fit the DES light-curves.

#### SALT3.DES5YR:
This is the SALT3 model used for the **Nominal** DES-SN5YR cosmological analysis.

This model has been trained on the same SN sample presented by Kenworthy et al 2021 (https://arxiv.org/abs/2104.07795) with two major differences:
- data have been recalibrated using the work by Supercal-Fragilistic (https://arxiv.org/abs/2112.03864),
- we exclude CFA-U band data.

#### SALT3.DES5YR-SYS:
These are the 10 SALT3 models (SALT3.MODEL000 to SALT3.MODEL009) used to incorporate Calibration and LC fitting Systematics in the DES-SN5YR cosmological analysis.
Each model is re-trained applying calibration uncertainties shifts to each filter's zero-point and effective mean wavelength.
The calibration shifts are randoly drwan from the calibration uncertainty covariance matrix presented by Brout et al., 2021 (https://arxiv.org/abs/2112.03864, Matrix availabel at `https://github.com/PantheonPlusSH0ES/DataRelease/blob/main/Pantheon%2B_Data/2_CALIBRATION/FRAGILISTIC_COVARIANCE.npz`)
The calibration shifts applied to build each of the SALT3 models presented here are in `./SALT3.DES5YR-SYS/calib_shiftlists`


