# ⚡ - Aproximação Discreta da Transformada de Laplace usando Potência de 2

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  

---

## Frase do conceito

> A soma de potências decrescentes aproximadas pode representar funções contínuas, facilitando seu estudo e aplicações práticas no dia a dia.

---

## Sumário

* [1. Introdução ao Conceito](#1-introdução-ao-conceito)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `Laplace.py`](#2-script-laplacepy)
  * [2.1 Relação com o Conceito](#21-relação-com-o-conceito)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3. Extras](#3-extras)
  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referencias)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4. Contato](#4-contato)
* [5. Nota](#5-nota)

---

## 1. Introdução ao Conceito

### 1.1 Resumo

Este projeto mostra como somar potências da forma 2 * e^(-s), de modo crescente, para aproximar uma função contínua no tempo. A ideia é fácil de entender e ajuda a visualizar fenômenos naturais e tecnológicos do nosso cotidiano, que podem ser representados por essas somas.

### 1.2 Exemplos Práticos

- Controle de velocidade em ventiladores e motores elétricos.  
- Sistemas automáticos em carros, como ABS e controle de estabilidade.  
- Processos industriais que controlam temperatura e pressão.  
- Processamento de sinais digitais, como áudio e vídeo.

### 1.3 Explicação Detalhada

O script calcula o somatório parcial da sequência:  

"cada termo é igual a (2 vezes o valor de e elevado a -s) elevado a n",  

onde n é o número do termo na sequência. A soma dos primeiros n termos aproxima a função completa.  

Também mostramos os números de Mersenne (2^n - 1), que são importantes na matemática e servem para comparar o crescimento dos valores.

### 1.4 Aplicações

Esses conceitos ajudam engenheiros e cientistas a entender e simular sistemas reais usando métodos simples, discretos, que podem ser aplicados em softwares de controle e análise de dados.

### 1.5 Análise da Tabela

A tabela exibida mostra:  

- O número do termo (n).  
- O valor do termo individual.  
- A soma acumulada até aquele termo.  
- O número de Mersenne correspondente a n.  

Com isso, fica fácil visualizar o comportamento da soma e sua aproximação.

---

## 2. Script `Laplace.py`

### 2.1 Relação com o Conceito

Este script executa a soma dos termos que aproximam uma função que cresce em potências de 2 multiplicadas por um fator decrescente exponencial, para valores de n de 0 até 20.

### 2.2 Objetivo do Script

Mostrar a evolução da soma parcial e comparar com números matemáticos famosos (Mersennes), imprimindo uma tabela e gerando uma animação visual do processo.

### 2.3 Exemplo de Saída

```

## n |     Termo (2 e^-s)^n |  Soma parcial F\_n(s) | Mersenne 2^n - 1

0 |             1.000000 |             1.000000 |               0
1 |             0.735759 |             1.735759 |               1
2 |             0.541341 |             2.277100 |               3
...
20 |             0.002161 |             3.778404 |         1048575

```

### 2.4 Funcionamento Interno

- Calcula os termos da série para cada n.  
- Soma os termos progressivamente.  
- Calcula os números de Mersenne para comparação.  
- Imprime tabela formatada.  
- Cria animação da soma parcial crescendo no gráfico.

### 2.5 Tecnologias e Requisitos

- Python 3.8.10  
- Bibliotecas: `numpy`, `matplotlib`  
- Ambiente que suporte animações do matplotlib

---

## 3. Extras

### 3.1 Licença

MIT License — uso livre e aberto para fins acadêmicos e pessoais.

### 3.2 Referências

- Conceitos básicos de séries geométricas.  
- Aplicações práticas em engenharia e tecnologia.

### 3.3 Testes e Validações

Testado com Python 3.8.10 em ambiente local, com saída gráfica e tabular conforme esperado.

---

## 4. Contato

- Feito por CanalQb no GitHub  
- Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
- 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
- PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**e**: base da exponenciação, aproximadamente 2.718, que representa crescimento contínuo.  
**s**: parâmetro real positivo usado para controlar a taxa de decaimento.  
**n**: número inteiro representando o termo na sequência.  
**Soma parcial**: total acumulado até um certo termo da sequência.  
**Números de Mersenne**: números na forma 2^n - 1, usados em matemática para vários estudos.  
**Termo**: valor individual calculado para cada n.  

Esses termos são apresentados com linguagem simples para facilitar o entendimento.
