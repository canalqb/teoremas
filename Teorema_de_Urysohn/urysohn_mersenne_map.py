# urysohn_mersenne_map.py

def urysohn_aproximado(n_max=9, ponto_f=0.7):
    """
    Gera uma tabela com base na aplicação discreta do Teorema de Urysohn,
    interpolando suavemente entre 2^N e 2^(N+1) - 1.
    
    A função f(x) = (x - inicio) / (fim - inicio) simula a separação contínua
    entre conjuntos disjuntos {inicio} e {fim}, e o valor "esperado" é onde f(x) ≈ ponto_f.
    
    ponto_f deve estar em (0, 1). Por padrão, usamos 0.7.
    """
    if not (0 < ponto_f < 1):
        raise ValueError("O ponto de interpolação f deve estar entre 0 e 1 (ex: 0.7)")

    print(f"{'N':>2} | {'Início (2^N)':>13} | {'Estimado f⁻¹({ponto_f})':>21} | {'Fim (2^(N+1)-1)':>17}")
    print("-" * 63)

    for n in range(n_max + 1):
        inicio = 2 ** n
        fim = 2 ** (n + 1) - 1
        intervalo = fim - inicio

        # Aplicação invertida da função f(x) = (x - inicio) / (fim - inicio)
        # Queremos f(x) = ponto_f ⇒ x = inicio + ponto_f * (fim - inicio)
        estimado = int(round(inicio + ponto_f * intervalo))

        print(f"{n:>2} | {inicio:>13} | {estimado:>21} | {fim:>17}")

if __name__ == "__main__":
    urysohn_aproximado()
