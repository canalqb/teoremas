import numpy as np
import matplotlib.pyplot as plt

def simulate_brownian_motion(T=1.0, N=2048, n_paths=10):
    """
    Simula trajetórias do movimento browniano em [0, T] com N passos e n_paths trajetórias.
    """
    dt = T / N
    t = np.linspace(0, T, N + 1)
    dB = np.sqrt(dt) * np.random.randn(n_paths, N)
    B = np.cumsum(dB, axis=1)
    B = np.hstack((np.zeros((n_paths, 1)), B))  # B(0) = 0 para todas as trajetórias
    return t, B

def plot_brownian_paths(t, paths):
    """
    Plota as trajetórias simuladas do movimento browniano.
    """
    plt.figure(figsize=(10, 6))
    for i in range(paths.shape[0]):
        plt.plot(t, paths[i], label=f'Trajetória {i + 1}')
    plt.title("Trajetórias Simuladas do Movimento Browniano")
    plt.xlabel("Tempo")
    plt.ylabel("B(t)")
    plt.legend()
    plt.grid(True)
    plt.show()

def kolmogorov_intervals_analysis(t, paths, alpha=2, max_n=10):
    """
    Analisa os incrementos |X_t - X_s|^alpha para intervalos [2^n, 2^{n+1}-1] em número de passos,
    imprime os resultados e seleciona um ponto médio (interconexão) para cada intervalo.
    """
    N = len(t) - 1
    n_paths = paths.shape[0]

    print("Análise dos incrementos para intervalos [2^n, 2^{n+1} - 1] (em número de passos):\n")

    interconnection_points = []

    for n in range(max_n + 1):
        start = 2 ** n
        expected_end = (2 ** (n + 1)) - 1

        if start > N:
            print(f"n={n:2d} | Intervalo inicia além do tamanho dos dados (start={start} > N={N}), pulando...")
            break

        end = expected_end if expected_end <= N else N

        if end < expected_end:
            print(f"n={n:2d} | Intervalo esperado [{start}, {expected_end}] truncado para [{start}, {end}] devido ao tamanho dos dados.")

        increments_list = []

        for delta in range(start, end + 1):
            increments = np.abs(paths[:, delta:] - paths[:, :-delta]) ** alpha
            mean_increment = increments.mean()
            increments_list.append(mean_increment)

        interval_mean = np.mean(increments_list)

        inter_point = (start + end) // 2
        interconnection_points.append(inter_point)

        print(f"n={n:2d} | Intervalo passos [{start:4d}, {end:4d}] | Ponto interconexão: {inter_point:4d} | Média E[|X_t - X_s|^{alpha}] = {interval_mean:.6e}")

    # Plot log-log geral para todos incrementos
    diffs = []
    time_diffs = []
    for i in range(N + 1):
        for j in range(i + 1, N + 1):
            increment_vals = np.abs(paths[:, j] - paths[:, i]) ** alpha
            diffs.append(np.mean(increment_vals))
            time_diffs.append(t[j] - t[i])
    diffs = np.array(diffs)
    time_diffs = np.array(time_diffs)

    plt.figure(figsize=(8, 5))
    plt.scatter(time_diffs, diffs, s=5, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel(r'$|t - s|$ (escala logarítmica)')
    plt.ylabel(r'$\mathbb{E}[|X_t - X_s|^\alpha]$ (escala logarítmica)')
    plt.title(f'Condição Empírica do Teorema de Kolmogorov (alpha={alpha})')
    plt.grid(True, which='both', ls='--')
    plt.show()

    return interconnection_points


if __name__ == "__main__":
    T = 1.0
    N = 2048  # Passos para cobrir até n=10 sem truncar intervalos
    n_paths = 10
    alpha = 2

    # Simular movimento browniano
    t, paths = simulate_brownian_motion(T, N, n_paths)

    # Plotar trajetórias simuladas
    plot_brownian_paths(t, paths)

    # Analisar incrementos e imprimir resultados com pontos de interconexão
    pontos = kolmogorov_intervals_analysis(t, paths, alpha=alpha, max_n=10)
    print("\nPontos de interconexão escolhidos para cada intervalo:", pontos)
