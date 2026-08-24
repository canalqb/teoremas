#!/usr/bin/env python3
"""
Script de busca otimizado para Puzzle 71
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

print("Iniciando busca por Puzzle 71...")
print(f"Target: {target}")
start = time.time()

for i in range(10000000):
    k = base + i
    P = secp.scalar_multiply(k, secp.G)
    h160 = hash160_compressed(P.x, P.y)
    
    if h160 == target:
        print(f"✓ ENCONTRADO!")
        print(f"K = {hex(k)}")
        print(f"WIF = {wif_compressed(k)}")
        print(f"Iteração = {i}")
        break
    
    if i % 1000000 == 0 and i > 0:
        print(f"{i:,} verificados ({i/elapsed:.0f} chaves/s)")

print("Busca concluída - nenhum match encontrado")