from sympy import factorint

# Função de teste de Fermat com múltiplas bases
def eh_composto_fermat(n, bases=[2, 3, 5, 7]):
    if n < 2:
        return True  # 0 e 1 não são primos
    for a in bases:
        if a >= n:
            continue
        if pow(a, n - 1, n) != 1:
            return True  # Falhou em alguma base → composto
    return False  # Passou em todas → pode ser primo

# Tabela com (inicio, procurado, fim)
intervalos = [
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
    (4096, 5216, 8191),
    (8192, 10544, 16383)
]

# Bases a serem testadas
bases_fermat = [2, 3, 5, 7]

# Processar cada intervalo
for inicio, procurado, fim in intervalos:
    print(f"\n📌 Intervalo [{inicio}, {fim}] — Procurando: {procurado}")
    print("-" * 60)

    for n in range(inicio, fim + 1):
        if eh_composto_fermat(n, bases_fermat):
            if n == procurado:
                fatores = factorint(n)
                fator_str = " * ".join([f"{p}^{e}" if e > 1 else str(p) for p, e in fatores.items()])
                print(f"🎯 >>>>> {n} falha no teste de Fermat → COMPOSTO! | Fatores: {fator_str} <<<<<")
            else:
                pass  # outros compostos não precisam ser exibidos aqui
