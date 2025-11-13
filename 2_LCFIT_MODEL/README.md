## SALT3 models
This folder includes the differen SED time-series models used to fit the DES light-curves.

#### SALT3.DOVEKIE:
This is the SALT3 model used for the **Nominal** DES-Dovekie cosmological analysis.

This model has been trained on the same SN sample presented by Kenworthy et al 2021 (https://arxiv.org/abs/2104.07795) with two major differences:
- data have been recalibrated using the work by Dovekie (https://arxiv.org/abs/2506.05471)

#### SALT3.DOVEKIE-SYS:
These are the 10 SALT3 models (SALT3.MODEL000 to SALT3.MODEL009) used to incorporate Calibration and LC fitting Systematics in the DES-Dovekie cosmological analysis.
Each model is re-trained applying calibration uncertainties shifts to each filter's zero-point and effective mean wavelength.
The calibration shifts are randoly drawn from the calibration uncertainty covariance matrix presented by Dovekie `https://github.com/bap37/Dovekie/`)
The calibration shifts applied to build each of the SALT3 models presented here are in their respective SALT3.INFO files.


