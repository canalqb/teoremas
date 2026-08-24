def imprimir_intervalo_e_destacar(numero_destaque, inicio, fim):
    """
    Imprime números no intervalo [inicio, fim].
    Destaca um número específico.
    
    Args:
        numero_destaque (int): Número a ser destacado na impressão.
        inicio (int): Início do intervalo.
        fim (int): Fim do intervalo.
    """
    contador = 0
    for n in range(inicio, fim + 1):
        if n == numero_destaque:
            print(f"{n} <-- número destacado!")
        else:
            print(n)
        contador += 1
    print(f"Total: {contador} números gerados")

# Exemplo: destacar um número próximo a 2048 * sqrt(2)
import math
numero_destaque = round(2048 * math.sqrt(2))  # aproximação de sqrt(2)*2048
imprimir_intervalo_e_destacar(numero_destaque, 2048, 4096)
