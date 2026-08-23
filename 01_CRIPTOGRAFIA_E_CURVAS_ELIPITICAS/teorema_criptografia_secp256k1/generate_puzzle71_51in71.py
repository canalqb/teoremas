#!/usr/bin/env python3
"""
Script corrigido para gerar dados do Puzzle 71
- Números de 51 BITS dentro do range 71-bit (2^70 a 2^71-1)
- Exemplo: 2^70 + 2^51, 2^70 + 2*2^51, etc. (10 amostras)
"""

import json
import hashlib
import base58

# Importar secp256k1 do diretorio correto
import sys
sys.path.insert(0, r"C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1")

from secp256k1_demo import Secp256k1, Point

def hash160(data: bytes) -> bytes:
    sha = hashlib.sha256(data).digest()
    return hashlib.new('ripemd160', sha).digest()

def compress_pubkey(point: Point) -> bytes:
    prefix = b'\x02' if point.y % 2 == 0 else b'\x03'
    return prefix + point.x.to_bytes(32, 'big')

def private_key_to_wif_compressed(k: int) -> str:
    """Gera WIF C (compressed)"""
    k_bytes = k.to_bytes(32, 'big')
    extended_key = b'\x80' + k_bytes + b'\x01'
    checksum = hashlib.sha256(hashlib.sha256(extended_key).digest()).digest()[:4]
    wif = base58.b58encode(extended_key + checksum)
    return wif.decode()

def main():
    print("=" * 70)
    print("Gerando dados para Puzzle 71 - 51-bit dentro do range 71-bit")
    print("=" * 70)
    print()
    
    secp = Secp256k1()
    
    # Range 71-bit: 2^70 a 2^71-1
    base_71 = 2**70
    bit_51 = 2**51
    
    # Gerar amostras de números de 51 bits dentro do range 71-bit
    sample_data = []
    
    print("Gerando amostras de 51-bit dentro do range 71-bit (2^70 a 2^71-1)...")
    print()
    
    for i in range(1, 11):
        # Números de 51 bits dentro do range 71-bit
        # Exemplo: 2^70 + i * 2^51
        k = base_71 + (i * bit_51)
        
        P = secp.scalar_multiply(k, secp.G)
        h160 = hash160(compress_pubkey(P)).hex()
        wif = private_key_to_wif_compressed(k)
        
        sample_data.append({
            'index': i,
            'k': hex(k),
            'bits': 71,  # Todos são do range 71-bit
            'k_bits': 51,  # Mas usando offset de 51 bits
            'hash160': h160,
            'wif': wif,
            'decimal': k
        })
        
        print(f"{i}|k = 2^70 + {i}*2^51 = {k}")
        print(f"   hex: {hex(k)}")
        print(f"   WIF: {wif}")
        print(f"   hash160: {h160}")
        print()
    
    # Salvar JSON
    json_path = r"C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1/puzzle71_51bits_in_71bit_range.json"
    with open(json_path, 'w') as f:
        json.dump(sample_data, f, indent=2)
    print(f"✓ JSON salvo: {json_path}")
    
    # Salvar TXT (apenas WIFs)
    txt_path = r"C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1/puzzle71_51bits_in_71bit_wif.txt"
    with open(txt_path, 'w') as f:
        for item in sample_data:
            f.write(item['wif'] + '\n')
    print(f"✓ TXT salvo: {txt_path}")
    
    print()
    print("=" * 70)
    print("Execução concluída!")
    print("10 amostras de números de 51 bits dentro do range 71-bit gerados")
    print("=" * 70)

if __name__ == "__main__":
    main()