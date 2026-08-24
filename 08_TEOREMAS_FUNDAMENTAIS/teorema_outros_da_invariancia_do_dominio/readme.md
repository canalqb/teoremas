# 🧩 - Da Invariancia Do Dominio

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Invariância%20do%20Domínio-ff69b4.svg)](https://en.wikipedia.org/wiki/Invariance_of_domain)

## Frase do Teorema

> *Se você transforma um pedaço de espaço usando uma função que é contínua e não repete valores, o resultado ainda ocupa uma parte aberta do espaço original.* – Em outras palavras: o "tamanho" e a "forma" geral do espaço não se perdem com esse tipo de transformação.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `invariancia_dominio_discreta.py`](#2-script-invariancia_dominio_discretapy)

  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3. Extras](#3-extras)

  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referências)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4. Contato](#4-contato)
* [5. Nota](#5-nota)

---

## 1. Introdução ao Teorema

### 1.1 Resumo

O teorema da invariância do domínio mostra que uma função que mantém a ordem dos pontos (não dobra nem mistura) e é contínua preserva a estrutura do espaço que ela transforma.

### 1.2 Exemplos Práticos

* Um mapa de temperatura em uma cidade que é contínuo e não tem duas cidades com a mesma temperatura pode representar as regiões sem perder informação da "forma" do espaço.
* Se você desenhar um quadrado em uma folha e o esticar com as mãos sem dobrar, ele continua sendo uma figura aberta no plano.

### 1.3 Explicação Detalhada

Se você aplicar uma função que é:

* **Contínua** (sem saltos),
* **Injetora** (não repete pontos),

em um pedaço de espaço aberto do tipo R^n (por exemplo, um círculo ou uma bola 3D), o espaço resultante ainda vai ser aberto e terá a mesma dimensão.

### 1.4 Aplicações

* Topologia
* Teoria da dimensão
* Computação gráfica (manter integridade de malhas)
* Análise de espaços contínuos

### 1.5 Análise da Tabela

A tabela mostra a comparação entre três colunas:

* Início: o número 2 elevado à potência N
* Fim: o maior número possível nessa etapa (2^(N+1) - 1)
* Calculado: valor aproximado obtido com base em uma regra derivada de padrões numéricos e estruturais.

---

## 2. Script `invariancia_dominio_discreta.py`

### 2.1 Relação com o Teorema

Embora o teorema seja contínuo, este script trabalha com padrões discretos (valores inteiros). Ele tenta simular um comportamento similar ao "crescimento do espaço" mantendo a coerência entre início e fim, usando uma fórmula de aproximação baseada em potências de 2.

### 2.2 Objetivo do Script

O script calcula uma tabela com base em um padrão que cresce entre 2^N e 2^(N+1) - 1, tentando chegar em valores similares aos "esperados", sem usá-los diretamente.

### 2.3 Exemplo de Saída

```
N   | Inicio (2^N)  | Calculado  | Fim (2^(N+1)-1)
-------------------------------------------------------
0   | 1             | 1          | 1
1   | 2             | 2          | 3
2   | 4             | 5          | 7
3   | 8             | 12         | 15
4   | 16            | 27         | 31
5   | 32            | 58         | 63
6   | 64            | 121        | 127
7   | 128           | 248        | 255
8   | 256           | 503        | 511
9   | 512           | 1014       | 1023
```

### 2.4 Funcionamento Interno

* Para cada valor de N, o script calcula:

  * Início: 2 elevado a N
  * Fim: 2 elevado a (N+1) menos 1
  * Valor aproximado: usando soma de valores do tipo (2^k - 1) até N

* O valor final é ajustado para ficar dentro do intervalo entre início e fim.

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10**
* Script puro, sem bibliotecas externas
* Compatível com qualquer sistema operacional com Python instalado

---

## 3. Extras

### 3.1 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

### 3.2 Referências

* Wikipedia: [Invariance of Domain](https://en.wikipedia.org/wiki/Invariance_of_domain)
* CanalQb Blog: [https://canalqb.blogspot.com](https://canalqb.blogspot.com)

### 3.3 Testes e Validações

* Executado no terminal do Windows
* Validado com Python 3.8.10
* Comparado com valores de referência esperados

---

## 4. Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Contínua:**
Função que não dá saltos; você pode desenhar seu gráfico sem tirar o lápis do papel.

**Injetora:**
Função que nunca repete o mesmo valor de saída para entradas diferentes.

**Espaço aberto:**
Um conjunto de pontos que não inclui suas bordas (como um círculo sem a linha de contorno).

**Potência de 2:**
Números obtidos ao multiplicar 2 por ele mesmo várias vezes. Por exemplo: 2^3 = 8.

**Número de Mersenne:**
Número da forma 2^n - 1, como 3, 7, 15, etc.

**Soma de Mersenne:**
Soma de vários números de Mersenne. Ex: 1 + 3 + 7 = 11.

**R^n (espaço n-dimensional):**
Forma de representar um espaço com várias direções: R^2 é um plano, R^3 é o espaço tridimensional.
