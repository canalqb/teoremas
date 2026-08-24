# nome do script: teorema_whitehead.py

import pandas as pd

# Função que calcula os valores de "Início" (2^N) e "Fim" (2^(N+1)-1)
def calcular_intervalos(n):
    inicio = 2 ** n
    fim = 2 ** (n + 1) - 1
    return inicio, fim

# Teorema - Aproximação para calcular o valor esperado
# Vamos assumir que o teorema define uma aproximação dentro do intervalo (Início, Fim)
def teorema_aproximacao(inicio, fim):
    # O teorema hipotético pode ser uma função que ajusta os valores de acordo com algum critério.
    # Uma abordagem simples seria a média ponderada entre o início e o fim.
    
    # Aproximação com base em uma fórmula que tenta "aplicar o teorema"
    # Por exemplo, ajustamos a média com um fator dependente do tamanho do intervalo
    intervalo = fim - inicio + 1
    fator_ajuste = (intervalo / 2)  # fator de ajuste hipotético
    
    # Uma forma de ajustarmos pode ser:
    esperado = (inicio + fim) // 2 + fator_ajuste // 4
    return esperado

# Função para gerar e preencher a tabela
def gerar_tabela():
    tabela = []
    
    for n in range(10):  # Para N de 0 a 9
        inicio, fim = calcular_intervalos(n)
        tabela.append([n, inicio, None, fim])  # A coluna "Esperado pelo Teorema" será calculada depois
    
    return tabela

# Função para aplicar o teorema e preencher os valores esperados
def preencher_esperado(tabela):
    for i, linha in enumerate(tabela):
        n = linha[0]
        inicio = linha[1]
        fim = linha[3]

        # Aplica o teorema para calcular o valor esperado
        esperado = teorema_aproximacao(inicio, fim)
        tabela[i][2] = esperado

    return tabela

# Função para imprimir a tabela
def imprimir_tabela(tabela):
    df = pd.DataFrame(tabela, columns=["N", "Início (2^N)", "Esperado pelo Teorema", "Fim (2^(N+1))-1"])
    print(df)

# Execução
tabela = gerar_tabela()  # Cria a tabela com intervalos
tabela = preencher_esperado(tabela)  # Aplica o teorema e preenche os valores esperados
imprimir_tabela(tabela)  # Exibe a tabela final
