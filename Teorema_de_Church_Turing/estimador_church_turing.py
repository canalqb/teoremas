# estimador_church_turing.py

def estimar_valores_teorema(n_max):
    tabela = []
    for n in range(n_max + 1):
        inicio = 2 ** n
        fim = 2 ** (n + 1) - 1
        
        # Estimativa baseada em crescimento computacional limitado
        # Por exemplo: logaritmo multiplicado, para evitar ultrapassar 'fim'
        # A função abaixo é arbitrária, mas tenta seguir o padrão dos dados reais

        estimado = int(inicio * (n + 1) ** 0.8)

        # Corrigir se ultrapassar o valor máximo possível
        if estimado > fim:
            estimado = fim

        tabela.append((n, inicio, estimado, fim))

    return tabela


def imprimir_tabela(tabela):
    print(f"{'N':<3} | {'Início (2^N)':<14} | {'Estimado (Teorema)':<20} | {'Fim (2^(N+1)-1)':<16}")
    print("-" * 65)
    for linha in tabela:
        n, inicio, estimado, fim = linha
        print(f"{n:<3} | {inicio:<14} | {estimado:<20} | {fim:<16}")


if __name__ == "__main__":
    n_max = 9
    tabela = estimar_valores_teorema(n_max)
    imprimir_tabela(tabela)
