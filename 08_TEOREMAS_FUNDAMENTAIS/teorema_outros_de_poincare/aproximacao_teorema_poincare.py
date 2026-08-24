# aproximacao_teorema_poincare.py

def aproximar_valor(N):
    """
    Aproxima um valor dentro do intervalo [2^N, 2^(N+1)-1]
    baseado num crescimento não-linear simples,
    sem usar o valor esperado da tabela.
    """
    inicio = 2**N
    fim = 2**(N+1) - 1
    
    # Exemplo de aproximação: vamos usar uma função quadrática ajustada
    # para crescer entre início e fim, algo como:
    # valor = inicio + (fim - inicio) * (N / 10)^2, limitado ao intervalo.
    # O denominador 10 é arbitrário para ajustar o crescimento.
    
    fator = (N / 10)**2
    valor = inicio + (fim - inicio) * fator
    
    # Limitar valor ao intervalo [inicio, fim]
    if valor < inicio:
        valor = inicio
    if valor > fim:
        valor = fim
    
    return int(round(valor))

def gerar_tabela(max_N=9):
    print(f"{'N':>2} | {'Início (2^N)':>12} | {'Aproximado':>11} | {'Fim (2^(N+1)-1)':>15}")
    print("-" * 50)
    for N in range(max_N + 1):
        inicio = 2**N
        fim = 2**(N+1) - 1
        aprox = aproximar_valor(N)
        print(f"{N:2d} | {inicio:12d} | {aprox:11d} | {fim:15d}")

if __name__ == "__main__":
    gerar_tabela()
