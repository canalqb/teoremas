# lebesgue_external_measure_viz.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from mpl_toolkits.mplot3d import Axes3D

# Parâmetros de entrada
n_values = np.arange(0, 11)
pot2 = 2 ** n_values
mersenne = 2 ** (n_values + 1) - 1

# Coordenadas no espaço (x, y, z)
x = pot2
y = mersenne
z = n_values
points = list(zip(x, y, z))

# Criar figura em proporção vertical (9:16)
fig = plt.figure(figsize=(6, 12))
ax = fig.add_subplot(111, projection='3d')
ax.set_title("Visualização do Teorema da Medida Externa de Lebesgue", fontsize=10)

# Limites dos eixos
ax.set_xlim(0, max(x) * 1.1)
ax.set_ylim(0, max(y) * 1.1)
ax.set_zlim(0, max(z) + 1)

# Rótulos dos eixos
ax.set_xlabel(r"$2^n$")
ax.set_ylabel(r"Número de Mersenne: $2^{n+1} - 1$")
ax.set_zlabel("n")

# Objetos gráficos
scatter = ax.scatter([], [], [], c='red', s=50)
lines = []

# Função de inicialização
def init():
    scatter._offsets3d = ([], [], [])
    return scatter,

# Função de atualização por frame
def update(frame):
    xi, yi, zi = points[frame]
    prev_x, prev_y, prev_z = scatter._offsets3d

    # Adicionar novo ponto
    new_x = list(prev_x) + [xi]
    new_y = list(prev_y) + [yi]
    new_z = list(prev_z) + [zi]
    scatter._offsets3d = (new_x, new_y, new_z)

    # Adicionar linha do ponto à origem
    line = ax.plot([0, xi], [0, yi], [0, zi], color='blue', alpha=0.6)[0]
    lines.append(line)

    return scatter, *lines

# Criar animação
frames = len(points)
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=False)

# Salvar como vídeo MP4 com duração de 20 segundos
fps = frames / 20  # 20 segundos de duração total
writer = FFMpegWriter(fps=fps)

ani.save("lebesgue_visualization.mp4", writer=writer)

# Mostrar visualização (opcional)
plt.show()
