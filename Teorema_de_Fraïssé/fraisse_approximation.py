# fraisse_approximation.py

def gerar_tabela_fraisse(limite=10):
    print(f"{'N':<2} | {'Início (2^N)':<15} | {'Aproximado pelo teorema':<26} | {'Fim (2^(N+1)-1)':<18}")
    print("-" * 70)
    
    for N in range(limite):
        inicio = 2 ** N
        fim = 2 ** (N + 1) - 1
        
        # Aproximação inspirada no crescimento de subestruturas
        # Usamos a soma de potências anteriores (estrutura cumulativa)
        # Similar a 2^(N+1) - N - 1, como uma heurística inicial
        if N == 0:
            aproximado = 1
        else:
            aproximado = sum(2 ** i for i in range(N + 1)) - N  # ou - N - 1
        
        print(f"{N:<2} | {inicio:<15} | {aproximado:<26} | {fim:<18}")

if __name__ == "__main__":
    gerar_tabela_fraisse(10)
