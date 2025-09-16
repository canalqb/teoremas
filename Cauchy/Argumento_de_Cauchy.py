import numpy as np

def f(z, n):
    zeros = [2**k for k in range(n+1)]
    poles = [2**k - 1 for k in range(n+1)]
    
    numerator = 1
    denominator = 1
    
    for zero in zeros:
        numerator *= (z - zero)
    for pole in poles:
        denominator *= (z - pole)
    
    return numerator / denominator

def df(z, n, h=1e-6):
    # Derivada numérica por diferença central
    return (f(z + h, n) - f(z - h, n)) / (2*h)

def z_param(t, R=1, center=0):
    # Curva circular parametrizada
    return center + R * np.exp(1j * t)

def integrand(t, n, R):
    z = z_param(t, R)
    val = df(z, n) / f(z, n)
    dz_dt = 1j * z
    return val * dz_dt

def count_zeros_poles(n, R):
    zeros = [2**k for k in range(n+1)]
    poles = [2**k - 1 for k in range(n+1)]
    
    zeros_inside = sum(z <= R for z in zeros)
    poles_inside = sum(p <= R for p in poles)
    
    return zeros, poles, zeros_inside, poles_inside, zeros_inside - poles_inside

N = 10000
t_vals = np.linspace(0, 2*np.pi, N)

print("n | Raio R       | Zeros dentro | Polos dentro | Z - P (contagem) | Zeros           | Polos (Mersenne)          | Z-P (estimado)")
print("-"*120)

for n in range(11):
    R = 2**n + 0.5  # Raio para incluir até o zero 2^n
    
    zeros, poles, zeros_inside, poles_inside, diff = count_zeros_poles(n, R)
    
    integrand_vals = integrand(t_vals, n, R)
    integral = np.trapz(integrand_vals, t_vals)
    resultado = integral / (2j * np.pi)
    
    zeros_str = " ".join([f"2^{k}" for k in range(n+1)])
    poles_str = " ".join([f"2^{k}-1" for k in range(n+1)])
    
    print(f"{n:2d} | {R:<12.1f} | {zeros_inside:<12} | {poles_inside:<11} | {diff:<15} | {zeros_str:<15} | {poles_str:<25} | {resultado.real:.4f}")
