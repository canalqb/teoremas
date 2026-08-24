import numpy as np
import matplotlib.pyplot as plt

# Função f(z)
def f(z):
    return z**5 + 3*z + 1

# Função simples para encontrar raiz aproximada por bissecção em intervalo [a, b]
def find_root_bisection(f, a, b, tol=1e-5, max_iter=100):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        return None  # sem raiz garantida aqui
    
    for _ in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        if abs(fc) < tol:
            return c
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return (a + b) / 2

# Potências de 2 (positivas e negativas simples)
powers_of_two = np.array([-8, -4, -2, -1, -0.5, -0.25, 0.25, 0.5, 1, 2, 4, 8])

# Primos para gerar números de Mersenne (usando primos pequenos)
primes = [2, 3, 5, 7, 11, 13, 17, 19]

# Calculando Mersennes correspondentes
mersennes = np.array([2**p - 1 for p in primes])

# Filtrando mersennes dentro do intervalo de potências de 2
mersennes_filtered = mersennes[(mersennes >= -8) & (mersennes <= 8)]

# Combinar e ordenar pontos
combined_points = np.sort(np.concatenate((powers_of_two, mersennes_filtered)))

# Calcular f(z) nos pontos
f_combined = f(combined_points)

# Encontrar intervalos com mudança de sinal para encontrar raízes aproximadas
roots = []
for i in range(len(combined_points) - 1):
    a, b = combined_points[i], combined_points[i+1]
    if f(a) * f(b) < 0:  # sinal muda -> raiz entre a e b
        root = find_root_bisection(f, a, b)
        if root is not None:
            roots.append(root)

# Imprimir tabela original com tipo
print("    z     |  f(z) = z^5 + 3z + 1")
print("-------------------------------")
for z, val in zip(combined_points, f_combined):
    tipo = "Potência de 2" if z in powers_of_two else "Mersenne"
    print(f"{z:8.3f} | {val:14.4f}  ({tipo})")

# Imprimir as raízes aproximadas encontradas
print("\nRaízes aproximadas encontradas entre os pontos:")
for r in roots:
    print(f"{r:.5f} -> f(z) = {f(r):.5e}")

# Plot contínuo para visualização suave
z_continuous = np.linspace(-9, 9, 500)
f_continuous = f(z_continuous)

plt.figure(figsize=(10,6))
plt.plot(z_continuous, f_continuous, label=r'$f(z) = z^5 + 3z + 1$', color='blue')

# Pontos potências de 2 (vermelho)
plt.scatter(powers_of_two, f(powers_of_two), color='red', label='Potências de 2', zorder=5)
for x, y in zip(powers_of_two, f(powers_of_two)):
    plt.text(x, y, str(int(round(x))), color='red', fontsize=9, ha='right', va='bottom')

# Pontos Mersenne (verde)
plt.scatter(mersennes_filtered, f(mersennes_filtered), color='green', label='Números de Mersenne', zorder=5)
for x, y in zip(mersennes_filtered, f(mersennes_filtered)):
    plt.text(x, y, str(int(round(x))), color='green', fontsize=9, ha='left', va='bottom')

# Pontos das raízes (preto)
plt.scatter(roots, f(np.array(roots)), color='black', label='Raízes aproximadas', zorder=10, s=80, marker='X')
for x, y in zip(roots, f(np.array(roots))):
    plt.text(x, y, str(int(round(x))), color='black', fontsize=10, ha='center', va='top')

plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

plt.title("Função $f(z) = z^5 + 3z + 1$ com legendas inteiras nos pontos")
plt.xlabel("z (real)")
plt.ylabel("f(z)")
plt.grid(True)
plt.legend()
plt.show()
