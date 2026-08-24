# 🧩 - De Black Scholes
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![LGN](https://img.shields.io/badge/Teorema-Black--Scholes-ff69b4.svg)](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model)

## Frase do Teorema

> *A fórmula de Black–Scholes permite calcular o preço justo de uma opção financeira com base na variabilidade do ativo subjacente.* – Em linguagem simples: com essa fórmula, podemos prever o valor de contratos no mercado mesmo com incerteza.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `Teorema_de_Black_Scholes.py`](#2-script-teorema_de_black_scholespy)
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
O **Teorema de Black–Scholes** é um modelo matemático que revolucionou o mundo das finanças. Ele permite **prever o preço de opções**, ou seja, contratos que dão o direito (mas não a obrigação) de comprar ou vender ativos no futuro.

### 1.2 Exemplos Práticos  
- Quanto vale uma opção para comprar ações da Apple daqui a 30 dias?  
- Qual o impacto da **volatilidade** no preço de uma opção?  
- Como prever tendências mesmo sem saber o futuro?

### 1.3 Explicação Detalhada  
Este projeto **não implementa a fórmula clássica do teorema** (que usa distribuição normal e conceitos mais complexos), mas **se inspira na ideia central**: modelar dados financeiros por meio de funções que capturam o crescimento, a incerteza e a tendência.

Aqui, modelamos os dados com a seguinte fórmula empírica:

```
y = a \* x^b + c
```


Onde:
- `x` representa a variável independente (por exemplo, tempo)
- `y` é a variável observada (por exemplo, valor de um ativo)
- `a`, `b` e `c` são parâmetros ajustados automaticamente

### 1.4 Aplicações  
- Previsão de valores futuros com base em padrões passados  
- Análise de crescimento não linear  
- Visualização de ajuste de curvas em dados reais  
- Educação financeira com foco em modelagem de incertezas

### 1.5 Análise da Tabela  
O script imprime uma tabela que compara valores reais com os valores previstos, e também exibe uma **previsão futura** para o próximo valor de `x` (como por exemplo `x = 65536`), com base no modelo ajustado.

---

## 2. Script `Teorema_de_Black_Scholes.py`

### 2.1 Relação com o Teorema  
Apesar de não usar a fórmula completa do modelo original, o script **carrega a essência do Teorema de Black–Scholes**: prever o valor de algo com base em padrões observados anteriormente, mesmo com incertezas.

### 2.2 Objetivo do Script  
- Modelar uma sequência de pontos `x, y` que crescem segundo potências de 2  
- Ajustar uma **função matemática do tipo potência** para descrever os dados  
- Prever o próximo valor  
- Exibir os resultados em uma tabela e em um gráfico interativo

### 2.3 Exemplo de Saída  

```text
Tabela comparando valores reais e previstos:
-------------------------------------------
x = 256 | y real = 259 | y previsto = 261.34
x = 512 | y real = 515 | y previsto = 520.89

Previsão para x = 65536 -> y previsto = 65501.27
````

Além disso, um **gráfico interativo** é exibido, mostrando os pontos reais, a curva ajustada e a previsão.

### 2.4 Funcionamento Interno

1. Os dados `x` e `y` são fornecidos com `x` em potências de 2
2. O modelo tenta ajustar `y = a * x^b + c` aos dados usando um otimizador do `scipy`
3. Uma previsão é feita para o próximo `x` da sequência (ex: 65536)
4. O gráfico é gerado com `plotly` e exibido no navegador

### 2.5 Tecnologias e Requisitos

**Tecnologias**:

* Python 3.8.10
* Bibliotecas: `numpy`, `scipy`, `plotly`

**Instalação das dependências**:

```bash
pip install numpy scipy plotly
```

**Execução**:

```bash
python Teorema_de_Black_Scholes.py
```

---

## 3 Extras

### 3.1 Licença

Este projeto está sob a licença **MIT**, permitindo uso, modificação e compartilhamento com liberdade.

### 3.2 Referências

* Teorema de Black–Scholes original (modelo financeiro)
* Modelagem com funções potenciais
* Ajuste de curva com `curve_fit`
* Visualização com `plotly`

### 3.3 Testes e Validações

* O modelo é validado visualmente no gráfico
* A previsão numérica é comparável com o padrão de crescimento
* Resultados consistentes mesmo com pequenos ruídos nos dados

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Volatilidade:** O quanto um valor varia com o tempo. Por exemplo, se o preço de uma ação sobe e desce muito, dizemos que ela é volátil.

**Valor esperado:** Uma média ponderada de resultados possíveis.

**Previsão:** Tentativa de estimar o que vai acontecer no futuro com base em dados anteriores.

**Ajuste de curva:** Processo de encontrar uma fórmula que se encaixe bem aos dados.

**Função potencial (ou potência):** Uma fórmula como `y = a * x^b + c`, onde `x` cresce e `y` acompanha de forma não linear.

**Modelo empírico:** Um modelo baseado na observação de dados, e não em teoria pura.
