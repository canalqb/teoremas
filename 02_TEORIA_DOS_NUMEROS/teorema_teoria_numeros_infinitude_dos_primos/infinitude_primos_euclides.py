import math

# Função para gerar primos até um limite usando o Crivo de Eratóstenes
def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for start_num in range(2, int(math.isqrt(limit)) + 1):
        if primes[start_num]:
            for multiple in range(start_num * start_num, limit + 1, start_num):
                primes[multiple] = False
    return {n for n, is_prime_val in enumerate(primes) if is_prime_val}

# Lista de primos conhecidos (usando set para busca e adição mais rápidas)
known_primes_set = set()

# Cabeçalho da tabela
print(f"{'ID':>2} | {'Intervalo':^17} | {'Qtd. de Primos':^15} | {'Produto + 1 (Euclides)':^30}")
print("-" * 75)

# Processar intervalos de 0 a 10
for i in range(5):
    start = 2**i
    end = 2**(i+1) - 1

    # Gerar primos até o 'end' do intervalo atual usando o Crivo
    current_sieve_limit = end
    all_primes_up_to_current_limit = sieve_of_eratosthenes(current_sieve_limit)
    primos_intervalo = [n for n in range(start, end + 1) if n in all_primes_up_to_current_limit]

    # Atualizar lista de primos conhecidos
    known_primes_set.update(primos_intervalo)

    # Calcular produto dos primos + 1
    if known_primes_set:
        produto = 1
        for p in known_primes_set:
            produto *= p

        def is_prime_for_euclides(n):
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for j in range(3, int(math.isqrt(n)) + 1, 2):
                if n % j == 0:
                    return False
            return True

        euclides_n = produto + 1
        status = "Primo" if is_prime_for_euclides(euclides_n) else "Composto"
        euclides_result = f"{euclides_n} ({status})"
    else:
        euclides_result = "-"

    # Imprimir imediatamente o resultado desta iteração
    print(f"{i:>2} | [{start}, {end}]:^17 | {len(primos_intervalo):>15} | {euclides_result:<30}")
