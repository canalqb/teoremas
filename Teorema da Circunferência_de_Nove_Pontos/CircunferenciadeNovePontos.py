import math

# Verifica se um número é primo
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Encontra o próximo primo de Mersenne maior que 2^n
def next_mersenne(n):
    p = n + 1
    while True:
        mersenne = 2 ** p - 1
        if is_prime(mersenne):
            return mersenne, p
        p += 1

# Gera uma simulação dos pontos da circunferência de 9 pontos
def simulate_nine_point_circle(n, base, mersenne):
    print(f"\n🔢 n = {n}")
    print(f"📌 2^{n} = {base}")
    print(f"🧠 Próximo número de Mersenne = {mersenne} (p = {int(math.log2(mersenne + 1))})")

    # Simulação dos 9 pontos (nomeando-os com base nas relações)
    print("🟠 Pontos da circunferência de 9 pontos (simulados):")
    points = {
        "Médios dos lados": [base / 2, mersenne / 2, (base + mersenne) / 2],
        "Pés das alturas": [math.sqrt(base), math.sqrt(mersenne), math.sqrt(base * mersenne)],
        "Médios vértice-ortocentro": [(base + mersenne)/4, (base + mersenne)/3, (base + mersenne)/5]
    }

    for categoria, valores in points.items():
        print(f"  📍 {categoria}: {[round(v, 2) for v in valores]}")

# Loop principal de n = 0 até 10
for n in range(0, 11):
    base = 2 ** n
    mersenne, p = next_mersenne(n)
    simulate_nine_point_circle(n, base, mersenne)

