# 🔁 - Teorema do Ponto Fixo de Banach
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Banach](https://img.shields.io/badge/Teorema-Ponto%20Fixo%20de%20Banach-ff69b4.svg)](https://en.wikipedia.org/wiki/Banach_fixed-point_theorem)

## Frase do Teorema

> Toda função contraente definida num espaço completo tem exatamente um ponto que, ao ser usado como entrada, gera ele mesmo como saída – ou seja, um ponto fixo.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `banach.py`](#2-script-banachpy)
  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3. Extras](#3-extras)
  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referências)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4. Contato](#4-contato)
* [5. Nota](#5-nota)

---

## 1. Introdução ao Teorema

### 1.1 Resumo

O **Teorema do Ponto Fixo de Banach** garante que, se tivermos uma função que "encurta distâncias" (ou seja, é uma *função contraente*), e aplicarmos essa função várias vezes a qualquer valor inicial, vamos acabar chegando a um valor específico que não muda mais. Esse valor é chamado de *ponto fixo*.

### 1.2 Exemplos Práticos

Imagine que você dobra um papel e depois corta no meio repetidamente. No fim, não importa o tamanho do papel: sempre vai convergir para um tamanho que não muda mais — esse é o *ponto fixo* da transformação.

### 1.3 Explicação Detalhada

Neste projeto, aplicamos esse conceito em intervalos do tipo:

```

\[2^n, 2^(n+1) - 1]

```

Para cada intervalo, criamos uma função contraente que, ao ser repetidamente aplicada, converge para um número inteiro dentro do próprio intervalo. Isso é feito **sem usar sorteio (random)** e **sem sempre cair no meio do intervalo**, garantindo variação e controle.

### 1.4 Aplicações

* Algoritmos de otimização
* Métodos numéricos iterativos
* Processos de equilíbrio (como preços em economia)
* Soluções aproximadas para equações complexas

### 1.5 Análise da Tabela

A saída do script mostra que, para cada valor de `n`, temos um intervalo e um ponto fixo calculado com precisão. Veja um exemplo:

```
Intervalo \[8, 15] - Ponto fixo aproximado (inteiro): x\* = 10
Intervalo \[16, 31] - Ponto fixo aproximado (inteiro): x\* = 21
Intervalo \[32, 63] - Ponto fixo aproximado (inteiro): x\* = 42

```

---

## 2. Script `banach.py`

### 2.1 Relação com o Teorema

O script aplica exatamente o que o teorema afirma: definimos uma função contraente em um intervalo específico e usamos iteração para chegar ao ponto fixo.

### 2.2 Objetivo do Script

* Construir funções matematicamente válidas e determinísticas
* Evitar aleatoriedade
* Mostrar, para cada `n`, que o ponto fixo está dentro do intervalo e não é sempre o centro

### 2.3 Exemplo de Saída

```bash
Intervalo [64, 127] - Ponto fixo aproximado (inteiro): x* = 85
Intervalo [128, 255] - Ponto fixo aproximado (inteiro): x* = 170
Intervalo [256, 511] - Ponto fixo aproximado (inteiro): x* = 341
````

### 2.4 Funcionamento Interno

1. Define o intervalo com base em `n`
2. Escolhe um ponto fixo específico dentro do intervalo
3. Calcula os parâmetros da função contraente
4. Aplica a função repetidamente até convergir
5. Arredonda o resultado final para inteiro

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10**
* Sem bibliotecas externas
* Código 100% compatível com qualquer sistema com Python instalado

---

## 3. Extras

### 3.1 Licença

Este projeto está licenciado sob os termos da **MIT License**.

### 3.2 Referências

* Wikipédia: [Teorema do Ponto Fixo de Banach](https://pt.wikipedia.org/wiki/Teorema_do_ponto_fixo_de_Banach)
* Canal QB: [https://canalqb.blogspot.com](https://canalqb.blogspot.com)

### 3.3 Testes e Validações

* Verificado em Python 3.8.10
* Saída validada manualmente
* Convergência garantida pela construção matemática

---

## 4. Contato

* Feito por **CanalQb** no GitHub
* Visite o blog: [canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**função contraente**: uma função que sempre aproxima os valores ao invés de afastá-los. Em outras palavras, ela diminui a diferença entre os números.

**ponto fixo**: um valor que, ao ser passado para a função, retorna ele mesmo. Ex: se T(5) = 5, então 5 é um ponto fixo.

**iterar**: aplicar uma função repetidamente sobre o resultado anterior. Ex: começar com 2, aplicar T, depois T de T(2), e assim por diante.

**espaço completo**: um conjunto de números onde toda sequência que se aproxima de algum valor realmente chega a esse valor dentro do próprio conjunto.

**lambda (L)**: apenas uma letra usada para representar um número entre 0 e 1 que mede "o quanto a função encolhe" as distâncias.
