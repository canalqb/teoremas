import numpy as np
import matplotlib.pyplot as plt

# Potências de 2
powers_of_two = [2**n for n in range(1, 11)]
# Mersennes
mersennes = [2**n - 1 for n in range(1, 11)]

# Função analítica para testar
def f(z):
    return z**2

print(f"{'Intervalo':<20} {'|f(start)|':>10} {'|f(end)|':>10} {'Máx |f(z)|':>12} {'Ponto máx':>10}")
print("-"*65)

plt.figure(figsize=(14, 7))
colors = plt.cm.tab10(np.linspace(0, 1, len(powers_of_two)-1))

for i in range(len(powers_of_two)-1):
    start = powers_of_two[i]
    end = mersennes[i+1]

    z_values = np.linspace(start, end, 500)
    f_values = np.abs(f(z_values))

    max_value = np.max(f_values)
    max_index = np.argmax(f_values)
    max_point = z_values[max_index]

    val_start = abs(f(start))
    val_end = abs(f(end))

    print(f"[{start:>4}, {end:<4}] {val_start:10.2f} {val_end:10.2f} {max_value:12.2f} {max_point:10.2f}")

    # Plot da curva do módulo
    plt.plot(z_values, f_values, color=colors[i], label=f'Intervalo [{start}, {end}]')

    # Marca bordas (fronteiras)
    plt.scatter([start, end], [val_start, val_end], color=colors[i], edgecolor='black', s=80, zorder=5)
    plt.text(start, val_start, f"{val_start:.1f}", fontsize=8, ha='right', va='bottom')
    plt.text(end, val_end, f"{val_end:.1f}", fontsize=8, ha='left', va='bottom')

    # Marca máximo interno (se não for borda)
    if max_point != start and max_point != end:
        plt.scatter([max_point], [max_value], color='red', s=100, marker='*', label=f'Máx interno {i+1}')
        plt.text(max_point, max_value, f"{max_value:.1f}", fontsize=9, ha='center', va='bottom', color='red')

plt.title("Módulo de f(z) = z² nos intervalos formados por potências de 2 e Mersennes")
plt.xlabel("z (real)")
plt.ylabel("|f(z)|")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
