# 🔐 Teorema de Curvas Elípticas - secp256k1

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Cryptography](https://img.shields.io/badge/Topic-ECC%20secp256k1-ff69b4.svg)](https://en.wikipedia.org/wiki/Elliptic_curve_digital_signature_algorithm)

## Descrição

A **curva secp256k1** é uma curva elíptica específica usada no Bitcoin e em muitas outras criptomoedas para gerar chaves públicas e assinaturas digitais através do algoritmo ECDSA (Elliptic Curve Digital Signature Algorithm).

## 🎯 Relevância para o 1000 BTC Puzzle

Este teorema é **ESSENCIAL** para o puzzle porque:

- **Base da criptografia do Bitcoin**: Todas as transações dependem dela
- **Geração de chaves**: Endereços Bitcoin derivam de chaves secp256k1
- **Assinaturas digitais**: Validam propriedade dos bitcoins
- **Segurança**: Baseada na dificuldade do logaritmo discreto elíptico

## 📋 Parâmetros da Curva

A secp256k1 é definida pela equação: `y² = x³ + 7 (mod p)`

Onde:
- **p** = 2²⁵⁶ - 2³² - 977 (número primo grande)
- **a** = 0
- **b** = 7
- **G** = Ponto gerador com coordenadas específicas
- **n** = Ordem do ponto gerador

## 🚀 Como Usar

### Executar Demonstração
```bash
cd 01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_secp256k1
python secp256k1_demo.py
```

### Exemplo de Uso
```python
from secp256k1_demo import Secp256k1

# Criar instância da curva
secp = Secp256k1()

# Gerar par de chaves
private_key, public_key = secp.generate_key_pair()

# Verificar se ponto está na curva
is_valid = secp.is_on_curve(public_key)
```

## 🔧 Operações Implementadas

### 1. Adição de Pontos
```python
# P1 + P2 = P3
result = secp.point_add(point1, point2)
```

### 2. Dobro de Ponto
```python
# 2P = P + P
double_point = secp.point_double(point)
```

### 3. Multiplicação Escalar
```python
# k * P
result = secp.scalar_multiply(k, point)
```

### 4. Geração de Chaves
```python
# Chave privada → Chave pública
private_key, public_key = secp.generate_key_pair()
```

## 📊 Aplicações no Bitcoin

### 1. Geração de Endereços
```
Chave Privada → Chave Pública → Hash → Endereço Bitcoin
```

### 2. Assinaturas Digitais
```
Mensagem + Chave Privada → Assinatura ECDSA
```

### 3. Verificação de Transações
```
Assinatura + Chave Pública + Mensagem → Válido/Inválido
```

## 🔍 Conceitos Matemáticos

### Curva Elíptica
Conjunto de pontos (x, y) que satisfazem `y² = x³ + ax + b (mod p)`

### Grupo Aditivo
Pontos na curva formam um grupo com operação de "adição"

### Ponto no Infinito
Elemento neutro do grupo, representado como O

### Ordem do Ponto
Menor inteiro n tal que `n * G = O`

## 🛡️ Aspectos de Segurança

### Problema do Logaritmo Discreto Elíptico (ECDLP)
Dado P e kP, é computacionalmente difícil encontrar k

### Segurança de 128 bits
A secp256k1 oferece ~128 bits de segurança

### Resistência Quântica
Vulnerável a computadores quânticos (algoritmo de Shor)

## 📚 Referências

- [Bitcoin Wiki - secp256k1](https://en.bitcoin.it/wiki/Secp256k1)
- [Wikipedia - Elliptic Curve Cryptography](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography)
- [Standards for Efficient Cryptography - SEC 2](https://www.secg.org/sec2-v2.pdf)

## 🧩 Relação com o 1000 BTC Puzzle

Para resolver o puzzle, você pode precisar:

1. **Analisar chaves públicas**: Derivar informações de chaves conhecidas
2. **Verificar assinaturas**: Validar transações do puzzle
3. **Explorar curvas**: Entender propriedades matemáticas
4. **Testar vulnerabilidades**: Investigar possíveis fraquezas

## ⚠️ Limitações da Implementação

Esta é uma **implementação educacional** simplificada:

- Não otimizada para performance
- Sem medidas de segurança contra ataques de timing
- Sem validação completa de entradas
- Para uso educacional apenas

## 🔄 Próximos Passos

Para pesquisa avançada:
1. Estudar ECDSA completo
2. Implementar validação de assinaturas
3. Explorar curvas diferentes
4. Investigar ataques conhecidos

---

*Este teorema forma a base matemática fundamental do Bitcoin e é essencial para entender o 1000 BTC Puzzle.*
