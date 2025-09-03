# 📘 - Teorema de Itô
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Teorema%20de%20It%C3%B4-ff69b4.svg)](https://en.wikipedia.org/wiki/It%C5%8D%27s_lemma)

## Frase do Teorema

> O **Teorema de Itô** é uma regra para calcular a variação de funções que dependem de processos aleatórios, levando em conta o comportamento incerto desses processos. – Ele adapta a regra da cadeia do cálculo para lidar com o acaso presente em movimentos como o movimento browniano 🐾.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `Teorema_de_Ito.py`](#2-script-teoremadeitopy)
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

O **Teorema de Itô** é como uma "regra da cadeia com ruído". Ele permite calcular como uma função muda ao longo do tempo quando essa função depende de uma variável que se move de forma incerta, como uma partícula afetada por muitos fatores aleatórios.

### 1.2 Exemplos Práticos

- **Mercado financeiro** 💹: Previsão de preços de ações que variam de forma aleatória.
- **Biologia** 🧬: Modelagem de populações sujeitas a eventos imprevisíveis.
- **Física** ⚛️: Estudo de partículas em suspensão (movimento browniano).
- **Engenharia** ⚙️: Simulação de sinais com ruído.

### 1.3 Explicação Detalhada

O teorema descreve como se calcula a mudança (ou diferencial) de uma função `f(t, X_t)` onde:

- `t` é o tempo ⏱️
- `X_t` é uma variável aleatória que muda com o tempo, como o preço de uma ação 📈

A fórmula, sem símbolos complicados, diz:

```

df = parte do tempo + parte da variação normal + parte do efeito do acaso

```

Essa terceira parte (efeito do acaso) é o que diferencia o Teorema de Itô de uma simples derivada clássica. Ele leva em conta que a incerteza afeta os resultados de forma especial, com mais impacto do que o esperado.

### 1.4 Aplicações

- **Simulações estocásticas**: Onde o futuro é incerto.
- **Finanças quantitativas**: Modelagem de derivativos.
- **Física estatística**: Análise de sistemas caóticos.
- **Machine Learning**: Modelos que lidam com incerteza temporal.

### 1.5 Análise da Tabela

O script mostra como o valor previsto se afasta do valor real à medida que o `x` aumenta. Esse desvio é explicado pela incerteza do modelo e pela simulação aleatória feita com base no teorema.

---

## 2. Script `Teorema_de_Ito.py`

### 2.1 Relação com o Teorema

Este script utiliza conceitos do **Teorema de Itô** para aplicar uma simulação com ruído aleatório sobre uma previsão feita por um modelo simples. A ideia é mostrar como o comportamento de dados reais pode ser influenciado por incertezas, imitando a variação estocástica.

### 2.2 Objetivo do Script

- Prever um valor `y` dado um `x`
- Adicionar ruído inspirado no Teorema de Itô para simular incerteza
- Mostrar os efeitos dessa incerteza em um gráfico e tabela

### 2.3 Exemplo de Saída

```text
      x    y_observado    y_previsto   erro_absoluto
   2048         2683       2912.19         229.19
   4096         5216       6020.23         804.23
   8192        10544      12301.70        1757.70
  16384        26867      25126.23        1740.76
  32768        51510      51821.67         311.67
  65536        95823     109397.97       13574.97
````

### 2.4 Funcionamento Interno

1. **Leitura dos dados** em forma de lista
2. **Ajuste de um polinômio** para prever os valores futuros
3. **Cálculo da simulação com ruído** baseado no Teorema de Itô
4. **Geração de gráfico interativo** usando Plotly
5. **Impressão de tabela comparativa** com os resultados

### 2.5 Tecnologias e Requisitos

* Python 3.8.10+
* Bibliotecas: `numpy`, `pandas`, `scipy`, `plotly`

Instale com:

```bash
pip install numpy pandas scipy plotly
```

Execute com:

```bash
python Teorema_de_Ito.py
```

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### 3.2 Referências

* Wikipedia: [Itô's Lemma](https://en.wikipedia.org/wiki/It%C5%8D%27s_lemma)
* Livro: "Stochastic Calculus for Finance" – Steven Shreve
* Khan Academy e outras fontes didáticas sobre movimento browniano e cálculo estocástico

### 3.3 Testes e Validações

* O script foi testado com Python 3.8.10
* Dados fictícios foram utilizados para validação visual e numérica
* O gráfico interativo permite verificar a adequação do modelo de forma intuitiva

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **Teorema de Itô**: Trata do comportamento de variáveis que mudam ao longo do tempo com influência de fatores aleatórios. Ele é uma versão do "efeito borboleta" com cálculo.
* **Browniano (movimento browniano)**: Movimento aleatório como o de partículas na água, frequentemente usado para modelar incertezas.
* **Variação quadrática**: Modo de medir como algo muda quando está sujeito a incertezas. No mundo estocástico, pequenas variações acumulam efeito rapidamente.
* **Estocástico**: Tudo que envolve *aleatoriedade* ou incerteza.
* **Esperança (esperança matemática)**: É como a média esperada de um resultado.
* **Lambda**: Em matemática, às vezes representa um parâmetro ou valor, mas neste contexto não foi usado.
