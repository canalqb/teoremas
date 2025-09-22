# 📐 - Teorema de Tietze

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)

## Frase do Teorema

> Se uma função contínua está definida numa parte fechada de um espaço normal, então é possível estendê-la para todo o espaço mantendo essa continuidade.
> *Em outras palavras, você pode “esticar” essa função para um domínio maior sem criar “buracos” ou “saltos” inesperados.*

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `tietze_intervals.py`](#2-script-tietze_intervalspy)

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

O **Teorema de Tietze** afirma que, quando você tem uma função que é “suave” (contínua) em um conjunto fechado, você pode estendê-la para um conjunto maior sem perder essa suavidade. Esse resultado é muito importante na matemática porque permite construir funções em espaços maiores a partir de partes menores.

### 1.2 Exemplos Práticos

Imagine que você tem um mapa que descreve a temperatura em uma região fechada (por exemplo, uma cidade). O teorema garante que podemos criar um mapa para uma área maior que inclui essa cidade, mantendo a temperatura suave, sem “saltos” ou mudanças bruscas.

### 1.3 Explicação Detalhada

No dia a dia, “função contínua” significa algo sem pulos ou que muda devagar. Espaço normal é um tipo de espaço onde conseguimos separar áreas diferentes com “cercas invisíveis”. O teorema mostra que, se sabemos como a função se comporta numa parte fechada (com limites definidos), podemos estendê-la para todo o espaço de forma organizada.

### 1.4 Aplicações

Esse teorema é útil em análise matemática, física e engenharia, especialmente quando precisamos estender dados ou funções parciais para domínios maiores mantendo propriedades importantes.

### 1.5 Análise da Tabela

Na tabela, vemos intervalos baseados em potências de 2. Cada intervalo vai de 2 elevado a N até 2 elevado a (N+1), menos 1. O fim do intervalo é um número conhecido como número de Mersenne (um número um a menos que uma potência de 2).

O valor esperado pelo teorema é um número que está dentro desses intervalos, mostrando que podemos “estender” valores com segurança nesse intervalo. No script, usamos apenas os limites para gerar valores intermediários, sem usar o resultado esperado.

---

## 2 Script `tietze_intervals.py`

### 2.1 Relação com o Teorema

O script trabalha com os intervalos baseados em potências de 2 e números de Mersenne, que são usados para definir faixas onde o valor gerado fica “estendido” dentro desses limites — de maneira análoga à ideia do teorema de extensão contínua, mas aplicada a números.

### 2.2 Objetivo do Script

Gerar valores dentro de cada intervalo definido entre 2^N e (2^(N+1))-1, usando apenas os limites para cálculo, sem usar o valor esperado para o cálculo, mostrando que é possível “estender” ou criar valores válidos dentro desses intervalos.

### 2.3 Exemplo de Saída

```
N   | Inicio (2^N)  | Valor Teorema  | Fim (2^(N+1))-1
-------------------------------------------------------
0   | 1            | 1              | 1              
1   | 2            | 3              | 3              
2   | 4            | 7              | 7              
3   | 8            | 11             | 15             
4   | 16           | 23             | 31             
5   | 32           | 47             | 63             
6   | 64           | 95             | 127            
7   | 128          | 191            | 255            
8   | 256          | 383            | 511            
9   | 512          | 767            | 1023           
```

### 2.4 Funcionamento Interno

* Para cada N, calcula o início como 2^N.
* Calcula o fim como (2^(N+1)) - 1, o número de Mersenne correspondente.
* O valor é o número inteiro no meio do intervalo, mostrando que está dentro do intervalo.
* Isso demonstra uma forma de “extensão” ou aproximação dentro dos limites.

### 2.5 Tecnologias e Requisitos

* Python 3.8.10 (ou superior)
* Ambiente que suporte execução de scripts Python

---

## 3 Extras

### 3.1 Licença

Projeto sob licença MIT — sinta-se livre para usar, modificar e distribuir.

### 3.2 Referências

* Wikipédia: [Teorema de Tietze](https://pt.wikipedia.org/wiki/Teorema_de_Tietze)
* Números de Mersenne: números que são um a menos que uma potência de 2, como 3, 7, 15, 31...
* Conceitos básicos de topologia e funções contínuas.

### 3.3 Testes e Validações

* Validado para N de 0 a 9, com saída consistente dentro dos intervalos.
* A tabela de saída confere que valores ficam sempre entre os limites calculados.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5 Nota

**Função contínua:** significa uma função que não tem “saltos” ou mudanças bruscas; seu gráfico pode ser desenhado sem tirar o lápis do papel.

**Espaço normal:** é um tipo de espaço onde podemos separar conjuntos que não se tocam usando “vizinhanças” abertas — pense como separar grupos em áreas distintas.

**Número de Mersenne:** números que são sempre um a menos que uma potência de 2, tipo 3 (2^2-1), 7 (2^3-1), 15 (2^4-1), etc.

**Potência de 2:** resultado de multiplicar o número 2 por ele mesmo N vezes, por exemplo 2^3 = 2 × 2 × 2 = 8.

**Intervalo:** conjunto de números entre um início e um fim. Aqui, entre 2^N e 2^(N+1)-1.
