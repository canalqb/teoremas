import csv
import json
from math import gcd
import matplotlib.pyplot as plt

def gerar_ternas_pitagoricas(c_min, c_max, incluir_nao_primitivas=False):
    ternas = []
    m = 1
    while True:
        m2 = m * m
        if m2 > c_max:
            break
        for n in range(1, m):
            if (m - n) % 2 == 1 and gcd(m, n) == 1:  # ternas primitivas
                x = m2 - n * n
                y = 2 * m * n
                z = m2 + n * n
                if c_min < z < c_max:
                    if incluir_nao_primitivas:
                        k = 1
                        while k * z < c_max:
                            ternas.append((k * x, k * y, k * z))
                            k += 1
                    else:
                        ternas.append((x, y, z))
        m += 1
    return ternas

def exportar_csv(arquivo, dados):
    with open(arquivo, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Intervalo", "a", "b", "c"])
        for intervalo, ternas in dados.items():
            for x, y, z in ternas:
                writer.writerow([intervalo, x, y, z])

def exportar_json(arquivo, dados):
    with open(arquivo, "w") as f:
        json.dump(dados, f, indent=4)

def plotar_ternas(dados):
    xs, ys = [], []
    for ternas in dados.values():
        for x, y, _ in ternas:
            xs.append(x)
            ys.append(y)

    plt.figure(figsize=(8, 8))
    plt.scatter(xs, ys, s=10, c='blue', alpha=0.6)
    plt.title("Ternas Pitagóricas (a, b)")
    plt.xlabel("a")
    plt.ylabel("b")
    plt.grid(True)
    plt.axis("equal")
    plt.show()

def main():
    incluir_nao_primitivas = True  # Mude para False para só primitivas
    resultados = {}

    for c in range(0, 10):
        c_min = 2 ** c
        c_max = 2 ** (c + 1) - 1
        intervalo_label = f"{c_min}–{c_max}"
        ternas_encontradas = gerar_ternas_pitagoricas(c_min, c_max, incluir_nao_primitivas)
        resultados[intervalo_label] = ternas_encontradas

        for x, y, z in ternas_encontradas:
            print(f"{intervalo_label} -> a = {x}, b = {y}, c = {z}")

    # Exportar arquivos
    exportar_csv("ternas_pitagoricas.csv", resultados)
    exportar_json("ternas_pitagoricas.json", resultados)

    # Gerar gráfico
    plotar_ternas(resultados)

if __name__ == "__main__":
    main()
