#!/usr/bin/env python3
"""
Busca corrigida para Puzzle 71
Target hash160 CORRIGIDO: f6f5431d255bbf7b12e8add9af5e3475c44a0a5b8 (40 chars)
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
    target = "f6f5431d255bbf7b12e8add9af5e3475c44a0a5b8"  # CORRIGIDO: 40 chars
    base = 2**70
    
    print("=" * 70)
    print("PUZZLE 71 - Busca Brute Force 10 Milhões de Chaves")
    print("=" * 70)
    print(f"Target: {target}")
    print(f"Comprimento: {len(target)} caracteres")
    print(f"Range: 2^70 a 2^71-1")
    print()
    
    start = time.time()
    found = False
    
    for i in range(10000000):
        k = base + i
        P = secp.scalar_multiply(k, secp.G)
        h160 = hash160_compressed(P.x, P.y)
        
        if h160 == target:
            elapsed = time.time() - start
            print("\n✓ ENCONTRADO!")
            print(f"K = {hex(k)}")
            print(f"WIF = {wif_compressed(k)}")
            print(f"Índice = {i}")
            print(f"Tempo = {elapsed:.2f}s")
            found = True
            break
        
        if i % 1000000 == 0 and i > 0:
            elapsed = time.time() - start
            rate = i / elapsed
            remaining = (10000000 - i) / rate if rate > 0 else 0
            print(f"{i:,} verificados | {rate:,.0f} chaves/s | Restante: {remaining:.0f}s")
    
    elapsed = time.time() - start
    print()
    print("=" * 70)
    print(f"Busca concluída em {elapsed:.2f}s")
    print(f"Rate: {10000000/elapsed:,.0f} chaves/segundo")
    if not found:
        print("Nenhum match encontrado - continue a busca ou verifique o target")

if __name__ == "__main__":
    main()