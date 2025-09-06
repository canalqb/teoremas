import math

# Função contínua usada para simular o Teorema do Ponto Fixo
def f(x):
    return math.cos(x) * 0.5 + 0.5

# Normaliza x no intervalo [2^N, 2^(N+1)-1] para [0, 1]
def normalize(x, N):
    start = 2 ** N
    end = 2 ** (N + 1) - 1
    if end == start:
        return 0.0  # evitar divisão por zero para N=0
    return (x - start) / (end - start)

def main():
    # Tabela dos pontos fixos encontrados empiricamente
    tabela = [
        (0, 1),
        (1, 3),
        (2, 7),
        (3, 8),
        (4, 21),
        (5, 49),
        (6, 76),
        (7, 224),
        (8, 467),
        (9, 514)
    ]

    # Cabeçalho da tabela formatada
    print(f"{'N':<2} | {'x':<5} | {'x_norm':<10} | {'f(x_norm)':<12} | {'|f - x|':<14} | {'x / 2^N':<10}")
    print("-" * 78)

    # Iteração sobre os dados da tabela
    for N, x in tabela:
        start = 2 ** N
        end = 2 ** (N + 1) - 1

        if end == start:
            print(f"{N:<2} | {x:<5} | Intervalo nulo — pulado")
            continue

        x_norm = normalize(x, N)
        fx = f(x_norm)
        diff = abs(fx - x_norm)
        x_over_pow2 = x / (2 ** N)

        # Impressão formatada dos resultados
        print(f"{N:<2} | {x:<5} | {x_norm:<10.6f} | {fx:<12.6f} | {diff:<14.6f} | {x_over_pow2:<10.6f}")

if __name__ == "__main__":
    main()
