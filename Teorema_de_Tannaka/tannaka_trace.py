import numpy as np
import matplotlib.pyplot as plt

# Valores reais (para validação)
powers_of_two = np.array([1, 2, 4, 8, 16, 32, 64, 128])
procurados_reais = np.array([1, 3, 7, 8, 21, 49, 76, 224])

# Estimativa: vamos tentar ajustar uma função do tipo f(n) = a * 2^n + b * n + c
n_vals = np.arange(len(powers_of_two))  # já que 2^n = powers_of_two, n = log2(powers_of_two)
x = powers_of_two
y = procurados_reais

# Construção de variáveis para regressão
X = np.vstack([x, np.log2(x), np.ones_like(x)]).T  # [2^n, n, 1]
coeffs, *_ = np.linalg.lstsq(X, y, rcond=None)
a, b, c = coeffs

def tannaka(x):
    """Teorema de Tannaka (heurístico): prediz Procurapeloteorema com base em 2^n"""
    return a * x + b * np.log2(x) + c

# Teste nos mesmos dados
valores_estimados = tannaka(powers_of_two)

# Mostrar os dados
print("2^n | Procurado Real | Estimado pelo Teorema de Tannaka")
print("----|----------------|-------------------------------")
for i in range(len(x)):
    print(f"{x[i]:>3} | {y[i]:>14} | {valores_estimados[i]:>25.2f}")

# Opcional: gráfico
plt.figure(figsize=(10, 6))
plt.plot(powers_of_two, y, 'o-', label="Valores reais (dados)")
plt.plot(powers_of_two, valores_estimados, 's--', label="Estimativa Teorema de Tannaka")
plt.xlabel("2^n (Início do intervalo)")
plt.ylabel("Procurapeloteorema")
plt.title("Validação do Teorema de Tannaka (heurístico)")
plt.legend()
plt.grid(True)
plt.xscale("log", base=2)
plt.xticks(powers_of_two, labels=[f"2^{int(np.log2(i))}" for i in powers_of_two])
plt.tight_layout()
plt.show()
