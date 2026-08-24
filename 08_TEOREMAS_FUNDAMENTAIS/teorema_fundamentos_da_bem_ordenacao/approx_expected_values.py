# approx_expected_values.py

def approx_expected_values(max_n=9):
    print(f"{'N':>2} | {'Início (2^N)':>12} | {'Fim (2^(N+1))-1':>16} | {'Tamanho':>7} | {'Soma':>10} | {'Média':>8}")
    print("-" * 70)

    for N in range(max_n + 1):
        inicio = 2 ** N
        fim = (2 ** (N + 1)) - 1
        tamanho = fim - inicio + 1  # deve ser 2^N
        # Soma dos números do intervalo: soma dos inteiros de inicio a fim
        # Fórmula da soma de PA: S = n*(a1 + an)/2
        soma = tamanho * (inicio + fim) // 2
        media = soma / tamanho

        print(f"{N:2} | {inicio:12} | {fim:16} | {tamanho:7} | {soma:10} | {media:8.2f}")

if __name__ == "__main__":
    approx_expected_values()
