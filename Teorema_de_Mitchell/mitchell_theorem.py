# mitchell_theorem.py

def bitcount(n):
    """Conta o número de bits ligados em n"""
    return bin(n).count('1')

def mitchell_function(start, end):
    """Aplica a função de Mitchell: soma do bitcount no intervalo [start, end)"""
    return sum(bitcount(i) for i in range(start, end))

def main():
    dados = [
        (1, 2, 1),
        (2, 4, 3),
        (4, 8, 7),
        (8, 16, 8),
        (16, 32, 21),
        (32, 64, 49),
        (64, 128, 76),
        (128, 256, 224),
    ]

    print(f"{'Início':>6} | {'Fim':>6} | {'Esperado':>9} | {'Calculado':>10}")
    print("-" * 42)
    for inicio, fim, esperado in dados:
        calculado = mitchell_function(inicio, fim)
        print(f"{inicio:6} | {fim:6} | {esperado:9} | {calculado:10}")

if __name__ == "__main__":
    main()
