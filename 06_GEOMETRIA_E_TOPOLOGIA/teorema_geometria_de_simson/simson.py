import numpy as np
import matplotlib.pyplot as plt

def distance(p1, p2):
    return np.linalg.norm(p1 - p2)

def perpendicular_projection(p, a, b):
    ap = p - a
    ab = b - a
    t = np.dot(ap, ab) / np.dot(ab, ab)
    proj = a + t * ab
    return proj

def circumcenter(a, b, c):
    mid_ab = (a + b) / 2
    mid_bc = (b + c) / 2
    perp_ab = np.array([-(b - a)[1], (b - a)[0]])
    perp_bc = np.array([-(c - b)[1], (c - b)[0]])
    
    A = np.array([perp_ab, -perp_bc]).T
    b_vec = mid_bc - mid_ab

    # Verifica se A é singular antes de resolver
    if np.linalg.matrix_rank(A) < 2:
        return None  # Circuncentro não definido (triângulo degenerado)

    t_s = np.linalg.solve(A, b_vec)
    center = mid_ab + t_s[0] * perp_ab
    return center


def law_of_cosines_angle(a, b, c):
    # ângulo oposto ao lado c, com lados a e b
    return np.arccos((a**2 + b**2 - c**2) / (2 * a * b))

for n in range(0, 11):
    AB = 2**n
    BC = 2**n - 1
    
    # Fixamos AC arbitrariamente para formar um triângulo válido
    AC = max(1, AB / 2)  # Só para garantir não ser zero
    
    # Posicionamos A em (0,0), B em (AB,0)
    A = np.array([0, 0])
    B = np.array([AB, 0])
    
    # Calcula a posição de C usando a lei dos cossenos:
    # lado AC = AC (fixo)
    # lado BC = BC (Mersenne)
    # lado AB = AB (base)
    # C estará em (x,y) tal que:
    # distance(B,C) = BC
    # distance(A,C) = AC
    
    # Vamos achar x,y de C:
    # Seja C = (x, y)
    # |C - A| = AC -> x^2 + y^2 = AC^2
    # |C - B| = BC -> (x - AB)^2 + y^2 = BC^2
    
    # Subtraindo as equações para eliminar y^2:
    # x^2 + y^2 = AC^2
    # (x - AB)^2 + y^2 = BC^2
    # => x^2 + y^2 - [(x - AB)^2 + y^2] = AC^2 - BC^2
    # => x^2 - (x - AB)^2 = AC^2 - BC^2
    # => x^2 - (x^2 - 2*AB*x + AB^2) = AC^2 - BC^2
    # => 2*AB*x - AB^2 = AC^2 - BC^2
    # => 2*AB*x = AC^2 - BC^2 + AB^2
    # => x = (AC^2 - BC^2 + AB^2) / (2*AB)
    
    x_C = (AC**2 - BC**2 + AB**2) / (2 * AB)
    y_C_sq = AC**2 - x_C**2
    if y_C_sq < 0:
        print(f"Para n={n}, não é possível formar um triângulo com esses lados.")
        continue
    y_C = np.sqrt(y_C_sq)
    C = np.array([x_C, y_C])
    
    # Circuncírculo
    O = circumcenter(A, B, C) 
    if O is None:
        print(f"n = {n}: Triângulo degenerado — pulando.")
        continue
    R = distance(O, A)
    
    # Escolhe um ângulo para o ponto P no circuncírculo (vamos variar com n)
    angle = np.deg2rad(30 + 10*n)  # varia de 30° a 130°
    P = O + R * np.array([np.cos(angle), np.sin(angle)])
    
    # Projeções ortogonais
    proj_AB = perpendicular_projection(P, A, B)
    proj_BC = perpendicular_projection(P, B, C)
    proj_CA = perpendicular_projection(P, C, A)
    
    # Plot
    plt.figure(figsize=(6,6))
    plt.axis('equal')
    plt.title(f"n={n}, AB=2^{n}={AB}, BC=2^{n}-1={BC}")
    
    # Triângulo
    plt.plot([A[0], B[0]], [A[1], B[1]], 'k-')
    plt.plot([B[0], C[0]], [B[1], C[1]], 'k-')
    plt.plot([C[0], A[0]], [C[1], A[1]], 'k-')
    
    # Circuncírculo
    circle = plt.Circle(O, R, color='b', fill=False, linestyle='dashed')
    plt.gca().add_artist(circle)
    
    # Pontos
    plt.plot(*A, 'ro', label='A')
    plt.plot(*B, 'ro', label='B')
    plt.plot(*C, 'ro', label='C')
    plt.plot(*P, 'go', label='P (circuncírculo)')
    plt.plot(*proj_AB, 'bo', label='Proj. AB')
    plt.plot(*proj_BC, 'bo', label='Proj. BC')
    plt.plot(*proj_CA, 'bo', label='Proj. CA')
    
    # Reta de Simson
    xs = np.array([proj_AB[0], proj_BC[0], proj_CA[0]])
    ys = np.array([proj_AB[1], proj_BC[1], proj_CA[1]])
    coef = np.polyfit(xs[:2], ys[:2], 1)
    x_line = np.linspace(min(xs)-1, max(xs)+1, 100)
    y_line = np.polyval(coef, x_line)
    plt.plot(x_line, y_line, 'm--', label='Reta de Simson')
    
    plt.legend()
    plt.grid(True)
    plt.show()
