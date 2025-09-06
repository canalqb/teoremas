# borsuk_ulam_approx.py

def gerar_tabela(N_max=9):
    print(f"{'N':>2} | {'Inicio (2^N)':>12} | {'Aprox. Teorema':>15} | {'Fim (2^(N+1))-1':>18}")
    print("-" * 55)
    
    for N in range(N_max+1):
        inicio = 2 ** N
        fim = (2 ** (N + 1)) - 1
        
        # Aproximação: média do intervalo [inicio, fim]
        aproximado = (inicio + fim) // 2
        
        print(f"{N:>2} | {inicio:>12} | {aproximado:>15} | {fim:>18}")

if __name__ == "__main__":
    gerar_tabela()
