# ♾️ - Teorema de Cantor–Bernstein  
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![LGN](https://img.shields.io/badge/Teorema-Cantor–Bernstein-ff69b4.svg)](https://en.wikipedia.org/wiki/Cantor–Bernstein_theorem)

## Frase do Teorema

> *Se dois conjuntos têm funções injetoras entre si, então existe uma correspondência exata entre seus elementos.* – Ou seja, mesmo sem contar um por um, podemos dizer que dois conjuntos têm o **mesmo tamanho**, mesmo sendo infinitos.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `cantor_bernstein_interval.py`](#2-script-cantor_bernstein_intervalpy)  
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
O **Teorema de Cantor–Bernstein** diz que se há uma **função injetora** (ou seja, que não repete valores) de um conjunto A em outro B e vice-versa, então existe uma **função bijetora** entre eles – uma correspondência perfeita, um-para-um.

Isso nos permite dizer que **os dois conjuntos têm o mesmo "tamanho"**, mesmo que sejam infinitos.

### 1.2 Exemplos Práticos  

- Conjunto dos números naturais (1, 2, 3, ...)  
- Conjunto dos números pares (2, 4, 6, ...)

Mesmo parecendo que os pares são "menos", existe uma correspondência perfeita: basta multiplicar por 2. Isso prova que eles têm a mesma **quantidade infinita** de elementos.

### 1.3 Explicação Detalhada  

Este projeto aplica esse teorema em intervalos exponenciais como:

```

\[2^N, 2^(N+1) - 1]

````

Em vez de contar um por um, usamos **médias** (geométrica e aritmética) como **estimativas da quantidade de elementos**.

### 1.4 Aplicações  

- Análise de crescimento de dados  
- Compressão binária  
- Estudo de codificações  
- Teoria dos conjuntos e cardinalidades  
- Criptografia e segurança digital

### 1.5 Análise da Tabela  

| N | Início (2^N) | GeoMédia | AritMédia | Fim (2^(N+1)-1) |
|---|--------------|----------|-----------|------------------|
| 0 | 1            | 1        | 1         | 1                |
| 1 | 2            | 2        | 2         | 3                |
| 2 | 4            | 5        | 5         | 7                |
| 3 | 8            | 10       | 11        | 15               |
| 4 | 16           | 22       | 23        | 31               |
| 5 | 32           | 44       | 47        | 63               |
| 6 | 64           | 90       | 95        | 127              |
| 7 | 128          | 180      | 191       | 255              |
| 8 | 256          | 361      | 383       | 511              |
| 9 | 512          | 723      | 767       | 1023             |

---

## 2. Script `cantor_bernstein_interval.py`

### 2.1 Relação com o Teorema  
Usamos o **Teorema de Cantor–Bernstein** como base teórica para estimar a quantidade de elementos dentro de um intervalo binário **sem contar todos eles**.

### 2.2 Objetivo do Script  
- Criar uma tabela de intervalos exponenciais  
- Calcular a média geométrica e aritmética entre os extremos  
- Usar essas médias como estimativas de cardinalidade  
- Mostrar como esse método reflete a lógica do teorema

### 2.3 Exemplo de Saída  

```text
N = 5
Intervalo: [32, 63]
Média geométrica: 44.00
Média aritmética: 47.00
````

### 2.4 Funcionamento Interno

1. Define um intervalo com base em `2^N`
2. Calcula:

   * Início: `2^N`
   * Fim: `2^(N+1) - 1`
   * Média geométrica: `sqrt(2^N * (2^(N+1) - 1))`
   * Média aritmética: `(2^N + (2^(N+1) - 1)) / 2`
3. Gera uma tabela com os resultados para vários valores de N

### 2.5 Tecnologias e Requisitos

**Linguagem:** Python 3.8.10
**Bibliotecas utilizadas:** Nenhuma externa

**Execução:**

```bash
python cantor_bernstein_interval.py
```

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a **MIT License**.

### 3.2 Referências

* [Wikipedia: Cantor–Bernstein Theorem](https://en.wikipedia.org/wiki/Cantor%E2%80%93Bernstein_theorem)
* Estudo de cardinalidade e teoria dos conjuntos
* Matemática discreta e funções bijetoras

### 3.3 Testes e Validações

* Todos os cálculos foram testados para múltiplos valores de N
* Resultados conferem com cálculos teóricos
* O script é simples e não depende de bibliotecas externas

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Injeção:** Função que nunca repete o mesmo valor de saída para dois valores diferentes de entrada.

**Bijetora:** Função que é injetora *e* cobre todos os valores do conjunto destino.

**Cardinalidade:** É o número de elementos de um conjunto, mesmo que ele seja infinito.

**Média geométrica:** Usada quando os valores crescem exponencialmente. Ela dá uma ideia mais justa de "centro" nesse tipo de crescimento.

**Média aritmética:** Soma dos extremos dividida por 2.

**Bijeção teórica:** Garantia de que é possível criar uma correspondência perfeita entre conjuntos, mesmo sem construir a função na prática.
