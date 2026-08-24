#!/usr/bin/env python3
"""
Busca brute force para Puzzle 71 - 10 milhões de verificações
Hash160 target: f6f5431d255bbf7b12e8add9af5e3475c44a0a5b8
Range: 2^70 a 2^71-1 (71-bit numbers)
"""

import json
import hashlib
import base58
import time
import sys
sys.path.insert(0, r"C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1")

from secp256k1_demo import Secp256k1

def hash160_from_bytes(data: bytes) -> str:
    sha = hashlib.sha256(data).digest()
    return hashlib.new('ripemd160', sha).hexdigest()

def compress_pubkey(x: int, y: int) -> bytes:
    prefix = b'\x02' if y % 2 == 0 else b'\x03'
    return prefix + x.to_bytes(32, 'big')

def wif_compressed(k: int) -> str:
    k_bytes = k.to_bytes(32, 'big')
    extended = b'\x80' + k_bytes + b'\x01'
    checksum = hashlib.sha256(hashlib.sha256(extended).digest()).digest()[:4]
    return base58.b58encode(extended + checksum).decode()

def main():
    secp = Secp256k1()
    target = "f6f5431d255bbf7b12e8add9af5e3475c44a0a5b8"
    
    start = 2**70
    end = 2**71
    total = end - start
    
    print("=" * 70)
    print(f"BUSCA BRUTE FORCE - Puzzle 71")
    print(f"Target: {target}")
    print(f"Range: 2^70 a 2^71-1")
    print(f"Total de chaves a testar: {total:,}")
    print("=" * 70)
    print()
    
    # Testar 10 milhões de chaves
    max_checks = 10_000_000
    found = []
    start_time = time.time()
    
    print(f"Testando primeiros {max_checks:,} valores...")
    
    for i in range(max_checks):
        k = start + i
        P = secp.scalar_multiply(k, secp.G)
        h160 = hash160_from_bytes(compress_pubkey(P.x, P.y))
        
        if h160 == target:
            wif = wif_compressed(k)
            found.append({
                'k': hex(k),
                'wif': wif,
                'hash160': h160,
                'decimal': k
            })
            print(f"\n✓✓✓ ENCONTRADO! ✓✓✓")
            print(f"k = {hex(k)}")
            print(f"WIF = {wif}")
            print(f"hash160 = {h160}")
            print()
        
        # Progresso a cada 1 milhão
        if (i + 1) % 1_000_000 == 0:
            elapsed = time.time() - start_time
            rate = (i + 1) / elapsed
            print(f"Progresso: {i+1:,} / {max_checks:,} ({100*(i+1)/max_checks:.1f}%) - {rate:,.0f} chaves/s")
    
    elapsed = time.time() - start_time
    
    if found:
        print(f"\n✓ SUCESSO! Encontrado {len(found)} chave(s)")
        with open('puzzle71_solution.json', 'w') as f:
            json.dump(found, f, indent=2)
    else:
        print(f"\n❌ Nenhuma coincidência nos primeiros {max_checks:,} valores")
        print(f"Tempo total: {elapsed:.2f} segundos")
        print(f"Taxa: {max_checks/elapsed:,.0f} chaves/segundo")
    
    print()
    return found

if __name__ == "__main__":
    main()