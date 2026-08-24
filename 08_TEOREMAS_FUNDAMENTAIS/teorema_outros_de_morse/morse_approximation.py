# # morse_approximation.py

import numpy as np

# Definir os valores para N, Início (2^N), e Fim (2^(N+1) - 1)
valores_N = np.arange(10)  # N vai de 0 a 9
inicio = 2 ** valores_N  # Início (2^N)
fim = (2 ** (valores_N + 1)) - 1  # Fim (2^(N+1) - 1)

# Função para calcular uma aproximação dentro do intervalo [Início, Fim]
def aproximar_teorema(inicio, fim):
    # Aproximação simples para gerar os valores esperados (não usar diretamente a coluna Esperado)
    return (inicio + fim) // 2  # Média entre início e fim como aproximação

# Gerar a tabela de valores e a coluna de "Esperado pelo Teorema"
tabela = []

for i in range(len(valores_N)):
    esperado = aproximar_teorema(inicio[i], fim[i])
    tabela.append([valores_N[i], inicio[i], esperado, fim[i]])

# Exibir a tabela
print("Tabela gerada:")
print(f"{'N':<3} {'Início (2^N)':<15} {'Esperado pelo Teorema':<25} {'Fim (2^(N+1))-1':<20}")
for linha in tabela:
    print(f"{linha[0]:<3} {linha[1]:<15} {linha[2]:<25} {linha[3]:<20}")

