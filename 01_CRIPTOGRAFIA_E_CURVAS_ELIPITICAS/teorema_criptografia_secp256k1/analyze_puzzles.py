#!/usr/bin/env python3
"""
Análise de padrões entre puzzles Bitcoin resolvidos
"""

import json
import hashlib
import base58
import sys
sys.path.insert(0, r"C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1")

from secp256k1_demo import Secp256k1

def analyze_puzzles():
    """Analisar padrões entre puzzles 1-30"""
    
    # Dados do CSV (puzzles 1-30)
    puzzles = [
        {"num": 1, "addr": "1BgGZ9tcN4rm9KBzDn7KprQz87SZ26SAMH", "hash160": "751e76e8199196d454941c45d1b3a323f1433bd6", "value": 100000},
        {"num": 2, "addr": "1CUNEBjYrCn2y1SdiUMohaKUi4wpP326Lb", "hash160": "7dd65592d0ab2fe0d0257d571abf032cd9db93dc", "value": 200000},
        {"num": 3, "addr": "19ZewH8Kk1PDbSNdJ97FP4EiCjTRaZMZQA", "hash160": "5dedfbf9ea599dd4e3ca6a80b333c472fd0b3f69", "value": 300000},
        {"num": 4, "addr": "1EhqbyUMvvs7BfL8goY6qcPbD6YKfPqb7e", "hash160": "9652d86bedf43ad264362e6e6eba6eb764508127", "value": 400000},
        {"num": 5, "addr": "1E6NuFjCi27W5zoXg8TRdcSRq84zJeBW3k", "hash160": "8f9dff39a81ee4abcbad2ad8bafff090415a2be8", "value": 500000},
        {"num": 6, "addr": "1PitScNLyp2HCygzadCh7FveTnfmpPbfp8", "hash160": "f93ec34e9e34a8f8ff7d600cdad83047b1bcb45c", "value": 600000},
        {"num": 7, "addr": "1McVt1vMtCC7yn5b9wgX1833yCcLXzueeC", "hash160": "e2192e8a7dd8dd1c88321959b477968b941aa973", "value": 700000},
        {"num": 8, "addr": "1M92tSqNmQLYw33fuBvjmeadirh1ysMBxK", "hash160": "dce76b2613052ea012204404a97b3c25eac31715", "value": 800000},
        {"num": 9, "addr": "1CQFwcjw1dwhtkVWBttNLDtqL7ivBonGPV", "hash160": "7d0f6c64afb419bbd7e971e943d7404b0e0daab4", "value": 900000},
        {"num": 10, "addr": "1LeBZP5QCwwgXRtmVUvTVrraqPUokyLHqe", "hash160": "d7729816650e581d7462d52ad6f732da0e2ec93b", "value": 1000000},
    ]
    
    secp = Secp256k1()
    
    print("=" * 70)
    print("ANÁLISE DE PADRÕES - Puzzles 1-10")
    print("=" * 70)
    print()
    
    results = []
    
    for p in puzzles:
        h = p['hash160']
        
        # Converter hash160 para chave privada possível
        # Para puzzles, os valores são geralmente múltiplos simples
        k_candidate = p['value']  # O valor diretamente
        
        # Testar algumas conversões
        for multiplier in [1, 2, 5, 10]:
            k = k_candidate * multiplier
            
            # Gerar pubkey
            P = secp.scalar_multiply(k % (2**256 - 2**32 - 977), secp.G)
            
            # Hash160 da pubkey
            prefix = b'\x02' if P.y % 2 == 0 else b'\x03'
            pubkey = prefix + P.x.to_bytes(32, 'big')
            sha = hashlib.sha256(pubkey).digest()
            calc_hash = hashlib.new('ripemd160', sha).hexdigest()
            
            if calc_hash == h:
                print(f"Puzzle {p['num']}: ✓ Encontrou hash!")
                print(f"  k = {hex(k)} (decimal: {k})")
                print(f"  value = {p['value']} * multiplier = {multiplier}")
                results.append({
                    'puzzle': p['num'],
                    'k': hex(k),
                    'value': p['value'],
                    'multiplier': multiplier
                })
                break
    
    print()
    print("=" * 70)
    print("PATRÃO IDENTIFICADO")
    print("=" * 70)
    print()
    
    if results:
        print("Os puzzles seguem o padrão:")
        print("k = value * 1 (multiplier direto)")
        print()
        print("Para o Puzzle 71:")
        target_value = 71000000  # 71 * 1000000 (seguindo o padrão)
        print(f"k esperado = {target_value}")
        print(f"k em hex = {hex(target_value)}")
        
        # Verificar se esse k gera o hash target
        k = target_value
        P = secp.scalar_multiply(k % (2**256 - 2**32 - 977), secp.G)
        prefix = b'\x02' if P.y % 2 == 0 else b'\x03'
        pubkey = prefix + P.x.to_bytes(32, 'big')
        sha = hashlib.sha256(pubkey).digest()
        h160 = hashlib.new('ripemd160', sha).hexdigest()
        
        print(f"\nHash160 calculado: {h160}")
        print(f"Hash160 target:    f6f5431d255bbf7b12e8add9af5e3475c44a0a5b8")
        print(f"Match: {h160 == 'f6f5431d255bbf7b12e8add9af5e3475c44a0a5b8'}")
        
        # WIF
        wif_bytes = k.to_bytes(32, 'big')
        extended = b'\x80' + wif_bytes + b'\x01'
        checksum = hashlib.sha256(hashlib.sha256(extended).digest()).digest()[:4]
        wif = base58.b58encode(extended + checksum).decode()
        print(f"\nWIF gerado: {wif}")
        print(f"Verificar se WIF começa com 'Kw': {wif.startswith('Kw')}")

if __name__ == "__main__":
    analyze_puzzles()