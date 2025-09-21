# 📏 - Teorema Medida Externa de Lebesgue

[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Medida%20Externa%20de%20Lebesgue-ff69b4.svg)](https://en.wikipedia.org/wiki/Lebesgue_measure)

## Frase do Teorema

> A medida externa de Lebesgue é a menor soma de comprimentos de intervalos que conseguimos usar para cobrir qualquer conjunto – ou seja, o menor "tamanho total possível" que conseguimos medir com intervalos abertos.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `lebesgue_external_measure_viz.py`](#2-script-lebesgue_external_measure_vizpy)

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

A medida externa de Lebesgue é uma forma de dar um "tamanho" até para conjuntos muito complicados, como os que têm infinitos pontos bagunçados. É como tentar medir algo com uma régua, mas usando pedaços variáveis de régua para cobrir tudo de forma eficiente.

---

### 1.2 Exemplos Práticos

* Medir o tamanho de todos os números entre 0 e 1, mesmo que alguns estejam faltando.
* Calcular áreas em casos onde o método tradicional (como o de Riemann) não funciona.
* Estimar o "tamanho" de conjuntos de pontos em gráficos, mesmo que eles não formem segmentos contínuos.

---

### 1.3 Explicação Detalhada

Para descobrir a medida externa de um conjunto, você cobre ele com vários pedaços (intervalos) abertos e mede o total. A menor soma de comprimentos desses pedaços é o valor da medida externa.

Por exemplo:
Se você quer medir um ponto só (como 0), pode usar intervalos cada vez menores ao redor dele, como de -0.1 até 0.1, depois -0.01 até 0.01, e assim por diante. A soma pode ficar bem pequena, mas nunca será zero. Por isso, o ponto tem medida externa zero.

---

### 1.4 Aplicações

* Base para a **integração de Lebesgue**, uma forma mais poderosa de somar áreas.
* Usada para entender **probabilidades** em espaços contínuos.
* Aplicada na física, especialmente na mecânica quântica e em sistemas dinâmicos.

---

### 1.5 Análise da Tabela

| n   | 2^n (potência de 2) | 2^(n+1)-1 (Mersenne) |
| --- | ------------------- | -------------------- |
| 0   | 1                   | 1                    |
| 1   | 2                   | 3                    |
| 2   | 4                   | 7                    |
| 3   | 8                   | 15                   |
| ... | ...                 | ...                  |
| 10  | 1024                | 2047                 |

Esses valores representam pontos e linhas usados no script para criar intervalos visuais, que simulam coberturas de conjuntos.

---

## 2. Script `lebesgue_external_measure_viz.py`

### 2.1 Relação com o Teorema

Cada par de valores mostra o uso de intervalos (como se fossem pequenas réguas) para cobrir um espaço de pontos. Isso representa visualmente o processo de medir conjuntos usando coberturas, o que é a essência da medida externa.

---

### 2.2 Objetivo do Script

Criar uma animação 3D que mostra pontos com base nas potências de 2 e nos números de Mersenne. Esses pontos são conectados com vetores (linhas), simulando o processo de cobrir um conjunto com intervalos para medir seu "tamanho".

---

### 2.3 Exemplo de Saída

* Um GIF animado de 20 segundos
* Formato vertical (9:16)
* Pontos e linhas em 3D surgindo de forma sequencial
* Nome do arquivo gerado: `lebesgue_visualization.gif`

---

### 2.4 Funcionamento Interno

* Define 11 pares de valores para potências de 2 e números de Mersenne
* Constrói uma espiral em 3D para posicionar os pontos
* Usa `matplotlib` para desenhar e animar
* Salva a animação em um arquivo `.gif`

---

### 2.5 Tecnologias e Requisitos

* Python 3.8.10
* Bibliotecas usadas:

  * `matplotlib`
  * `numpy`
  * `Pillow`

Para instalar, use:

```bash
pip install matplotlib numpy pillow
```

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a licença MIT – veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

### 3.2 Referências

* Wikipedia: [Medida de Lebesgue](https://en.wikipedia.org/wiki/Lebesgue_measure)
* Apostilas de Cálculo Real e Medida
* Livro: *Medida e Integração* – Elias Zakon

---

### 3.3 Testes e Validações

* Testado em Python 3.8.10
* Funciona corretamente em sistemas Linux e Windows
* Verificado manualmente com diferentes valores de n

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com → [https://canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**conjunto:**
Um grupo de elementos, como números, letras ou pontos.

**intervalo aberto:**
Um pedaço de reta que não inclui suas extremidades. Ex: entre 1 e 2, mas sem o 1 e o 2.

**medida externa:**
Tentativa de medir o tamanho de um conjunto, mesmo que ele seja complexo ou infinito.

**inf (infinimum):**
É o menor valor possível que uma sequência ou conjunto pode alcançar, sem necessariamente fazer parte dele.

**Mersenne:**
Números criados com a fórmula 2^(n+1) - 1, usados em várias áreas da matemática.
