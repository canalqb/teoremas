# invariancia_dimensao.py

def calcular_intervalos(n_max):
    tabela = []
    acumulador = 1  # Valor inicial para N = 0

    for n in range(n_max + 1):
        inicio = 2 ** n
        fim = 2 ** (n + 1) - 1
        
        if n == 0:
            esperado = 1
        elif n == 1:
            esperado = 3
        elif n == 2:
            esperado = 7
        elif n == 3:
            esperado = 8
        else:
            # Heurística: soma acumulativa com fração do intervalo
            incremento = (fim - inicio) // 2  # aproximação usando metade do intervalo
            esperado = acumulador + incremento
        
        acumulador = esperado

        tabela.append((n, inicio, esperado, fim))
    
    return tabela

def imprimir_tabela(tabela):
    print(f"{'N':>2} | {'Inicio (2^N)':>13} | {'Esperado':>8} | {'Fim (2^(N+1)-1)':>17}")
    print("-" * 50)
    for n, inicio, esperado, fim in tabela:
        print(f"{n:>2} | {inicio:>13} | {esperado:>8} | {fim:>17}")

if __name__ == "__main__":
    tabela = calcular_intervalos(9)
    imprimir_tabela(tabela)
