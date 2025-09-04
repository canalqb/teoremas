# classificacao_superficies.py

def classificacao_superficies(max_n=6):
    """
    Representação simbólica da classificação de superfícies orientáveis.
    Para cada n, gênero g = 2^n e número de Mersenne M_n = 2^n - 1.
    A característica de Euler é calculada para a superfície orientável:
    χ = 2 - 2g
    """
    print(f"{'N':>2} | {'Gênero g=2^N':>10} | {'Mersenne M_N=2^N-1':>18} | {'Euler χ=2-2g':>12}")
    print("-" * 55)
    
    for N in range(max_n + 1):
        genero = 2 ** N
        mersenne = 2 ** N - 1
        euler = 2 - 2 * genero
        print(f"{N:2d} | {genero:10d} | {mersenne:18d} | {euler:12d}")

if __name__ == "__main__":
    classificacao_superficies()
