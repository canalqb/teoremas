# 🧩 - Glivenko Cantelli
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![Glivenko-Cantelli](https://img.shields.io/badge/Teorema-Glivenko-Cantelli-ff69b4.svg)](https://en.wikipedia.org/wiki/Glivenko%E2%80%93Cantelli_theorem)

## Frase do Teorema

> À medida que aumentamos o tamanho de uma amostra aleatória, a distribuição observada nos dados (chamada de distribuição empírica) se aproxima de forma uniforme da distribuição verdadeira (teórica) que gerou esses dados – ou seja, com mais dados, a amostra “revela” a verdadeira forma da distribuição.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `Glivenko_Cantelli.py`](#2-script-glivenko_cantellipy)  
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
O **Teorema de Glivenko-Cantelli** diz que se você pegar uma amostra grande o suficiente de dados aleatórios vindos de qualquer distribuição, a forma dos dados (distribuição empírica) vai ficar cada vez mais parecida com a forma da distribuição verdadeira (distribuição teórica).

### 1.2 Exemplos Práticos  
Imagine lançar uma moeda mil vezes: a proporção de caras e coroas observada ficará próxima da verdadeira probabilidade (50% cada).  
O mesmo vale para dados normais, dados de altura, notas escolares — com muitos dados, a forma observada fica parecida com a esperada.

### 1.3 Explicação Detalhada  
A distribuição empírica é basicamente um gráfico que conta “quantos dados estão abaixo de cada valor”. A distribuição teórica é a “curva ideal” que conhecemos na matemática.  
O teorema garante que, conforme aumentamos a quantidade de dados, a maior diferença entre essas duas curvas diminui e tende a zero.

### 1.4 Aplicações  
- Estatística: para validar modelos e hipóteses  
- Machine learning: para entender se os dados seguem uma certa distribuição  
- Processamento de sinais e dados em geral  

### 1.5 Análise da Tabela  

O script mostra, para amostras cada vez maiores (tamanho `n` próximo de potências de 2), onde ocorre a maior diferença entre a CDF observada e a teórica, chamada aqui de **‘PROCURANDO’**.  

| 2^A  | PROCURANDO | 2^(A+1)-1 |  
|------|------------|-----------|  
| 1    | 1          | 1         |  
| 2    | 3          | 3         |  
| 4    | 5          | 7         |  
| 8    | 10         | 15        |  
| 16   | 29         | 31        |  
| 32   | 57         | 63        |  
| 64   | 101        | 127       |  
| 128  | 184        | 255       |  
| 256  | 438        | 511       |  
| 512  | 785        | 1023      |  
| 1024 | 1586       | 2047      |  
| 2048 | 2479       | 4095      |  
| 4096 | 6905       | 8191      |  

Cada linha mostra que quanto maior a amostra, maior a busca pela verdade (menor diferença entre as distribuições).

---

## 2. Script `Glivenko_Cantelli.py`

### 2.1 Relação com o Teorema  
O script é um experimento visual que demonstra o Teorema de Glivenko-Cantelli, mostrando como a diferença entre a distribuição empírica e teórica diminui conforme aumentamos o número de dados.

### 2.2 Objetivo do Script  
- Gerar amostras da distribuição normal padrão (média zero, desvio padrão um)  
- Calcular a distribuição acumulada empírica (CDF dos dados)  
- Comparar com a CDF teórica da normal padrão  
- Encontrar o ponto com a maior diferença entre as duas CDFs  
- Mapear esse ponto para um número inteiro dentro de um intervalo para análise  

### 2.3 Exemplo de Saída  

```bash
2^A        PROCURANDO      2^(A+1)-1  
1          1              1  
2          3              3  
4          5              7  
8          10             15  
16         29             31  
32         57             63  
64         101            127  
128        184            255  
256        438            511  
512        785            1023  
1024       1586           2047  
2048       2479           4095  
4096       6905           8191  
````

Além disso, o script mostra exemplos de “mapas inversos”, que indicam qual valor na distribuição normal corresponde a posições específicas no intervalo.

### 2.4 Funcionamento Interno

* Usa funções do `numpy` e `scipy` para gerar dados e calcular CDF e sua inversa (ppf).
* Para cada valor de A, cria uma amostra de tamanho n = 2^(A+1) - 1.
* Calcula a maior diferença entre CDF empírica e teórica (ponto ‘PROCURANDO’).
* Exibe resultados formatados para fácil compreensão.

### 2.5 Tecnologias e Requisitos

* Python 3.8.10
* Pacotes `numpy` e `scipy` instalados (`pip install numpy scipy`)

Executar com:

```bash
python Glivenko_Cantelli.py
```

---

## 3 Extras

### 3.1 Licença

Este projeto está sob **Licença MIT**. Consulte o arquivo LICENSE para detalhes.

### 3.2 Referências

* [Glivenko-Cantelli theorem - Wikipedia](https://en.wikipedia.org/wiki/Glivenko%E2%80%93Cantelli_theorem)
* Documentação SciPy: [https://docs.scipy.org/doc/scipy/reference/stats.html](https://docs.scipy.org/doc/scipy/reference/stats.html)

### 3.3 Testes e Validações

Testado em Python 3.8.10 com `numpy` e `scipy` nas versões recentes, o script executa corretamente e mostra resultados coerentes com o teorema.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Distribuição empírica:** gráfico que mostra a frequência acumulada dos dados observados até certo valor.
**Distribuição teórica:** curva matemática que descreve como os dados deveriam se comportar, se tirássemos infinitos dados.
**CDF (Função Distribuição Acumulada):** função que para cada valor mostra a proporção dos dados que são menores ou iguais a ele.
**Ponto de maior diferença:** valor onde a diferença entre a distribuição empírica e a teórica é maior.
**ppf (Percent Point Function):** função que calcula o valor correspondente a uma dada probabilidade acumulada — é o “inverso” da CDF.

---
