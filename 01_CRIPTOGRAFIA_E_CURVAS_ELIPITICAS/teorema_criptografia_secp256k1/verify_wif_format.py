#!/usr/bin/env python3
"""
VERIFICAÇÃO: Verificar se os WIFs nos arquivos estão no formato C correto
"""

import sys
sys.path.insert(0, r"C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1")

from secp256k1_demo import Secp256k1
import hashlib
import base58

def wif_c_to_private_key(wif: str) -> int:
    """Decodifica WIF C para chave privada"""
    decoded = base58.b58decode(wif)
    if len(decoded) != 34:
        raise ValueError(f"WIF inválido: {wif}")
    if decoded[0] != 0x80:
        raise ValueError(f"Prefixo WIF inválido")
    if decoded[-1] != 0x01:
        raise ValueError(f"Flag de compressão ausente")
    
    checksum = decoded[-4:]
    key_bytes = decoded[1:-5]
    
    # Verificar checksum
    computed = hashlib.sha256(hashlib.sha256(decoded[:-4]).digest()).digest()[:4]
    if computed != checksum:
        raise ValueError(f"Checksum inválido para {wif}")
    
    return int.from_bytes(key_bytes, 'big')

def main():
    secp = Secp256k1()
    
    # Ler alguns WIFs dos arquivos
    test_files = [
        "puzzle71_wif_51bit.txt",
        "puzzle71_wif_71bit_sample.txt",
        "puzzle71_51bits_in_71bit_wif.txt"
    ]
    
    print("=" * 70)
    print("VERIFICANDO FORMATO WIF C NOS ARQUIVOS")
    print("=" * 70)
    print()
    
    for filename in test_files:
        filepath = f"C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1/{filename}"
        try:
            with open(filepath, 'r') as f:
                lines = f.readlines()
                print(f"\n{filename}:")
                print(f"  Total de WIFs: {len(lines)}")
                
                # Verificar primeiros 5
                valid_count = 0
                for i, line in enumerate(lines[:5], 1):
                    parts = line.strip().split('|')
                    if len(parts) >= 2:
                        wif = parts[1]
                        if wif.startswith('Kw') or wif.startswith('K`):
                            print(f"  {i}| {wif[:20]}... ✓ Formato C")
                            valid_count += 1
                        elif wif.startswith('5'):
                            print(f"  {i}| {wif[:20]}... ✗ Formato U (ERRO USUÁRIO RECLAMA)")
                        else:
                            print(f"  {i}| {wif[:20]}... ? Formato desconhecido")
                
                if valid_count == 5:
                    print(f"  ✅ Todos os WIFs verificados estão em formato C (compressado)")
                else:
                    print(f"  ⚠️  Apenas {valid_count}/5 WIFs em formato C")
                    
        except FileNotFoundError:
            print(f"\n{filename}: ARQUIVO NÃO ENCONTRADO")
    
    print()
    print("=" * 70)

if __name__ == "__main__":
    main()