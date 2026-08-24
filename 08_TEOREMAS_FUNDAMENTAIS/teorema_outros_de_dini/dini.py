import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Domínio em potências de 2
k_vals = np.linspace(-5, 0, 100)
x = 2 ** k_vals
log_x = np.log10(x)

# Valores de n para a sequência f_n
n_values = np.arange(5, 60, 2)

# Função limite
f_limite = np.sqrt(x)

# Setup da figura 3D
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')
ax.set_title("Representação do Teorema de Dini com erro na cor", fontsize=14)
ax.set_xlabel('log10(x = 2^k)')
ax.set_ylabel('fₙ(x)')
ax.set_zlabel('n')

ax.set_xlim(log_x.min(), log_x.max())
ax.set_ylim(0, np.sqrt(1.1))  # f(x) máximo perto de 1
ax.set_zlim(n_values[0], n_values[-1])

# Variáveis para a animação
surf = None

# Função para atualizar o gráfico
def update(i):
    global surf
    n = n_values[i]
    f_n = np.sqrt(x + 1/n)
    erro = np.abs(f_n - f_limite)
    
    ax.clear()
    ax.set_title(f"Teorema de Dini — n = {n}", fontsize=14)
    ax.set_xlabel('log10(x = 2^k)')
    ax.set_ylabel('fₙ(x)')
    ax.set_zlabel('n')
    ax.set_xlim(log_x.min(), log_x.max())
    ax.set_ylim(0, np.sqrt(1.1))
    ax.set_zlim(n_values[0], n_values[-1])
    
    # Superfície: n constante para toda linha, função e erro em cor
    # Usamos scatter 3D colorido para mostrar o erro
    sc = ax.scatter(log_x, f_n, np.full_like(x, n), c=erro, cmap='viridis', marker='o')
    
    # Curva da função limite no nível máximo n
    ax.plot(log_x, f_limite, np.full_like(x, n_values[-1]), color='black', linestyle='--', linewidth=2, label='Limite f(x)=√x')
    
    ax.legend()
    
    return sc,

ani = FuncAnimation(fig, update, frames=len(n_values), interval=300, blit=False)

plt.tight_layout()
plt.show()
