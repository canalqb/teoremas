# 📊 - Teorema de Chebyshev

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)

## Frase do Teorema

> *O Teorema de Chebyshev* mostra que a quantidade de números primos até um certo valor **x** pode ser aproximada com base em uma fórmula envolvendo o próprio número e o logaritmo dele – **mesmo sem saber exatamente onde os primos estão**.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `chebyshev_intervalos.py`](#2-script-chebyshev_intervalospy)

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

O Teorema de Chebyshev é uma forma de prever quantos números primos existem até um certo número **x**, mesmo sem listá-los. Ele usa uma função que envolve **dividir o número x por seu logaritmo**.

### 1.2 Exemplos Práticos

Se você quiser saber quantos primos existem entre 256 e 511, pode aplicar a fórmula:

```
pi(511) - pi(255) ≈ 511 / log(511) - 255 / log(255)
```

O valor final é uma estimativa da quantidade de primos nesse intervalo.

### 1.3 Explicação Detalhada

A ideia principal é que a quantidade de primos menores que um número **x** não é aleatória, ela segue uma tendência. O teorema ajuda a calcular uma faixa provável para essa contagem, sem a necessidade de identificar cada número primo manualmente.

### 1.4 Aplicações

* Estimar a quantidade de primos em intervalos grandes
* Comparar com valores reais de listas de primos
* Criar algoritmos com base em previsões matemáticas confiáveis

### 1.5 Análise da Tabela

A tabela gerada no script mostra:

* O intervalo de potências de 2 (de 2^N até 2^(N+1) - 1)
* Quantos primos existem **estimados** pelo teorema entre esses valores

---

## 2. Script `chebyshev_intervalos.py`

### 2.1 Relação com o Teorema

O script utiliza diretamente a fórmula aproximada:

```
pi(x) ≈ x / log(x)
```

E aplica a diferença:

```
pi(2^(N+1) - 1) - pi(2^N - 1)
```

Essa diferença representa quantos primos existem no intervalo \[2^N, 2^(N+1)-1].

### 2.2 Objetivo do Script

* Calcular estimativas da quantidade de números primos em intervalos definidos por potências de 2
* Evitar usar dados reais de primos, confiando apenas na fórmula do teorema

### 2.3 Exemplo de Saída

```
+-----+----------------+-------------------------+---------------------+
|   N |   Início (2^N) |   Estimado pelo Teorema |   Fim (2^(N+1) - 1) |
+=====+================+=========================+=====================+
|   0 |              1 |                       0 |                   1 |
|   1 |              2 |                       3 |                   3 |
|   2 |              4 |                       1 |                   7 |
|   3 |              8 |                       2 |                  15 |
|   4 |             16 |                       3 |                  31 |
|   5 |             32 |                       6 |                  63 |
|   6 |             64 |                      11 |                 127 |
|   7 |            128 |                      20 |                 255 |
|   8 |            256 |                      36 |                 511 |
|   9 |            512 |                      66 |                1023 |
+-----+----------------+-------------------------+---------------------+
```

### 2.4 Funcionamento Interno

* Usa a biblioteca `math` para calcular logaritmos
* Usa a biblioteca `tabulate` para imprimir tabelas bonitas
* Usa Python 3.8.10 (ou superior)

### 2.5 Tecnologias e Requisitos

* Python 3.8.10+
* Biblioteca `tabulate` (instalar com `pip install tabulate`)

---

## 3 Extras

### 3.1 Licença

Este projeto está sob a licença MIT – veja o arquivo LICENSE para mais detalhes.

### 3.2 Referências

* Wikipedia: [Teorema de Chebyshev](https://pt.wikipedia.org/wiki/Teorema_de_Chebyshev)
* Projeto Euler e listas de primos

### 3.3 Testes e Validações

* Validado com Python 3.8.10
* Resultados compatíveis com estimativas conhecidas da distribuição dos primos

---

## 4 Contato

* Feito por **CanalQb** no GitHub
* Visite o blog: [canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via **Bitcoin**: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* **PIX**: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**logaritmo**:
É a operação inversa da exponenciação. Por exemplo, log(100) base 10 é 2 porque 10^2 = 100

**pi(x)**:
Função matemática que representa quantos números primos existem menores ou iguais a x

**número primo**:
É um número maior que 1 que só pode ser dividido por 1 e por ele mesmo

**potência de 2**:
São números como 2, 4, 8, 16, 32... que podem ser escritos como 2 elevado a algum número inteiro

**estimativa**:
É um valor aproximado, uma previsão, não exata mas próxima do valor real 
