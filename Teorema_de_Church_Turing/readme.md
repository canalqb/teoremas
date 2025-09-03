# 🤖 - Teorema de Church–Turing  
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![LGN](https://img.shields.io/badge/Teorema-Church%E2%80%93Turing-ff69b4.svg)](https://en.wikipedia.org/wiki/Church%E2%80%93Turing_thesis)  

## Frase do Teorema

> Qualquer função que pode ser calculada logicamente pode ser executada por uma máquina de Turing – ou seja, tudo que é computável pode ser simulado por um modelo simples e universal.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `estimador_church_turing.py`](#2-script-estimador_church_turingpy)  
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

O **Teorema de Church–Turing** diz que qualquer processo que possa ser descrito como uma sequência lógica de passos (um algoritmo) pode ser executado por uma máquina de Turing — um modelo simples e universal de computação.

### 1.2 Exemplos Práticos

- Todos os algoritmos em linguagens de programação conhecidas podem ser simulados por uma máquina de Turing.  
- Isso unifica diferentes modelos de computação, mostrando que têm o mesmo poder.

### 1.3 Explicação Detalhada

Pense em uma máquina de Turing como um computador básico que lê e escreve símbolos em uma fita infinita. O teorema diz que qualquer coisa que um algoritmo possa fazer, essa máquina também consegue fazer, mesmo que de forma lenta ou com muitos passos.

### 1.4 Aplicações

- Fundamentos da ciência da computação e teoria da computação.  
- Definição do que é computável e o que não é.  
- Compreensão dos limites dos programas e algoritmos.

### 1.5 Análise da Tabela

A tabela gerada pelo script mostra estimativas da quantidade de programas computáveis possíveis entre potências de 2, refletindo o crescimento realista e controlado dessa quantidade, diferente do crescimento puramente exponencial.

---

## 2. Script `estimador_church_turing.py`

### 2.1 Relação com o Teorema

O script usa o conceito do Teorema de Church–Turing para estimar quantos processos computáveis cabem em intervalos que crescem em potências de 2, lembrando que nem todas as sequências de bits formam programas válidos.

### 2.2 Objetivo do Script

- Calcular para cada N os valores: início (2^N), fim (2^(N+1)-1) e uma estimativa de processos computáveis.  
- Mostrar que o número de computações válidas cresce, mas não tão rápido quanto o número total de combinações possíveis.

### 2.3 Exemplo de Saída

```text
N   | Início (2^N)   | Estimado (Teorema)   | Fim (2^(N+1)-1)
-----------------------------------------------------------------
0   | 1              | 1                    | 1
1   | 2              | 2                    | 3
2   | 4              | 5                    | 7
3   | 8              | 9                    | 15
4   | 16             | 21                   | 31
5   | 32             | 44                   | 63
6   | 64             | 85                   | 127
7   | 128            | 170                  | 255
8   | 256            | 340                  | 511
9   | 512            | 512                  | 1023
````

### 2.4 Funcionamento Interno

* Calcula os limites dos intervalos por potências de 2.
* Aplica uma função estimadora para aproximar a quantidade de programas computáveis dentro do intervalo.
* Imprime a tabela formatada no terminal.

### 2.5 Tecnologias e Requisitos

* Desenvolvido para **Python 3.8.10** (compatível com 3.7+).
* Sem dependências externas, usa apenas bibliotecas padrão.
* Executado via linha de comando.

---

## 3 Extras

### 3.1 Licença

Projeto com licença **MIT**, livre para uso, modificação e distribuição, desde que mantida a atribuição.

### 3.2 Referências

* [Teorema de Church–Turing - Wikipedia](https://en.wikipedia.org/wiki/Church%E2%80%93Turing_thesis)
* Textos introdutórios em teoria da computação.

### 3.3 Testes e Validações

Testes simples confirmam que os valores seguem a tendência esperada, garantindo a coerência da estimativa feita pelo script.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **N**: número natural (0,1,2,...) usado para definir o tamanho do espaço computacional.

* **2^N**: potência de 2, ou seja, 2 multiplicado por ele mesmo N vezes.

* **Processos computáveis**: programas ou funções que podem ser executados por uma máquina de Turing.

* **Estimativa**: valor aproximado da quantidade de processos válidos, que não é o total de combinações possíveis, mas uma fração realista.

* **Máquina de Turing**: modelo matemático que representa um computador idealizado, capaz de executar qualquer algoritmo definido.
