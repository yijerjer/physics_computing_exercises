from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt


def integrate_with_limits(function, low_lim, up_lim):
	u = np.linspace(low_lim, up_lim, 1000)
	vquad = np.vectorize(integrate.quad)
	return vquad(function, 0, u)

def get_spiral_vals(low_lim, up_lim):
	c = lambda x : np.cos((np.pi * x**2) / 2)
	s = lambda x : np.sin((np.pi * x**2) / 2)
	c_vals = integrate_with_limits(c, low_lim, up_lim)[0]
	s_vals = integrate_with_limits(s, low_lim, up_lim)[0]
	return (c_vals, s_vals)

def plot_spiral(low_lim, up_lim):
	c_vals, s_vals = get_spiral_vals(low_lim, up_lim)
	
	plt.plot(c_vals, s_vals, linewidth=0.7)
	plt.xlabel("C(u)")
	plt.ylabel("S(u)")
	plt.title("Cornu Spiral")
	plt.savefig("ex1_core_2.pdf")

plot_spiral(-10, 10)