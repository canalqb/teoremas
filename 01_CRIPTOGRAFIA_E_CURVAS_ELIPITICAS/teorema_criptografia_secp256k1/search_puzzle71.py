#!/usr/bin/env python3
"""
Busca eficiente paralela para Puzzle 71
Hash160 target: f6f5431d255bbf7b12e8add9af5e3475c44a0a5b8
Endereço target: 1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU
Range: 2^70 a 2^71-1 (71-bit numbers)
"""

import json
import hashlib
import base58
import multiprocessing as mp
from functools import partial
import sys
sys.path.insert(0, r"C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1")

from secp256k1_demo import Secp256k1

secp = Secp256k1()

def hash160_from_pubkey(x: int, y: int) -> str:
    """Gera hash160 do pubkey"""
    prefix = b'\x02' if y % 2 == 0 else b'\x03'
    pubkey = prefix + x.to_bytes(32, 'big')
    sha = hashlib.sha256(pubkey).digest()
    ripemd = hashlib.new('ripemd160', sha).digest()
    return ripemd.hex()

def test_range(start_k: int, count: int, target_hash: str) -> dict:
    """Testa um range de chaves"""
    found = []
    for i in range(count):
        k = start_k + i
        P = secp.scalar_multiply(k, secp.G)
        h160 = hash160_from_pubkey(P.x, P.y)
        
        if h160 == target_hash:
            wif_bytes = k.to_bytes(32, 'big')
            extended = b'\x80' + wif_bytes + b'\x01'
            checksum = hashlib.sha256(hashlib.sha256(extended).digest()).digest()[:4]
            wif = base58.b58encode(extended + checksum).decode()
            found.append({
                'k': hex(k),
                'wif': wif,
                'hash160': h160
            })
            print(f"✓ ENCONTRADO: k={hex(k)}, WIF={wif}")
        
        if i % 100000 == 0 and i > 0:
            print(f"Progresso: {i}/{count} testados")
    
    return found

def main():
    target_hash = "f6f5431d255bbf7b12e8add9af5e3475c44a0a5b8"
    base = 2**70
    
    print("=" * 70)
    print("BUSCA POR CHAVE PARA O PUZZLE 71")
    print(f"Target hash160: {target_hash}")
    print(f"Range: 2^70 a 2^71-1")
    print("=" * 70)
    print()
    
    # Testar primeiros 100.000 valores
    print("Testando primeiros 100.000 valores do range...")
    result = test_range(base, 100000, target_hash)
    
    if not result:
        print("\n❌ Nenhuma coincidência nos primeiros 100,000 valores")
        print("O puzzle 71 pode exigir:\n")
        print("1. Busca em posições específicas (padrão conhecido)")
        print("2. Método diferente de geração de chave")
        print("3. A chave pode estar em um sub-range específico")
    else:
        print(f"\n✓ Encontrado: {result}")
        
        # Salvar resultado
        with open("puzzle71_keyfound.json", 'w') as f:
            json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()