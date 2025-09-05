# tietze_extension_simulator.py

def gerar_tabela_tietze(max_n=9):
    print(f"{'N':<3} | {'Início (2^N)':<15} | {'Fim (2^(N+1)-1)':<18} | {'Gerado (estimado)':<20}")
    print("-" * 65)

    resultados = []
    
    for n in range(max_n + 1):
        inicio = 2 ** n
        fim = 2 ** (n + 1) - 1

        # Estratégia 1: Soma do anterior com uma potência de dois reduzida
        if n == 0:
            gerado = 1
        elif n == 1:
            gerado = resultados[-1] + 2
        else:
            incremento = 2 ** (n - 1) + (n % 2)  # Pequeno ajuste alternando
            gerado = resultados[-1] + incremento
            # Garante que não ultrapasse o Fim
            if gerado > fim:
                gerado = fim

        resultados.append(gerado)

        print(f"{n:<3} | {inicio:<15} | {fim:<18} | {gerado:<20}")

if __name__ == "__main__":
    gerar_tabela_tietze(9)
