# kolmogorov_representation_intervals_reduced.py

import numpy as np
import matplotlib.pyplot as plt

# Funções
def original_function(x, y):
    return np.sin(x) * np.cos(y)

def psi1(x):
    return np.sin(x)

def psi2(y):
    return np.cos(y)

def phi1(z):
    return 0.5 * np.sin(z)

def approximated_function(x, y):
    return phi1(psi1(x) + psi2(y))

# Gerar valores dos intervalos [2^n, 2^{n+1} - 1] com amostragem
interval_values = []

for n in range(0, 30):
    start = 2 ** n
    end = (2 ** (n + 1)) - 1
    step = max(1, (end - start) // 16)  # amostragem inteligente (máx. 16 pontos por intervalo)
    interval_values.extend(range(start, end + 1, step))

# Converter para array numpy
interval_values = np.array(interval_values)

# Criar grid
X, Y = np.meshgrid(interval_values, interval_values)

# Avaliar funções
Z_original = original_function(X, Y)
Z_approx = approximated_function(X, Y)

# Amostras dos dados
print("Amostra de valores da função original (Z_original):")
print(Z_original[:5, :5])

print("\nAmostra de valores da aproximação (Z_approx):")
print(Z_approx[:5, :5])

# Exibir gráfico 3D (agora com menos dados)
fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.plot_surface(X, Y, Z_original, cmap='viridis')
ax1.set_title('Função Original')

ax2 = fig.add_subplot(1, 2, 2, projection='3d')
ax2.plot_surface(X, Y, Z_approx, cmap='plasma')
ax2.set_title('Aproximação via Kolmogorov')

plt.tight_layout()
plt.show()
