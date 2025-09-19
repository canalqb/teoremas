# 🔁 - Teorema de Hurwitz  
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Hurwitz-ff69b4.svg)](https://en.wikipedia.org/wiki/Hurwitz%27s_theorem_(complex_analysis))

## Frase do Teorema

> Se uma sequência de funções analíticas não se anula e converge para uma função limite, então a função limite também não pode ter zeros — **a menos que esses zeros venham da própria sequência**.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `hurwitz_animacao.py`](#2-script-hurwitz_animacaopy)
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

## 1 Introdução ao Teorema

### 1.1 Resumo

O Teorema de Hurwitz trata do comportamento dos **zeros** de uma sequência de funções que **não se anulam**. Ele afirma que **os zeros de uma função limite não podem simplesmente aparecer do nada** — eles precisam ser "herdados" da sequência original.

### 1.2 Exemplos Práticos

Imagine uma sequência de curvas que nunca tocam o eixo horizontal. Se elas vão se aproximando de uma curva final, essa curva final também não pode cortar esse eixo — **a menos que essas aproximações já estivessem fazendo isso antes**.

### 1.3 Explicação Detalhada

Se temos várias funções que não possuem zeros (ou seja, não cruzam a linha horizontal), e essas funções se aproximam cada vez mais de uma outra, então essa última também **não deve** ter zeros. Caso ela tenha, os zeros devem estar **sendo "trazidos" pela aproximação**.

### 1.4 Aplicações

* Análise complexa
* Teoria das funções
* Sistemas dinâmicos
* Computação visual de funções analíticas

### 1.5 Análise da Tabela

Tabela dos valores calculados:

```

## n  |  2^n  |  Mersenne (2^n - 1)  |   f\_n(0)   |  f\_n(-10)  |  f\_n(10)

1  |   2   |          1           |   0.0000   |   0.5440   |  -0.5440
2  |   4   |          3           |   0.0000   |   0.1906   |  -0.1906
3  |   8   |          7           |   0.0000   |  -0.9899   |   0.9899
4  |  16   |          15          |   0.0000   |  -0.6184   |   0.6184
5  |  32   |          31          |   0.0000   |  -0.3170   |   0.3170

````

---

## 2 Script `hurwitz_animacao.py`

### 2.1 Relação com o Teorema

O script simula uma sequência de funções que depende de números **Mersenne**, e exibe essas curvas como se estivessem **girando em círculos**, representando visualmente como os **comportamentos se repetem e evoluem** — de forma coerente com o Teorema de Hurwitz.

### 2.2 Objetivo do Script

Criar uma **animação interativa e visual** que mostre as curvas definidas por `f_n(z) = sin(z / M_n)` orbitando ao redor da origem, com velocidades variadas.

### 2.3 Exemplo de Saída

A saída será uma animação interativa onde as curvas senoidais **giram em círculo**, cada uma com uma cor e velocidade próprias.

### 2.4 Funcionamento Interno

O código segue os seguintes passos:

1. Calcula `2^n` e `M_n = 2^n - 1`
2. Define a função `f_n(z) = sin(z / M_n)`
3. Gera os pontos `z` entre -10 e 10
4. Cria uma animação onde cada curva gira com base no tempo

### 2.5 Tecnologias e Requisitos

- Python 3.8.10
- `matplotlib`
- `numpy`

Instale os pacotes com:

```bash
pip install matplotlib numpy
````

Para salvar como GIF:

```python
anim.save('curvas_rotacionando.gif', writer='pillow', fps=30)
```

---

## 3 Extras

### 3.1 Licença

Este projeto está sob a licença MIT.

### 3.2 Referências

* [Teorema de Hurwitz – Wikipedia](https://en.wikipedia.org/wiki/Hurwitz%27s_theorem_%28complex_analysis%29)
* Visualizações matemáticas com Python
* Análise complexa aplicada à computação

### 3.3 Testes e Validações

Testado em:

* Python 3.8.10
* Windows 10 e 11
* VSCode, PyCharm e terminal

---

## 4 Contato

* Feito por **CanalQb** no GitHub
* Visite o blog: canalqb.blogspot.com
  👉 [https://canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via **Bitcoin**: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* 📩 **PIX**: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**analítica (ou holomorfa)**:
Uma função suave e bem-comportada, com derivada em todos os pontos (sem cantos ou quebras)

**Mersenne**:
Um número da forma 2 elevado a n, menos 1 (ex: 3, 7, 31...)

**convergência**:
Quando uma sequência vai chegando cada vez mais perto de um valor ou forma final

**zero de uma função**:
Um ponto onde a função "corta" o eixo horizontal (onde o valor da função é 0)

**sequência de funções**:
Várias funções diferentes, normalmente com algum padrão entre elas, analisadas em ordem

**herdar zeros**:
Significa que os pontos onde a função vale zero vêm da própria sequência anterior 
