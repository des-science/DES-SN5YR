"""
The likelihood module for the DES-SN5YR sample
This likelihood analytically marginalize over M (SN absolute brightness).
M is fully degenerate with H0. Do not try to measure H0 with SN data
"""

from cosmosis.gaussian_likelihood import GaussianLikelihood
from cosmosis.datablock import names
import os
import numpy as np
from astropy.table import Table


default_data_file = os.path.join(os.path.split(__file__)[0], "DES-SN5YR_HD.csv")
default_covmat_file = os.path.join(os.path.split(__file__)[0], "STAT+SYS.txt.gz")

def cov_log_likelihood(mu_model, mu, inv_cov):
    """ 
    Computes modified likelihood computation to marginalize offset M 
    from https://arxiv.org/abs/astro-ph/0104009v1, see Equation A9-12 
    """
    delta = np.array([mu_model - mu])
    deltaT = np.transpose(delta)
    chit2 = np.sum(delta @ inv_cov @ deltaT)
    B = np.sum(delta @ inv_cov)
    C = np.sum(inv_cov)
    chi2 = chit2 - (B**2 / C) + np.log(C / (2 * np.pi))
    return -0.5*chi2

class DovekieLikelihood(GaussianLikelihood):
    x_section = names.distances
    x_name = "z"
    y_section = names.distances
    y_name = "D_A"
    like_name = "desy5sn"

    def build_data(self):
        """
        Run once at the start to load in the data vectors.

        Returns x, y where x is the independent variable (redshift in this case)
        and y is the Gaussian-distribured measured variable (magnitude in this case).

        """
        filename = self.options.get_string("data_file", default=default_data_file)
        print("Loading Dovekie SN data from {}".format(filename))
        data = Table.read(filename, format='ascii.csv')
        self.origlen = len(data)

        # The only columns that we actually need here are the redshift,
        # distance modulus and distance modulus error
        self.ww = (data['zHD']>0.00) 

        #use the vpec corrected redshift for zCMB 
        self.zCMB = data['zHD'][self.ww] 
        self.zHEL = data['zHEL'][self.ww]

        # distance modulus and relative stat uncertainties. Note MUERR instead or MUERR_FINAL
        self.mu_obs = data['MU'][self.ww]
        self.mu_obs_err = data['MUERR'][self.ww]

        # Return this to the parent class, which will use it
        # when working out the likelihood
        print(f"Found {len(self.zCMB)} Dovekie 5 supernovae (or bins if you used the binned data file)")
        return self.zCMB, self.mu_obs

    def build_covariance(self):
        """Run once at the start to build the covariance matrix for the data"""
        filename = self.options.get_string("covmat_file", default=default_covmat_file)
        print("Loading Dovekie SN covariance from {}".format(filename))

        # The file format for the covariance has been changed in the new SNANA version in use after DES
        # Covtot_inv is the inverse of stat+sys because it makes no sense to invert covsys
        # This data file is stored with .npz (which will work with np.load)
        # in upper triangular format
        # changes are made to accomodate anticipated much larger files from LSST
        d = np.load(filename)
        n = d[d.files[0]][0]
        inv_cov = np.zeros((n, n))
        inv_cov[np.triu_indices(n)] = d[d.files[1]]

        # Reflect to lower triangular part to make it symmetric
        i_lower = np.tril_indices(n, -1)
        inv_cov[i_lower] = inv_cov.T[i_lower]
	# Unfortunately, to make this work in cosmosis we need to invert the inverse covariance and return that ... sigh ...
        C = np.linalg.inv(inv_cov)

        # Return the covariance; the parent class knows to invert this
        # later to get the precision matrix that we need for the likelihood.
        C = C[self.ww][:, self.ww]

        return C

    def extract_theory_points(self, block):
        """
        Run once per parameter set to extract the mean vector that our
        data points are compared to. 
        """
        import scipy.interpolate

        # Pull out theory DA and z from the block.
        theory_x = block[self.x_section, self.x_name]
        theory_y = block[self.y_section, self.y_name]

        # Interpolation function of theory so we can evaluate at redshifts of the data
        f = scipy.interpolate.interp1d(theory_x, theory_y, kind=self.kind)
        
        zcmb = self.zCMB
        zhel = self.zHEL

        # distance modulus
        theory_ynew = 5.0 * np.log10((1.0 + zcmb) * (1.0 + zhel) * np.atleast_1d(f(zcmb))) + 25.

        # The offset M will be marginalized in the modified log likelihood computation
        return theory_ynew

    def do_likelihood(self, block):
        # get data x by interpolation
        x = np.atleast_1d(self.extract_theory_points(block))
        mu = np.atleast_1d(self.data_y)

        # If covariance is a function of parameters, compute the 
        # new one now.
        if not self.constant_covariance:
            self.cov = np.atleast_2d(self.extract_covariance(block))
            self.inv_cov = np.atleast_2d(self.extract_inverse_covariance(block))

        # modified log-likelihood computation to marginalize offset M
        like = cov_log_likelihood(x, mu, self.inv_cov)
        chi2 = -2.0*like

        # It can be useful to save the chi^2 as well as the likelihood,
        # especially when the covariance is non-constant.
        block[names.data_vector, self.like_name+"_CHI2"] = chi2
        block[names.data_vector, self.like_name+"_N"] = mu.size

        # if the covariance is a function of parameters then we must 
        # account for this in the likelihood.
        if not self.constant_covariance:
            log_det = self.extract_covariance_log_determinant(block)
        else:
            log_det = self.log_det_constant            

        norm = -0.5 * log_det
        like += norm
        block[names.data_vector, self.like_name+"_LOG_DET"] = float(log_det)
        block[names.data_vector, self.like_name+"_NORM"] = float(norm)

        # Numpy has started returning a 0D array in recent versions (1.14).
        # Convert this to a float.
        like = float(like)

        #Now save the resulting likelihood
        block[names.likelihoods, self.like_name+"_LIKE"] = like

        # For some very fast likelihoods the overhead from
        # the steps below is painful.  Setting likelihood_only avoids that.
        if self.likelihood_only:
            return

        #And also the predicted data points - the vector of observables 
        # that in a fisher approch we want the derivatives of.
        #and inverse cov mat which also goes into the fisher matrix.
        block[names.data_vector, self.like_name + "_theory"] = x
        block[names.data_vector, self.like_name + "_data"] = mu
        block[names.data_vector, self.like_name + "_inverse_covariance"] = self.inv_cov

        #We might just be calculating the inverse cov and ignoring the covmat.
        #in that case we do not try to save it
        if self.cov is not None:
            block[names.data_vector, self.like_name + "_covariance"] = self.cov
            #Also save a simulation of the data - the mean with added noise
            #these can be used among other places by the ABC sampler.
            #This also requires the cov mat.
            # If we have a parameter-dependent covariance we need
            # to re-calculate the Cholesky decomposition to simulate some data.
            if not self.constant_covariance:
                self.chol = np.linalg.cholesky(self.cov)
            sim = self.simulate_data_vector(x)
            block[names.data_vector, self.like_name + "_simulation"] = sim


# This takes our class and turns it into 
setup, execute, cleanup = DovekieLikelihood.build_module()
