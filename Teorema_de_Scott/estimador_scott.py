# estimador_scott.py

def gerar_tabela_scott(max_n=9):
    tabela = []
    for n in range(max_n + 1):
        inicio = 2 ** n
        fim = 2 ** (n + 1) - 1
        
        # Estimativa baseada em soma de nós com ponderação empírica
        # Para simular crescimento, usamos uma função logística ou exponencial suavizada
        if n == 0:
            esperado = 1
        else:
            esperado = round(sum(2 ** k for k in range(n)) * (1 + n / 5.0))

        tabela.append((n, inicio, esperado, fim))
    return tabela

def imprimir_tabela(tabela):
    print(f"{'N':<2} | {'Início (2^N)':<14} | {'Estimado (Teorema)':<22} | {'Fim (2^(N+1))-1'}")
    print("-" * 60)
    for n, inicio, esperado, fim in tabela:
        print(f"{n:<2} | {inicio:<14} | {esperado:<22} | {fim}")

if __name__ == "__main__":
    tabela = gerar_tabela_scott()
    imprimir_tabela(tabela)
