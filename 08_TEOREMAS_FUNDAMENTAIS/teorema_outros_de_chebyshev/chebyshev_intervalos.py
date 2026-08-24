# chebyshev_intervalos.py

import math
from tabulate import tabulate

def pi_approx(x):
    return x / math.log(x) if x > 1 else 0

def chebyshev_interval_estimates(n_max):
    results = []
    for n in range(n_max + 1):
        start = 2 ** n
        end = (2 ** (n + 1)) - 1
        pi_end = pi_approx(end)
        pi_start_minus1 = pi_approx(start - 1) if start > 1 else 0
        estimated_primes = round(pi_end - pi_start_minus1)
        results.append([n, start, estimated_primes, end])
    return results

# Gerar a tabela para N de 0 a 9
table = chebyshev_interval_estimates(9)

# Exibir a tabela formatada
headers = ["N", "Início (2^N)", "Estimado pelo Teorema", "Fim (2^(N+1) - 1)"]
print(tabulate(table, headers=headers, tablefmt="grid"))
