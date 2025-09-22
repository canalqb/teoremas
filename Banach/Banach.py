def ponto_fixo_banach(T, x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_next = T(x)
        if abs(x_next - x) < tol:
            return int(round(x_next))
        x = x_next
    return int(round(x))

def gerar_intervalo(n):
    a = 2**n
    b = 2**(n + 1) - 1
    return a, b

def T_n_factory(n):
    """Cria uma função T_n(x) = Lx + c tal que o ponto fixo esteja em [a, b]"""
    a, b = gerar_intervalo(n)
    L = 0.6  # fator de contração

    # Escolhe ponto fixo determinístico, mas não central
    # Por exemplo, 1/3 do intervalo acima de a
    x_star = a + (b - a) // 3

    # Calcula c a partir do ponto fixo
    c = (1 - L) * x_star

    # Verifica se T(x) permanece dentro do intervalo
    def T(x):
        return L * x + c

    if a <= T(a) <= b and a <= T(b) <= b:
        return T
    else:
        raise ValueError(f"Ponto fixo {x_star} gera T(x) fora do intervalo [{a}, {b}]")

# Executa para vários valores de n
for n in range(0, 10):
    a, b = gerar_intervalo(n)
    try:
        T = T_n_factory(n)
        x0 = a  # ponto inicial
        x_estrela = ponto_fixo_banach(T, x0)
        print(f"Intervalo [{a}, {b}] - Ponto fixo aproximado (inteiro): x* = {x_estrela}") 
    except ValueError as e:
        print(f"Erro para n={n}: {e}")
