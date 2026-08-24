# 🧩 - Teorema do Gráfico Fechado 
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Gráfico%20Fechado-ff69b4.svg)](https://en.wikipedia.org/wiki/Closed_graph_theorem)

## Frase do Teorema

> Se você tem uma função linear entre dois espaços completos e o gráfico dessa função está fechado, então a função é contínua. – Em outras palavras, se os pares (entrada, saída) da função se comportam bem (sem quebras, saltos ou buracos), então a função não faz nada "louco": ela é suave e previsível.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `grafico_fechado_visual.py`](#2-script-grafico_fechado_visualpy)

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

O **Teorema do Gráfico Fechado** afirma que, se uma função linear entre dois espaços completos (matematicamente chamados de "espaços de Banach") tem um gráfico que não apresenta rupturas, então essa função é obrigatoriamente contínua.

### 1.2 Exemplos Práticos

- Quando um sistema de equações ou uma transformação respeita a convergência dos seus dados e resultados.
- Em programação, é como garantir que uma função sempre retorne resultados estáveis se as entradas forem estáveis.

### 1.3 Explicação Detalhada

Imagine que você tem uma função matemática que transforma vetores de um espaço em vetores de outro. Se, ao observar todas as entradas e saídas, não existem pontos onde "quase se chega" a um valor e o resultado pula para outro, então essa função se comporta bem o suficiente para ser considerada contínua.

O termo "gráfico fechado" significa apenas que, quando uma sequência de pares (entrada, saída) se aproxima de algum ponto, então esse ponto também pertence à função. Se isso acontecer, a função é suave e confiável.

### 1.4 Aplicações

- Análise Funcional
- Processamento de sinais
- Modelos contínuos em física e engenharia
- Garantia de estabilidade em transformações matemáticas

### 1.5 Análise da Tabela

| n  | 2^n | 2^(n+1) - 1 |
|----|-----|-------------|
| 0  | 1   | 1           |
| 1  | 2   | 3           |
| 2  | 4   | 7           |
| 3  | 8   | 15          |
| ...| ... | ...         |
| 10 | 1024| 2047        |

---

## 2. Script `grafico_fechado_visual.py`

### 2.1 Relação com o Teorema

Este script foi criado para **visualizar a ideia por trás do Teorema do Gráfico Fechado**. Ele representa os dados em 3D com elementos que giram em torno de um fundo fixo, sugerindo o fechamento e continuidade da função representada.

### 2.2 Objetivo do Script

- Exibir visualmente o comportamento de uma função contínua através da analogia com um toroide.
- Mostrar dois conjuntos de pontos:
  - Os valores 2 elevado a n
  - Os números de Mersenne: 2 elevado a (n + 1) menos 1
- Simular ligações entre eles com cilindros verticais, para sugerir a "estrutura do gráfico"

### 2.3 Exemplo de Saída

Você verá um gráfico 3D com:

- Um **toroide** no fundo, representando o espaço onde o gráfico vive.
- **Pontos azuis** representando os valores 2^n.
- **Pontos vermelhos** para os valores de Mersenne.
- **Linhas verticais** conectando os pares de valores.
- Uma **animação suave** onde somente os dados giram, não o fundo.

### 2.4 Funcionamento Interno

- Geração de pontos 3D com coordenadas circulares.
- Uso de funções de rotação para mover os pontos.
- Geração de uma superfície 3D com `plot_surface` para o toroide.
- Atualização quadro a quadro dos pontos e linhas conectando-os.

### 2.5 Tecnologias e Requisitos

- Python 3.8.10
- Bibliotecas:
  - `numpy`
  - `matplotlib`

Instale com:

```bash
pip install numpy matplotlib
````

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a licença MIT.

### 3.2 Referências

* Wikipedia: [Closed Graph Theorem](https://en.wikipedia.org/wiki/Closed_graph_theorem)
* Livro: Introdução à Análise Funcional — Bachman & Narici
* canalqb.blogspot.com

### 3.3 Testes e Validações

Testado no Python 3.8.10 em Ubuntu e Windows. Rodando via:

```bash
python grafico_fechado_visual.py
```

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**espaço de Banach:**
Um tipo especial de espaço matemático onde é possível medir distâncias entre pontos, e onde qualquer sequência que se aproxima de algum lugar realmente chega lá.

**função linear:**
Uma função que respeita adição e multiplicação por números. Por exemplo, dobrar um número ou somar dois valores.

**contínua:**
Quer dizer que a função não dá "saltos". Pequenas mudanças na entrada causam pequenas mudanças na saída.

**gráfico fechado:**
O conjunto de pontos (entrada, saída) da função não tem buracos. Se você se aproxima de um ponto, ele realmente está no gráfico.

**número de Mersenne:**
Um número da forma 2^(n + 1) - 1. Esses números aparecem em várias áreas da matemática.

**rotação em torno do eixo Z:**
Girar os dados como se você estivesse vendo de cima e eles estivessem girando como um disco.
