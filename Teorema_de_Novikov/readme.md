# 🧮 - Teorema de Novikov

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Frase do Teorema

> **Teorema de Novikov** – Este teorema trata de um método probabilístico para justificar ou aproximar certos resultados dentro de um intervalo, usando uma progressão baseada em exponenciais e valores relacionados a grandezas iniciais e finais.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `novikov_theorem.py`](#2-script-novikov_theorempy)

  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3. Extras](#3-extras)

  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referencias)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4. Contato](#4-contato)
* [5. Nota](#5-nota)

---

## 1. Introdução ao Teorema

### 1.1 Resumo

O **Teorema de Novikov** é um conceito matemático utilizado para justificar ou aproximar certos resultados esperados dentro de um intervalo, onde as variáveis crescem exponencialmente. Ele pode ser aplicado em áreas como teoria de probabilidades ou em processos estocásticos.

### 1.2 Exemplos Práticos

O teorema é utilizado para definir valores aproximados esperados com base em intervalos exponenciais. A tabela a seguir mostra os cálculos feitos para diversos valores de N.

### 1.3 Explicação Detalhada

**O teorema** em questão pode ser entendido como uma abordagem para calcular uma média dentro de um intervalo crescente. Para cada valor de N, o intervalo é definido por duas quantidades exponenciais: 2^N e 2^(N+1)-1. O valor esperado do teorema é uma média entre esses dois valores.

### 1.4 Aplicações

Esse teorema pode ser usado para modelar sistemas de crescimento exponencial ou em processos onde se deseja prever um valor médio dentro de um intervalo.

### 1.5 Análise da Tabela

A tabela de valores abaixo mostra a relação entre N, o início do intervalo (2^N), o valor esperado pelo teorema e o fim do intervalo (2^(N+1)-1). Note que a coluna **Esperado pelo Teorema** é uma aproximação do valor esperado dentro desse intervalo.

```
Tabela de Valores Calculados:
N | Início (2^N) | Esperado pelo Teorema | Fim (2^(N+1))-1
0 | 1           | 1                     | 1
1 | 2           | 2                     | 3
2 | 4           | 5                     | 7
3 | 8           | 11                    | 15
4 | 16          | 23                    | 31
5 | 32          | 47                    | 63
6 | 64          | 95                    | 127
7 | 128         | 191                   | 255
8 | 256         | 383                   | 511
9 | 512         | 767                   | 1023
```

---

## 2. Script `novikov_theorem.py`

### 2.1 Relação com o Teorema

O script **`novikov_theorem.py`** implementa a lógica do teorema calculando os valores aproximados esperados dentro dos intervalos definidos pelos valores de 2^N e 2^(N+1)-1. A saída do script gera uma tabela com esses cálculos.

### 2.2 Objetivo do Script

O objetivo do script é calcular o valor esperado pelo teorema para diferentes valores de N, baseando-se na média entre o início e o fim de cada intervalo. Isso é feito através de uma função simples que calcula a média dos valores iniciais e finais do intervalo.

### 2.3 Exemplo de Saída

Ao executar o script, você verá uma saída como a tabela apresentada acima, onde cada linha representa o valor de N, o intervalo de início e fim, e o valor esperado aproximado pelo teorema.

### 2.4 Funcionamento Interno

O script funciona iterando sobre valores de N, calculando os valores de **Início** (2^N) e **Fim** (2^(N+1)-1) para cada N. A partir disso, o valor esperado é calculado como a média entre **Início** e **Fim**. Esses resultados são então impressos em uma tabela organizada.

### 2.5 Tecnologias e Requisitos

* **Python**: 3.8.10 ou superior
* **Bibliotecas**: Nenhuma dependência externa necessária. O script utiliza apenas funcionalidades nativas do Python.

---

## 3. Extras

### 3.1 Licença

Este projeto está licenciado sob a **MIT License**.

### 3.2 Referências

1. [Lei dos Grandes Números](https://en.wikipedia.org/wiki/Law_of_large_numbers) – Uma explicação geral sobre teoremas semelhantes.
2. [Probabilidade e Estatística](https://en.wikipedia.org/wiki/Probability_and_statistics) – Para entender melhor os conceitos usados no cálculo de probabilidades.

### 3.3 Testes e Validações

O script foi validado para garantir que os cálculos do valor esperado estejam corretos, baseando-se nos intervalos definidos pelos valores de 2^N e 2^(N+1)-1.

---

## 4. Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Variância**: A variância é uma medida de quanto os números em um conjunto de dados estão distantes da média.

**Esperança**: A esperança é o valor médio de um conjunto de números, ou seja, a média ponderada dos resultados possíveis de um evento.

**Intervalo**: O intervalo é a faixa de valores entre o valor inicial e o valor final.

**Exponencial**: Uma função exponencial é uma função matemática na qual uma quantidade cresce a uma taxa proporcional ao seu valor atual.
