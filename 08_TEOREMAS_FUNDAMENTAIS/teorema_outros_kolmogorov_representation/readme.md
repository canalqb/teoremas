# 🧩 - Kolmogorov Representation
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![Kolmogorov](https://img.shields.io/badge/Teorema-Kolmogorov--Arnold-6495ED.svg)](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Arnold_representation_theorem)  

## Frase do Teorema

> Toda função contínua de múltiplas variáveis pode ser representada como uma composição finita de funções contínuas de uma única variável e de adição – isso significa que funções complexas podem ser construídas só com somas e funções simples de uma variável.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Demonstração Computacional](#15-análise-da-demonstração-computacional)  
* [2. Script `kolmogorov_representation_intervals_reduced.py`](#2-script_kolmogorov_representation_intervals_reducedpy)  
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

O **Teorema de Kolmogorov–Arnold** é um resultado matemático surpreendente que mostra que qualquer função contínua com várias variáveis pode ser escrita usando só funções de uma variável e somas. Isso quebra a ideia de que funções multivariadas precisam de operações complicadas.

### 1.2 Exemplos Práticos

Imagine que você tem uma função que depende de duas variáveis, como f(x, y) = sin(x) * cos(y). O teorema garante que essa função pode ser aproximada por uma soma de funções simples, que só recebem uma variável de cada vez.

### 1.3 Explicação Detalhada

A função original f(x1, x2, ..., xn) pode ser expressa como uma soma de funções univariadas aplicadas à soma de outras funções univariadas sobre cada variável, assim:

f(x1, x2, ..., xn) = soma para q de phi_q ( soma para p de psi_{q,p}(x_p) )

Aqui, phi e psi são funções que só recebem uma variável e são contínuas.

### 1.4 Aplicações

- Base teórica para redes neurais profundas  
- Redução dimensional em análise matemática  
- Compressão e modelagem de dados complexos  
- Teoria da computação e análise funcional  

### 1.5 Análise da Demonstração Computacional

Este projeto apresenta uma versão simplificada para duas variáveis: f(x,y) = sin(x)*cos(y) é aproximada por:

f_approx(x,y) = phi_1(psi_1(x) + psi_2(y))  

com psi_1(x) = sin(x), psi_2(y) = cos(y), e phi_1(z) = 0.5 * sin(z).

O script compara visualmente a função original com a aproximação, mostrando que mesmo com uma simplificação, a ideia do teorema se mantém.

---

## 2. Script `kolmogorov_representation_intervals_reduced.py`

### 2.1 Relação com o Teorema

O script demonstra computacionalmente o teorema, usando uma versão reduzida que aproxima uma função bidimensional por funções univariadas e soma, conforme a estrutura do teorema.

### 2.2 Objetivo do Script

Mostrar na prática como funções complexas podem ser reconstruídas usando apenas funções simples e operações de soma, validando a teoria por meio de visualizações gráficas.

### 2.3 Exemplo de Saída

O programa gera:

- Uma tabela com amostras dos valores da função original e da aproximação  
- Dois gráficos 3D lado a lado comparando as superfícies das funções  

### 2.4 Funcionamento Interno

- Gera pontos amostrais em intervalos baseados em potências de 2  
- Avalia f(x,y) = sin(x)*cos(y) nos pontos gerados  
- Avalia a aproximação reduzida via funções univariadas e soma  
- Exibe gráficos 3D para visualização comparativa  

### 2.5 Tecnologias e Requisitos

- Python 3.8.10  
- Bibliotecas: `numpy` e `matplotlib`  

Para instalar as dependências:

```bash
pip install numpy matplotlib
````

---

## 3 Extras

### 3.1 Licença

Este projeto está sob licença **MIT**, podendo ser utilizado livremente para fins educacionais e acadêmicos.

### 3.2 Referências

* Kolmogorov, A.N. (1957). Representação de funções contínuas
* Arnold, V.I. (1957). Extensão do teorema
* Hecht-Nielsen, R. (1987). Teorema de redes neurais

### 3.3 Testes e Validações

Testado em Python 3.8.10 com dados gerados para comparação visual e análise numérica, validando o funcionamento esperado.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Função contínua**: função que não apresenta "saltos" ou quebras no seu gráfico, ou seja, pode ser desenhada sem levantar a caneta do papel.

**Variável univariada**: função que depende de uma única variável.

**Composição de funções**: usar uma função dentro de outra, por exemplo, f(g(x)).

**Aproximação**: estimativa ou cálculo que chega próximo do valor real, mas não necessariamente igual.

**Potências de 2**: números obtidos multiplicando 2 por ele mesmo várias vezes (ex: 2, 4, 8, 16, 32...).
