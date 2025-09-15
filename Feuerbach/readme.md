# 📐 - Teorema de Feuerbach  
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)  

## Frase do Teorema  

> O círculo que passa por nove pontos especiais de um triângulo toca internamente o círculo que fica dentro dele e toca externamente outros círculos importantes que ficam fora dele – em outras palavras, esses círculos se encaixam perfeitamente ao redor e dentro do triângulo.

## Sumário  

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script feuerbach_model.py](#2-script-feuerbach_modelpy)  
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

## 1. Introdução ao Teorema  

### 1.1 Resumo  
Este conceito fala sobre uma relação especial entre círculos relacionados a um triângulo. Existem círculos importantes que passam por pontos notáveis do triângulo, e eles tocam uns aos outros de maneira muito precisa e elegante.  

### 1.2 Exemplos Práticos  
Imagine um triângulo desenhado num papel. Dentro dele, existe um círculo que toca os três lados. Também existem círculos fora dele, e outro círculo que passa por nove pontos importantes do triângulo. Esses círculos se encaixam como peças de quebra-cabeça.  

### 1.3 Explicação Detalhada  
O círculo inscrito fica dentro do triângulo, tocando os lados. O círculo dos nove pontos passa por pontos médios dos lados, pontos onde as alturas do triângulo tocam os lados e pontos entre os vértices e um ponto chamado ortocentro (onde as alturas se encontram). Este círculo de nove pontos toca internamente o círculo inscrito e externamente três outros círculos fora do triângulo chamados excírculos.  

### 1.4 Aplicações  
Este arranjo é usado para entender propriedades profundas da geometria do triângulo, ajudando em estudos de matemática, engenharia e física onde formas e proporções são importantes.  

### 1.5 Análise da Tabela  
Na representação dos pontos e círculos, observamos as relações de distância e tangência entre eles, confirmando como o círculo de nove pontos se encaixa perfeitamente nos outros círculos associados.  

## 2. Script feuerbach_model.py  

### 2.1 Relação com o Teorema  
O script cria triângulos com tamanhos baseados em potências de 2 e calcula os círculos relacionados ao triângulo, especialmente o círculo inscrito e o círculo dos nove pontos, para mostrar visualmente como eles se encaixam, ilustrando o conceito do teorema.  

### 2.2 Objetivo do Script  
Visualizar e entender, por meio de gráficos, como os círculos importantes de um triângulo estão relacionados e confirmam a propriedade da tangência entre eles.  

### 2.3 Exemplo de Saída  
O script gera imagens mostrando o triângulo, o círculo inscrito em laranja, o círculo dos nove pontos em azul, e os pontos notáveis em vermelho, permitindo perceber a interação entre os círculos.  

### 2.4 Funcionamento Interno  
- Define triângulos com vértices usando potências de 2 para as coordenadas.  
- Calcula pontos médios, pés das alturas e o ortocentro.  
- Calcula os centros e raios dos círculos inscritos e dos nove pontos.  
- Plota todos os elementos para visualização.  

### 2.5 Tecnologias e Requisitos  
- Python 3.8.10  
- Bibliotecas: numpy, matplotlib  
- Ambiente gráfico para exibição das imagens  

## 3 Extras  

### 3.1 Licença  
Este projeto está sob a licença MIT, permitindo uso, modificação e distribuição livre.  

### 3.2 Referências  
- Geometria Euclidiana básica  
- Artigos e livros sobre círculos notáveis em triângulos  
- Documentação do matplotlib e numpy  

### 3.3 Testes e Validações  
O código foi testado para valores de n entre 0 e 3 para garantir que os cálculos e gráficos são gerados corretamente e que as relações visuais entre os círculos são evidentes.  

## 4 Contato  

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*  

## 5. Nota  

- **Círculo inscrito**: círculo que fica dentro do triângulo e toca seus três lados.  
- **Círculo excêntrico (excírculo)**: círculo fora do triângulo que toca um lado e as extensões dos outros dois lados.  
- **Círculo de nove pontos**: círculo que passa por nove pontos especiais do triângulo, como pontos médios dos lados e pés das alturas.  
- **Ortócentro**: ponto onde as três alturas do triângulo se encontram.  
- **Altura**: linha traçada de um vértice perpendicular ao lado oposto.  
- **Tangência**: quando dois círculos se tocam em exatamente um ponto.  
