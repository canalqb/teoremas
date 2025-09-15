# 🌐 - Teorema da Esfera de Gauss  
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  

## Frase do Teorema

> A curvatura de uma superfície em um ponto mede como a superfície “dobra” naquele ponto, e está relacionada à forma como os vetores normais daquela região são mapeados para a esfera unitária.  

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script Esfera_de_Gauss.py](#2-script-esfera_de_gausspy)  
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
O teorema da Esfera de Gauss relaciona a forma como uma superfície curva é mapeada por seus vetores normais para uma esfera. A ideia central é que a curvatura em cada ponto da superfície pode ser vista pela forma como aquela região da superfície “projeta” sua normal na esfera unitária.  

### 1.2 Exemplos Práticos  
Imagine uma bola de futebol: a superfície é curva e os vetores normais apontam para fora. Quando você olha para a “imagem” desses vetores normais na esfera, eles cobrem uma área proporcional à curvatura da bola. Uma superfície plana tem todos os vetores normais apontando na mesma direção, mapeando para um ponto só, indicando curvatura zero.  

### 1.3 Explicação Detalhada  
A curvatura Gaussiana é um número que expressa o quanto a superfície está “dobrando” localmente. O teorema diz que a área da imagem do mapeamento dos vetores normais de uma região da superfície é igual à integral dessa curvatura naquela região.  

### 1.4 Aplicações  
Esse conceito é importante em geometria diferencial, física, engenharia e em áreas que lidam com superfícies curvas, como modelagem 3D, óptica e análise de formas.  

### 1.5 Análise da Tabela  
A tabela criada no script apresenta valores simulados de áreas de regiões na superfície e suas imagens na esfera. A razão entre essas áreas é uma forma aproximada de entender como a curvatura varia, ilustrando o princípio do teorema.  

---

## 2. Script Esfera_de_Gauss.py  

### 2.1 Relação com o Teorema  
O script simula a ideia do mapeamento da superfície para a esfera através de uma tabela com áreas crescentes e áreas correspondentes na esfera, calculando uma curvatura aproximada para cada intervalo.  

### 2.2 Objetivo do Script  
Gerar uma tabela que mostra:  
- Uma área da superfície (crescendo exponencialmente),  
- A área da imagem projetada na esfera,  
- A curvatura aproximada como a relação entre as duas áreas.  

### 2.3 Exemplo de Saída  

```

## n |   Área Superfície (A\_n) |   Área Esfera (A\_n prime) |  Curvatura K\_n

0 |                     1 |                   1.00 |       1.000000
1 |                     2 |                   1.41 |       0.707107
2 |                     4 |                   2.00 |       0.500000
3 |                     8 |                   2.83 |       0.353553
4 |                    16 |                   4.00 |       0.250000
5 |                    32 |                   5.66 |       0.176777
6 |                    64 |                   8.00 |       0.125000
7 |                   128 |                  11.31 |       0.088388
8 |                   256 |                  16.00 |       0.062500
9 |                   512 |                  22.63 |       0.044194
10 |                 1,024 |                  32.00 |       0.031250

```

### 2.4 Funcionamento Interno  
Para cada valor de n de 0 a 10:  
- Calcula uma área da superfície como 2 elevado a n.  
- Calcula a área da imagem na esfera como 2 elevado a (n dividido por 2).  
- Calcula a curvatura aproximada como a razão entre a área na esfera e a área da superfície.  

### 2.5 Tecnologias e Requisitos  
- Python 3.8.10 ou superior  
- Ambiente de execução padrão para scripts Python  

---

## 3 Extras  

### 3.1 Licença  
Este projeto está licenciado sob a licença MIT.  

### 3.2 Referências  
- Livros e artigos sobre geometria diferencial e curvatura Gaussiana.  
- Recursos didáticos sobre superfícies e mapeamento da normal Gaussiana.  

### 3.3 Testes e Validações  
O script foi testado em Python 3.8.10. A saída foi verificada para garantir que as operações matemáticas e o formato da tabela estejam corretos.  

---

## 4 Contato  

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*  

---

## 5. Nota  

**Curvatura Gaussiana**: um número que descreve o quanto uma superfície curva localmente, indicando se a região é “achatada”, “côncava” ou “convexa”.  
**Normal Gaussiana**: o vetor perpendicular à superfície em um ponto, usado para descrever a orientação da superfície.  
**Integral**: uma soma contínua que calcula a área ou outra medida em regiões infinitesimais.  
**Exponencial**: operação matemática onde um número é multiplicado por ele mesmo várias vezes, como 2^n (2 elevado a n).  
**Razão**: uma comparação entre dois números, geralmente representada como uma divisão.  
**Superfície**: uma forma bidimensional que pode ser plana ou curva, como uma folha de papel ou uma bola.  
**Imagem (no contexto de mapeamento)**: o resultado da aplicação de uma função em um conjunto, como os vetores normais mapeados para a esfera.  
**Esfera unitária**: esfera de raio 1 usada como referência para medir direções e áreas.  
**Mapa ou mapeamento**: uma regra ou função que associa cada ponto de um conjunto a um ponto de outro conjunto.  
```
