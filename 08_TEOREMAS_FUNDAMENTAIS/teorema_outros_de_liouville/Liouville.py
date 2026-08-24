import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Funções inteiras
def f1(z): return np.full_like(z, 5, dtype=np.float64)    # Constante
def f2(z): return z**2 + 3*z + 2                          # Polinomial
def f3(z): return np.exp(z)                               # Exponencial

# Valores de n
n = np.arange(0, 11)

# Valores de z para avaliação
z1 = 2**n                  # 2^n
z2 = 2**(n+1) - 1          # 2^(n+1) - 1

# Avaliação das funções nas duas sequências de z
vals_f1_z1 = f1(z1)
vals_f1_z2 = f1(z2)

vals_f2_z1 = f2(z1)
vals_f2_z2 = f2(z2)

vals_f3_z1 = f3(z1)
vals_f3_z2 = f3(z2)

# Criando uma tabela para mostrar os valores
data = {
    "n": n,
    "z = 2^n": z1,
    "f1(2^n)": vals_f1_z1,
    "f2(2^n)": vals_f2_z1,
    "f3(2^n)": vals_f3_z1,
    "z = 2^(n+1)-1": z2,
    "f1(2^(n+1)-1)": vals_f1_z2,
    "f2(2^(n+1)-1)": vals_f2_z2,
    "f3(2^(n+1)-1)": vals_f3_z2,
}

df = pd.DataFrame(data)

# Imprimindo a tabela formatada
pd.set_option('display.float_format', '{:.3e}'.format)
print(df)

# Plot único com todas as linhas cruzadas
plt.figure(figsize=(10, 6))

plt.plot(n, vals_f1_z1, 'o-', label='f1(z) em 2^n')
plt.plot(n, vals_f1_z2, 'o--', label='f1(z) em 2^(n+1)-1')

plt.plot(n, vals_f2_z1, 's-', label='f2(z) em 2^n')
plt.plot(n, vals_f2_z2, 's--', label='f2(z) em 2^(n+1)-1')

plt.plot(n, vals_f3_z1, '^-', label='f3(z) em 2^n')
plt.plot(n, vals_f3_z2, '^--', label='f3(z) em 2^(n+1)-1')

plt.yscale('log')  # escala logarítmica para enxergar melhor f3
plt.xlabel('n')
plt.ylabel('Valor da função')
plt.title('Avaliação das funções f1, f2 e f3 em 2^n e 2^(n+1)-1')
plt.legend()
plt.grid(True)
plt.show()
