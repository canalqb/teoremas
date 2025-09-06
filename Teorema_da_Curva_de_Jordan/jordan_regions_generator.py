# jordan_regions_generator.py

def jordan_regions(N_max):
    """
    Calcula, para cada N, o número de regiões geradas por curvas simples fechadas
    dentro do intervalo [2^N, 2^(N+1) - 1], simulando uma subdivisão topológica com base
    no Teorema da Curva de Jordan.
    """
    tabela = []

    for n in range(N_max + 1):
        inicio = 2 ** n
        fim = (2 ** (n + 1)) - 1
        curvas = fim - inicio + 1  # número de curvas possíveis no intervalo

        # Modelo: cada curva cria uma nova subdivisão topológica (seguindo estrutura piramidal)
        # Total de regiões criadas apenas neste nível (não acumulativo)
        regioes = (curvas * (curvas + 1)) // 2  # Soma dos primeiros N números inteiros

        tabela.append((n, inicio, regioes, fim))

    return tabela


def imprimir_tabela(tabela):
    print(f"{'N':<3} | {'Início (2^N)':<14} | {'Esperado (calculado)':<23} | {'Fim (2^(N+1)-1)':<17}")
    print("-" * 65)
    for linha in tabela:
        n, inicio, esperado, fim = linha
        print(f"{n:<3} | {inicio:<14} | {esperado:<23} | {fim:<17}")


if __name__ == "__main__":
    N = 9  # até N=9 conforme a tabela fornecida
    tabela = jordan_regions(N)
    imprimir_tabela(tabela)
