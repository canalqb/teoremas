def gerar_pontos_fora_reta(k_values, n_max=10):
    """
    Para cada n de 0 até n_max, gera pontos (x, y) com x no intervalo [2^n, 2^{n+1} - 1]
    e y = 2*x + k para cada k em k_values (k != 0 para estar fora da reta).
    
    Retorna um dicionário {n: lista_de_pontos}.
    """
    pontos_fora_reta = {}

    for n in range(n_max + 1):
        inicio = 2 ** n
        fim = 2 ** (n + 1) - 1

        pontos_no_intervalo = []
        for x in range(inicio, fim + 1):
            for k in k_values:
                y = 2 * x + k
                pontos_no_intervalo.append((x, y))
        pontos_fora_reta[n] = pontos_no_intervalo

    return pontos_fora_reta

def main():
    # Valores de k diferentes de zero para garantir que o ponto nao esteja na reta y=2x
    k_values = [-2, -1, 1, 2]
    pontos_fora = gerar_pontos_fora_reta(k_values, n_max=10)  

    for n, pontos in pontos_fora.items():
        print(f"\nIntervalo para n={n}: x in [{2**n}, {2**(n+1)-1}]")
        print(f"Exemplos de pontos fora da reta y=2x (total {len(pontos)} pontos):")
        # Mostrar só os primeiros 10 para não poluir a saída
        for ponto in pontos[:10]:
            print(f"  {ponto}")

if __name__ == "__main__":
    main()
