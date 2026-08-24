# cantor_diagonal_simulation.py

from itertools import product

def generate_power_set(n):
    """Gera o conjunto das partes de um conjunto com n elementos"""
    elements = list(range(n))
    power_set = []
    for bits in product([0, 1], repeat=n):
        subset = tuple(elements[i] for i in range(n) if bits[i])
        power_set.append(subset)
    return power_set

def diagonal_subsets(n):
    """
    Simula subconjuntos únicos usando diagonalização.
    Não gera todos os 2^n subconjuntos, mas sim uma quantidade crescente
    que demonstra que há mais subconjuntos do que elementos.
    """
    power_set = generate_power_set(n)
    diagonal_set = set()

    for i in range(len(power_set)):
        # cria subconjunto com bit invertido na diagonal
        new_subset = list(power_set[i])
        if i in new_subset:
            new_subset.remove(i)
        else:
            new_subset.append(i)
        diagonal_set.add(tuple(sorted(new_subset)))

    return diagonal_set

def main():
    print(f"{'N':<3} | {'Inicio (2^N)':<13} | {'Diagonal Count':<15} | {'Fim (2^(N+1))-1'}")
    print("-" * 60)

    for N in range(10):
        start = 2 ** N
        end = (2 ** (N + 1)) - 1
        diagonal = diagonal_subsets(N)
        diagonal_count = len(diagonal)
        print(f"{N:<3} | {start:<13} | {diagonal_count:<15} | {end}")

if __name__ == "__main__":
    main()
