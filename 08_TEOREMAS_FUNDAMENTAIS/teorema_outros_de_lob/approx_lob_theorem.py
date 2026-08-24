def inicio(N):
    return 2**N

def fim(N):
    return 2**(N+1) - 1

def esperado_aproximado(N):
    """
    Aproximação do valor esperado pelo teorema sem usar a coluna fornecida.
    Uma hipótese baseada na observação da tabela é:
    - Para N < 3, valor esperado = fim(N-1) + inicio(N)
    - Para N >= 3, uma aproximação usando uma combinação de potências e somas.

    Vamos tentar uma combinação de somas parciais:
    valor = inicio(N) + int(0.5 * (fim(N) - inicio(N)))
    """
    start = inicio(N)
    end = fim(N)
    # Média entre início e fim:
    approx = start + (end - start) // 2
    return approx

def print_tabela(max_N=9):
    print(f"{'N':>2} | {'Inicio (2^N)':>12} | {'Esperado aprox.':>15} | {'Fim (2^(N+1))-1':>15}")
    print("-"*55)
    for N in range(max_N+1):
        ini = inicio(N)
        fim_val = fim(N)
        exp_aprox = esperado_aproximado(N)
        print(f"{N:>2} | {ini:>12} | {exp_aprox:>15} | {fim_val:>15}")

if __name__ == "__main__":
    print_tabela()
