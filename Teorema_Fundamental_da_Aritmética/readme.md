# 🧮 - Teorema Fundamental da Aritmética  
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![Fundamental](https://img.shields.io/badge/Teorema-Fundamental%20da%20Aritmética-ff69b4.svg)](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic)

## Frase do Teorema

> Todo número inteiro maior que 1 pode ser escrito de forma única como um produto de números primos, desconsiderando a ordem dos fatores – ou seja, cada número tem uma “assinatura” única feita de primos.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `teorema_fundamental_da_aritmetica.py`](#2-script-teorema_fundamental_da_aritmeticapy)  
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
O **Teorema Fundamental da Aritmética** diz que *qualquer número inteiro maior que 1 pode ser escrito como um produto de números primos, e essa forma é única, se a ordem dos fatores for ignorada*.  

### 1.2 Exemplos Práticos  
- 8 = 2 × 2 × 2  
- 21 = 3 × 7  
- 18 = 2 × 3 × 3  

Cada número tem uma “receita” única de primos que o formam.

### 1.3 Explicação Detalhada  
Imagine que todo número é feito de “blocos” que são os números primos (aqueles que só podem ser divididos por 1 e por eles mesmos). Não importa como você fatora o número, a combinação desses blocos será sempre a mesma, só que a ordem pode variar.

### 1.4 Aplicações  
Essa propriedade é fundamental para:  

- Criptografia, que protege dados usando números primos  
- Algoritmos matemáticos e computacionais  
- Compreensão da estrutura dos números  

### 1.5 Análise da Tabela  

O script divide os números em intervalos crescentes baseados em potências de 2:

| Intervalo      | Exemplo de fatoração                 |  
| -------------- | ---------------------------------- |  
| [1,1]          | 1 (não fatorável, base)             |  
| [2,3]          | 2 = 2, 3 = 3                       |  
| [4,7]          | 4 = 2², 5 = 5, 6 = 2 × 3, 7 = 7   |  
| [8,15]         | 8 = 2³, 9 = 3², ...                |  
| [16,31]        | 21 = 3 × 7, 28 = 2² × 7, ...      |  

Alguns números são destacados para melhor visualização.

---

## 2. Script `teorema_fundamental_da_aritmetica.py`

### 2.1 Relação com o Teorema  
O script ilustra na prática a fatoração única de cada número em seus primos, mostrando a essência do Teorema Fundamental da Aritmética.

### 2.2 Objetivo do Script  
Percorrer intervalos de números e exibir suas fatorações primárias, destacando alguns números importantes para facilitar o entendimento.

### 2.3 Exemplo de Saída  

```bash
Intervalo [2, 3]:
------------------------------
2 = 2
>>>>> 3 = 3 <<<<<
````

```bash
Intervalo [8, 15]:
------------------------------
>>>>> 8 = 2^3 <<<<<
9 = 3^2
10 = 2 * 5
...
```

```bash
Intervalo [16, 31]:
------------------------------
...
>>>>> 21 = 3 * 7 <<<<<
...
```

### 2.4 Funcionamento Interno

* O script usa a função `factorint()` da biblioteca `sympy` para fatorar cada número.
* Percorre os números dentro dos intervalos definidos por potências de 2.
* Imprime a fatoração com um formato claro, usando expoentes quando necessário.
* Destaca números especiais para facilitar o estudo.

### 2.5 Tecnologias e Requisitos

* Python 3.8.10
* Biblioteca `sympy` (instale via `pip install sympy`)

Executar com:

```bash
python teorema_fundamental_da_aritmetica.py
```

---

## 3 Extras

### 3.1 Licença

Este projeto é distribuído sob a **Licença MIT**. Veja o arquivo LICENSE para detalhes.

### 3.2 Referências

* [Fundamental theorem of arithmetic - Wikipedia](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic)
* Documentação Sympy: [https://docs.sympy.org/latest/modules/ntheory.html](https://docs.sympy.org/latest/modules/ntheory.html)

### 3.3 Testes e Validações

O script foi testado com sucesso nos intervalos indicados, mostrando fatorações corretas e únicas para os números apresentados.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Número primo:** número maior que 1 que só pode ser dividido por 1 e por ele mesmo, como 2, 3, 5, 7...

**Expoente:** número que indica quantas vezes um fator se repete, por exemplo, 2³ significa 2 × 2 × 2.

**Fatoração:** forma de escrever um número como produto de outros números (fatores).

**Potência de 2:** resultado de multiplicar 2 por ele mesmo várias vezes, por exemplo, 2, 4, 8, 16, 32...

**Intervalo:** faixa de números entre dois valores, usados aqui para organizar a análise.

--- 
