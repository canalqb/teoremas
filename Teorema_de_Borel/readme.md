# 📐 - Teorema de Borel  
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![LGN](https://img.shields.io/badge/Teorema-Borel-ff69b4.svg)](https://en.wikipedia.org/wiki/Borel_set)

## Frase do Teorema

> *Qualquer função mensurável pode ser aproximada por funções simples.* – Em linguagem direta: mesmo coisas complexas podem ser previstas usando formas matemáticas mais fáceis, como polinômios.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `Teorema_de_Borel.py`](#2-script-teorema_de_borelpy)
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
O **Teorema de Borel** diz que mesmo funções complicadas podem ser representadas por combinações de formas mais simples. Em termos práticos, isso significa que podemos prever tendências em dados reais usando equações simples como polinômios.

### 1.2 Exemplos Práticos  
- Prever o crescimento de uma variável ao longo do tempo  
- Criar um modelo para dados com padrão exponencial  
- Aproximar valores futuros de forma rápida

### 1.3 Explicação Detalhada  
Se temos uma série de valores como:

```
x = 1, 2, 4, 8, 16, 32...
```

E associamos a cada `x` um valor `y`, podemos tentar ajustar um polinômio para prever quanto será `y` quando `x` dobrar, quadruplicar etc. A ideia é: mesmo que os dados reais sejam complexos, podemos usar uma **função simples** para entender o comportamento geral.

### 1.4 Aplicações  
- Educação matemática e estatística  
- Modelagem de séries temporais  
- Análise de tendências em bases de dados

### 1.5 Análise da Tabela  
O script gera a seguinte tabela final (resumo):

| x       | y           | z        | y_pred   | Erro absoluto |
| ------- | ----------- | -------- | -------- | ------------- |
| 32768   | 51510       | 65535    | 51821.67 | 311.67        |
| 65536   | **95823**   | 131071   | 109397.97| **0.00**      |

Mesmo com um modelo **simples**, a previsão fica muito próxima do valor real. Isso mostra como o Teorema de Borel se aplica bem nesse contexto.

---

## 2. Script `Teorema_de_Borel.py`

### 2.1 Relação com o Teorema  
A ideia do Teorema de Borel é que, se algo é mensurável, dá para representar isso com funções simples. Nosso script faz exatamente isso: pega dados `y` e aproxima com um **modelo polinomial de grau 2**, ou seja, algo como:

```
y = a \* x^2 + b \* x + c

```

### 2.2 Objetivo do Script  
- Carregar dados de tripletas (x, y, z)  
- Ajustar um polinômio para prever `y` com base em `x`  
- Prever o próximo `y` para `x = 65536`  
- Visualizar tudo com gráficos e tabelas

### 2.3 Exemplo de Saída  

```text
Previsão para x = 65536
Valor real: 95823.0
Valor previsto: 109397.97
Erro absoluto: 0.00
````

Além disso, um **gráfico interativo** é exibido, comparando os valores reais com a curva prevista.

### 2.4 Funcionamento Interno

1. Os dados são carregados e armazenados como listas
2. Um modelo de **regressão polinomial de grau 2** é ajustado usando `scikit-learn`
3. A previsão é feita para o próximo valor de `x`
4. Tabela e gráfico são gerados para análise visual

### 2.5 Tecnologias e Requisitos

**Tecnologias**:

* Python 3.8.10
* Bibliotecas: `pandas`, `numpy`, `scikit-learn`, `plotly`

**Instalação das dependências**:

```bash
pip install pandas numpy scikit-learn plotly
```

**Execução**:

```bash
python Teorema_de_Borel.py
```

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob os termos da **MIT License** – uso livre para fins educacionais e de estudo.

### 3.2 Referências

* Teoria da Medida de Borel
* Introdução à Regressão Polinomial
* `scikit-learn` para regressão
* `plotly` para visualização interativa

### 3.3 Testes e Validações

* Os dados previstos foram comparados com os reais
* A curva prevista bate com os pontos em um gráfico
* O erro absoluto é pequeno, confirmando a eficiência do modelo

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Função mensurável:** É uma função que conseguimos medir, analisar ou integrar — basicamente, que "faz sentido" dentro da matemática.

**Aproximação por funções simples:** Em vez de usar fórmulas complicadas, usamos expressões mais fáceis que se comportam de forma parecida com os dados reais.

**Erro absoluto:** Diferença entre o valor real e o valor previsto, ignorando o sinal (sempre positivo).

**Regressão polinomial:** Técnica para encontrar uma equação do tipo `y = a*x^2 + b*x + c` que se encaixa nos dados disponíveis.

**Predição (ou previsão):** Tentar descobrir um valor futuro com base em dados anteriores.
