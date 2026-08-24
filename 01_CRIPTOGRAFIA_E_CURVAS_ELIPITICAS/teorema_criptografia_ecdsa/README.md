# 🔐 Teorema de Criptografia - ECDSA

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Cryptography](https://img.shields.io/badge/Topic-ECDSA-ff69b4.svg)](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm)

## Descrição

O **ECDSA (Elliptic Curve Digital Signature Algorithm)** é um algoritmo de assinatura digital baseado em criptografia de curva elíptica. É o algoritmo usado no Bitcoin para assinar transações e provar propriedade de bitcoins.

## 🎯 Relevância para o 1000 BTC Puzzle

Este teorema é **CRÍTICO** para o puzzle porque:

- **Assinaturas do puzzle**: Todas as transações usam ECDSA
- **Verificação de autenticidade**: Valida quem assinou o que
- **Análise de padrões**: Possível encontrar vulnerabilidades
- **Segurança criptográfica**: Base da confiança no sistema

## 🚀 Como Usar

### Executar Demonstração
```bash
cd 01_CRIPTOGRAFIA_E_CURVAS_ELIPITICAS/teorema_criptografia_ecdsa
python ecdsa_demo.py
```

### Exemplo de Uso
```python
from ecdsa_demo import ECDSA

# Criar instância ECDSA
ecdsa = ECDSA()

# Gerar chaves
private_key, public_key = ecdsa.generate_key_pair()

# Assinar mensagem
message = "Mensagem do puzzle"
signature = ecdsa.sign(private_key, message)

# Verificar assinatura
is_valid = ecdsa.verify(public_key, message, signature)
```

## 📋 Processo de Assinatura ECDSA

### 1. Geração de Chaves
```
Chave Privada (d) → Chave Pública (Q = dG)
```

### 2. Criação da Assinatura
```
1. Escolher k aleatório
2. Calcular R = kG
3. r = R.x mod n
4. s = k^(-1)(H(m) + rd) mod n
5. Assinatura = (r, s)
```

### 3. Verificação da Assinatura
```
1. Calcular w = s^(-1) mod n
2. u1 = H(m)w mod n
3. u2 = rw mod n
4. P = u1G + u2Q
5. Verificar: P.x mod n = r
```

## 🔧 Operações Implementadas

### Assinatura Digital
```python
# Criar assinatura
signature = ecdsa.sign(private_key, message)
# Retorna: (r, s)
```

### Verificação
```python
# Verificar assinatura
is_valid = ecdsa.verify(public_key, message, signature)
# Retorna: True/False
```

### Geração de Chaves
```python
# Gerar par de chaves
private_key, public_key = ecdsa.generate_key_pair()
```

## 📊 Parâmetros secp256k1

- **Curva**: y² = x³ + 7 (mod p)
- **Campo primo (p)**: 2²⁵⁶ - 2³² - 977
- **Ordem (n)**: FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
- **Ponto gerador (G)**: Coordenadas específicas

## 🛡️ Propriedades de Segurança

### Segurança Computacional
- Baseado no **ECDLP** (Elliptic Curve Discrete Logarithm Problem)
- **~128 bits** de segurança
- Resistente a ataques conhecidos (clássicos)

### Vulnerabilidades
- **Ataque de k reutilizado**: Se k for reutilizado, chave privada pode ser descoberta
- **Ataque de timing**: Implementações podem vazar informações
- **Ataques quânticos**: Vulnerável ao algoritmo de Shor

## 🔍 Aplicações no Bitcoin

### 1. Assinatura de Transações
```
Entradas + Chave Privada → Assinatura ECDSA
```

### 2. Verificação de Bloco
```
Bloco + Assinaturas → Validação ECDSA
```

### 3. Geração de Endereços
```
Chave Pública → Hash → Endereço Bitcoin
```

## 🧩 Análise para o 1000 BTC Puzzle

### Possíveis Abordagens
1. **Análise de assinaturas existentes**
   - Buscar padrões nas assinaturas do puzzle
   - Verificar se há vulnerabilidades conhecidas

2. **Verificação de autenticidade**
   - Confirmar que transações são válidas
   - Identificar possíveis falsificações

3. **Estudo de parâmetros**
   - Investigar se parâmetros incomuns foram usados
   - Analisar desvios do padrão Bitcoin

4. **Ataques teóricos**
   - Explorar ataques matemáticos conhecidos
   - Investigar propriedades especiais

## 📚 Conceitos Matemáticos

### Curva Elíptica
Conjunto de pontos formando um grupo abeliano com operação de adição

### Problema do Logaritmo Discreto Elíptico
Dado P e Q = kP, encontrar k é computacionalmente difícil

### Assinatura Digital
Esquema criptográfico para provar autoria de uma mensagem

## ⚠️ Limitações da Implementação

Esta é uma **implementação educacional**:

- **Segurança**: Não adequada para uso em produção
- **Performance**: Não otimizada para velocidade
- **Aleatoriedade**: Usa random() simples (não criptográfico)
- **Validação**: Sem validação completa de entradas

## 🔄 Próximos Passos

Para pesquisa avançada:
1. Estudar implementações reais do Bitcoin
2. Investigar bibliotecas criptográficas profissionais
3. Explorar ataques conhecidos ao ECDSA
4. Analisar curvas elípticas alternativas

## 📈 Estatísticas da Implementação

- **Tamanho da chave**: 256 bits
- **Tamanho da assinatura**: 512 bits (2 × 256)
- **Tempo de geração**: ~1ms (educacional)
- **Tempo de verificação**: ~1ms (educacional)

## 📚 Referências

- [Bitcoin Wiki - ECDSA](https://en.bitcoin.it/wiki/Elliptic_Curve_Digital_Signature_Algorithm)
- [Wikipedia - ECDSA](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm)
- [SEC 1: Elliptic Curve Cryptography](https://www.secg.org/sec1-v2.pdf)

---

*Este teorema é fundamental para entender como o Bitcoin garante a segurança e propriedade das transações.*
