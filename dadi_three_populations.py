import dadi
import math
import OutOfAfrica

# Loading data
data = dadi.Spectrum.from_file("YRI.CEU.CHB.fs")

# Making an extrapolating model based on OutOfAfrica model from file OutOfAfrica (downloaded from dadi github)
extrap_model = dadi.Numerics.make_extrap_log_func(OutOfAfrica.OutOfAfrica)

# Sample sizes in data
sample_sizes = [20, 20, 20]

# Initial grid for extrapolation
pts_l = [30, 40, 50]

# Bounds for parameters optimization
upper_bound = [
    100,100,100,100,100,100,
    10,10,10,10,
    5,5,5
]
lower_bound = [
    1e-2, 1e-2, 1e-2, 1e-2, 1e-2, 1e-2,
    0, 0, 0, 0,
    0, 0, 0
]

# Initial paramaters values
parameters = [1 for i in range(13)]

# Names of parameters
params_names = ["nuAf", "nuB", "nuEu0", "nuEu", "nuAs0", "nuAs", "mAfB", "mAfEu", "mAfAs", "mEuAs", "TAf", "TB", "TEuAs"]

# Number of local optimizations. The higher - the higher probability of finding a global optimum
iterations = 10
for i in range(iterations):
    # Changing starting points a little bit (we don't want to run series of the same optimizations)
    p0 = dadi.Misc.perturb_params(parameters, fold=1, upper_bound=upper_bound, lower_bound=lower_bound)
    print("Start optimising")

    # Parameters optimization
    optimal_parameters = dadi.Inference.optimize(p0, data, extrap_model, pts_l, upper_bound=upper_bound, lower_bound=lower_bound)
    for j in range(len(optimal_parameters)):
        print("%5s: %5s %20s %20s %5s" % (params_names[j], str(lower_bound[j]), str(p0[j]), str(optimal_parameters[j]), str(upper_bound[j])))

    # Obtaining likelihood with optimal parameters
    model = extrap_model(optimal_parameters, sample_sizes, pts_l)
    model_likelihood = dadi.Inference.ll_multinom(model, data)
    print("likelihood: ", math.exp(model_likelihood), model_likelihood)

    # Writing data into file.
    with open("simulation_results_dadi.txt", "a") as fl:
        for j in range(len(optimal_parameters)):
            fl.write(params_names[j] + ":\t" + str(optimal_parameters[j]) + "\n")
        fl.write("-----\n")

    print(str(i+1) + "/" + str(iterations))



