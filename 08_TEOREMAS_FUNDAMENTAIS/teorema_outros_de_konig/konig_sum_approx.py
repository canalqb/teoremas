# konig_sum_approx.py

import math

def gerar_tabela(max_n=9):
    print(f"{'N':<2} | {'Início (2^N)':<14} | {'Estimado (König)':<20} | {'Fim (2^(N+1)-1)':<18}")
    print("-" * 65)
    for n in range(max_n + 1):
        inicio = 2 ** n
        fim = 2 ** (n + 1) - 1
        
        if n == 0:
            estimado = 1
        else:
            # Soma dos níveis anteriores: 2^n - 1
            soma_anteriores = 2 ** n - 1
            
            # Fração ajustada dos nós do nível atual
            fracao = math.log2(n + 2) / (n + 2)
            parte_nivel_n = int(2 ** n * fracao)
            
            estimado = soma_anteriores + parte_nivel_n

        print(f"{n:<2} | {inicio:<14} | {estimado:<20} | {fim:<18}")

if __name__ == "__main__":
    gerar_tabela()
