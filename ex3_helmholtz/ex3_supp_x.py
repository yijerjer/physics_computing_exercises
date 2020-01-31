from ex3_core import *

R = 1; N = 20; size = 100
x_line = np.linspace(-9, 9, size)

X, Y, Z = np.meshgrid(x_line, 0, 0)
coordinates_points = np.transpose(np.vstack([X.ravel(), Y.ravel(), Z.ravel()]))

plt.figure()
max_length = 10 * R
for N_coils in [5, 10, 20, 50, 100]:
    coil_x_location = np.linspace(-max_length / 2, max_length / 2, N_coils)
    wire = []
    for loc in coil_x_location:
        if len(wire) == 0:
            wire = circular_coil(R, [loc, 0, 0], N)
        else:
            wire = np.concatenate((wire, circular_coil(R, [loc, 0, 0], N)))


    B_field = get_B_field(coordinates_points, wire)
    B_field_magnitude = np.sqrt(np.einsum("ij,ij->i", B_field, B_field))
    plt.plot(x_line, B_field_magnitude, label=f"{N_coils} coils")

plt.xlabel("x")
plt.ylabel("magnitude of B field |B|")
plt.title("Plot of the B field along the x axis for different number of coils")
plt.legend()
plt.savefig("ex3_supp_x.pdf")
