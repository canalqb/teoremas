# Levy.py

# Tabela dada
tabela = [
    (1, 1, 1),
    (2, 3, 3),
    (4, 7, 7),
    (8, 8, 15),
    (16, 21, 31),
    (32, 49, 63),
    (64, 76, 127),
    (128, 224, 255),
    (256, 467, 511),
    (512, 514, 1023),
    (1024, 1155, 2047),
    (2048, 2683, 4095),
]

def pode_decompor(valor, mersennes):
    """
    Função recursiva que tenta decompor 'valor' em soma dos números de Mersenne fornecidos.
    Retorna (True, lista_de_componente) se possível, (False, []) se não.
    """
    if valor == 0:
        return True, []
    if valor < 0 or not mersennes:
        return False, []

    m = mersennes[0]

    # Tentar usar m
    usar_m, lista_com_m = pode_decompor(valor - m, mersennes)
    if usar_m:
        return True, [m] + lista_com_m

    # Tentar sem usar m
    return pode_decompor(valor, mersennes[1:])

def validate_table(table):
    for inicio, meio, fim in table:
        assert fim == 2 * inicio - 1, f"Fim {fim} não corresponde a 2*Inicio-1 para Inicio={inicio}"
        assert inicio <= meio <= fim, f"Meio {meio} fora do intervalo [{inicio}, {fim}]"

        mersennes = [2**k - 1 for k in range(1, fim.bit_length() + 1) if 2**k - 1 <= fim]
        mersennes.sort(reverse=True)

        pode, decomposicao = pode_decompor(meio, mersennes)

        print(f"Inicio: {inicio}, Meio: {meio}, Fim: {fim}")
        if pode:
            print(f"Decomposição de {meio} em soma de Mersennes <= {fim}: {decomposicao}")
        else:
            print(f"Não foi possível decompor {meio} em soma de Mersennes <= {fim}")
        print("-" * 40)

        assert pode, f"Meio {meio} não decompõe completamente em Mersennes menores ou iguais que {fim}"

def decompor_intervalo(inicio, fim):
    """
    Decompõe e imprime a decomposição de todos os números entre 'inicio' e 'fim'
    em soma de números de Mersenne ≤ fim.
    """
    mersennes = [2**k - 1 for k in range(1, fim.bit_length() + 1) if 2**k - 1 <= fim]
    mersennes.sort(reverse=True)

    print(f"Decompondo todos os números de {inicio} até {fim} em soma de Mersennes ≤ {fim}:")
    print("-" * 60)
    for num in range(inicio, fim + 1):
        pode, decomposicao = pode_decompor(num, mersennes)
        if pode:
            print(f"{num}: {decomposicao}")
        else:
            print(f"{num}: Não foi possível decompor.")
    print("-" * 60)
    
if __name__ == "__main__": 
    validate_table(tabela)
    decompor_intervalo(1, 4095)
 
