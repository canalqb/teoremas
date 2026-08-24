# 🧩 - De Lob

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-L%C3%B6b-ff69b4.svg)](https://en.wikipedia.org/wiki/L%C3%B6b%27s_theorem)

## Frase do Teorema

> Se um sistema formal prova que "se P é provado, então P é verdadeiro", então o próprio P pode ser provado – isso mostra que certas afirmações autorreferentes podem ser confirmadas dentro do sistema.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `approx_lob_theorem.py`](#2-script-approx_lob_theorempy)

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

O **Teorema de Löb** é um conceito importante da **lógica matemática** que trata da relação entre provar uma proposição e a própria proposição ser verdadeira dentro de sistemas formais.

### 1.2 Exemplos Práticos

Imagine que um sistema consegue provar: "se a prova de P existe, então P é verdadeiro". O Teorema de Löb afirma que, neste caso, o sistema pode provar diretamente P. Isso ajuda a entender sistemas que fazem autorreferência, como programas que verificam sua própria correção.

### 1.3 Explicação Detalhada

O teorema mostra uma ligação especial: não basta apenas dizer que P é verdadeiro se for provado; o sistema pode concluir P a partir dessa condição. É um resultado que explica como certas declarações autorreferentes funcionam, e é muito usado em lógica modal e teoria da prova.

### 1.4 Aplicações

* **Lógica e fundamentos da matemática:** entender autoprova e autorreferência.
* **Teoria da Computação:** análise de sistemas formais e verificadores automáticos.
* **Filosofia da matemática:** estudar limites do conhecimento formal.

### 1.5 Análise da Tabela

A tabela gerada pelo script mostra valores para N entre 0 e 9, com três colunas:

* **Início:** 2 elevado a N (2^N), o limite inferior.
* **Fim:** 2 elevado a (N+1) menos 1 (2^(N+1) - 1), o limite superior.
* **Esperado aproximado:** média entre Início e Fim, que serve como uma boa aproximação simples para o valor esperado pelo teorema.

---

## 2. Script `approx_lob_theorem.py`

### 2.1 Relação com o Teorema

Este script tenta aproximar uma sequência que respeita os limites naturais indicados por potências de 2, simulando valores esperados relacionados ao Teorema de Löb.

### 2.2 Objetivo do Script

Gerar e imprimir uma tabela que exibe para cada N:

* O valor mínimo (Início = 2^N).
* O valor máximo (Fim = 2^(N+1) - 1).
* Uma estimativa intermediária (a média entre os dois valores).

### 2.3 Exemplo de Saída

```
 N  | Início (2^N) | Esperado Aproximado | Fim (2^(N+1)-1)
--------------------------------------------------------
 0  | 1            | 1                   | 1
 1  | 2            | 2                   | 3
 2  | 4            | 5                   | 7
 3  | 8            | 11                  | 15
 4  | 16           | 23                  | 31
 5  | 32           | 47                  | 63
 6  | 64           | 95                  | 127
 7  | 128          | 191                 | 255
 8  | 256          | 383                 | 511
 9  | 512          | 767                 | 1023
```

### 2.4 Funcionamento Interno

* Calcula o limite inferior como 2 elevado a N.
* Calcula o limite superior como 2 elevado a (N+1) menos 1.
* Calcula o esperado aproximado como a média entre esses dois valores.
* Imprime os resultados formatados para N de 0 a 9.

### 2.5 Tecnologias e Requisitos

* Python 3.8.10
* Biblioteca padrão (não requer dependências externas).

---

## 3 Extras

### 3.1 Licença

Projeto sob **licença MIT**, permitindo uso, cópia e modificação livre.

### 3.2 Referências

* [Wikipedia: Löb's theorem](https://en.wikipedia.org/wiki/L%C3%B6b%27s_theorem)
* Textos introdutórios sobre lógica modal e teoria da prova.

### 3.3 Testes e Validações

O script pode ser conferido comparando a saída com os limites teóricos, garantindo que os valores intermediários estejam dentro do intervalo esperado.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **Sistema formal:** um conjunto de regras e axiomas usados para provar proposições matemáticas ou lógicas.
* **Prova:** um conjunto de passos lógicos que confirmam que uma proposição é verdadeira.
* **Autorreferência:** quando uma afirmação fala sobre si mesma.
* **Potência de 2 (2^N):** 2 multiplicado por ele mesmo N vezes, por exemplo, 2^3 = 2×2×2 = 8.
* **Média:** soma de dois valores dividida por 2, para encontrar um valor intermediário.
