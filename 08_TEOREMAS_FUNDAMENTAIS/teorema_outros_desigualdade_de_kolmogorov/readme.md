# 🧩 - Desigualdade De Kolmogorov

## 🧾 Frase do Teorema

> A probabilidade do *máximo desvio absoluto* da soma acumulada de variáveis aleatórias independentes e com média zero ultrapassar um limite λ é limitada pelo valor da variância total dividido por λ².

## 📚 Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `Desigualdade_de_Kolmogorov.py`](#2-script-desigualdade_de_kolmogorompy)

  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3 Extras](#3-extras)

  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referencias)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4 📬 Contato](#4-📬-contato)
* [5. Nota](#5-nota)

---

## 1. Introdução ao Teorema

### 1.1 Resumo

A **Desigualdade de Kolmogorov** é um resultado da teoria das probabilidades que permite controlar o *risco* de grandes desvios na soma acumulada de variáveis aleatórias independentes e com média zero. Ela fornece um limite superior para a chance de que a soma parcial máxima ultrapasse um valor escolhido λ.

Matematicamente, para variáveis X₁, X₂, ..., Xₙ independentes com média zero, definimos as somas parciais como:

```
S_k = X₁ + X₂ + ... + X_k
```

A desigualdade diz que, para qualquer valor positivo λ:

```
P(max |S_k| para k=1 até n >= λ) <= E[S_n²] / λ²
```

Ou seja, a probabilidade do *maior desvio absoluto* ser maior que λ é limitada pela variância total da soma dividida por λ².

### 1.2 Exemplos Práticos

Imagine que você:

* Está somando resultados de lançamentos de dados;
* Avalia as variações acumuladas no preço de uma ação na bolsa;
* Ou acompanha erros acumulados em medições.

A desigualdade ajuda a estimar qual a chance dessas somas acumuladas desviarem muito do valor esperado, mesmo sem conhecer a distribuição exata das variáveis.

### 1.3 Explicação Detalhada

O teorema é especialmente útil para controlar *desvios máximos* em processos estocásticos e reforça resultados como a Lei dos Grandes Números e o Teorema Central do Limite.

Ele funciona para qualquer somatório parcial, ou seja, em qualquer instante k ≤ n, e não apenas para o total Sₙ.

### 1.4 Aplicações

* **Finanças**: controlar risco de movimentos extremos acumulados em preços ou retornos.
* **Engenharia**: análise de falhas e erros acumulados em processos.
* **Estatística**: base para criação e validação de testes estatísticos e intervalos de confiança.
* **Ciência de Dados**: validação de modelos probabilísticos e predição.

### 1.5 Análise da Tabela

A tabela abaixo mostra como a probabilidade do desvio extremo diminui rapidamente à medida que o tamanho n da soma parcial cresce, usando λ = 2n - 1 como limite:

| 2^A | Limite da Probabilidade (E\[S\_n²]/λ²) | λ = 2n - 1 |
| --- | -------------------------------------- | ---------- |
| 1   | 1.000000                               | 1          |
| 2   | 0.222222                               | 3          |
| 4   | 0.081633                               | 7          |
| 8   | 0.035556                               | 15         |
| 16  | 0.016653                               | 31         |
| 32  | 0.008065                               | 63         |
| 64  | 0.003962                               | 127        |
| 128 | 0.001966                               | 255        |
| 256 | 0.000979                               | 511        |

---

## 2. Script `Desigualdade_de_Kolmogorov.py`

### 2.1 Relação com o Teorema

O script ilustra na prática o comportamento da Desigualdade de Kolmogorov, calculando o limite superior da probabilidade para somas parciais de tamanhos 2^A, com λ = 2n - 1.

### 2.2 Objetivo do Script

Visualizar como a probabilidade do desvio extremo diminui rapidamente conforme aumentamos n, reforçando a aplicabilidade do teorema em casos reais.

### 2.3 Exemplo de Saída

```
| 2^A | Limite da Probabilidade | λ = 2n - 1 |
|-----|-------------------------|------------|
| 1   | 1.000000                | 1          |
| 2   | 0.222222                | 3          |
| ... | ...                     | ...        |
```

### 2.4 Funcionamento Interno

* Para A de 0 a 8:

  * Calcula n = 2^A;
  * Define λ = 2n - 1;
  * Calcula limite = n / λ²;
* Imprime os valores em formato tabular.

### 2.5 Tecnologias e Requisitos

* Python 3
* Biblioteca pandas (para manipulação e exibição de tabelas)

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a licença MIT — consulte o arquivo LICENSE para detalhes.

### 3.2 Referências

* William Feller, *An Introduction to Probability Theory and Its Applications*, 1957.
* Kolmogorov, A. N., "On the Empirical Determination of a Distribution Law", 1933.

### 3.3 Testes e Validações

O script foi testado com valores de A variando de 0 a 8 e os resultados conferem com os limites teóricos do teorema.

---

## 4 📬 Contato

* Feito por **CanalQb** no GitHub
* Visite o blog: [canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

Aqui explicamos alguns termos e símbolos importantes usados:

* **λ (lambda)**: o *limite* para o desvio máximo considerado.
* **S\_k**: soma das primeiras k variáveis aleatórias (parcial da soma total).
* **E\[S\_n²]**: esperança do quadrado da soma total, equivalente à variância total quando as variáveis têm média zero.
* **P(...)**: probabilidade de o evento dentro dos parênteses ocorrer.
* **max |S\_k| para k=1 até n**: o maior valor absoluto das somas parciais, entre 1 e n.
