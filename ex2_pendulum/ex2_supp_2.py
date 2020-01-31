import matplotlib.pyplot as plt
from ex2_core_1 import Pendulum

q_F_tups = [(0, 0), (0.5, 0), (0.5, 1.2), (0.5, 1.45), (1.5, 0), (1.5, 1.2), (1.5, 1.45)]

fig, axes = plt.subplots(len(q_F_tups), 1)
fig.set_figheight(30)
fig.suptitle("Plot of angular displacement against angular velocity", y=0.99)
fig.tight_layout(pad=6)

for ind, tup in enumerate(q_F_tups):
    pendulum = Pendulum(q=tup[0], F=tup[1])
    sol = pendulum.solve_integral([0.01, 0], 20)

    axes[ind].plot(sol.y[0], sol.y[1])
    axes[ind].set_xlabel((r"angular displacement $\theta$ / $rad s^{-1}$"))
    axes[ind].set_ylabel(r"angular velocity $\omega$ / $rad s^{-1}$")
    axes[ind].set_title(f"q = {tup[0]}, F = {tup[1]}")

fig.savefig("ex2_supp_2.pdf")
