# 📚 - Teorema de Crescimento Zorniano

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)

## Frase do Teorema

> "Em intervalos que crescem por potências de dois, podemos estimar um valor esperado intermediário que cresce acumulativamente, respeitando os limites do intervalo." – isso significa que o crescimento dos valores não é nem apenas o mínimo nem o máximo, mas um valor “esperado” que fica no meio e cresce conforme definimos.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `teoremazorn.py`](#2-script-teoremazornpy)

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

O **Teorema de Crescimento Zorniano** trata de entender o crescimento de valores dentro de intervalos que crescem com potências de 2, usando uma lógica inspirada no **Teorema de Zorn**, que fala sobre existência de máximos em conjuntos parcialmente ordenados. Aqui, aplicamos essa ideia para encontrar um valor esperado dentro desses intervalos.

### 1.2 Exemplos Práticos

Imagine que temos uma sequência de números que sempre ficam entre um valor inicial (2 elevado a N) e um valor final (2 elevado a N+1 menos 1). O teorema nos ajuda a estimar onde, dentro desse intervalo, um valor “esperado” vai aparecer — nem no começo, nem no fim, mas em algum ponto do meio.

### 1.3 Explicação Detalhada

O Teorema de Zorn, na matemática, garante que em certas situações existe um elemento que não pode ser ultrapassado (um maximal). Traduzindo para números: em cada intervalo \[2^N, 2^(N+1) - 1], procuramos um valor esperado que cresce de forma acumulativa.
Essa expectativa não é simplesmente o limite inferior ou superior, mas um valor que reflete um crescimento “controlado” dentro dos limites.

### 1.4 Aplicações

* Teoria dos conjuntos e lógica matemática
* Análise de algoritmos que precisam garantir máximos ou limites internos
* Modelagem de crescimento em estruturas discretas (árvores, grafos)
* Combinatória e estudos sobre cardinalidades

### 1.5 Análise da Tabela

| N   | Início (2^N) | Esperado | Fim (2^(N+1) - 1) |
| --- | ------------ | -------- | ----------------- |
| 0   | 1            | 1        | 1                 |
| 1   | 2            | 3        | 3                 |
| 2   | 4            | 7        | 7                 |
| 3   | 8            | 8        | 15                |
| 4   | 16           | 21       | 31                |
| ... | ...          | ...      | ...               |

Observe que o valor esperado não é um extremo, mas um número entre o começo e o fim do intervalo que cresce de forma acumulativa.

---

## 2. Script `teoremazorn.py`

### 2.1 Relação com o Teorema

O script implementa a lógica de estimar valores “esperados” dentro dos intervalos definidos pelo teorema, simulando o crescimento descrito pelo Teorema de Crescimento Zorniano.

### 2.2 Objetivo do Script

Calcular e imprimir valores estimados que respeitam os limites dos intervalos \[2^N, 2^(N+1) - 1], simulando o comportamento esperado pelo teorema.

### 2.3 Exemplo de Saída

```
N=0: Início=1, Estimado=1.0, Fim=1
N=1: Início=2, Estimado=3.0, Fim=3
N=2: Início=4, Estimado=7.0, Fim=7
N=3: Início=8, Estimado=12.8, Fim=15
N=4: Início=16, Estimado=21.0, Fim=31
...
```

### 2.4 Funcionamento Interno

* Para cada N, define o intervalo \[2^N, 2^(N+1) - 1].
* Calcula o tamanho do intervalo.
* Estima o valor esperado somando ao valor anterior uma fração (alpha) do tamanho do intervalo.
* Repete o processo acumulando o crescimento.

### 2.5 Tecnologias e Requisitos

* Python 3.8.10 (recomendado)
* Nenhuma biblioteca externa necessária

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).

### 3.2 Referências

* Teorema de Zorn: [https://en.wikipedia.org/wiki/Zorn%27s\_lemma](https://en.wikipedia.org/wiki/Zorn%27s_lemma)
* Teoria dos conjuntos e ordens parciais
* Estimativas de crescimento em sequências matemáticas

### 3.3 Testes e Validações

O script inclui validações básicas e pode ser facilmente extendido para testar outros valores de alpha e intervalos maiores.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Potência de 2**: número obtido multiplicando 2 por ele mesmo várias vezes. Exemplo: 2 elevado a 3 é 2 x 2 x 2 = 8.

**Valor esperado**: aqui, significa um número estimado que representa o crescimento médio dentro do intervalo.

**Teorema de Zorn**: princípio matemático que garante que em certas estruturas existe um elemento máximo que não pode ser ultrapassado.

**Intervalo \[a, b]**: conjunto de números entre a e b, incluindo a e b.

**Alpha (α)**: fração usada para ajustar o crescimento estimado no script, pode ser entendida como “percentual de avanço” dentro do intervalo.
