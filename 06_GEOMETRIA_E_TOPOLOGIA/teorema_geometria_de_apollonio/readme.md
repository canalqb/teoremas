# 📐 - Mediana em Triângulos com Valores Especiais

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Frase do conceito

> A mediana em um triângulo é o segmento que une um vértice ao ponto médio do lado oposto, dividindo o triângulo em duas partes com áreas iguais.

## Sumário

* [1. Introdução ao Conceito](#1-introdução-ao-conceito)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
* [2. Script `Apolonio.py`](#2-script-apoloniopy)

  * [2.1 Relação com o Conceito](#21-relação-com-o-conceito)
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

## 1. Introdução ao Conceito

### 1.1 Resumo

A mediana de um triângulo é uma linha que sai de um dos vértices e vai até o ponto que divide o lado oposto em duas partes iguais. Essa linha tem um comprimento que pode ser calculado se soubermos os lados do triângulo.

### 1.2 Exemplos Práticos

Imagine um triângulo com lados medindo alguns números especiais, como potências de 2 e números próximos a potências de 2. O comprimento da mediana pode ser calculado para esses casos, ajudando a entender melhor a geometria desses triângulos.

### 1.3 Explicação Detalhada

O comprimento da mediana que sai do vértice A até o ponto médio do lado BC pode ser calculado com a fórmula:
**AM² = (2 \* AB² + 2 \* AC² - BC²) / 4**
Aqui, AB, AC e BC são os comprimentos dos lados do triângulo. A fórmula mostra como usar os lados para achar a mediana, mesmo sem desenhar o triângulo.

### 1.4 Aplicações

Esse cálculo é útil para analisar propriedades geométricas de triângulos com lados definidos por sequências matemáticas, especialmente em estudos de padrões, algoritmos e até na computação gráfica.

---

## 2. Script `Apolonio.py`

### 2.1 Relação com o Conceito

O script calcula o comprimento da mediana em triângulos cujos lados seguem padrões específicos baseados em potências de 2 e valores próximos.

### 2.2 Objetivo do Script

Testar combinações dos valores dos lados e verificar para quais casos o cálculo da mediana resulta em valores reais e positivos, significando triângulos válidos.

### 2.3 Exemplo de Saída

```
Combinação 1: AB = 1, AC = 1, BC = 2  
  AM^2 = 0.0  
  AM (mediana) = 0.0000  
----------------------------------------  
Combinação 12: AB = 1, AC = 3, BC = 2  
  AM^2 = 4.0  
  AM (mediana) = 2.0000  
----------------------------------------
```

### 2.4 Funcionamento Interno

O script cria listas para os valores dos lados com base em potências de 2 e valores próximos. Depois, combina esses valores em todas as possíveis combinações e calcula a mediana usando a fórmula explicada. O script imprime resultados somente para valores válidos (onde o cálculo da mediana não gera número negativo).

### 2.5 Tecnologias e Requisitos

* Python 3.8.10
* Biblioteca padrão do Python: math e itertools

---

## 3 Extras

### 3.1 Licença

MIT License

### 3.2 Referências

* Conceitos básicos de geometria sobre triângulos e medianas
* Documentação Python (math, itertools)

### 3.3 Testes e Validações

O script verifica se o valor calculado para AM² é maior ou igual a zero antes de calcular a raiz quadrada, evitando erros com valores imaginários.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **Mediana:** segmento que sai de um vértice do triângulo até o ponto médio do lado oposto, dividindo-o em duas partes iguais.
* **Potência de 2:** resultado de multiplicar o número 2 por ele mesmo várias vezes (exemplo: 2^3 = 2 x 2 x 2 = 8).
* **Raiz quadrada:** número que, multiplicado por ele mesmo, dá o valor original (exemplo: raiz quadrada de 9 é 3, porque 3 x 3 = 9).
* **Triângulo válido:** triângulo cujos lados satisfazem a condição de que a soma de dois lados é maior que o terceiro.
* **Número imaginário:** resultado de uma operação matemática que não pode ser representada na reta dos números reais (exemplo: raiz quadrada de número negativo).
