# 🧠 - Teorema Yoneda

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Yoneda](https://img.shields.io/badge/Teorema-Teorema%20de%20Yoneda-ff69b4.svg)](https://en.wikipedia.org/wiki/Yoneda_lemma)

## Frase do Teorema

> *"Um objeto é completamente determinado por todos os morfismos que partem de outros objetos em direção a ele."* – Isso quer dizer que para entender algo, basta observar todas as formas como ele é visto ou relacionado dentro de um sistema.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `yoneda_count_growth.py`](#2-script-yoneda_count_growthpy)

  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3. Extras](#3-extras)

  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referencias)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4 Contato](#4-contato)
* [5. Nota](#5-nota)

---

## 1. Introdução ao Teorema

### 1.1 Resumo

O **Teorema de Yoneda** é um conceito central na **teoria das categorias**, que afirma que a essência de um objeto pode ser completamente entendida por meio de todas as formas como outros objetos se conectam a ele — chamados de *morfismos*.

Essa ideia muda o foco de "o que é o objeto" para "como o objeto é visto", ou seja, para a sua relação com o resto do sistema.

---

### 1.2 Exemplos Práticos

| N | Início (2^N) | Estimado (Yoneda) | Fim (2^(N+1) - 1) |
| - | ------------ | ----------------- | ----------------- |
| 0 | 1            | 1                 | 1                 |
| 1 | 2            | 3                 | 3                 |
| 2 | 4            | 7                 | 7                 |
| 3 | 8            | 15                | 15                |
| 4 | 16           | 31                | 31                |
| 5 | 32           | 63                | 63                |

Aqui vemos que o valor estimado é uma soma cumulativa que cresce em potências de 2, refletindo o aumento das "formas de ver".

---

### 1.3 Explicação Detalhada

O que o teorema diz, em linguagem simples, é que para conhecer um objeto, não precisamos entendê-lo isoladamente, mas sim observar todas as maneiras pelas quais outros objetos se relacionam com ele.

Matematicamente, isso é representado pela soma dos morfismos, que pode ser vista como a soma de potências de 2: para cada nível N, o número de relações dobra, acumulando-se ao longo do tempo.

Assim, o crescimento é dado pela soma:

soma dos valores 2^0 + 2^1 + ... + 2^N = 2^(N+1) - 1

Isso indica um crescimento rápido e cumulativo, que simboliza o aumento das formas pelas quais um objeto é percebido ou mapeado.

---

### 1.4 Aplicações

Esse entendimento é útil em:

* **Teoria das categorias** — base para matemática abstrata e lógica
* **Ciência da computação** — modelagem de estruturas e relações entre dados
* **Lógica e filosofia** — compreensão de entidades pela relação, não só pela essência
* **Sistemas complexos** — análise de redes e interconexões

---

### 1.5 Análise da Tabela

A tabela mostra que para cada incremento em N:

* O valor inicial é 2 elevado a N
* O valor estimado é a soma acumulada de todos os valores anteriores, que cresce rapidamente
* O valor final é o limite máximo da soma até aquele ponto

Isso demonstra um crescimento exponencial cumulativo — uma das bases da ideia do Teorema de Yoneda.

---

## 2. Script `yoneda_count_growth.py`

---

### 2.1 Relação com o Teorema

O script modela a ideia de que o número total de "formas de ver" um objeto (ou seja, os morfismos) cresce somando as potências de 2 para cada nível.

---

### 2.2 Objetivo do Script

* Gerar uma tabela que ilustra o crescimento acumulado das "formas de ver" para cada nível N
* Demonstrar na prática como a soma cumulativa de potências de 2 cresce de forma rápida e controlada
* Facilitar o entendimento computacional do conceito abstrato do Teorema de Yoneda

---

### 2.3 Exemplo de Saída

```text
N   | Início (2^N) | Estimado (Yoneda) | Fim (2^(N+1) - 1)
--------------------------------------------------------
0   | 1            | 1                 | 1
1   | 2            | 3                 | 3
2   | 4            | 7                 | 7
3   | 8            | 15                | 15
4   | 16           | 31                | 31
5   | 32           | 63                | 63
```

---

### 2.4 Funcionamento Interno

O script executa:

1. Loop para N de 0 até um limite definido (por exemplo, 10)
2. Para cada N, calcula:

   * `inicio` = 2 elevado a N
   * `estimado` = soma acumulativa dos inícios de 0 até N (igual a 2^(N+1)-1)
   * `fim` = 2 elevado a (N+1) menos 1
3. Imprime os valores em uma tabela organizada

---

### 2.5 Tecnologias e Requisitos

* **Linguagem:** Python 3.8.10
* **Bibliotecas:** Nenhuma externa
* **Execução:** Terminal ou IDE local
* **Compatibilidade:** Windows, Linux, macOS

---

## 3 Extras

---

### 3.1 Licença

Este projeto está sob a **Licença MIT** — uso livre para estudo, modificações e distribuição.

---

### 3.2 Referências

* [Teorema de Yoneda - Wikipedia](https://en.wikipedia.org/wiki/Yoneda_lemma)
* Awodey, Steve. *Category Theory*, Oxford University Press
* Mac Lane, Saunders. *Categories for the Working Mathematician*
* Introdução à Teoria das Categorias — blog posts e artigos online

---

### 3.3 Testes e Validações

* Os valores calculados foram verificados manualmente para assegurar que a soma acumulada corresponde à fórmula teórica
* Testes garantem que os valores crescem de forma consistente e respeitam os limites

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **Potência (ex: 2^N):** significa multiplicar o número 2 por ele mesmo N vezes. Por exemplo, 2^3 = 2 \* 2 \* 2 = 8.
* **Morfismos:** formas de relacionar ou mapear um objeto para outro dentro de um sistema. Pense como “ligações” ou “caminhos” que conectam coisas.
* **Soma acumulativa:** soma de todos os valores até certo ponto. Por exemplo, a soma acumulativa até 3 de 1, 2, 4 é 1 + 2 + 4 = 7.
* **Teoria das categorias:** ramo da matemática que estuda objetos e suas relações abstratas, focando mais nas conexões do que nos objetos em si.
* **Teorema de Yoneda:** afirma que um objeto pode ser identificado completamente pelo modo como ele se relaciona com outros objetos.
