# 📐 - Teorema de Scott

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)

## Frase do Teorema

> "O número esperado de elementos entre níveis em uma estrutura binária pode ser aproximado por uma função empírica de crescimento exponencial." – Em outras palavras, podemos estimar quantos elementos existem até um certo nível em uma árvore binária usando uma fórmula simples baseada na soma dos níveis anteriores e um ajuste proporcional.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `estimador_scott.py`](#2-script-estimador_scottpy)

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

O **Teorema de Scott** é uma ideia baseada em observações práticas sobre como o número de elementos cresce em níveis sucessivos de uma árvore binária completa. Ele propõe uma forma simples de estimar esse crescimento usando uma fórmula que soma potências de dois e aplica um ajuste linear para melhor aproximar o resultado real.

### 1.2 Exemplos Práticos

Imagine uma árvore binária onde cada nível tem o dobro de elementos do anterior:

* No nível 0, temos 1 elemento.
* No nível 1, temos 2 elementos.
* No nível 2, 4 elementos, e assim por diante.

O teorema ajuda a estimar a soma total dos elementos até um dado nível, sem precisar contar um por um.

### 1.3 Explicação Detalhada

A ideia principal é que o número mínimo de elementos em um nível N é 2 elevado a N (2^N). Já o total acumulado até o nível N, numa árvore binária completa, é dado por 2^(N+1) - 1.

O **Teorema de Scott** introduz uma fórmula para estimar o total acumulado, ajustando a soma dos níveis anteriores por um fator proporcional ao nível atual (N/5). Ou seja:

* Soma dos elementos até N-1: somar 2^0 + 2^1 + ... + 2^(N-1)
* Multiplicar essa soma por (1 + N/5) para aproximar o crescimento real.

### 1.4 Aplicações

Este modelo pode ser usado para:

* Analisar estruturas de dados, como árvores binárias.
* Estimar complexidade em algoritmos recursivos.
* Simular crescimento em processos ramificados.
* Ensinar conceitos de crescimento exponencial e somas cumulativas.

### 1.5 Análise da Tabela

A tabela gerada pelo script mostra os valores reais e estimados para cada nível N:

| N | Início (2^N) | Estimado (Teorema) | Fim (2^(N+1)-1) |
| - | ------------ | ------------------ | --------------- |
| 0 | 1            | 1                  | 1               |
| 1 | 2            | 1                  | 3               |
| 2 | 4            | 4                  | 7               |
| 3 | 8            | 11                 | 15              |
| 4 | 16           | 27                 | 31              |
| 5 | 32           | 62                 | 63              |
| 6 | 64           | 139                | 127             |
| 7 | 128          | 305                | 255             |
| 8 | 256          | 663                | 511             |
| 9 | 512          | 1431               | 1023            |

Observamos que a estimativa cresce mais rápido que o total real, o que ajuda a capturar variações em estruturas mais complexas.

---

## 2. Script `estimador_scott.py`

### 2.1 Relação com o Teorema

O script implementa a fórmula do Teorema de Scott para calcular e exibir a estimativa para níveis de 0 a 9, permitindo visualizar o crescimento e comparar com valores exatos.

### 2.2 Objetivo do Script

Mostrar uma forma prática e simples de calcular o número estimado de elementos até o nível N em uma árvore binária, usando Python e conceitos básicos de exponenciação e somas.

### 2.3 Exemplo de Saída

```text
N  | Início (2^N)   | Estimado (Teorema)     | Fim (2^(N+1))-1
------------------------------------------------------------
0  | 1              | 1                      | 1
1  | 2              | 1                      | 3
2  | 4              | 4                      | 7
3  | 8              | 11                     | 15
4  | 16             | 27                     | 31
5  | 32             | 62                     | 63
6  | 64             | 139                    | 127
7  | 128            | 305                    | 255
8  | 256            | 663                    | 511
9  | 512            | 1431                   | 1023
```

### 2.4 Funcionamento Interno

O cálculo principal é feito por:

```python
estimado = round(sum(2 ** k for k in range(n)) * (1 + n / 5.0))
```

Aqui:

* `sum(2 ** k for k in range(n))` soma os elementos dos níveis anteriores.
* `(1 + n / 5.0)` é o fator de ajuste proporcional ao nível N.
* `round` arredonda para o número inteiro mais próximo.

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10** (recomendado)
* Nenhuma biblioteca externa necessária.

---

## 3. Extras

### 3.1 Licença

Projeto sob licença MIT. Consulte o arquivo `LICENSE` para mais informações.

### 3.2 Referências

* Conceitos básicos de árvores binárias e exponenciação.
* Observações empíricas baseadas no crescimento em estruturas binárias.

### 3.3 Testes e Validações

Os valores exibidos foram validados manualmente e conferem com as somas e potências calculadas.

---

## 4. Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **Lambda (λ)**: termo usado para representar uma constante ou parâmetro em fórmulas. Aqui, não usamos explicitamente, mas se aparecer, pense como um valor fixo.
* **Esperança**: é a média esperada de um conjunto de valores, ou seja, o valor "normal" que esperamos encontrar.
* **Variância**: mede o quanto os valores se espalham em relação à média — ou seja, se os valores ficam próximos ou distantes da média.
* Quando falamos de "nível N", queremos dizer a posição ou camada dentro da árvore, começando do zero no topo.
