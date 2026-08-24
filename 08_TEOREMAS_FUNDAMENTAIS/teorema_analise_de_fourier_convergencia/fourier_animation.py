import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Função original: onda quadrada periódica
def square_wave(x):
    return np.where(np.mod(x, 2*np.pi) < np.pi, 1, -1)

# Série de Fourier da onda quadrada com N termos ímpares
def fourier_series_square_wave(x, N):
    result = np.zeros_like(x)
    for k in range(N):
        n = 2*k + 1  # Apenas ímpares
        result += (4 / (np.pi * n)) * np.sin(n * x)
    return result

# --- Configuração da animação ---
x = np.linspace(-2*np.pi, 2*np.pi, 1500)
f = square_wave(x)
n_values = range(1, 6)  # n de 1 até 5 (10 animações total)
total_frames = 200

# Prepara os dados de cada gráfico
data = []

for n in n_values:
    N_pow2 = 2**n
    N_mersenne = 2**n - 1

    y_pow2 = fourier_series_square_wave(x, N_pow2)
    y_mersenne = fourier_series_square_wave(x, N_mersenne)

    # Pulso: posição inicial e final diferentes
    for y, label in [(y_pow2, f'Potência de 2: N={N_pow2}'), (y_mersenne, f'Mersenne: N={N_mersenne}')]:
        idx_start = np.random.randint(0, len(x))
        idx_end = np.random.randint(0, len(x))

        # Interpola caminho do pulso
        indices = np.linspace(idx_start, idx_end, total_frames).astype(int)
        data.append({
            'x': x,
            'y': y,
            'label': label,
            'pulse_indices': indices
        })

# --- Criar a figura com subplots ---
fig, axes = plt.subplots(len(n_values), 2, figsize=(14, 10), sharex=True, sharey=True)
axes = axes.flatten()

lines = []
pulses = []

for i, d in enumerate(data):
    ax = axes[i]
    line, = ax.plot(d['x'], d['y'], 'gray', lw=1.5, label=d['label'])
    pulse, = ax.plot([], [], 'ro', markersize=8, label='Pulso elétrico')
    ax.set_title(d['label'])
    ax.set_ylim(-1.5, 1.5)
    ax.grid(True)
    ax.legend()
    lines.append(line)
    pulses.append(pulse)

fig.suptitle("Animação de Pulsos Elétricos nas Séries de Fourier (Potência de 2 vs Mersenne)", fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# --- Função de animação ---
def update(frame):
    for i, d in enumerate(data):
        idx = d['pulse_indices'][frame % len(d['pulse_indices'])]
        px = d['x'][idx]
        py = d['y'][idx]
        pulses[i].set_data([px], [py])
    return pulses

# --- Criar animação ---
ani = FuncAnimation(fig, update, frames=total_frames, interval=50, blit=True)

# --- Salvar como GIF ---
ani.save('fourier.gif', writer='pillow', fps=20)

plt.show()
