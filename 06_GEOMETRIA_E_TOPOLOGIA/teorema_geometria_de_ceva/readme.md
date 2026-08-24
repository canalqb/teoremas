# 🧩 - De Ceva

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Frase do Teorema

> Em um triângulo, se três segmentos saem de cada vértice e se cruzam em um mesmo ponto dentro do triângulo, existe uma relação especial entre as divisões feitas nos lados. Essa relação ajuda a saber se essas três linhas realmente se encontram num ponto comum.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)

* [2. Script `ceva.py`](#2-script-cevapy)

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

O teorema afirma que, dentro de um triângulo, se três linhas traçadas de cada vértice até o lado oposto se cruzam em um mesmo ponto, a multiplicação de três razões de segmentos dos lados será igual a 1.

### 1.2 Exemplos Práticos

Se dentro de um triângulo você traçar segmentos de cada vértice até o lado oposto (chamados de cevianas), e eles se encontrarem em um único ponto, você pode usar as divisões feitas nos lados para testar se isso é verdade.

### 1.3 Explicação Detalhada

Cada lado do triângulo é dividido em dois pedaços pelos pontos onde as cevianas tocam. As razões desses pedaços (por exemplo, BD dividido por DC) são multiplicadas entre si. Se o resultado for 1, significa que as três linhas realmente se encontram num mesmo ponto.

### 1.4 Aplicações

* Verificar se três cevianas se encontram num mesmo ponto dentro do triângulo.
* Resolver problemas de geometria envolvendo divisões proporcionais.
* Usado em demonstrações envolvendo baricentro, incentro e outras construções geométricas.

### 1.5 Análise da Tabela

Com diversos valores dados, é possível verificar se a condição de equilíbrio é mantida (produto igual a 1). Caso não seja, os segmentos não se cruzam em um único ponto.

---

## 2. Script `ceva.py`

### 2.1 Relação com o Teorema

Este script implementa diretamente a condição do Teorema de Ceva, usando três razões de divisão dos lados do triângulo para verificar se as linhas se encontram num ponto comum.

### 2.2 Objetivo do Script

Calcular a terceira razão a partir de duas fornecidas, garantindo que o produto final seja igual a 1.

### 2.3 Exemplo de Saída

```
Para a = 2 e b = 3, o valor de c é 1/6 ≈ 0.166666...
```

### 2.4 Funcionamento Interno

O script realiza o seguinte cálculo:
c = 1 / (a \* b)

Esse valor mantém a relação:
(a) \* (b) \* (c) = 1

### 2.5 Tecnologias e Requisitos

* Linguagem: Python 3.8.10
* Nenhuma biblioteca externa necessária.

---

## 3 Extras

### 3.1 Licença

Este projeto está sob a licença MIT.

### 3.2 Referências

* Wikipédia: Ceva’s theorem
* Livros de Geometria Plana

### 3.3 Testes e Validações

Testado com várias combinações de a e b, e os valores de c mantêm o equilíbrio exigido pelo teorema.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Ceviana**: linha que vai de um vértice até o lado oposto, dentro de um triângulo
**Razão**: divisão entre dois valores
**Produto**: resultado da multiplicação
**Segmento**: pedaço de uma linha entre dois pontos
**Colinear**: quando pontos estão na mesma reta
**Baricentro**: ponto onde as medianas de um triângulo se cruzam
**Incentro**: ponto onde as bissetrizes de um triângulo se cruzam
