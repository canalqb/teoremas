# 🧩 - Radon Nikodym

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Radon%E2%80%93Nikodym-ff69b4.svg)](https://pt.wikipedia.org/wiki/Teorema_de_Radon%E2%80%93Nikodym)

## Frase do Teorema

> Se uma "medida" (como uma forma de contar ou medir algo) pode ser sempre explicada como uma "densidade" multiplicada por outra medida, então existe uma função que mostra exatamente essa relação.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)

* [2. Script `radon_nikodym_animation.py`](#2-script-radon_nikodym_animationpy)

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

Este resultado diz que se você tem duas formas de medir algo, e uma delas sempre "segue" a outra, então é possível encontrar uma função que mostra a relação exata entre elas, como uma espécie de "densidade" que transforma uma medida na outra.

### 1.2 Exemplos Práticos

Imagine que uma medida conta a quantidade de objetos numa caixa, e outra mede o peso total. Se o peso sempre cresce proporcionalmente à quantidade, então existe uma função que diz o peso por objeto — essa é a "densidade" que o teorema garante existir.

### 1.3 Explicação Detalhada

* "Medida" é uma forma de contar ou avaliar uma coisa em um espaço, como quantidade, probabilidade ou peso.
* Quando dizemos que uma medida está “absolutamente contínua” em relação a outra, significa que quando a primeira diz que algo tem valor zero, a outra também.
* A função que o teorema afirma existir é chamada de "derivada de Radon–Nikodym" e serve para transformar uma medida em outra por meio da multiplicação.

### 1.4 Aplicações

* Em probabilidade, para transformar distribuições diferentes
* Em estatística, para calcular densidades relativas
* Em física, para relacionar diferentes formas de medir grandezas

### 1.5 Análise da Tabela

Não aplicável neste contexto.

---

## 2 Script `radon_nikodym_animation.py`

### 2.1 Relação com o Teorema

O script usa sequências numéricas (potências de 2 e números de Mersenne) para criar pontos e vetores que representam visualmente a ideia de transformar uma medida em outra usando uma função densidade, ilustrando a essência do resultado.

### 2.2 Objetivo do Script

Gerar uma animação 3D vertical (formato 9:16) que exibe os pontos e as conexões entre eles sequencialmente, com duração de 20 segundos, e salvar como GIF.

### 2.3 Exemplo de Saída

Um gráfico 3D animado onde os pontos aparecem um a um, conectados por linhas, mostrando a relação entre as medidas e sua transformação.

### 2.4 Funcionamento Interno

* Calcula pontos baseados nas potências de 2 e nos números de Mersenne para n = 0 a 10
* Exibe os pontos e conecta-os com linhas vermelhas que simbolizam a "densidade" entre medidas
* Anima os pontos e linhas aparecendo sequencialmente com intervalo controlado
* Salva a animação em arquivo GIF e exibe o gráfico ao final

### 2.5 Tecnologias e Requisitos

* Python 3.8.10
* Bibliotecas: numpy, matplotlib

Instalação via pip:

```
pip install numpy matplotlib
```

---

## 3 Extras

### 3.1 Licença

MIT License – livre para uso, modificação e distribuição

### 3.2 Referências

* Wikipedia: [Teorema de Radon–Nikodym](https://pt.wikipedia.org/wiki/Teorema_de_Radon%E2%80%93Nikodym)
* Documentação matplotlib: [https://matplotlib.org](https://matplotlib.org)

### 3.3 Testes e Validações

O script foi testado em Python 3.8.10 e gera animações conforme esperado, com boa performance em computadores comuns.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5 Nota

* **Medida:** forma de contar ou avaliar algo em um espaço, como quantidade, peso ou probabilidade
* **Densidade:** função que indica a relação entre duas medidas, mostrando "quanto" uma medida representa em relação à outra em cada ponto
* **Absolutamente contínua:** situação em que, se uma medida diz que algo é zero, a outra também diz que é zero, garantindo que uma depende da outra sem "buracos"
* **Função derivada de Radon–Nikodym:** a função densidade que transforma uma medida em outra
* **Probabilidade:** medida que expressa a chance ou possibilidade de um evento acontecer
* **Distribuição:** forma de espalhar valores ou probabilidades ao longo de um conjunto
