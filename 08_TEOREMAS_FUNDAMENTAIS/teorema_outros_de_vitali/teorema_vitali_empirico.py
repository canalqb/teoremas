def estimativa_empirica(N):
    if N == 0:
        return 1
    else:
        return (2 ** (N + 1)) - N - 2

def gerar_tabela_completa(limite_n=9):
    print(f"{'N':<3} | {'Estimativa Empírica':<20} | {'2^N':<8} | {'Mersenne (2^N - 1)':<18}")
    print("-" * 60)
    for N in range(limite_n + 1):
        estimado = estimativa_empirica(N)
        potencia = 2 ** N
        mersenne = 2 ** (N+1) - 1
        print(f"{N:<3} | {potencia:<8} | {estimado:<20} | {mersenne:<18}")

if __name__ == "__main__":
    gerar_tabela_completa()
