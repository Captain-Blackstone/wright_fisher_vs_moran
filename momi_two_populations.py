# The optimized parameters inferred by model below 'N_A': 7112.960327549957, 'nu_1F': 1.8953321345501677,
# 'g_2': 0.00022571614926807427, 'nu_2F': 10.68845341370844, 'tp': 0.3867203375853, 't': 0.06987273292805748
# 'Optimized log-likelihood:' -63731.995051340724

import momi
from matplotlib import pyplot as plt
import numpy as np
def model():
	# nu1F, nu2B, nu2F, !m!, Tp, T 
	model = momi.DemographicModel(N_e=1, gen_time=25,
                              muts_per_gen=2.35e-8)
	model.add_size_param('N_A')
	model.add_size_param("nu_1F", lower=1e-2, upper=100)
#	model.add_size_param("nu_2B", lower=1e-2, upper=100)
	model.add_growth_param('g_2')
	model.add_size_param("nu_2F", lower=1e-2, upper=100)
	model.add_time_param("tp", lower=0, upper=5)
	model.add_time_param("t", lower=0, upper=5)
	
	model.add_leaf("CEU", N=lambda x: x.nu_2F * x.N_A, g='g_2')
	model.add_leaf("YRI", N=lambda x: x.nu_1F * x.N_A)
	model.move_lineages("CEU", "YRI", t=lambda x: x.t * 50 * x.N_A, N=lambda x: x.nu_1F * x.N_A)
	model.set_size("YRI", N='N_A', g=0, t=lambda x: (x.t + x.tp) * 50 * x.N_A)
	
	#model.set_params(randomize=True)
	# [1.880, 0.0724, 1.764, !0.930!, 0.363, 0.112]	
	model.set_params({'N_A': 7300, 'nu_1F': 1.880, 'g_2' : np.log(1.764/0.0724) / (0.112 * 50 * 7300), 'nu_2F': 1.764, 'tp': 0.363, 't': 0.112})
	return model

dem_model = model()

data = momi.sfs_from_dadi("YRI_CEU.fs")

dem_model.set_data(data)

print(dem_model.get_params())

print(dem_model.log_likelihood())

#dem_model.optimize(method="TNC")

#print(dem_model.get_params())

#print(dem_model.log_likelihood())


#def func(params):
#	try:
#		N_A, nu1F, g2, nu2F, tp, t = params
#		nu1F = np.exp(nu1F)
#		nu2F = np.exp(nu2F)
#		tp = np.exp(tp)
#		t = np.exp(t)
#		dem_model.set_params({'N_A': N_A, 'nu_1F': nu1F, 'g_2' : g2, 'nu_2F': nu2F, 'tp': tp, 't': t})
#		print(N_A, nu1F, g2, nu2F, tp, t )
#		print ( dem_model.log_likelihood(), dem_model.get_params())
#		return - dem_model.log_likelihood()
#	except:
#		print("FAILED")
#		return 200000
#
#bounds = [[100, 10e4], [np.log(1e-2), np.log(100)], [-1e-3, 1e-3],[np.log(1e-2), np.log(100)], [np.log(1e-15), np.log(5)],  [np.log(1e-15), np.log(5)]]
#
#from scipy.optimize import differential_evolution

#result = differential_evolution(func, bounds)
#print(result.x, result.fun)
#
#yticks = [1e4, 2.5e4, 5e4, 7.5e4, 1e5, 2e5]
#fig = momi.DemographyPlot(
#    dem_model, ["YRI", "CEU"],
#    figsize=(6,8),
#    major_yticks=yticks)
##    linthreshy=1e5, pulse_color_bounds=(0,.25))
#plt.show()
