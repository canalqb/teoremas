# 🧩 - De Kraft Mcmillan

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Kraft%E2%80%93McMillan-ff69b4.svg)](https://en.wikipedia.org/wiki/Kraft%E2%80%93McMillan_inequality)

## Frase do Teorema

> *Se a soma de 2 elevado a menos o comprimento de cada código binário for menor ou igual a 1, então existe um código prefixo com esses comprimentos.* – Em outras palavras, dá para construir um sistema de codificação sem ambiguidade se essa soma for no máximo 1.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `Teorema_de_Kraft_McMillan.py`](#2-script-teorema_de_kraft_mcmillanpy)

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

O **Teorema de Kraft–McMillan** define uma condição necessária e suficiente para a existência de **códigos prefixos** (sem ambiguidade) baseados nos comprimentos dos códigos. Isso é essencial em compressão de dados, como nos algoritmos de Huffman.

### 1.2 Exemplos Práticos

Imagine um conjunto de símbolos codificados em binário. Se os comprimentos desses códigos forem: 2, 3, e 3, então a soma `2^-2 + 2^-3 + 2^-3 = 0.25 + 0.125 + 0.125 = 0.5`, que é menor que 1. Isso significa que existe uma forma de codificar esses símbolos sem que um código seja prefixo de outro.

### 1.3 Explicação Detalhada

A fórmula geral é:
**Soma de 2 elevado a menos o comprimento do código ≤ 1**
Ou seja, se `l_i` representa o comprimento do i-ésimo código, então:
**2^(-l\_1) + 2^(-l\_2) + ... + 2^(-l\_n) <= 1**

Se essa soma der exatamente 1, o código é chamado de *completo* (não cabe mais ninguém sem perder a propriedade de prefixo).

### 1.4 Aplicações

* Compressores de dados (ex: zip, jpeg)
* Codificação de fontes (teorema de Shannon)
* Algoritmo de Huffman
* Árvores binárias otimizadas

### 1.5 Análise da Tabela

O script usa uma tabela com tripletas `(x, y, z)`, onde:

* `x` e `z` são potências de 2
* `y` cresce com base nesses valores

O crescimento é modelado e previsto com base no comportamento logarítmico dos dados.

---

## 2. Script `Teorema_de_Kraft_McMillan.py`

### 2.1 Relação com o Teorema

Embora o script não aplique diretamente a fórmula do Teorema, ele **explora uma estrutura binária crescente** — uma característica fundamental em codificação de prefixo e árvores de decisão. O uso de potências de 2 e o padrão de crescimento têm uma analogia conceitual com sistemas binários.

### 2.2 Objetivo do Script

* Prever o valor de `y` para `x = 65536`, baseado nos dados anteriores
* Ajustar uma regressão linear com `log2(x)` como variável explicativa
* Visualizar o padrão de crescimento e comparar a previsão com o valor real (`95823`)

### 2.3 Exemplo de Saída

```
Valor previsto para x = 65536: 95720.41
Valor real conhecido: 95823
Erro absoluto: 102.59
```

Gráfico e tabela são gerados mostrando todos os pontos e a linha de tendência.

### 2.4 Funcionamento Interno

1. Transforma `x` em `log2(x)`
2. Ajusta a regressão linear: `y = a * log2(x) + b`
3. Previsão para `x = 65536` (log2 = 16)
4. Compara valor previsto com o real
5. Gera gráfico interativo (`plotly`) e exibe tabela de erro

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10**
* **NumPy**, **Pandas**
* **Scikit-learn** (para regressão)
* **Plotly** (para gráfico interativo)

Instale os pacotes:

```bash
pip install numpy pandas scikit-learn plotly
```

Execute com:

```bash
python Teorema_de_Kraft_McMillan.py
```

---

## 3 Extras

### 3.1 Licença

Este projeto está sob a **Licença MIT** — livre para uso e modificação com créditos ao autor.

### 3.2 Referências

* Kraft–McMillan inequality: [https://en.wikipedia.org/wiki/Kraft%E2%80%93McMillan\_inequality](https://en.wikipedia.org/wiki/Kraft%E2%80%93McMillan_inequality)
* Codificação de Huffman: [https://pt.wikipedia.org/wiki/Codifica%C3%A7%C3%A3o\_de\_Huffman](https://pt.wikipedia.org/wiki/Codifica%C3%A7%C3%A3o_de_Huffman)
* Árvores binárias em compressão: [https://en.wikipedia.org/wiki/Binary\_tree](https://en.wikipedia.org/wiki/Binary_tree)

### 3.3 Testes e Validações

* A previsão foi validada com dados reais (`y = 95823`)
* O erro de previsão ficou abaixo de 0.2%
* A curva se encaixa bem com crescimento logarítmico de `x`

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

* **Código prefixo**: um código em que nenhum código é o começo (prefixo) de outro. Ex: 0, 10, 110 são prefixos válidos.
* **Função log2**: calcula o logaritmo de base 2. Usada para transformar crescimentos exponenciais em linhas retas.
* **Regressão linear**: técnica que encontra uma reta que melhor aproxima um conjunto de pontos.
* **Potências de 2**: números como 2, 4, 8, 16, 32... que representam o crescimento típico de estruturas binárias.
* **Modelo preditivo**: ferramenta matemática usada para prever valores futuros com base em dados observados.
