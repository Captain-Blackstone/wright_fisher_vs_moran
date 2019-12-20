# # The optimized parameters inferred by model below 'nu1F': 1.89895375, 'nu2B': 0.03951815, 'nu2F': 9.48464048,
# 'm': 0, 'Tp': 0.40006345, 'T': 0.07088507]
# 'Optimized log-likelihood:' -1146.05261631283430

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

func = demographic_models.prior_onegrow_mig
# ll for this model: -1066.66
params = array([11.27297817, 36.10289795, 12.3547213, 0, 2.30969484, 1.63538355])
params = array([50, 50, 50, 0, 2.30969484, 1.63538355])
# The upper_bound array is for use in optimization. Occasionally the optimizer
# will try wacky parameter values. We in particular want to exclude values with
# very long times, as they will take a long time to evaluate.
upper_bound = [100, 100, 100, 100, 3, 3]
lower_bound = [1e-2, 1e-2, 1e-2, 0, 0, 0]

params = array([1.89895375, 0.03951815, 9.48464048, 0, 0.40006345, 0.07088507])
# Makde the extrapolating version of our demographic model function.
func_ex = dadi.Numerics.make_extrap_log_func(func)
# Calculate the model AFS.
model = func_ex(params, ns, pts_l)
# Likelihood of the data given the model AFS.
ll_model = dadi.Inference.ll_multinom(model, data)
print 'Model log-likelihood:', ll_model
# The optimal value of theta given the model.
theta = dadi.Inference.optimal_sfs_scaling(model, data)
theta

iter = 10
ll_opt_v = []
for i in range(iter):
    print(i)
    p0 = dadi.Misc.perturb_params(params, fold=1, upper_bound=upper_bound)
    fixed_params = array([None, None, None, 0, None, None])
    popt = dadi.Inference.optimize_log(p0, data, func_ex, pts_l,
                                   lower_bound=lower_bound,
                                   upper_bound=upper_bound,
                                   fixed_params=fixed_params,
                                   verbose=len(params))
    print 'Optimized parameters', repr(popt)
    model = func_ex(popt, ns, pts_l)
    ll_opt = dadi.Inference.ll_multinom(model, data)
    print 'Optimized log-likelihood:', ll_opt
    ll_opt_v.append(ll_opt)
    with open("rez.txt", "a") as rez:
        # rez.write(i + "\t" + ll_opt + "\t" + popt + "\n")
        rez.write('%s, ll %s, param %s' % (i, ll_opt, str(popt)))
        rez.write("\n")
with open("rez.txt", "a") as rez:
    llmax = max(ll_opt_v)
    rez.write('llmax %s' % (llmax))


