# riesz_repr_l2.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Valores de N de 0 a 10
N_values = np.arange(0, 11)

# Limites do intervalo para cada N
inicio = 2 ** N_values
fim = 2 ** (N_values + 1) - 1

def calcula_valor_teorema(N):
    tamanho = fim[N] - inicio[N] + 1  # tamanho do intervalo = 2^N
    x = np.ones(tamanho)               # vetor x: função constante 1 no intervalo
    y = np.arange(1, tamanho + 1)     # vetor y: vetor crescente (1, 2, ..., tamanho)
    return int(np.dot(x, y))           # produto interno

# Calcula valores do teorema para cada N
valores_teorema = np.array([calcula_valor_teorema(N) for N in range(len(N_values))])

# Imprime a tabela completa
print(f"{'N':>2} | {'Início (2^N)':>12} | {'Valor do Teorema':>16} | {'Fim (2^{N+1}-1)':>15}")
print("-" * 56)
for n, ini, val, f in zip(N_values, inicio, valores_teorema, fim):
    print(f"{n:2d} | {ini:12d} | {val:16d} | {f:15d}")

# Dados para pontos 3D: vamos incluir a coluna do teorema no eixo Z para enriquecer a visualização
X = N_values
Y = inicio
Z = valores_teorema

# Setup da figura e eixo 3D (proporção vertical 9:16)
fig = plt.figure(figsize=(6, 10))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('N')
ax.set_ylabel('Início (2^N)')
ax.set_zlabel('Valor do Teorema (Produto Interno)')
ax.set_title('Representação do Teorema de Riesz em L²')

# Definindo limites dos eixos para melhor visualização
ax.set_xlim(0, 10)
ax.set_ylim(min(Y) - 10, max(Y) + 10)
ax.set_zlim(min(Z) - 10, max(Z) + 10)

# Inicializa os pontos (vazios)
scat = ax.scatter([], [], [], c='red', s=50)

# Guarda as linhas para poder remover depois
lines = []

def init():
    scat._offsets3d = ([], [], [])
    return scat,

def update(frame):
    xdata = X[:frame+1]
    ydata = Y[:frame+1]
    zdata = Z[:frame+1]
    scat._offsets3d = (xdata, ydata, zdata)

    # Remove linhas antigas
    while lines:
        line = lines.pop()
        line.remove()

    # Desenha linhas conectando cada ponto ao próximo para mostrar evolução
    for i in range(frame):
        line, = ax.plot([X[i], X[i+1]], [Y[i], Y[i+1]], [Z[i], Z[i+1]], color='blue', alpha=0.5)
        lines.append(line)

    return scat, *lines

frames = len(N_values)
interval = 2000  # intervalo de 2s entre frames para totalizar ~20s

ani = FuncAnimation(fig, update, frames=frames, init_func=init,
                    interval=interval, blit=False, repeat=False)

gif_filename = "riesz_repr_l2.gif"
writergif = PillowWriter(fps=frames/20)
ani.save(gif_filename, writer=writergif)

print(f"GIF salvo como {gif_filename}")

plt.show()
