# 🧩 - De Borsuk Ulam

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)

## Frase do Teorema

> Para qualquer função que conecta pontos de uma esfera a pontos em um espaço plano, sempre existe um par de pontos opostos na esfera que são mapeados exatamente para o mesmo ponto no plano – isso significa que, por exemplo, dois pontos opostos na Terra podem ter exatamente as mesmas condições medidas ao mesmo tempo.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `borsuk_ulam_approx.py`](#2-script-borsuk_ulam_approxpy)

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

O teorema afirma que, se você pegar qualquer forma esférica (como uma bola ou a Terra) e ligar pontos dela a um espaço menor (como um plano), sempre existirá pelo menos um par de pontos opostos (diametralmente opostos) que levam ao mesmo ponto no espaço menor.

### 1.2 Exemplos Práticos

Imagine que você mede temperatura e pressão ao mesmo tempo em todos os lugares da Terra. Esse resultado garante que existem dois pontos exatamente opostos na Terra com a mesma temperatura e pressão naquele instante.

### 1.3 Explicação Detalhada

Não importa como você conecte ou mapeie os pontos da esfera para o plano, sempre haverá um par de pontos opostos na esfera com a mesma "imagem" ou resultado na conexão. Isso acontece porque a esfera tem uma estrutura especial, que força essa coincidência.

### 1.4 Aplicações

Esse resultado é útil em diversas áreas como física, matemática, ciências ambientais e qualquer área que estude fenômenos naturais sobre superfícies esféricas.

### 1.5 Análise da Tabela

A tabela usada relaciona números baseados em potências de 2 (2^N) e números chamados de Mersenne (2^(N+1) - 1). Ela mostra intervalos numéricos que crescem em potência de 2. O valor esperado do fenômeno está sempre dentro desse intervalo. O script vai calcular uma aproximação usando a média desses intervalos para estimar esses valores.

---

## 2. Script `borsuk_ulam_approx.py`

### 2.1 Relação com o Teorema

O script trabalha com os números relacionados à ideia do teorema, usando potências de 2 para gerar intervalos onde o valor esperado deve estar, sem usar diretamente o valor esperado para cálculo.

### 2.2 Objetivo do Script

Gerar uma tabela de valores para N variando de 0 a 9, mostrando o intervalo entre 2^N e 2^(N+1)-1, e calculando uma aproximação do valor esperado como a média desses limites.

### 2.3 Exemplo de Saída

```
 N | Inicio (2^N) | Aprox. Teorema | Fim (2^(N+1))-1
-------------------------------------------------------
 0 |            1 |               1 |                 1
 1 |            2 |               2 |                 3
 2 |            4 |               5 |                 7
 3 |            8 |              11 |                15
 4 |           16 |              23 |                31
 5 |           32 |              47 |                63
 6 |           64 |              95 |               127
 7 |          128 |             191 |               255
 8 |          256 |             383 |               511
 9 |          512 |             767 |              1023
```

### 2.4 Funcionamento Interno

Para cada N, o script calcula:

* **Início:** 2 elevado a N (2^N)
* **Fim:** 2 elevado a (N+1) menos 1 (2^(N+1) - 1)
* **Aproximação:** a média inteira entre o início e o fim, ou seja, (início + fim) dividido por 2

### 2.5 Tecnologias e Requisitos

* Python 3.8.10
* Nenhuma biblioteca externa é necessária.

---

## 3 Extras

### 3.1 Licença

Este projeto está sob licença MIT.

### 3.2 Referências

* Wikipédia: [Borsuk-Ulam theorem](https://en.wikipedia.org/wiki/Borsuk–Ulam_theorem)
* Introdução à topologia e mapeamentos esféricos.

### 3.3 Testes e Validações

O script imprime a tabela diretamente, permitindo fácil verificação dos valores para N de 0 a 9. Pode ser facilmente adaptado para outros valores de N.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **Teorema:** Resultado matemático que apresenta uma verdade comprovada rigorosamente.
* **Potência:** Resultado da multiplicação de um número por ele mesmo várias vezes, por exemplo, 2 elevado a N significa multiplicar 2 por ele mesmo N vezes.
* **Número de Mersenne:** Número que é sempre uma potência de 2 menos 1, por exemplo, 3, 7, 15, 31, etc.
* **Média:** Valor que fica no meio entre dois números.
* **Função Contínua:** Forma de conectar números ou pontos onde não há "saltos" ou interrupções.
* **Ponto Antipodal:** Dois pontos que estão exatamente opostos um ao outro numa esfera, como os polos da Terra.
