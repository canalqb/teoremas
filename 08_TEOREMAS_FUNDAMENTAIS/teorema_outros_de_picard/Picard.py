import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Gerar potências de 2 e Mersennes
n_values = np.arange(0, 11)
powers_of_two = 2 ** n_values
mersenne_numbers = powers_of_two - 1
distances = np.abs(powers_of_two - mersenne_numbers)

# Criar tabela
table = pd.DataFrame({
    'n': n_values,
    '2^n (Início)': powers_of_two,
    'Mersenne (2^n - 1) (Fim)': mersenne_numbers,
    'Distância': distances
})

# Exibir tabela
print("\nTabela de distâncias entre potências de 2 e seus Mersennes:\n")
print(table)

# Gráfico com curvas suaves (arcos horizontais)
plt.figure(figsize=(12, 6))

for i in range(len(n_values)):
    x0 = powers_of_two[i]
    x1 = mersenne_numbers[i]

    # Curva suave com arco parabólico (horizontal)
    t = np.linspace(0, 1, 100)
    x = (1 - t) * x0 + t * x1
    y = 4 * t * (1 - t) * 5  # curva parabólica para cima

    plt.plot(x, y, label=f'n={n_values[i]}')

# Configurações do gráfico
plt.title('Curvas entre 2^n e Mersenne (2^n - 1)')
plt.xlabel('Valor (x)')
plt.ylabel('Curvatura (visual)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
