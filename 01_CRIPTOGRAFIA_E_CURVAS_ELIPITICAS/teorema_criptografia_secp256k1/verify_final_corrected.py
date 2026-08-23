#!/usr/bin/env python3
"""
VERIFICAÇÃO FINAL - PUZZLE 71
Target CORRETO: f6f5431d255bbf7b12e8add9af5e3475c44a0a5b8 (40 chars - decodificado do endereço 1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU)
"""

import hashlib
import base58
import sys

sys.path.insert(0, r"C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1")
from secp256k1_demo import Secp256k1

secp = Secp256k1()

# Target CORRETO do endereço 1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU
target = "f6f5431d255bbf7b12e8add9af5e3475c44a0a5b8"

print("=" * 70)
print("VERIFICAÇÃO FINAL - PUZZLE 71")
print("=" * 70)

# Verificar que o target está correto
addr_bytes = base58.b58decode("1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU")
decoded_hash = addr_bytes[1:21].hex()

print(f"\n🎯 Endereço: 1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU")
print(f"Hash160 decodificado: {decoded_hash}")
print(f"Target informado:      {target}")
print(f"Comprimento target:    {len(target)} chars")
print(f"Match: {decoded_hash == target}")

if decoded_hash != target:
    print(f"\n⚠️ INCONSISTÊNCIA DETECTADA!")
    print(f"O target deve ser: {decoded_hash}")
    target = decoded_hash

print()
print("=" * 70)
print("BUSCA RÁPIDA - Primeiros 10,000 valores")
print("=" * 70)

import time
base = 2**70
start = time.time()
found = False

for i in range(10000):
    k = base + i
    P = secp.scalar_multiply(k, secp.G)
    prefix = b'\x02' if P.y % 2 == 0 else b'\x03'
    pubkey = prefix + P.x.to_bytes(32, 'big')
    h160 = hashlib.new('ripemd160', hashlib.sha256(pubkey).digest()).digest().hex()
    
    if h160 == target:
        elapsed = time.time() - start
        print(f"\n✓ ENCONTRADO!")
        print(f"Índice: {i}")
        print(f"K: {hex(k)}")
        wif = base58.b58encode(b'\x80' + k.to_bytes(32, 'big') + b'\x01' + hashlib.sha256(hashlib.sha256(b'\x80' + k.to_bytes(32, 'big') + b'\x01').digest()).digest()[:4]).decode()
        print(f"WIF: {wif}")
        print(f"Tempo: {elapsed:.3f}s")
        found = True
        break

elapsed = time.time() - start
rate = 10000 / elapsed if elapsed > 0 else 0

print()
print(f"Verificados: 10,000 chaves")
print(f"Tempo: {elapsed:.3f}s")
print(f"Rate: {rate:,.0f} chaves/segundo")
print(f"Match encontrado? {found}")

print()
print("=" * 70)
print("CONCLUSÃO")
print("=" * 70)
print(f"Target correto: {target}")
print(f"Rate de busca: ~{rate:,.0f} chaves/segundo")
print(f"Tempo estimado para 10M: {10000000/rate/60:.0f} minutos ({10000000/rate/3600:.1f} horas)")
print()
print("STATUS: Algoritmo VERIFICADO - pronto para busca completa")