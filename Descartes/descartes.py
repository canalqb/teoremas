import math

def mersenne(n):
    """Retorna o número de Mersenne M_n = 2^n - 1"""
    return 2**n - 1

def descartes(k1, k2, k3):
    """
    Aplica a fórmula de Descartes para encontrar as duas soluções possíveis de k4
    (curvatura do quarto círculo tangente a três círculos com curvaturas k1, k2, k3).
    """
    s = k1 + k2 + k3
    discriminante = 2 * (k1*k2 + k2*k3 + k3*k1)
    k4_pos = s + 2 * math.sqrt(discriminante)
    k4_neg = s - 2 * math.sqrt(discriminante)
    return k4_pos, k4_neg

# Lista de expoentes
n_values = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# Gerar potências de 2 e números de Mersenne
potencias_de_2 = [2**n for n in n_values]
mersennes = [mersenne(n) for n in n_values]

# Combinar em uma lista única de curvaturas intercalando potência e Mersenne
curvaturas = []
for p, m in zip(potencias_de_2, mersennes):
    curvaturas.append(p)
    curvaturas.append(m)

print("Curvaturas (potências de 2 e Mersennes intercaladas):")
print(curvaturas)
print("\nResultados usando o Teorema de Descartes:\n")

# Aplicar o Teorema de Descartes a cada grupo de 3 curvaturas consecutivas
for i in range(len(curvaturas) - 2):
    k1, k2, k3 = curvaturas[i], curvaturas[i+1], curvaturas[i+2]
    k4_1, k4_2 = descartes(k1, k2, k3)
    print(f"k1={k1}, k2={k2}, k3={k3} -> k4 = {k4_1:.4f} ou {k4_2:.4f}")
