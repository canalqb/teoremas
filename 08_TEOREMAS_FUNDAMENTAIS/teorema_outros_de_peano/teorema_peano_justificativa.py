# nome do script: peano_justificativa.py

# Função para calcular a resposta esperada pelo teorema (aproximada)
def calcular_esperado(n):
    # O intervalo dado é [2^N, 2^(N+1) - 1]
    inicio = 2 ** n
    fim = (2 ** (n + 1)) - 1
    
    # A resposta esperada será um valor dentro desse intervalo.
    # Vamos aproximar o valor com a média do intervalo como uma heurística.
    esperado = (inicio + fim) // 2
    
    return inicio, esperado, fim

# Função principal para gerar a tabela de valores
def gerar_tabela():
    tabela = []
    for n in range(10):  # Para valores de N de 0 a 9
        inicio, esperado, fim = calcular_esperado(n)
        tabela.append([n, inicio, esperado, fim])
    
    return tabela

# Função para imprimir a tabela
def imprimir_tabela():
    tabela = gerar_tabela()
    
    # Cabeçalho da tabela
    print(f"{'N':<3} {'Inicio (2^N)':<15} {'Esperado pelo teorema':<25} {'Fim (2^(N+1))-1':<15}")
    
    # Imprimindo os valores da tabela
    for linha in tabela:
        n, inicio, esperado, fim = linha
        print(f"{n:<3} {inicio:<15} {esperado:<25} {fim:<15}")

# Chamando a função para imprimir a tabela
imprimir_tabela()
