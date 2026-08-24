import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parâmetros
np.random.seed(42)
mu = 0.5  # Esperança da distribuição Bernoulli(p=0.5)
n_total = 256
X = np.random.binomial(n=1, p=mu, size=n_total)  # Amostras i.i.d de Bernoulli(0.5)

# Tabela dos intervalos
intervalos = [
    (1, 2),
    (2, 4),
    (4, 8),
    (8, 16),
    (16, 32),
    (32, 64),
    (64, 128),
    (128, 256)
]

# Calculando médias amostrais por intervalo
dados = []
for inicio, fim in intervalos:
    amostra = X[inicio:fim]
    media = np.mean(amostra)
    dados.append({
        'Inicio': inicio,
        'Fim': fim,
        'Tamanho': fim - inicio,
        'Media Amostral': media
    })

df = pd.DataFrame(dados)
print("\nDados da Amostra por Intervalo:\n")
print(df)

# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(df['Fim'], df['Media Amostral'], marker='o', label='Média Amostral')
plt.axhline(y=mu, color='r', linestyle='--', label='Esperança Teórica (μ = 0.5)')
plt.title('Lei dos Grandes Números - Convergência da Média Amostral')
plt.xlabel('Fim do Intervalo')
plt.ylabel('Média Amostral')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
