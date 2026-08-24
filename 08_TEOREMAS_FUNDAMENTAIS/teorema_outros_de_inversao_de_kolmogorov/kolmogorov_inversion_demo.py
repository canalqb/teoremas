import numpy as np
from scipy.integrate import quad

# Função característica da normal padrão
def phi_normal(t):
    return np.exp(-0.5 * t**2)

# Teorema de Inversão de Kolmogorov com limite variável T
def kolmogorov_cdf_approx(x, T):
    def integrand(t):
        if t == 0:
            return 0
        return np.real((np.exp(-1j * t * x) - 1) * phi_normal(t) / (1j * t))
    integral, _ = quad(integrand, -T, T, limit=100)
    return 0.5 - (1 / np.pi) * integral

# Valores de A e intervalo associado
A_values = list(range(0, 9))  # A = 0 a 8

x = 0  # ponto para calcular CDF (normal padrão: CDF(0) = 0.5)

print(f"{'2^A':>5} | {'Retorno Teorema':>16} | {'Intervalo':>12}")
print("-" * 40)

for A in A_values:
    T = 2**A
    retorno = kolmogorov_cdf_approx(x, T)
    intervalo = f"[{2**A}, {2**(A+1)-1}]"
    print(f"{2**A:5} | {retorno:16.10f} | {intervalo:12}")
