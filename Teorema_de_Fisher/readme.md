# 🧬 - Teorema de Fisher
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Teorema%20de%20Fisher-ff69b4.svg)](https://en.wikipedia.org/wiki/Fisher%27s_fundamental_theorem_of_natural_selection)

## Frase do Teorema

> *A taxa de aumento da aptidão média de uma população é proporcional à variância genética em aptidão.* — Ou seja, **quanto mais variedade há entre os indivíduos, maior é a chance da população melhorar com o tempo.**

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `Teorema_de_Fisher.py`](#2-script-teorema_de_fisherpy)
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

O **Teorema de Fisher**, da biologia evolutiva, conecta duas ideias fundamentais:

- A **variância genética** (diferença entre os indivíduos)
- O **aumento da aptidão média** da população ao longo do tempo

Em outras palavras: **é a diversidade que permite evolução e melhora**.

### 1.2 Exemplos Práticos

- Em uma população de organismos, aqueles com características mais adaptadas tendem a se reproduzir mais.
- A variedade genética garante que alguns indivíduos sempre tenham vantagem — o que empurra a média da população para cima.

### 1.3 Explicação Detalhada

O teorema afirma que:

```
Mudança na média da aptidão = Variância genética da aptidão
```

Ou seja, **quanto mais diferentes os indivíduos são entre si (em termos genéticos), mais rapidamente a média da aptidão da população melhora**.

No contexto do nosso script, a variabilidade dos dados ajuda a prever o comportamento futuro de uma função.

### 1.4 Aplicações

- Biologia evolutiva
- Algoritmos genéticos
- Modelagem estatística
- Previsões baseadas em dados variáveis

### 1.5 Análise da Tabela

Usamos uma tabela com valores `(x, y, z)`, onde:

- `x` cresce exponencialmente (potências de 2)
- `y` é a variável que queremos modelar
- `z = 2 * x - 1` (uma transformação direta de x)

Nosso objetivo é **modelar y em função de x** e prever o valor de y para um novo x.

---

## 2. Script `Teorema_de_Fisher.py`

### 2.1 Relação com o Teorema

O script usa o princípio da **variância como motor de aprendizado**:

- Os dados de entrada variam bastante (crescem rápido)
- Essa variância permite que um modelo consiga "aprender" e **prever** corretamente o comportamento de y em relação a x

### 2.2 Objetivo do Script

* Construir um modelo matemático simples (polinômio) que represente `y = f(x)`
* Usar esse modelo para prever `y` para um novo valor de `x = 65536`
* Comparar a previsão com o valor real informado (`y = 95823`)
* Exibir um **gráfico interativo** para facilitar a análise

### 2.3 Exemplo de Saída

Modelo ajustado:
```
y = a*x^2 + b*x + c
```

Previsão para x=65536:
```
y\_predito = 95789
```

Valor real esperado:
```
y\_real = 95823
```

Diferença = 34

E o gráfico gerado mostrará os pontos reais e a curva ajustada, com tooltips para explorar.

### 2.4 Funcionamento Interno

1. Organiza os dados em um DataFrame
2. Ajusta uma função quadrática (grau 2) do tipo:

```
y = a \* x^2 + b \* x + c
``` 
3. Aplica a previsão com `x = 65536`
4. Exibe o gráfico interativo com `Plotly`

### 2.5 Tecnologias e Requisitos

Use Python 3.8.10 com as seguintes bibliotecas:

```bash
pip install numpy pandas plotly
````

*Execução:*

```bash
python Teorema_de_Fisher.py
```

O gráfico será aberto automaticamente no navegador padrão.

---

## 3 Extras

### 3.1 Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.

### 3.2 Referências

* Fisher, R.A. (1930). *The Genetical Theory of Natural Selection*.
* Ewens, W\.J. (2004). *Mathematical Population Genetics*.
* Documentação oficial do [Plotly](https://plotly.com/python/)

### 3.3 Testes e Validações

O modelo foi validado com:

* **Erro absoluto pequeno** (diferença < 50 unidades)
* **Gráfico coerente** com os dados observados
* **Boa aderência visual da curva ao padrão dos dados**

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

📘 **Glossário de termos técnicos:**

* **Variância**: medida de quão diferentes os valores estão entre si. Quanto maior, mais dispersos os dados.
* **Aptidão**: quão "bom" um indivíduo é para sobreviver e se reproduzir.
* **Modelo polinomial**: uma fórmula matemática que usa potências de x para representar uma curva.
* **Predição**: estimativa de um valor com base em um modelo.
* **x, y, z**: variáveis da tabela. x cresce exponencialmente, y é o valor estudado, z é calculado a partir de x.
* **Plotly**: biblioteca de gráficos que permite interatividade e visualizações ricas. 
