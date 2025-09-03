# 📊 - Teorema de Aproximação dos Intervalos

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Aproximação%20dos%20Intervalos-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)

## Frase do Teorema

> **Aproximação entre limites de intervalo** – Este é um cálculo simples para encontrar um valor aproximado dentro de um intervalo de potências de dois, onde a média entre o início e o fim é usada como o valor esperado.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `skolem_teorema.py`](#2-script-skolem_teoremapy)

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

Este **teorema de aproximação** trata de como encontrar um valor esperado dentro de um intervalo definido pelas potências de dois. A tabela a seguir apresenta intervalos de valores de $2^N$ a $2^{(N+1)} - 1$ e uma estimativa de um valor esperado entre esses dois limites, sendo calculado pela **média simples** entre os valores de início e fim.

### 1.2 Exemplos Práticos

Vamos ver alguns exemplos simples com $N = 0$ a $N = 9$:

* Para $N = 0$, o intervalo é de **1 a 1** e o valor esperado é 1.
* Para $N = 1$, o intervalo vai de **2 a 3** e o valor esperado é 2.
* Para $N = 2$, o intervalo vai de **4 a 7** e o valor esperado é 5.

Esses cálculos continuam para valores maiores de $N$.

### 1.3 Explicação Detalhada

A ideia é usar o intervalo dado por $2^N$ (que é o **Início**) e $2^{(N+1)} - 1$ (que é o **Fim**), e depois calcular a **média simples** desses dois valores. Essa média nos dá um valor aproximado de **esperado** dentro do intervalo. O valor obtido pode ser interpretado como um valor central do intervalo.

### 1.4 Aplicações

Esse tipo de cálculo pode ser útil em problemas de **análise de intervalos** e em **algoritmos que trabalham com potências de dois**, como no caso de determinadas operações em **estruturas de dados** ou **algoritmos de busca**. Além disso, pode ser útil em **simulações computacionais** onde se trabalha com limites definidos de forma exponencial.

### 1.5 Análise da Tabela

A tabela gerada pelo script mostra como o valor esperado varia conforme $N$ cresce. O cálculo da média entre o início e o fim de cada intervalo permite que observemos como a distribuição se aproxima dos limites sem ultrapassá-los.

---

## 2. Script `skolem_teorema.py`

### 2.1 Relação com o Teorema

O script **`skolem_teorema.py`** implementa o cálculo da média entre o **Início** $2^N$ e o **Fim** $2^{(N+1)} - 1$ para diferentes valores de $N$, e gera uma tabela com o valor esperado para cada intervalo.

### 2.2 Objetivo do Script

O objetivo do script é fornecer uma forma simples de calcular o valor esperado dentro dos intervalos definidos pelas potências de dois, ajudando na compreensão de como os limites de intervalo funcionam em cálculos simples.

### 2.3 Exemplo de Saída

Abaixo está um exemplo da saída do script, que mostra os valores de $N$, **Início**, **Esperado pelo Teorema** e **Fim**:

```
N   | Início (2^N)   | Esperado pelo Teorema    | Fim (2^(N+1))-1
----------------------------------------------------------------------
0   | 1               | 1                        | 1
1   | 2               | 2                        | 3
2   | 4               | 5                        | 7
3   | 8               | 11                       | 15
4   | 16              | 23                       | 31
5   | 32              | 47                       | 63
6   | 64              | 95                       | 127
7   | 128             | 191                      | 255
8   | 256             | 383                      | 511
9   | 512             | 767                      | 1023
```

### 2.4 Funcionamento Interno

O script calcula a média entre os valores **Início** e **Fim** para cada valor de $N$ de 0 a 9. A função `calcular_esperado_pelo_teorema` usa uma fórmula simples de média para determinar o valor esperado. A tabela é gerada e impressa na tela.

### 2.5 Tecnologias e Requisitos

* **Linguagem**: Python 3.8.10
* **Dependências**: Nenhuma dependência externa
* **Requisitos**: O script pode ser executado diretamente em qualquer ambiente que suporte Python 3.8 ou superior.

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a **MIT License**. Consulte o arquivo LICENSE para mais informações.

### 3.2 Referências

* [Lei dos Grandes Números – Wikipedia](https://en.wikipedia.org/wiki/Law_of_large_numbers)
* [Python 3.8 Documentation](https://docs.python.org/3.8/)

### 3.3 Testes e Validações

O script foi testado para valores de $N$ de 0 a 9. Todos os cálculos foram validados e a saída está conforme esperado.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Média Simples**: Quando dizemos "média simples", estamos nos referindo ao cálculo onde somamos dois valores e depois dividimos o resultado por 2.

**Potências de Dois**: Potências de dois são números gerados pela fórmula $2^N$, onde $N$ é um número inteiro. Exemplo: $2^3 = 8$, $2^4 = 16$, e assim por diante.

**Intervalos**: Quando falamos de intervalos, estamos nos referindo a uma faixa de números entre o valor inicial e o valor final. Neste caso, o valor inicial é $2^N$ e o valor final é $2^{(N+1)} - 1$.
