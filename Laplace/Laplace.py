import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Valor fixo de s (pode mudar para testar)
s = 1.0

# Novo range de n: 0 até 20
n_values = np.arange(0, 21)

# Função para calcular o termo geral da série geométrica
def term(n, s):
    return (2 * np.exp(-s))**n

# Calculando termos individuais e somas parciais
terms = [term(n, s) for n in n_values]
partial_sums = np.cumsum(terms)

# Calculando números de Mersenne: M_n = 2^n - 1
mersennes = [2**n - 1 for n in n_values]

# Imprimindo tabela de valores
print(f"{'n':>2} | {'Termo (2 e^-s)^n':>20} | {'Soma parcial F_n(s)':>20} | {'Mersenne 2^n - 1':>15}")
print('-'*65)
for i in range(len(n_values)):
    print(f"{n_values[i]:2d} | {terms[i]:20.6f} | {partial_sums[i]:20.6f} | {mersennes[i]:15d}")

# Criando figura e eixo para animação
fig, ax = plt.subplots(figsize=(9,6))
ax.set_xlim(0, max(n_values))
ax.set_ylim(0, max(partial_sums)*1.1)
ax.set_xlabel('Número de termos somados (n)')
ax.set_ylabel(r'Soma parcial $F_n(s)$')
ax.set_title(r'Animação da soma parcial $F_n(s) = \sum_{k=0}^n (2 e^{-s})^k$, com $s=1$')
ax.grid(True)

line, = ax.plot([], [], 'o-', lw=2, label='Soma parcial')

ax.legend()

# Função para atualizar cada frame da animação
def update(frame):
    x = n_values[:frame+1]
    y = partial_sums[:frame+1]
    line.set_data(x, y)
    return line,

# Criando animação
ani = FuncAnimation(fig, update, frames=len(n_values), interval=500, blit=True, repeat=True)

plt.show()
