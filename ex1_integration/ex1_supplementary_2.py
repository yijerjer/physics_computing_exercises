import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate


vquad = np.vectorize(integrate.quad)
c = lambda x : np.cos((np.pi * (x)**2) / 2)
s = lambda x : np.sin((np.pi * (x)**2) / 2)

d = 0.01
wave_lambda = 0.001

for D in [0.03, 0.05, 0.1]:
	x = np.linspace(-10, 10, 500)
	u = x * np.sqrt(2 / (wave_lambda * D))
	delta_u = d * np.sqrt(2 / (wave_lambda * D))
	
	integral_low_limit = -(u + d / 2)
	integral_up_limit = -(u - d / 2)

	c_vals, c_errs = vquad(c, integral_low_limit, integral_up_limit)
	s_vals, s_errs = vquad(s, integral_low_limit, integral_up_limit)

	magnitude = np.square(c_vals) + np.square(s_vals)
	phase = np.arctan(s_vals / c_vals)

	fig, (ax1, ax2) = plt.subplots(1, 2)
	plt.subplots_adjust(wspace=0.4)
	fig.suptitle(rf"Intensity and phase of Fresnel Diffraction for $D = {D}cm$")
	ax1.plot(u, magnitude)
	ax1.set_xlabel(r"$x\sqrt{2/\lambda D}$")
	ax1.set_ylabel("Intensity")

	ax2.plot(u, phase)
	ax2.set_xlabel(r"$x\sqrt{2/\lambda D}$")
	ax2.set_ylabel("Phase")

	fig.savefig(f"ex1_supplmentary_2_{D}.pdf")
	plt.close(fig)




