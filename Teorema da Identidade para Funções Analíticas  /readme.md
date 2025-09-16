# 🔍 - Teorema da Identidade para Funções Analíticas  
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Frase do Teorema

> Se duas funções analíticas forem iguais em vários pontos que se aproximam de um mesmo lugar, elas serão iguais para todos os pontos desse lugar — ou seja, elas são a mesma função.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `teorema_identidade_justificacao.py`](#2-script-teorema_identidade_justificacaopy)

  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)  
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

## 1. Introdução ao Teorema

### 1.1 Resumo

Este conceito diz que se duas funções muito "bem comportadas" (chamadas de *analíticas*) forem iguais em muitos pontos que se juntam em um lugar, elas serão iguais em todo o domínio. Isso ajuda a garantir que funções complexas não podem ser diferentes e ainda parecer iguais em uma sequência de pontos próximos.

### 1.2 Exemplos Práticos

Imagine duas funções que você conhece em alguns valores especiais, como potências de 2 (1, 2, 4, 8...) ou números chamados Mersenne (que são 2 elevado a um número primo menos 1, como 3, 7, 31...). Se essas funções derem o mesmo resultado nesses valores, e elas forem analíticas, então elas serão idênticas para todos os valores.

### 1.3 Explicação Detalhada

Funções analíticas podem ser representadas por somas de termos com potências (séries de potências). Se todas as somas desses termos forem iguais para uma sequência de pontos que se juntam, então todos os termos da soma (que representam as derivadas) devem ser iguais — assim, as funções são iguais para qualquer valor.

### 1.4 Aplicações

Esse conceito é importante para garantir que soluções de problemas matemáticos complexos são únicas, especialmente em física, engenharia e ciências da computação.

### 1.5 Análise da Tabela

A tabela gerada pelo script mostra valores da função exponencial em pontos especiais, confirmando que em todos esses pontos \( f(z) = g(z) \). Isso reforça a ideia da unicidade da função nesses pontos e, portanto, em todo domínio.

---

## 2. Script `teorema_identidade_justificacao.py`

### 2.1 Relação com o Teorema

Este script verifica se duas funções analíticas coincidem em pontos importantes (potências de 2 e números de Mersenne) e, com base nisso, conclui que elas são iguais em todo domínio.

### 2.2 Objetivo do Script

Mostrar de maneira simples e prática que se duas funções coincidem em vários pontos que “se acumulam” em um lugar, elas devem ser a mesma função em todo o lugar onde são bem comportadas.

### 2.3 Exemplo de Saída

```

Ponto   f(z)           g(z)           Igual?
1       2.71828        2.71828        True
2       7.38906        7.38906        True
4       54.59815       54.59815       True
8       2980.95799     2980.95799     True
16      8886110.52051  8886110.52051  True
32      7.8963e13      7.8963e13      True
3       20.08554       20.08554       True
7       1096.63316     1096.63316     True
31      2.9e13         2.9e13         True
127     1.43e38        1.43e38        True

Se as funções coincidirem nesses pontos e forem analíticas,
elas são iguais em todo o domínio onde estão definidas.

```

### 2.4 Funcionamento Interno

- Define as funções analíticas (exemplo: exponencial)
- Gera pontos especiais (potências de 2 e números de Mersenne)
- Avalia as funções nesses pontos e compara os resultados
- Se os valores coincidirem, conclui que as funções são iguais

### 2.5 Tecnologias e Requisitos

- **Python 3.8.10**  
- Biblioteca **sympy** para manipulação simbólica e cálculos matemáticos

---

## 3. Extras

### 3.1 Licença

Este projeto está licenciado sob a licença MIT — sinta-se livre para usar, modificar e compartilhar.

### 3.2 Referências

- Funções analíticas e séries de potências (para iniciantes)
- Números de Mersenne: números da forma 2^p - 1, onde p é um número primo  
- Documentação oficial do Python e Sympy

### 3.3 Testes e Validações

Testes simples com funções exponenciais e polinomiais confirmam a validade do conceito apresentado.

---

## 4. Contato

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

*{Função analítica}: uma função que pode ser representada por uma soma infinita de potências (como uma soma de termos com z, z², z³...) perto de qualquer ponto dentro do seu domínio.*  

*{Número de Mersenne}: um número que é 2 elevado a um número primo menos 1 (por exemplo, 3, 7, 31).*  

*{Ponto de acumulação}: um ponto onde você pode encontrar muitos valores diferentes de uma sequência cada vez mais perto desse ponto.*  

*{Domínio}: o conjunto de todos os valores onde uma função está definida e "funciona bem".*  

*{Derivada}: uma medida de como uma função muda em cada ponto (uma ideia simples de inclinação).*  
