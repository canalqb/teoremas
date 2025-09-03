# teorema_smale.py

import random

def gerar_tabela_smales(n_max):
    tabela = []
    
    for n in range(n_max + 1):
        inicio = 2 ** n
        fim = (2 ** (n + 1)) - 1
        
        # Aproximação para "Esperado pelo teorema", que é um valor aleatório dentro do intervalo
        esperado_teorema = random.randint(inicio, fim)
        
        tabela.append((n, inicio, esperado_teorema, fim))
    
    return tabela

def imprimir_tabela(tabela):
    print("N | Inicio (2^N) | Esperado pelo teorema | Fim (2^(N+1))-1")
    print("------------------------------------------------------------")
    for linha in tabela:
        print(f"{linha[0]} | {linha[1]} | {linha[2]} | {linha[3]}")

if __name__ == "__main__":
    # Gerar tabela com valores de N de 0 a 9 (como no exemplo fornecido)
    tabela = gerar_tabela_smales(9)
    imprimir_tabela(tabela)
