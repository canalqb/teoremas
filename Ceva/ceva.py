def calcular_c(a, b):
    """
    Calcula o valor de c para o Teorema de Ceva,
    dado os valores de a e b, onde:
    a = razão do primeiro segmento
    b = razão do segundo segmento
    c = razão do terceiro segmento
    e a * b * c = 1
    """
    if a == 0 or b == 0:
        raise ValueError("Os valores de a e b devem ser diferentes de zero.")

    c = 1 / (a * b)
    return c

def main():
    print("Cálculo da terceira razão pelo Teorema de Ceva")
    try:
        a = float(input("Digite o valor de a (primeira razão): "))
        b = float(input("Digite o valor de b (segunda razão): "))
        c = calcular_c(a, b)
        print(f"Para a = {a} e b = {b}, o valor de c é {c:.6f}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()



C:\Users\34630737\Desktop\ler>ceva
Cálculo da terceira razão pelo Teorema de Ceva
Digite o valor de a (primeira razão): 64
Digite o valor de b (segunda razão): 32
Para a = 64.0 e b = 32.0, o valor de c é 0.000488

C:\Users\34630737\Desktop\ler>
