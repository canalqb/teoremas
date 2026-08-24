import math

def simulate_kolmogorov_table(max_a=8):
    print(f"{'2^A':>6} {'PROCURANDO':>12} {'2^(A+1)-1':>14} {'% Incompressíveis':>20}")
    print("-" * 60)

    for a in range(1, max_a + 1):
        num_programs = 2 ** a                   # Número de programas de tamanho <= A bits
        max_string_value = 2 ** (a + 1) - 1     # Maior valor com A+1 bits
        total_strings = max_string_value + 1   # Quantidade total de strings (0 até 2^{A+1}-1)

        # Máximo de strings que podem ser geradas por programas ≤ A bits
        # (teoricamente, nem todos programas válidos geram strings únicas, mas vamos assumir o melhor caso)
        compressible_strings = num_programs - 1  # Tirando o programa vazio (ou inválido)

        # Strings restantes são incompressíveis
        incompressible = total_strings - compressible_strings
        percent_incompressible = 100 * incompressible / total_strings

        print(f"{2**a:6} {compressible_strings:12} {max_string_value:14} {percent_incompressible:20.2f}%")

simulate_kolmogorov_table()
