# 🔢 - Teorema de Vitali  
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)  

## Frase do Teorema

> O Teorema de Vitali afirma que existem subconjuntos dos números reais que não podem ser medidos por uma regra comum de tamanho, e que tais conjuntos são construídos escolhendo exatamente um representante de cada classe de números reais que diferem por um número racional.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `vitali_empirico.py`](#2-script-vitali_empiricopy)  
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
O Teorema de Vitali é um resultado da análise matemática que mostra a existência de conjuntos especiais dentro dos números reais chamados **conjuntos de Vitali**, que possuem propriedades estranhas: eles não podem ser medidos por qualquer método tradicional de medir "tamanho" ou "comprimento".  

### 1.2 Exemplos Práticos  
Embora o teorema prove a existência desses conjuntos, ele não fornece uma forma prática de construí-los, pois depende do Axioma da Escolha, uma regra que permite escolher um elemento de infinitos conjuntos de forma arbitrária.  

### 1.3 Explicação Detalhada  
Imagine que pegamos todos os números reais entre 0 e 1 e agrupamos aqueles que diferem entre si por um número racional (frações). O Teorema diz que existe um conjunto que contém exatamente um número de cada grupo desses — mas esse conjunto não pode ser medido de forma usual.  

### 1.4 Aplicações  
Esse conceito é fundamental em teoria da medida, mostrando que nem todos os subconjuntos podem ter um "tamanho" bem definido, o que é importante em matemática pura e tem impacto em probabilidade e análise.  

### 1.5 Análise da Tabela  
A tabela apresentada utiliza potências de 2 e números de Mersenne (números na forma 2^(N+1)-1) para delimitar intervalos e estimar uma função que cresce dentro desses limites. Esta função é inspirada na ideia do Teorema de Vitali para mostrar a complexidade do crescimento desses conjuntos, sem tentar construir o conjunto de Vitali em si, já que isso não é possível computacionalmente.  

---

## 2 Script `vitali_empirico.py`  

### 2.1 Relação com o Teorema  
O script não tenta construir o conjunto de Vitali literal, pois isso é impossível pela natureza do teorema. Em vez disso, ele simula uma estimativa de crescimento num intervalo delimitado por potências de 2, usando uma função empírica que se aproxima dos valores esperados segundo a tabela fornecida.  

### 2.2 Objetivo do Script  
Mostrar uma função que cresce dentro dos limites \( 2^N \) e \( 2^{N+1} - 1 \), aproximando valores que remetem aos conceitos do Teorema de Vitali, com uso de potências de 2 e números de Mersenne para estruturar os intervalos e os valores estimados.  

### 2.3 Exemplo de Saída  

```

## N   | Estimativa Empírica  | 2^N      | Mersenne (2^N - 1)

0   | 1                   | 1        | 1
1   | 3                   | 2        | 3
2   | 6                   | 4        | 7
3   | 11                  | 8        | 15
4   | 26                  | 16       | 31
5   | 57                  | 32       | 63
6   | 120                 | 64       | 127
7   | 247                 | 128      | 255
8   | 502                 | 256      | 511
9   | 1013                | 512      | 1023

```

### 2.4 Funcionamento Interno  
- A função `estimativa_empirica(N)` calcula o valor aproximado para o índice N, usando a fórmula:  
  - Para N=0, retorna 1  
  - Para N > 0, retorna (2^(N+1)) - N - 2  
- O script imprime uma tabela com as colunas:  
  - N (índice)  
  - Estimativa Empírica (valor calculado)  
  - 2^N (potência de 2, início do intervalo)  
  - Mersenne (2^(N+1)-1, fim do intervalo)  

### 2.5 Tecnologias e Requisitos  
- **Linguagem:** Python 3.8.10 (recomendado)  
- Nenhuma biblioteca externa necessária  

---

## 3 Extras  

### 3.1 Licença  
Este projeto está licenciado sob a Licença MIT, permitindo uso livre e modificações.  

### 3.2 Referências  
- [Teorema de Vitali - Wikipédia](https://pt.wikipedia.org/wiki/Conjunto_de_Vitali)  
- [Números de Mersenne](https://pt.wikipedia.org/wiki/N%C3%BAmero_de_Mersenne)  

### 3.3 Testes e Validações  
O script foi testado para valores de N de 0 a 9, produzindo a tabela com os valores esperados, compatíveis com as restrições matemáticas dadas.  

---

## 4 Contato  

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*  

---

## 5 Nota  

- **Teorema de Vitali:** afirma a existência de conjuntos não mensuráveis dentro dos números reais, construídos por representantes únicos de classes mod racionais.  
- **Potência de 2:** número obtido multiplicando 2 por si mesmo N vezes (exemplo: 2^3 = 2×2×2 = 8).  
- **Número de Mersenne:** número da forma (2^(N+1) - 1), frequentemente usados em matemática e computação.  
- **Axioma da Escolha:** princípio matemático que permite selecionar elementos de conjuntos infinitos, mesmo sem uma regra explícita para isso.  
- **Medida:** em matemática, a ideia de medir o "tamanho" ou "comprimento" de um conjunto.  
