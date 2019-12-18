import momi
from scipy.optimize import differential_evolution

data = momi.sfs_from_dadi("YRI.CEU.CHB.fs")
model = momi.DemographicModel(N_e=1e5, muts_per_gen=2.35e-8)
model.set_data(data, length=4.04*(10**6))

model.add_size_param("nuA")
model.add_size_param("nuEu")
model.add_size_param("nuAf")
model.add_size_param("nuAs")
model.add_size_param("nuB")

model.add_growth_param('gAs')
model.add_growth_param('gEu')


model.add_time_param("TEuAs")
model.add_time_param("TB")
model.add_time_param("TAf")


model.add_leaf("CEU", N="nuEu")
model.add_leaf("YRI", N="nuAf")
model.add_leaf("CHB", N="nuAs")

# set growth rates
model.set_size("CEU", N="nuEu", t=0, g='gEu') #lambda params: np.log(params.nuEu/params.nuEu0)/params.TEuAs)
model.set_size("CHB", N="nuAs", t=0, g='gAs') #lambda params: np.log(params.nuAs/params.nuAs0)/params.TEuAs)

# Eu and As coalescence
model.move_lineages("CHB", "CEU", t="TEuAs", N="nuB")

# Eu (Eu+As) and Af coalescence
model.move_lineages("CEU", "YRI", N="nuAf", t=lambda params: params.TEuAs + params.TB)
model.set_size("YRI", N="nuA", t=lambda params: params.TEuAs + params.TB + params.TAf)


#model.set_params({'nuA': 7300, 'nuAf': 13000, 'TAf': 80000, 'nuB':2000, 'TB': 100000, 'nuAs0': 500, 'nuEu0': 1500, 'nuAs': 50000, 'nuEu': 30000, 'TEuAs': 40000})
# nAs = 50000
# nAs0 = 500
# nEu = 30000
# nEu0 = 1500
# T = 40000
# model.set_params({'nuA': 7300, 'nuAf': 13000, 'TAf': 80000, 'nuB':2000, 'TB': 100000, 'gAs': np.log(nAs/nAs0) / T, 'gEu':  np.log(nEu/nEu0) / T, 'nuAs': 50000, 'nuEu': 30000, 'TEuAs': 40000})
# print(model.get_params())
# print(model.log_likelihood())
from matplotlib import pyplot as plt
# yticks = [1e4, 2.5e4, 5e4, 7.5e4, 1e5, 2e5, 300000]
# fig = momi.DemographyPlot(
#     model, ["YRI", "CEU", "CHB"],
#     figsize=(6,8),
#     major_yticks=yticks)
    # linthreshy=1e5, pulse_color_bounds=(0,.25))
# plt.show()


"""
And this is a global optimization
"""

def func(params):
    nuA, nuEu, nuAf, nuAs, nuB, gEu, gAs, TEuAs, TB, TAf = params
    model.set_params({"nuEu": nuEu,
                      "nuA" : nuA,
                      "gEu": gEu,
                      "nuAf": nuAf,
                      "gAs": gAs,
                      "nuAs": nuAs,
                      "nuB": nuB,
                      "TEuAs": TEuAs,
                      "TB": TB,
                      "TAf": TAf})
    try:
        return - model.log_likelihood()
    except:
        print("FAILED")
        return 200000

def global_optimizer():
    pop_size_bounds = [1, 10e6]
    growth_speed_bounds = [-1e-3, 1e-3]
    time_bounds = [1, 0.7e5]
    bounds = [pop_size_bounds,
              pop_size_bounds,
              pop_size_bounds,
              pop_size_bounds,
              pop_size_bounds,
              growth_speed_bounds,
              growth_speed_bounds,
              time_bounds,
              time_bounds,
              time_bounds]
    results = []
    for i in range(10):
        result = differential_evolution(func, bounds)
        results.append(result)
        with open("optimized_parameters.txt", "a") as fl:
            fl.write(str(i) + "\n")
            fl.write(str(results[-1].x) + " , " + str(results[-1].fun) + "\n")
            fl.write("---------" + "\n")
    results.sort(key=lambda el: el.fun)
    print(results[0].x, results[0].fun)
    print(results[-1].x, results[-1].fun)


def local_optimizer():
    with open("optimized_parameters.txt") as fl:
        lines = fl.readlines()
    likelihoods = []
    for line in lines:
        if "]" in line:
            likelihoods.append(float(line.split()[-1]))
    maximum = max(likelihoods)
    for line in lines:
        if str(maximum) in line:
            end_index = lines.index(line)
            str_params = [line.strip().replace("[", "").replace("]", "") for line in lines[end_index-2:end_index+1]]
            params = []
            for line in str_params:
                line = line.split()
                for element in line:
                    params.append(float(element))
    params = params[:-1]
    model.set_params({'nuA': params[0],
                      'nuEu': params[1],
                      'nuAf': params[2],
                      'nuAs': params[3],
                      'nuB': params[4],
                      'gEu': params[5],
                      'gAs': params[6],
                      'TEuAs': params[7],
                      'TB' : params[8],
                      'TAf': params[9]})
    print("starting optimization")
    results = []
    for i in range(1):
        print(i)
        optimized = model.optimize()
        results.append(optimized)
    best = sorted(results, key=lambda r: r.log_likelihood)[-1]
    for key in best.parameters.keys():
        print(key, best.parameters[key])
    print(best.log_likelihood)

local_optimizer()