# alaoglu_potencias_mersenne.py

def potencia_de_2(n):
    return 2 ** n

def mersenne(n):
    return 2 ** (n + 1) - 1

def gera_tabela(N_max):
    print(f"{'N':>2} | {'Inicio (2^N)':>12} | {'Fim (2^(N+1))-1':>18}")
    print("-" * 40)
    for N in range(N_max + 1):
        inicio = potencia_de_2(N)
        fim = mersenne(N)
        print(f"{N:>2} | {inicio:>12} | {fim:>18}")

def valor_estimado_alaoglu(N):
    """
    Função que tenta aproximar um valor dentro do intervalo [2^N, 2^(N+1)-1]
    sem usar a coluna 'Esperado pelo teorema'.
    Por simplicidade, vamos usar uma média ponderada simples.
    """
    inicio = potencia_de_2(N)
    fim = mersenne(N)
    
    # Exemplo de uma média ponderada:
    # Pesamos o início mais que o fim para refletir o crescimento da função
    estimado = int((inicio * 0.6) + (fim * 0.4))
    return estimado

def gera_tabela_com_estimados(N_max):
    print(f"{'N':>2} | {'Inicio (2^N)':>12} | {'Estimado':>9} | {'Fim (2^(N+1))-1':>18}")
    print("-" * 55)
    for N in range(N_max + 1):
        inicio = potencia_de_2(N)
        fim = mersenne(N)
        estimado = valor_estimado_alaoglu(N)
        print(f"{N:>2} | {inicio:>12} | {estimado:>9} | {fim:>18}")

if __name__ == "__main__":
    N_max = 9
    print("Tabela de intervalos baseados em potências de 2 e números de Mersenne:")
    gera_tabela(N_max)
    print("\nTabela com valores estimados baseados no teorema (sem usar coluna esperada):")
    gera_tabela_com_estimados(N_max)
