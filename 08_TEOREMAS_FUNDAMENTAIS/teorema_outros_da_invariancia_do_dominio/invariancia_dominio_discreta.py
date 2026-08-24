# invariancia_dominio_discreta.py

def gerar_tabela(max_n=9):
    print(f"{'N':<3} | {'Inicio (2^N)':<13} | {'Calculado':<10} | {'Fim (2^(N+1)-1)':<18}")
    print("-" * 55)

    for n in range(max_n + 1):
        inicio = 2 ** n
        fim = 2 ** (n + 1) - 1

        # Usando uma aproximação combinatória baseada em somatórios ou exponenciais
        # Aqui, vamos testar uma heurística: somatório de (2^k - 1) de k=0 até N
        # Ou usar funções que cresçam mais rápido com N
        
        if n == 0:
            calculado = 1
        else:
            # Heurística baseada na soma de números de Mersenne anteriores
            calculado = sum([2**k - 1 for k in range(1, n + 1)]) + 1

        # Garante que o valor está dentro do intervalo [inicio, fim]
        calculado = max(inicio, min(calculado, fim))

        print(f"{n:<3} | {inicio:<13} | {calculado:<10} | {fim:<18}")

if __name__ == "__main__":
    gerar_tabela()
