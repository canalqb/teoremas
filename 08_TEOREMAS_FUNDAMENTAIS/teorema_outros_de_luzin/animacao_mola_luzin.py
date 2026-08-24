import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Dados: potências de 2 de n=0 até n=10
n = np.arange(0, 11)
x = 2 ** n

# Função com descontinuidades nos pontos 8 e 128
def f(x):
    y = np.log2(x)
    y[x == 8] = 20
    y[x == 128] = -10
    return y

y = f(x)

# Limites do gráfico
y_min, y_max = -15, 25

# Amplitude de oscilação (10% da distância até topo e fundo)
amp_up = 0.1 * (y_max - y)
amp_down = 0.1 * (y - y_min)
amplitudes_base = np.minimum(amp_up, amp_down)

# Parâmetros da animação
frames = 100
decay = 0.95  # amortecimento da oscilação

freq_base = 2 * np.pi * 2  # frequência base (2 ciclos por segundo)

np.random.seed(42)  # para reprodução

# Amplitudes e frequências individuais com variação para cada ponto
amplitudes = amplitudes_base * (0.7 + 0.6 * np.random.rand(len(x)))  # entre 0.7x e 1.3x
frequencies = freq_base * (0.8 + 0.4 * np.random.rand(len(x)))       # entre 0.8x e 1.2x

# Criar figura e scatter plot
fig, ax = plt.subplots(figsize=(12, 7))
scat = ax.scatter(x, y, color='blue', s=100)

ax.set_xlim(0, 1100)
ax.set_ylim(y_min, y_max)
ax.set_xlabel('x = 2^n')
ax.set_ylabel('f(x)')
ax.set_title('Animação efeito mola com energias diferentes - Teorema de Luzin')
ax.grid(True)
ax.set_xticks(x)
ax.set_xticklabels([f'$2^{i}$' for i in n])

# Texto para mostrar o frame atual
text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

def update(frame):
    global amplitudes
    amplitudes *= decay
    offsets = amplitudes * np.sin(frequencies * frame / frames * 2 * np.pi)
    y_anim = y + offsets
    scat.set_offsets(np.c_[x, y_anim])
    text.set_text(f'Frame: {frame+1}/{frames}')
    return scat, text

ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True, repeat=False)

# Salvar como GIF
gif_path = "animacao_mola_luzin.gif"
writer = PillowWriter(fps=20)  # 20 frames por segundo (ajuste se quiser)
ani.save(gif_path, writer=writer)
print(f"Animação salva em {gif_path}")

plt.show()
