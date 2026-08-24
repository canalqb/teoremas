# tietze_intervals.py

def mersenne(n):
    """Número de Mersenne: 2^n - 1"""
    return 2**n - 1

def valor_teorema(n):
    """
    Para cada N, retornamos um valor dentro do intervalo [2^N, 2^(N+1)-1].
    Sem usar a coluna Esperado, tentamos gerar um valor baseado em:
    - 2^N (início)
    - mersenne(N+1) (fim)
    Como uma função simples que fica na metade entre início e fim.
    """
    inicio = 2**n
    fim = mersenne(n+1)
    # Valor no meio do intervalo, arredondado para inteiro
    valor = (inicio + fim) // 2
    return valor

def imprimir_tabela(max_n=9):
    print(f"{'N':<3} | {'Inicio (2^N)':<12} | {'Valor Teorema':<14} | {'Fim (2^(N+1))-1':<15}")
    print("-" * 55)
    for n in range(max_n + 1):
        inicio = 2**n
        fim = mersenne(n+1)
        valor = valor_teorema(n)
        print(f"{n:<3} | {inicio:<12} | {valor:<14} | {fim:<15}")

if __name__ == "__main__":
    imprimir_tabela()
