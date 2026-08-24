# teorema_completude_godel.py

import random

# Função para gerar valor aleatório dentro do intervalo definido pelo teorema
def gerar_valor_aleatorio(n):
    inicio = 2 ** n
    fim = (2 ** (n + 1)) - 1
    return random.randint(inicio, fim)

# Gerar a tabela de valores
def gerar_tabela():
    tabela = []
    for n in range(10):  # Para N de 0 a 9
        inicio = 2 ** n
        fim = (2 ** (n + 1)) - 1
        esperado = gerar_valor_aleatorio(n)
        tabela.append([n, inicio, esperado, fim])
    return tabela

# Função para imprimir a tabela de forma legível
def imprimir_tabela(tabela):
    print("Tabela de Valores Gerados:")
    print("N  Início (2^N)      Esperado pelo Teorema        Fim (2^(N+1)) - 1")
    for linha in tabela:
        print(f"{linha[0]:<2}  {linha[1]:<16}  {linha[2]:<24}  {linha[3]:<15}")

# Gerar a tabela e imprimi-la
tabela = gerar_tabela()
imprimir_tabela(tabela)
