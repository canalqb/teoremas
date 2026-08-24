# 🧩 - De Tychonoff

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)

## Frase do Teorema

> "O produto de qualquer coleção de espaços compactos é compacto" – isso significa que, quando juntamos muitos conjuntos que têm uma propriedade especial chamada *compactação*, o conjunto todo também mantém essa propriedade, mesmo que sejam muitos.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)

* [2. Script `mersenne_teorema.py`](#2-script-mersenne_teoremapy)

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

O Teorema de Tychonoff fala sobre um conceito chamado *compactação*, que é uma propriedade especial de conjuntos ou espaços usados em matemática. Ele diz que se você pegar vários conjuntos que têm essa propriedade e juntar todos eles em um só conjunto (chamado produto), o conjunto todo continuará tendo essa propriedade, mesmo que sejam muitos conjuntos juntos.

### 1.2 Exemplos Práticos

Imagine que você tem várias caixas, e cada caixa está completamente fechada (isso é uma forma de *compactação*). Se você juntar todas essas caixas em uma grande caixa, essa caixa maior também estará fechada de forma especial. O teorema garante isso, mesmo que haja muitas caixas.

### 1.3 Explicação Detalhada

* **Compactação:** é uma propriedade que, de forma simples, garante que um conjunto não "vaza" para fora, e que podemos sempre encontrar subgrupos ou subconjuntos que “cobrem” o conjunto inteiro.
* O teorema diz que, se cada um desses conjuntos pequenos é compacto, o conjunto formado por todos eles juntos (produto) também é compacto, mesmo que tenha muitos deles (até infinitos).
* Isso é importante porque muitos problemas matemáticos lidam com produtos de espaços, e saber que a compactação se mantém ajuda a provar várias coisas.

### 1.4 Aplicações

Este teorema é usado em áreas como análise matemática, teoria dos conjuntos e topologia, onde entender o comportamento de espaços complexos ajuda a resolver problemas em física, ciência da computação e matemática pura.

### 1.5 Análise da Tabela

No contexto prático, para entender intervalos de números, podemos usar aproximações baseadas em potências de 2 e números chamados de Mersenne, que ajudam a estimar valores dentro desses intervalos — mesmo sem usar o resultado direto do teorema.

---

## 2. Script `mersenne_teorema.py`

### 2.1 Relação com o Teorema

Embora o Teorema de Tychonoff trate de espaços compactos, o script cria uma aproximação numérica usando potências de 2 e números de Mersenne, que refletem os limites dos intervalos usados para ilustrar como valores podem crescer e serem aproximados.

### 2.2 Objetivo do Script

Gerar uma tabela para valores de n que mostra:

* O início do intervalo: 2 elevado a n
* O fim do intervalo: 2 elevado a (n+1) menos 1
* A estimativa aproximada baseada na soma dos números de Mersenne até n-1, combinada com a potência de 2 para chegar perto dos valores esperados.

### 2.3 Exemplo de Saída

```
N   | Início (2^N) | Fim (2^(N+1)-1) | Estimativa
-------------------------------------------------------
0   | 1            | 1               | 1
1   | 2            | 3               | 2
2   | 4            | 7               | 4
3   | 8            | 15              | 10
4   | 16           | 31              | 21
5   | 32           | 63              | 45
6   | 64           | 127             | 92
7   | 128          | 255             | 188
8   | 256          | 511             | 379
9   | 512          | 1023            | 763
```

### 2.4 Funcionamento Interno

* A função calcula números de Mersenne (2^k - 1) para valores k até n
* Soma esses números para formar uma base de cálculo
* A estimativa para cada n é dada pela potência 2^n somada à metade dessa soma dos Mersennes anteriores, tentando ficar próximo do valor real esperado

### 2.5 Tecnologias e Requisitos

* Python 3.8.10
* Sem dependências externas
* Fácil execução em qualquer sistema com Python instalado

---

## 3. Extras

### 3.1 Licença

Projeto sob licença MIT.

### 3.2 Referências

* Conceitos básicos de compactação e espaços topológicos
* Números de Mersenne e potências de 2

### 3.3 Testes e Validações

Tabela gerada pode ser conferida manualmente para pequenos valores de n, permitindo validação simples.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **Compactação:** propriedade especial que garante que um conjunto é “fechado” e “limitado”, não deixando escapar pontos importantes.
* **Potência de 2:** número obtido multiplicando 2 por ele mesmo várias vezes. Exemplo: 2^3 = 2×2×2 = 8.
* **Número de Mersenne:** número da forma 2^n - 1, ou seja, uma potência de 2 menos 1. Exemplo: 2^4 - 1 = 15.
* **Estimativa:** valor aproximado que serve para prever ou entender um resultado sem calculá-lo exatamente.
* **Intervalo:** faixa de números entre um começo e um fim, podendo incluir ou não os extremos.
