# 🧩 - Pequeno Teorema de Fermat

[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Fermat](https://img.shields.io/badge/Teorema-Pequeno%20de%20Fermat-ff69b4.svg)](https://en.wikipedia.org/wiki/Fermat's_little_theorem)

## Frase do Teorema

> Se um número primo **p** não divide um número **a**, então **a elevado a (p-1) deixa resto 1 quando dividido por p** – ou seja, a^(p-1) mod p = 1.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `pequeno_teorema_de_fermat.py`](#2-script-pequeno_teorema_de_fermatpy)
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

O **Pequeno Teorema de Fermat** diz que, se você escolher um número primo **p** e outro número **a** que não seja múltiplo de **p**, então elevar **a** a **p - 1** e dividir o resultado por **p** sempre dá resto 1.

Se isso **não acontecer**, então o número testado **não é primo**.

### 1.2 Exemplos Práticos

- Para p = 7 e a = 2: 2^6 mod 7 = 64 mod 7 = 1 ✅
- Para n = 49 e a = 2: 2^48 mod 49 = 18 ❌ (não deu 1 → 49 não é primo)

### 1.3 Explicação Detalhada

O teste é usado principalmente para **detectar compostos**. Ele é útil porque, se **a^(n-1) mod n != 1**, então com certeza **n é composto**.

Mas há casos em que um número composto **passa** no teste – são os **falsos positivos**, como os **números de Carmichael**.

### 1.4 Aplicações

- Testes de primalidade rápidos
- Algoritmos criptográficos
- Pré-filtragem de números antes de testes mais robustos
- Criptografia de chave pública (ex: RSA)

### 1.5 Análise da Tabela

O script percorre vários **intervalos numéricos**, testando um valor "procurado" em cada um. Para cada número:

- Testa com bases 2, 3, 5 e 7.
- Se **falhar em alguma base**, já sabemos que ele é composto.
- Mostra sua **fatoração prima** como explicação.

---

## 2. Script `pequeno_teorema_de_fermat.py`

### 2.1 Relação com o Teorema

O script é uma aplicação direta do Pequeno Teorema de Fermat para detectar números **certamente compostos**, usando múltiplas bases.

### 2.2 Objetivo do Script

Identificar e exibir **números compostos** rapidamente, com base em sua **falha no teste de Fermat**.

### 2.3 Exemplo de Saída

```bash
📌 Intervalo [32, 63] — Procurando: 49
------------------------------------------------------------
🎯 >>>>> 49 falha no teste de Fermat → COMPOSTO! | Fatores: 7^2 <<<<<
````

Outro exemplo:

```bash
📌 Intervalo [224, 255] — Procurando: 224
------------------------------------------------------------
🎯 >>>>> 224 falha no teste de Fermat → COMPOSTO! | Fatores: 2^5 × 7 <<<<<
```

### 2.4 Funcionamento Interno

O script:

1. Define uma tabela de intervalos e números "procurados".
2. Para cada número, testa se ele **falha no teste de Fermat** para as bases: 2, 3, 5 e 7.
3. Se falhar, exibe o número e sua **fatoração**.
4. Os falsos positivos não são garantidamente detectados — o foco é **detecção de compostos**.

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10**
* Bibliotecas necessárias:

```bash
pip install sympy
```

Usa a biblioteca `sympy` para fatoração e manipulação de inteiros grandes.

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

### 3.2 Referências

* 📘 [Wikipedia: Pequeno Teorema de Fermat](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem)
* 📗 *Elementary Number Theory* – David Burton
* 📙 [Numberphile: Fermat and Primality Testing](https://www.youtube.com/watch?v=2z0lo4U4jWg)

### 3.3 Testes e Validações

* Validado com números compostos e primos conhecidos
* Fatorações conferidas com `sympy`
* Resultados consistentes com teoria clássica

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

### Termos Técnicos Explicados

* **Módulo (mod)**: operação que calcula o resto da divisão de dois números.
* **Primo**: número que só pode ser dividido por 1 e por ele mesmo.
* **Fatoração**: escrever um número como produto de números menores.
* **Fermat base a**: significa testar um número com o valor de **a** no teorema.
* **Número de Carmichael**: composto que engana o teste de Fermat (falso positivo).
* **Falso positivo de Fermat**: número que passa no teste mesmo não sendo primo.

---
