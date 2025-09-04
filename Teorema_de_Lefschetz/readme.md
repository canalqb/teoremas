# 📐 - Teorema de Lefschetz
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Topologia%20Algebraica-ff69b4.svg)](https://en.wikipedia.org/wiki/Lefschetz_fixed-point_theorem)

## Frase do Teorema

> *Se uma função contínua for aplicada sobre um espaço bem comportado e o número de Lefschetz não for zero, então essa função possui pelo menos um ponto fixo.* – Isso significa que, em certas condições, uma função obrigatoriamente se "encontra consigo mesma" em algum ponto.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)

* [2. Script `lefschetz_power_estimate.py`](#2-script-lefschetz_power_estimatepy)
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

O **Teorema de Lefschetz dos Pontos Fixos** trata da existência de pontos fixos de funções contínuas, ou seja, pontos onde a função retorna o próprio valor de entrada.

### 1.2 Exemplos Práticos

- Em uma superfície como uma esfera, qualquer função contínua que mapeia a esfera para ela mesma deve ter pelo menos um ponto que permaneça no mesmo lugar.
- Esse teorema tem aplicações em áreas como geometria, sistemas dinâmicos, inteligência artificial e teoria dos grafos.

### 1.3 Explicação Detalhada

O teorema usa ferramentas da topologia algébrica, como grupos de homologia e traços de mapas induzidos, para calcular um número chamado **número de Lefschetz**. Se esse número for diferente de zero, **existe um ponto fixo** garantido.

### 1.4 Aplicações

- Verificação de estabilidade em sistemas físicos.
- Análise de comportamento de funções em espaços contínuos.
- Geração de algoritmos baseados em padrões fixos.

### 1.5 Análise da Tabela

Neste repositório, construímos uma tabela baseada no comportamento de potências de 2 e tentamos ajustar estimativas para o número de Lefschetz dentro de intervalos crescentes:

| N | 2^N (Início) | Mersenne (2^N - 1) | L(f) Estimado | Intervalo       |
|---|--------------|--------------------|----------------|------------------|
| 0 | 1            | 0                  | 1              | [1, 1]           |
| 1 | 2            | 1                  | 3              | [2, 3]           |
| 2 | 4            | 3                  | 7              | [4, 7]           |
| 3 | 8            | 7                  | 15             | [8, 15]          |
| 4 | 16           | 15                 | 31             | [16, 31]         |
| 5 | 32           | 31                 | 63             | [32, 63]         |
| 6 | 64           | 63                 | 127            | [64, 127]        |
| 7 | 128          | 127                | 255            | [128, 255]       |
| 8 | 256          | 255                | 511            | [256, 511]       |
| 9 | 512          | 511                | 1023           | [512, 1023]      |

---

## 2. Script `lefschetz_power_estimate.py`

### 2.1 Relação com o Teorema

O script cria uma simulação numérica que se inspira no crescimento dos valores associados ao teorema, adaptando-os a um contexto computacional usando potências de 2 e números de Mersenne.

### 2.2 Objetivo do Script

* Estimar valores que crescem dentro do intervalo definido por potências de 2.
* Usar aproximações matemáticas sem depender dos valores esperados como entrada.
* Gerar uma tabela coerente e visualmente compreensível para análise.

### 2.3 Exemplo de Saída

```bash
N  | 2^N (Início)   | Mersenne (2^N - 1)    | L(f) Estimado    | Intervalo
--------------------------------------------------------------------------------
0  | 1              | 0                     | 1                | [1, 1]
1  | 2              | 1                     | 3                | [2, 3]
2  | 4              | 3                     | 7                | [4, 7]
3  | 8              | 7                     | 15               | [8, 15]
...
````

### 2.4 Funcionamento Interno

* Utiliza **logaritmo na base 2** para estimar o crescimento do valor L(f).
* Usa a expressão:

  ```
  estimado = (2^n) * log2(n + 1) + n^1.5
  ```
* Garante que o valor esteja dentro do intervalo \[2^n, 2^(n+1)-1].

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10**
* Nenhuma biblioteca externa é necessária.
* Compatível com qualquer sistema operacional que tenha Python instalado.

---

## 3 Extras

### 3.1 Licença

Distribuído sob a licença **MIT**.

### 3.2 Referências

* [Wikipedia: Lefschetz Fixed Point Theorem](https://en.wikipedia.org/wiki/Lefschetz_fixed-point_theorem)
* [Mersenne Numbers](https://en.wikipedia.org/wiki/Mersenne_prime)

### 3.3 Testes e Validações

O script foi executado localmente no terminal do Windows com sucesso, gerando a tabela completa de forma legível.

---

## 4 Contato

* Feito por **CanalQb** no GitHub
* Visite o blog: [https://canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via **Bitcoin**: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* **PIX:** [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**ponto fixo:**
Um ponto onde a função aplicada retorna o próprio valor. Exemplo: se f(5) = 5, então 5 é ponto fixo.

**contínua:**
Uma função sem saltos ou quebras. O gráfico da função pode ser desenhado sem tirar o lápis do papel.

**homologia:**
Uma técnica matemática usada para "medir buracos" em um espaço, muito usada em topologia.

**logaritmo (log2):**
Função que responde à pergunta: "qual potência de 2 dá o número que eu tenho?"

**mersenne:**
Números da forma 2^n - 1, usados em criptografia, teoria dos números e outras áreas da matemática.
