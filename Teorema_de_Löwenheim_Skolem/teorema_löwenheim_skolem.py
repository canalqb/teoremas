# teorema_löwenheim_skolem.py

import random

# Função para calcular o valor esperado dentro do intervalo
def calcular_valor_esperado(inicio, fim):
    # Vamos gerar um número aleatório dentro do intervalo dado
    return random.randint(inicio, fim)

# Tabela de valores de N, Início (2^N) e Fim (2^(N+1))-1
tabela = [
    (0, 2**0, 2**(0+1)-1),
    (1, 2**1, 2**(1+1)-1),
    (2, 2**2, 2**(2+1)-1),
    (3, 2**3, 2**(3+1)-1),
    (4, 2**4, 2**(4+1)-1),
    (5, 2**5, 2**(5+1)-1),
    (6, 2**6, 2**(6+1)-1),
    (7, 2**7, 2**(7+1)-1),
    (8, 2**8, 2**(8+1)-1),
    (9, 2**9, 2**(9+1)-1)
]

# Gerar a tabela de valores com a coluna "Esperado pelo teorema"
resultados = []

# Calcular o valor esperado para cada linha
for N, inicio, fim in tabela:
    esperado = calcular_valor_esperado(inicio, fim)
    resultados.append((N, inicio, esperado, fim))

# Imprimir a tabela de valores gerados
print("Tabela de Valores Gerados:")
print(f"{'N':<3} {'Início (2^N)':<15} {'Esperado pelo Teorema':<22} {'Fim (2^(N+1))-1':<20}")
for N, inicio, esperado, fim in resultados:
    print(f"{N:<3} {inicio:<15} {esperado:<22} {fim:<20}")
