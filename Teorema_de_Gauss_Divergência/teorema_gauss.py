# teorema_gauss.py

import numpy as np

def calcular_teorema_gauss(n):
    """
    Função para calcular o valor esperado segundo o teorema de Gauss, baseado na tabela fornecida.
    A fórmula usada para a aproximação será uma soma entre 2^N e uma constante ajustada.

    """
    inicio = 2 ** n
    fim = 2 ** (n + 1) - 1
    
    # Aqui, aplicamos uma fórmula aproximada para o esperado, baseada na forma como os valores aumentam.
    # Suponhamos que a constante de ajuste seja algo próximo da média do intervalo.
    constante_ajuste = (inicio + fim) / 2
    esperado = constante_ajuste
    return inicio, esperado, fim

def gerar_tabela():
    """
    Função que gera a tabela completa com os valores para 0 <= N <= 9.
    """
    tabela = []
    for n in range(10):  # Considerando N de 0 a 9
        inicio, esperado, fim = calcular_teorema_gauss(n)
        tabela.append([n, inicio, esperado, fim])
    return tabela

def imprimir_tabela(tabela):
    """
    Função que imprime a tabela gerada.
    """
    print(" N  | Início (2^N) | Esperado pelo Teorema | Fim (2^(N+1)) - 1 ")
    print("------------------------------------------------------------")
    for linha in tabela:
        print(f" {linha[0]:<2} | {linha[1]:<12} | {linha[2]:<19} | {linha[3]:<18} ")

if __name__ == "__main__":
    tabela = gerar_tabela()
    imprimir_tabela(tabela)
