#!/usr/bin/env python3
"""
Script para gerar HASH160 e WIF para Puzzle 71
Range 51-bit: 2^51 a 2^52-1 (10,000 amostras)
Range 71-bit: 2^70 a 2^71-1 (10 amostras)
"""

import sys
import json
import hashlib

sys.path.insert(0, "C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1")

try:
    import base58
except ImportError:
    # Implementação inline de base58 se a biblioteca não estiver disponível
    import string
    ALPHABET = string.ascii_letters + string.digits + '+/'
    BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    
    class Base58:
        @staticmethod
        def encode(data):
            if isinstance(data, str):
                data = data.encode('utf-8')
            
            # Contar zeros à esquerda
            leading_zeros = 0
            for byte in data:
                if byte == 0:
                    leading_zeros += 1
                else:
                    break
            
            # Converter para inteiro
            num = int.from_bytes(data, 'big')
            
            # Converter para base58
            result = ''
            while num > 0:
                num, remainder = divmod(num, 58)
                result = BASE58_ALPHABET[remainder] + result
            
            # Adicionar caracteres '1' para cada zero à esquerda
            return '1' * leading_zeros + result
    
    base58 = Base58()

from secp256k1_demo import Secp256k1, Point

def hash160(data: bytes) -> bytes:
    """SHA256 + RIPEMD160"""
    sha = hashlib.sha256(data).digest()
    return hashlib.new('ripemd160', sha).digest()

def compress_pubkey(point: Point) -> bytes:
    """Compress pubkey - 33 bytes"""
    prefix = b'\x02' if point.y % 2 == 0 else b'\x03'
    return prefix + point.x.to_bytes(32, 'big')

def private_key_to_wif_compressed(k: int) -> str:
    """Private key para WIF C (comprimido)"""
    k_bytes = k.to_bytes(32, 'big')
    # WIF version = 0x80
    extended_key = b'\x80' + k_bytes
    # Adiciona byte de compression flag (01) nas chaves comprimidas
    extended_with_flag = extended_key + b'\x01'
    # Checksum duplo SHA256
    checksum = hashlib.sha256(hashlib.sha256(extended_with_flag).digest()).digest()[:4]
    # Codifica em base58
    wif = base58.encode(extended_with_flag + checksum)
    return wif

def main():
    print("=" * 70)
    print("Geração WIF C para Puzzle 71")
    print("=" * 70)
    
    secp = Secp256k1()
    
    # ========================================
    # PARTE 1: 51-BIT RANGE (2^51 a 2^52-1)
    # ========================================
    print("\nGerando 10,000 amostras para 2^51 a 2^52-1...")
    
    base_51 = 2**51
    hash160_51bit = []
    wif_51bit = []
    
    for i in range(10000):
        if i % 2000 == 0:
            print(f"  Progresso: {i:,}/10,000")
        
        k = base_51 + i
        P = secp.scalar_multiply(k, secp.G)
        h160 = hash160(compress_pubkey(P)).hex()
        wif = private_key_to_wif_compressed(k)
        
        hash160_51bit.append({
            'index': i,
            'k': hex(k),
            'hash160': h160,
            'wif': wif
        })
        wif_51bit.append(f"{i}|{wif}")
    
    # Salva JSON
    json_path = "C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1/puzzle71_hash160_51bit.json"
    with open(json_path, 'w') as f:
        json.dump(hash160_51bit, f, indent=2)
    print(f"  JSON salvo: {json_path}")
    
    # Salva TXT
    txt_path = "C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1/puzzle71_wif_51bit.txt"
    with open(txt_path, 'w') as f:
        f.write('\n'.join(wif_51bit))
    print(f"  TXT salvo: {txt_path}")
    
    # ========================================
    # PARTE 2: 71-BIT RANGE (2^70 a 2^71-1)
    # ========================================
    print("\nGerando 10 amostras para 2^70 a 2^71-1...")
    
    base_71 = 2**70
    hash160_71bit = []
    wif_71bit = []
    
    target = "f6f5431d255bbf7b12e8add9af5e3475c44a0a5b8"
    
    for i in range(10):
        k = base_71 + i
        P = secp.scalar_multiply(k, secp.G)
        h160 = hash160(compress_pubkey(P)).hex()
        wif = private_key_to_wif_compressed(k)
        
        hash160_71bit.append({
            'index': i,
            'k': hex(k),
            'hash160': h160,
            'wif': wif
        })
        wif_71bit.append(f"{i}|{wif}")
        
        if h160 == target:
            print(f"  🎉 ENCONTRADO! k = {hex(k)}")
    
    # Salva JSON
    json_path = "C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1/puzzle71_hash160_71bit_sample.json"
    with open(json_path, 'w') as f:
        json.dump(hash160_71bit, f, indent=2)
    print(f"  JSON salvo: {json_path}")
    
    # Salva TXT
    txt_path = "C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1/puzzle71_wif_71bit_sample.txt"
    with open(txt_path, 'w') as f:
        f.write('\n'.join(wif_71bit))
    print(f"  TXT salvo: {txt_path}")
    
    # ========================================
    # RESUMO
    # ========================================
    print("\n" + "=" * 70)
    print("CONCLUSÃO")
    print("=" * 70)
    print(f"\nArquivos criados com WIF C (compressed):")
    print(f"  1. puzzle71_hash160_51bit.json         (10,000 entradas)")
    print(f"  2. puzzle71_wif_51bit.txt             (10,000 linhas)")
    print(f"  3. puzzle71_hash160_71bit_sample.json (10 entradas)")
    print(f"  4. puzzle71_wif_71bit_sample.txt      (10 linhas)")
    print()
    print("Formato dos arquivos TXT: <indice>|<WIF_C>")
    print("Exemplo: 0|KWdiBf89QgGbjEhKnhXJuH7LrciVrZi3qxGLkchTagWEWquHPtvw")

if __name__ == "__main__":
    main()