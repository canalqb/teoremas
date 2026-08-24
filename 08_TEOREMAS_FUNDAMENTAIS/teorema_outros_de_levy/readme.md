# 🧩 - De Levy

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Levy-ff69b4.svg)](https://en.wikipedia.org/wiki/L%C3%A9vy_continuity_theorem)

## Frase do Teorema

> A convergência das funções características implica na convergência das distribuições – ou seja, podemos entender o comportamento limite de sequências complexas de variáveis aleatórias olhando para suas funções características.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `Teorema_de_Levy.py`](#2-script-teorema_de_levypy)

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

O **Teorema de Lévy** é um princípio importante da **probabilidade** que fala sobre como sequências de variáveis aleatórias se comportam quando vão “se aproximando” de uma variável limite. Ele usa a chamada *função característica*, que é uma forma de “representar” uma variável aleatória de modo a facilitar o estudo de suas propriedades.

### 1.2 Exemplos Práticos

Imagine que você joga uma moeda muitas vezes e quer entender a distribuição dos resultados conforme o número de jogadas cresce. O teorema ajuda a saber se essa sequência de distribuições vai convergir para algo que conhecemos, como a distribuição normal.

### 1.3 Explicação Detalhada

A função característica é como um código que contém todas as informações de uma variável aleatória, similar a uma “assinatura”. O teorema diz que, se essa assinatura de uma sequência de variáveis converge para a assinatura de outra variável, então as distribuições delas também convergem — ou seja, a sequência “se aproxima” da distribuição limite.

### 1.4 Aplicações

* **Estatística:** base para o Teorema Central do Limite.
* **Engenharia:** análise de ruído e sinais aleatórios.
* **Ciência de Dados:** modelagem e inferência probabilística.
* **Matemática Pura:** estudo de distribuições e limites.

### 1.5 Análise da Tabela

O script mostra uma tabela com potências de 2, números de Mersenne (2^n - 1), e uma coluna intermediária aproximada usando uma função cúbica. Essa tabela simboliza a ideia do teorema: uma sequência (coluna do meio) que converge ou se aproxima de outras duas (potências de 2 e Mersenne).

---

## 2. Script `Teorema_de_Levy.py`

### 2.1 Relação com o Teorema

O script inspira-se no conceito de convergência e funções características para criar uma aproximação numérica que liga potências de 2 e números de Mersenne por meio de uma sequência intermediária estimada.

### 2.2 Objetivo do Script

Calcular e comparar três colunas:

* Potências de 2 para valores de n (2^n).
* Números de Mersenne (2^n - 1).
* Uma sequência intermediária estimada por uma fórmula cúbica de n.

### 2.3 Exemplo de Saída

```
n | 2^n  | Estimado | 2^n - 1  
--------------------------------
1 | 2    | 1        | 1       
2 | 4    | 3        | 3       
3 | 8    | 7        | 7       
... (e assim por diante)
```

A saída mostra a aproximação e ajuda a visualizar onde o modelo é exato ou necessita ajustes.

### 2.4 Funcionamento Interno

* Calcula as potências e números de Mersenne para n variando.
* Usa uma fórmula cúbica para estimar o valor intermediário.
* Compara os valores, imprimindo resultados e erros.

### 2.5 Tecnologias e Requisitos

* Python 3.8.10
* Nenhuma biblioteca externa necessária (padrão Python).

---

## 3. Extras

### 3.1 Licença

Este projeto está sob a licença **MIT**, permitindo uso livre, cópia e modificação.

### 3.2 Referências

* Wikipédia: [Teorema de Lévy](https://en.wikipedia.org/wiki/L%C3%A9vy_continuity_theorem)
* Apostilas de Probabilidade e Estatística Básica.
* CanalQb – Blog e projetos relacionados.

### 3.3 Testes e Validações

O script imprime uma tabela para validação visual e pode ser adaptado para incluir testes automáticos de comparação entre valores estimados e reais.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **Função característica**: É uma função especial que ajuda a “descrever” completamente uma variável aleatória, como se fosse uma assinatura digital dela.
* **Variável aleatória**: Um valor que pode mudar, geralmente resultado de um experimento com elementos de incerteza (ex: jogar dado).
* **Convergência em distribuição**: Quando a sequência de variáveis aleatórias “se aproxima” em comportamento de uma variável limite, em termos de probabilidade.
* **Potências de 2 (2^n)**: Significa multiplicar 2 por ele mesmo n vezes, por exemplo, 2^3 = 2×2×2 = 8.
* **Número de Mersenne**: É um número que é sempre 1 a menos que uma potência de 2, por exemplo, 7 = 2^3 - 1.
