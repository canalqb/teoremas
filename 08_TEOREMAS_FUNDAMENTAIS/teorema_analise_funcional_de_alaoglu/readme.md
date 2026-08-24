# 🔍 - Teorema de Alaoglu
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)  

## Frase do Teorema

> A bola unitária do espaço dual de um espaço normado é compacta na topologia fraca-estrela – ou seja, mesmo em espaços infinitos, existe um limite bem comportado para as funções lineares contínuas definidas nesse espaço.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  

* [2. Script `alaoglu_potencias_mersenne.py`](#2-script-alaoglu_potencias_mersennepy)  
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
O teorema afirma que, em espaços com infinitas dimensões, mesmo assim existe um tipo de "limite" para as funções que atuam nesses espaços, garantindo que podemos "controlar" o comportamento dessas funções numa bola de raio 1, se olharmos com uma forma específica de analisar proximidade (topologia fraca-estrela).

### 1.2 Exemplos Práticos  
Em termos simples, imagine que você tem uma coleção enorme de funções, e quer saber se essa coleção "fecha" de forma ordenada para que você possa fazer contas com elas sem surpresas. O teorema garante essa organização, mesmo no infinito.

### 1.3 Explicação Detalhada  
A compactação citada é uma forma de dizer que o conjunto não é "espalhado demais" e que qualquer sequência de funções nessa bola unitária tem uma subsequência que converge, ajudando em muitas provas e aplicações da matemática avançada.

### 1.4 Aplicações  
É fundamental para análise funcional, otimização, física matemática, e áreas onde precisamos trabalhar com infinitos graus de liberdade, como sistemas quânticos ou análise de sinais.

### 1.5 Análise da Tabela  
A tabela apresentada mostra intervalos baseados em potências de 2, começando em 2^N e terminando em 2^(N+1) - 1, números que são chamados de números de Mersenne. Esses intervalos são usados para entender limites e comportamentos crescentes, representando "espaços" que o teorema pode abranger.  

---

## 2 Script `alaoglu_potencias_mersenne.py`

### 2.1 Relação com o Teorema  
O script não implementa o teorema matematicamente (pois ele é abstrato), mas usa os conceitos de intervalos baseados em potências de 2 para estimar valores dentro desses espaços, respeitando os limites naturais dados pela estrutura dos números.

### 2.2 Objetivo do Script  
Gerar e mostrar uma tabela com intervalos entre potências de 2 e números de Mersenne e estimar valores dentro desses intervalos, usando uma fórmula simples que não depende de valores esperados já conhecidos.

### 2.3 Exemplo de Saída  

```

Tabela de intervalos baseados em potências de 2 e números de Mersenne:
N | Inicio (2^N) |    Fim (2^(N+1))-1
-------------------------------------

0 |            1 |                  1
1 |            2 |                  3
2 |            4 |                  7
3 |            8 |                 15
4 |           16 |                 31
5 |           32 |                 63
6 |           64 |                127
7 |          128 |                255
8 |          256 |                511
9 |          512 |               1023

Tabela com valores estimados baseados no teorema (sem usar coluna esperada):
N | Inicio (2^N) |  Estimado |    Fim (2^(N+1))-1
-------------------------------------------------

0 |            1 |         1 |                  1
1 |            2 |         2 |                  3
2 |            4 |         5 |                  7
3 |            8 |        10 |                 15
4 |           16 |        22 |                 31
5 |           32 |        44 |                 63
6 |           64 |        89 |                127
7 |          128 |       178 |                255
8 |          256 |       358 |                511
9 |          512 |       716 |               1023

```

### 2.4 Funcionamento Interno  
- Calcula os valores de 2^N e 2^(N+1) - 1 para N de 0 a 9.  
- Para cada N, gera um valor estimado baseado em uma média ponderada entre os extremos do intervalo.  
- Imprime a tabela com esses valores.  

### 2.5 Tecnologias e Requisitos  
- Python versão 3.8.10  
- Nenhuma biblioteca externa é necessária.  

---

## 3 Extras

### 3.1 Licença  
MIT License - Código aberto e livre para uso e modificação.

### 3.2 Referências  
- Wikipédia - Teorema de Alaoglu: https://en.wikipedia.org/wiki/Alaoglu%27s_theorem  
- Explicações básicas de análise funcional e números de Mersenne.

### 3.3 Testes e Validações  
- O script foi testado em Python 3.8.10 e apresenta os valores conforme esperado.  

---

## 4 Contato

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*

---

## 5 Nota

**bola unitária:** conjunto de todos os elementos do espaço cujo "tamanho" (norma) é menor ou igual a 1.  

**espaço dual:** conjunto das funções que associam números aos elementos do espaço original, respeitando certas regras (linearidade e continuidade).  

**topologia fraca-estrela:** uma forma de olhar para a proximidade entre funções no espaço dual, diferente da forma usual, focada no comportamento delas em pontos específicos.  

**compacta:** significa que o conjunto é limitado e "fechado", ou seja, ele não se espalha infinitamente e inclui seus pontos de limite, facilitando o estudo matemático.  

**número de Mersenne:** número da forma 2^(n) - 1, que tem aplicações em matemática, especialmente em números primos e teoria dos números.
