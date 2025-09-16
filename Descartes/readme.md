# 🔵 - Teorema de Descartes (Círculos Tangentes)
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Círculos%20Tangentes-ff69b4.svg)](https://en.wikipedia.org/wiki/Descartes%27_theorem)

## Frase do Teorema

> *Se três círculos são tangentes entre si, então existe um ou dois outros círculos que também são tangentes a esses três. O valor da curvatura (inverso do raio) desses círculos pode ser calculado usando uma fórmula específica.* – Essa fórmula permite descobrir o raio do quarto círculo que toca três outros círculos dados.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `descartes.py`](#2-script-descartespy)
  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3 Extras](#3-extras)
  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referências)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4 Contato](#4-contato)
* [5. Nota](#5-nota)

---

## 1. Introdução ao Teorema

### 1.1 Resumo

O **Teorema de Descartes** trata da relação entre quatro círculos que são todos tangentes entre si. Ele nos dá uma forma direta de calcular a curvatura (que é o inverso do raio) de um quarto círculo tangente a outros três.

---

### 1.2 Exemplos Práticos

Imagine que você tem três moedas encostadas uma na outra. Se quiser colocar uma quarta moeda que toque todas as três, este teorema diz qual o tamanho ideal dessa quarta moeda.

---

### 1.3 Explicação Detalhada

A fórmula funciona com a **curvatura** de cada círculo, que é apenas `1 dividido pelo raio`.

Se os três primeiros círculos têm curvaturas k1, k2 e k3, a fórmula calcula a curvatura k4 do quarto círculo assim:

```

k4 = k1 + k2 + k3 ± 2 \* raiz\_quadrada(k1*k2 + k2*k3 + k3\*k1)

```

Isso gera dois valores porque podem existir **dois círculos possíveis**: um menor por dentro, e outro maior por fora.

---

### 1.4 Aplicações

- Desenho e arte geométrica
- Construções de círculos encaixados (como no problema de Apolônio)
- Computação gráfica
- Estudos sobre empacotamento de círculos

---

### 1.5 Análise da Tabela

A saída gerada pelo script mostra como as curvaturas crescem com base em potências de 2 e números de Mersenne, com uma tendência de valores cada vez maiores ou negativos (caso o círculo esteja invertido ou interno).

---

## 2. Script `descartes.py`

### 2.1 Relação com o Teorema

Este script aplica a fórmula do **Teorema de Descartes** em uma sequência gerada com **potências de 2** e **números de Mersenne**.

---

### 2.2 Objetivo do Script

O objetivo é automatizar o cálculo da quarta curvatura com base em três anteriores, variando os valores conforme potências de 2 e seus respectivos Mersennes.

---

### 2.3 Exemplo de Saída

```

k1=4, k2=3, k3=8 -> k4 = 38.3238 ou -8.3238
k1=3, k2=8, k3=7 -> k4 = 46.4253 ou -10.4253
k1=8, k2=7, k3=16 -> k4 = 79.6621 ou -17.6621
...

```

---

### 2.4 Funcionamento Interno

- Usa **potências de 2** como base (ex: 2, 4, 8, 16, ...)
- Calcula os **números de Mersenne** (2^n - 1)
- Intercala os dois tipos de valores em uma lista
- Aplica o Teorema de Descartes em trios consecutivos dessa lista
- Mostra os dois possíveis valores de curvatura k4

---

### 2.5 Tecnologias e Requisitos

- Python 3.8.10 ✅
- Nenhuma biblioteca externa
- Roda direto no terminal

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a Licença MIT.

---

### 3.2 Referências

- Wikipedia: [Descartes' Theorem](https://en.wikipedia.org/wiki/Descartes%27_theorem)
- OEIS: [Mersenne Numbers](https://oeis.org/A000225)

---

### 3.3 Testes e Validações

- Testado com Python 3.8.10 no Windows
- Resultados consistentes com a fórmula original
- Sem dependências externas

---

## 4 Contato

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com  
  [https://canalqb.blogspot.com](https://canalqb.blogspot.com)  
* 💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  
*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**curvatura:** valor igual a 1 dividido pelo raio do círculo  
**tangente:** quando dois círculos encostam exatamente em um ponto  
**discriminante:** parte dentro da raiz quadrada numa fórmula  
**inverso:** o resultado de 1 dividido por algum número  
**raio:** distância do centro do círculo até sua borda  
**círculo interno/externo:** círculo por dentro ou por fora dos outros três  
**número de Mersenne:** número na forma 2^n - 1, famoso por gerar primos especiais  
**potência de 2:** número obtido multiplicando 2 por ele mesmo várias vezes (ex: 2, 4, 8, 16...)  
