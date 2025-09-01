# yoneda_count_growth.py

def gerar_tabela(n_max):
    tabela = []
    
    acumulado = 0  # Total acumulado simula quantidade de "visões" ou "morfismos"
    
    for n in range(n_max + 1):
        inicio = 2**n
        fim = 2**(n+1) - 1
        
        # Yoneda: número de formas de "ver" esse nível baseado nos anteriores
        # Vamos simular isso usando um acumulador + o próprio valor atual
        acumulado += inicio  # como se novos morfismos fossem adicionados
        yoneda_estimado = acumulado  # nossa estimativa do que o teorema "esperaria"
        
        tabela.append((n, inicio, yoneda_estimado, fim))
    
    return tabela

def imprimir_tabela(tabela):
    print(f"{'N':<2} | {'Inicio (2^N)':<14} | {'Estimado (Yoneda)':<20} | {'Fim (2^(N+1))-1'}")
    print("-" * 60)
    for n, inicio, yoneda_estimado, fim in tabela:
        print(f"{n:<2} | {inicio:<14} | {yoneda_estimado:<20} | {fim}")

# Executa
if __name__ == "__main__":
    n_max = 9
    tabela = gerar_tabela(n_max)
    imprimir_tabela(tabela)
