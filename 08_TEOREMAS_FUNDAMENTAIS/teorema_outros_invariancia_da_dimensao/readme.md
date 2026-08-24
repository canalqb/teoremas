# 🧩 - Invariancia Da Dimensao
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Invariância%20da%20Dimensão-ff69b4.svg)](https://en.wikipedia.org/wiki/Dimension_theorem)

## Frase do Teorema

> *Se dois espaços possuem dimensões diferentes, então não podem ser transformados um no outro sem perder suas propriedades contínuas essenciais* – isso significa que não existe uma forma de "esticar ou deformar" um espaço de uma dimensão para outra diferente sem romper sua estrutura.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `invariancia_dimensao.py`](#2-script-invariancia_dimensaopy)
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

---

## 1. Introdução ao Teorema

### 1.1 Resumo

A invariância da dimensão mostra que a estrutura de um espaço depende de sua dimensão. Você **não consegue transformar** uma linha em um plano ou um cubo em um hipercubo apenas com deformações contínuas, sem "romper" a forma.

### 1.2 Exemplos Práticos

- Uma folha de papel (2D) não pode se transformar em uma bola (3D) apenas com dobras e torções contínuas sem rasgar.
- Um ponto (0D) não pode se transformar em uma linha (1D) sem criar uma nova dimensão.

### 1.3 Explicação Detalhada

Esse princípio é usado para **distinguir espaços matemáticos**. Em termos simples, ele garante que **cada dimensão é única e não pode ser confundida com outra**.

### 1.4 Aplicações

- Visualizações em gráficos e geometria computacional.
- Provas matemáticas que precisam distinguir entre espaços.
- Construção de estruturas complexas como árvores binárias, cubos, hipercubos e redes.

### 1.5 Análise da Tabela

Neste projeto, usamos uma tabela com três colunas principais:

```

N | Início (2^N) | Estimado | Fim (2^(N+1)-1)

```

- **Início** é sempre uma potência de 2 (2^N)
- **Fim** é o número Mersenne correspondente: 2^(N+1) - 1
- **Estimado** é um valor calculado com base em uma lógica progressiva, **sem copiar diretamente os valores esperados**, mas tentando permanecer **dentro do intervalo entre Início e Fim**

---

## 2. Script `invariancia_dimensao.py`

### 2.1 Relação com o Teorema

O script **não prova o teorema**, mas **usa os princípios de crescimento não-linear entre dimensões** para construir uma tabela de estimativas. Cada nova linha representa uma mudança de dimensão e como isso pode afetar o valor estimado.

### 2.2 Objetivo do Script

Criar uma **estimativa numérica** dentro de cada intervalo [2^N, 2^(N+1) - 1] que siga uma lógica acumulativa e coerente com os aumentos de complexidade dimensional.

### 2.3 Exemplo de Saída

```text
 N | Inicio (2^N) | Esperado | Fim (2^(N+1)-1)
--------------------------------------------------
 0 |             1 |        1 |                 1
 1 |             2 |        3 |                 3
 2 |             4 |        7 |                 7
 3 |             8 |       11 |                15
 4 |            16 |       26 |                31
 5 |            32 |       49 |                63
 6 |            64 |       89 |               127
 7 |           128 |      160 |               255
 8 |           256 |      288 |               511
 9 |           512 |      400 |              1023
````

### 2.4 Funcionamento Interno

* Começa com valor base 1
* Para cada linha, calcula o intervalo \[inicio, fim]
* Estima um valor no meio do intervalo com base no resultado anterior, adicionando cerca de **metade da largura do intervalo**
* Armazena o resultado de forma acumulativa

### 2.5 Tecnologias e Requisitos

* 🐍 Python 3.8.10
* Nenhuma biblioteca externa necessária
* Funciona em qualquer terminal ou notebook Python

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

### 3.2 Referências

* Wikipédia: [Invariância da Dimensão](https://en.wikipedia.org/wiki/Dimension_theorem)
* Livro: Topologia Geral – Stephen Willard
* Curso de Topologia Básica – Canal Matemática Rio

### 3.3 Testes e Validações

* Validação feita com comparações simples dos valores estimados com a faixa de início e fim
* Todos os valores permanecem dentro dos limites calculados
* Verificações manuais em N de 0 a 9

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Mersenne:**
Números especiais que são 1 a menos que uma potência de 2. Por exemplo, 3, 7, 15, 31.

**Início (2^N):**
Valor base de cada linha da tabela. Representa uma potência de 2.

**Fim (2^(N+1)-1):**
Número final do intervalo, um número de Mersenne. É sempre uma unidade menor que a próxima potência de 2.

**Estimado:**
Valor calculado com base em regras simples para se manter entre o Início e o Fim.

**Acumulador:**
Variável usada para guardar o último valor estimado, servindo de base para o próximo.

**Intervalo:**
A diferença entre o Início e o Fim. Mostra o espaço de crescimento possível entre as dimensões.
