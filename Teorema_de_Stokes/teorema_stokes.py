# teorema_stokes.py

import numpy as np

def calcular_esperado_por_teorema(N):
    """
    Função para calcular o valor esperado baseado na tabela fornecida
    Usando um modelo heurístico para aproximar os valores.
    """
    inicio = 2 ** N
    fim = 2 ** (N + 1) - 1

    # Formula simples para modelar a tendência dos resultados esperados
    # Essa fórmula vai ser ajustada conforme os dados da tabela.
    esperado = (inicio + fim) // 2

    return esperado

# Função para gerar a tabela de resultados
def gerar_tabela(n_max):
    """
    Gera a tabela baseada no valor de N e faz o cálculo esperado pelo teorema.
    """
    tabela = []

    for N in range(n_max + 1):
        inicio = 2 ** N
        fim = 2 ** (N + 1) - 1
        esperado = calcular_esperado_por_teorema(N)
        
        tabela.append([N, inicio, esperado, fim])
    
    return tabela

def imprimir_tabela(tabela):
    """
    Função para imprimir a tabela formatada.
    """
    print(f"{'N':<5}{'Inicio (2^N)':<15}{'Esperado pelo teorema':<25}{'Fim (2^(N+1))-1'}")
    for linha in tabela:
        print(f"{linha[0]:<5}{linha[1]:<15}{linha[2]:<25}{linha[3]}")

# Gerar a tabela até N = 9 (como o exemplo fornecido)
tabela = gerar_tabela(9)

# Imprimir a tabela gerada
imprimir_tabela(tabela)
