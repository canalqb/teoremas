# 🧩 - De Egorov

[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![EGV](https://img.shields.io/badge/Teorema-Egorov-ff69b4.svg)](https://en.wikipedia.org/wiki/Egorov%27s_theorem)

## Frase do Teorema

> *Se temos uma sequência de funções que converge ponto a ponto para uma função limite em um intervalo, então para qualquer margem de erro positiva, existe um subconjunto grande desse intervalo no qual essa convergência é uniforme.* – Ou seja, mesmo que as funções se aproximem da função final de forma “bagunçada” ponto a ponto, ainda conseguimos achar uma parte grande onde essa aproximação é “organizada” e ocorre de forma suave.

---
[![Siga o CanalQb](https://img.youtube.com/vi/Km-ucmJwvEw/hqdefault.jpg)](https://youtu.be/Km-ucmJwvEw)

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `egorov_animacao.py`](#2-script-egorov_animacaopy)

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

O Teorema de Egorov é um resultado da análise matemática que fala sobre como uma sequência de funções pode se comportar de forma mais "bonita" em grande parte de um intervalo, mesmo que originalmente pareça desorganizada.

### 1.2 Exemplos Práticos

Imagine que várias curvas vão se aproximando de uma curva final. Mesmo que essa aproximação não seja perfeita em todos os pontos, ainda conseguimos encontrar quase todo o intervalo onde essa aproximação acontece de maneira suave e previsível.

### 1.3 Explicação Detalhada

A convergência **ponto a ponto** significa que cada ponto no eixo x vai lentamente se aproximando do valor correto, mas em velocidades diferentes. O teorema afirma que é possível encontrar uma grande parte desse intervalo onde todas as funções da sequência se comportam quase da mesma forma — aproximando-se de forma uniforme da função limite.

### 1.4 Aplicações

* Em análise real e teoria da medida
* Visualização da transição de funções com comportamento pontual para comportamento uniforme
* Fundamento em provas de outros teoremas, como o da convergência dominada

### 1.5 Análise da Tabela

Neste projeto, a ideia não é uma tabela numérica, mas uma **animação** que demonstra visualmente a aproximação suave das funções. Cada linha representa uma função `x^k`, onde `k` cresce com o tempo — isso mostra como as funções se tornam cada vez mais "concentradas" no ponto `x = 1`, convergindo ponto a ponto para uma função tipo "degrau".

---

## 2. Script `egorov_animacao.py`

### 2.1 Relação com o Teorema

A animação ilustra como, mesmo que a convergência pareça caótica ao variar os expoentes `k` de `x^k`, ainda é possível visualizar um comportamento *uniforme* em grande parte do intervalo. Isso reflete diretamente o que o **Teorema de Egorov** afirma.

### 2.2 Objetivo do Script

📽️ Mostrar visualmente uma sequência de funções `f_k(x) = x^k`, onde `k` cresce de forma contínua. A animação exibe como essas curvas se tornam cada vez mais “esticadas” para o lado direito, convergindo ponto a ponto para uma função que vale 0 para `x < 1` e 1 em `x = 1`.

### 2.3 Exemplo de Saída

A saída do script é uma **animação 3D** com curvas que sobem juntas ao longo do eixo z (progresso da animação). Cada linha representa uma sequência de potências de `x`, suavemente interpoladas.

> A sensação final é de ver as curvas "caminhando juntas" para um mesmo destino.

### 2.4 Funcionamento Interno

* Usa o `matplotlib` com visualização 3D.
* Interpola valores de `k` de forma contínua entre `2^n` e `2^(n+1) - 1`.
* Aplica suavização na progressão com a função `smoothstep`.
* Cada curva é renderizada em uma camada `z` diferente, mostrando sua evolução no tempo.
* O eixo `z` simboliza o tempo/progresso da aproximação.

### 2.5 Tecnologias e Requisitos

* Python **3.8.10**
* `numpy`
* `matplotlib`

Para rodar o script:

```bash
pip install numpy matplotlib
python egorov_animacao.py
```

---

## 3. Extras

### 3.1 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### 3.2 Referências

* [Wikipedia - Teorema de Egorov](https://en.wikipedia.org/wiki/Egorov%27s_theorem)
* Livros de análise real e teoria da medida

### 3.3 Testes e Validações

Este projeto foi testado com Python **3.8.10** e bibliotecas atualizadas. A animação foi validada em sistemas Linux e Windows.

---

## 4. Contato

* Feito por **CanalQb** no GitHub
* Visite o blog: canalqb.blogspot.com → [https://canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**convergência ponto a ponto**: a função se aproxima da função final em cada ponto individualmente, mas não necessariamente ao mesmo tempo

**convergência uniforme**: a aproximação acontece com a mesma velocidade em todos os pontos do intervalo

**subconjunto de medida quase total**: um pedaço do intervalo que é quase tudo, só falta uma parte muito pequena

**função degrau**: uma função que "salta" de um valor para outro de forma abrupta, como 0 em quase todo lugar e 1 em um ponto

**interpolação**: técnica usada para fazer uma transição suave entre dois valores (como entre potências diferentes)

**suavização (smoothstep)**: fórmula que deixa a progressão mais fluida, sem saltos bruscos
