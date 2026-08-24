# 🧩 - De Peano

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Frase do Teorema

> **Teorema de Peano**: O teorema define formalmente os números naturais com base em axiomas simples, usando a ideia de sucessores para construir números naturais a partir de 0.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `teorema_peano_justificativa.py`](#2-script-peano_justificativapy)

  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3. Extras](#3-extras)

  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referências)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4. Contato](#4-contato)
* [5. Nota](#5-nota)

---

## 1. Introdução ao Teorema

### 1.1 Resumo

O **Teorema de Peano** estabelece uma base formal para os números naturais. A ideia central é que, começando de 0, podemos construir todos os números naturais aplicando a operação de "sucessor" repetidamente. Ele é fundamental para a aritmética e serve de base para muitos conceitos em matemática.

### 1.2 Exemplos Práticos

Exemplo simples de construção de números naturais com base no Teorema de Peano:

* Começamos com 0.
* O sucessor de 0 é 1.
* O sucessor de 1 é 2, e assim por diante.

### 1.3 Explicação Detalhada

O **Teorema de Peano** define três axiomas principais:

1. **0 é um número natural**.
2. **Para todo número natural n, existe um sucessor de n**, denotado como "S(n)".
3. **Não existe nenhum número natural cujo sucessor seja 0**.

Isso nos permite definir e trabalhar com os números naturais de maneira formal, construindo-os progressivamente a partir de 0.

### 1.4 Aplicações

O Teorema de Peano é usado em diversas áreas, como:

* **Teoria dos Números**: para entender a estrutura dos números naturais.
* **Lógica Matemática**: como base para a construção formal de provas.
* **Computação**: como fundamento para algoritmos que operam com números naturais.

### 1.5 Análise da Tabela

Na tabela abaixo, temos o intervalo entre os valores **Inicio (2^N)** e **Fim (2^(N+1) - 1)** para $N$ variando de 0 a 9. A coluna "Esperado pelo Teorema" aproxima os valores esperados dentro desse intervalo, usando a média entre o início e o fim.

| N | Inicio (2^N) | Esperado pelo teorema | Fim (2^(N+1))-1 |
| - | ------------ | --------------------- | --------------- |
| 0 | 1            | 1                     | 1               |
| 1 | 2            | 2                     | 3               |
| 2 | 4            | 5                     | 7               |
| 3 | 8            | 11                    | 15              |
| 4 | 16           | 23                    | 31              |
| 5 | 32           | 47                    | 63              |
| 6 | 64           | 95                    | 127             |
| 7 | 128          | 191                   | 255             |
| 8 | 256          | 383                   | 511             |
| 9 | 512          | 767                   | 1023            |

---

## 2. Script `teorema_peano_justificativa.py`

### 2.1 Relação com o Teorema

O script `teorema_peano_justificativa.py` usa o intervalo definido pelo Teorema de Peano para calcular uma aproximação dos valores "esperados" entre o **Inicio (2^N)** e **Fim (2^(N+1) - 1)**. A fórmula utilizada para calcular o "Esperado pelo Teorema" é uma média simples entre o início e o fim do intervalo, o que justifica a aproximação dos resultados.

### 2.2 Objetivo do Script

O objetivo do script é calcular, para cada valor de $N$ de 0 a 9, um valor aproximado do "Esperado pelo Teorema", dentro do intervalo determinado por $2^N$ e $2^{(N+1)} - 1$. Esses valores são apresentados em uma tabela.

### 2.3 Exemplo de Saída

Ao rodar o script, o seguinte será impresso:

```
N   Inicio (2^N)    Esperado pelo teorema     Fim (2^(N+1))-1
0   1               1                         1
1   2               2                         3
2   4               5                         7
3   8               11                        15
4   16              23                        31
5   32              47                        63
6   64              95                        127
7   128             191                       255
8   256             383                       511
9   512             767                       1023
```

### 2.4 Funcionamento Interno

O script realiza os seguintes passos:

1. Para cada valor de $N$, calcula o **Inicio** como $2^N$ e o **Fim** como $2^{(N+1)} - 1$.
2. A fórmula para o **Esperado pelo Teorema** é a média do intervalo entre o **Inicio** e o **Fim**.
3. A tabela é gerada e exibida no terminal, mostrando os resultados para $N$ de 0 a 9.

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10 ou superior**.
* Nenhuma biblioteca externa é necessária para rodar o script.

---

## 3. Extras

### 3.1 Licença

Este projeto é licenciado sob a licença **MIT**. Para mais informações, consulte o arquivo `LICENSE`.

### 3.2 Referências

* [Teorema de Peano - Wikipedia](https://en.wikipedia.org/wiki/Peano_axioms)
* [Lei dos Grandes Números - Wikipedia](https://en.wikipedia.org/wiki/Law_of_large_numbers)

### 3.3 Testes e Validações

Os valores esperados pela tabela são testados para garantir que a fórmula forneça resultados dentro do intervalo estabelecido.

---

## 4. Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Esperado pelo teorema**: Refere-se ao valor aproximado calculado dentro do intervalo definido pelo teorema. Neste caso, usamos a média entre o início e o fim do intervalo como uma boa aproximação.
