# mersenne_teorema.py

def mersenne(n):
    return 2**n - 1

def soma_mersenne_ate(n):
    # Soma dos números de Mersenne de 1 até n
    return sum(mersenne(k) for k in range(1, n+1))

def estimativa(n):
    """
    Estimativa que tenta aproximar o valor esperado
    baseado em potências de 2 e números de Mersenne.
    
    Aqui usamos:
    estimativa = 2^n + soma dos mersennes até n-1 dividido por um fator
    para tentar chegar próximo do valor esperado.
    """
    if n == 0:
        return 1
    return 2**n + soma_mersenne_ate(n-1) // 2

def gerar_tabela(limit_n=9):
    tabela = []
    for n in range(limit_n + 1):
        inicio = 2**n
        fim = 2**(n+1) - 1
        est = estimativa(n)
        tabela.append((n, inicio, fim, est))
    return tabela

def imprimir_tabela(tabela):
    print(f"{'N':<3} | {'Início (2^N)':<12} | {'Fim (2^(N+1)-1)':<15} | {'Estimativa':<10}")
    print("-"*55)
    for n, inicio, fim, est in tabela:
        print(f"{n:<3} | {inicio:<12} | {fim:<15} | {est:<10}")

if __name__ == "__main__":
    tabela = gerar_tabela(9)
    imprimir_tabela(tabela)
