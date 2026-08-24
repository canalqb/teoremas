# teorema_hurewicz_v2.py

# Função que gera os valores conforme a fórmula fornecida
def gerar_valores():
    tabela = []

    # Vamos usar uma aproximação para o valor esperado
    for N in range(10):  # Estamos utilizando N de 0 a 9
        inicio = 2 ** N
        fim = (2 ** (N + 1)) - 1

        # Aproximação do valor esperado pelo teorema
        # A fórmula abaixo é uma tentativa de modelar um comportamento semelhante ao que você espera
        # Ela assume um crescimento não linear que parece adequado dado a tabela fornecida.
        esperado = (inicio + fim) // 2 + (inicio // 2)

        # Adicionando à tabela
        tabela.append([N, inicio, esperado, fim])

    return tabela


# Função para imprimir a tabela gerada
def imprimir_tabela():
    tabela = gerar_valores()

    # Imprimindo cabeçalho
    print("N | Inicio (2^N) | Esperado pelo teorema | Fim (2^(N+1))-1")
    print("-" * 50)

    # Imprimindo os valores da tabela
    for linha in tabela:
        print(f"{linha[0]} | {linha[1]} | {linha[2]} | {linha[3]}")

# Função principal
if __name__ == "__main__":
    imprimir_tabela()
