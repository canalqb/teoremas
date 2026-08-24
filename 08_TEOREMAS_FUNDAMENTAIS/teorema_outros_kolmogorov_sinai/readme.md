# 🧩 - Kolmogorov Sinai

## Frase do Teorema

> A entropia de um sistema dinâmico mede a **quantidade máxima de informação** (ou aleatoriedade) que ele gera com o tempo – ou seja, o grau de **imprevisibilidade** do seu comportamento.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `Kolmogorov_Sinai.py`](#2-script-kolmogorov_sinaipy)
  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3 Extras](#3-extras)
  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referencias)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4 Contato](#4-contato)
* [5. Nota](#5-nota)

---

## 1. Introdução ao Teorema

### 1.1 Resumo

O **Teorema de Kolmogorov–Sinai** é um pilar da **teoria ergódica** e da **teoria da informação**. Ele permite medir o quanto um sistema dinâmico é **aleatório** ou **informativo** com o passar do tempo.

Se observarmos uma sequência de dados (como 0s e 1s), esse teorema nos ajuda a entender **quanta informação nova aparece a cada passo**.

### 1.2 Exemplos Práticos

- Avaliar a aleatoriedade de geradores de números binários
- Medir o conteúdo de informação em sensores ou sinais digitais
- Detectar padrões escondidos em fluxos de dados

### 1.3 Explicação Detalhada

Imagine uma longa sequência de bits como:

```
011010001011...

```

Dividimos essa sequência em **blocos de tamanho k** (por exemplo, blocos de 2 bits: 01, 10, 00, ...), e medimos a **diversidade** desses blocos. Se todos aparecem com a mesma frequência, temos **alta entropia**.

A entropia por bit é definida como:

```
h = limite de H\_k / k, quando k vai para o infinito

```

Onde:

- `H_k` é a entropia total dos blocos de tamanho `k`
- `k` é o tamanho do bloco

Quanto mais próximo de **1.0** estiver `H_k / k`, mais aleatória é a sequência.

### 1.4 Aplicações

- Avaliar se uma fonte de dados é criptograficamente segura
- Medir compressibilidade de arquivos
- Detectar redundância em transmissões
- Estudar o comportamento caótico de sistemas complexos

### 1.5 Análise da Tabela

O script mostra como a entropia cresce com o tamanho dos blocos `k`.  
Exemplo de saída:

```
| k | Blocos únicos | Total blocos | H\_k (bits) | H\_k / k |
| - | ------------- | ------------ | ----------- | -------- |
| 1 | 2             | 100000       | 1.000000    | 1.0000   |
| 2 | 4             | 50000        | 2.000000    | 1.0000   |
| 3 | 8             | 33333        | 3.000000    | 1.0000   |

```

Blocos totalmente aleatórios ocupam **todos os padrões possíveis** (2^k).  
Se isso acontece, o valor `H_k / k` tende a **1.0**, que é o valor máximo de entropia por bit.

---

## 2. Script `Kolmogorov_Sinai.py`

### 2.1 Relação com o Teorema

Este script mostra como calcular a entropia de uma sequência binária com base no Teorema de Kolmogorov–Sinai. Ele verifica **quantos padrões únicos existem** à medida que o tamanho dos blocos aumenta.

### 2.2 Objetivo do Script

- Gerar uma sequência binária segura e aleatória
- Dividir essa sequência em blocos de tamanho `k`
- Calcular a **entropia de Shannon** desses blocos
- Mostrar a **entropia por bit** (H_k / k)
- Permitir análise de aleatoriedade de forma prática

### 2.3 Exemplo de Saída

📊 Análise de Entropia com base em Kolmogorov–Sinai
Total de bits gerados: 100000
Fonte: secrets.token\_bytes

```
| k | Blocos únicos | Total blocos | H\_k (bits) | H\_k / k |
| - | ------------- | ------------ | ----------- | -------- |
| 1 | 2             | 100000       | 1.000000    | 1.0000   |
| 2 | 4             | 50000        | 2.000000    | 1.0000   |
| 3 | 8             | 33333        | 3.000000    | 1.0000   |

```

### 2.4 Funcionamento Interno

O script:

1. Gera uma sequência binária com `secrets.token_bytes`
2. Converte os bytes em bits (0s e 1s)
3. Para cada valor de `k`, forma blocos consecutivos
4. Conta as ocorrências de cada bloco
5. Calcula a entropia `H_k` usando a fórmula de Shannon
6. Exibe a entropia total e a entropia por bit (`H_k / k`)

### 2.5 Tecnologias e Requisitos

- **Python 3.8.10**
- Bibliotecas utilizadas:
  - `secrets`
  - `math`
  - `collections`

Instalação:

Nenhuma instalação externa é necessária. Tudo funciona com bibliotecas padrão do Python.

---

## 3 Extras

### 3.1 Licença

Este projeto é **open source** sob a licença **MIT**.  
Use, compartilhe e modifique livremente!

### 3.2 Referências

- A.N. Kolmogorov — *Entropy per Unit Time as a Metric Invariant of Automorphisms*
- C.E. Shannon — *A Mathematical Theory of Communication*
- Cover & Thomas — *Elements of Information Theory*

### 3.3 Testes e Validações

- O script foi testado com diferentes valores de `n_bits` e `k_max`
- A entropia por bit aproxima-se de 1.0 em fontes verdadeiramente aleatórias
- O código foi validado com sequências artificiais e reais

---

## 4 Contato

* Feito por **CanalQb** no GitHub  
* Visite o blog: [canalqb.blogspot.com](https://canalqb.blogspot.com)  
* 💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

_Readme.md corrigido por ChatGPT_

---

## 5. Nota

### Termos Técnicos Explicados

- **Entropia**: medida de incerteza ou quantidade de informação em uma fonte de dados.
- **Entropia por bit (H_k / k)**: valor médio de incerteza de cada bit na sequência.
- **Shannon**: criador da teoria da informação, que define como medir a entropia.
- **Teoria ergódica**: área da matemática que estuda como sistemas evoluem com o tempo.
- **Aleatoriedade criptográfica**: geração de números imprevisíveis, mesmo para um atacante que conhece o sistema.
- **Blocos de k bits**: grupos de bits consecutivos usados para calcular padrões e medir a entropia.
- **Fonte de informação**: qualquer sequência de dados ou sinais que transmite algo com o tempo.

---
