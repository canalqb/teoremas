# 📈 - Teorema de Mostowski e Crescimento Recursivo

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Teoria%20dos%20Modelos-ff69b4.svg)](https://en.wikipedia.org/wiki/Mostowski_collapse_theorem)

## Frase do Teorema

> O crescimento de estruturas recursivas que se duplicam a cada passo segue uma regra simples: o valor no próximo nível é o dobro do anterior mais um – isso ajuda a prever o tamanho dessas estruturas em processos recursivos.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `mostowski_growth_table.py`](#2-script-mostowski_growth_tablepy)

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

O **Teorema de Mostowski** é um conceito da lógica matemática que trata da construção e crescimento de estruturas recursivas, como árvores que se duplicam a cada nível. Ele nos ajuda a entender como o tamanho dessas estruturas cresce com o tempo.

### 1.2 Exemplos Práticos

Imagine uma árvore binária, onde cada nó gera dois novos nós no próximo nível, e assim por diante. A quantidade total de nós cresce rápido, seguindo a regra:
valor no próximo nível = 2 vezes o valor atual + 1.

### 1.3 Explicação Detalhada

Essa regra simples significa que, para cada novo nível da estrutura, dobramos o tamanho do nível anterior e adicionamos um novo elemento para a camada atual. Isso gera um crescimento exponencial e acumulativo.

### 1.4 Aplicações

* **Lógica matemática** e estudo de modelos formais.
* **Análise de algoritmos recursivos** que criam estruturas em árvore.
* **Estruturas de dados**, como árvores binárias e suas variantes.
* **Pesquisa em computabilidade e complexidade**, onde entender o crescimento é crucial.

### 1.5 Análise da Tabela

A tabela abaixo mostra o crescimento esperado de acordo com o teorema, comparado com os limites teóricos:

| N | Início (2^N) | Valor esperado pelo teorema | Fim (2^(N+1)) - 1 |
| - | ------------ | --------------------------- | ----------------- |
| 0 | 1            | 1                           | 1                 |
| 1 | 2            | 3                           | 3                 |
| 2 | 4            | 7                           | 7                 |
| 3 | 8            | 15                          | 15                |
| 4 | 16           | 31                          | 31                |
| 5 | 32           | 63                          | 63                |
| 6 | 64           | 127                         | 127               |
| 7 | 128          | 255                         | 255               |
| 8 | 256          | 511                         | 511               |
| 9 | 512          | 1023                        | 1023              |

---

## 2. Script `mostowski_growth_table.py`

### 2.1 Relação com o Teorema

O script exemplifica a aplicação prática do teorema ao calcular e mostrar a progressão dos valores segundo a regra recursiva M(n+1) = 2 × M(n) + 1.

### 2.2 Objetivo do Script

* Gerar uma tabela que ilustre o crescimento dos valores baseados no teorema.
* Mostrar a base do crescimento (2^N), o valor esperado pela regra e o limite máximo natural.
* Facilitar o entendimento visual e numérico do crescimento recursivo.

### 2.3 Exemplo de Saída

```
N   | Inicio (2^N)     | Esperado pelo teorema      | Fim (2^(N+1)) - 1
----------------------------------------------------------------------
0   | 1                | 1                          | 1
1   | 2                | 3                          | 3
2   | 4                | 7                          | 7
3   | 8                | 15                         | 15
4   | 16               | 31                         | 31
5   | 32               | 63                         | 63
6   | 64               | 127                        | 127
7   | 128              | 255                        | 255
8   | 256              | 511                        | 511
9   | 512              | 1023                       | 1023
```

### 2.4 Funcionamento Interno

* Inicializa o valor base M(0) = 1.
* Para cada próximo nível N, calcula M(N+1) como 2 vezes M(N) mais 1.
* Calcula os valores 2^N (início) e 2^(N+1) - 1 (fim) para comparação.
* Imprime todos os valores formatados em tabela.

### 2.5 Tecnologias e Requisitos

* Desenvolvido em **Python 3.8.10**.
* Sem dependências externas, usa apenas bibliotecas padrão.

---

## 3 Extras

### 3.1 Licença

Este projeto está sob a **licença MIT**, permitindo uso, cópia, modificação e distribuição livre.

### 3.2 Referências

* [Mostowski Collapse Theorem - Wikipedia](https://en.wikipedia.org/wiki/Mostowski_collapse_theorem)
* Lógica matemática e teoria dos modelos.

### 3.3 Testes e Validações

Para testar, compare os valores gerados para pequenos N com cálculos manuais da fórmula recursiva, garantindo que:
M(n+1) = 2 × M(n) + 1.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **Estrutura recursiva:** algo que se constrói repetidamente, usando a si mesmo como base.
* **Nível (N):** etapa ou camada na construção da estrutura.
* **Valor esperado:** resultado previsto pela regra matemática.
* **2^N:** significa "2 elevado à potência N", ou seja, 2 multiplicado por ele mesmo N vezes.
* **Fim (2^(N+1) - 1):** o valor máximo ou limite da estrutura naquele nível.
