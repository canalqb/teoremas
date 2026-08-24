# 🧩 - Numeros De Goldbach Levy
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Goldbach--Levy-ff69b4.svg)](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture)

## Frase do Teorema

> *Todo número ímpar maior que 5 pode ser escrito como a soma de um número primo e dois números primos (iguais ou diferentes).* – Em outras palavras, qualquer número ímpar grande pode ser decomposto de forma curiosa em uma combinação simples de primos. Este script explora essa ideia usando **números de Mersenne**, que são do tipo `2^n - 1`.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `teorema_de_goldbach_levy.py`](#2-script-teorema_de_goldbach_levypy)
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

O **Teorema de Goldbach-Levy** é uma ideia matemática que diz que é possível escrever qualquer número ímpar grande como a soma de **três números primos**. No caso deste projeto, usamos um conjunto especial desses primos: os **números de Mersenne**, que são números da forma `2^n - 1`.

### 1.2 Exemplos Práticos

- O número `21` pode ser escrito como: `15 + 3 + 3`
- O número `1023`: `511 + 255 + 255 + 1 + 1`

Todos os valores utilizados são **números de Mersenne**.

### 1.3 Explicação Detalhada

O script verifica se é possível decompor um número em **somatórios de Mersennes**. Ele percorre números ímpares e verifica, por tentativa e erro (de forma recursiva), se é possível formar o número a partir de somas válidas.

### 1.4 Aplicações

- Exploração de **conjecturas matemáticas**
- Treinamento de lógica para competições e olimpíadas
- Visualização de padrões em conjuntos numéricos especiais

### 1.5 Análise da Tabela

A tabela usada no script contém tuplas no formato `(inicio, meio, fim)`. A decomposição do valor `meio` é feita utilizando números de Mersenne menores ou iguais a `fim`.

---

## 2. Script `teorema_de_goldbach_levy.py`

### 2.1 Relação com o Teorema

O script explora uma **variação prática e computacional** da ideia de Goldbach-Levy, tentando decompor números em somas específicas com números do tipo `2^n - 1`.

### 2.2 Objetivo do Script

- Verificar a decomposição de valores com base em números de Mersenne
- Validar a estrutura de uma tabela de intervalos
- Imprimir decomposições de vários números ímpares até `4095`

### 2.3 Exemplo de Saída

```

Inicio: 16, Meio: 21, Fim: 31
Decomposição de 21 em soma de Mersennes <= 31: \[15, 3, 3]
----------------------------------------------------------

...
1023: \[511, 255, 255, 1, 1]

```

### 2.4 Funcionamento Interno

**Funções principais:**

- `pode_decompor(valor, mersennes)`  
  → Verifica recursivamente se o número pode ser formado por uma soma de Mersennes.

- `validate_table(tabela)`  
  → Confere a validade das tuplas `(inicio, meio, fim)` e exibe a decomposição de `meio`.

- `decompor_intervalo(inicio, fim)`  
  → Aplica a decomposição a todos os números do intervalo.

### 2.5 Tecnologias e Requisitos

- **Python 3.8.10**  
- Sem dependências externas

**Como rodar:**

```bash
python teorema_de_goldbach_levy.py
````

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a Licença MIT. Você pode usar, modificar e distribuir livremente com os devidos créditos.

### 3.2 Referências

* Teorema de Goldbach: [Wikipedia](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture)
* Números de Mersenne: `M(n) = 2^n - 1`
* Python docs: [https://docs.python.org/3/](https://docs.python.org/3/)

### 3.3 Testes e Validações

* Decomposições testadas de `1` até `4095`
* Conferência de todos os `meio` da tabela fornecida
* Verificação da igualdade entre soma e valor esperado

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

📘 **Glossário de termos técnicos usados neste projeto:**

* **Número primo**: número natural maior que 1 que só pode ser dividido por 1 e por ele mesmo.
* **Número de Mersenne**: número da forma `2^n - 1`, onde `n` é inteiro. Alguns desses números são primos e muito importantes em criptografia.
* **Decomposição**: dividir um número em partes (somatórios) que obedecem uma regra.
* **Intervalo**: conjunto de números entre dois valores definidos (`inicio` e `fim`).
* **Recursão**: técnica onde a função chama a si mesma para resolver um problema por partes menores.
