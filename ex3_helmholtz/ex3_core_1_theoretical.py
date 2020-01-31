from ex3_core import *


def theoretical_B_field_on_axis(radius, x):
    I = 1 / cst.mu_0
    B = cst.mu_0 * I * radius**2 / (2 * np.power(radius**2 + x**2, 3/2))
    return B


R = 1; N = 20
X, Y, Z = np.mgrid[-5:5:1000j, 0:0:1j, 0:0:1j]
coordinates_points = np.transpose(np.vstack([X.ravel(), Y.ravel(), Z.ravel()]))
wire = circular_coil(R, [0, 0, 0], N)

B_field = get_B_field(coordinates_points, wire)
B_field_magnitude = np.sqrt(np.einsum("ij,ij->i", B_field, B_field))

plt.figure(1)
plt.plot(X.ravel(), B_field_magnitude, label="Calculated B Field", linewidth=0.7)
plt.plot(X.ravel(), theoretical_B_field_on_axis(R, X.ravel()), label="Theoretical B Field", linewidth=0.5)
plt.title("Plot of the calculated and theoretical B field along the x axis for N = 20")
plt.xlabel("x")
plt.ylabel("magnitude of B field |B|")
plt.legend()
plt.savefig("ex3_core_1_theoretical.pdf")


plt.figure(2)

for n in [10, 20, 50, 100]:
    wire = circular_coil(R, [0, 0, 0], n)
    B_field_n = get_B_field(coordinates_points, wire)
    B_field_magnitude_n = np.sqrt(np.einsum("ij,ij->i", B_field_n, B_field_n))
    plt.plot(X.ravel(), theoretical_B_field_on_axis(R, X.ravel()) - B_field_magnitude_n, label=f"N = {n}", linewidth=0.7)

plt.title("Plot of the difference between calculated and theoretical B field \n along the x axis for N = 10, 20, 50, 100")
plt.xlabel("x")
plt.ylabel("difference between calculated and theoretical B field")
plt.legend()
plt.savefig("ex3_core_1_theoretical_diff.pdf")












