# poincare_hopf_mersenne.py

def mersenne(n):
    return 2**(n+1) - 1

def aproximacao_poincare_hopf(n):
    """
    Aproxima o valor esperado do teorema no intervalo [2^n, 2^(n+1)-1].
    Como não podemos usar a coluna 'Esperado pelo teorema', 
    tentaremos uma aproximação simples.
    
    Vamos usar uma fórmula que combina o início e fim do intervalo,
    ponderando de forma não linear para tentar se aproximar do padrão.
    """

    inicio = 2**n
    fim = mersenne(n)
    
    # Tentativa 1: média geométrica entre início e fim
    media_geom = (inicio * fim) ** 0.5
    
    # Tentativa 2: média aritmética
    media_arit = (inicio + fim) / 2
    
    # Combinação ponderada (tentativa experimental)
    # Damos mais peso para fim, já que valores crescem perto do fim do intervalo
    valor_aprox = 0.3 * media_geom + 0.7 * media_arit
    
    # Arredondar para inteiro para ficar mais "contável"
    return round(valor_aprox)

def gerar_tabela(max_n=9):
    print(f"{'N':<3} | {'Inicio (2^N)':<12} | {'Aprox. Poincaré–Hopf':<22} | {'Fim (2^(N+1))-1':<15}")
    print("-" * 60)
    for n in range(max_n+1):
        inicio = 2**n
        fim = mersenne(n)
        aprox = aproximacao_poincare_hopf(n)
        print(f"{n:<3} | {inicio:<12} | {aprox:<22} | {fim:<15}")

if __name__ == "__main__":
    gerar_tabela()
