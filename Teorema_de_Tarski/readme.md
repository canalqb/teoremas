# 📐 - Teorema Tarski-Exponencial  
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)

## 🧾 Frase do Teorema

> *"A verdade de uma linguagem formal suficientemente expressiva não é definível dentro dela mesma, e os valores esperados em suas interpretações numéricas crescem de forma controlada entre potências de 2."* – Este teorema delimita a capacidade de definição da verdade e estabelece limites para o crescimento lógico e numérico de propriedades dentro de sistemas formais.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `tarski_approximation.py`](#2-script-tarski_approximationpy)
  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3. Extras](#3-extras)
  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referencias)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4 Contato](#4-contato)
* [5. Nota](#5-nota)

---

## 1. Introdução ao Teorema

### 1.1 Resumo

O **Teorema Tarski-Exponencial** é uma aplicação computacional inspirada no Teorema de Tarski original. Ele se propõe a modelar o crescimento controlado de valores esperados dentro de **intervalos exponenciais**, partindo da ideia de que qualquer valor "verdadeiro" deve estar contido entre 2 elevado a N e 2 elevado a (N+1) menos 1, respeitando os limites lógicos da linguagem formal onde foi definido.

---

### 1.2 Exemplos Práticos

| N | Início (2^N) | Esperado (aproximado) | Fim (2^(N+1) - 1) |
|---|--------------|----------------------|-------------------|
| 0 | 1            | 1                    | 1                 |
| 1 | 2            | 3                    | 3                 |
| 2 | 4            | 6                    | 7                 |
| 3 | 8            | 12                   | 15                |
| 4 | 16           | 25                   | 31                |
| 5 | 32           | 44                   | 63                |

Esses valores mostram que para cada nível N, o valor calculado cresce, mas sempre respeitando os limites do intervalo definido pelo teorema.

---

### 1.3 Explicação Detalhada

A origem deste teorema está na lógica formal. O **Teorema de Tarski** demonstra que uma linguagem formal robusta (como a aritmética de Peano) **não pode conter uma definição interna da sua própria verdade**.

Aplicando isso a modelos numéricos, os valores que representam verdades, propriedades ou interpretações **crescem com a complexidade**, mas dentro de **intervalos previsíveis**, e não de forma arbitrária.

Ou seja, **a verdade não pode ser definida dentro do próprio sistema, mas também cresce de forma controlada e dentro de limites claros**.

---

### 1.4 Aplicações

Este teorema (e sua adaptação numérica) é utilizado em áreas como:

- **Lógica formal e teoria dos modelos**  
- **Criptografia** — crescimento exponencial como base da segurança  
- **Complexidade computacional** — limites de expressividade e crescimento  
- **Teoria da computação** — análise de máquinas de Turing e limites de prova  
- **Fundamentação matemática** — consistência e completude de sistemas formais

---

### 1.5 Análise da Tabela

A tabela apresentada define para cada N:

- O **início** do intervalo (2^N)  
- O **fim** do intervalo (2^(N+1) - 1)  
- Um valor "esperado" ou calculado, que respeita os limites  

Esta análise mostra que os valores **não crescem de forma linear**, mas também **não ultrapassam o limite superior**, criando uma **função de crescimento exponencial controlado**, exatamente como propõe o Teorema Tarski-Exponencial.

---

## 2. Script `tarski_approximation.py`

---

### 2.1 Relação com o Teorema

O script representa na prática a ideia central do Teorema Tarski-Exponencial: **valores que crescem respeitando intervalos definidos por potências de 2**.

Ele não usa o valor "esperado" da tabela como entrada, mas o deduz com base apenas nos limites do intervalo (início e fim).

---

### 2.2 Objetivo do Script

O script tem como objetivo:

- Gerar uma **aproximação realista** de um valor esperado para cada N  
- Demonstrar crescimento ordenado dentro de intervalos exponenciais  
- Produzir uma tabela clara para análise prática e teórica  

---

### 2.3 Exemplo de Saída

```text
N   | Início (2^N)  | Aproximação  | Fim (2^(N+1)-1)
----------------------------------------------------
0   | 1             | 1            | 1
1   | 2             | 3            | 3
2   | 4             | 6            | 7
3   | 8             | 12           | 15
4   | 16            | 25           | 31
5   | 32            | 44           | 63
6   | 64            | 86           | 127
7   | 128           | 168          | 255
8   | 256           | 321          | 511
9   | 512           | 612          | 1023
````

---

### 2.4 Funcionamento Interno

O script funciona assim:

1. Itera sobre valores de N, de 0 até 9.
2. Para cada N:

   * Calcula o início do intervalo: 2 elevado a N
   * Calcula o fim do intervalo: 2 elevado a (N+1) menos 1
   * Aplica uma fórmula de média ponderada para gerar uma aproximação realista dentro do intervalo
3. Imprime uma tabela com os resultados completos.

---

### 2.5 Tecnologias e Requisitos

* **Linguagem:** Python 3.8.10
* **Bibliotecas externas:** Nenhuma
* **Execução:** Via terminal ou script local
* **Compatibilidade:** Windows, Linux, macOS

---

## 3. Extras

---

### 3.1 Licença

Este projeto é distribuído sob a **Licença MIT** — uso livre para fins acadêmicos, educacionais e de pesquisa.

---

### 3.2 Referências

* Alfred Tarski, *The Semantic Conception of Truth*, 1944
* Stanford Encyclopedia of Philosophy – Tarski's Truth Definitions
* Introdução à Teoria dos Modelos – Wilfrid Hodges
* Problemas de crescimento em algoritmos – Cormen et al.

---

### 3.3 Testes e Validações

Os resultados foram validados para garantir que:

* Nenhum valor ultrapasse os limites definidos
* Os valores crescem com N
* A função de aproximação é **monótona crescente**

---

## 4. 📬 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **Linguagem formal:** sistema matemático rigoroso com regras bem definidas para formar sentenças e provas
* **Valor esperado:** uma média ponderada ou previsão do valor que esperamos obter, baseada em dados ou teoria
* **Potência de 2:** resultado de multiplicar o número 2 por ele mesmo várias vezes (ex: 2^3 = 2 x 2 x 2 = 8)
* **Monótona crescente:** função ou sequência que nunca diminui, só pode aumentar ou manter o mesmo valor
* **Média ponderada:** média onde alguns valores têm mais importância que outros, usada para dar mais peso a certos dados
