from math import comb

def mersenne_numbers_up_to(max_val):
    mersennes = []
    p = 1
    while True:
        m = 2**p - 1
        if m > max_val:
            break
        mersennes.append(m)
        p += 1
    return mersennes

def pascal_row(n):
    """Retorna a n-ésima linha do triângulo de Pascal (linha 0 é [1])"""
    return [comb(n, k) for k in range(n+1)]

def identificar_numero(n):
    """
    Para um dado n, retorna um número dentro do intervalo [2^n, 2^{n+1} - 1]
    usando combinação entre potências de 2, números de Mersenne, e coeficientes de Pascal.
    """
    inicio = 2**n
    fim = 2**(n+1) - 1
    mersennes = mersenne_numbers_up_to(fim)
    linha_pascal = pascal_row(n)

    # Uma forma simples: somar potências de 2 ponderadas pelos coeficientes de Pascal,
    # limitado ao intervalo
    # Exemplo: soma_i (coef_pascal[i] * 2^i)
    soma = sum([linha_pascal[i] * (2**i) for i in range(len(linha_pascal))])
    
    # Ajustar soma para ficar dentro do intervalo
    if soma < inicio:
        soma = inicio
    elif soma > fim:
        soma = fim
    
    return {
        "n": n,
        "intervalo": (inicio, fim),
        "mersennes_no_intervalo": [m for m in mersennes if inicio <= m <= fim],
        "linha_pascal": linha_pascal,
        "numero_identificado": soma
    }

def main():
    resultados = []
    for n in range(11):
        res = identificar_numero(n)
        resultados.append(res)
    return resultados

if __name__ == "__main__":
    resultados = main()
    for res in resultados:
        print(f"n={res['n']}, intervalo={res['intervalo']}, mersennes no intervalo={res['mersennes_no_intervalo']}")
        print(f"linha Pascal: {res['linha_pascal']}")
        print(f"número identificado: {res['numero_identificado']}")
        print("-" * 40)
