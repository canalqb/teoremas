# 🧩 - Numeros Fraco De Goldbach
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![Goldbach](https://img.shields.io/badge/Teorema-Fraco%20de%20Goldbach-ff69b4.svg)](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture#Weak_Goldbach_conjecture)

## Frase do Teorema

> Todo número ímpar maior que 5 pode ser escrito como a soma de três números primos – isto significa que qualquer número ímpar (3, 5, 7, 9, ...) acima de 5 pode ser formado somando três primos.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `teorema_goldbach_fraco.py`](#2-script-goldbach_weakpy)  
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
O **Teorema Fraco de Goldbach** afirma que *todo número ímpar maior que 5 pode ser escrito como a soma de três números primos*. Essa conjectura foi um desafio matemático até ser comprovada em 2013 por Harald Helfgott.

### 1.2 Exemplos Práticos  
- 7 = 2 + 2 + 3  
- 21 = 3 + 7 + 11  
- 33 = 3 + 13 + 17  

Esses exemplos mostram como números ímpares podem ser representados como soma de três primos.

### 1.3 Explicação Detalhada  
O que o teorema diz, em linguagem simples, é que não importa quão grande seja um número ímpar (desde que seja maior que 5), ele sempre pode ser "quebrado" em três números primos que somados dão ele de volta.

### 1.4 Aplicações  
Esse teorema ajuda a entender a distribuição dos números primos e tem impacto em criptografia e na teoria dos números, áreas que influenciam a segurança da informação e algoritmos matemáticos.

### 1.5 Análise da Tabela  

| **Início** | **Meio** | **Fim** |  
| ----------:| -------- | -------:|  
| 1          | 1        | 1       |  
| 2          | 3        | 3       |  
| 4          | 7        | 7       |  
| 8          | 8        | 15      |  
| 16         | 21       | 31      |  
| 32         | 49       | 63      |  
| 64         | 76       | 127     |  
| 128        | 224      | 255     |  
| 256        | 467      | 511     |  
| 512        | 514      | 1023    |  
| 1024       | 1155     | 2047    |  
| 2048       | 2683     | 4095    |  

- A coluna **Fim** segue a fórmula:  
  *Fim = 2 × Início - 1*  
  Estes são números de Mersenne, que têm forma especial na matemática.  
- A coluna **Meio** contém valores ímpares testados para o teorema.

---

## 2. Script `teorema_goldbach_fraco.py`

### 2.1 Relação com o Teorema  
O script valida se o número da coluna **Meio** pode ser escrito como a soma de três primos, aplicando diretamente o Teorema Fraco de Goldbach.

### 2.2 Objetivo do Script  
Verificar, para vários valores de teste, se eles seguem a regra do teorema e mostrar a decomposição em três números primos.

### 2.3 Exemplo de Saída  

```bash
Início: 16, Meio: 21, Fim: 31
✅ 21 = 2 + 2 + 17
````

### 2.4 Funcionamento Interno

* O script lê cada linha da tabela.
* Para cada número do meio, tenta encontrar três primos cuja soma seja igual ao valor.
* Se encontrar, imprime a decomposição; caso contrário, indica que não foi possível.

### 2.5 Tecnologias e Requisitos

* Python 3.8.10 (ou superior)
* Biblioteca **sympy** para funções de números primos

Instalação da dependência:

```bash
pip install sympy
```

Execução:

```bash
python teorema_goldbach_fraco.py
```

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a **Licença MIT** — veja o arquivo LICENSE para mais detalhes.

### 3.2 Referências

* [Weak Goldbach conjecture - Wikipedia](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture#Weak_Goldbach_conjecture)
* Harald Helfgott (2013), prova do Teorema Fraco de Goldbach.

### 3.3 Testes e Validações

O script foi testado para os valores da tabela e validou com sucesso a soma em três primos conforme esperado.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Número primo:** número que só pode ser dividido por 1 e por ele mesmo, como 2, 3, 5, 7, 11...

**Número ímpar:** número que não é divisível por 2, como 1, 3, 5, 7, 9...

**Números de Mersenne:** números que têm a forma 2ⁿ - 1, ou seja, um número que é potência de 2 menos 1.

**Potência de 2:** resultado de multiplicar 2 por ele mesmo várias vezes, por exemplo 2, 4, 8, 16, 32...

**Teorema:** é uma afirmação matemática que foi comprovada ser verdadeira.

--- 
