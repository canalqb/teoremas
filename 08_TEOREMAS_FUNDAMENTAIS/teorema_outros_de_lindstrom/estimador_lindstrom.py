# estimador_lindstrom.py

from math import comb

def estimativa_lindstrom(N):
    """
    Estima o valor baseado no Teorema de Lindström.
    Usamos uma soma ponderada de combinações para simular subconjuntos distinguíveis.
    """
    total = 0
    for k in range(N + 1):
        # O peso (N - k + 1) simula a 'distinguibilidade'
        peso = N - k + 1
        total += comb(N, k) * peso
    return total // (N + 1)  # Ajuste por normalização empírica


def gerar_tabela(max_n=9):
    print(f"{'N':<2} | {'Inicio (2^N)':<13} | {'Estimado':<10} | {'Fim (2^(N+1))-1':<16}")
    print("-" * 55)
    for N in range(max_n + 1):
        inicio = 2 ** N
        fim = 2 ** (N + 1) - 1
        estimado = estimativa_lindstrom(N)
        print(f"{N:<2} | {inicio:<13} | {estimado:<10} | {fim:<16}")


if __name__ == "__main__":
    gerar_tabela()
