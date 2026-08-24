# nome do script: skolem_teorema.py

import numpy as np

def calcular_esperado_pelo_teorema(n):
    """
    Função para calcular o valor esperado dentro do intervalo [2^N, 2^(N+1) - 1]
    O cálculo é baseado em uma aproximação simples da distribuição dos números.
    """
    inicio = 2 ** n
    fim = (2 ** (n + 1)) - 1
    
    # Aproximação do valor esperado: usaremos a média entre o início e o fim.
    esperado = (inicio + fim) // 2
    
    return esperado

def gerar_tabela():
    """
    Função para gerar a tabela de valores com base nos cálculos realizados.
    """
    tabela = []
    for n in range(10):  # Para N de 0 a 9
        inicio = 2 ** n
        fim = (2 ** (n + 1)) - 1
        esperado = calcular_esperado_pelo_teorema(n)
        tabela.append([n, inicio, esperado, fim])
    return tabela

def imprimir_tabela(tabela):
    """
    Função para imprimir a tabela de valores.
    """
    print(f"{'N':<3} | {'Início (2^N)':<15} | {'Esperado pelo Teorema':<25} | {'Fim (2^(N+1))-1':<20}")
    print("-" * 70)
    for linha in tabela:
        print(f"{linha[0]:<3} | {linha[1]:<15} | {linha[2]:<25} | {linha[3]:<20}")

# Gerar e imprimir a tabela
tabela = gerar_tabela()
imprimir_tabela(tabela)
