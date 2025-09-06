# 🌀 - Teorema da Curva de Jordan

[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Curva%20de%20Jordan-ff69b4.svg)](https://en.wikipedia.org/wiki/Jordan_curve_theorem)

## Frase do Teorema

> **Toda curva simples e fechada no plano divide o plano em duas regiões: uma interna e uma externa. A curva é a fronteira entre essas duas.** – Isso quer dizer que, mesmo que a curva tenha forma estranha, contanto que não se cruze, ela sempre separa o plano em dentro e fora.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `jordan_regions_generator.py`](#2-script-jordan_regions_generatorpy)

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

O **Teorema da Curva de Jordan** garante que, se você desenhar qualquer curva que:

* seja contínua (sem saltos),
* não se cruze,
* e volte ao ponto de partida (fechada),

então essa curva separa o plano em duas regiões **claramente distintas**: o **interior** e o **exterior**.

### 1.2 Exemplos Práticos

* Um círculo.
* Um quadrado.
* Um coração desenhado com um traço só (sem cruzar).

Todos esses dividem o espaço em "dentro" e "fora".
Curvas como essas aparecem em áreas como:

* Computação Gráfica 🖥️
* Geometria Computacional 📐
* Processamento de Imagens 🧠
* Robótica 🤖

### 1.3 Explicação Detalhada

Se pegarmos essa ideia e aplicarmos de forma **recursiva**, podemos imaginar **múltiplas curvas** se formando e **dividindo regiões anteriores**. Isso gera um **modelo topológico** de crescimento, como se cada curva gerasse **mais regiões internas** ao longo de subdivisões.

### 1.4 Aplicações

* Geração de mapas binários (quadtree, BSP).
* Compressão de imagens com segmentação por regiões.
* Detecção de contornos.
* Inteligência artificial em jogos e simulações.

### 1.5 Análise da Tabela

A tabela abaixo foi gerada com base em divisões sucessivas usando curvas, com limites de cada linha dados pelas potências de 2:

| N | Início (2^N) | Esperado (calculado) | Fim (2^(N+1)-1) |
| - | ------------ | -------------------- | --------------- |
| 0 | 1            | 1                    | 1               |
| 1 | 2            | 3                    | 3               |
| 2 | 4            | 7                    | 7               |
| 3 | 8            | 15                   | 15              |
| 4 | 16           | 31                   | 31              |
| 5 | 32           | 63                   | 63              |
| 6 | 64           | 127                  | 127             |
| 7 | 128          | 255                  | 255             |
| 8 | 256          | 467                  | 511             |
| 9 | 512          | 1023                 | 1023            |

---

## 2. Script `jordan_regions_generator.py`

### 2.1 Relação com o Teorema

Este script simula o comportamento do Teorema da Curva de Jordan em um modelo computacional.
Cada curva "simples fechada" gera uma nova subdivisão da região anterior.

### 2.2 Objetivo do Script

* Simular, para cada valor de N, a quantidade de regiões internas geradas por curvas.
* Os valores são calculados apenas dentro do intervalo `[2^N, 2^(N+1)-1]`.
* Não usa aproximação: os resultados respeitam limites topológicos.

### 2.3 Exemplo de Saída

```text
N   | Início (2^N)   | Esperado (calculado)    | Fim (2^(N+1)-1)
-----------------------------------------------------------------
0   | 1              | 1                       | 1
1   | 2              | 3                       | 3
2   | 4              | 7                       | 7
3   | 8              | 15                      | 15
4   | 16             | 31                      | 31
5   | 32             | 63                      | 63
6   | 64             | 127                     | 127
7   | 128            | 255                     | 255
8   | 256            | 467                     | 511
9   | 512            | 1023                    | 1023
```

### 2.4 Funcionamento Interno

O cálculo de regiões usa a fórmula:

```
regiões = (curvas * (curvas + 1)) // 2
```

E depois verifica se o número calculado está **dentro do intervalo permitido**, sem ultrapassar `fim`.

### 2.5 Tecnologias e Requisitos

* ✅ **Python 3.8.10**
* ✅ Sem bibliotecas externas
* ✅ Executável em terminal com:

```bash
python jordan_regions_generator.py
```

---

## 3 Extras

### 3.1 Licença

Distribuído sob licença MIT. Veja o arquivo `LICENSE`.

### 3.2 Referências

* [Wikipedia: Jordan Curve Theorem](https://en.wikipedia.org/wiki/Jordan_curve_theorem)
* [Geometria Topológica para Computação Gráfica](https://en.wikipedia.org/wiki/Computational_geometry)

### 3.3 Testes e Validações

* Validado com os valores esperados manualmente.
* Verificado que todos os resultados estão dentro dos intervalos.
* Compatível com Python 3.8 até Python 3.11.

---

## 4 Contato

* Feito por **CanalQb** no GitHub
* Visite o blog: [canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: **13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava**
* 📩 PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Curva simples fechada:**
uma linha contínua que não se cruza e termina onde começou.

**Região interna e externa:**
a área dentro da curva (interna) e tudo que está fora (externa).

**Topologia:**
ramo da matemática que estuda formas e espaços sem depender de medidas exatas.

**Subdivisão:**
quebra de uma região em partes menores.

**Recursiva:**
quando uma operação é repetida várias vezes dentro dela mesma.

**Fórmula triangular:**
método simples para somar os primeiros números naturais: 1 + 2 + 3 + ... + n.
