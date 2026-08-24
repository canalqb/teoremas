def calcular_c(a, b):
    """
    Calcula o valor de c segundo o Teorema de Menelau,
    dado os valores de a e b, onde:
    a = AD/DB
    b = BE/EC
    c = CF/FA
    e a * b * c = -1
    """
    c = -1 / (a * b)
    return c

# Exemplo com a=32 e b=64
a = 1155
b = 1024
c = calcular_c(a, b)

print(f"Para a = {a} e b = {b}, o valor de c é {c}")
