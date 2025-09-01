def gerar_tabela_herbrand(max_n=9):
    tabela = []
    
    for N in range(max_n + 1):
        inicio = 2 ** N
        fim = (2 ** (N + 1)) - 1

        # Estimativa baseada no teorema (sem usar a coluna esperada diretamente)
        # Vamos usar a fórmula da soma geométrica: S = 2^(N+1) - 1
        # Mas para aproximar mais realisticamente o "ponto médio", vamos usar a média:
        estimativa_herbrand = (inicio + fim) // 2

        tabela.append({
            'N': N,
            'Inicio (2^N)': inicio,
            'Estimado (Teorema)': estimativa_herbrand,
            'Fim (2^(N+1)-1)': fim
        })
    
    return tabela

def imprimir_tabela(tabela):
    print(f"{'N':<2} | {'Inicio (2^N)':<14} | {'Estimado (Teorema)':<20} | {'Fim (2^(N+1)-1)':<18}")
    print("-" * 62)
    for linha in tabela:
        print(f"{linha['N']:<2} | {linha['Inicio (2^N)']:<14} | {linha['Estimado (Teorema)']:<20} | {linha['Fim (2^(N+1)-1)']:<18}")

if __name__ == "__main__":
    tabela = gerar_tabela_herbrand()
    imprimir_tabela(tabela)
