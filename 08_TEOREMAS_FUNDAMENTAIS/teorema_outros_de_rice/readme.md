# 🧩 - De Rice

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Teorema%20de%20Rice-ff69b4.svg)](https://en.wikipedia.org/wiki/Rice%27s_theorem)

## Frase do Teorema

> Toda propriedade semântica não trivial de linguagens reconhecíveis por máquinas de Turing é indecidível – ou seja, não há um método geral para saber se um programa tem uma propriedade "interessante" sem analisar caso a caso.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `estimativa_rice.py`](#2-script-estimativa_ricepy)

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

O **Teorema de Rice** é uma descoberta importante na **teoria da computação** que diz que não existe um algoritmo universal capaz de decidir se um programa tem ou não uma certa propriedade não trivial relacionada ao seu comportamento.

### 1.2 Exemplos Práticos

Imagine querer saber se um programa sempre para, se imprime algo específico, ou se aceita certas entradas. Segundo o Teorema de Rice, não há uma fórmula mágica que responda isso para todos os programas — você precisa analisar cada caso.

### 1.3 Explicação Detalhada

* Uma propriedade é **não trivial** quando não vale para todos os programas nem para nenhum deles.
* Propriedades triviais seriam "este programa existe" (sempre verdadeiro) ou "este programa não existe" (sempre falso).
* O teorema diz que não existe um teste computacional que, para todos os programas, determine se eles possuem uma propriedade não trivial.

### 1.4 Aplicações

* Fundamento teórico para a indecidibilidade na computação.
* Compreensão dos limites do que os computadores podem decidir.
* Base para estudos em análise de programas, segurança, e complexidade computacional.

### 1.5 Análise da Tabela

A tabela gerada pelo script mostra uma estimativa da quantidade de funções que podem ter uma propriedade não trivial entre números definidos pelo intervalo `2^N` até `2^(N+1)-1`.

| N   | Início (2^N) | Fim (2^(N+1)-1) | Estimado |
| --- | ------------ | --------------- | -------- |
| 0   | 1            | 2               | 1        |
| 1   | 2            | 4               | 3        |
| 2   | 4            | 8               | 7        |
| 3   | 8            | 16              | 11       |
| 4   | 16           | 32              | 24       |
| ... | ...          | ...             | ...      |

Esse resultado é uma aproximação empírica que ajuda a visualizar o comportamento dessas funções mesmo sem uma decisão exata.

---

## 2. Script `estimativa_rice.py`

### 2.1 Relação com o Teorema

Embora o Teorema de Rice diga que não é possível decidir certas propriedades para todos os programas, o script **estima quantitativamente** a presença dessas propriedades em conjuntos finitos, ajudando a entender o cenário na prática.

### 2.2 Objetivo do Script

* Definir intervalos de números entre `2^N` e `2^(N+1)-1` para vários valores de N.
* Estimar, por meio de uma função matemática baseada em `log2`, quantas funções dentro desses intervalos podem ter propriedades não triviais.
* Gerar uma tabela clara e simples para visualização dessas estimativas.

### 2.3 Exemplo de Saída

```
N  | Início (2^N) | Fim (2^(N+1)-1) | Estimado
------------------------------------------------
0  | 1            | 2               | 1
1  | 2            | 4               | 3
2  | 4            | 8               | 7
3  | 8            | 16              | 11
4  | 16           | 32              | 24
...
```

### 2.4 Funcionamento Interno

* Para cada N no intervalo definido, calcula os limites inferior e superior do intervalo.
* Aplica uma função baseada em logaritmos para estimar a quantidade de funções com a propriedade não trivial.
* Imprime os valores em formato tabular para fácil leitura.

### 2.5 Tecnologias e Requisitos

* Desenvolvido em **Python 3.8.10**.
* Utiliza apenas bibliotecas padrão para cálculos e exibição.

---

## 3 Extras

### 3.1 Licença

Este projeto é aberto e gratuito para uso educacional e acadêmico sob a **licença MIT**.

### 3.2 Referências

* Henry Gordon Rice (1953) – artigo original sobre o Teorema de Rice.
* [Wikipedia: Rice’s theorem](https://en.wikipedia.org/wiki/Rice%27s_theorem)
* Livros e materiais introdutórios em teoria da computação.

### 3.3 Testes e Validações

O script foi validado com valores de N de 0 a 9, verificando a coerência dos resultados e a consistência do modelo matemático aplicado.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **Função:** programa ou processo computacional que recebe entrada e produz saída.
* **Propriedade não trivial:** característica que não é verdadeira para todos os programas, nem para nenhum.
* **Indecidível:** problema para o qual não existe um método computacional geral para dar resposta correta em todos os casos.
* **log2:** função que calcula o logaritmo na base 2, ou seja, quantas vezes você deve dividir um número por 2 para chegar a 1.
