import matplotlib.pyplot as plt
from ex2_core_1 import Pendulum


pendulum_1 = Pendulum(F=1.2)
sol_1 = pendulum_1.solve_integral([0.2, 0], 1000)

pendulum_2 = Pendulum(F=1.2)
sol_2 = pendulum_2.solve_integral([0.20001, 0], 1000)

plt.plot(sol_1.t, sol_1.y[0], label=r"$\theta_{o}$ = 0.2")
plt.plot(sol_2.t, sol_2.y[0], label=r"$\theta_{o}$ = 0.20001")
plt.ylabel(r"angular displacement $\theta$ / $rad s^{-1}$")
plt.xlabel(r"time $t$ / $s$")
plt.title("Plot of angular displacement against time for \n two very similar values of initial displacement")
plt.legend()
plt.tight_layout()

plt.savefig("ex2_supp_1.pdf")