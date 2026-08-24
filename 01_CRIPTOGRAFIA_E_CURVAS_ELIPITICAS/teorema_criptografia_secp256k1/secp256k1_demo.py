#!/usr/bin/env python3
"""
🔐 Teorema de Curvas Elípticas - secp256k1
Demonstração básica da curva elíptica usada no Bitcoin
"""

class Point:
    """Ponto em curva elíptica"""
    def __init__(self, x, y, infinity=False):
        self.x = x
        self.y = y
        self.infinity = infinity
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.infinity == other.infinity
    
    def __repr__(self):
        if self.infinity:
            return "Point(INFINITY)"
        return f"Point({self.x}, {self.y})"

class Secp256k1:
    """Implementação básica da curva secp256k1"""
    
    def __init__(self):
        # Parâmetros da secp256k1 (usada no Bitcoin)
        self.p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
        self.a = 0
        self.b = 7
        self.Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
        self.Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
        self.n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
        self.h = 1
        
        # Ponto gerador G
        self.G = Point(self.Gx, self.Gy)
    
    def mod_inverse(self, a, p):
        """Calcula inverso modular usando pow(a, -1, p)"""
        return pow(a, -1, p)
    
    def point_add(self, p1, p2):
        """Adição de pontos na curva elíptica"""
        if p1.infinity:
            return p2
        if p2.infinity:
            return p1
        
        if p1.x == p2.x:
            if p1.y == p2.y:
                # Dobro de ponto
                return self.point_double(p1)
            else:
                # Ponto no infinito (p1 + (-p1) = O)
                return Point(0, 0, infinity=True)
        
        # Adição de pontos diferentes
        lambda_val = (p2.y - p1.y) * self.mod_inverse(p2.x - p1.x, self.p) % self.p
        x3 = (lambda_val * lambda_val - p1.x - p2.x) % self.p
        y3 = (lambda_val * (p1.x - x3) - p1.y) % self.p
        
        return Point(x3, y3)
    
    def point_double(self, p):
        """Dobro de ponto na curva elíptica"""
        if p.infinity:
            return p
        
        lambda_val = (3 * p.x * p.x + self.a) * self.mod_inverse(2 * p.y, self.p) % self.p
        x3 = (lambda_val * lambda_val - 2 * p.x) % self.p
        y3 = (lambda_val * (p.x - x3) - p.y) % self.p
        
        return Point(x3, y3)
    
    def scalar_multiply(self, k, point):
        """Multiplicação escalar: k * point"""
        if k == 0:
            return Point(0, 0, infinity=True)
        if k == 1:
            return point
        
        # Algoritmo Double-and-Add
        result = Point(0, 0, infinity=True)
        addend = point
        
        while k:
            if k & 1:
                result = self.point_add(result, addend)
            addend = self.point_double(addend)
            k >>= 1
        
        return result
    
    def is_on_curve(self, point):
        """Verifica se ponto está na curva"""
        if point.infinity:
            return True
        
        left = (point.y * point.y) % self.p
        right = (point.x * point.x * point.x + self.a * point.x + self.b) % self.p
        return left == right
    
    def generate_key_pair(self, private_key=None):
        """Gera par de chaves (privada, pública)"""
        if private_key is None:
            # Chave privada aleatória (simplificado)
            import random
            private_key = random.randint(1, self.n - 1)
        
        # Chave pública = private_key * G
        public_key = self.scalar_multiply(private_key, self.G)
        
        return private_key, public_key
    
    def demonstrate(self):
        """Demonstração da curva secp256k1"""
        print("🔐 DEMONSTRAÇÃO - CURVA ELÍPTICA secp256k1")
        print("=" * 50)
        print("Curva usada no Bitcoin para assinaturas digitais")
        print()
        
        # Parâmetros da curva
        print("📋 Parâmetros da Curva:")
        print(f"   Campo primo (p): {self.p}")
        print(f"   Coeficiente a: {self.a}")
        print(f"   Coeficiente b: {self.b}")
        print(f"   Ordem (n): {self.n}")
        print()
        
        # Ponto gerador
        print("📍 Ponto Gerador G:")
        print(f"   Gx: {self.Gx}")
        print(f"   Gy: {self.Gy}")
        print()
        
        # Verificação do ponto G na curva
        print("✅ Verificação: Ponto G está na curva?")
        print(f"   Resultado: {self.is_on_curve(self.G)}")
        print()
        
        # Geração de chaves
        print("🔑 Geração de Par de Chaves:")
        private_key, public_key = self.generate_key_pair()
        print(f"   Chave Privada: {private_key}")
        print(f"   Chave Pública: ({public_key.x}, {public_key.y})")
        print()
        
        # Verificação da chave pública
        print("✅ Verificação: Chave Pública está na curva?")
        print(f"   Resultado: {self.is_on_curve(public_key)}")
        print()
        
        # Operações básicas
        print("🔄 Operações com Pontos:")
        
        # Adição: G + G
        double_g = self.point_double(self.G)
        print(f"   2G = ({double_g.x}, {double_g.y})")
        
        # Multiplicação escalar: 3G
        triple_g = self.scalar_multiply(3, self.G)
        print(f"   3G = ({triple_g.x}, {triple_g.y})")
        print()
        
        # Verificação da ordem
        print("🔍 Verificação da Ordem:")
        nG = self.scalar_multiply(self.n, self.G)
        print(f"   {self.n} * G = {nG}")
        print(f"   Deveria ser ponto no infinito: {nG.infinity}")
        print()
        
        print("🎯 Aplicação no Bitcoin:")
        print("   • Chaves privadas controlam bitcoins")
        print("   • Chaves públicas geram endereços")
        print("   • Assinaturas digitais usam ECDSA")
        print("   • Segurança baseada no logaritmo discreto elíptico")

def main():
    """Função principal"""
    print("🚀 INICIANDO DEMONSTRAÇÃO DA secp256k1")
    print()
    
    secp = Secp256k1()
    secp.demonstrate()
    
    print("\n🎉 DEMONSTRAÇÃO CONCLUÍDA!")
    print("📚 Para mais detalhes, estude:")
    print("   • Elliptic Curve Cryptography (ECC)")
    print("   • ECDSA (Elliptic Curve Digital Signature Algorithm)")
    print("   • Curva secp256k1 específica do Bitcoin")

if __name__ == "__main__":
    main()
