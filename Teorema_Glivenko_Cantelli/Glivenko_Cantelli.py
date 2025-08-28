import numpy as np
from scipy.stats import norm

# Valores de A (potência de 2)
A_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Ponto fixo para avaliação da CDF
x_values = np.linspace(-4, 4, 1000)

# Cabeçalho da tabela
print(f"{'2^A':<10} {'PROCURANDO':<15} {'2^(A+1)-1'}")

for A in A_values:
    inicio = 2**A
    fim = 2**(A+1) - 1
    n = fim  # usar o valor final como tamanho da amostra

    # Amostra da normal padrão
    sample = np.random.normal(0, 1, n)

    # Função de distribuição empírica
    F_n = np.array([np.mean(sample <= x) for x in x_values])
    F = norm.cdf(x_values)

    # Diferença suprema
    diff = np.abs(F_n - F)
    i_max = np.argmax(diff)
    x_procurado = x_values[i_max]

    # Mapear x_procurado para índice da amostra ordenada
    # Como estamos em distribuição normal, usamos quantil:
    proporcao = norm.cdf(x_procurado)
    procurando = int(round(inicio + proporcao * (fim - inicio)))

    # Garante que fique dentro do intervalo [inicio, fim]
    procurando = max(inicio, min(procurando, fim))

    # Imprime linha da tabela
    print(f"{inicio:<10} '{procurando:<14} {fim}")
