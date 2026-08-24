# 🔐 01 - Criptografia e Curvas Elípticas

## 🎯 Relevância para o 1000 BTC Puzzle

O **1000 BTC Puzzle** está fundamentalmente ligado à criptografia de curvas elípticas usada no Bitcoin. Entender estes conceitos é essencial para qualquer abordagem matemática ao puzzle.

## � Teoremas Disponíveis

### 🔐 **Curvas Elípticas e Segurança**
- **[teorema_criptografia_secp256k1](./teorema_criptografia_secp256k1/)** - Curva secp256k1 usada no Bitcoin
- **[teorema_criptografia_ecdsa](./teorema_criptografia_ecdsa/)** - Algoritmo de assinatura digital

### 📡 **Teoria da Informação Criptográfica**
- **[teorema_criptografia_de_shannon](./teorema_criptografia_de_shannon/)** - Fundamentos da teoria da informação
- **[teorema_criptografia_de_huffman](./teorema_criptografia_de_huffman/)** - Compressão e codificação

## �📚 Conceitos Fundamentais

### Curva Elíptica secp256k1
- **Equação**: y² = x³ + 7 (mod p)
- **Campo**: Primo de 256 bits
- **Ponto Gerador**: Ponto base usado para gerar chaves

### ECDSA (Elliptic Curve Digital Signature Algorithm)
- Assinaturas digitais Bitcoin
- Verificação de transações
- Relação chave privada ↔ chave pública

### Teoria da Informação
- Entropia e compressão
- Limites fundamentais da comunicação
- Codificação eficiente

## 🔍 Aplicações ao Puzzle

### 1. Análise do Espaço de Chaves
```python
# Espaço de busca: 2^256 possibilidades
# Puzzle específico: subrange de 66 bits
```

### 2. Propriedades Matemáticas
- **Discrete Log Problem**: Base da segurança
- **Trapdoor Functions**: Fáceis de calcular, difíceis de reverter
- **Group Theory**: Estrutura algébrica das curvas

## 🛠️ Como Usar os Teoremas

### Curva secp256k1
```bash
cd teorema_criptografia_secp256k1
python secp256k1_demo.py
```

### ECDSA
```bash
cd teorema_criptografia_ecdsa
python ecdsa_demo.py
```

### Teoria de Shannon
```bash
cd teorema_criptografia_de_shannon
python Teorema_de_Shannon.py
```

### Codificação de Huffman
```bash
cd teorema_criptografia_de_huffman
python teorema_huffman_codificacao.py
```

## 📖 Material de Referência

### Recursos Online
- [Bitcoin Wiki - Elliptic Curve](https://en.bitcoin.it/wiki/Elliptic_curve)
- [Learn Me A Bitcoin - Elliptic Curve](https://learnmeabitcoin.com/technical/cryptography/elliptic-curve/)
- [Secp256k1 Parameters](https://en.bitcoin.it/wiki/Secp256k1)

### Livros Recomendados
- *Guide to Elliptic Curve Cryptography* - Hankerson, Menezes, Vanstone
- *Elliptic Curves: Number Theory and Cryptography* - Washington

## 🧩 Desafios Específicos do Puzzle

### 1. Otimização de Busca
- Redução do espaço de busca
- Algoritmos especializados para curvas
- Paralelização eficiente

### 2. Análise de Padrões
- Distribuição de chaves no espaço
- Propriedades estatísticas
- Correlações matemáticas

## 🚀 Como Começar

1. **Estude a matemática básica** das curvas elípticas
2. **Implemente operações básicas** (adição, duplicação)
3. **Explore algoritmos de busca** otimizados
4. **Analise padrões** no espaço de chaves do puzzle

## ⚠️ Aviso Importante

Este material é para fins educacionais e de pesquisa. A segurança criptográfica do Bitcoin depende da dificuldade computacional destes problemas.

---

**Próximo passo**: Explore `02_TEORIA_DOS_NUMEROS` para entender os fundamentos matemáticos subjacentes.
