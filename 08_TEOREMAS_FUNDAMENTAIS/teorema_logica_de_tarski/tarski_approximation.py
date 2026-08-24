# tarski_approximation.py

def tarski_expected(N):
    """
    Aproxima um valor esperado pelo teorema dentro do intervalo [2^N, 2^{N+1} - 1].
    A função tenta modelar um crescimento que é maior que 2^N, mas menor que 2^{N+1} - 1,
    sem usar diretamente a coluna 'Esperado pelo teorema'.
    """

    start = 2 ** N
    end = 2 ** (N + 1) - 1

    if N == 0:
        return start  # base trivial

    # Aproximação baseada em uma média ponderada entre start e end
    # A ponderação decresce conforme N aumenta, aproximando mais do limite superior lentamente
    weight = (N / (N + 2))  # varia entre 0 (N=0) até próximo de 1 conforme N cresce
    approx = int(start + weight * (end - start))

    return approx

def main():
    print(f"{'N':<3} | {'Início (2^N)':<12} | {'Aproximação':<12} | {'Fim (2^(N+1))-1':<15}")
    print("-" * 50)
    for N in range(10):
        start = 2 ** N
        end = 2 ** (N + 1) - 1
        approx = tarski_expected(N)
        print(f"{N:<3} | {start:<12} | {approx:<12} | {end:<15}")

if __name__ == "__main__":
    main()
