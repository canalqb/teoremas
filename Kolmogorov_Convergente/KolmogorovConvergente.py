import numpy as np
import matplotlib.pyplot as plt

# Definir os valores de A
A_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultados = []

np.random.seed(42)  # Reprodutibilidade

for A in A_values:
    start = 2**(A - 1)
    end = 2**A - 1
    tamanho_intervalo = end - start + 1

    # Gerar variáveis aleatórias independentes com esperança 0 e variância controlada
    # Usamos distribuição normal padrão escalada por 1/n^1.5 para garantir convergência (decrescimento rápido de variância)
    X = np.array([np.random.normal(0, 1 / (n ** 1.5)) for n in range(start, end + 1)])

    # Soma parcial da série neste intervalo
    soma = np.sum(X)

    # Centro do intervalo
    centro = (start + end) / 2

    resultados.append({
        '2^A': 2**A,
        'intervalo': f'[{start}, {end}]',
        'ponto_convergencia': centro,
        'soma_intervalo': soma
    })

# Exibir resultados
print("2^A\tIntervalo\t\tPonto_Médio\tSoma Aleatória")
for r in resultados:
    print(f"{r['2^A']}\t{r['intervalo']}\t{r['ponto_convergencia']:.1f}\t\t{r['soma_intervalo']:.5f}")

# Plotar as somas para visualizar convergência
plt.figure(figsize=(10, 5))
somas = [r['soma_intervalo'] for r in resultados]
pontos = [r['ponto_convergencia'] for r in resultados]

plt.plot(pontos, somas, marker='o', linestyle='-', color='purple')
plt.axhline(0, color='gray', linestyle='--')
plt.title("Convergência das Somatórias por Intervalo (Kolmogorov)")
plt.xlabel("Ponto médio do intervalo [2^{A-1}, 2^A - 1]")
plt.ylabel("Soma parcial das variáveis aleatórias")
plt.grid(True)
plt.tight_layout()
plt.show()
