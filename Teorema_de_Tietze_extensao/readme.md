# 🔢 - Teorema da Extensão Numérica por Potências de 2
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Extensao%20por%20Potencias%20de%202-ff69b4.svg)](https://pt.wikipedia.org/wiki/Pot%C3%AAncia_de_dois)

## Frase do Teorema

> Um processo recursivo de extensão baseado em potências de 2 pode gerar uma sequência que cresce progressivamente, permanecendo dentro de limites definidos por 2^N e 2^(N+1)-1.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `tietze_extension_simulator.py`](#2-script-tietze_extension_simulatorpy)  
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

Este projeto apresenta uma estrutura numérica baseada em potências de 2, que permite simular uma expansão sequencial com crescimento previsível. A ideia central é usar limites bem definidos para garantir que o crescimento esteja sempre dentro de um intervalo seguro.

### 1.2 Exemplos Práticos

Considere um processo que parte de 1, depois 3, 5, 10, 18... e assim por diante. Cada valor pertence a um intervalo entre duas potências consecutivas de 2. Isso permite simular crescimentos controlados e escaláveis.

### 1.3 Explicação Detalhada

Para cada valor de N, usamos:
- Início: 2^N
- Fim: 2^(N+1) - 1

Com isso, é possível garantir que qualquer valor gerado esteja dentro desses limites. O valor seguinte é sempre um acréscimo em relação ao anterior, com base em uma fração ou função do próprio N.

### 1.4 Aplicações

Esse tipo de estrutura pode ser útil em:
- Algoritmos de compressão
- Distribuição de dados binários
- Geração de IDs em sistemas hierárquicos
- Simulações com árvore binária ou grafos binários

### 1.5 Análise da Tabela

| N  | Início (2^N) | Fim (2^(N+1)-1) | Gerado (estimado) |
|----|--------------|------------------|--------------------|
| 0  | 1            | 1                | 1                  |
| 1  | 2            | 3                | 3                  |
| 2  | 4            | 7                | 5                  |
| 3  | 8            | 15               | 10                 |
| 4  | 16           | 31               | 18                 |
| 5  | 32           | 63               | 35                 |
| 6  | 64           | 127              | 67                 |
| 7  | 128          | 255              | 132                |
| 8  | 256          | 511              | 260                |
| 9  | 512          | 1023             | 517                |

---

## 2. Script `tietze_extension_simulator.py`

### 2.1 Relação com o Teorema

Este script é uma simulação da ideia de extensão numérica entre potências de dois. Ele demonstra como gerar uma sequência crescente sem ultrapassar os limites definidos para cada N.

### 2.2 Objetivo do Script

- Gerar valores estimados entre os intervalos [2^N, 2^(N+1)-1]
- Não utilizar a coluna "esperado" diretamente
- Aproximar os resultados de uma forma consistente e previsível

### 2.3 Exemplo de Saída

```plaintext
N   | Início (2^N)    | Fim (2^(N+1)-1)    | Gerado (estimado)
-----------------------------------------------------------------
0   | 1               | 1                  | 1
1   | 2               | 3                  | 3
2   | 4               | 7                  | 5
3   | 8               | 15                 | 10
4   | 16              | 31                 | 18
5   | 32              | 63                 | 35
6   | 64              | 127                | 67
7   | 128             | 255                | 132
8   | 256             | 511                | 260
9   | 512             | 1023               | 517
````

### 2.4 Funcionamento Interno

O script utiliza um algoritmo simples:

* Para N=0, inicia em 1
* Para os próximos valores, aplica um incremento baseado em uma fração da potência anterior
* Garante que o novo valor nunca ultrapasse o limite máximo do intervalo

### 2.5 Tecnologias e Requisitos

* **Python**: 3.8.10
* Nenhuma biblioteca externa é necessária

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob os termos da **MIT License**.

### 3.2 Referências

* Potências de dois — [Wikipedia](https://pt.wikipedia.org/wiki/Pot%C3%AAncia_de_dois)
* Estrutura binária em algoritmos
* Sequências numéricas recursivas

### 3.3 Testes e Validações

Testado com:

* Python 3.8.10 no Windows 10
* Execução por terminal: `python tietze_extension_simulator.py`

---

## 4 Contato

* Feito por **CanalQb** no GitHub
* Visite o blog: [canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via **Bitcoin**: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* **PIX**: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **Potência de dois**: número obtido multiplicando 2 por ele mesmo várias vezes (ex: 2, 4, 8, 16, 32...)
* **Sequência recursiva**: quando um termo depende de valores anteriores da sequência
* **Intervalo**: espaço numérico entre dois valores, neste caso entre 2^N e 2^(N+1)-1
* **Binário**: sistema numérico que usa apenas os dígitos 0 e 1, base de funcionamento dos computadores
* **Incremento**: quanto um valor aumenta em relação ao anterior
