# 📐 - Série de Laurent  
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  

## Frase da Série  

> A Série de Laurent permite representar funções complexas como uma soma infinita de termos, incluindo potências negativas e positivas de uma variável complexa, facilitando a análise de pontos problemáticos da função.  

## Sumário  

* [1. Introdução à Série](#1-introdução-à-série)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `Laurent.py`](#2-script-laurentpy)  
  * [2.1 Relação com a Série](#21-relação-com-a-série)  
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

## 1. Introdução à Série  

### 1.1 Resumo  
A Série de Laurent é uma forma de escrever funções que envolvem números complexos usando uma soma de potências da variável, que pode incluir termos com potências negativas. Essa série ajuda a entender o comportamento das funções em pontos onde elas podem não ser definidas normalmente.

### 1.2 Exemplos Práticos  
Imagine querer entender uma função que "explode" em um ponto, como 1 dividido por (z vezes z menos 1). Usando a Série de Laurent, conseguimos descrever essa função como uma soma de várias partes que facilitam a análise.

### 1.3 Explicação Detalhada  
A ideia básica é dividir a função em pedaços que são potências da variável z. Diferente das séries tradicionais, aqui podemos ter potências negativas, que são úteis para estudar pontos chamados de singularidades — onde a função pode ter comportamento estranho.

### 1.4 Aplicações  
Essa série é muito usada em áreas como engenharia, física e matemática para estudar funções complexas, principalmente para resolver problemas envolvendo circuitos, fluidos e campos eletromagnéticos.

### 1.5 Análise da Tabela  
Os valores somados em blocos crescentes de potências mostram como a soma parcial da série se aproxima da função original. Isso ajuda a entender o quanto cada grupo de termos contribui para o resultado final.

## 2. Script `Laurent.py`  

### 2.1 Relação com a Série  
O script calcula e visualiza a soma da Série de Laurent para uma função específica, mostrando como cada grupo de termos afeta a aproximação da função.

### 2.2 Objetivo do Script  
Gerar gráficos 3D animados que mostram a série aproximando a função real em uma curva complexa, rotacionando para facilitar a visualização da contribuição dos termos.

### 2.3 Exemplo de Saída  
```

Ponto fixo z = 0.5657+0.5657j
Termo para k=-1 (z^-1): 0.8839-0.8839j
n = 0, intervalo k = \[1, 1], soma do bloco = 0.565685+0.565685j
...
Erro absoluto: 2.517306e+00

```

### 2.4 Funcionamento Interno  
O script calcula os coeficientes da série para potências de z, soma esses termos em blocos que dobram de tamanho a cada passo, e então plota essas somas parciais em gráficos 3D. A animação rotaciona as curvas para uma visão melhor das relações entre elas.

### 2.5 Tecnologias e Requisitos  
* Python 3.8.10  
* Bibliotecas: numpy, matplotlib  
* Pillow para salvar animações em GIF  

## 3 Extras  

### 3.1 Licença  
MIT License – uso livre e aberto para modificações e compartilhamento.  

### 3.2 Referências  
* Artigos sobre séries e funções complexas  
* Documentação do matplotlib e numpy  

### 3.3 Testes e Validações  
O script foi testado para garantir que a soma parcial converge para a função original dentro de um erro aceitável.

## 4 Contato  

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*  

## 5. Nota  

*{negrito}: lambda* — é a letra grega usada para representar uma constante ou parâmetro em muitas fórmulas. Aqui, só lembramos que é uma letra comum usada em matemática.

*{negrito}: variância* — significa o quanto os valores de um conjunto estão espalhados em relação à média. É uma medida de dispersão.

*{negrito}: esperança* — é o valor médio esperado de um resultado em um experimento ou conjunto de dados, uma forma de "média" ponderada.

*{negrito}: singularidade* — ponto onde a função não está definida normalmente, como divisão por zero.

*{negrito}: coeficiente* — número que multiplica uma variável ou termo numa soma ou produto.
