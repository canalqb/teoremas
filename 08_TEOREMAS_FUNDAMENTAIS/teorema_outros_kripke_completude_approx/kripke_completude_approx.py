def kripke_completude_approx(N_max):
    print(f"{'N':>2} | {'Inicio (2^N)':>12} | {'Fim (2^(N+1))-1':>16} | {'Aproximação':>12}")
    print("-" * 52)
    
    soma_acumulada = 0
    for N in range(N_max + 1):
        inicio = 2 ** N
        fim = (2 ** (N + 1)) - 1
        # Soma acumulada dos 2^k até N
        soma_acumulada = fim
        
        # Vamos tentar uma aproximação: média entre inicio e fim somada à metade da soma acumulada anterior
        # Como valor inicial para N=0, aproximamos como inicio (que é 1)
        if N == 0:
            aproximacao = inicio
        else:
            aproximacao = (inicio + fim) // 2  # média do intervalo
            # Tentativa: somar metade do valor da aproximação anterior (pode representar acumulo de acessibilidade)
            aproximacao += int(aproximacao / 2)
        
        print(f"{N:2} | {inicio:12} | {fim:16} | {aproximacao:12}")

# Executar para N=0 até 9
kripke_completude_approx(9)
