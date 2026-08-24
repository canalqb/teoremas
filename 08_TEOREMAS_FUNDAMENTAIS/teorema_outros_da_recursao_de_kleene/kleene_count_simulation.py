def kleene_fixed_point_simulation(n_max):
    print(f"{'N':<3} | {'Início (2^N)':<14} | {'Esperado pelo teorema':<25} | {'Fim (2^(N+1))-1':<17}")
    print('-' * 70)

    for n in range(n_max + 1):
        start = 2 ** n
        end = (2 ** (n + 1)) - 1
        count = 0

        for i in range(start, end + 1):
            # Critério simulado: programa "i" se comporta como f(i) se i mod log2(i+1) == 0
            # Uma simulação de ponto fixo ou autorreferência
            if i % max(1, int((i + 1).bit_length() - 1)) == 0:
                count += 1

        print(f"{n:<3} | {start:<14} | {count:<25} | {end:<17}")

# Executa o script
for A in range(0,10):
    kleene_fixed_point_simulation(A)
