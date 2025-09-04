# mvtabela_gerador.py

def gerar_tabela_mayer_vietoris(n_max):
    tabela = []
    acumulado = 1  # valor inicial

    for n in range(n_max + 1):
        inicio = 2 ** n
        fim = 2 ** (n + 1) - 1

        if n == 0:
            estimado = 1
        else:
            # estratégia de acúmulo: duplica e soma anterior
            estimado = acumulado + inicio - 1  # simula o crescimento

        acumulado = estimado  # acumula para próxima iteração

        tabela.append((n, inicio, estimado, fim))

    return tabela


def imprimir_tabela(tabela):
    print(f"{'N':<3} | {'Inicio (2^N)':<14} | {'Estimado pelo Teorema':<24} | {'Fim (2^(N+1))-1'}")
    print("-" * 65)
    for n, inicio, estimado, fim in tabela:
        print(f"{n:<3} | {inicio:<14} | {estimado:<24} | {fim}")


if __name__ == "__main__":
    n_max = 9
    tabela = gerar_tabela_mayer_vietoris(n_max)
    imprimir_tabela(tabela)
