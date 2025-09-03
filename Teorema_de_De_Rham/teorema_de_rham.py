# nome: teorema_de_rham.py

import numpy as np

# Função para calcular o valor esperado pelo teorema dentro do intervalo
def calcular_valor_esperado(inicio, fim):
    # Aproximação simples usando o valor médio do intervalo (ou alguma outra heurística que você preferir)
    return (inicio + fim) // 2

# Tabela de entrada
valores = []
for N in range(10):  # Limite de 0 a 9
    inicio = 2**N
    fim = 2**(N+1) - 1
    esperado = calcular_valor_esperado(inicio, fim)
    valores.append([N, inicio, esperado, fim])

# Imprimir a tabela gerada
print("Tabela Gerada:")
print("N | Início (2^N) | Esperado pelo Teorema | Fim (2^(N+1))-1")
for linha in valores:
    print(f"{linha[0]}  | {linha[1]}         | {linha[2]}                   | {linha[3]}")

# Para referência, podemos verificar o quanto os valores esperados diferem dos valores fornecidos (coluna Esperado)
valores_reais = [1, 3, 7, 8, 21, 49, 76, 224, 467, 514]  # Os valores fornecidos na tabela
erros = [abs(valores[i][2] - valores_reais[i]) for i in range(10)]

# Imprimir os erros de aproximação
print("\nErros de Aproximação:")
for i, erro in enumerate(erros):
    print(f"N = {i}, Erro = {erro}")
