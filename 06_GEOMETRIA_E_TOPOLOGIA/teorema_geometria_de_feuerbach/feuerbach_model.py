import numpy as np
import matplotlib.pyplot as plt

def midpoint(P, Q):
    return (P + Q) / 2

def foot_of_perpendicular(A, B, C):
    # Projeção do ponto A na linha BC
    BA = A - B
    BC = C - B
    t = np.dot(BA, BC) / np.dot(BC, BC)
    return B + t * BC

def circle_center_radius(A, B, C):
    # Centro e raio do círculo circunscrito ao triângulo ABC
    D = 2 * (A[0]*(B[1]-C[1]) + B[0]*(C[1]-A[1]) + C[0]*(A[1]-B[1]))
    Ux = ((np.linalg.norm(A)**2)*(B[1]-C[1]) + (np.linalg.norm(B)**2)*(C[1]-A[1]) + (np.linalg.norm(C)**2)*(A[1]-B[1])) / D
    Uy = ((np.linalg.norm(A)**2)*(C[0]-B[0]) + (np.linalg.norm(B)**2)*(A[0]-C[0]) + (np.linalg.norm(C)**2)*(B[0]-A[0])) / D
    center = np.array([Ux, Uy])
    radius = np.linalg.norm(center - A)
    return center, radius

def incenter(A, B, C):
    # Centro do círculo inscrito do triângulo
    a = np.linalg.norm(B - C)
    b = np.linalg.norm(A - C)
    c = np.linalg.norm(A - B)
    P = a + b + c
    x = (a*A[0] + b*B[0] + c*C[0]) / P
    y = (a*A[1] + b*B[1] + c*C[1]) / P
    center = np.array([x, y])
    # Raio do incírculo
    s = P / 2
    area = np.sqrt(s*(s - a)*(s - b)*(s - c))
    radius = area / s
    return center, radius

def nine_point_circle(A, B, C):
    # Ponto médio dos lados
    M_AB = midpoint(A, B)
    M_BC = midpoint(B, C)
    M_CA = midpoint(C, A)
    # Pés das alturas
    H_A = foot_of_perpendicular(A, B, C)
    H_B = foot_of_perpendicular(B, A, C)
    H_C = foot_of_perpendicular(C, A, B)
    # Ortocentro
    # Usar interseção das alturas
    # Altura de A é linha A-H_A, altura de B é B-H_B
    def line(p1, p2):
        A_ = p2[1] - p1[1]
        B_ = p1[0] - p2[0]
        C_ = A_*p1[0] + B_*p1[1]
        return A_, B_, C_

    A1, B1, C1 = line(A, H_A)
    A2, B2, C2 = line(B, H_B)
    D = A1*B2 - A2*B1
    if D == 0:
        ortho = np.array([np.nan, np.nan])  # Paralelas, triângulo degenerado
    else:
        x = (C1*B2 - C2*B1) / D
        y = (A1*C2 - A2*C1) / D
        ortho = np.array([x, y])

    # Pontos médios dos segmentos de vértices até ortocentro
    M_AO = midpoint(A, ortho)
    M_BO = midpoint(B, ortho)
    M_CO = midpoint(C, ortho)

    # Centro do círculo de nove pontos é o circuncentro do triângulo M_AB, M_BC, M_CA
    center, radius = circle_center_radius(M_AB, M_BC, M_CA)
    return center, radius, [M_AB, M_BC, M_CA, H_A, H_B, H_C, M_AO, M_BO, M_CO]

def plot_circle(ax, center, radius, color, label=None):
    circle = plt.Circle(center, radius, fill=False, color=color, lw=2, label=label)
    ax.add_patch(circle)

def modelar_teorema_feuerbach(n):
    # Definir triângulo com potências de 2
    A = np.array([0, 0])
    B = np.array([2**n, 0])
    C = np.array([0, 2**(n+1)])

    fig, ax = plt.subplots(figsize=(8,8))
    ax.set_aspect('equal', 'box')
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_title(f"Triângulo e círculos associados - n={n}")

    # Plotar triângulo
    tri_x = [A[0], B[0], C[0], A[0]]
    tri_y = [A[1], B[1], C[1], A[1]]
    ax.plot(tri_x, tri_y, 'k-', lw=2, label='Triângulo')

    # Círculo inscrito
    in_center, in_radius = incenter(A, B, C)
    plot_circle(ax, in_center, in_radius, 'orange', 'Círculo inscrito')

    # Círculo de nove pontos
    nine_center, nine_radius, nine_points = nine_point_circle(A, B, C)
    plot_circle(ax, nine_center, nine_radius, 'blue', 'Círculo de nove pontos')

    # Plotar pontos importantes
    pts = [A, B, C, in_center, nine_center] + nine_points
    labels = ['A', 'B', 'C', 'Incentro', '9-Pontos'] + [f'P{i+1}' for i in range(len(nine_points))]
    for p, l in zip(pts, labels):
        ax.plot(p[0], p[1], 'ro')
        ax.text(p[0]+0.05, p[1]+0.05, l)

    # Ajustar limites
    max_val = 2**(n+1) * 1.2
    ax.set_xlim(-1, max_val)
    ax.set_ylim(-1, max_val)

    ax.legend()
    plt.show()

# Testar para n de 0 a 3
for i in range(4):
    modelar_teorema_feuerbach(i)
