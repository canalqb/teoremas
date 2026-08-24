# seifert_van_kampen_mersenne.py

def intervalo_potencia(n):
    """Retorna intervalo simbólico U para 2^n até 2^{n+1} - 1"""
    return list(range(2**n, 2**(n+1)))

def numero_mersenne(n):
    """Retorna o número de Mersenne: 2^n - 1"""
    return 2**n - 1

def aplicar_teorema_svkm(n):
    # Espaços U e V
    U = intervalo_potencia(n)
    V = intervalo_potencia(n + 1)
    
    # Interseção simbólica
    intersecao = [numero_mersenne(n + 1)]  # Elemento que conecta os dois conjuntos
    
    # União via SVK (colagem na interseção)
    espaco_colado = list(set(U + V))  # União sem duplicatas
    
    return {
        "n": n,
        "U": U,
        "V": V,
        "Intersecao": intersecao,
        "EspacoColado": espaco_colado
    }

def imprimir_resultado(resultado):
    print(f"=== Seifert–van Kampen simbólico para n = {resultado['n']} ===")
    print(f"U               = {resultado['U']}")
    print(f"V               = {resultado['V']}")
    print(f"U ∩ V (Mersenne)= {resultado['Intersecao']}")
    print(f"U ∪ V (colado)  = {sorted(resultado['EspacoColado'])}")
    print()

if __name__ == "__main__":
    for n in range(3):
        resultado = aplicar_teorema_svkm(n)
        imprimir_resultado(resultado)
