import numpy as np
from scipy.integrate import quad

def teorema_pappus(n, limit_quad=200):
    a = 2**n
    b = 2**(n+1) - 1

    if a == b:
        print(f"Intervalo inválido para n={n}: a == b == {a}")
        return None

    def f(x):
        return np.sin(x) + 2

    def integrand_length(x):
        dy_dx = np.cos(x)
        return np.sqrt(1 + dy_dx**2)

    comprimento, _ = quad(integrand_length, a, b, limit=limit_quad)
    if comprimento == 0:
        print(f"Comprimento zero para n={n}, intervalo [{a}, {b}]")
        return None

    def integrand_centroid_y(x):
        return f(x) * integrand_length(x)

    y_c, _ = quad(integrand_centroid_y, a, b, limit=limit_quad)
    y_c /= comprimento

    distancia = 2 * np.pi * y_c
    area_superficie = comprimento * distancia

    area_regiao, _ = quad(f, a, b, limit=limit_quad)
    if area_regiao == 0:
        print(f"Área da região zero para n={n}, intervalo [{a}, {b}]")
        return None

    def integrand_centroid_area(x):
        return f(x) * f(x)

    y_bar, _ = quad(integrand_centroid_area, a, b, limit=limit_quad)
    y_bar /= area_regiao

    distancia_area = 2 * np.pi * y_bar
    volume = area_regiao * distancia_area

    return {
        "n": n,
        "a": a,
        "b": b,
        "comprimento": comprimento,
        "centroide_curva_y": y_c,
        "distancia_curva": distancia,
        "area_superficie": area_superficie,
        "area_regiao": area_regiao,
        "centroide_area_y": y_bar,
        "distancia_area": distancia_area,
        "volume": volume
    }


limit_quad = 20000

for n in range(11):
    resultados = teorema_pappus(n, limit_quad=limit_quad)
    if resultados is None:
        continue
    print(f"\nn = {resultados['n']}, intervalo: [{resultados['a']}, {resultados['b']}]")
    print(f"Comprimento da curva: {resultados['comprimento']:.4f}")
    print(f"Centroide da curva (y_c): {resultados['centroide_curva_y']:.4f}")
    print(f"Distância percorrida pelo centroide: {resultados['distancia_curva']:.4f}")
    print(f"Área da superfície gerada pela rotação da curva: {resultados['area_superficie']:.4f}")
    print(f"Área da região: {resultados['area_regiao']:.4f}")
    print(f"Centroide da área (y_bar): {resultados['centroide_area_y']:.4f}")
    print(f"Distância percorrida pelo centroide da área: {resultados['distancia_area']:.4f}")
    print(f"Volume do sólido gerado pela rotação da área: {resultados['volume']:.4f}")
