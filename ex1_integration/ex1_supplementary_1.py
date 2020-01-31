import os.path
import numpy as np
import matplotlib.pyplot as plt


def error_plot_compare(repeats=25, new_data=False):
    filename = "ex1_core_1.csv"
    N_vals = np.power(np.full(7, 10), np.arange(1,8))
    errors_mat = None

    if os.path.isfile(filename) and not new_data:
        errors_mat = np.loadtxt(filename)
        mc_means = np.mean(errors_mat, axis=1)

        theoretical_error = 10**6 * np.power(np.pi / 8, 8) * np.sqrt(0.5 / N_vals)

        print(theoretical_error)
        plt.scatter(N_vals, mc_means, label="Error from MC Integration")
        plt.scatter(N_vals, theoretical_error, label="Theoretical Error")
        plt.loglog()
        plt.legend()
        plt.xlabel("N")
        plt.ylabel("Error in Integral")
        plt.title("Plot of theoretical and MC error against the number of samples N")
        plt.show()
        plt.savefig("ex1_supplmentary_1.pdf")
    else:
        print("Run ex1_core_1.py first to get csv file.")
        

error_plot_compare()