# 📚 Teorema da Incompletude de Gödel
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Frase do Teorema

> **"Em qualquer sistema formal consistente que seja suficientemente poderoso para expressar a aritmética básica, existem proposições verdadeiras que não podem ser provadas dentro desse sistema."**

Este teorema descreve a limitação fundamental de sistemas formais que tentam representar toda a matemática. Isso implica que nem todas as verdades podem ser formalmente provadas, o que desafia a ideia de que todos os problemas podem ser resolvidos por um conjunto fixo de regras.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `teorema_incompletude_godel.py`](#2-script-teorema_incompletude_godelpy)

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

## 1. Introdução ao Teorema

### 1.1 Resumo

O **Teorema de Incompletude de Gödel** tem dois aspectos principais que definem suas implicações:

- **Primeiro Teorema da Incompletude**: afirma que em sistemas formais suficientemente poderosos (como a aritmética), existem proposições que são verdadeiras, mas não podem ser provadas dentro do sistema.
  
- **Segundo Teorema da Incompletude**: afirma que a consistência de um sistema formal não pode ser provada dentro do próprio sistema.

### 1.2 Exemplos Práticos

Imagine que estamos tentando resolver todos os problemas matemáticos dentro de um sistema formal. O teorema nos diz que, por mais que tentemos, sempre haverá algumas questões que não podemos resolver dentro desse sistema, mesmo que saibamos que a resposta está correta.

### 1.3 Explicação Detalhada

Os dois teoremas demonstram que não existe um único sistema formal capaz de resolver todas as questões matemáticas, uma vez que sempre existirão proposições que são verdadeiras mas indecidíveis dentro do próprio sistema.

### 1.4 Aplicações

Esses teoremas têm implicações profundas em campos como a lógica matemática, ciência da computação e filosofia, porque sugerem que não podemos sempre confiar na totalidade de um sistema para resolver qualquer tipo de problema.

### 1.5 Análise da Tabela

A tabela abaixo mostra como os valores gerados de acordo com o teorema se comportam. Cada linha representa o valor de N, o intervalo gerado e o valor esperado (que está dentro do intervalo definido entre **Início (2^N)** e **Fim (2^(N+1)-1)**).

| N  | Início (2^N) | Esperado pelo Teorema | Fim (2^(N+1)) - 1 |
|----|--------------|-----------------------|-------------------|
| 0  | 1            | 1                     | 1                 |
| 1  | 2            | 2                     | 3                 |
| 2  | 4            | 6                     | 7                 |
| 3  | 8            | 13                    | 15                |
| 4  | 16           | 16                    | 31                |
| 5  | 32           | 61                    | 63                |
| 6  | 64           | 119                   | 127               |
| 7  | 128          | 223                   | 255               |
| 8  | 256          | 445                   | 511               |
| 9  | 512          | 520                   | 1023              |

## 2. Script `teorema_incompletude_godel.py`

### 2.1 Relação com o Teorema

Este script é baseado na ideia de que existe um intervalo para cada valor de N, e dentro desse intervalo geramos um valor aleatório que está em conformidade com o teorema. A ideia é ilustrar como os valores gerados podem se encaixar dentro desses limites.

### 2.2 Objetivo do Script

O objetivo do script é gerar valores dentro dos intervalos definidos por 2^N e 2^(N+1)-1 para cada valor de N, e apresentar uma tabela com esses valores.

### 2.3 Exemplo de Saída

Quando o script for executado, ele gerará uma tabela parecida com a seguinte:

```

Tabela de Valores Gerados:
N  Início (2^N)      Esperado pelo Teorema        Fim (2^(N+1))-1
0  1                  1                            1
1  2                  2                            3
2  4                  6                            7
3  8                  13                           15
4  16                 16                           31
5  32                 61                           63
6  64                 119                          127
7  128                223                          255
8  256                445                          511
9  512                520                          1023

```

### 2.4 Funcionamento Interno

O script gera aleatoriamente um número dentro dos intervalos definidos para cada valor de N, garantindo que o número gerado esteja sempre dentro do intervalo [2^N, 2^(N+1)-1]. Ele utiliza a função `random.randint()` para gerar esses números aleatórios.

### 2.5 Tecnologias e Requisitos

- **Python 3.8.10**
- Biblioteca `random` (embutida no Python)

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### 3.2 Referências

- Gödel, Kurt. "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I". *Monatshefte für Mathematik und Physik*, 1931.
- [Wikipedia: Teorema de Gödel](https://pt.wikipedia.org/wiki/Teorema_da_incompletude_de_G%C3%B6del)

### 3.3 Testes e Validações

- O script foi testado para garantir que os valores gerados estão dentro dos intervalos especificados.

## 4 Contato

- Feito por CanalQb no GitHub
- Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com](https://canalqb.blogspot.com)
- 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
- PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

## 5. Nota

{**Termos técnicos**}:   
- **Sistema formal**: um conjunto de regras e axiomas usados para derivar teoremas matemáticos.
- **Proposição indecidível**: uma afirmação que não pode ser provada nem refutada dentro de um sistema formal.
- **Aritmética**: o ramo da matemática que lida com números e operações básicas, como adição, subtração, multiplicação e divisão.
