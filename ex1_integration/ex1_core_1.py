import numpy as np
import os.path
import matplotlib.pyplot as plt

def mc_integration(N, function, limit, dimensions):
	V = np.power(limit, dimensions)
	rand_points = np.random.rand(N, dimensions) * limit
	function_with_val = function(np.sum(rand_points, axis=1))
	mean_f = (1/N) * np.sum(function_with_val)
	mean_f_squared = (1/N) * np.sum(np.square(function_with_val))
	
	sigma = V * np.sqrt((mean_f_squared - np.square(mean_f)) / N)
	integral = V * mean_f

	return (np.power(10, 6) * np.array([integral, sigma]))

def mc_integration_error(N, function, limit, dimensions):
	val_and_error = mc_integration(N, function, limit, dimensions)
	return val_and_error[1]

def error_plot(repeats=25, new_data=False):
	filename = "ex1_core_1.csv"
	N_vals = np.power(np.full(7, 10), np.arange(1,8))
	errors_mat = None

	if os.path.isfile(filename) and not new_data:
		errors_mat = np.loadtxt(filename)
	else:
		N_vals_repeated = np.matrix.transpose(np.full([repeats, len(N_vals)], N_vals))
		vmc_integration = np.vectorize(mc_integration_error)
		errors_mat = vmc_integration(N_vals_repeated, np.sin, np.pi/8, 8)

		np.savetxt(filename, errors_mat)

	means = np.mean(errors_mat, axis=1)
	stds = np.std(errors_mat, axis=1)

	plt.errorbar(N_vals, means, yerr=stds)
	plt.loglog()
	plt.xlabel("N")
	plt.ylabel("Error in Integral")
	plt.title("Plot of error in integral against the number of Monte Carlo samples N")
	plt.show()
	plt.savefig("ex1_core_1.pdf")





error_plot()
print(mc_integration(10**7, np.sin, np.pi/8, 8))