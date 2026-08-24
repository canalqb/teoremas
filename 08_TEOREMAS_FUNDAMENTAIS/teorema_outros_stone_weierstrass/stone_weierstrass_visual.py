import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import interp1d

# Dados
n_values = np.arange(0, 11)
x_vals = 2 ** n_values
y_vals = (2 ** (n_values + 1)) - 1
z_vals = x_vals + y_vals

# Animação
fps = 5
duration = 20
frames = fps * duration

# Interpolação
t_original = np.linspace(0, 1, len(x_vals))
t_interp = np.linspace(0, 1, frames)

fx = interp1d(t_original, x_vals, kind='linear')
fy = interp1d(t_original, y_vals, kind='linear')
fz = interp1d(t_original, z_vals, kind='linear')

x_interp = fx(t_interp)
y_interp = fy(t_interp)
z_interp = fz(t_interp)

# Figura vertical
fig = plt.figure(figsize=(5, 9))
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(0, max(x_vals) * 1.1)
ax.set_ylim(0, max(y_vals) * 1.1)
ax.set_zlim(0, max(z_vals) * 1.1)
ax.set_xlabel("2^n")
ax.set_ylabel("2^{n+1} - 1")
ax.set_zlabel("Aproximação")
ax.set_title("Stone–Weierstrass - Visualização Compatível")

# Linha fixa
line, = ax.plot([], [], [], 'orange', linestyle='--', linewidth=1)

# Criar referência ao scatter (inicialmente None)
scatter = None

# Função de atualização
def update(frame):
    global scatter  # para podermos remover o anterior

    xi = x_interp[:frame+1]
    yi = y_interp[:frame+1]
    zi = z_interp[:frame+1]

    line.set_data(xi, yi)
    line.set_3d_properties(zi)

    # Remover o scatter anterior (se já foi criado)
    if scatter:
        scatter.remove()

    # Adicionar novo scatter
    scatter = ax.scatter(xi, yi, zi, c='blue', s=10)

    return line, scatter

# Criar animação
ani = FuncAnimation(fig, update, frames=frames, interval=1000 // fps, blit=False)

# Salvar GIF
ani.save("stone_weierstrass_animation.gif", writer='pillow', fps=fps)

# Mostrar em tela
plt.show()
