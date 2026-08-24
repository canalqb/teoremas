# 🧩 - Da Recursao De Kleene
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![LGN](https://img.shields.io/badge/Teorema-Kleene-ff69b4.svg)](https://en.wikipedia.org/wiki/Kleene%27s_recursion_theorem)

## Frase do Teorema

> *Para toda função computável, existe um programa que se comporta igual ao programa gerado por ela.* – Em linguagem simples: é possível criar um programa que "fala sobre si mesmo", ou seja, que acessa ou usa seu próprio código.  

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `kleene_count_simulation.py`](#2-script-kleene_count_simulationpy)  
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
O **Teorema da Recursão de Kleene** garante que para qualquer função computável, é possível encontrar um programa que gera a si mesmo — ou seja, um programa autorreferente.  

### 1.2 Exemplos Práticos  
- Um programa que imprime o seu próprio código (conhecido como *quine*)  
- Sistemas de compiladores que recompilam a si mesmos  
- Programas maliciosos (vírus) que se replicam com conhecimento do próprio código  

### 1.3 Explicação Detalhada  
Esse teorema mostra que é **matematicamente possível** criar programas que fazem referência ao seu próprio funcionamento. Isso é importante porque mostra limites e possibilidades da computação em nível fundamental.

### 1.4 Aplicações  
- **Metaprogramação**  
- **Teoria da computação**  
- **Compiladores**  
- **Sistemas reflexivos e autônomos**  
- **Segurança da informação** (ex: vírus e worms)  

### 1.5 Análise da Tabela  
O script simula quantos "programas" podem ser considerados autorreferentes em blocos de números. Isso **ajuda a visualizar** a tendência do crescimento dessa quantidade conforme aumentamos o espaço de busca.

---

## 2. Script `kleene_count_simulation.py`

### 2.1 Relação com o Teorema  
O script se inspira no Teorema da Recursão de Kleene para estimar, **de forma computável**, quantos índices (números que simbolizam programas) satisfazem uma **condição de autorreferência**.

### 2.2 Objetivo do Script  
Simular, para cada valor de `N`, quantos programas entre `2^N` e `2^(N+1) - 1` podem ser considerados autorreferentes, segundo uma **heurística computável**.

### 2.3 Exemplo de Saída

```text
| N | Início | Fim  | Estimativa de Pontos Fixos |
|---|--------|------|-----------------------------|
| 0 | 1      | 2    | 1                           |
| 1 | 2      | 4    | 1                           |
| 2 | 4      | 8    | 2                           |
| 3 | 8      | 16   | 2                           |
| 4 | 16     | 32   | 4                           |
| 5 | 32     | 64   | 7                           |
| 6 | 64     | 128  | 12                          |
| 7 | 128    | 256  | 18                          |
| 8 | 256    | 512  | 34                          |
| 9 | 512    | 1024 | 57                          |
````

### 2.4 Funcionamento Interno

* Para cada `N`, o script define o intervalo `[2^N, 2^(N+1) - 1]`
* Para cada número `i` nesse intervalo:

  * Converte para binário
  * Mede o tamanho do binário
  * Se `i % tamanho == 0`, considera o número como **simulando ponto fixo**
* Conta e imprime o total para cada `N`

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10**
* Nenhuma biblioteca externa
* Código puro, simples e comentado
* Executável com:

```bash
python kleene_count_simulation.py
```

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a **Licença MIT**.

### 3.2 Referências

* [Wikipedia - Teorema de Kleene](https://en.wikipedia.org/wiki/Kleene%27s_recursion_theorem)
* Materiais de teoria da computação
* Discussões sobre autorreferência computacional

### 3.3 Testes e Validações

O script foi testado para `N = 0` até `N = 9`. A tendência de crescimento foi validada manualmente e visualmente por inspeção da tabela.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Recursão de Kleene:** Teorema que afirma que é possível criar um programa que replica o comportamento de outro criado a partir de si mesmo.

**Ponto fixo:** Um valor que, quando aplicado em uma função, retorna ele mesmo. Ex: f(x) = x.

**Heurística:** Regra prática usada para simular algo complexo de forma simplificada.

**Autorreferência:** Quando algo (como um programa) faz referência a si próprio.

**Estimativa:** Uma aproximação ou valor calculado com base em critérios simples.

**Programa:** Aqui representado por números inteiros naturais, como se cada número fosse o "índice" de um programa possível.
