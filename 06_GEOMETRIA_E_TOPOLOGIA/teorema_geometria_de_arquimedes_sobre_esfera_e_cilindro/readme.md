# 🧩 - De Arquimedes Sobre Esfera E Cilindro

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Frase do estudo

> O volume da esfera é sempre dois terços do volume do cilindro que a envolve perfeitamente, assim como a área da superfície da esfera é dois terços da área da superfície do cilindro correspondente.

## Sumário

* [1. Introdução ao Estudo](#1-introdução-ao-estudo)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `esfera_e_cilindro.py`](#2-script-esfera_e_cilindropy)

  * [2.1 Relação com o Estudo](#21-relação-com-o-estudo)
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

## 1 Introdução ao Estudo

### 1.1 Resumo

Este estudo mostra uma relação fixa entre a esfera e o cilindro que a envolve: o volume da esfera é sempre 2/3 do volume do cilindro, e a área da superfície da esfera é também 2/3 da área da superfície do cilindro. Essa propriedade vale para esferas inscritas em cilindros onde a altura do cilindro é igual ao diâmetro da esfera.

### 1.2 Exemplos Práticos

Para diferentes valores do raio da esfera, inclusive usando números especiais chamados **números de Mersenne** (que são da forma 2ⁿ - 1), calculamos o volume e a área da esfera e do cilindro, mostrando que essa proporção se mantém.

### 1.3 Explicação Detalhada

* Volume da esfera = (4/3) × π × raio³
* Volume do cilindro = π × raio² × altura
* Como a altura do cilindro é o dobro do raio (altura = 2 × raio), o volume do cilindro = 2 × π × raio³
* Assim, a razão volume esfera/volume cilindro = (4/3)πr³ / 2πr³ = 2/3

O mesmo vale para a área da superfície, considerando que:

* Área da esfera = 4 × π × raio²
* Área do cilindro (incluindo as bases) = 2 × π × raio × altura + 2 × π × raio² = 6 × π × raio²
* A razão área esfera / área cilindro = 4πr² / 6πr² = 2/3

### 1.4 Aplicações

Esse conhecimento é útil em várias áreas, como engenharia e design, onde entender a relação entre volumes e superfícies é importante para economia de materiais e otimização de espaços.

### 1.5 Análise da Tabela

Na tabela gerada pelo script, para cada valor de n, mostramos os valores do raio, volume e área da esfera e do cilindro, e confirmamos a razão constante de 0.6667 (ou 2/3).

---

## 2 Script `esfera_e_cilindro.py`

### 2.1 Relação com o Estudo

O script calcula os volumes e áreas da esfera e cilindro para raios que são potências de 2 e números de Mersenne (2ⁿ - 1), mostrando a relação de 2/3 nas medidas.

### 2.2 Objetivo do Script

Visualizar graficamente a esfera e o cilindro para diferentes raios e imprimir uma tabela clara com os valores numéricos e suas relações.

### 2.3 Exemplo de Saída

```
--- n = 1 ---
  Raio |   Vol Esfera |   Vol Cilindro | Relação Vol |  Área Esfera |  Área Cilindro | Relação Área
------------------------------------------------------------------------------------------
     2 |        33.51 |          50.27 |      0.6667 |        50.27 |          75.40 |      0.6667
     1 |         4.19 |           6.28 |      0.6667 |        12.57 |          18.85 |      0.6667
```

### 2.4 Funcionamento Interno

O script:

* Calcula volumes e áreas conforme as fórmulas indicadas.
* Gera gráficos 3D mostrando a esfera em vermelho e o cilindro em azul translúcido.
* Imprime uma tabela formatada com os resultados para vários valores de n.

### 2.5 Tecnologias e Requisitos

* Python 3.8.10
* Bibliotecas: `numpy` para cálculos matemáticos, `matplotlib` para gráficos 3D.

---

## 3 Extras

### 3.1 Licença

MIT License – Uso livre, com atribuição.

### 3.2 Referências

* [https://pt.wikipedia.org/wiki/Esfera](https://pt.wikipedia.org/wiki/Esfera)
* [https://pt.wikipedia.org/wiki/Cilindro\_circular\_reto](https://pt.wikipedia.org/wiki/Cilindro_circular_reto)
* Explicações básicas de geometria em livros escolares.

### 3.3 Testes e Validações

Testado para valores de n entre 1 e 10, confirmando a razão constante de 2/3 para volume e área.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5 Nota

* **Pi**: constante matemática que representa a relação entre a circunferência e o diâmetro de um círculo (aproximadamente 3,1416).
* **Potência**: resultado de multiplicar um número por ele mesmo várias vezes; por exemplo, 2⁴ significa 2×2×2×2 = 16.
* **Número de Mersenne**: número que pode ser escrito como 2ⁿ - 1, onde n é um número natural.
* **Raio**: distância do centro de uma esfera ou círculo até sua borda.
* **Volume**: quantidade de espaço ocupado por um objeto tridimensional.
* **Área da superfície**: medida da superfície externa de um objeto tridimensional. 
