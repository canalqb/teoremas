import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Dados: potências de 2 e números de Mersenne
n_vals = np.arange(0, 11)
powers_of_2 = 2 ** n_vals
mersenne_numbers = 2 ** (n_vals + 1) - 1

# Toroide (fundo fixo)
def create_torus(R=10, r=3, n=100):
    theta = np.linspace(0, 2 * np.pi, n)
    phi = np.linspace(0, 2 * np.pi, n)
    theta, phi = np.meshgrid(theta, phi)
    X = (R + r * np.cos(theta)) * np.cos(phi)
    Y = (R + r * np.cos(theta)) * np.sin(phi)
    Z = r * np.sin(theta)
    return X, Y, Z

# Inicializa a figura
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Fundo fixo: toroide
X, Y, Z = create_torus()
ax.plot_surface(X, Y, Z, alpha=0.2, color='gray', edgecolor='k', linewidth=0.2)

# Inicializa os pontos (com placeholders que serão atualizados)
power_scatter = ax.scatter([], [], [], color='blue', s=50, label=r'$2^n$')
mersenne_scatter = ax.scatter([], [], [], color='red', s=50, label=r'$2^{n+1}-1$')
lines = []

# Eixos fixos
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.set_zlim(-5, 2500)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Valor")
ax.set_title("Teorema do Gráfico Fechado - Visual 3D Rotativo (Dados)")

# Cria os pontos 3D originais (x, y, z)
# Vamos posicionar os pontos em círculo no plano X-Y, com o valor em Z
angle_positions = np.linspace(0, 2 * np.pi, len(n_vals), endpoint=False)
radius = 10
x_base = radius * np.cos(angle_positions)
y_base = radius * np.sin(angle_positions)

power_points = np.stack([x_base, y_base, powers_of_2], axis=1)
mersenne_points = np.stack([x_base, y_base, mersenne_numbers], axis=1)

# Função para aplicar rotação em torno do eixo Z
def rotate_z(points, angle):
    rot_matrix = np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle),  np.cos(angle), 0],
        [0, 0, 1]
    ])
    return points @ rot_matrix.T

# Função de atualização da animação
def update(frame):
    angle = np.radians(frame)
    rot_power = rotate_z(power_points, angle)
    rot_mersenne = rotate_z(mersenne_points, angle)

    # Atualiza os pontos
    power_scatter._offsets3d = (rot_power[:, 0], rot_power[:, 1], rot_power[:, 2])
    mersenne_scatter._offsets3d = (rot_mersenne[:, 0], rot_mersenne[:, 1], rot_mersenne[:, 2])

    # Remove linhas anteriores
    for line in lines:
        line.remove()
    lines.clear()

    # Desenha "cilindros" verticais (como linhas) conectando cada par
    for p, m in zip(rot_power, rot_mersenne):
        x = [p[0], m[0]]
        y = [p[1], m[1]]
        z = [p[2], m[2]]
        line = ax.plot(x, y, z, color='black', linewidth=1)[0]
        lines.append(line)

    return power_scatter, mersenne_scatter, *lines

# Animação
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)

ax.legend()
plt.tight_layout()
plt.show()
