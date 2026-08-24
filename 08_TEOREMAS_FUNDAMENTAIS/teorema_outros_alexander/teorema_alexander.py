# teorema_alexander.py

def mersenne_number(k):
    """Retorna o número de Mersenne 2^k - 1"""
    return 2**k - 1

def valor_esperado(N):
    """
    Calcula um valor aproximado esperado pelo teorema usando
    a soma dos números de Mersenne até N.
    """
    # Soma dos números de Mersenne até N
    soma = 0
    for k in range(N+1):
        soma += mersenne_number(k)
    return soma

def gerar_tabela(N_max):
    print(f"{'N':>2} | {'Inicio (2^N)':>12} | {'Esperado pelo Teorema':>22} | {'Fim (2^(N+1)-1)':>18}")
    print("-" * 65)
    for N in range(N_max + 1):
        inicio = 2**N
        fim = 2**(N+1) - 1
        esperado = valor_esperado(N)
        print(f"{N:2d} | {inicio:12d} | {esperado:22d} | {fim:18d}")

if __name__ == "__main__":
    N_max = 9
    gerar_tabela(N_max)
