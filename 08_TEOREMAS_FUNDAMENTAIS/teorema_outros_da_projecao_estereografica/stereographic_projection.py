import numpy as np

def stereographic_projection(P, N, S):
    """
    Projeta o ponto P da esfera na reta que passa por N (ponto norte)
    até o plano tangente na esfera no ponto sul S.

    P, N, S: numpy arrays com coordenadas 3D
    Retorna o ponto projetado no plano tangente (3D).
    """

    # Vetor normal do plano tangente no ponto S (normal é S - centro)
    # Assumindo esfera centrada na origem
    normal = S

    # Parametrização da reta
    # L(t) = N + t*(P - N)

    numerator = np.dot(normal, (S - N))
    denominator = np.dot(normal, (P - N))

    if denominator == 0:
        # Reta paralela ao plano, sem interseção
        return None

    t = numerator / denominator

    # Ponto de interseção
    intersection = N + t * (P - N)

    return intersection

def generate_points_on_sphere(R, num_points=100):
    """
    Gera pontos aproximadamente uniformes na esfera de raio R.
    """
    points = []
    for _ in range(num_points):
        # Gerar ponto aleatório na esfera
        vec = np.random.normal(size=3)
        vec /= np.linalg.norm(vec)
        points.append(R * vec)
    return points

def main():
    for n in range(11):
        R = 2**n
        N = np.array([0, 0, 2**n])
        S = np.array([0, 0, 2**(n+1) - 1])

        print(f"n={n}, R={R}, Norte={N}, Sul={S}")

        points = generate_points_on_sphere(R, 5)

        for i, P in enumerate(points):
            proj = stereographic_projection(P, N, S)
            print(f"Ponto {i}: Original {P}, Projeção {proj}")
        print("----")

if __name__ == "__main__":
    main()
