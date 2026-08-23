#!/usr/bin/env python3
"""
Busca incremental para Puzzle 71
Executa em lotes para evitar timeout
Lote atual: 100,000 a 200,000
"""

import hashlib
import base58
import sys
import time

sys.path.insert(0, r"C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1")

from secp256k1_demo import Secp256k1

secp = Secp256k1()

def hash160_compressed(x: int, y: int) -> str:
    prefix = b'\x02' if y % 2 == 0 else b'\x03'
    pubkey = prefix + x.to_bytes(32, 'big')
    sha = hashlib.sha256(pubkey).digest()
    return hashlib.new('ripemd160', sha).digest().hex()

def wif_compressed(k: int) -> str:
    ext = b'\x80' + k.to_bytes(32, 'big') + b'\x01'
    cksum = hashlib.sha256(hashlib.sha256(ext).digest()).digest()[:4]
    return base58.b58encode(ext + cksum).decode()

def main():
    target = "f6f5431d255bbf7b12e8add9af5e3475c44a0a5b8"
    base = 2**70
    
    # Lote: 100,000 a 200,000
    start_idx = 100000
    end_idx = 200000
    
    print(f"Iniciando lote: {start_idx:,} a {end_idx:,}")
    print(f"Target: {target}")
    
    start_time = time.time()
    
    for i in range(start_idx, end_idx):
        k = base + i
        P = secp.scalar_multiply(k, secp.G)
        h160 = hash160_compressed(P.x, P.y)
        
        if h160 == target:
            elapsed = time.time() - start_time
            print(f"\n✓ ENCONTRADO!")
            print(f"K = {hex(k)} ({k})")
            print(f"WIF = {wif_compressed(k)}")
            print(f"Índice = {i}")
            print(f"Tempo = {elapsed:.2f}s")
            
            # Salvar resultado
            with open("puzzle71_found.txt", "w") as f:
                f.write(f"K = {hex(k)}\n")
                f.write(f"WIF = {wif_compressed(k)}\n")
                f.write(f"Índice = {i}\n")
            return
        
        if i % 10000 == 0:
            elapsed = time.time() - start_time
            rate = i / elapsed if elapsed > 0 else 0
            print(f"{i:,} verificados | {rate:,.0f} chaves/s")
    
    elapsed = time.time() - start_time
    print(f"\nLote concluído em {elapsed:.2f}s")
    print(f"Próximo lote: {end_idx:,} a {end_idx + 100000:,}")

if __name__ == "__main__":
    main()