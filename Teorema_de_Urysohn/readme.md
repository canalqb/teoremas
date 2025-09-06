# 🧠 - Teorema de Urysohn

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Urysohn-ff69b4.svg)](https://en.wikipedia.org/wiki/Urysohn's_lemma)

## Frase do Teorema

> Se dois conjuntos diferentes não se tocam dentro de um espaço com boas propriedades, existe uma forma suave (função) de separar eles usando apenas números entre 0 e 1.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `urysohn_mersenne_map.py`](#2-script-urysohn_mersenne_mappy)

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

O Teorema de Urysohn mostra que é possível separar dois conjuntos completamente separados dentro de um espaço bem comportado, usando uma função que vai de 0 a 1 de forma contínua (sem saltos).

---

### 1.2 Exemplos Práticos

* Imagine uma régua de 0 a 1.
* Se você tem dois pontos fixos nela (por exemplo, início e fim de um intervalo), o teorema garante que existe uma função que começa em 0 no primeiro ponto e vai crescendo até chegar em 1 no segundo ponto.
* Mesmo que você tenha muitos pontos no meio, essa função vai crescendo suavemente entre eles.

---

### 1.3 Explicação Detalhada

O teorema foi criado por Pavel Urysohn e trata de **espaços topológicos normais**, que são locais onde se pode distinguir bem conjuntos diferentes. Se você tem dois conjuntos que não se sobrepõem, o teorema diz que há uma função suave (sem saltos) que vale 0 em um conjunto e 1 no outro.

Neste repositório, aplicamos esse conceito de forma discreta, usando apenas números inteiros e potências de 2, como uma aproximação computacional simples.

---

### 1.4 Aplicações

* Processamento de imagem (diferenciar regiões com suavidade)
* Inteligência Artificial (normalização de variáveis)
* Matemática pura (provar outros teoremas)
* Simulações discretas e aproximações de funções contínuas

---

### 1.5 Análise da Tabela

A tabela gerada pelo script segue o formato:

```
N | Início (2^N) | Estimado f⁻¹(0.7) | Fim (2^(N+1)-1)
```

* O início e fim formam os conjuntos disjuntos.
* O valor intermediário (estimado) é onde a função atingiria cerca de **70% de transição** entre início e fim — ou seja, onde `f(x) ≈ 0.7`.
* Essa é uma maneira prática de representar o Teorema de Urysohn em números.

---

## 2. Script `urysohn_mersenne_map.py`

### 2.1 Relação com o Teorema

O script implementa uma versão discreta e computacional da ideia central do teorema: **interpolar suavemente entre dois extremos**. Ele faz isso usando potências de 2 e simula a função de separação contínua.

---

### 2.2 Objetivo do Script

* Criar uma tabela com colunas baseadas em potências de 2.
* Usar uma função contínua (linear) para estimar um valor intermediário.
* Mostrar como o Teorema de Urysohn pode ser aplicado em estruturas numéricas simples.

---

### 2.3 Exemplo de Saída

Rodando o script:

```
 N |  Início (2^N) | Estimado f⁻¹(0.7) |   Fim (2^(N+1)-1)
---------------------------------------------------------------
 0 |             1 |                     1 |                 1
 1 |             2 |                     3 |                 3
 2 |             4 |                     6 |                 7
 3 |             8 |                    13 |                15
 4 |            16 |                    26 |                31
 5 |            32 |                    54 |                63
 6 |            64 |                   108 |               127
 7 |           128 |                   217 |               255
 8 |           256 |                   434 |               511
 9 |           512 |                   870 |              1023
```

---

### 2.4 Funcionamento Interno

* A função `f(x) = (x - inicio) / (fim - inicio)` simula a transição suave entre início e fim.
* Para achar um valor `x` onde `f(x) = 0.7`, usamos a fórmula invertida:

  ```
  x = inicio + 0.7 * (fim - inicio)
  ```
* Isso garante um ponto intermediário coerente com a ideia de suavidade entre conjuntos separados.

---

### 2.5 Tecnologias e Requisitos

* ✅ Python 3.8.10
* Não são necessárias bibliotecas externas
* Funciona em qualquer terminal (Linux, Windows, Mac)

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

### 3.2 Referências

* Wikipedia: [Teorema de Urysohn](https://en.wikipedia.org/wiki/Urysohn's_lemma)
* Livro de Topologia Geral - Stephen Willard
* Curso de Matemática - Topologia Introdutória

---

### 3.3 Testes e Validações

* Validado com Python 3.8.10
* Todos os resultados comparados com potências de 2 e Mersenne
* Resultados consistentes com a ideia de interpolação contínua

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Contínuo**: significa que não há saltos ou buracos entre os valores.
**Função**: uma regra que associa cada valor de entrada a um único valor de saída.
**Normal**: um tipo especial de espaço matemático onde conjuntos separados podem ser tratados de forma organizada.
**Interpolar**: calcular um valor entre dois extremos, de forma proporcional.
**Potência de 2**: valores como 2, 4, 8, 16, 32... obtidos multiplicando 2 várias vezes.
**Mersenne**: número na forma 2^N - 1, usado em várias áreas da matemática.
**Estimado**: valor aproximado calculado com base em uma função matemática.
