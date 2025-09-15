# 📐 - Teorema da Geodésica

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Frase do Teorema

> Pontos fora de uma linha reta podem ser organizados em intervalos de valores crescentes, mostrando variações constantes fora da linha principal y = 2x. – Uma maneira simples de entender que há muitos pontos próximos a uma linha, mas não exatamente sobre ela.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `Geodesica.py`](#2-script-geodesicapy)

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

Este conceito mostra como pontos que não estão exatamente numa linha reta, como y = 2x, podem ser organizados em grupos usando valores crescentes para x. Para cada grupo, escolhemos valores k diferentes de zero, que "deslocam" a linha para cima ou para baixo, criando pontos fora da reta original.

### 1.2 Exemplos Práticos

Imagine uma linha reta no gráfico que segue a regra: para cada x, y é igual a duas vezes x (y = 2x). Os pontos que adicionamos não estão nessa linha exata, mas próximos, deslocados um pouco para cima ou para baixo. Assim, para x entre 1 e 1, 2 e 3, 4 e 7, e assim por diante, temos vários exemplos de pontos que ficam fora dessa linha principal.

### 1.3 Explicação Detalhada

Para cada valor n de 0 até 10, escolhemos x variando entre 2^n e 2^(n+1)-1. Para cada x, calculamos y = 2x + k, onde k é um pequeno número diferente de zero (como -2, -1, 1 ou 2) para garantir que o ponto não esteja na linha y=2x. Com isso, geramos um conjunto de pontos em cada intervalo que estão sempre próximos da linha original, mas fora dela.

### 1.4 Aplicações

Este conceito pode ser usado em estudos de geometria e análise de funções para entender a distribuição de pontos próximos a uma linha, assim como em processamento de sinais, computação gráfica e até em simulações matemáticas que lidam com aproximações.

### 1.5 Análise da Tabela

A saída do script mostra, para cada intervalo definido por n, o conjunto de pontos gerados fora da reta y=2x. O número de pontos dobra conforme n aumenta, seguindo o crescimento do intervalo de x. Os primeiros 10 pontos de cada grupo são exibidos para facilitar a visualização.

---

## 2. Script `Geodesica.py`

### 2.1 Relação com o Teorema

O script exemplifica na prática a ideia de gerar pontos fora de uma linha reta fixa, mostrando como podemos organizar esses pontos em intervalos crescentes de x, mantendo um deslocamento constante (k).

### 2.2 Objetivo do Script

Gerar e listar pontos fora da reta y = 2x, organizados em intervalos de valores de x que crescem em potências de 2. Cada ponto tem y calculado como y = 2x + k, com k diferente de zero para garantir que o ponto não pertença à reta.

### 2.3 Exemplo de Saída

```
Intervalo para n=0: x in [1, 1]
Exemplos de pontos fora da reta y=2x (total 4 pontos):
  (1, 0)
  (1, 1)
  (1, 3)
  (1, 4)
...
Intervalo para n=10: x in [1024, 2047]
Exemplos de pontos fora da reta y=2x (total 4096 pontos):
  (1024, 2046)
  (1024, 2047)
  (1024, 2049)
  (1024, 2050)
  (1025, 2048)
  (1025, 2049)
  (1025, 2051)
  (1025, 2052)
  (1026, 2050)
  (1026, 2051)
```

### 2.4 Funcionamento Interno

* Para cada n de 0 até n\_max (padrão 10):

  * Define o intervalo de x entre 2^n e 2^(n+1)-1.
  * Para cada x no intervalo, calcula y para cada k em k\_values.
  * Armazena os pontos (x, y) num dicionário com chave n.

### 2.5 Tecnologias e Requisitos

* Python 3.8.10 (testado nesta versão)
* Nenhuma biblioteca externa necessária, código puro Python

---

## 3 Extras

### 3.1 Licença

Este projeto está sob licença MIT, permitindo uso livre e modificações com atribuição.

### 3.2 Referências

* Conceitos básicos de geometria analítica
* Organização de dados em Python
* Estrutura de laços e coleções em Python

### 3.3 Testes e Validações

O script foi testado para n\_max até 10, gerando corretamente os pontos e exibindo os primeiros 10 de cada intervalo sem erros.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **k**: valor usado para deslocar a linha original para cima ou para baixo, garantindo que o ponto não esteja exatamente na reta.
* **reta y=2x**: uma linha onde o valor de y é sempre duas vezes o valor de x.
* **intervalo \[a, b]**: conjunto de números começando em a e terminando em b, incluindo ambos.
* **n**: número inteiro usado para definir o tamanho do intervalo onde os pontos serão gerados.
* **potência de 2 (2^n)**: número 2 multiplicado por ele mesmo n vezes, usado para crescer o intervalo de valores de x.
* **ponto (x, y)**: par de números que indica uma posição no gráfico, onde x é a posição horizontal e y é a vertical.
