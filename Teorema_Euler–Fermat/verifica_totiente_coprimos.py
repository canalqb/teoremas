from math import gcd

def phi(n):
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1
    return result

inicio = [1, 2, 4, 8, 16, 32, 64, 128, 256]
procurado = [1, 3, 7, 8, 21, 49, 76, 224, 467]
fim = [1, 3, 7, 15, 31, 63, 127, 255, 511]

print("Início | Procurado | Fim | Totiente(phi(Fim))")
for i, f in enumerate(fim):
    if f == 1:
        phi_val = 1
    else:
        phi_val = phi(f)
    print(f"{inicio[i]:6} | {procurado[i]:8} | {fim[i]:3} | {phi_val:18}")
