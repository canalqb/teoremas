# borel_cantelli_animation.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# --- Dados ---
n_values = np.arange(0, 11)  # n=0..10
powers_of_two = 2 ** n_values
mersenne_numbers = 2 ** (n_values + 1) - 1

# Normalizar para ficar visualmente melhor
x = n_values  # eixo x = índice n
y = powers_of_two / max(powers_of_two)  # eixo y = potências de 2 normalizadas
z = mersenne_numbers / max(mersenne_numbers)  # eixo z = números de Mersenne normalizados

# --- Configuração da figura 3D vertical (9:16) ---
fig = plt.figure(figsize=(6, 10))  # aspecto vertical
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(-1, 11)
ax.set_ylim(0, 1.1)
ax.set_zlim(0, 1.1)

ax.set_xlabel('n')
ax.set_ylabel('P(P_n)')
ax.set_zlabel('P(M_n)')

ax.set_title('Visualização do Teorema de Borel–Cantelli\nEventos e suas Probabilidades ao longo do tempo \n P(P_n)->(Potência de 2 normalizada) \n P(M_n)->(Número de Mersenne normalizado)')

points, = ax.plot([], [], [], 'o', color='red')
lines, = ax.plot([], [], [], '-', color='blue', alpha=0.7)

# Para a animação vamos mostrar pontos sequenciais
total_duration = 20  # segundos
fps = 30
total_frames = total_duration * fps
frames_per_point = total_frames // len(n_values)

# Armazenar dados animados
x_anim = []
y_anim = []
z_anim = []

def update(frame):
    global x_anim, y_anim, z_anim
    
    # Qual ponto deve ser mostrado agora?
    idx = min(frame // frames_per_point, len(n_values) - 1)
    
    # Atualiza os pontos animados
    x_anim = x[:idx+1]
    y_anim = y[:idx+1]
    z_anim = z[:idx+1]
    
    points.set_data(x_anim, y_anim)
    points.set_3d_properties(z_anim)
    
    # Atualiza as linhas conectando os pontos
    lines.set_data(x_anim, y_anim)
    lines.set_3d_properties(z_anim)
    
    return points, lines

# --- Criação da animação ---
anim = FuncAnimation(fig, update, frames=total_frames, interval=1000/fps, blit=True)

# --- Salvar como GIF ---
gif_filename = "borel_cantelli_animation.gif"
writer = PillowWriter(fps=fps)
anim.save(gif_filename, writer=writer)

print(f"Animação salva em {gif_filename}")
