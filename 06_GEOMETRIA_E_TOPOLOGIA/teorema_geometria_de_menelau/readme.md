# 🧩 - De Menelau

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Frase do Teorema

> Se uma reta corta os lados de um triângulo (ou seus prolongamentos), existe uma relação especial entre as divisões feitas nos lados. Essa relação ajuda a saber se três pontos estão alinhados em uma mesma reta.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)

* [2. Script `menelau.py`](#2-script-menelaupy)

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

O teorema mostra que, quando uma linha cruza os lados de um triângulo, a multiplicação de três razões de segmentos formados é sempre igual a -1. Isso é útil para saber se três pontos estão alinhados em linha reta dentro ou fora do triângulo.

### 1.2 Exemplos Práticos

Imagine um triângulo com lados cortados por uma reta em três pontos diferentes. Medindo as divisões feitas, o produto das três razões vai ser igual a -1 se esses pontos estiverem na mesma reta.

### 1.3 Explicação Detalhada

Os lados do triângulo são divididos em segmentos. Cada razão é uma divisão entre dois pedaços de um lado (por exemplo, AD dividido por DB). Multiplicando essas três razões obtidas em cada lado, o resultado é -1, indicando alinhamento.

### 1.4 Aplicações

* Verificar se três pontos são colineares (estão na mesma reta).
* Resolver problemas de geometria envolvendo triângulos.
* Ajudar em cálculos de segmentos dentro de figuras planas.

### 1.5 Análise da Tabela

Se observarmos valores diferentes para os segmentos, a relação só vale se o produto das razões for exatamente -1. Qualquer desvio indica que os pontos não estão alinhados.

---

## 2. Script `menelau.py`

### 2.1 Relação com o Teorema

O script usa os valores das duas primeiras razões para calcular a terceira, garantindo que a multiplicação das três seja -1, conforme a regra.

### 2.2 Objetivo do Script

Calcular o valor da última razão de segmentos de forma rápida, prática e automática, a partir de dois valores fornecidos.

### 2.3 Exemplo de Saída

```
Para a = 32 e b = 64, o valor de c é -0.00048828125
```

### 2.4 Funcionamento Interno

O script recebe dois valores (a e b), que representam as razões de segmentos, e calcula c como:
c = -1 / (a \* b)

### 2.5 Tecnologias e Requisitos

* Linguagem: Python 3.8.10
* Nenhuma biblioteca externa necessária.

---

## 3. Extras

### 3.1 Licença

Este projeto está sob a licença MIT.

### 3.2 Referências

* Wikipédia: Menelaus’ theorem
* Material didático de geometria plana.

### 3.3 Testes e Validações

O script foi testado com diversos valores para a e b, sempre retornando resultados consistentes conforme esperado pela regra.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

\*{Python}: linguagem de programação muito usada para cálculos e automações simples.
\*{Razão}: divisão entre dois valores, mostrando quantas vezes um contém o outro.
\*{Colinearidade}: quando três ou mais pontos estão alinhados na mesma linha reta.
\*{Segmento}: parte de uma linha que fica entre dois pontos.
\*{Ordem dos segmentos}: a forma como os pontos são considerados ao medir um segmento pode afetar o sinal do valor (positivo ou negativo).
