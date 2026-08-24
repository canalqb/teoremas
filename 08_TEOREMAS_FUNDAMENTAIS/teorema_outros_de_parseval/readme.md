# 🧩 - De Parseval
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  

## Frase do conceito  

> A energia total de um sinal pode ser obtida tanto somando o quadrado do valor do sinal ao longo do tempo quanto somando o quadrado das suas componentes de frequência. Isso mostra que a energia no tempo e no espectro são equivalentes.

## Sumário

* [1. Introdução ao conceito](#1-introdução-ao-conceito)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `parseval_onda_quadrada.py`](#2-script-parseval_onda_quadradapy)  
  * [2.1 Relação com o conceito](#21-relação-com-o-conceito)  
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

## 1. Introdução ao conceito  

### 1.1 Resumo  

A energia de um sinal, que é uma medida de quanta "força" ou "potência" ele contém, pode ser calculada de duas formas equivalentes: somando o quadrado dos valores do sinal no tempo ou somando o quadrado das suas componentes que formam o sinal nas diferentes frequências.

### 1.2 Exemplos Práticos  

Imagine uma música tocando: a energia do som pode ser entendida tanto pelo volume ao longo do tempo quanto pelas notas que compõem a música em diferentes frequências. Ambas as formas dão a mesma ideia da energia total.

### 1.3 Explicação Detalhada  

Quando um sinal é decomposto em ondas senoidais simples (por exemplo, usando Fourier), cada uma dessas ondas tem uma certa contribuição para o sinal original. Somando os quadrados dessas contribuições (que representam a energia em cada frequência) obtemos a energia total do sinal, que também pode ser obtida integrando o quadrado do sinal original no tempo.

### 1.4 Aplicações  

- Processamento de sinais para análise de áudio e imagens.  
- Compressão de dados onde entender a energia ajuda a reduzir o que é irrelevante.  
- Engenharia elétrica em circuitos e telecomunicações.  

### 1.5 Análise da Tabela  

No script, é possível ver a comparação numérica entre a energia calculada no tempo e na frequência, e a diferença entre elas é muito pequena, o que confirma a equivalência.

---

## 2. Script `parseval_onda_quadrada.py`  

### 2.1 Relação com o conceito  

Este script calcula a aproximação da energia de uma onda quadrada tanto no tempo quanto na frequência, mostrando na prática a equivalência entre as duas formas.

### 2.2 Objetivo do Script  

Mostrar numericamente como a energia no tempo e na frequência se igualam para um sinal periódico, aproximado pela soma de ondas senoidais.

### 2.3 Exemplo de Saída  

```

Energia no domínio do tempo: 1.000000
Energia no domínio da frequência (soma dos coeficientes): 0.979753
Diferença (deve ser próxima de zero): 0.020247

```

### 2.4 Funcionamento Interno  

- Calcula a soma das potências dos harmônicos (ondas senoidais com frequências múltiplas ímpares) que compõem a onda quadrada.  
- Mostra um gráfico da aproximação da onda quadrada usando diferentes números de termos.  
- Anima um ponto amarelo que percorre a curva, exibindo o valor do sinal em cada instante.

### 2.5 Tecnologias e Requisitos  

- Python 3.8.10  
- Bibliotecas: numpy, matplotlib  

---

## 3 Extras  

### 3.1 Licença  

Projeto aberto sob licença MIT.

### 3.2 Referências  

- [Fourier Series and Signal Energy Concepts](https://en.wikipedia.org/wiki/Parseval%27s_theorem)  
- [Matplotlib Documentation](https://matplotlib.org/stable/api/animation_api.html)  

### 3.3 Testes e Validações  

A validação principal é a comparação numérica entre energia no tempo e na frequência, que deve ser próxima de zero.

---

## 4 Contato  

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*

---

## 5. Nota  

{**lambda:**} é um nome usado para indicar uma frequência ou uma constante em matemática e física, aqui representa a frequência fundamental do sinal.  
{**variância:**} mede o quanto os valores de uma grandeza estão espalhados em relação à média, ou seja, indica a variação dos dados.  
{**esperança:**} é uma maneira formal de dizer "média" ou "valor esperado" de uma variável, indicando o valor médio que se espera obter em várias medições.  
{**harmônicos:**} são ondas com frequências múltiplas inteiras da frequência fundamental, usadas para construir sinais complexos.  
{**coeficientes de Fourier:**} são os números que indicam o peso de cada onda senoidal na composição do sinal original.  
