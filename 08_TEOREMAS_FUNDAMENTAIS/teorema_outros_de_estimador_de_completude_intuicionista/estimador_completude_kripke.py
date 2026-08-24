# estimador_completude_kripke.py

def estimar_completude_kripke(N_max):
    print(f"{'N':<3} | {'Início (2^N)':<14} | {'Estimado (Kripke)':<20} | {'Fim (2^(N+1)-1)':<15}")
    print("-" * 60)
    
    for N in range(N_max + 1):
        inicio = 2 ** N
        fim = (2 ** (N + 1)) - 1
        
        # Estimativa baseada em crescimento intuitivo via modelos de Kripke
        # Modelo 1: Soma ponderada crescente
        # A ideia é que os mundos possíveis crescem com base em combinações crescentes e irreversíveis
        estimado = sum(2 ** i for i in range(N + 1)) + (N * (N - 1))  # soma de 2^i + crescimento não-linear
        
        print(f"{N:<3} | {inicio:<14} | {estimado:<20} | {fim:<15}")

# Executar para N de 0 até 9
estimar_completude_kripke(9)
