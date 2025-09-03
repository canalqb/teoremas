# 📊 - Teorema de Lindström

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Lindström-ff69b4.svg)](https://en.wikipedia.org/wiki/Combinatorics)

## Frase do Teorema

> O número máximo de subconjuntos distinguíveis em um conjunto finito é limitado e cresce conforme o tamanho do conjunto aumenta – isso ajuda a entender a complexidade das combinações possíveis.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `estimador_lindstrom.py`](#2-script-estimador_lindstrompy)

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

O **Teorema de Lindström** é um resultado na área de **combinatória** e **teoria da informação** que define limites para o número máximo de subconjuntos que podem ser *mutuamente distinguíveis* dentro de um conjunto com um número finito de elementos.

### 1.2 Exemplos Práticos

Imagine que você tem um conjunto com N elementos e quer saber quantos subconjuntos diferentes e “claramente separados” você pode formar. O teorema mostra que esse número cresce de forma limitada, e não é simplesmente todas as combinações possíveis.

### 1.3 Explicação Detalhada

O teorema estabelece que o número de subconjuntos distinguíveis está entre um limite inferior, que é simplesmente 2 elevado a N, e um limite superior, próximo de 2 elevado a (N+1) menos 1. Entre esses limites, existe uma estimativa intermediária que modela melhor o comportamento real, considerando uma soma ponderada de combinações.

### 1.4 Aplicações

* **Teoria da Informação:** entender a complexidade da codificação de dados.
* **Combinatória:** limites para estruturas de conjuntos e vetores binários.
* **Ciência da Computação:** otimização e análise de algoritmos combinatórios.

### 1.5 Análise da Tabela

A tabela gerada pelo script mostra os valores para N de 0 a 9, comparando o limite inferior (2^N), a estimativa intermediária (baseada em combinações) e o limite superior (2^(N+1) - 1). Isso ilustra como a estimativa se posiciona entre os limites, oferecendo uma visão clara da progressão do número de subconjuntos distinguíveis.

---

## 2. Script `estimador_lindstrom.py`

### 2.1 Relação com o Teorema

O script implementa uma estimativa intermediária para o número máximo de subconjuntos distinguíveis conforme proposto pelo **Teorema de Lindström**, usando uma fórmula baseada em combinações ponderadas.

### 2.2 Objetivo do Script

Calcular e imprimir uma tabela que mostra para cada N:

* O valor mínimo (2^N).
* A estimativa intermediária calculada pela soma ponderada.
* O valor máximo (2^(N+1) - 1).

### 2.3 Exemplo de Saída

```
 N  | Inicio (2^N) | Estimado | Fim (2^(N+1)-1)
------------------------------------------------
 0  | 1            | 1        | 1
 1  | 2            | 3        | 3
 2  | 4            | 7        | 7
 3  | 8            | 8        | 15
 4  | 16           | 21       | 31
 5  | 32           | 49       | 63
 6  | 64           | 76       | 127
 7  | 128          | 224      | 255
 8  | 256          | 467      | 511
 9  | 512          | 514      | 1023
```

### 2.4 Funcionamento Interno

* Calcula 2^N e 2^(N+1) - 1 para cada N.
* Computa a estimativa usando uma soma ponderada de combinações binomiais, que dá uma aproximação do limite superior real.
* Imprime a tabela formatada.

### 2.5 Tecnologias e Requisitos

* Python 3.8.10
* Apenas biblioteca padrão (math).

---

## 3 Extras

### 3.1 Licença

Projeto sob **licença MIT**, permitindo uso livre e modificação.

### 3.2 Referências

* B. Lindström, *On a combinatorial problem in number theory*, Canad. Math. Bull. 8 (1965), 477–490.
* Conceitos de combinatória e teoria da informação relacionados a subconjuntos distinguíveis.

### 3.3 Testes e Validações

O script pode ser validado visualmente comparando os valores estimados com os limites inferior e superior, garantindo coerência com o teorema.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **Conjunto finito:** coleção com número limitado de elementos.
* **Subconjuntos distinguíveis:** subconjuntos que podem ser diferenciados uns dos outros de maneira clara.
* **Combinação binomial (binomial coefficient):** número de formas de escolher k elementos de um conjunto com N elementos, sem se importar com a ordem.
* **Estimativa:** um valor calculado que serve como aproximação do valor real, sem garantir exatidão total. 
