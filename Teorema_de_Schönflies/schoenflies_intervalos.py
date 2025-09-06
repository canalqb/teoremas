# schoenflies_intervalos.py

def inicio_fim(N):
    """Retorna o intervalo [2^N, 2^(N+1)-1]."""
    inicio = 2 ** N
    fim = (2 ** (N + 1)) - 1
    return inicio, fim

def valor_teorema(N):
    """
    Função que tenta gerar um valor dentro do intervalo [2^N, 2^(N+1)-1]
    apenas com operações envolvendo potências de 2, para se aproximar
    do 'Esperado pelo teorema' (sem usar essa coluna diretamente).
    
    Para isso, vamos usar uma combinação linear simples:
    valor = inicio + (fim - inicio) // 2 + offset
    
    Onde offset será calculado a partir de alguma função relacionada a N,
    como por exemplo a soma dos dígitos binários de N vezes alguma potência de 2.
    """
    inicio, fim = inicio_fim(N)
    
    # Vamos usar a soma dos bits em N para ajustar o valor
    soma_bits = bin(N).count('1')
    offset = soma_bits * (2 ** (N//2)) if N > 0 else 0
    
    valor = inicio + (fim - inicio) // 2 + offset
    
    # Ajustar para garantir que valor não ultrapasse fim
    if valor > fim:
        valor = fim
    
    return valor

def gerar_tabela(max_n):
    print(f"{'N':>2} | {'Inicio (2^N)':>12} | {'Valor Teorema':>15} | {'Fim (2^(N+1)-1)':>15}")
    print("-" * 55)
    for N in range(max_n + 1):
        inicio, fim = inicio_fim(N)
        valor = valor_teorema(N)
        print(f"{N:>2} | {inicio:>12} | {valor:>15} | {fim:>15}")

def main():
    max_n = 9
    gerar_tabela(max_n)

if __name__ == "__main__":
    main()
