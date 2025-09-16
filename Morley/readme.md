# 🧩 - Teorema de Morley

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Frase do Teorema

> "Os pontos de interseção dos trisectores dos ângulos internos de qualquer triângulo formam um triângulo equilátero." – Em outras palavras, se você dividir cada ângulo interno de um triângulo em três partes iguais e ligar certos pontos resultantes dessas divisões, vai aparecer um triângulo com todos os lados iguais, independente do formato inicial.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
* [2. Script `triangulo_morley.py`](#2-script-triangulo_morleypy)

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

## 1 Introdução ao Teorema

### 1.1 Resumo

O Teorema de Morley mostra que, mesmo em triângulos muito diferentes (com lados e ângulos variados), se você dividir cada ângulo em três partes iguais (trisecar) e ligar as linhas certas, sempre surge um triângulo equilátero dentro do original. Isso é surpreendente porque acontece para qualquer triângulo.

### 1.2 Exemplos Práticos

* Na geometria, pode ser usado para construir triângulos equiláteros de forma indireta.
* Em design gráfico e arte, para criar padrões que envolvem divisão de ângulos.

### 1.3 Explicação Detalhada

Imagine que você tem um triângulo qualquer. Cada canto tem um ângulo — a abertura entre os dois lados que se encontram. Agora, você divide cada ângulo em três partes iguais, como se cortasse uma pizza em três pedaços iguais. Aí, você desenha linhas chamadas "trisecantes" que dividem esses ângulos. O ponto onde certas dessas linhas se cruzam dentro do triângulo forma outro triângulo. O que é impressionante é que esse novo triângulo sempre terá seus três lados iguais — é equilátero, não importa o formato do triângulo inicial.

### 1.4 Aplicações

* Educação matemática: ajuda a mostrar propriedades surpreendentes da geometria.
* Modelagem geométrica e computação gráfica: para gerar formas específicas baseadas em ângulos.

---

## 2 Script `triangulo_morley.py`

### 2.1 Relação com o Teorema

Embora o script não implemente diretamente a construção dos trisecantes do Teorema de Morley, ele serve para entender e visualizar triângulos no plano 2D, calculando lados, ângulos e plotando os vértices. Isso é útil para quem quer estudar o teorema, pois é fundamental entender como manipular triângulos antes de aplicar as trisecantes.

### 2.2 Objetivo do Script

* Calcular os ângulos internos de um triângulo a partir dos seus lados usando a lei dos cossenos (uma regra para encontrar ângulos em triângulos).
* Calcular as coordenadas dos vértices desse triângulo para desenhá-lo num plano 2D.
* Mostrar visualmente o triângulo com os lados e ângulos indicados.

### 2.3 Exemplo de Saída

```
Lados do triângulo: a=64, b=48, c=64
Ângulos internos:
A = 58.99°
B = 62.01°
C = 59.00°
```

Em seguida, aparece o desenho do triângulo com vértices, lados e ângulos indicados.

### 2.4 Funcionamento Interno

* A função `lei_dos_cossenos` calcula os ângulos usando a fórmula que envolve o comprimento dos lados (a, b, c).
* A função `calcula_vertices` posiciona o triângulo no plano, assumindo o lado c na base, sobre o eixo horizontal.
* A função `plot_triangulo` usa a biblioteca matplotlib para desenhar o triângulo, mostrando os vértices e os valores dos ângulos e lados.

### 2.5 Tecnologias e Requisitos

* Python 3.8.10
* Biblioteca `matplotlib` para gráficos.
* Biblioteca padrão `math` para funções matemáticas.

---

## 3 Extras

### 3.1 Licença

Este projeto está sob licença MIT — você pode usar, modificar e distribuir livremente.

### 3.2 Referências

* [Teorema de Morley - Wikipedia](https://pt.wikipedia.org/wiki/Teorema_de_Morley)
* [Lei dos Cossenos](https://pt.wikipedia.org/wiki/Lei_dos_cossenos)

### 3.3 Testes e Validações

Testado com diferentes valores de lados para garantir que o triângulo seja válido e os ângulos corretos sejam calculados.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5 Nota

* **ângulo**: abertura entre dois lados que se encontram em um ponto (vértice).
* **trisecar**: dividir algo em três partes iguais.
* **triângulo equilátero**: triângulo que tem os três lados com o mesmo comprimento.
* **lei dos cossenos**: fórmula que relaciona os lados e os ângulos de um triângulo, permitindo calcular ângulos se você souber os lados.
* **coordenadas**: valores que dizem onde um ponto está em um plano, usando duas medidas (como x e y).
