def mostowski_teorema(N_max):
    resultados = []

    # Valor inicial (T(0)) é 1
    valores = [1]

    for N in range(N_max + 1):
        inicio = 2 ** N
        fim = (2 ** (N + 1)) - 1

        # Para gerar o "Esperado pelo Teorema", somamos os valores anteriores e o atual
        if N == 0:
            esperado = valores[0]
        else:
            esperado = valores[-1] + (2 ** N)
            valores.append(esperado)

        resultados.append({
            "N": N,
            "Inicio (2^N)": inicio,
            "Esperado pelo teorema": esperado,
            "Fim (2^(N+1)-1)": fim
        })

    return resultados


def imprimir_tabela(resultados):
    print(f"{'N':<3} | {'Inicio (2^N)':<15} | {'Esperado pelo teorema':<24} | {'Fim (2^(N+1))-1'}")
    print("-" * 70)
    for linha in resultados:
        print(f"{linha['N']:<3} | {linha['Inicio (2^N)']:<15} | {linha['Esperado pelo teorema']:<24} | {linha['Fim (2^(N+1)-1)']}")


# Executar o script para N de 0 a 9
tabela = mostowski_teorema(9)
imprimir_tabela(tabela)
