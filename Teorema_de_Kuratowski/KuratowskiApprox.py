# KuratowskiApprox.py

def main():
    print(f"{'N':>2} | {'Inicio (2^N)':>12} | {'Fim (2^(N+1))-1':>16} | {'Média':>8} | {'Aprox (chute)':>14}")
    print("-" * 65)
    
    for N in range(10):
        inicio = 2**N
        fim = 2**(N+1) - 1
        media = (inicio + fim) // 2
        
        # Aproximação com fórmula simples, ajustada para N
        aprox = int(inicio * (1 + N / 4))
        
        print(f"{N:2d} | {inicio:12d} | {fim:16d} | {media:8d} | {aprox:14d}")

if __name__ == "__main__":
    main()
