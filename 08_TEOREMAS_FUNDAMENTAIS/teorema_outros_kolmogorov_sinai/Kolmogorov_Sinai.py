import secrets
import math
from collections import Counter

def gerar_bits(n_bits):
    """Gera uma sequência binária com n_bits usando secrets."""
    n_bytes = (n_bits + 7) // 8
    data = secrets.token_bytes(n_bytes)
    bits = ''.join(f'{byte:08b}' for byte in data)
    return bits[:n_bits]

def entropia_bloco(bits, k):
    """Calcula a entropia de Shannon para blocos de tamanho k."""
    # Ajusta o comprimento para múltiplo de k
    tamanho_util = len(bits) - (len(bits) % k)
    blocos = [bits[i:i+k] for i in range(0, tamanho_util, k)]
    total = len(blocos)
    contagem = Counter(blocos)
    entropia = -sum((freq/total) * math.log2(freq/total) for freq in contagem.values())
    return entropia, len(contagem), total

def estimar_entropia_ks(n_bits=100_000, k_max=16):
    bits = gerar_bits(n_bits)
    print(f"\n📊 Análise de Entropia com base em Kolmogorov–Sinai")
    print(f"Total de bits gerados: {len(bits)}")
    print(f"Fonte: secrets.token_bytes\n")
    
    print(" k | Blocos únicos | Total blocos | H_k (bits) | H_k / k")
    print("---|----------------|---------------|-------------|--------")
    
    for k in range(1, k_max + 1):
        h_k, blocos_unicos, total_blocos = entropia_bloco(bits, k)
        taxa_entropia = h_k / k
        print(f"{k:2d} | {blocos_unicos:14d} | {total_blocos:13d} | {h_k:11.6f} | {taxa_entropia:6.4f}")

# Executar
if __name__ == "__main__":
    estimar_entropia_ks(n_bits=100_000, k_max=16)
