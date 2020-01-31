import numpy as np
import matplotlib.pyplot as plt
from ex2_core_1 import Pendulum


plt.plot()

for damping in [1, 5, 10]:
    pendulum = Pendulum(q=damping)
    solution = pendulum.solve_integral([0.1, 0], 5)

    plt.plot(solution.t, solution.y[0], label=f"damping q = {damping}")

plt.xlabel(r"time $t$ / $s$")
plt.ylabel(r"angular displacement $\theta$ / $rad s^{-1}$")
plt.title("Plot of angular displacement against time with different \n damping coefficients")
plt.legend()
plt.tight_layout()
plt.savefig(f"ex2_core_2_damping.pdf")
plt.close()