from math import gcd 

def gerar_ternas_pitagoricas(c_min, c_max):
    ternas = []
    m = 1
    while True:
        m2 = m * m
        if m2 > c_max:
            break
        for n in range(1, m):
            if (m - n) % 2 == 1 and gcd(m, n) == 1:  # ternas primitivas
                x = m * m - n * n
                y = 2 * m * n
                z = m * m + n * n
                if c_min < z < c_max:
                    ternas.append((x, y, z))
        m += 1
    return ternas

# Intervalo desejado
c = 0
for c in range(0,10):
    # Rodar o script
    ternas_encontradas = gerar_ternas_pitagoricas(2 ** c, 2 ** (c+1)-1)

    # Exibir resultado
    for x, y, z in ternas_encontradas:
        print(f"{c} -> a = {x}, b = {y}, c = {z}")
