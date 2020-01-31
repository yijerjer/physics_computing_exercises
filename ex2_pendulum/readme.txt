Core Task 1
- ex2_core_1.py contains a class Pendulum that contains the integral, theoretical function and energy of the system mentioned in the booklet.
- ex2_core_1_plots.py prints out 3 plots of the integral with RK4 method compared with the theoretical function after 10, 100, 1000 oscillations.
- ex2_core_1_plots.py also plots the evolution of the energy against time.
- the comparison with the theoretical function shows that the RK4 method gradually becomes more out of phase, amd grows in amplitude as the 
number of oscillations increases.
- the energy plot also shows the energy increasing in the RK4 method as time goes on.
- ex2_core_1_amplitude plots the period against the initial amplitude
- As the initial amplitude increases, the period also increases.
- At small initial amplitude, the period is very close to 2*pi, which is as expected. At pi/2, the period is 7.02 rad s^-1.
- Near to initial amplitude of pi, which corresponds to the pendulum standing vertically straight, the solution doesn't work well.

Core Task 2
- the damping coefficient result in the amplitude decaying to 0. q = 0.5 was underdamped, and q = 5, 10 was an overdamped system
- ex2_core_2_damping.pdf shows the effect of the damping coefficient
- the force coefficient lead to non sinusoidal displacement/velocity for high force coefficients
- ex2_core_2_force_displacement.pdf and ex2_core_2_force_displacement.pdf shows the effect of the force coefficient
- at high (1.44, 1.465) and low (0.5) force coefficient, the velocity is periodic. At medium force coefficient (1.2), the velocity is irregular.
- the period is around 8.6 rad s^-1 when there is a force

Supplementary Task 1
- ex2_supp_1.pdf contains the plot of the displacement after ~6000 seconds for the two values of initial displacement
- the displacement diverges between the two very similar values

Supplementary Task 2
- ex2_supp_2.pdf contains plots of velocity against time for different q and F values
- it appears that the more squiggly the lines are, the more chaotic the system is
- can see that low damping and high force cofficient leads to a very chaotic system
