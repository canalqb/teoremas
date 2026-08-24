#!/usr/bin/env python3
"""
Análise avançada dos puzzles - procura do k para o hash160 target
"""

import hashlib
import sys
import json

sys.path.insert(0, r"C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1")
from secp256k1_demo import Secp256k1

def main():
    secp = Secp256k1()
    target = "f6f5431d255bbf7b12e8add9af5e3475c44a0a5b8"
    
    print("=" * 70)
    print("ANÁLISE AVANÇADA - PUZZLE 71")
    print("=" * 70)
    print()
    
    # Carregar dados do JSON
    with open(r"C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1/puzzle71_hash160_51bit.json", 'r') as f:
        data = json.load(f)
    
    print(f"Total de entradas: {len(data)}")
    print()
    
    # Verificar se algum hash160 bate com o target
    print("Verificando hash160s contra o target...")
    
    found = False
    for entry in data:
        if entry['hash160'] == target:
            print(f"✓ ENCONTRADO!")
            print(f"  k = {entry['k']}")
            print(f"  WIF = {entry['wif']}")
            found = True
            break
    
    if not found:
        print(f"✗ Target não encontrado no range 2^51 a 2^52")
        print()
        print("O puzzle 71 está no range 2^70 a 2^71-1")
        print("Necessário fazer busca brute force nesse range")
        print()
        
        # Vamos verificar quantos hash160s têm prefixo igual ao target
        target_prefix = target[:4]
        print(f"Hash160s com prefixo '{target_prefix}':")
        count = 0
        for entry in data:
            if entry['hash160'].startswith(target_prefix):
                count += 1
                if count <= 5:
                    print(f"  {entry['hash160'][:32]} (k={entry['k']})")
        print(f"  ... total: {count} entradas")
    
    print()
    print("=" * 70)
    print("TEOREMA IDENTIFICADO")
    print("=" * 70)
    print()
    print("Padrão dos puzzles solucionados:")
    print("  - value = num * 1000000")
    print("  - k = value (inteiro direto)")
    print()
    print("Para Puzzle 71:")
    print(f"  - value = 710000000 (71 * 10000000)")
    print(f"  - No entanto, o target não corresponde a k = value")
    print()
    print("CONCLUSÃO: O Puzzle 71 requer busca brute force")
    print("no range 2^70 a 2^71-1 (aprox. 1.1 quintilhão de chaves)")

if __name__ == "__main__":
    main()