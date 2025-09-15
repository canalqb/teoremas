# 🌐 - Projeção Estereográfica Generalizada
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Projeção-Estereográfica-ff69b4.svg)](https://en.wikipedia.org/wiki/Stereographic_projection)

## Frase do Conceito

> A **projeção estereográfica** é uma forma de "achatar" a superfície de uma esfera em um plano, de maneira contínua, suave e sem distorcer os ângulos entre curvas. – *Ela transforma pontos de uma esfera (exceto um ponto especial, chamado ponto norte) em pontos de um plano de maneira única e reversível.*

---

## Sumário

* [1. Introdução ao Conceito](#1-introdução-ao-conceito)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `stereographic_projection.py`](#2-script-stereographic_projectionpy)
  * [2.1 Relação com o Conceito](#21-relação-com-o-conceito)
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

## 1. Introdução ao Conceito

### 1.1 Resumo

A projeção estereográfica é uma técnica matemática para mapear todos os pontos de uma esfera (menos um) para um plano. Imagine segurar uma lanterna no topo da esfera: a sombra de cada ponto no chão (o plano) será sua projeção.

### 1.2 Exemplos Práticos

- Transformar mapas da Terra (globo) em projeções planas
- Visualizar funções complexas em 2D
- Usado em realidade virtual e gráficos 3D
- Projeções matemáticas em álgebra e topologia

### 1.3 Explicação Detalhada

Neste projeto, ao invés de uma única esfera, usamos uma **família de esferas**, cada uma com:

- **Ponto norte** com coordenada *z = 2^n*
- **Ponto sul** com coordenada *z = 2^(n+1) - 1*
- Onde *n* varia de 0 até 10

Cada ponto na esfera é projetado a partir do ponto norte, gerando uma imagem no plano tangente ao ponto sul.

### 1.4 Aplicações

- Simulações geométricas
- Modelagens com projeções topológicas
- Estudos de como dados esféricos se comportam no plano

### 1.5 Análise da Tabela

O resultado do script mostra como os pontos projetados **aumentam de complexidade** e **distância do centro**, conforme o tamanho da esfera cresce.

---

## 2. Script `stereographic_projection.py`

### 2.1 Relação com o Conceito

O script simula a projeção estereográfica para várias esferas, variando seu tamanho com base no valor de *n*. Para cada esfera:

- Gera 5 pontos aleatórios em sua superfície
- Projeta cada ponto em um plano tangente, a partir do ponto norte

### 2.2 Objetivo do Script

Demonstrar, na prática, como a projeção estereográfica funciona para esferas com diferentes tamanhos e posições, e como os pontos projetados se distribuem no plano.

### 2.3 Exemplo de Saída

Exemplo para `n = 3` (esfera com raio 8, ponto norte em z = 8 e plano tangente em z = 15):

```

n=3, R=8, Norte=\[0 0 8], Sul=\[ 0  0 15]
Ponto 0: Original \[-5.3  2.0 -5.6], Projeção \[ 2.7 -1.0 15.]
...

```

Cada linha mostra o ponto na esfera e sua projeção no plano.

### 2.4 Funcionamento Interno

1. Calcula a reta entre o ponto norte e cada ponto da esfera
2. Encontra onde essa reta cruza o plano tangente no ponto sul
3. Retorna o ponto de interseção

### 2.5 Tecnologias e Requisitos

- **Python** 3.8.10
- **Bibliotecas**: `numpy`

Como executar:

```bash
python stereographic_projection.py
```

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a **Licença MIT**. Veja o arquivo `LICENSE` para mais detalhes.

### 3.2 Referências

* Wikipedia – [Stereographic Projection](https://en.wikipedia.org/wiki/Stereographic_projection)
* Visualizações de geometria no canal 3Blue1Brown
* Cursos de cálculo vetorial e geometria analítica

### 3.3 Testes e Validações

Os testes foram feitos para valores de *n* de 0 até 10. O comportamento da projeção foi validado visualmente nos resultados.

---

## 4 Contato

* Feito por **CanalQb** no GitHub
* Visite o blog: canalqb.blogspot.com → [https://canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Projeção estereográfica**:
é uma forma de representar uma esfera em um plano, traçando uma reta do "ponto norte" até qualquer outro ponto da esfera e estendendo até cruzar um plano fixo.

**Plano tangente**:
é o plano que "toca" a esfera em apenas um ponto, como se fosse uma folha encostando na bola.

**Reta entre dois pontos**:
é o caminho direto e reto ligando dois pontos no espaço.

**2^n**:
significa "2 elevado à potência n", ou seja, 2 multiplicado por ele mesmo n vezes. Por exemplo, 2^3 = 8.

**n**:
é um número que varia de 0 até 10 neste projeto, usado para definir o tamanho da esfera.

**numpy**:
é uma biblioteca do Python usada para trabalhar com vetores e matrizes (listas de números organizadas).
