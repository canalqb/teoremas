import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

# Parâmetros
x = np.linspace(-1, 1, 500)
n_vals = np.arange(0, 11)
X, N = np.meshgrid(x, n_vals)

# Frequências intercaladas: potências e Mersenne
freqs = np.array([
    2**n if n % 2 == 0 else 2**(n+1) - 1
    for n in n_vals
])

# Função base (sem tremor)
def base_surface(freqs, X):
    return np.sin(freqs[:, None] * X) / (1 + np.abs(X))

Z_base = base_surface(freqs, X)

# Configuração da figura
fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('n')
ax.set_zlabel('f_n(x)')
ax.set_title('Teorema de Banach–Steinhaus: Potências de 2 e Mersenne alternados')

# Inicialização do gráfico da superfície
surface = [ax.plot_surface(X, N, Z_base, cmap='viridis', edgecolor='none')]

# Função de animação
def animate(frame):
    # Remove superfície anterior
    for coll in ax.collections:
        coll.remove()

    # Ruído pequeno para o tremor (amplitude decrescente)
    noise = 0.1 * np.sin(frame / 5) * np.random.randn(*Z_base.shape)

    # Adiciona o ruído ao Z_base para simular tremor
    Z_noisy = Z_base + noise

    # Piscar (alternar transparência)
    alpha = 0.5 + 0.5 * np.sin(frame / 3)

    # Plota a superfície atualizada
    surf = ax.plot_surface(
        X, N, Z_noisy,
        cmap='viridis',
        edgecolor='none',
        alpha=alpha
    )
    return [surf]


# Criar animação
ani = animation.FuncAnimation(
    fig, animate, frames=100, interval=50, blit=False
)

plt.show()
