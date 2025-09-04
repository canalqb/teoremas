# 📐 - Teorema de Poincaré (Aproximação pelo Intervalo Binário)

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## Frase do Teorema

> Toda estrutura tridimensional que não possui buracos pode ser comparada a uma esfera — ou seja, qualquer laço dentro dela pode ser “desfeitos” até um ponto.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `aproximacao_teorema_poincare.py`](#2-script-aproximacao_teorema_poincarepy)
  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3 Extras](#3-extras)
  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referências)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4 Contato](#4-contato)
* [5. Nota](#5-nota)

---

## 1 Introdução ao Teorema

### 1.1 Resumo

O teorema afirma que toda forma tridimensional **sem buracos** (ou seja, onde qualquer laço pode ser "achatado" a um ponto) é equivalente a uma esfera tridimensional normal, mesmo que pareça diferente à primeira vista.

### 1.2 Exemplos Práticos

Imagine uma bola de borracha — qualquer laço nela pode ser esticado e "fechado" até virar um ponto. Já um donut tem um buraco no meio, então isso não acontece.

### 1.3 Explicação Detalhada

A conjectura foi um problema matemático que durou mais de 100 anos, até que foi resolvido usando um método que suaviza a forma com o tempo, parecido com derreter as imperfeições até sobrar a esfera perfeita.

### 1.4 Aplicações

Esse resultado ajuda a entender a forma de objetos no espaço, que é importante na física, na cosmologia e em outras áreas da ciência que estudam o universo e formas complexas.

### 1.5 Análise da Tabela

Para vários números naturais N, temos intervalos entre 2 elevado a N e 2 elevado a (N+1) menos 1. Queremos encontrar números dentro desse intervalo que possam representar algum "valor esperado" sem usar diretamente esses valores esperados.

---

## 2 Script `aproximacao_teorema_poincare.py`

### 2.1 Relação com o Teorema

O script usa a ideia de trabalhar dentro de intervalos definidos por potências de dois, aproximando valores que poderiam estar associados ao conceito principal do teorema, mas sem usar valores diretamente fornecidos. Ele usa uma função simples para preencher esses espaços.

### 2.2 Objetivo do Script

Criar valores aproximados dentro dos intervalos que possam se relacionar à ideia do teorema, garantindo que os valores estejam sempre dentro dos limites iniciais e finais definidos.

### 2.3 Exemplo de Saída

```

## N | Início (2^N) |  Aproximado | Fim (2^(N+1)-1)

0 |            1 |           1 |               1
1 |            2 |           2 |               3
2 |            4 |           4 |               7
3 |            8 |           9 |              15
4 |           16 |          18 |              31
5 |           32 |          40 |              63
6 |           64 |          87 |             127
7 |          128 |         190 |             255
8 |          256 |         419 |             511
9 |          512 |         926 |            1023

```

### 2.4 Funcionamento Interno

Para cada N, calcula o intervalo entre 2^N e 2^(N+1)-1. A seguir, calcula um valor aproximado dentro desse intervalo usando uma fórmula que cresce de forma quadrática simples, sem ultrapassar os limites.

### 2.5 Tecnologias e Requisitos

* Python 3.8.10 ou superior  
* Nenhuma biblioteca externa necessária

---

## 3 Extras

### 3.1 Licença

Este projeto está sob licença MIT — sinta-se livre para usar, modificar e distribuir.

### 3.2 Referências

* História da conjectura de Poincaré: artigos e vídeos populares de matemática  
* Material introdutório sobre topologia para iniciantes

### 3.3 Testes e Validações

O script foi testado para N de 0 a 9 e gera valores coerentes dentro dos intervalos.

---

## 4 Contato

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*

---

## 5 Nota

**Teorema:** é uma afirmação matemática que foi provada como verdadeira.  

**Valor esperado:** é o resultado que a matemática prevê que vai acontecer, como uma média prevista.  

**Potência de dois:** é um número que resulta de multiplicar 2 por ele mesmo várias vezes, como 2, 4, 8, 16, 32...  

**Intervalo:** é um espaço entre dois números, como entre 4 e 7.  

**Aproximação:** é quando usamos um número perto do valor exato, para facilitar cálculos ou entendimentos.
