from ex3_core import *


R = 1; N = 100; size = 100
x_line = np.linspace(-1.5, 1.5, size)
y_line = np.linspace(-1.5, 1.5, size)

X, Y, Z = np.meshgrid(x_line, y_line, 0)
coordinates_points = np.transpose(np.vstack([X.ravel(), Y.ravel(), Z.ravel()]))
wire = circular_coil(R, [0, 0, 0], N)

B_field = get_B_field(coordinates_points, wire)
B_field_magnitude = np.sqrt(np.einsum("ij,ij->i", B_field, B_field))

B_field_xy_grid = np.zeros([size, size])
for ind, coord in enumerate(coordinates_points):
    x_grid_position, = np.where(x_line == coord[0])
    y_grid_position, = np.where(y_line == coord[1])

    B_field_xy_grid[x_grid_position[0]][y_grid_position[0]] = B_field_magnitude[ind] if B_field_magnitude[ind] < 2 else 2


fig, ax = plt.subplots()
im = ax.imshow(np.transpose(B_field_xy_grid), extent=[-2, 2, -2, 2])
cbar = fig.colorbar(im)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("plot of B field in the x-y plane from a single circular coil")
fig.savefig("ex3_core_1_xy.pdf")





