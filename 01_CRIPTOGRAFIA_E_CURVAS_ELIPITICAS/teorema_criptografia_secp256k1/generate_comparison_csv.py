#!/usr/bin/env python3
"""
Geração de dados para comparação hash160 pública x privada
Puzzle 71 - Output em CSV com separador ;
"""

import json
import hashlib
import base58
import sys
sys.path.insert(0, r"C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1")

from secp256k1_demo import Secp256k1

secp = Secp256k1()

def hash160_from_pubkey(x: int, y: int) -> tuple:
    """Gera hash160 do pubkey, retorna hash e separador par/ímpar"""
    prefix = b'\x02' if y % 2 == 0 else b'\x03'
    pubkey = prefix + x.to_bytes(32, 'big')
    sha = hashlib.sha256(pubkey).digest()
    ripemd = hashlib.new('ripemd160', sha).digest()
    return ripemd.hex(), 'par' if y % 2 == 0 else 'impar'

def private_key_to_wif_compressed(k: int) -> str:
    k_bytes = k.to_bytes(32, 'big')
    extended = b'\x80' + k_bytes + b'\x01'
    checksum = hashlib.sha256(hashlib.sha256(extended).digest()).digest()[:4]
    return base58.b58encode(extended + checksum).decode()

def main():
    target = "f6f5431d255bbf7b12e8add9af5e3475c44a0a5b8"
    base = 2**70
    
    print("Gerando dados para análise de padrões...")
    print(f"Target hash160: {target}")
    print(f"Gerando amostras de 100.000 valores")
    print()
    
    csv_path = r"C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1/puzzle71_all_data_comparison.csv"
    
    with open(csv_path, 'w', encoding='utf-8') as f:
        # Header com separador ;
        f.write("index;k_hex;k_dec;hash160;wif;y_parity;match\n")
        
        for i in range(100000):
            k = base + i
            P = secp.scalar_multiply(k, secp.G)
            h160, parity = hash160_from_pubkey(P.x, P.y)
            wif = private_key_to_wif_compressed(k)
            match = "SIM" if h160 == target else "NÃO"
            
            # CSV com ; separador
            f.write(f"{i+1};{hex(k)[2:]};{k};{h160};{wif};{parity};{match}\n")
            
            if (i+1) % 10000 == 0:
                print(f"Progresso: {i+1:,} / 100,000")
    
    print()
    print(f"✓ Dados salvos em: puzzle71_all_data_comparison.csv")
    print("Formato: CSV com separador ;")
    print("Colunas: index; k_hex; k_dec; hash160; wif; y_parity; match")

if __name__ == "__main__":
    main()