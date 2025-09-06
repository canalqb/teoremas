# gauss_bonnet_powers.py

def gauss_bonnet_simulation(N_max):
    tabela = []
    
    for N in range(N_max + 1):
        inicio = 2 ** N
        fim = 2 ** (N + 1) - 1
        
        # Simulação de "esperado" usando a estrutura topológica:
        # Vamos simular que temos um grafo planar com V vértices (2^N)
        # Número máximo de arestas em um grafo planar sem múltiplas arestas:
        # E <= 3V - 6
        V = inicio
        E = min(3 * V - 6, fim - inicio)  # não pode passar do fim
        F = E - V + 2  # Fórmula de Euler para grafos planos: V - E + F = 2
        
        # A característica de Euler será:
        chi = V - E + F  # = 2
        
        # A soma esperada por analogia com o teorema:
        esperado = V + F  # valor total de "elementos topológicos"
        
        # Garante que está no intervalo
        if esperado < inicio:
            esperado = inicio
        elif esperado > fim:
            esperado = fim
        
        tabela.append((N, inicio, esperado, fim))
    
    return tabela


def imprimir_tabela(tabela):
    print(f"{'N':<3} | {'Inicio':<7} | {'Esperado (teorema)':<20} | {'Fim':<7}")
    print("-" * 50)
    for N, inicio, esperado, fim in tabela:
        print(f"{N:<3} | {inicio:<7} | {esperado:<20} | {fim:<7}")


if __name__ == "__main__":
    N_max = 9
    tabela = gauss_bonnet_simulation(N_max)
    imprimir_tabela(tabela)
