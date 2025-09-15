print(f"{'n':>2} | {'Área Superfície (A_n)':>20} | {'Área Esfera (A_n prime)':>20} | {'Curvatura K_n':>15}")
print("-" * 70)

for n in range(11):
    A_n = 2**n            # área da superfície (simplificada)
    A_n_prime = 2**(n/2)  # área da imagem na esfera (simulada)
    K_n = A_n_prime / A_n # curvatura aproximada
    print(f"{n:>2} | {A_n:>20,.0f} | {A_n_prime:>20,.2f} | {K_n:>15.6f}")
