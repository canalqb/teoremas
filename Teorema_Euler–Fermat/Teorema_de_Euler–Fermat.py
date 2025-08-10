from sympy import isprime, totient, gcd

# Tabela com intervalos e número procurado
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
]

def verifica_euler_fermat(n, a=2):
    if gcd(a, n) != 1:
        return False  # Base não coprima a n
    phi_n = int(totient(n))  # Conversão importante para evitar erro
    return pow(a, phi_n, n) == 1

print("🔎 Análise usando Teorema de Euler–Fermat (base a=2)\n")

for inicio, procurado, fim in intervalos:
    print(f"Intervalo: [{inicio}, {fim}]")
    print(f"Número Procurado: {procurado}")
    
    primo = isprime(procurado)
    phi = totient(procurado)
    euler_fermat_valido = verifica_euler_fermat(procurado, 2)
    
    print(f" → É primo? {'Sim' if primo else 'Não'}")
    print(f" → Totiente φ({procurado}) = {phi}")
    print(f" → Verificação Euler-Fermat: 2^φ(n) mod n == 1? {'Sim' if euler_fermat_valido else 'Não'}")
    print("-" * 40)
