#!/usr/bin/env python3
"""Verifica WIF C gerados corretamente"""
import base58
import hashlib

def wif_c_to_private_key(wif_c):
    """Decodifica WIF C e retorna a chave privada em bytes"""
    decoded = base58.b58decode(wif_c)
    # WIF C: 0x80 + 32 bytes privada + 0x01 + 4 bytes checksum
    if decoded[0] != 0x80:
        raise ValueError("Prefixo inválido")
    if decoded[-5] != 0x01:
        raise ValueError("Flag de compressão ausente")
    # Verifica checksum
    data = decoded[:-4]
    checksum = decoded[-4:]
    expected_checksum = hashlib.sha256(hashlib.sha256(data).digest()).digest()[:4]
    if checksum != expected_checksum:
        raise ValueError("Checksum inválido")
    return decoded[1:-5]  # Retorna apenas a chave privada de 32 bytes

def verify_wif_file(filepath):
    """Verifica todos os WIFs de um arquivo"""
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    print(f"Verificando {filepath}")
    print(f"Total de WIFs: {len(lines)}")
    
    errors = 0
    for i, line in enumerate(lines[:10]):  # Verifica primeiros 10
        parts = line.strip().split('|')
        if len(parts) != 2:
            print(f"  Erro no formato linha {i}: {line[:50]}")
            errors += 1
            continue
        
        idx, wif = parts[0], parts[1]
        try:
            priv_key = wif_c_to_private_key(wif)
            # Verifica se começa com K ou L (WIF C)
            if not (wif.startswith('K') or wif.startswith('L')):
                print(f"  Linha {idx}: WIF não é C (começa com {wif[0]})")
                errors += 1
        except Exception as e:
            print(f"  Linha {idx}: Erro {e}")
            errors += 1
    
    if errors == 0:
        print("✅ Todos os WIFs verificados são WIF C válidos!")
    else:
        print(f"❌ {errors} erros encontrados")
    
    return errors == 0

if __name__ == "__main__":
    print("=" * 70)
    print("VERIFICAÇÃO WIF C - PUZZLE 71")
    print("=" * 70)
    
    test = verify_wif_file(r"C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1/puzzle71_wif_51bit.txt")
    print()
    test2 = verify_wif_file(r"C:/Users/Qb/Desktop/ola/07. Teoremas_Matematica/teoremas/01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1/puzzle71_wif_71bit_sample.txt")