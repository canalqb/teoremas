# 🧩 - Teorema Dos Ngulos Internos De Poligonos
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  

## Frase do conceito

> A soma dos ângulos internos de um polígono com número de lados igual a um número de Mersenne (que é 2 elevado a um número primo menos 1) é dada multiplicando-se 180 graus pelo número de lados menos 2.

---

## Sumário

* [1. Introdução ao Conceito](#1-introdução-ao-conceito)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
* [2. Script `mersenne_poligono.py`](#2-script-mersenne_poligonopy)  
  * [2.1 Relação com o Conceito](#21-relação-com-o-conceito)  
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

## 1. Introdução ao Conceito

### 1.1 Resumo

Um polígono é uma figura formada por vários lados que se unem formando ângulos. A soma de todos os seus ângulos internos depende da quantidade de lados.

Quando essa quantidade de lados é um número especial chamado número de Mersenne — que tem a forma 2 elevado a um número primo menos 1 — podemos calcular a soma dos ângulos internos usando uma fórmula simples.

---

### 1.2 Exemplos Práticos

- Para p = 3, número de Mersenne = 2^3 - 1 = 7 lados  
  Soma dos ângulos internos = (7 - 2) × 180 = 900 graus  

- Para p = 11, número de Mersenne = 2^11 - 1 = 2047 lados  
  Soma dos ângulos internos = (2047 - 2) × 180 = 368100 graus

---

### 1.3 Explicação Detalhada

A soma dos ângulos internos de qualquer polígono é:

**(n - 2) × 180**

onde *n* é o número de lados.

Se *n* for um número de Mersenne, ou seja:

**n = 2^p - 1**, com *p* sendo um número primo,

então a soma fica:

**(2^p - 1 - 2) × 180 = (2^p - 3) × 180**

---

### 1.4 Aplicações

- Entender propriedades geométricas especiais de polígonos.  
- Relacionar conceitos matemáticos como potências, números primos e figuras geométricas.  
- Uso em matemática pura, criptografia e teoria dos números.

---

## 2. Script `mersenne_poligono.py`

### 2.1 Relação com o Conceito

O script calcula o número de lados do polígono usando o número de Mersenne e depois a soma dos seus ângulos internos.

---

### 2.2 Objetivo do Script

- Receber um número primo *p*.  
- Calcular *n = 2^p - 1*.  
- Calcular e mostrar a soma dos ângulos internos para o polígono com *n* lados.

---

### 2.3 Exemplo de Saída

```

Cálculo da soma dos ângulos internos para polígono com lados de número de Mersenne
Digite um número primo p: 31

Número de lados (Mersenne): n = 2^31 - 1 = 2147483647
Soma dos ângulos internos do polígono: (n - 2) x 180° = 386547056100°

```

---

### 2.4 Funcionamento Interno

- Calcula n como 2 elevado a p menos 1.  
- Calcula a soma dos ângulos internos como (n - 2) vezes 180.  
- Imprime os resultados para o usuário.

---

### 2.5 Tecnologias e Requisitos

- Desenvolvido em **Python 3.8.10**  
- Funciona em qualquer sistema com Python instalado  
- Interface simples via terminal

---

## 3. Extras

### 3.1 Licença

Projeto sob licença **MIT**, permitindo uso, modificação e distribuição livre.

---

### 3.2 Referências

- [Números de Mersenne - Wikipédia](https://pt.wikipedia.org/wiki/Número_de_Mersenne)  
- Conceitos básicos de polígonos e ângulos internos

---

### 3.3 Testes e Validações

O script assume que o número *p* digitado é primo. Para melhorar, pode-se adicionar uma verificação para confirmar isso.

---

## 4. Contato

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

{**Número primo**}: número natural maior que 1 que só pode ser dividido por 1 e por ele mesmo, sem deixar resto.  
{**Número de Mersenne**}: número que pode ser escrito como 2 elevado a um número primo, menos 1 (exemplo: 3, 7, 31, 127...).  
{**Polígono**}: figura fechada formada por segmentos de reta que se juntam formando ângulos.  
{**Ângulo interno**}: espaço entre dois lados adjacentes dentro do polígono.  
{**Soma dos ângulos internos**}: resultado da adição de todos os ângulos internos de um polígono.
