import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as cst


def circular_coil(radius, centre_of_coil, N_points):
    # centre of coil should be an array in [x, y, z] form
    # assume that the axis is in the x direction
    theta = np.linspace(0, 2 * np.pi, N_points)
    points_on_coil = np.array([
        [centre_of_coil[0]] * N_points, 
        centre_of_coil[1] + np.sin(theta),
        centre_of_coil[2] + np.cos(theta)
    ])

    return np.transpose(points_on_coil)


def get_B_field(coordinates, wire):
    I = 1 / cst.mu_0
    B_field = []

    for coord in coordinates:
        dBs = []        
        for i in range(1, len(wire)):
            dl = wire[i] - wire[i - 1]
            r = coord - wire[i - 1]
            r_magnitude = np.sqrt(r.dot(r))

            dB = cst.mu_0 * I * np.cross(dl, r) / (4 * cst.pi * r_magnitude**3)
            dBs.append(dB)
        
        B_field.append(np.sum(dBs, axis=0))

    return B_field