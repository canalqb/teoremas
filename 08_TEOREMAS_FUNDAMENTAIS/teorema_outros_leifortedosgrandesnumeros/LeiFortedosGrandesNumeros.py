import numpy as np
import pandas as pd

# Parâmetros da simulação
mu = 5           # média verdadeira
sigma = 2        # desvio padrão
max_power = 8    # maior potência de 2 (ajuste aqui)

# Gerar variáveis aleatórias normais (i.i.d.)
N = 2**(max_power + 1)  # tamanho máximo da sequência
X = np.random.normal(loc=mu, scale=sigma, size=N)

# Função para calcular média amostral nos pontos desejados
def calc_means(X, max_power):
    results = []
    for A in range(1, max_power + 1):
        pow_2 = 2**A
        mersenne = 2**(A+1) - 1

        mean_pow_2 = np.mean(X[:pow_2])
        mean_mersenne = np.mean(X[:mersenne])

        results.append({
            '2^A': pow_2,
            'Média em 2^A': mean_pow_2,
            '2^(A+1)-1 (Mersenne)': mersenne,
            'Média em Mersenne': mean_mersenne
        })
    return results

# Calcular médias
data = calc_means(X, max_power)

# Mostrar tabela usando pandas
df = pd.DataFrame(data)
print(df.to_string(index=False))
