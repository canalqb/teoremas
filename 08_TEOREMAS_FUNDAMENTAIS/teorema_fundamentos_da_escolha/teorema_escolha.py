# teorema_escolha.py

def calcular_esperado(inicio, fim):
    """
    Calcula uma estimativa para o valor esperado usando
    uma média ponderada entre inicio e fim.
    Ajustado para se aproximar dos valores observados.
    """
    # Experimento com média ponderada:
    # Peso maior para inicio, pois parece crescer menos rápido
    peso_inicio = 0.7
    peso_fim = 0.3
    esperado = peso_inicio * inicio + peso_fim * fim
    return int(round(esperado))

def main():
    tabela = [
        {"N":0, "Inicio": 2**0, "Fim": 2**(0+1)-1},
        {"N":1, "Inicio": 2**1, "Fim": 2**(1+1)-1},
        {"N":2, "Inicio": 2**2, "Fim": 2**(2+1)-1},
        {"N":3, "Inicio": 2**3, "Fim": 2**(3+1)-1},
        {"N":4, "Inicio": 2**4, "Fim": 2**(4+1)-1},
        {"N":5, "Inicio": 2**5, "Fim": 2**(5+1)-1},
        {"N":6, "Inicio": 2**6, "Fim": 2**(6+1)-1},
        {"N":7, "Inicio": 2**7, "Fim": 2**(7+1)-1},
        {"N":8, "Inicio": 2**8, "Fim": 2**(8+1)-1},
        {"N":9, "Inicio": 2**9, "Fim": 2**(9+1)-1},
    ]

    # Cabeçalho da tabela
    print(f"{'N':>2} | {'Inicio (2^N)':>12} | {'Estimativa':>10} | {'Fim (2^(N+1))-1':>16}")
    print("-" * 50)

    for linha in tabela:
        N = linha["N"]
        inicio = linha["Inicio"]
        fim = linha["Fim"]
        estimativa = calcular_esperado(inicio, fim)
        print(f"{N:2} | {inicio:12} | {estimativa:10} | {fim:16}")

if __name__ == "__main__":
    main()
