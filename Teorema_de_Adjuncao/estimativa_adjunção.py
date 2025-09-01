# estimativa_adjunção.py

def calcular_estimativas(n_max):
    resultados = []
    estimativas = []

    for n in range(n_max + 1):
        inicio = 2 ** n
        fim = (2 ** (n + 1)) - 1

        # Ajuste com base na tabela fornecida
        if n == 0:
            estimado = 1
        elif n == 1:
            estimado = 3
        elif n == 2:
            estimado = 7
        elif n == 3:
            estimado = 8
        else:
            # Modelo ajustado com soma de dois anteriores para simular adjunção
            estimado = estimativas[-1] + estimativas[-2]

        estimativas.append(estimado)

        resultados.append({
            "N": n,
            "Inicio": inicio,
            "Estimado": estimado,
            "Fim": fim
        })

    return resultados

def imprimir_tabela(dados):
    print(f"{'N':<3} | {'Inicio (2^N)':<14} | {'Estimado':<9} | {'Fim (2^(N+1)-1)':<17}")
    print("-" * 52)
    for linha in dados:
        print(f"{linha['N']:<3} | {linha['Inicio']:<14} | {linha['Estimado']:<9} | {linha['Fim']:<17}")

if __name__ == "__main__":
    n_max = 9
    tabela = calcular_estimativas(n_max)
    imprimir_tabela(tabela)
