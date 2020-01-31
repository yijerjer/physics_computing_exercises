from ex3_core import *


def get_mean_max_deviation(B_field_magnitude):
    mean = np.mean(B_field_magnitude)
    fractional_deviation = np.abs(mean - B_field_magnitude) / mean
    max_deviation = max(fractional_deviation)
    print(f"mean: {mean}, maximum deviation from mean: {max_deviation}")
    

R = 1; N = 100; size = 100
x_line = np.linspace(-0.05, 0.05, size)
y_line = np.linspace(-0.05, 0.05, size)

X, Y, Z = np.meshgrid(x_line, y_line, 0)
coordinates_points = np.transpose(np.vstack([X.ravel(), Y.ravel(), Z.ravel()]))
helmholtz_wire = np.concatenate((circular_coil(R, [-R/2, 0, 0], 100), circular_coil(R, [R/2, 0, 0], 100)))

B_field = get_B_field(coordinates_points, helmholtz_wire)
B_field_magnitude = np.sqrt(np.einsum("ij,ij->i", B_field, B_field))
get_mean_max_deviation(B_field_magnitude)

B_field_xy_grid = np.zeros([size, size])
for ind, coord in enumerate(coordinates_points):
    x_grid_position, = np.where(x_line == coord[0])
    y_grid_position, = np.where(y_line == coord[1])

    B_field_xy_grid[x_grid_position[0]][y_grid_position[0]] = B_field_magnitude[ind] if B_field_magnitude[ind] < 2 else 2


fig, ax = plt.subplots()
im = ax.imshow(np.transpose(B_field_xy_grid), extent=[-0.05, 0.05, -0.05, 0.05])
cbar = fig.colorbar(im)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("plot of B field in the x-y plane from a Helmholtz coil near the origin")
plt.savefig("ex3_core_2_xy_zoom.pdf")
