# lefschetz_power_estimate.py 

import math

def calcular_numero_lefschetz_estimado(n):
    """
    Gera uma estimativa empírica para o número de Lefschetz baseado em n,
    restringida ao intervalo [2^n, 2^{n+1} - 1]
    """
    inicio = 2 ** n
    fim = (2 ** (n + 1)) - 1

    if n == 0:
        return 1
    elif n == 1:
        return 3
    else:
        # Estimativa empírica: simula crescimento sub-exponencial
        estimado = round((2 ** n) * math.log2(n + 1) + n ** 1.5)
        return min(max(estimado, inicio), fim)

def gerar_tabela_lefschetz(max_n=9):
    print(f"{'N':<2} | {'2^N (Início)':<14} | {'Mersenne (2^N - 1)':<21} | {'L(f) Estimado':<16} | {'Intervalo'}")
    print("-" * 80)

    for n in range(max_n + 1):
        inicio = 2 ** n
        fim = (2 ** (n + 1)) - 1
        mersenne = 2 ** n - 1
        lefschetz_estimado = calcular_numero_lefschetz_estimado(n)

        print(f"{n:<2} | {inicio:<14} | {mersenne:<21} | {lefschetz_estimado:<16} | [{inicio}, {fim}]")

if __name__ == "__main__":
    gerar_tabela_lefschetz()
