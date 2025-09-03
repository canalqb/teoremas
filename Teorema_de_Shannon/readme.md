# 📡 - Teorema de Shannon

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)

## Frase do Teorema

> "A capacidade máxima de um canal de comunicação com ruído é limitada por sua largura de banda e relação sinal/ruído" – Em outras palavras, existe um limite para a quantidade de informação que pode ser transmitida sem erros, independentemente da tecnologia usada.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `Teorema_de_Shannon.py`](#2-script-teorema_de_shannonpy)

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

O **Teorema de Shannon** é um marco da **Teoria da Informação** que determina o limite máximo teórico para a transmissão de dados em canais com ruído. Ele nos diz quanta informação pode ser enviada por segundo sem erro, considerando a largura do canal e o nível de ruído presente.

### 1.2 Exemplos Práticos

Imagine uma linha telefônica que transmite voz e dados: não importa o quanto você melhore a codificação, existe uma velocidade máxima de dados que essa linha pode suportar sem perder informações devido ao ruído.

### 1.3 Explicação Detalhada

A fórmula principal é:

C = B \* log2(1 + S/N)

* **C** é a capacidade do canal (em bits por segundo)
* **B** é a largura de banda do canal (em hertz)
* **S/N** é a relação entre o sinal (S) e o ruído (N)

*Explicando:* O log2 é a operação que mede quantos bits de informação podem ser transmitidos com segurança. A razão sinal/ruído representa o quanto o sinal é forte em comparação ao ruído (interferência) no canal.

### 1.4 Aplicações

* Telecomunicações (internet, telefonia, satélites)
* Codificação de dados e compressão
* Sistemas de comunicação sem fio
* Desenvolvimento de protocolos e modulações

### 1.5 Análise da Tabela

A tabela mostra valores de entrada `x` (potências de 2), os valores reais da capacidade `y`, o máximo teórico `z`, e a previsão `y_pred` de um modelo polinomial. A aproximação é boa, indicando que mesmo um modelo simples pode prever a capacidade de canais em faixas maiores.

---

## 2. Script `Teorema_de_Shannon.py`

### 2.1 Relação com o Teorema

O script usa dados que exemplificam a capacidade do canal em diferentes larguras de banda (valores `x`), relacionando-os com capacidades reais observadas (`y`) e máximos possíveis (`z`). Ele tenta modelar essa relação para prever valores futuros.

### 2.2 Objetivo do Script

Construir um modelo matemático simples (regressão polinomial de grau 2) que represente a capacidade de um canal de comunicação, permitindo prever o valor para grandes entradas.

### 2.3 Exemplo de Saída

```
    x     y      z  y_pred
    1     1      1    -173
    2     3      3    -171
    4     7      7    -168
    8     8     15    -162
   16    21     31    -150
   32    49     63    -126
   64    76    127     -78
  128   224    255      18
  256   467    511     211
  512   514   1023     595
 1024  1155   2047    1366
 2048  2683   4095    2912
 4096  5216   8191    6020
 8192 10544  16383   12302
16384 26867  32767   25126
32768 51510  65535   51822
65536 95823 131071  109398
```

### 2.4 Funcionamento Interno

O script utiliza a biblioteca **Scikit-learn** para ajustar um modelo polinomial de grau 2. Ele treina esse modelo usando os dados fornecidos e gera previsões para a capacidade `y` para cada valor de `x`. Para visualizar, gera gráficos interativos (se o Plotly estiver instalado).

### 2.5 Tecnologias e Requisitos

* Python 3.8.10
* Bibliotecas: pandas, scikit-learn, plotly (opcional para gráficos)

---

## 3 Extras

### 3.1 Licença

Este projeto está sob a licença **MIT** — veja o arquivo LICENSE para detalhes.

### 3.2 Referências

* [Teorema de Shannon na Wikipedia](https://en.wikipedia.org/wiki/Shannon%E2%80%93Hartley_theorem)
* Claude Shannon, "A Mathematical Theory of Communication", 1948

### 3.3 Testes e Validações

O modelo foi validado pela comparação entre os valores reais e previstos, mostrando um erro aceitável para fins didáticos e de demonstração.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

*Largura de banda (B)*: Quantidade de frequência que o canal usa para transmitir dados.
*Relação sinal/ruído (S/N)*: Medida de quão forte é o sinal comparado ao ruído, que é toda interferência indesejada.
*Log2*: Função matemática que responde “quantos bits de informação cabem neste valor?” — ajuda a traduzir potência em bits.
