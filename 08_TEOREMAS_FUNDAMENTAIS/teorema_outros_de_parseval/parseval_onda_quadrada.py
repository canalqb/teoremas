import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

T = 2 * np.pi
w0 = 2 * np.pi / T
t_vals = np.linspace(0, T, 500)

# Função para aproximar a onda quadrada com N termos (N é potência de 2)
def square_wave_approx(t, N_terms):
    result = np.zeros_like(t)
    # Somente harmônicos ímpares: 1, 3, 5, ..., até (2*N_terms - 1)
    for k in range(1, 2*N_terms, 2):
        result += np.sin(k * w0 * t) / k
    return (4 / np.pi) * result

# Prepara figura e eixo
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2, label='Aproximação Onda Quadrada')
point, = ax.plot([], [], 'yo', markersize=10)
label = ax.text(0, 0, '', fontsize=9, color='orange', bbox=dict(facecolor='black', alpha=0.5))

ax.set_xlim(0, T)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('t')
ax.set_ylabel('x(t)')
ax.set_title('Aproximação da Onda Quadrada com N termos = 2^n')
ax.grid(True)
ax.legend()

# Valores de n (0 a 10)
n_values = np.arange(0, 11)

def update(frame):
    n = n_values[frame]
    N_terms = 2**n
    y_vals = square_wave_approx(t_vals, N_terms)
    line.set_data(t_vals, y_vals)
    
    # Ponto amarelo andando
    i = frame * 5  # controla posição do ponto na linha
    if i >= len(t_vals):
        i = len(t_vals) - 1
    t = t_vals[i]
    y = y_vals[i]
    point.set_data([t], [y])
    label.set_position((t, y + 0.3))
    label.set_text(f'N=2^{n}={N_terms}\nt={t:.2f}\nx={y:.2f}')
    
    return line, point, label

ani = FuncAnimation(fig, update, frames=len(n_values), interval=1000, repeat=True, blit=True)
ani.save('Parseval.gif', writer='pillow', fps=2)

plt.show()
