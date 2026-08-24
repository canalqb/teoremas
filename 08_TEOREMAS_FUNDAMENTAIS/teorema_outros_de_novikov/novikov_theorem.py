# novikov_theorem.py

import numpy as np

# Função para calcular o valor esperado com base no intervalo
def calcular_valor_esperado(inicio, fim):
    return (inicio + fim) // 2  # Valor médio como aproximação do valor esperado

# Definir a tabela com os valores de N e seus respectivos intervalos (Início e Fim)
valores_N = list(range(10))  # De 0 a 9
tabela = []

# Preencher a tabela com os valores de Início, Fim e Esperado pelo Teorema
for N in valores_N:
    inicio = 2 ** N
    fim = (2 ** (N + 1)) - 1
    esperado = calcular_valor_esperado(inicio, fim)
    tabela.append([N, inicio, esperado, fim])

# Imprimir a tabela gerada
print("Tabela de Valores Calculados:")
print("N | Início (2^N) | Esperado pelo Teorema | Fim (2^(N+1))-1")
for linha in tabela:
    print(f"{linha[0]} | {linha[1]} | {linha[2]} | {linha[3]}")
