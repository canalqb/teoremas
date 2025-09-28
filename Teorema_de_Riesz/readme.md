# 📐 - Teorema de Riesz (Representação em L²)  
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)  

## Frase do Teorema  

> "Para cada funcional linear contínuo definido em um espaço L², existe um vetor único nesse espaço que representa esse funcional via produto interno." – Isso quer dizer que toda forma de medir algo linearmente em um espaço de funções pode ser representada por um vetor especial que faz essa medição de forma simples, usando uma operação chamada produto interno.  

## Sumário  

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `riesz_repr_l2.py`](#2-script-riesz_repr_l2py)  
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

## 1 Introdução ao Teorema  

### 1.1 Resumo  
O teorema afirma que para qualquer funcional linear (uma forma de medir coisas linearmente) que é contínuo em um espaço L² (um espaço de funções onde podemos calcular médias de quadrados), podemos representar esse funcional usando um vetor específico nesse espaço. Ou seja, medir é equivalente a calcular um produto especial entre vetores.  

### 1.2 Exemplos Práticos  
Imagine que você quer medir a “média ponderada” de uma função. O teorema garante que existe um vetor que, ao calcular um produto com essa função, entrega esse valor de média. Isso é muito usado em análise de sinais, estatística e mecânica quântica.  

### 1.3 Explicação Detalhada  
No espaço L², as funções têm norma baseada na média dos quadrados dos valores. O teorema diz que para cada funcional linear contínuo — que é basicamente uma regra que transforma funções em números, respeitando linearidade e continuidade — existe um vetor que representa essa transformação como um produto interno. Isso simplifica muito o trabalho matemático e facilita a análise.  

### 1.4 Aplicações  
- Análise funcional  
- Processamento de sinais  
- Estatística matemática  
- Mecânica quântica  

### 1.5 Análise da Tabela  
A tabela relaciona valores calculados para potências de 2 (início e fim dos intervalos) e o valor obtido pelo produto interno (que representa o funcional). Observe que o valor do produto cresce rapidamente e é um reflexo direto da soma dos números naturais no intervalo correspondente, mostrando a aplicação prática do teorema.  

## 2 Script `riesz_repr_l2.py`  

### 2.1 Relação com o Teorema  
O script implementa o cálculo do produto interno que representa o funcional linear no intervalo definido pelas potências de 2, como afirma o teorema. Ele demonstra a construção desse vetor único para cada N, ilustrando a representação do funcional.  

### 2.2 Objetivo do Script  
- Calcular os valores do produto interno para cada intervalo definido por potências de 2.  
- Imprimir uma tabela com os valores calculados.  
- Gerar uma animação 3D mostrando a evolução desses valores com o aumento de N, facilitando o entendimento visual da representação do funcional.  

### 2.3 Exemplo de Saída  
```

## N | Início (2^N) | Valor do Teorema | Fim (2^{N+1}-1)

0 |            1 |                1 |               1
1 |            2 |                3 |               3
2 |            4 |               10 |               7
3 |            8 |               36 |              15
4 |           16 |              136 |              31
5 |           32 |              528 |              63
6 |           64 |             2080 |             127
7 |          128 |             8256 |             255
8 |          256 |            32896 |             511
9 |          512 |           131328 |            1023
10 |         1024 |           524800 |            2047

```

### 2.4 Funcionamento Interno  
Para cada N:  
- Cria-se um vetor constante 1 com tamanho igual ao intervalo entre 2^N e 2^{N+1}-1.  
- Cria-se um vetor crescente de 1 até o tamanho do intervalo.  
- Calcula-se o produto interno desses vetores, que é o valor do funcional linear.  
- Os valores são armazenados e usados para animar um gráfico 3D.  

### 2.5 Tecnologias e Requisitos  
- Python 3.8.10  
- Bibliotecas: numpy, matplotlib (com suporte a animação e gravação de gif)  

## 3 Extras  

### 3.1 Licença  
MIT License — sinta-se livre para usar, modificar e compartilhar.  

### 3.2 Referências  
- [Representação de Riesz no Wikipedia](https://pt.wikipedia.org/wiki/Teorema_de_representa%C3%A7%C3%A3o_de_Riesz)  
- [Produto interno e espaços L²](https://pt.wikipedia.org/wiki/Espa%C3%A7o_Lp)  
- [Matplotlib Documentação](https://matplotlib.org/stable/api/animation_api.html)  

### 3.3 Testes e Validações  
O script foi testado para os valores N=0 a 10 e gera resultados coerentes com a soma dos números naturais do intervalo, evidenciando a representação do funcional.  

## 4 Contato  

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*  

## 5 Nota  

**Funcional linear:** é uma regra que transforma uma função em um número de forma linear, ou seja, respeitando soma e multiplicação por escalares.  

**Produto interno:** é uma operação que pega dois vetores e gera um número, representando uma forma de medir o "ângulo" ou "proximidade" entre eles.  

**Espaço L²:** é um conjunto de funções onde podemos medir o tamanho delas considerando a média dos quadrados dos seus valores.  

**Contínuo:** significa que pequenas mudanças na função de entrada causam pequenas mudanças no resultado, garantindo estabilidade.  

**Vetores únicos:** significa que existe um e só um vetor que representa a ação do funcional linear nesse espaço, uma característica muito útil para simplificar problemas complexos.  
