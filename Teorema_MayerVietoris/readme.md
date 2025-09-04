# 🔍 - Teorema Mayer–Vietoris
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Mayer--Vietoris-ff69b4.svg)](https://en.wikipedia.org/wiki/Mayer–Vietoris_sequence)

## Frase do Teorema

> Se um espaço pode ser decomposto em duas partes com interseção controlada, então é possível calcular informações globais (como formas e buracos) a partir das partes menores – ou seja, o todo pode ser entendido pelas partes.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `mvtabela_extrator.py`](#2-script-mvtabela_extratorpy)
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

O teorema de Mayer–Vietoris é uma técnica usada para calcular propriedades de objetos complexos, usando informações de partes mais simples. É uma estratégia de decomposição e reconstrução.

### 1.2 Exemplos Práticos

- Análise de formas em computação gráfica
- Entendimento de espaços topológicos
- Quebra de problemas complexos em blocos mais simples

### 1.3 Explicação Detalhada

Se um objeto pode ser dividido em duas partes que se sobrepõem de forma controlada, é possível extrair informações globais usando as informações dessas partes e da sobreposição.

### 1.4 Aplicações

- Matemática pura (homologia, álgebra)
- Ciência de dados (decomposição)
- Análise de algoritmos recursivos

### 1.5 Análise da Tabela

O script usa a lógica de crescimento cumulativo. A ideia é simular uma **construção incremental**, em que cada novo intervalo reutiliza resultados anteriores, refletindo o espírito do teorema.

---

## 2. Script `mvtabela_extrator.py`

### 2.1 Relação com o Teorema

Simula a ideia de "somar as partes" para formar o todo. Em vez de trabalhar com grupos de homologia, trabalha com blocos de números.

### 2.2 Objetivo do Script

Construir uma tabela com:

- O valor inicial do intervalo (2^N)
- O valor final (2^(N+1)-1)
- Uma estimativa "esperada" que cresce com base nos valores anteriores

Sem usar diretamente a coluna de "esperado pelo teorema".

### 2.3 Exemplo de Saída

```text
N   | Inicio (2^N)   | Estimado       | Fim (2^(N+1))-1
------------------------------------------------------------
0   | 1              | 1              | 1
1   | 2              | 3              | 3
2   | 4              | 7              | 7
3   | 8              | 15             | 15
4   | 16             | 31             | 31
5   | 32             | 63             | 63
6   | 64             | 127            | 127
7   | 128            | 255            | 255
8   | 256            | 511            | 511
9   | 512            | 1023           | 1023
````

### 2.4 Funcionamento Interno

* Usa potências de 2 para definir intervalos.
* Soma os tamanhos de intervalos aos valores acumulados.
* Simula a sobreposição e expansão das partes.

### 2.5 Tecnologias e Requisitos

* Python 3.8.10
* Sem bibliotecas externas
* Executar com:

```bash
python mvtabela_extrator.py
```

---

## 3 Extras

### 3.1 Licença

MIT License

### 3.2 Referências

* [Wikipedia: Mayer–Vietoris sequence](https://en.wikipedia.org/wiki/Mayer–Vietoris_sequence)
* CanalQB blog

### 3.3 Testes e Validações

Validação feita por inspeção visual da tabela gerada com relação ao crescimento por partes.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com
  👉 [https://canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin:
  `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**teorema:**
é uma afirmação matemática que pode ser provada com base em outros resultados aceitos.

**potência de 2:**
é um número obtido multiplicando 2 por ele mesmo várias vezes, como 2, 4, 8, 16...

**acumulado:**
é o valor total somado até um certo ponto.

**intervalo:**
é o espaço entre dois números, inclusive os próprios.

**homologia:**
é uma ferramenta matemática usada para estudar a forma de objetos em várias dimensões.
