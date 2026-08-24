import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

def f(z):
    return 1 / (z * (z - 1))

def coef(k):
    return 1 if k >= -1 else 0

r = 0.8
theta = np.linspace(0, 2*np.pi, 400)
z_points = r * np.exp(1j * theta)
f_vals = f(z_points)

term_neg1 = coef(-1) * z_points**(-1)
partial_sum = term_neg1.copy()
partial_sums_per_n = [partial_sum.copy()]

for n in range(11):
    start = 2**n
    end = 2**(n+1) - 1
    block_sum = np.zeros_like(z_points, dtype=complex)
    for k in range(start, end + 1):
        block_sum += coef(k) * z_points**k
    partial_sum += block_sum
    partial_sums_per_n.append(partial_sum.copy())

blocks_to_plot = [0, 1, 3, 5, 10]
colors = plt.cm.viridis(np.linspace(0, 1, len(blocks_to_plot)))

fig = plt.figure(figsize=(14, 6))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

# Configurações visuais
for ax, vals, title, ylabel in zip(
    [ax1, ax2],
    [f_vals.real, f_vals.imag],
    ['Parte Real', 'Parte Imaginária'],
    ['Re', 'Im']
):
    ax.set_title(title)
    ax.set_xlabel('θ')
    ax.set_ylabel(ylabel)
    ax.set_zlabel('Profundidade (rotação)')
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(min(vals)*1.1, max(vals)*1.1)
    ax.set_zlim(-2, 2)

    # Ajustar câmera para visual mais plano e de frente
    ax.view_init(elev=10, azim=-90)

    # Remover "paredes" (background panes) 
    ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))  # invisível
    ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

    # Opcional: tirar grades
    ax.grid(False)

line_f_real, = ax1.plot([], [], [], color='black', linewidth=2, label='f(z) real')
line_f_imag, = ax2.plot([], [], [], color='black', linewidth=2, label='f(z) imag')

lines_real = []
lines_imag = []
for c in colors:
    lreal, = ax1.plot([], [], [], '--', color=c, label='Série parcial')
    limag, = ax2.plot([], [], [], '--', color=c, label='Série parcial')
    lines_real.append(lreal)
    lines_imag.append(limag)

ax1.legend()
ax2.legend()

def rotation_x(angle_rad):
    c, s = np.cos(angle_rad), np.sin(angle_rad)
    return np.array([
        [1, 0, 0],
        [0, c, -s],
        [0, s, c]
    ])

def update(frame):
    angle = np.radians(frame)
    R = rotation_x(angle)

    points_f_real = np.vstack([theta, f_vals.real, np.zeros_like(theta)])
    points_f_imag = np.vstack([theta, f_vals.imag, np.zeros_like(theta)])

    rotated_f_real = R @ points_f_real
    rotated_f_imag = R @ points_f_imag

    line_f_real.set_data(rotated_f_real[0], rotated_f_real[1])
    line_f_real.set_3d_properties(rotated_f_real[2])

    line_f_imag.set_data(rotated_f_imag[0], rotated_f_imag[1])
    line_f_imag.set_3d_properties(rotated_f_imag[2])

    for i, block_i in enumerate(blocks_to_plot):
        y_real = partial_sums_per_n[block_i].real
        y_imag = partial_sums_per_n[block_i].imag

        points_real = np.vstack([theta, y_real, np.zeros_like(theta)])
        points_imag = np.vstack([theta, y_imag, np.zeros_like(theta)])

        rotated_real = R @ points_real
        rotated_imag = R @ points_imag

        lines_real[i].set_data(rotated_real[0], rotated_real[1])
        lines_real[i].set_3d_properties(rotated_real[2])

        lines_imag[i].set_data(rotated_imag[0], rotated_imag[1])
        lines_imag[i].set_3d_properties(rotated_imag[2])

    return lines_real + lines_imag + [line_f_real, line_f_imag]

anim = FuncAnimation(
    fig, update,
    frames=np.linspace(0, 180, 90),
    interval=50,
    blit=False
)

plt.suptitle('Rotação vertical da Série de Laurent — visual limpo e plano')
anim.save("serie_laurent.gif", writer='pillow', fps=20)
plt.show()
