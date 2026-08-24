#!/usr/bin/env python3
"""
🔐 Teorema de Criptografia - ECDSA
Demonstração do Elliptic Curve Digital Signature Algorithm
"""

import hashlib
import random

class ECDSA:
    """Implementação simplificada do ECDSA para secp256k1"""
    
    def __init__(self):
        # Parâmetros secp256k1
        self.p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
        self.a = 0
        self.b = 7
        self.Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
        self.Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
        self.n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
        
        # Ponto gerador
        self.G = (self.Gx, self.Gy)
    
    def mod_inverse(self, a, m):
        """Calcula inverso modular"""
        if a < 0:
            a = (a % m)
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('Modular inverse does not exist')
        else:
            return x % m
    
    def egcd(self, a, b):
        """Extended Euclidean Algorithm"""
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.egcd(b % a, a)
            return (g, x - (b // a) * y, y)
    
    def point_add(self, p1, p2):
        """Adição de pontos na curva elíptica"""
        if p1 is None:
            return p2
        if p2 is None:
            return p1
        
        x1, y1 = p1
        x2, y2 = p2
        
        if x1 == x2:
            if y1 == y2:
                return self.point_double(p1)
            else:
                return None  # Ponto no infinito
        
        s = ((y2 - y1) * self.mod_inverse(x2 - x1, self.p)) % self.p
        x3 = (s * s - x1 - x2) % self.p
        y3 = (s * (x1 - x3) - y1) % self.p
        
        return (x3, y3)
    
    def point_double(self, p):
        """Dobro de ponto"""
        if p is None:
            return None
        
        x, y = p
        s = ((3 * x * x + self.a) * self.mod_inverse(2 * y, self.p)) % self.p
        x3 = (s * s - 2 * x) % self.p
        y3 = (s * (x - x3) - y) % self.p
        
        return (x3, y3)
    
    def scalar_multiply(self, k, point):
        """Multiplicação escalar"""
        if k == 0 or point is None:
            return None
        
        result = None
        addend = point
        
        while k:
            if k & 1:
                result = self.point_add(result, addend)
            addend = self.point_double(addend)
            k >>= 1
        
        return result
    
    def generate_key_pair(self):
        """Gera par de chaves"""
        private_key = random.randint(1, self.n - 1)
        public_key = self.scalar_multiply(private_key, self.G)
        return private_key, public_key
    
    def hash_message(self, message):
        """Hash da mensagem usando SHA-256"""
        return int(hashlib.sha256(message.encode()).hexdigest(), 16)
    
    def sign(self, private_key, message):
        """Cria assinatura digital"""
        # Hash da mensagem
        z = self.hash_message(message)
        
        # Escolhe k aleatório
        while True:
            k = random.randint(1, self.n - 1)
            if self.mod_inverse(k, self.n) is not None:
                break
        
        # Calcula ponto R = kG
        R = self.scalar_multiply(k, self.G)
        if R is None:
            return self.sign(private_key, message)  # Tentar novamente
        
        r = R[0] % self.n
        if r == 0:
            return self.sign(private_key, message)  # Tentar novamente
        
        # Calcula s
        k_inv = self.mod_inverse(k, self.n)
        s = (k_inv * (z + r * private_key)) % self.n
        
        if s == 0:
            return self.sign(private_key, message)  # Tentar novamente
        
        return (r, s)
    
    def verify(self, public_key, message, signature):
        """Verifica assinatura digital"""
        r, s = signature
        
        # Verifica bounds
        if r < 1 or r >= self.n or s < 1 or s >= self.n:
            return False
        
        # Hash da mensagem
        z = self.hash_message(message)
        
        # Calcula w = s^(-1) mod n
        w = self.mod_inverse(s, self.n)
        
        # Calcula u1 = zw mod n e u2 = rw mod n
        u1 = (z * w) % self.n
        u2 = (r * w) % self.n
        
        # Calcula pontos
        P1 = self.scalar_multiply(u1, self.G)
        P2 = self.scalar_multiply(u2, public_key)
        
        if P1 is None or P2 is None:
            return False
        
        # Calcula ponto final
        P = self.point_add(P1, P2)
        
        if P is None:
            return False
        
        # Verificação
        v = P[0] % self.n
        return v == r
    
    def demonstrate(self):
        """Demonstração do ECDSA"""
        print("🔐 DEMONSTRAÇÃO - ECDSA (Elliptic Curve Digital Signature Algorithm)")
        print("=" * 70)
        print("Algoritmo de assinatura digital usado no Bitcoin")
        print()
        
        # Geração de chaves
        print("🔑 Geração de Par de Chaves:")
        private_key, public_key = self.generate_key_pair()
        print(f"   Chave Privada: {private_key}")
        print(f"   Chave Pública: ({public_key[0]}, {public_key[1]})")
        print()
        
        # Mensagem para assinar
        message = "Este é o 1000 BTC Puzzle"
        print(f"📝 Mensagem: '{message}'")
        print()
        
        # Criação da assinatura
        print("✍️  Criando Assinatura Digital:")
        signature = self.sign(private_key, message)
        print(f"   Assinatura (r, s): ({signature[0]}, {signature[1]})")
        print()
        
        # Verificação da assinatura
        print("✅ Verificando Assinatura:")
        is_valid = self.verify(public_key, message, signature)
        print(f"   Resultado: {is_valid}")
        print()
        
        # Teste com mensagem diferente
        print("🔍 Teste com Mensagem Diferente:")
        wrong_message = "Esta mensagem é diferente"
        is_valid_wrong = self.verify(public_key, wrong_message, signature)
        print(f"   Mensagem: '{wrong_message}'")
        print(f"   Resultado: {is_valid_wrong}")
        print()
        
        # Propriedades matemáticas
        print("📊 Propriedades Matemáticas:")
        print(f"   • Ordem da curva (n): {self.n}")
        print(f"   • Campo primo (p): {self.p}")
        print(f"   • Ponto gerador G: ({self.G[0]}, {self.G[1]})")
        print()
        
        # Segurança
        print("🛡️  Aspectos de Segurança:")
        print("   • Baseado no problema do logaritmo discreto elíptico")
        print("   • Assinatura única por mensagem (com k aleatório)")
        print("   • Verificação pública, assinatura privada")
        print("   • Segurança de ~128 bits")
        print()
        
        # Aplicações no Bitcoin
        print("₿ Aplicações no Bitcoin:")
        print("   • Assinatura de transações")
        print("   • Prova de propriedade de bitcoins")
        print("   • Validação de blocos")
        print("   • Geração de endereços")
        print()
        
        print("🎯 Relevância para o 1000 BTC Puzzle:")
        print("   • Análise de assinaturas existentes")
        print("   • Verificação de autenticidade")
        print("   • Estudo de padrões criptográficos")
        print("   • Investigação de vulnerabilidades")

def main():
    """Função principal"""
    print("🚀 INICIANDO DEMONSTRAÇÃO DO ECDSA")
    print()
    
    try:
        ecdsa = ECDSA()
        ecdsa.demonstrate()
        
        print("\n🎉 DEMONSTRAÇÃO CONCLUÍDA!")
        print("📚 Para mais detalhes, estude:")
        print("   • Elliptic Curve Digital Signature Algorithm")
        print("   • Criptografia de curva elíptica")
        print("   • Implementações do Bitcoin")
        
    except Exception as e:
        print(f"❌ Erro na demonstração: {e}")

if __name__ == "__main__":
    main()
