# radon_nikodym_animation.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from mpl_toolkits.mplot3d import Axes3D

# Configurações para o formato vertical (9:16)
fig = plt.figure(figsize=(6, 10))  # proporção aproximada 9:16
ax = fig.add_subplot(111, projection='3d')

# Geração dos pontos: potências de 2 e números de Mersenne para n=0..10
n_vals = np.arange(0, 11)
x_vals = 2**n_vals
y_vals = 2**(n_vals + 1) - 1
z_vals = np.zeros_like(x_vals)  # Z = 0 para todos

# Para efeito visual, adicionamos z crescente (apenas para efeito 3D)
z_vals = np.linspace(0, 10, len(n_vals))

# Inicializar o gráfico
ax.set_xlim(0, max(x_vals)*1.1)
ax.set_ylim(0, max(y_vals)*1.1)
ax.set_zlim(0, max(z_vals)*1.1)
ax.set_xlabel("Potências de 2 (2^n)")
ax.set_ylabel("Números de Mersenne (2^(n+1)-1)")
ax.set_zlabel("Dimensão Z (animação)")

ax.set_title("Aplicação visual do Teorema de Radon–Nikodym\n"
             "Pontos e vetores conectando medidas")

# Armazenar linhas e pontos para animação
points, = ax.plot([], [], [], 'o', color='blue', markersize=8, label='Pontos (Medida μ)')
lines = []

# Função para criar vetores entre os pontos - Representa a "densidade" ou transformação f
def create_lines():
    for i in range(len(n_vals) - 1):
        line, = ax.plot([], [], [], color='red', alpha=0.6, lw=2)
        lines.append(line)

create_lines()

# Número total de frames = duração * fps
duration = 20  # segundos
fps = 30
total_frames = duration * fps

# Mostrar os pontos e linhas sequencialmente
def update(frame):
    # Quantidade de pontos para mostrar proporcional ao frame
    max_points = int(len(n_vals) * frame / total_frames) + 1
    max_points = min(max_points, len(n_vals))

    # Atualizar pontos
    points.set_data(x_vals[:max_points], y_vals[:max_points])
    points.set_3d_properties(z_vals[:max_points])

    # Atualizar linhas conectando os pontos já exibidos
    for i, line in enumerate(lines):
        if i < max_points - 1:
            x_line = [x_vals[i], x_vals[i+1]]
            y_line = [y_vals[i], y_vals[i+1]]
            z_line = [z_vals[i], z_vals[i+1]]
            line.set_data(x_line, y_line)
            line.set_3d_properties(z_line)
        else:
            line.set_data([], [])
            line.set_3d_properties([])

    return [points, *lines]

# Criar animação
anim = FuncAnimation(fig, update, frames=total_frames, interval=1000/fps, blit=True)

# Salvar GIF
gif_filename = "radon_nikodym_animation.gif"
print("Gerando GIF, aguarde...")

writer = PillowWriter(fps=fps)
anim.save(gif_filename, writer=writer, dpi=80)

print(f"GIF salvo como {gif_filename}")

plt.legend()
plt.show()
