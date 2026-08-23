#!/usr/bin/env python3
"""
Script de busca rápida para Puzzle 71
Verifica todos os 10M valores do range 2^70 a 2^71-1
"""

import hashlib
import base58
import time
import sys
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

target = "f6f5431d255bbf7b12e8add9af5e3475c44a0a5b8"
base = 2**70

print("=" * 70)
print("PUZZLE 71 - Busca Brute Force 10 Milhões de Chaves")
print("=" * 70)
print(f"Target: {target}")
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
        print(f"Iteração = {i}")
        print(f"Tempo = {elapsed:.2f}s")
        found = True
        break
    
    if i % 500000 == 0 and i > 0:
        elapsed = time.time() - start
        rate = i / elapsed
        print(f"{i:,} verificados | {rate:,.0f} chaves/s")

elapsed = time.time() - start
print()
print("=" * 70)
print(f"Busca concluída em {elapsed:.2f}s")
print(f"Rate: {10000000/elapsed:,.0f} chaves/segundo")
if not found:
    print("Nenhum match encontrado - verificar se o target está correto")