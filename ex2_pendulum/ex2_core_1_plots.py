import os.path
import numpy as np
import matplotlib.pyplot as plt
from ex2_core_1 import Pendulum

data_filename = "ex2_core_1_data.csv"
all_data = None

if os.path.isfile(data_filename):
    all_data = np.loadtxt(data_filename)
else:
    pendulum = Pendulum()
    solution = pendulum.solve_integral([0.01, 0], 10000)

    all_data = np.array([solution.t, solution.y[0], pendulum.theoretical_theta, solution.y[1], pendulum.energy])
    np.savetxt(data_filename, all_data)

t = all_data[0]
theta = all_data[1]
theoretical_theta = all_data[2]
omega = all_data[3]
energy = all_data[4]

for osc in [10, 100, 1000]:
    plt.plot(t[osc * 100:(osc * 100) + 500], theta[osc * 100:(osc * 100) + 500], label="RK4 method")
    plt.plot(t[osc * 100:(osc * 100) + 500], theoretical_theta[osc * 100:(osc * 100) + 500], label="Theoretical value")
    plt.xlabel(r"time $t$ / $s$")
    plt.ylabel(r"angular displacement $\theta$ / $rad s^{-1}$")
    plt.title(f"Plot of displacement against time for both RK4 method \n and theoreotical value after {osc} oscillations")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"ex2_core_1_theta_{osc}.pdf")
    plt.close()


plt.plot(t, energy)
plt.xlabel("time t / s")
plt.ylabel("Energy E / J")
plt.title("Plot of energy against time with the RK4 method")
plt.tight_layout()
plt.savefig("ex2_core_1_energy.pdf")


