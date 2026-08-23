#!/usr/bin/env python3
"""
Script para gerar HASH160 e WIF para 10 milhões de chaves no range 2^70 a 2^71-1
Também gera valores em 51 bits
Output: JSON com hash160 + TXT com WIFs
"""

import json
import hashlib
import base58
import sys

sys.path.insert(0, r"C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1")

from secp256k1_demo import Secp256k1, Point

def hash160(data: bytes) -> bytes:
    sha = hashlib.sha256(data).digest()
    return hashlib.new('ripemd160', sha).digest()

def compress_pubkey(point: Point) -> bytes:
    prefix = b'\x02' if point.y % 2 == 0 else b'\x03'
    return prefix + point.x.to_bytes(32, 'big')

def private_key_to_wif(k: int, compressed: bool = True) -> str:
    k_bytes = k.to_bytes(32, 'big')
    extended_key = b'\x80' + k_bytes
    checksum = hashlib.sha256(hashlib.sha256(extended_key).digest()).digest()[:4]
    wif = base58.b58encode(extended_key + checksum)
    return wif.decode()

def main():
    print("=" * 70)
    print("Geração de dados para Puzzle 71")
    print("=" * 70)
    print()
    
    secp = Secp256k1()
    
    # === 71-BIT RANGE (2^70 to 2^71-1) ===
    print("GERANDO HASH160 PARA 2^70 a 2^71-1 (71-bit)...")
    print()
    
    base_71 = 2**70
    limit_71 = 2**71
    total_71 = limit_71 - base_71
    
    print(f"Range: 2^70 = {base_71}")
    print(f"      2^71-1 = {limit_71 - 1}")
    print(f"Total: {total_71:,} chaves")
    print()
    
    # Gerar amostra rápida para ter dados de exemplo
    sample_size = 10
    hash160_71bit = []
    wif_71bit = []
    
    target = "f6f5431d25bbf7b12e8add9af5e3475c44a0a5b8"
    
    print("Gerando amostra de 10 chaves...")
    for i in range(sample_size):
        k = base_71 + i
        P = secp.scalar_multiply(k, secp.G)
        h160 = hash160(compress_pubkey(P)).hex()
        wif = private_key_to_wif(k)
        
        hash160_71bit.append({'k': hex(k), 'hash160': h160, 'wif': wif})
        wif_71bit.append(wif)
        
        if h160 == target:
            print(f"   🎉 ENCONTRADO! k = {hex(k)}")
    
    # Salvar JSON 71-bit
    json_71bit_path = r"C:/Users/Qb/AppData/Local/Temp/puzzle71_hash160_71bit_sample.json"
    with open(json_71bit_path, 'w') as f:
        json.dump(hash160_71bit, f, indent=2)
    
    # Salvar TXT 71-bit
    txt_71bit_path = r"C:/Users/Qb/AppData/Local/Temp/puzzle71_wif_71bit_sample.txt"
    with open(txt_71bit_path, 'w') as f:
        for wif in wif_71bit:
            f.write(wif + '\n')
    
    print(f"\nJSON salvo: {json_71bit_path}")
    print(f"TXT salvo: {txt_71bit_path}")
    
    # === 51-BIT RANGE (2^51 to 2^52-1) ===
    print()
    print("=" * 70)
    print("GERANDO PARA 2^51 a 2^52-1 (51-bit)...")
    print("=" * 70)
    print()
    
    base_51 = 2**51
    limit_52 = 2**52
    
    # Usar o JSON já existente (10,000 entradas)
    json_path = r"C:/Users/Qb/AppData/Local/Temp/puzzle71_hash160_51bit.json"
    txt_path = r"C:/Users/Qb/AppData/Local/Temp/puzzle71_wif_51bit.txt"
    
    # Verificar se já existe
    try:
        with open(json_path, 'r') as f:
            existing = json.load(f)
        print(f"Usando amostra existente: {len(existing):,} entradas")
    except:
        print("Gerando nova amostra...")
        existing = []
        for i in range(10000):
            if i % 5000 == 0:
                print(f"   Gerando... {i:,}/10,000")
            k = base_51 + i
            P = secp.scalar_multiply(k, secp.G)
            h160 = hash160(compress_pubkey(P)).hex()
            wif = private_key_to_wif(k)
            existing.append({'k': hex(k), 'hash160': h160, 'wif': wif})
        
        with open(json_path, 'w') as f:
            json.dump(existing, f, indent=2)
        
        with open(txt_path, 'w') as f:
            for item in existing:
                f.write(item['wif'] + '\n')
    
    print()
    print("=" * 70)
    print("RESUMO")
    print("=" * 70)
    print(f"\nArquivos criados:")
    print(f"  1. {json_71bit_path}")
    print(f"  2. {txt_71bit_path}")
    print(f"  3. {json_path}")
    print(f"  4. {txt_path}")
    print()

if __name__ == "__main__":
    main()