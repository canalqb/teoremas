import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

R = 1  # raio do círculo unitário
n_vals = range(0, 11)

def z(t):
    return R * np.exp(1j * t)

def dz_dt(t):
    return 1j * R * np.exp(1j * t)

errors = []
a_vals = []
integrals = []
expected_vals = []

for n in n_vals:
    a = 2**n - 1  # número de Mersenne para n
    a_vals.append(a)
    
    def f(z):
        return z**n

    def integrand(t):
        return (f(z(t)) / (z(t) - a)) * dz_dt(t)

    real_part = quad(lambda t: np.real(integrand(t)), 0, 2*np.pi)[0]
    imag_part = quad(lambda t: np.imag(integrand(t)), 0, 2*np.pi)[0]
    integral = real_part + 1j * imag_part
    integrals.append(integral)

    # Aplicação do Teorema de Cauchy:
    # Se |a| < R, valor esperado = 2*pi*i*f(a)
    # Senão, valor esperado = 0 (integral sobre curva não envolvendo singularidade)
    if abs(a) < R:
        expected = 2 * np.pi * 1j * f(a)
    else:
        expected = 0

    expected_vals.append(expected)

    error = abs(integral - expected)
    errors.append(error)

    print(f"n={n:2d}, a={a:6.1f}, |a|={'{:.2f}'.format(abs(a))}, Integral={integral:.5f}, Esperado={expected:.5f}, Erro={error:.2e}")

# Plotando erros e localização de a
fig, ax1 = plt.subplots(figsize=(10,6))

color = 'tab:blue'
ax1.set_xlabel('n')
ax1.set_ylabel('Erro absoluto (log)', color=color)
ax1.plot(n_vals, errors, 'o-', color=color, label='Erro absoluto')
ax1.set_yscale('log')
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True, which='both', ls='--', lw=0.5)

ax2 = ax1.twinx()  # eixo secundário para a
color = 'tab:red'
ax2.set_ylabel('|a| = |Mersenne|', color=color)
ax2.plot(n_vals, [abs(val) for val in a_vals], 's--', color=color, label='|a| (Mersenne)')
ax2.axhline(y=R, color='green', linestyle=':', label='Raio do círculo (R=1)')
ax2.tick_params(axis='y', labelcolor=color)

fig.suptitle('Aplicação do Teorema de Cauchy com pontos a = números de Mersenne (2^n - 1)')
fig.legend(loc='upper left', bbox_to_anchor=(0.15,0.85))

plt.show()
