# teorema_lusternik_schnirelmann.py

def calcular_esperado_pelo_teorema(inicio, fim):
    """
    Função para aproximar o valor esperado pelo teorema.
    A ideia é retornar um valor que está dentro do intervalo (inicio, fim).
    Vamos assumir que o valor esperado é uma média ponderada entre o início e o fim.
    """
    return (inicio + fim) // 2

def gerar_tabela():
    """
    Função para gerar a tabela de valores de acordo com o padrão de crescimento dado:
    - Início = 2^N
    - Fim = 2^(N+1) - 1
    - Esperado pelo teorema = Aproximação dentro do intervalo [Início, Fim]
    """
    tabela = []
    
    for N in range(10):  # Vamos gerar para N de 0 a 9
        inicio = 2 ** N
        fim = (2 ** (N + 1)) - 1
        esperado = calcular_esperado_pelo_teorema(inicio, fim)
        tabela.append([N, inicio, esperado, fim])
    
    return tabela

# Gerar a tabela e imprimir os valores
tabela = gerar_tabela()

# Imprimir a tabela gerada
print(f"{'N':<3} {'Início (2^N)':<15} {'Esperado pelo Teorema':<20} {'Fim (2^(N+1))-1':<20}")
for linha in tabela:
    print(f"{linha[0]:<3} {linha[1]:<15} {linha[2]:<20} {linha[3]:<20}")
