# teorema_incompletude_godel.py

import random

# Função para calcular o valor "Esperado pelo Teorema"
def calcular_valor_esperado(inicio, fim):
    return random.randint(inicio, fim)

# Função para gerar e exibir a tabela
def gerar_tabela():
    print("Tabela de Valores Gerados:")
    print(f"{'N':<3}{'Início (2^N)':<20}{'Esperado pelo Teorema':<25}{'Fim (2^(N+1))-1'}")
    
    for N in range(10):
        inicio = 2**N
        fim = (2**(N+1)) - 1
        esperado = calcular_valor_esperado(inicio, fim)
        print(f"{N:<3}{inicio:<20}{esperado:<25}{fim}")

# Executando a função para gerar a tabela
if __name__ == "__main__":
    gerar_tabela()
