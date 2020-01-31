from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

class Pendulum:
    def __init__(self, g=1, l=1, m=1, q=0, F=0, sigma=2/3):
        self.g = g; self.l = l; self.m = m
        self.q = q; self.F = F
        self.sigma = 2/3

    def derivative(self, t, y):
        y0_derivative = y[1]
        y1_derivative = -(self.g/self.l) * np.sin(y[0]) - self.q * y[1] + self.F * np.sin(self.sigma * t)
        return (y0_derivative, y1_derivative)
        
    def solve_integral(self, initial_y, oscill_num, t_space_size=None):
        t_max = oscill_num * 2 * np.pi
        if not t_space_size:
            t_space_size = oscill_num * 10**2
        self.t_space = np.linspace(0, t_max, t_space_size)
        self.solution = solve_ivp(self.derivative, [0, t_max], initial_y, t_eval=self.t_space)
        self.set_energy()
        self.theoretical_integral(initial_y[0])

        # printing 50 rows of t, theta, omega and energy 
        interval_size = t_space_size / 50
        for i in range(50):
            index = int(i * interval_size)
            print(f"t = {'{:10.5f}'.format(self.solution.t[index])}, theta = {'{:10.5f}'.format(self.solution.y[0][index])}, omega = {'{:10.5f}'.format(self.solution.y[1][index])}, energy = {'{:10.6f}'.format(self.energy[index])}")

        return self.solution

    def theoretical_integral(self, amplitude):
        self.theoretical_theta = amplitude * np.cos(np.sqrt(self.g/self.l) * self.t_space)

    def set_energy(self):
        # The energy is given by (1/2)* inertia * omega^2 + (1/2) * g * l * theta^2
        theta = self.solution.y[0]
        omega = self.solution.y[1]

        self.energy = (1/2) * self.m * self.l**2 * omega**2 + (1/2) * self.g * self.l * theta**2
    