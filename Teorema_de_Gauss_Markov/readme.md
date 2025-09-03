# 📘 - Teorema de Gauss-Markov
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Gauss--Markov-ff69b4.svg)](https://en.wikipedia.org/wiki/Gauss%E2%80%93Markov_theorem)

## Frase do Teorema

> *Dentre todos os estimadores lineares sem viés, o método dos mínimos quadrados fornece o de menor variância.* – Em outras palavras: se você quer prever algo com uma linha e sem fazer suposições erradas, o método dos mínimos quadrados é a forma mais precisa possível.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `Teorema_de_Gauss_Markov.py`](#2-script-teorema_de_gauss_markovpy)
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

O **Teorema de Gauss-Markov** afirma que o método dos **Mínimos Quadrados Ordinários (OLS)** é o melhor estimador possível *dentro da classe dos estimadores lineares e sem viés*.

### 1.2 Exemplos Práticos

- Prever preços de casas com base em tamanho
- Modelar o tempo de entrega de um serviço conforme a distância
- Estimar crescimento populacional com base em anos

### 1.3 Explicação Detalhada

O método OLS busca **ajustar uma curva (ou reta)** que minimiza os **erros quadráticos** entre os valores reais e os previstos. O Teorema garante que, sob certas condições (como dados bem distribuídos e sem erro sistemático), esse ajuste será o melhor possível dentro de sua categoria.

### 1.4 Aplicações

- Econometria
- Regressão linear em aprendizado de máquina
- Engenharia e ciências aplicadas
- Modelos de previsão estatística

### 1.5 Análise da Tabela

O script gera uma tabela com os valores reais (`y_real`) e os valores previstos (`y_pred`) para cada valor de `x`. Essa tabela mostra se o modelo está prevendo bem ou não.

---

## 2. Script `Teorema_de_Gauss_Markov.py`

### 2.1 Relação com o Teorema

Este script aplica o **Teorema de Gauss-Markov** na prática: ele ajusta um modelo polinomial de grau 2 para prever `y` com base em `x`, garantindo o melhor ajuste possível dentro das condições do teorema.

### 2.2 Objetivo do Script

- Aplicar o método dos mínimos quadrados para ajustar um modelo
- Comparar os valores reais de `y` com os previstos
- Fazer uma previsão para `x = 65536` e verificar se é próxima do valor real (95823)
- Exibir os dados em um gráfico interativo

### 2.3 Exemplo de Saída

```
   x     y_real     y_pred
   1          1       -172
   2          3       -171
   4          7       -168
   8          8       -162
  16         21       -150
  32         49       -125
  64         76        -77
 128        224         18
 256        467        210
 512        514        595
1024       1155       1366
2048       2683       2912
4096       5216       6020
8192      10544      12301
16384      26867      25126
32768      51510      51821
65536      95823     109397 (Previsão)
```

### 2.4 Funcionamento Interno

O script segue os seguintes passos:

1. Recebe uma lista de dados no formato `(x, y, z)`.
2. Usa a biblioteca `numpy` para ajustar um polinômio de grau 2 que relaciona `x` e `y`.
3. Aplica o modelo para prever o valor de `y` quando `x = 65536`.
4. Mostra uma tabela comparando os valores reais e previstos.
5. Cria um gráfico interativo com os pontos reais e a curva do modelo usando `plotly`.

### 2.5 Tecnologias e Requisitos

* Python 3.8.10
* Bibliotecas necessárias:
  - `numpy`
  - `plotly`

Instale os pacotes com:

```bash
pip install numpy plotly
````

Execute com:

```bash
python Teorema_de_Gauss_Markov.py
```

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### 3.2 Referências

* Gauss-Markov Theorem — [Wikipedia](https://en.wikipedia.org/wiki/Gauss%E2%80%93Markov_theorem)
* Teoria da Regressão Linear
* Econometria Básica — Gujarati

### 3.3 Testes e Validações

* Verificação manual da curva ajustada
* Comparação visual via gráfico interativo
* Comparação com o valor real de `y` para `x = 65536` (95823)

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

* **Mínimos Quadrados**: técnica para ajustar uma curva minimizando a soma dos quadrados das diferenças entre os valores reais e os previstos.
* **Variância**: medida de quão espalhados estão os valores em torno da média. Quanto menor, mais precisas são as previsões.
* **Estimador**: fórmula ou processo que fornece um valor estimado com base em dados.
* **Insesgado (sem viés)**: um estimador é insesgado quando, em média, acerta o valor verdadeiro.
* **Linear**: refere-se a modelos que usam combinações lineares de variáveis (mesmo que o gráfico final pareça uma curva).
* **BLUE**: sigla para *Best Linear Unbiased Estimator* — o melhor, mais preciso e sem viés dentro dos estimadores lineares.
