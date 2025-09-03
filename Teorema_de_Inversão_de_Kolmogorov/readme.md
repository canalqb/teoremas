# 🌈 - Teorema de Inversão de Kolmogorov

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Inversão%20de%20Kolmogorov-ff69b4.svg)](https://en.wikipedia.org/wiki/Characteristic_function_%28probability_theory%29)

## Frase do Teorema

> *É possível recuperar a função de distribuição acumulada (CDF) de uma variável aleatória contínua usando apenas sua função característica.* – Em termos simples: se você conhece a "assinatura matemática" de uma distribuição (chamada função característica), você pode reconstruir a probabilidade acumulada dela com uma fórmula de integração.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `kolmogorov_inversion_demo.py`](#2-script-kolmogorov_inversion_demopy)

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

## 1 Introdução ao Teorema

### 1.1 Resumo

O **Teorema de Inversão de Kolmogorov** mostra que é possível calcular a **probabilidade acumulada** de uma variável contínua (ou seja, a *chance de ela assumir valores até certo ponto*) **usando apenas sua função característica** — que é uma forma alternativa de descrever a distribuição.

### 1.2 Exemplos Práticos

No script, usamos esse teorema para recuperar a **CDF da normal padrão** (a famosa "curva em forma de sino"), e verificamos o valor da CDF em `x = 0`. Para essa distribuição, sabemos que esse valor deve ser `0.5`.

### 1.3 Explicação Detalhada

A fórmula do teorema envolve uma **integração numérica** com limites infinitos. Como não podemos integrar até o infinito na prática, o script aproxima esse limite usando valores finitos crescentes de `T`, como `2^1`, `2^2`, ..., `2^8`.

### 1.4 Aplicações

* Reconstrução de distribuições a partir de suas transformadas
* Estatística teórica e modelagem matemática
* Verificação numérica de funções probabilísticas

### 1.5 Análise da Tabela

A saída mostra, para cada `T = 2^A`, qual foi o valor aproximado da CDF no ponto `x = 0`. À medida que `T` cresce, os valores se aproximam do resultado esperado `0.5`.

---

## 2. Script `kolmogorov_inversion_demo.py`

### 2.1 Relação com o Teorema

O script **implementa numericamente a fórmula** do Teorema de Inversão de Kolmogorov, aplicando-a à função característica da distribuição normal padrão.

### 2.2 Objetivo do Script

Demonstrar como aproximar uma função de distribuição acumulada (CDF) a partir da função característica da variável aleatória.

### 2.3 Exemplo de Saída

```plaintext
 2^A |  Retorno Teorema |    Intervalo
----------------------------------------
    1 |     0.2387324146 | [1, 1]
    2 |     0.4073114293 | [2, 3]
    4 |     0.4761618351 | [4, 7]
    8 |     0.4953725875 | [8, 15]
   16 |     0.4993134552 | [16, 31]
   32 |     0.4999285633 | [32, 63]
   64 |     0.4999951846 | [64, 127]
  128 |     0.4999998583 | [128, 255]
  256 |     0.4999999986 | [256, 511]
```

### 2.4 Funcionamento Interno

* Define a **função característica da normal padrão**, que é `exp(-t^2 / 2)`
* Aplica uma fórmula de integração (numérica) para cada intervalo `[1, T]`
* Calcula o valor da CDF no ponto `x = 0` com base nessa aproximação

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10**
* **SciPy** (para integração numérica)

Instale o pacote necessário:

```bash
pip install scipy
```

E execute o script com:

```bash
python kolmogorov_inversion_demo.py
```

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a **Licença MIT** — uso livre, com créditos mantidos ao autor original.

### 3.2 Referências

* Teorema de Inversão de Kolmogorov:
  [https://en.wikipedia.org/wiki/Characteristic\_function\_(probability\_theory)](https://en.wikipedia.org/wiki/Characteristic_function_%28probability_theory%29)
* Normal padrão e sua CDF:
  [https://en.wikipedia.org/wiki/Normal\_distribution](https://en.wikipedia.org/wiki/Normal_distribution)
* SciPy:
  [https://scipy.org/](https://scipy.org/)

### 3.3 Testes e Validações

* Validação feita usando o ponto `x = 0`, onde `F(0) = 0.5` para a normal padrão.
* Os resultados numéricos convergem corretamente à medida que `T` aumenta.
* O script pode ser modificado facilmente para testar outros pontos ou distribuições.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

📘 **Glossário de termos usados:**

* **Função característica**: é como uma "impressão digital" matemática de uma variável aleatória. Serve para descrever distribuições, e muitas vezes é mais fácil de trabalhar do que a função de distribuição acumulada (CDF).
* **CDF (Função de Distribuição Acumulada)**: mostra a chance de uma variável aleatória ser menor ou igual a um certo valor.
* **Integração numérica**: técnica para estimar o valor de uma integral (área sob a curva), usando métodos computacionais.
* **Aproximação**: quando usamos um número finito em vez de infinito para obter um resultado que se aproxima do ideal.
