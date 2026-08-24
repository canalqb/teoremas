import math
import matplotlib.pyplot as plt

def graus(rad):
    return math.degrees(rad)

def lei_dos_cossenos(a, b, c):
    # Calcula os ângulos internos em graus
    A = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
    B = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
    C = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
    return graus(A), graus(B), graus(C)

def calcula_vertices(a, b, c):
    """
    Calcula as coordenadas dos vértices do triângulo no plano 2D.
    Assume:
    - Vértice A em (0, 0)
    - Vértice B em (c, 0) (base sobre o eixo x)
    - Vértice C calculado por coordenadas (x, y)
    """
    # A (0, 0)
    Ax, Ay = 0, 0
    # B (c, 0)
    Bx, By = c, 0

    # Usar Lei dos Cossenos para encontrar x e y do ponto C
    # Distância entre A e C é b
    # Distância entre B e C é a

    # x = (b² - a² + c²) / (2c)
    x = (b**2 - a**2 + c**2) / (2 * c)
    # y = sqrt(b² - x²)
    y = math.sqrt(b**2 - x**2)

    Cx, Cy = x, y

    return (Ax, Ay), (Bx, By), (Cx, Cy)

def plot_triangulo(vertices, angulos, lados):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Desempacotar os vértices
    A, B, C = vertices

    # Criar lista de pontos para plotar o polígono
    x_coords = [A[0], B[0], C[0], A[0]]
    y_coords = [A[1], B[1], C[1], A[1]]

    # Plotar triângulo
    ax.plot(x_coords, y_coords, 'b-', label='Triângulo')

    # Marcar vértices
    ax.plot(*A, 'ro')
    ax.plot(*B, 'ro')
    ax.plot(*C, 'ro')

    # Escrever nomes dos vértices
    ax.text(A[0] - 1, A[1] - 1, 'A')
    ax.text(B[0] + 1, B[1] - 1, 'B')
    ax.text(C[0], C[1] + 1, 'C')

    # Mostrar valores dos lados perto do lado correspondente
    def midpoint(p1, p2):
        return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

    mid_AB = midpoint(A, B)
    mid_BC = midpoint(B, C)
    mid_CA = midpoint(C, A)

    ax.text(mid_AB[0], mid_AB[1] - 1, f'{lados[2]:.1f}')  # lado c (AB)
    ax.text(mid_BC[0] + 0.5, mid_BC[1], f'{lados[0]:.1f}')  # lado a (BC)
    ax.text(mid_CA[0] - 1.5, mid_CA[1], f'{lados[1]:.1f}')  # lado b (CA)

    # Mostrar ângulos nos vértices
    ax.text(A[0] - 3, A[1], f'{angulos[0]:.1f}°')
    ax.text(B[0] + 1, B[1], f'{angulos[1]:.1f}°')
    ax.text(C[0], C[1] + 2, f'{angulos[2]:.1f}°')

    ax.set_title('Triângulo com lados e ângulos')
    ax.grid(True)
    plt.show()

def main():
    # Lados do triângulo (exemplo)
    lado_a = 64  # base
    lado_b = 48  # lado direito
    lado_c = 64  # lado esquerdo (exemplo, pode mudar)

    print(f"Lados do triângulo: a={lado_a}, b={lado_b}, c={lado_c}")

    # 1. Calcular ângulos internos
    angulo_A, angulo_B, angulo_C = lei_dos_cossenos(lado_a, lado_b, lado_c)
    print(f"Ângulos internos:")
    print(f"A = {angulo_A:.2f}°")
    print(f"B = {angulo_B:.2f}°")
    print(f"C = {angulo_C:.2f}°")

    # 2. Calcular os vértices no plano
    vertices = calcula_vertices(lado_a, lado_b, lado_c)

    # 3. Plotar triângulo
    plot_triangulo(vertices, (angulo_A, angulo_B, angulo_C), (lado_a, lado_b, lado_c))

if __name__ == "__main__":
    main()
