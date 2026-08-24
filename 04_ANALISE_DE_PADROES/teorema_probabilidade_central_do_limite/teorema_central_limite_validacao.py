import numpy as np
import matplotlib.pyplot as plt

# Tabela fornecida
intervalos = [
    (1, 2, 1),
    (2, 4, 3),
    (4, 8, 7),
    (8, 16, 8),
    (16, 32, 21),
    (32, 64, 49),
    (64, 128, 76),
    (128, 256, 224)
]

def simular_validacao(n_amostras, tamanho_amostra, mu=0, sigma=1):
    """
    Simula n_amostras médias de uma distribuição normal
    Retorna o número de médias que caem no intervalo [mu - 0.1, mu + 0.1]
    """
    medias = [np.mean(np.random.normal(mu, sigma, tamanho_amostra)) for _ in range(n_amostras)]
    acertos = sum([1 for m in medias if mu - 0.1 <= m <= mu + 0.1])
    return acertos / n_amostras  # Proporção de médias "válidas"

print("Validando colunas com base no Teorema Central do Limite:")
for inicio, fim, procuras in intervalos:
    tamanho_amostra = fim - inicio
    proporcao_estavel = simular_validacao(procuras, tamanho_amostra)
    print(f"Amostra de tamanho {tamanho_amostra:>3}, procuras: {procuras:>3} -> Proporção dentro do intervalo esperado: {proporcao_estavel:.2f}")

# Opcional: visualização
tamanhos = [fim - inicio for inicio, fim, _ in intervalos]
procuras = [p for _, _, p in intervalos]

plt.figure(figsize=(10, 6))
plt.plot(tamanhos, procuras, marker='o')
plt.xlabel("Tamanho da Amostra (Fim - Início)")
plt.ylabel("Número de Procuras (Simulações)")
plt.title("Validação da coluna do meio pelo Teorema Central do Limite")
plt.grid(True)
plt.show()
