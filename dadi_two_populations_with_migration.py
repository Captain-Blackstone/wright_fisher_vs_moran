# # The optimized parameters inferred by model below 'nu1F': 1.881, 'nu2B': 0.0710, 'nu2F': 1.845,
# 'm': 0.911, 'Tp': 0.355, 'T': 0.111]
# 'Optimized log-likelihood:' -1066.66


# Numpy is the numerical library dadi is built upon
import numpy
from numpy import array

import dadi

# In demographic_models.py, we've defined a custom model for this problem
import demographic_models

# Load the data
data = dadi.Spectrum.from_file('YRI_CEU.fs')
ns = data.sample_sizes

# These are the grid point settings will use for extrapolation.
pts_l = [40,50,60]

# The Demographics1D and Demographics2D modules contain a few simple models,
# mostly as examples. We could use one of those.
func = dadi.Demographics2D.split_mig
# ll for this model: -1136.61
params = array([1.792, 0.426, 0.309, 1.551])
upper_bound = [100, 100, 3, 20]

# Instead, we'll work with our custom model
func = demographic_models.prior_onegrow_mig
# ll for this model: -1066.66
params = array([1.881, 0.0710, 1.845, 0.911, 0.355, 0.111])
# The upper_bound array is for use in optimization. Occasionally the optimizer
# will try wacky parameter values. We in particular want to exclude values with
# very long times, as they will take a long time to evaluate.
upper_bound = [100, 100, 100, 100, 3, 3]
lower_bound = [1e-2, 1e-2, 1e-2, 0, 0, 0]

# Makde the extrapolating version of our demographic model function.
func_ex = dadi.Numerics.make_extrap_log_func(func)
# Calculate the model AFS.
model = func_ex(params, ns, pts_l)
# Likelihood of the data given the model AFS.
ll_model = dadi.Inference.ll_multinom(model, data)
print 'Model log-likelihood:', ll_model
# The optimal value of theta given the model.
theta = dadi.Inference.optimal_sfs_scaling(model, data)

# Perturb our parameter array before optimization. This does so by taking each
# parameter a up to a factor of two up or down.
p0 = dadi.Misc.perturb_params(params, fold=1, upper_bound=upper_bound)
# Do the optimization. By default we assume that theta is a free parameter,
# since it's trivial to find given the other parameters. If you want to fix
# theta, add a multinom=False to the call.
# (This is commented out by default, since it takes several minutes.)
# The maxiter argument restricts how long the optimizer will run. For production
# runs, you may want to set this value higher, to encourage better convergence.
popt = dadi.Inference.optimize_log(p0, data, func_ex, pts_l, 
                                   lower_bound=lower_bound,
                                   upper_bound=upper_bound,
                                   verbose=len(params))
print 'Optimized parameters', repr(popt)
model = func_ex(popt, ns, pts_l)
ll_opt = dadi.Inference.ll_multinom(model, data)
print 'Optimized log-likelihood:', ll_opt

# Plot a comparison of the resulting fs with the data.
import pylab
pylab.figure()
dadi.Plotting.plot_2d_comp_multinom(model, data, vmin=1, resid_range=3,
                                    pop_ids =('YRI','CEU'))
# This ensures that the figure pops up. It may be unecessary if you are using
# ipython.
pylab.show()
pylab.savefig('YRI_CEU.png', dpi=50)