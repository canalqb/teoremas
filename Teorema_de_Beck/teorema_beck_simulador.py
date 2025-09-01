def gerar_tabela_beck(n_max):
    tabela = []
    
    # Valores iniciais do "Esperado" baseados na árvore binária cheia
    esperado = {0: 1, 1: 3, 2: 7}
    
    for n in range(n_max + 1):
        inicio = 2 ** n
        fim = 2 ** (n + 1) - 1
        
        # Definir o esperado com base na regra empírica:
        if n in esperado:
            valor_esperado = esperado[n]
        else:
            # Aparentemente, a partir de N=3, a fórmula muda
            # Vamos usar uma regra derivada por aproximação:
            # esperado[n] = esperado[n-1] + 2*(2**(n-2))
            valor_esperado = esperado[n-1] + 2 * (2 ** (n - 2))
            esperado[n] = valor_esperado
        
        tabela.append((n, inicio, valor_esperado, fim))
    
    return tabela


def imprimir_tabela(tabela):
    print(f"{'N':<3} | {'Início (2^N)':<14} | {'Esperado':<10} | {'Fim (2^(N+1)-1)':<18}")
    print("-" * 55)
    for linha in tabela:
        n, inicio, esperado, fim = linha
        print(f"{n:<3} | {inicio:<14} | {esperado:<10} | {fim:<18}")


# Executar o script
if __name__ == "__main__":
    n_max = 9
    tabela = gerar_tabela_beck(n_max)
    imprimir_tabela(tabela)
