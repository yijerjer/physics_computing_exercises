import numpy as np
import matplotlib.pyplot as plt
from ex2_core_1 import Pendulum

def get_period(t, theta, oscill_num):
    sign_switch_count = 0
    sign_tracking = 1
    start_t = 0
    end_t = 0

    for ind, val in enumerate(theta):
        if sign_switch_count >= (oscill_num * 2):
            end_t = t[ind]
            break

        current_sign = 1 if val > 0 else -1
        if current_sign != sign_tracking:
            if sign_switch_count == 0:
                start_t = t[ind]
            sign_switch_count += 1
            sign_tracking = current_sign
    
    return (end_t - start_t) / (oscill_num)


amplitude = np.linspace(0.01, np.pi, 20)
period = []
for a in amplitude:
    pendulum = Pendulum()
    solution = pendulum.solve_integral([a, 0], 100)
    period.append(get_period(solution.t, solution.y[0], 10))

plt.plot(amplitude, period)
plt.xlabel(r"amplitude $A$")
plt.ylabel(r"period $T / t$")
plt.title("Plot of period against amplitude using RK4 method for integration")
plt.savefig("ex2_core_1_amplitude.pdf")

pendulum = Pendulum()
solution = pendulum.solve_integral([np.pi / 2, 0], 100)
print(get_period(solution.t, solution.y[0], 10))
