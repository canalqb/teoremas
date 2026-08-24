import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

def powers_of_two(n_max):
    return [2**n for n in range(n_max+1)]

def mersenne_numbers_exp(n_max):
    mersennes = []
    for n in range(n_max+1):
        # Calcula 2^(2^n) mod grande para evitar overflow e transformar em ângulo rad
        exp_val = pow(2, 2**n, int(2*np.pi*1e6))
        angle = (exp_val / 1e6) % (2*np.pi)
        mersennes.append(angle)
    return mersennes

# Parâmetros
n_max = 10
fps = 30
duration = 5  # segundos
frames = fps * duration

# Preparar dados
powers = powers_of_two(n_max)
mersennes = mersenne_numbers_exp(n_max)

# Pontos no círculo unitário (menos pontos para performance)
theta = np.linspace(0, 2*np.pi, 200)
z = np.exp(1j * theta)

# Setup figura
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.grid(True)
ax.set_title('Família f_n(z) = z^(2^n) * e^{i M_n} com movimentos diferenciados')

colors = plt.cm.viridis(np.linspace(0, 1, n_max+1))
lines = []

for i in range(n_max+1):
    line, = ax.plot([], [], color=colors[i], lw=1.5, label=f'n={i}')
    lines.append(line)

ax.legend(loc='upper right', fontsize=8)

def update(frame):
    t = frame / fps  # tempo em segundos
    
    for n in range(n_max+1):
        base_f = z**powers[n] * np.exp(1j * mersennes[n])
        
        # Rotação no tempo
        direction = -1 if n % 2 == 0 else 1
        rot_angle = direction * t
        
        moved = base_f * np.exp(1j * rot_angle)
        
        # Tremor para múltiplos de 5 (exceto zero)
        if n != 0 and n % 5 == 0:
            tremor_amp = 0.1
            tremor_x = tremor_amp * np.sin(10 * t)
            tremor_y = tremor_amp * np.cos(10 * t)
            moved += tremor_x + 1j * tremor_y
        
        lines[n].set_data(moved.real, moved.imag)
    
    return lines

ani = FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# Salvar como GIF usando PillowWriter
ani.save("montel_potencias_mersennes.gif", writer=PillowWriter(fps=fps))

print("GIF salvo como montel_potencias_mersennes.gif")
