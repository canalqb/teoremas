# teorema_hopf_rinow.py

import numpy as np

# Definição da tabela fornecida
tabela = [
    (0, 1, 1, 1),
    (1, 2, 3, 3),
    (2, 4, 7, 7),
    (3, 8, 8, 15),
    (4, 16, 21, 31),
    (5, 32, 49, 63),
    (6, 64, 76, 127),
    (7, 128, 224, 255),
    (8, 256, 467, 511),
    (9, 512, 514, 1023)
]

# Função para calcular o valor esperado do teorema com base na fórmula
def calcular_esperado_inicio_fim(inicio, fim):
    # Usaremos uma simples média entre o inicio e o fim como aproximação
    return (inicio + fim) // 2

# Função para gerar a tabela de resultados esperados
def gerar_resultados(tabela):
    resultados = []
    for N, inicio, esperado, fim in tabela:
        esperado_calculado = calcular_esperado_inicio_fim(inicio, fim)
        resultados.append((N, inicio, esperado_calculado, fim))
    return resultados

# Gerar os resultados
resultados = gerar_resultados(tabela)

# Exibir a tabela com os resultados
print("Tabela de Resultados:")
print("| N  | Inicio (2^N) | Esperado pelo teorema | Fim (2^(N+1))-1 |")
print("|----|--------------|----------------------|-----------------|")
for resultado in resultados:
    N, inicio, esperado, fim = resultado
    print(f"| {N:<2} | {inicio:<12} | {esperado:<20} | {fim:<15} |")
