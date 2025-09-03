# 🧠 - Teorema de Mitchell – Contagem de Bits em Intervalos

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Contagem%20de%20Bits-ff69b4.svg)](https://en.wikipedia.org/wiki/Population_count)

## Frase do Teorema

> A soma do número de bits ligados (1s) em todos os números dentro do intervalo entre 2 elevado a n e 2 elevado a n+1 segue um padrão que pode ser previsto – isso ajuda a entender como bits se comportam em blocos binários.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `mitchell_theorem.py`](#2-script-mitchell_theorempy)

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

O **Teorema de Mitchell** é uma observação sobre a soma da quantidade de bits ligados (`1`s) na representação binária dos números dentro de intervalos crescentes de potências de 2.

### 1.2 Exemplos Práticos

Considere o intervalo entre 2 elevado a n e 2 elevado a n+1, ou seja, todos os números de 2^n até (2^(n+1) - 1). Se somarmos o total de bits `1` que aparecem em todos esses números, o resultado segue um padrão curioso que pode ser analisado matematicamente.

### 1.3 Explicação Detalhada

Cada número binário tem alguns bits ligados (`1`s). Ao somar esses bits para todos os números em um intervalo específico, podemos notar tendências que refletem a estrutura dos números binários, como a distribuição e repetição de bits.

### 1.4 Aplicações

* **Compressão de dados e criptografia:** otimização baseada em propriedades dos bits.
* **Análise de algoritmos:** estudo da complexidade em operações bit a bit.
* **Matemática recreativa:** exploração de padrões em números binários.

### 1.5 Análise da Tabela

A tabela a seguir ilustra a soma dos bits ligados para alguns intervalos:

| Início | Fim | Soma de bits ligados |
| ------ | --- | -------------------- |
| 1      | 2   | 1                    |
| 2      | 4   | 3                    |
| 4      | 8   | 7                    |
| 8      | 16  | 8                    |
| 16     | 32  | 21                   |
| ...    | ... | ...                  |

Esses números mostram o padrão e ajudam a formular conjecturas e estudos.

---

## 2. Script `mitchell_theorem.py`

### 2.1 Relação com o Teorema

O script computa exatamente essa soma de bits ligados para intervalos que vão de 2^n até 2^(n+1) - 1, permitindo analisar e confirmar o comportamento observado pelo "Teorema de Mitchell".

### 2.2 Objetivo do Script

* Calcular a soma dos bits ligados para cada número no intervalo.
* Gerar uma tabela com os intervalos e seus totais.
* Facilitar a comparação com valores esperados e análise de padrões.

### 2.3 Exemplo de Saída

```
N | Início | Fim  | Soma bits ligados
--------------------------------------
0 | 1      | 1    | 1
1 | 2      | 3    | 3
2 | 4      | 7    | 7
3 | 8      | 15   | 8
4 | 16     | 31   | 21
...
```

### 2.4 Funcionamento Interno

* Define uma função que conta os bits `1` em um número (usando operações binárias simples).
* Para cada N, calcula o intervalo entre 2^N e 2^(N+1) - 1.
* Soma a contagem de bits de todos os números nesse intervalo.
* Imprime os resultados formatados.

### 2.5 Tecnologias e Requisitos

* Python 3.8.10
* Biblioteca padrão (sem dependências externas).

---

## 3 Extras

### 3.1 Licença

Este projeto está sob a **licença MIT**, permitindo uso e modificações livres.

### 3.2 Referências

* [Wikipedia: Population count (Contagem de bits)](https://en.wikipedia.org/wiki/Population_count)
* Estudos sobre representação binária e algoritmos bit a bit.

### 3.3 Testes e Validações

Testes podem ser realizados comparando as somas para intervalos pequenos com resultados manuais para garantir a precisão.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **Bit ligado:** um dígito `1` na representação binária de um número.
* **Intervalo:** um conjunto de números consecutivos entre um valor inicial e final.
* **2^n:** "2 elevado a n", ou seja, o número 2 multiplicado por ele mesmo n vezes.
* **Soma:** juntar vários números para formar um total.
