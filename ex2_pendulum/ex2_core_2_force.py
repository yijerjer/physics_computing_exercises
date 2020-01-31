import numpy as np
import matplotlib.pyplot as plt
from ex2_core_1 import Pendulum


for force in [0.5, 1.2, 1.44, 1.465]:
    pendulum = Pendulum(q=0.5, F=force)
    solution = pendulum.solve_integral([0.1, 0], 10)

    plt.figure(1)
    plt.plot(solution.t, solution.y[1], label=f"force F = {force}", linewidth=0.6)
    plt.figure(2)
    plt.plot(solution.t, solution.y[0], label=f"force F = {force}", linewidth=0.6)

plt.figure(1)
plt.xlabel(r"time $t$ / $s$")
plt.ylabel(r"angular velocity $\omega$ / $rad s^{-1}$")
plt.title("Plot of angular velocity against time with different \n force coefficients")
plt.legend()
plt.tight_layout()
plt.savefig("ex2_core_2_force_velocity.pdf")

plt.figure(2)
plt.xlabel(r"time $t$ / $s$")
plt.ylabel(r"angular displacement $\theta$ / $rad s^{-1}$")
plt.title("Plot of angular displacement against time with different \n force coefficients")
plt.legend()
plt.tight_layout()
plt.savefig("ex2_core_2_force_displacement.pdf")

plt.close()