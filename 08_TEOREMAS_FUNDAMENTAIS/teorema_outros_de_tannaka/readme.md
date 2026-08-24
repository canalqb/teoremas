# 🧩 - De Tannaka
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)  

## Frase do Teorema

> O Teorema de Tannaka diz que é possível reconstruir um grupo a partir das suas representações lineares – ou seja, a estrutura do grupo está nas transformações que ele permite.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `tannaka_trace.py`](#2-script-tannaka_tracepy)
  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3. Extras](#3-extras)
  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referencias)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4. Contato](#4-contato)
* [5. Nota](#5-nota)

---

## 1. Introdução ao Teorema

### 1.1 Resumo

O **Teorema de Tannaka** estabelece que é possível entender completamente um grupo conhecendo só as suas representações lineares, ou seja, as formas como ele pode agir transformando objetos.

### 1.2 Exemplos Práticos

Se você souber todas as maneiras que um conjunto de simetrias pode modificar vetores, poderá descobrir toda a estrutura desse conjunto de simetrias.

### 1.3 Explicação Detalhada

Grupos são conjuntos que descrevem simetrias e operações. O teorema mostra que, ao analisar como essas simetrias transformam espaços vetoriais, pode-se reconstruir o grupo original. Isso torna o estudo dos grupos mais simples ao focar em suas representações.

### 1.4 Aplicações

* Teoria dos grupos compactos  
* Física teórica, como em simetrias de partículas  
* Álgebra abstrata  
* Inspiração para modelagem matemática de dados reais  

### 1.5 Análise da Tabela

O script compara os valores reais da série chamada “procurapeloteorema” com os valores estimados pela função ajustada, mostrando o quanto a modelagem representa o comportamento da série.

---

## 2. Script `tannaka_trace.py`

### 2.1 Relação com o Teorema

Embora o teorema original seja abstrato e teórico, este projeto se inspira nele para modelar dados reais com uma função que combina potências de 2 e termos lineares, ilustrando a ideia de entender estruturas complexas por representações simples.

### 2.2 Objetivo do Script

Ajustar uma função do tipo:

f(n) = a * 2^n + b * n + c

onde n é o logaritmo base 2 de x, para aproximar os dados reais da série “procurapeloteorema”.

### 2.3 Exemplo de Saída

O script exibe no terminal uma tabela comparando valores reais e estimados, e gera um gráfico com escala logarítmica em base 2 para facilitar a visualização.

### 2.4 Funcionamento Interno

* Recebe dados reais (valores da série)  
* Calcula n = log base 2 de cada valor x  
* Usa regressão linear para encontrar os coeficientes a, b e c que melhor ajustam a função f(n) aos dados  
* Exibe resultados no terminal e plota gráfico para análise visual  

### 2.5 Tecnologias e Requisitos

* Python 3.8.10  
* Bibliotecas: numpy, matplotlib  

---

## 3. Extras

### 3.1 Licença

Projeto sob licença MIT — veja o arquivo LICENSE para detalhes.

### 3.2 Referências

* Wikipédia: Teorema de Tannaka  
* Documentação das bibliotecas numpy e matplotlib  

### 3.3 Testes e Validações

Validação feita pela comparação entre valores reais e estimados e pela análise visual do gráfico gerado.

---

## 4. Contato

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**logaritmo base 2:** função que responde quantas vezes você precisa dividir um número por 2 até chegar a 1.  

**regressão linear:** método matemático para encontrar a melhor linha ou função que aproxima um conjunto de dados.  

**função exponencial 2^n:** função que cresce muito rápido, dobrando seu valor cada vez que n aumenta em 1.  

**coeficientes a, b e c:** números que ajustam a função para que ela se aproxime o máximo possível dos dados reais.  

**série "procurapeloteorema":** sequência de números reais usados como base para o ajuste e comparação da função.   
