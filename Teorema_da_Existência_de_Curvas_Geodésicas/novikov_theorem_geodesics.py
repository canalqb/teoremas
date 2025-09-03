# novikov_theorem_geodesics.py

import numpy as np

# Tabela com os valores de Inicio e Fim
tabela = [
    (0, 1, 1), (1, 2, 3), (2, 4, 7), (3, 8, 15), (4, 16, 31), 
    (5, 32, 63), (6, 64, 127), (7, 128, 255), (8, 256, 511), (9, 512, 1023)
]

# Função que gera valores dentro do intervalo [Inicio, Fim]
def geodesic_values():
    resultados = []
    
    for N, inicio, fim in tabela:
        # Gerando os valores entre Inicio e Fim
        # Usaremos uma progressão que "cresce" dentro do intervalo
        valores = np.linspace(inicio, fim, num=fim - inicio + 1, dtype=int)
        
        # Adiciona os valores na lista de resultados
        resultados.append((N, inicio, valores, fim))
    
    return resultados

# Função para aproximar o valor esperado pelo teorema
def aproximar_teorema():
    resultados = geodesic_values()
    aproximados = []
    
    for N, inicio, valores, fim in resultados:
        # A média da progressão gerada pode ser uma aproximação do "Esperado pelo teorema"
        media = np.mean(valores)
        aproximados.append((N, inicio, round(media), fim))
    
    return aproximados

# Função principal para exibir a tabela com os resultados aproximados
def exibir_tabela():
    aproximados = aproximar_teorema()
    
    print("N | Inicio (2^N) | Esperado pelo teorema | Fim (2^(N+1))-1")
    print("-" * 50)
    for N, inicio, esperado, fim in aproximados:
        print(f"{N:2} | {inicio:12} | {esperado:20} | {fim:18}")

# Execução principal
if __name__ == "__main__":
    exibir_tabela()
