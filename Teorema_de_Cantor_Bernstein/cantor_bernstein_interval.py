# cantor_bernstein_interval.py

def cantor_bernstein_estimate(N):
    inicio = 2 ** N
    fim = 2 ** (N + 1) - 1

    geo_mean = int((inicio * fim) ** 0.5)
    arit_mean = (inicio + fim) // 2  # só para comparação

    return inicio, geo_mean, arit_mean, fim


def gerar_tabela(max_n=10):
    print(f"{'N':<3} | {'Início':<10} | {'GeoMédia':<10} | {'AritMédia':<10} | {'Fim':<10}")
    print("-" * 55)
    for N in range(max_n):
        inicio, geo, arit, fim = cantor_bernstein_estimate(N)
        print(f"{N:<3} | {inicio:<10} | {geo:<10} | {arit:<10} | {fim:<10}")


if __name__ == "__main__":
    gerar_tabela()
