# lebesgue_potencias2.py

import math

def f(x, N):
    """
    Função simples integrável definida em cada intervalo [2^N, 2^{N+1} - 1]
    Neste caso, f(x) = N, uma constante, para garantir integrabilidade.
    """
    return N

def lebesgue_integral(N):
    """
    Aplica o Teorema de Lebesgue sobre derivadas para o intervalo [2^N, 2^{N+1}-1]
    Calcula a integral de f(x) = N no intervalo e obtém F(x)
    """
    inicio = 2 ** N
    fim = 2 ** (N + 1) - 1
    comprimento = fim - inicio + 1

    # Como f(x) = N é constante, a integral de f de a até b é f(x)*(b - a)
    integral = f(inicio, N) * comprimento

    return {
        "N": N,
        "Início (2^N)": inicio,
        "Esperado pelo teorema": integral,
        "Fim (2^(N+1)-1)": fim
    }

def gerar_tabela(max_N=9):
    print(f"{'N':<3} | {'Início (2^N)':<14} | {'Esperado pelo teorema':<23} | {'Fim (2^(N+1))-1'}")
    print("-" * 70)
    for N in range(max_N + 1):
        linha = lebesgue_integral(N)
        print(f"{linha['N']:<3} | {linha['Início (2^N)']:<14} | {linha['Esperado pelo teorema']:<23} | {linha['Fim (2^(N+1)-1)']}")

if __name__ == "__main__":
    gerar_tabela()
