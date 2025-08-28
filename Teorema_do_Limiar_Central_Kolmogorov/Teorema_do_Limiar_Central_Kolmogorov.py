import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Número de amostras por valor de A
N = 10000
A_values = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Lista para armazenar estatísticas
tabela = []

# Coleta de dados
for A in A_values:
    n = 2**A
    upper_bound = 2**(A+1) - 1

    # Geração das amostras Bernoulli(0.5)
    samples = np.random.randint(0, 2, size=(N, n))
    sums = samples.sum(axis=1)

    # Cálculo do retorno do teorema (média das somas)
    retorno_teorema = np.mean(sums)

    # Armazena para tabela e gráficos
    tabela.append((2**A, retorno_teorema, upper_bound, sums, A))

# Impressão da TABELA
print(f"{'2^A':<7} {'Retorno do teorema (média)':<30} {'2^(A+1)-1':<15}")
print("-" * 60)
for linha in tabela:
    n, media, limite_superior, _, _ = linha
    print(f"{n:<7} {media:<30.2f} {limite_superior:<15}")

# PLOT dos GRÁFICOS
for n, media, limite_superior, sums, A in tabela:
    std = np.std(sums)
    z_scores = (sums - media) / std

    plt.figure(figsize=(8, 4))
    plt.hist(z_scores, bins=50, density=True, alpha=0.6, label='Distribuição da Soma Normalizada')

    # Curva Normal padrão
    x = np.linspace(-4, 4, 200)
    plt.plot(x, norm.pdf(x), 'r--', label='Curva Normal Padrão N(0,1)')

    plt.title(f'TLC - Soma de {n} Variáveis Bernoulli (A = {A})')
    plt.xlabel('Z-score')
    plt.ylabel('Densidade')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
