import dadi
import math

import OutOfAfrica

data = dadi.Spectrum.from_file("YRI.CEU.CHB.fs")
extrap_model = dadi.Numerics.make_extrap_log_func(OutOfAfrica.OutOfAfrica)
sample_sizes = [20, 20, 20]
pts_l = [30, 40, 50]
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
parameters = [1, 50, 50, 50, 50, 50,
              5,5,5,5,
              2.5,2.5,2.5]
parameters = [1 for i in range(13)]
params_names = ["nuAf", "nuB", "nuEu0", "nuEu", "nuAs0", "nuAs", "mAfB", "mAfEu", "mAfAs", "mEuAs", "TAf", "TB", "TEuAs"]
iterations = 10
for i in range(iterations):
    p0 = dadi.Misc.perturb_params(parameters, fold=1, upper_bound=upper_bound, lower_bound=lower_bound)
    print("Start optimising")
    optimal_parameters = dadi.Inference.optimize(p0, data, extrap_model, pts_l, upper_bound=upper_bound, lower_bound=lower_bound)
    for j in range(len(optimal_parameters)):
        print("%5s: %5s %20s %20s %5s" % (params_names[j], str(lower_bound[j]), str(p0[j]), str(optimal_parameters[j]), str(upper_bound[j])))
    model = extrap_model(optimal_parameters, sample_sizes, pts_l)
    model_likelihood = dadi.Inference.ll_multinom(model, data)
    print("likelihood: ", math.exp(model_likelihood), model_likelihood)
    with open("simulation_results.txt", "a") as fl:
        for j in range(len(optimal_parameters)):
            fl.write(params_names[j] + ":\t" + str(optimal_parameters[j]) + "\n")
        fl.write("-----\n")
    print(str(i+1) + "/" + str(iterations))



