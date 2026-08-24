#!/usr/bin/env python3
"""
Análise detalhada dos puzzles - busca de padrão específico
"""

import hashlib
import base58
import sys
sys.path.insert(0, r"C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1")

from secp256k1_demo import Secp256k1

def main():
    secp = Secp256k1()
    
    # Dados dos puzzles 1-10
    puzzles = [
        {"num": 1, "hash160": "751e76e8199196d454941c45d1b3a323f1433bd6", "value": 100000},
        {"num": 2, "hash160": "7dd65592d0ab2fe0d0257d571abf032cd9db93dc", "value": 200000},
        {"num": 3, "hash160": "5dedfbf9ea599dd4e3ca6a80b333c472fd0b3f69", "value": 300000},
        {"num": 4, "hash160": "9652d86bedf43ad264362e6e6eba6eb764508127", "value": 400000},
        {"num": 5, "hash160": "8f9dff39a81ee4abcbad2ad8bafff090415a2be8", "value": 500000},
        {"num": 6, "hash160": "f93ec34e9e34a8f8ff7d600cdad83047b1bcb45c", "value": 600000},
        {"num": 7, "hash160": "e2192e8a7dd8dd1c88321959b477968b941aa973", "value": 700000},
        {"num": 8, "hash160": "dce76b2613052ea012204404a97b3c25eac31715", "value": 800000},
        {"num": 9, "hash160": "7d0f6c64afb419bbd7e971e943d7404b0e0daab4", "value": 900000},
        {"num": 10, "hash160": "d7729816650e581d7462d52ad6f732da0e2ec93b", "value": 1000000},
    ]
    
    print("=" * 70)
    print("BUSCA POR K VALOR PARA CADA PUZZLE")
    print("=" * 70)
    print()
    
    # Para cada puzzle, procurar o k que gera o hash160
    for p in puzzles:
        print(f"Puzzle {p['num']} - hash160: {p['hash160'][:32]}...")
        
        # Testar diferentes possíveis k
        found_k = None
        
        # Testar valores próximos ao value
        for offset in range(-1000, 1001):
            for multiplier in [1, 2, 3, 4, 5]:
                k_test = (p['value'] + offset) * multiplier
                
                if k_test <= 0 or k_test >= 2**256 - 2**32 - 977:
                    continue
                
                P = secp.scalar_multiply(k_test, secp.G)
                prefix = b'\x02' if P.y % 2 == 0 else b'\x03'
                pubkey = prefix + P.x.to_bytes(32, 'big')
                sha = hashlib.sha256(pubkey).digest()
                h160 = hashlib.new('ripemd160', sha).hexdigest()
                
                if h160 == p['hash160']:
                    found_k = k_test
                    print(f"  ✓ k encontrado: {hex(k_test)} = {k_test}")
                    print(f"    (value={p['value']}, offset={offset}, mult={multiplier})")
                    break
            
            if found_k:
                break
        
        if not found_k:
            print(f"  ❌ k não encontrado no range testado")
            print(f"     Testando k próximo ao hash...")
            
            # Tentar converter hash160 para k (quando possível)
            try:
                hash_int = int(p['hash160'], 16)
                for mult in [1, 2, 10, 100]:
                    k_test = hash_int * mult
                    P = secp.scalar_multiply(k_test % (2**256 - 2**32 - 977), secp.G)
                    prefix = b'\x02' if P.y % 2 == 0 else b'\x03'
                    pubkey = prefix + P.x.to_bytes(32, 'big')
                    sha = hashlib.sha256(pubkey).digest()
                    h160 = hashlib.new('ripemd160', sha).hexdigest()
                    
                    if h160 == p['hash160']:
                        print(f"  ✓ k = hash160 * {mult} = {hex(k_test)}")
            except:
                pass
        
        print()
    
    print("=" * 70)
    print("TENTATIVA COM PUZZLE 71 TARGET")
    print("=" * 70)
    print()
    
    target_hash = "f6f5431d255bbf7b12e8add9af5e3475c44a0a5b8"
    
    # Vários valores testados
    test_values = [
        71000000,
        71000000 * 2,
        71000000 * 10,
        71 * 1000000,
        71 * 1000000 * 2,
        2**70,  # Início do range 71-bit
        2**70 + 1,
        2**70 + 100000,
    ]
    
    for k_test in test_values:
        P = secp.scalar_multiply(k_test, secp.G)
        prefix = b'\x02' if P.y % 2 == 0 else b'\x03'
        pubkey = prefix + P.x.to_bytes(32, 'big')
        sha = hashlib.sha256(pubkey).digest()
        h160 = hashlib.new('ripemd160', sha).hexdigest()
        
        match = "✓ MATCH!" if h160 == target_hash else ""
        print(f"k={k_test}: {h160} {match}")

if __name__ == "__main__":
    main()