# 🧩 - Stone Weierstrass
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Stone--Weierstrass-ff69b4.svg)](https://en.wikipedia.org/wiki/Stone%E2%80%93Weierstrass_theorem)

## Frase do Teorema

> Qualquer função contínua definida em um intervalo fechado pode ser aproximada, tão bem quanto quisermos, por funções polinomiais – O Teorema de Stone–Weierstrass afirma que podemos "chegar perto o suficiente" de qualquer função contínua apenas combinando funções mais simples.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `stone_weierstrass_visual.py`](#2-script-stone_weierstrass_visualpy)
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

## 1. Introdução ao Teorema

### 1.1 Resumo

O Teorema de Stone–Weierstrass mostra que, se tivermos uma função contínua qualquer, podemos aproximá-la muito bem usando combinações de funções mais simples como potências ou polinômios. Ou seja, **funções complicadas podem ser construídas a partir de funções simples**.

### 1.2 Exemplos Práticos

Imagine que você tem uma função que representa o crescimento de uma planta ao longo dos dias. Mesmo que ela seja complexa, o teorema garante que você pode usar uma combinação de funções simples (como x², x³, etc.) para representar esse crescimento de forma bastante próxima.

### 1.3 Explicação Detalhada

- Se temos um intervalo fixo, como de 0 até 1, e uma função contínua dentro dele...
- Então podemos usar combinações de funções simples (como polinômios ou senos/cossenos) para gerar uma função que **se aproxime muito** da original.
- Isso significa que **modelagens complexas** podem ser feitas com **blocos simples**.

### 1.4 Aplicações

- Gráficos de aproximação de curvas
- Compressão de imagens e sons (formas simples representando dados complexos)
- Engenharia, computação gráfica, matemática aplicada e redes neurais

### 1.5 Análise da Tabela

Neste projeto, usamos potências de 2 e números de Mersenne para construir visualmente um exemplo de aproximação, simulando como funções mais simples podem compor algo mais complexo. Veja a tabela base:

```

N | Inicio (2^N) | Fim (2^(N+1)) - 1
0 | 1           | 1
1 | 2           | 3
2 | 4           | 7
3 | 8           | 15
4 | 16          | 31
5 | 32          | 63
6 | 64          | 127
7 | 128         | 255
8 | 256         | 511
9 | 512         | 1023
10| 1024        | 2047

```

---

## 2. Script `stone_weierstrass_visual.py`

### 2.1 Relação com o Teorema

O script mostra como **funções simples (baseadas em potências)** podem gerar algo mais complexo, representado por uma curva 3D. Isso é um exemplo visual da ideia central do Teorema de Stone–Weierstrass: **aproximação por simplicidade**.

### 2.2 Objetivo do Script

- Criar uma animação 3D com pontos gerados pelas potências de 2 e números de Mersenne
- Representar graficamente uma "função" que cresce com base em valores simples
- Gerar um arquivo `.gif` mostrando essa construção ponto a ponto

### 2.3 Exemplo de Saída

O script gera um arquivo chamado:

```
stone_weierstrass_animation.gif
```

Este arquivo mostra a animação dos pontos crescendo e se conectando no espaço tridimensional.

### 2.4 Funcionamento Interno

- Usa as fórmulas:
  - `x = 2^n`
  - `y = 2^(n+1) - 1`
  - `z = x + y`
- Anima os pontos um por um
- Conecta os pontos com uma linha
- Salva a visualização como um GIF com duração de 20 segundos

### 2.5 Tecnologias e Requisitos

- Python **3.8.10**
- Bibliotecas necessárias:
  ```bash
  pip install matplotlib scipy pillow
---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a licença **MIT**.

### 3.2 Referências

* [Wikipedia - Teorema de Stone–Weierstrass](https://en.wikipedia.org/wiki/Stone%E2%80%93Weierstrass_theorem)
* Visualização inspirada em conceitos de aproximação numérica

### 3.3 Testes e Validações

Testado com:

* Python 3.8.10 (Windows)
* GIF gerado corretamente
* Baixo consumo de memória

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com
  👉 [https://canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* 📧 PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Função contínua**:
Uma função que não tem "saltos" ou "quebras" — é suave em todo o intervalo.

**Aproximação**:
Chegar o mais próximo possível de um valor ou forma, sem precisar ser exatamente igual.

**Polinômio**:
Uma fórmula que envolve apenas multiplicações e somas de um número por si mesmo. Exemplo: x² + 2x + 3.

**Número de Mersenne**:
Um tipo especial de número que tem a forma 2^(n+1) - 1.

**Potência de 2**:
Números como 1, 2, 4, 8, 16... Cada um é o dobro do anterior.

**z = x + y**:
Nesse projeto, usamos isso como uma forma de compor dois valores simples (x e y) em um resultado mais complexo.
