#!/usr/bin/env python3
"""
Script corrigido para gerar dados do Puzzle 71 com WIF C correto
"""

import json
import hashlib
import base58
import csv

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
    """Gera WIF C (compressed) - formato correto para chaves comprimidas"""
    k_bytes = k.to_bytes(32, 'big')
    # Prefix 0x80 + 32 bytes private key + 0x01 (compressed indicator) + 4 bytes checksum
    extended_key = b'\x80' + k_bytes + b'\x01'
    checksum = hashlib.sha256(hashlib.sha256(extended_key).digest()).digest()[:4]
    wif = base58.b58encode(extended_key + checksum)
    return wif.decode()

def main():
    print("=" * 70)
    print("Geração corrigida de dados para Puzzle 71 (WIF C)")
    print("=" * 70)
    print()
    
    secp = Secp256k1()
    
    # === GERAR HASH160 PARA 51-bit (2^51 a 2^52-1) ===
    print("Gerando hash160 para 51-bit...")
    base_51 = 2**51
    data_51bit = []
    
    for i in range(10000):
        if i % 2000 == 0:
            print(f"   Progresso: {i}/10000")
        k = base_51 + i
        P = secp.scalar_multiply(k, secp.G)
        h160 = hash160(compress_pubkey(P)).hex()
        wif = private_key_to_wif_compressed(k)
        data_51bit.append({
            'index': i + 1,
            'k_he': hex(k),
            'hash160': h160,
            'wif': wif
        })
    
    # Salvar JSON
    json_path = r"C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1/puzzle71_hash160_51bit.json"
    with open(json_path, 'w') as f:
        json.dump(data_51bit, f, indent=2)
    print(f"✓ JSON salvo: {json_path}")
    
    # Salvar TXT (apenas WIFs)
    txt_path = r"C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1/puzzle71_wif_51bit.txt"
    with open(txt_path, 'w') as f:
        for item in data_51bit:
            f.write(item['wif'] + '\n')
    print(f"✓ TXT salvo: {txt_path}")
    
    # === GERAR AMOSTRA PARA 71-bit ===
    print()
    print("Gerando amostra para 71-bit (2^70 a 2^71-1)...")
    base_71 = 2**70
    sample_71bit = []
    
    for i in range(10):
        k = base_71 + i
        P = secp.scalar_multiply(k, secp.G)
        h160 = hash160(compress_pubkey(P)).hex()
        wif = private_key_to_wif_compressed(k)
        sample_71bit.append({
            'k': hex(k),
            'hash160': h160,
            'wif': wif
        })
    
    # Salvar JSON 71-bit sample
    json_71bit_path = r"C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1/puzzle71_hash160_71bit_sample.json"
    with open(json_71bit_path, 'w') as f:
        json.dump(sample_71bit, f, indent=2)
    print(f"✓ JSON 71-bit salvo: {json_71bit_path}")
    
    # Salvar TXT 71-bit sample
    txt_71bit_path = r"C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1/puzzle71_wif_71bit_sample.txt"
    with open(txt_71bit_path, 'w') as f:
        for item in sample_71bit:
            f.write(item['wif'] + '\n')
    print(f"✓ TXT 71-bit salvo: {txt_71bit_path}")
    
    print()
    print("=" * 70)
    print("Execução concluída com WIF C (compressed format)")
    print("=" * 70)

if __name__ == "__main__":
    main()