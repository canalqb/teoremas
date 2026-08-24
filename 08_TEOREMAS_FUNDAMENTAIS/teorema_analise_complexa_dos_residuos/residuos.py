import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Variável complexa
z = sp.symbols('z')

# Limite superior de n (configurável)
N_MAX = 10

# Cores dinâmicas com colormap
cmap = plt.cm.viridis
colors = cmap(np.linspace(0, 1, N_MAX + 1))

# Inicializar listas para gráfico
x_vals = []
y_vals = []
labels = []

# Loop principal para calcular pontos
for n in range(N_MAX + 1):
    a_n = 2 ** n
    M_n = 2 ** n - 1
    f = (z + M_n) / (z**2 + a_n)
    polos = sp.solve(sp.denom(f), z)
    # Polo com parte imaginária positiva
    polo_positivo = max(polos, key=lambda val: sp.im(val))
    res_pos = sp.residue(f, z, polo_positivo)
    produto = M_n * res_pos
    produto_num = sp.N(produto)
    x = float(sp.re(produto_num))
    y = float(sp.im(produto_num))
    x_vals.append(x)
    y_vals.append(y)
    labels.append(f"n = {n}")

# Configuração do gráfico e figura
fig, ax = plt.subplots(figsize=(10, 6))

# Plot dos pontos fixos
for i in range(N_MAX + 1):
    ax.plot(x_vals[i], y_vals[i], 'o', color=colors[i])
    ax.text(x_vals[i], y_vals[i], f"n={i}", fontsize=8, ha='right', va='bottom')

# Plot da trajetória (linha ligando os pontos)
ax.plot(x_vals, y_vals, linestyle='--', color='gray', alpha=0.5)

# Ponto que vai “andar” no gráfico
point, = ax.plot([], [], 'o', color='black', markersize=12)

# Configurações do gráfico
ax.axhline(0, color='gray', linestyle='--', linewidth=0.5)
ax.axvline(0, color='gray', linestyle='--', linewidth=0.5)
ax.set_xlabel('Parte Real')
ax.set_ylabel('Parte Imaginária')
ax.set_title('Produto: Resíduo × Número de Mersenne (por n) com Trajetória Animada')
ax.grid(True)
plt.tight_layout()

# Função de inicialização da animação
def init():
    point.set_data([], [])
    return point,

# Função para atualizar o ponto na animação
def update(frame):
    x = x_vals[frame]
    y = y_vals[frame]
    point.set_data([x], [y])  # <-- aqui, passar listas
    return point,


# Criar animação
ani = FuncAnimation(fig, update, frames=range(N_MAX + 1),
                    init_func=init, blit=True, interval=700, repeat=True)

plt.show()
