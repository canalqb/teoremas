# 📐 - Teorema Poincaré–Hopf  
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  

## Frase do Teorema  

> A soma dos "índices" dos pontos especiais em uma superfície é igual a uma característica que mede a forma geral dessa superfície – ou seja, um número que descreve a topologia dela.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `poincare_hopf_mersenne.py`](#2-script-poincare_hopf_mersennepy)  
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
O teorema relaciona propriedades locais de pontos especiais em uma superfície (chamados de pontos críticos ou zeros de um campo vetorial) com uma propriedade global que caracteriza a forma da superfície. Essa soma dos índices desses pontos é um número importante que fala sobre a topologia da superfície.

### 1.2 Exemplos Práticos  
Imagine que você tem uma esfera e um campo de vento sobre ela, onde o vento para em alguns pontos. O teorema diz que se somarmos certas características desses pontos onde o vento para, obteremos um número que depende só da esfera, independente de como o vento sopra.

### 1.3 Explicação Detalhada  
Em linguagem simples, o teorema mostra que a soma dos "efeitos locais" (índices) dos pontos especiais do campo vetorial coincide com uma medida global da superfície chamada "característica de Euler", que é como um código da forma da superfície.

### 1.4 Aplicações  
Este conceito é usado em matemática pura e também em física para entender propriedades globais de espaços, sistemas dinâmicos e até no estudo de formas geométricas complexas.

### 1.5 Análise da Tabela  
Na tabela apresentada, temos intervalos que começam em potências de 2 e terminam em números de Mersenne (que são potências de 2 menos 1). O valor esperado está entre esses dois, mostrando um crescimento rápido que pode representar a soma dos índices dos pontos para diferentes níveis (N). O script usa essas bordas para tentar aproximar esses valores sem usar diretamente o valor esperado.

---

## 2. Script `poincare_hopf_mersenne.py`  

### 2.1 Relação com o Teorema  
O script usa potências de 2 e números de Mersenne para delimitar intervalos e calcula uma aproximação para a soma dos índices desses pontos especiais, alinhando com o conceito da soma ser um número que cresce entre esses valores.

### 2.2 Objetivo do Script  
Calcular, para cada N, um valor aproximado da soma dos índices, usando uma combinação entre a potência de 2 e o número de Mersenne relacionados a N, sem usar diretamente os valores esperados fornecidos.

### 2.3 Exemplo de Saída  
```

## N   | Inicio (2^N) | Aprox. Poincaré–Hopf   | Fim (2^(N+1))-1

0   | 1            | 1                      | 1
1   | 2            | 2                      | 3
2   | 4            | 5                      | 7
3   | 8            | 11                     | 15
4   | 16           | 23                     | 31
5   | 32           | 47                     | 63
6   | 64           | 94                     | 127
7   | 128          | 188                    | 255
8   | 256          | 377                    | 511
9   | 512          | 754                    | 1023

```

### 2.4 Funcionamento Interno  
Para cada N, o script:  
- Calcula o início do intervalo como 2^N  
- Calcula o fim do intervalo como (2^(N+1)) - 1 (número de Mersenne)  
- Calcula uma aproximação ponderada entre a média geométrica e a média aritmética desses dois números, para simular um crescimento que representa a soma dos índices.

### 2.5 Tecnologias e Requisitos  
- Python versão 3.8.10 (ou superior)  

---

## 3. Extras  

### 3.1 Licença  
Este projeto está sob licença MIT.  

### 3.2 Referências  
- Conceitos básicos de campos vetoriais e topologia diferencial  
- Números de Mersenne e potências de 2  

### 3.3 Testes e Validações  
Os valores produzidos pelo script são aproximações e devem ser usados para fins didáticos ou exploratórios, não como resultados formais.

---

## 4 Contato  

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*

---

## 5. Nota  

- **_Índice_**: número que representa a "força" ou "tipo" de um ponto especial em um campo vetorial  
- **_Característica de Euler_**: número que mede a forma geral de uma superfície, como o número de buracos ou "pontos de curvatura"  
- **_Campo vetorial_**: uma "função" que associa a cada ponto do espaço um vetor (como uma seta indicando direção e intensidade)  
- **_Média geométrica_**: tipo de média que multiplica os números e tira a raiz, usada para valores que crescem exponencialmente  
- **_Média aritmética_**: média simples somando os números e dividindo pela quantidade  
- **_Número de Mersenne_**: números que são uma potência de dois menos 1, como 3, 7, 15, 31...  
