# 🧩 - De Girsanov
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Girsanov-ff69b4.svg)](https://en.wikipedia.org/wiki/Girsanov_theorem)

## Frase do Teorema

> *Se mudarmos o ponto de vista sobre a aleatoriedade de um processo, podemos ajustar sua tendência como se estivéssemos "mudando o mundo".* – Em outras palavras: com o Teorema de Girsanov, é possível transformar um processo aleatório com uma certa tendência (ou direção) em outro com comportamento diferente, o que é muito útil para simulações e previsões.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `Teorema_de_Girsanov.py`](#2-script-teorema_de_girsanovpy)
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

O **Teorema de Girsanov** permite simular diferentes cenários de processos aleatórios, mudando a *maneira como vemos o acaso*. Ele é muito usado para criar **modelos financeiros e físicos mais realistas**, especialmente quando queremos incluir ou remover tendências de comportamento ao longo do tempo.

### 1.2 Exemplos Práticos

- Simular o preço de uma ação em mercados com diferentes níveis de risco
- Representar partículas em movimento afetadas por campos externos
- Gerar múltiplos futuros possíveis em previsões econômicas

### 1.3 Explicação Detalhada

Normalmente, usamos processos aleatórios que se comportam de forma neutra (sem tendência). O Teorema de Girsanov mostra como mudar a **distribuição de probabilidade** de tal processo para simular cenários com outra tendência ou direção. É como *mudar a regra do jogo, mantendo os dados base*.

### 1.4 Aplicações

- Finanças quantitativas
- Modelos climáticos e físicos
- Inteligência artificial para jogos de simulação
- Engenharia de sistemas estocásticos

### 1.5 Análise da Tabela

O script utiliza uma tabela com dados do tipo `(x, y, z)`, onde:

- `x` e `z` crescem como potências de 2
- `y` cresce de forma mais "natural", com oscilações realistas

A previsão do valor `y` para `x = 65536` é feita com base nesse padrão, com e sem ruído estocástico.

---

## 2. Script `Teorema_de_Girsanov.py`

### 2.1 Relação com o Teorema

Este script aplica o conceito do Teorema de Girsanov de forma adaptada e acessível: **simulando incertezas** sobre uma previsão polinomial feita com base em dados reais, e adicionando variações aleatórias controladas.

### 2.2 Objetivo do Script

- Ajustar um modelo polinomial de grau 2 para prever `y` com base em `x`
- Realizar **1000 simulações estocásticas**, refletindo diferentes possíveis resultados
- Mostrar a previsão para `x = 65536` com e sem ruído
- Exibir os dados reais, previstos e simulados em um **gráfico interativo**

### 2.3 Exemplo de Saída

```

Tabela de comparação:
x      y      z
0      1      1      1
1      2      3      3
2      4      7      7
...
15  32768  51510  65535
```
Previsão do modelo para x=65536: y = 94012
Valor real conhecido: y = 95823


### 2.4 Funcionamento Interno

1. O script recebe dados no formato `(x, y, z)`
2. Ajusta um polinômio de grau 2 com `numpy`
3. Simula 1000 valores para `x = 65536`, adicionando ruído com `numpy.random.normal`
4. Mostra:
   - A previsão média
   - O desvio (grau de incerteza)
   - Um gráfico interativo com todos os resultados

### 2.5 Tecnologias e Requisitos

* Python 3.8.10
* Bibliotecas necessárias:
  - `numpy`
  - `pandas`
  - `scikit-learn`
  - `plotly`

Instale as dependências com:

```bash
pip install numpy pandas scikit-learn plotly
````

Execute com:

```bash
python Teorema_de_Girsanov.py
```

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a Licença MIT. Sinta-se livre para usar, modificar e distribuir com os devidos créditos.

### 3.2 Referências

* [Teorema de Girsanov – Wikipedia](https://en.wikipedia.org/wiki/Girsanov_theorem)
* Livro: Stochastic Calculus for Finance – Steven Shreve
* Simulações estocásticas – Khan Academy e Coursera

### 3.3 Testes e Validações

* Verificação da curva polinomial ajustada visualmente
* Comparação entre `y_pred` e `y_real`
* Simulações estocásticas repetidas com estatísticas (média e desvio)

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

📘 **Glossário de termos técnicos usados neste projeto:**

* **Estocástico**: significa aleatório, ou seja, com incertezas naturais.
* **Ruído Gaussiano**: pequenas variações geradas por sorteios aleatórios com base em uma distribuição parecida com o "sino da normal".
* **Drift (tendência)**: direção média que um processo segue ao longo do tempo.
* **Medida de probabilidade**: conjunto de regras que determina a chance de cada resultado acontecer.
* **Simulação**: processo de testar várias possibilidades para entender o comportamento de um sistema.
* **Distribuição normal**: tipo de sorteio onde valores próximos da média são mais prováveis.
* **Desvio padrão**: quanto os resultados variam, em média, em relação à média geral. 
