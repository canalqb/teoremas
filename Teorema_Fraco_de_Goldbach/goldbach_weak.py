import sympy

# Tabela com intervalos definidos por potências de 2 e números de Mersenne
tabela = [
    (1, 1, 1),
    (2, 3, 3),
    (4, 7, 7),
    (8, 8, 15),
    (16, 21, 31),
    (32, 49, 63),
    (64, 76, 127),
    (128, 224, 255),
    (256, 467, 511),
    (512, 514, 1023),
    (1024, 1155, 2047),
    (2048, 2683, 4095),
]

def is_goldbach_weak(n):
    """
    Verifica se o número ímpar n pode ser escrito como a soma de três primos.
    Retorna a primeira decomposição encontrada ou None.
    """
    if n <= 5 or n % 2 == 0:
        return None

    primos = list(sympy.primerange(2, n))
    for i in range(len(primos)):
        for j in range(i, len(primos)):
            for k in range(j, len(primos)):
                if primos[i] + primos[j] + primos[k] == n:
                    return (primos[i], primos[j], primos[k])
    return None

def validar_tabela_com_teorema(tabela):
    print("Validando a coluna 'Meio' com o Teorema Fraco de Goldbach:")
    print("-" * 60)
    for inicio, meio, fim in tabela:
        resultado = is_goldbach_weak(meio)
        print(f"Início: {inicio}, Meio: {meio}, Fim: {fim}")
        if resultado:
            print(f"✅ {meio} = {resultado[0]} + {resultado[1]} + {resultado[2]}")
        else:
            print(f"❌ {meio} não foi decomposto como soma de 3 primos!")
        print("-" * 60)

if __name__ == "__main__":
    validar_tabela_com_teorema(tabela)
