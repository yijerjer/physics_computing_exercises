from ex3_core import *


R = 1; N = 20; size = 100
N_coils = 10; max_length = 10 * R
x_line = np.linspace(-7, 7, size)
y_line = np.linspace(-7, 7, size)

X, Y, Z = np.meshgrid(x_line, y_line, 0)
coordinates_points = np.transpose(np.vstack([X.ravel(), Y.ravel(), Z.ravel()]))

coil_x_location = np.linspace(-max_length / 2, max_length / 2, N_coils)
wire = []
for loc in coil_x_location:
    if len(wire) == 0:
        wire = circular_coil(R, [loc, 0, 0], N)
    else:
        wire = np.concatenate((wire, circular_coil(R, [loc, 0, 0], N)))


B_field = get_B_field(coordinates_points, wire)
B_field_magnitude = np.sqrt(np.einsum("ij,ij->i", B_field, B_field))

B_field_xy_grid = np.zeros([size, size])
for ind, coord in enumerate(coordinates_points):
    x_grid_position, = np.where(x_line == coord[0])
    y_grid_position, = np.where(y_line == coord[1])

    B_field_xy_grid[x_grid_position[0]][y_grid_position[0]] = B_field_magnitude[ind] if B_field_magnitude[ind] < 2 else 2


fig, ax = plt.subplots()
im = ax.imshow(np.transpose(B_field_xy_grid), extent=[-7, 7, -7, 7])
cbar = fig.colorbar(im)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("plot of B field in the x-y plane from a 10 coils")
plt.savefig("ex3_supp_xy.pdf")