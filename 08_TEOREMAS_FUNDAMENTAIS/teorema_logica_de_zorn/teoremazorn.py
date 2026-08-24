# teoremazorn.py

def calcular_esperado_por_teorema(tabela, alpha=0.6):
    resultados = []
    esperado_anterior = tabela[0][1]  # Inicio para N=0

    for i, (N, inicio, fim) in enumerate(tabela):
        if N == 0:
            esperado = inicio
        else:
            tamanho_intervalo = fim - inicio + 1  # igual a 2^N
            esperado = esperado_anterior + alpha * tamanho_intervalo
            # Garantir que esperado fique dentro do intervalo
            esperado = max(inicio, min(esperado, fim))
        resultados.append((N, inicio, esperado, fim))
        esperado_anterior = esperado

    return resultados


def imprimir_tabela(resultados):
    print(f"{'N':<3} | {'Inicio (2^N)':<12} | {'Estimado':<9} | {'Fim (2^(N+1))-1':<15}")
    print("-" * 47)
    for N, inicio, esperado, fim in resultados:
        print(f"{N:<3} | {inicio:<12} | {int(esperado):<9} | {fim:<15}")


def main():
    tabela = [
        (0, 1, 1),
        (1, 2, 3),
        (2, 4, 7),
        (3, 8, 15),
        (4, 16, 31),
        (5, 32, 63),
        (6, 64, 127),
        (7, 128, 255),
        (8, 256, 511),
        (9, 512, 1023),
    ]
    
    # Ajusta alpha para tentar aproximar os valores "Esperado pelo teorema"
    alpha = 0.6
    resultados = calcular_esperado_por_teorema(tabela, alpha)
    imprimir_tabela(resultados)


if __name__ == "__main__":
    main()
