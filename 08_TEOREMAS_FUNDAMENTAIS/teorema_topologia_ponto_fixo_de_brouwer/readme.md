# 🔁 - Teorema do Ponto Fixo de Brouwer

[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Teorema](https://img.shields.io/badge/Teorema-Ponto%20Fixo%20de%20Brouwer-ff69b4.svg)](https://en.wikipedia.org/wiki/Brouwer_fixed-point_theorem)

## 🧠 Frase do Teorema

> *Toda função contínua que mapeia um espaço compacto e convexo em si mesmo tem pelo menos um ponto fixo.* – Ou seja, existe algum valor que, ao ser aplicado na função, retorna ele mesmo.

---

## 📚 Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `brouwer_fixpoint_2pow.py`](#2-script-brouwer_fixpoint_tablepy)

  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3. Extras](#3-extras)

  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referencias)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4. Contato](#4-contato)
* [5. Nota](#5-nota)

---

## 1. Introdução ao Teorema

### 1.1 Resumo

O **Teorema do Ponto Fixo de Brouwer** é um resultado da matemática que garante que, em certas condições, existe pelo menos um ponto que permanece no mesmo lugar após ser transformado por uma função.

### 1.2 Exemplos Práticos

Imagine mexer suavemente no conteúdo de uma tigela de sopa com uma colher: por mais que você mexa, **sempre haverá uma gota que não saiu do lugar**. Este é um ponto fixo!

### 1.3 Explicação Detalhada

Para qualquer função contínua aplicada a um intervalo fechado e limitado, se o resultado continua dentro do mesmo intervalo, **existe pelo menos um ponto que se mapeia para si mesmo**.

Exemplo simples:

```python
def f(x):
    return cos(x) * 0.5 + 0.5
```

Se x estiver no intervalo \[0, 1], o valor de f(x) também estará. Logo, existe algum x onde `f(x) == x`.

### 1.4 Aplicações

* Equilíbrio de mercados econômicos
* Equilíbrios de Nash (jogos e decisões)
* Simulações numéricas e estabilidade
* Inteligência Artificial e sistemas dinâmicos

### 1.5 Análise da Tabela

A tabela usada no script apresenta valores empíricos que **simulam pontos fixos** dentro de intervalos definidos por potências de 2:

| N   | Início (2^N) | Valor (ponto fixo esperado) | Fim (2^(N+1) - 1) |
| --- | ------------ | --------------------------- | ----------------- |
| 0   | 1            | 1                           | 1                 |
| 1   | 2            | 3                           | 3                 |
| 2   | 4            | 7                           | 7                 |
| 3   | 8            | 8                           | 15                |
| 4   | 16           | 21                          | 31                |
| ... | ...          | ...                         | ...               |

---

## 2. Script `brouwer_fixpoint_2pow.py`

### 2.1 Relação com o Teorema

Este script **aplica uma função contínua** dentro de intervalos construídos com potências de 2, simulando o comportamento do Teorema de Brouwer — procurando um ponto fixo que satisfaça `f(x) == x`.

### 2.2 Objetivo do Script

Para cada valor de N:

1. Define o intervalo `[2^N, 2^(N+1) - 1]`
2. Normaliza um valor dentro desse intervalo para `[0, 1]`
3. Aplica a função contínua `f(x) = cos(x) * 0.5 + 0.5`
4. Calcula a diferença entre `x` e `f(x)`
5. Compara e analisa se `x` é (ou está próximo de) um ponto fixo

### 2.3 Exemplo de Saída

```text
N  | x     | x_norm     | f(x_norm)    | |f - x|        | x / 2^N  
------------------------------------------------------------------------
0  | 1     | 0.000000   | 1.000000     | 1.000000       | 1.000000  
1  | 3     | 0.500000   | 0.938791     | 0.438791       | 1.500000  
2  | 7     | 0.750000   | 0.843228     | 0.093228       | 1.750000  
3  | 8     | 0.000000   | 1.000000     | 1.000000       | 1.000000  
...
```

### 2.4 Funcionamento Interno

O script possui as seguintes funções:

* `f(x)`: função contínua baseada em cosseno
* `normalize(x, N)`: transforma x para o intervalo \[0, 1]
* `main()`: executa o loop pelos dados da tabela e imprime os resultados formatados

### 2.5 Tecnologias e Requisitos

* Python 3.8.10 ✅
* Biblioteca padrão (`math`)
* Compatível com qualquer sistema que suporte Python 3+

---

## 3. Extras

### 3.1 Licença

Distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

### 3.2 Referências

* [Teorema do Ponto Fixo – Wikipedia](https://en.wikipedia.org/wiki/Brouwer_fixed-point_theorem)
* [Funções Contínuas](https://pt.khanacademy.org/math)
* [Canal Qb no GitHub](https://github.com/CanalQb)

### 3.3 Testes e Validações

Este script foi executado com:

```bash
python3 brouwer_fixpoint_2pow.py
```

Funciona corretamente com saída tabulada.

---

## 4. Contato

* Feito por **CanalQb** no GitHub
* Visite o blog: canalqb.blogspot.com ➡ [https://canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via **Bitcoin**: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* **PIX:** [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Função contínua:**
É uma função suave, sem saltos ou quebras. Exemplo: cosseno, seno, etc.

**Ponto fixo:**
É um valor que, ao ser aplicado na função, retorna ele mesmo. Ou seja, `f(x) = x`.

**Espaço compacto:**
É um conjunto limitado e fechado (com bordas incluídas).

**Convexo:**
Se você pegar dois pontos quaisquer no conjunto e a linha entre eles estiver dentro do conjunto, ele é convexo.

**Normalizar:**
Transformar um valor de qualquer intervalo para um intervalo entre 0 e 1.
