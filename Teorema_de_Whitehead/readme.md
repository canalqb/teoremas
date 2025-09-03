# 📊 - Teorema de Whitehead

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)

## Frase do Teorema

> O **Teorema de Whitehead** apresenta uma sequência que descreve o crescimento de valores dentro de um intervalo específico, com base em potências de 2, para determinar a aproximação esperada dentro desse intervalo.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `teorema_whitehead.py`](#2-script-teorema_whiteheadpy)

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

O **Teorema de Whitehead** descreve como os valores de uma sequência **crescem exponencialmente** dentro de um intervalo específico. Ele utiliza potências de 2 para calcular os valores **Início** (2^N) e **Fim** (2^(N+1)-1), que representam limites superiores e inferiores para o crescimento da sequência.

### 1.2 Exemplos Práticos

Ao aplicar o teorema, temos os seguintes exemplos:

* Para **N = 0**, temos **Início = 1** e **Fim = 1**. O valor esperado seria **1**.
* Para **N = 1**, temos **Início = 2** e **Fim = 3**, com o valor esperado sendo **2**.
* Para **N = 2**, temos **Início = 4** e **Fim = 7**, com o valor esperado sendo **5**.

Esses valores demonstram como o teorema gera uma sequência de números, fornecendo uma aproximação dos valores dentro do intervalo.

### 1.3 Explicação Detalhada

O **Teorema de Whitehead** utiliza uma fórmula baseada em potências de 2 para calcular o **Início** e **Fim** de cada valor na sequência. O valor esperado pelo teorema é calculado com uma média ponderada dentro desse intervalo.

* A fórmula para o **Início** é **2^N** e para o **Fim** é **2^(N+1)-1**.
* O valor esperado é calculado com uma aproximação baseada na média desses limites.

### 1.4 Aplicações

Este tipo de sequência pode ser útil em várias áreas, incluindo **teoria dos números**, **análise de algoritmos** e **computação**. O teorema de Whitehead pode ser utilizado para estudar o comportamento de funções exponenciais e como elas se comportam dentro de intervalos específicos.

### 1.5 Análise da Tabela

A tabela gerada pelo script de **Teorema de Whitehead** calcula o valor esperado para diferentes valores de N, com base nos limites de **Início** e **Fim**:

| N | Início (2^N) | Esperado pelo Teorema | Fim (2^(N+1))-1 |
| - | ------------ | --------------------- | --------------- |
| 0 | 1            | 1.0                   | 1               |
| 1 | 2            | 2.0                   | 3               |
| 2 | 4            | 5.0                   | 7               |
| 3 | 8            | 12.0                  | 15              |
| 4 | 16           | 25.0                  | 31              |
| 5 | 32           | 51.0                  | 63              |
| 6 | 64           | 103.0                 | 127             |
| 7 | 128          | 207.0                 | 255             |
| 8 | 256          | 415.0                 | 511             |
| 9 | 512          | 831.0                 | 1023            |

## 2. Script `teorema_whitehead.py`

### 2.1 Relação com o Teorema

Este script foi projetado para **calcular os valores esperados** baseados no Teorema de Whitehead. Ele usa os **intervalos de potências de 2** para determinar os limites de crescimento e gera os valores esperados dentro desses intervalos.

### 2.2 Objetivo do Script

O objetivo do script é calcular os valores **Início** (2^N), **Fim** (2^(N+1)-1) e o valor **esperado pelo teorema**. Através de uma aproximação, o script gera a tabela completa, conforme mostrado na seção anterior.

### 2.3 Exemplo de Saída

Aqui está um exemplo da saída gerada pelo script:

```plaintext
   N  Início (2^N)  Esperado pelo Teorema  Fim (2^(N+1))-1
0   0              1                     1.0                  1
1   1              2                     2.0                  3
2   2              4                     5.0                  7
3   3              8                    12.0                 15
4   4             16                    25.0                 31
5   5             32                    51.0                 63
6   6             64                   103.0                127
7   7            128                   207.0                255
8   8            256                   415.0                511
9   9            512                   831.0               1023
```

### 2.4 Funcionamento Interno

O script utiliza as seguintes etapas:

1. **Cálculo de Intervalos**: Para cada valor de **N**, ele calcula o **Início** e o **Fim** com base nas fórmulas dadas (2^N e 2^(N+1)-1).
2. **Aproximação de Valor Esperado**: Aplica a fórmula do teorema para gerar o valor esperado dentro do intervalo.
3. **Exibição de Tabela**: Exibe a tabela final com os valores calculados para **N**, **Início**, **Esperado** e **Fim**.

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10**
* **Bibliotecas**: `pandas` (para exibição de tabela).

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### 3.2 Referências

* **Teorema de Whitehead**: Referências matemáticas podem ser encontradas na literatura especializada.
* **Python**: [https://www.python.org/](https://www.python.org/)

### 3.3 Testes e Validações

O script foi testado para valores de **N** de 0 a 9, com resultados consistentes na geração da tabela. A fórmula utilizada para calcular o valor esperado tem como base uma aproximação simples.

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Média Ponderada**: A média ponderada é uma maneira de calcular a média de um conjunto de números, mas


com **pesos diferentes** para cada número. No contexto do teorema, ela é usada para aproximar o valor esperado dentro de um intervalo.

**Intervalo**: O intervalo é o intervalo de valores entre o **Início** e o **Fim** calculado pela fórmula. O valor esperado deve estar dentro desse intervalo, representando uma aproximação de valores entre os dois limites.

**Potência de 2**: A potência de 2 é uma operação matemática onde o número 2 é multiplicado por si mesmo várias vezes, como em **2^N**. Isso gera uma sequência de números como 1, 2, 4, 8, 16, etc.
