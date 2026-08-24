# 🧩 - De Fraisse
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Fraïssé-ff69b4.svg)](https://en.wikipedia.org/wiki/Fra%C3%AFss%C3%A9%27s_theorem)

## Frase do Teorema

> *Dada uma classe de estruturas finitas com certas propriedades, existe uma estrutura infinita que contém todas as anteriores e respeita sua forma.* – Em termos simples, é possível **reconstruir algo infinito a partir de todas as peças pequenas**, desde que elas sigam certas regras.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `fraisse_approximation.py`](#2-script-fraisse_approximationpy)
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

O **Teorema de Fraïssé** trata da construção de estruturas infinitas a partir de pedaços finitos, contanto que essas partes tenham uma boa "coerência interna". Isso permite construir **estruturas grandes que preservam as relações das menores**.

### 1.2 Exemplos Práticos

- Construir uma árvore genealógica infinita a partir de pequenos grupos familiares coerentes.
- Montar um grafo infinito que contenha todos os grafos pequenos de uma classe, sem contradições.

### 1.3 Explicação Detalhada

A ideia é que, se temos muitas estruturas pequenas (por exemplo, tabelas com dados organizados de formas diferentes), podemos imaginar um "modelo gigante" que contenha todas elas — **sem quebrar nenhuma das conexões ou relações** entre os dados.

Esse modelo é:

- **Universal**: inclui todas as peças pequenas.
- **Ultrahomogêneo**: as partes pequenas podem ser movidas, e o todo continua igual.

### 1.4 Aplicações

- Teoria dos modelos (Lógica)
- Banco de dados relacionais (consistência)
- Lógica para Inteligência Artificial
- Estruturas combinatórias

### 1.5 Análise da Tabela

O script gera uma tabela com três colunas:

| N | Início (2^N) | Aproximado | Fim (2^(N+1)-1) |
|---|--------------|------------|-----------------|
| 0 | 1            | 1          | 1               |
| 1 | 2            | 2          | 3               |
| 2 | 4            | 5          | 7               |
| 3 | 8            | 12         | 15              |
| 4 | 16           | 27         | 31              |
| 5 | 32           | 58         | 63              |
| 6 | 64           | 121        | 127             |
| 7 | 128          | 248        | 255             |
| 8 | 256          | 503        | 511             |
| 9 | 512          | 1014       | 1023            |

---

## 2. Script `fraisse_approximation.py`

### 2.1 Relação com o Teorema

O script simula **como cresce o número de estruturas** que satisfazem as condições do Teorema de Fraïssé, mostrando que esse crescimento é **rápido e acumulativo**, como esperado.

### 2.2 Objetivo do Script

- Simular a contagem de estruturas possíveis até um nível `N`
- Estimar o número "mínimo necessário" para garantir completude
- Exibir o crescimento da complexidade combinatória

### 2.3 Exemplo de Saída

```
N = 0 | Início: 1 | Aproximado: 1 | Fim: 1
N = 1 | Início: 2 | Aproximado: 2 | Fim: 3
N = 2 | Início: 4 | Aproximado: 5 | Fim: 7
...
N = 9 | Início: 512 | Aproximado: 1014 | Fim: 1023
```

### 2.4 Funcionamento Interno

O script usa a fórmula:

```python
aproximado = sum(2 ** i for i in range(N + 1)) - N
````

Ou seja:

* Soma as potências de 2 até `N`
* Subtrai `N` como ajuste fino
* Exibe os valores mínimo (`2^N`), aproximado, e máximo (`2^(N+1)-1`)

Isso modela a **acumulação das subestruturas** até o nível `N`.

### 2.5 Tecnologias e Requisitos

* Linguagem: **Python 3.8.10**
* Não utiliza bibliotecas externas — apenas `print` e `range`

Para executar:

```bash
python fraisse_approximation.py
```

---

## 3 Extras

### 3.1 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### 3.2 Referências

* Fraïssé, Roland. *Sur certaines relations qui généralisent l'ordre des nombres rationnels*. C. R. Acad. Sci. Paris, 1954.
* Model Theory — Hodges, W. (Cambridge University Press)
* [Wikipedia - Fraïssé's Theorem](https://en.wikipedia.org/wiki/Fra%C3%AFss%C3%A9%27s_theorem)

### 3.3 Testes e Validações

* Resultados verificados até `N = 9`
* A função de aproximação mostra crescimento quase máximo, com desvio controlado
* Pode ser expandido facilmente para `N > 10`

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

📘 **Glossário de termos técnicos usados:**

* **Estrutura**: em lógica, é um conjunto com regras ou relações (como grafos, ordens, grupos, etc.)
* **Classe de estruturas**: conjunto de modelos com propriedades semelhantes
* **Subestrutura**: parte de uma estrutura que também respeita suas regras
* **Universalidade**: capacidade de conter todas as outras da classe
* **Ultrahomogeneidade**: qualquer pedaço pode ser movido dentro da estrutura sem mudar sua essência
* **Isomorfismo**: equivalência entre estruturas (mesma forma)
* **Automorfismo**: uma reordenação da estrutura que não altera suas propriedades
* **Variância**: (não usada aqui, mas comum em teoremas) – medida de dispersão de valores
