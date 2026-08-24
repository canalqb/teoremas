# 🧩 - De Cantor Diagonalizacao
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![LGN](https://img.shields.io/badge/Teorema-Diagonalização%20de%20Cantor-ff69b4.svg)](https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument)  

## Frase do Teorema

> Para qualquer conjunto, o conjunto de todos os seus subconjuntos é sempre maior do que ele – ou seja, não dá para listar todos os subconjuntos, mesmo para conjuntos infinitos.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `cantor_diagonal_simulation.py`](#2-script-cantor_diagonal_simulationpy)  
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

O **Teorema de Cantor**, conhecido também como **Teorema da Diagonalização**, mostra que o conjunto formado por todos os subconjuntos de um conjunto (chamado conjunto das partes) sempre tem mais elementos do que o próprio conjunto original.

### 1.2 Exemplos Práticos

- Para um conjunto com N elementos, existem 2 elevado a N subconjuntos diferentes.  
- No caso de infinitos, mesmo que você tente listar todos os subconjuntos, sempre haverá pelo menos um que ficou de fora.

### 1.3 Explicação Detalhada

Imagine que você tenta listar todos os subconjuntos de um conjunto infinito, colocando-os em uma tabela, linha por linha. Cantor criou um método que “vira a diagonal” dessa tabela e gera um subconjunto que não está na lista — provando que a lista nunca está completa.

### 1.4 Aplicações

- Compreensão dos diferentes tamanhos de infinitos.  
- Prova da não enumerabilidade dos números reais.  
- Fundamentos da ciência da computação, especialmente problemas indecidíveis.  
- Limites teóricos na compressão e criptografia.

### 1.5 Análise da Tabela

A tabela gerada pelo script mostra, para diferentes valores de N, quantos subconjuntos “fora da lista” aparecem, confirmando o crescimento muito rápido e que ultrapassa a contagem original.

---

## 2. Script `cantor_diagonal_simulation.py`

### 2.1 Relação com o Teorema

O script simula o processo de diagonalização de Cantor para demonstrar computacionalmente como os subconjuntos “não listáveis” crescem e excedem a simples enumeração.

### 2.2 Objetivo do Script

- Gerar subconjuntos que representam a diagonal invertida.  
- Contar quantos desses subconjuntos são únicos e fora da enumeração padrão.  
- Mostrar que o número desses subconjuntos cresce mais rápido que o conjunto original.

### 2.3 Exemplo de Saída

```text
N   | Inicio (2^N)   | Diagonal Count   | Fim (2^(N+1))-1
------------------------------------------------------------
0   | 1              | 1                | 1
1   | 2              | 3                | 3
2   | 4              | 6                | 7
3   | 8              | 8                | 15
4   | 16             | 19               | 31
5   | 32             | 37               | 63
6   | 64             | 70               | 127
7   | 128            | 138              | 255
8   | 256            | 272              | 511
9   | 512            | 531              | 1023
````

### 2.4 Funcionamento Interno

* Usa funções do Python para criar listas e subconjuntos.
* Aplica a lógica de diagonalização invertendo elementos na “diagonal” de uma matriz imaginária de subconjuntos.
* Conta e imprime os resultados em uma tabela simples.

### 2.5 Tecnologias e Requisitos

* Python 3.8.10 (funciona em versões 3.7+ também).
* Biblioteca padrão `itertools`.
* Executável via linha de comando.

---

## 3 Extras

### 3.1 Licença

Este projeto está sob a licença **MIT** — uso livre com atribuição.

### 3.2 Referências

* [Teorema da Diagonalização de Cantor - Wikipedia](https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument)
* Livros introdutórios de Teoria dos Conjuntos e Matemática Discreta.

### 3.3 Testes e Validações

Testes simples foram feitos para garantir que a contagem segue a progressão esperada, validando o comportamento do script.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **N**: representa um número natural (0,1,2,3...) que define o tamanho do conjunto.

* **2^N**: é a quantidade de subconjuntos que um conjunto com N elementos tem (exponencial em relação a N).

* **Diagonalização**: processo de modificar elementos ao longo da “diagonal” de uma matriz para criar algo novo e único.

* **Cardinalidade**: termo que indica o “tamanho” ou número de elementos de um conjunto, mesmo que infinito.

* **Injeção/Bijeção**: funções matemáticas que indicam como elementos de um conjunto podem ser associados a elementos de outro conjunto, importante para comparar tamanhos de conjuntos.
