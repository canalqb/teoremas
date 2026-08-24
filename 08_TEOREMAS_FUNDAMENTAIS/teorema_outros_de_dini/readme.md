# 🧩 - De Dini
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)  

## Frase do Teorema

> Se uma sequência de funções contínuas que diminuem ponto a ponto e convergem para uma função contínua em um intervalo fechado, então essa convergência acontece de forma *uniforme* — ou seja, a diferença entre as funções da sequência e a função limite pode ser controlada para todos os pontos ao mesmo tempo.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `dini.py`](#2-script-dinipy)  
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

Este conceito fala sobre o comportamento de funções que formam uma sequência, onde cada função vai ficando mais próxima da função final, chamada de limite. Quando essa aproximação acontece de forma organizada, decrescente e para todos os pontos do intervalo ao mesmo tempo, dizemos que a convergência é *uniforme*.

### 1.2 Exemplos Práticos

Imagine uma sequência de termômetros que medem a temperatura em vários pontos de uma sala, onde cada novo termômetro melhora a precisão em todos os cantos da sala. A medida que mais termômetros são usados, a leitura fica mais uniforme e próxima da temperatura real.

### 1.3 Explicação Detalhada

Seja uma sequência de funções que são contínuas (sem "buracos" ou "saltos") e que diminuem seu valor em cada ponto conforme o índice cresce. Se essa sequência chega a uma função limite que também é contínua no intervalo fechado, então a diferença entre essas funções e o limite pode ser feita pequena ao mesmo tempo para *todos* os pontos, não apenas para alguns.

### 1.4 Aplicações

Este princípio é importante para garantir que certos métodos matemáticos e numéricos funcionem de forma estável e precisa, como em análise de séries, aproximações em cálculo e na modelagem de fenômenos físicos.

### 1.5 Análise da Tabela

Nas simulações realizadas, observamos que à medida que o índice cresce, as funções da sequência se aproximam cada vez mais da função limite de forma homogênea, o que confirma a uniformidade da convergência prevista.

---

## 2. Script `dini.py`

### 2.1 Relação com o Teorema

O script implementa uma sequência de funções baseadas em potências de 2 no domínio, com uma forma que respeita as condições do conceito, garantindo a convergência uniforme para a função limite.

### 2.2 Objetivo do Script

Visualizar em 3D, com animação, a sequência de funções e a função limite, mostrando como elas se aproximam de forma uniforme e visualmente intuitiva.

### 2.3 Exemplo de Saída

Uma animação onde o eixo X representa valores do domínio em potências de 2 (usando escala logarítmica), o eixo Y mostra o valor das funções, e o eixo Z indica o índice da sequência. A função limite aparece como uma curva fixa, e a sequência animada converge para ela.

### 2.4 Funcionamento Interno

- O domínio é criado como potências de 2, entre 1/32 e 1.  
- Cada função da sequência é definida como raiz quadrada de (x + 1/n).  
- A função limite é raiz quadrada de x.  
- A animação mostra o movimento da sequência convergindo para o limite, com eixos e escalas configurados para evidenciar o comportamento uniforme.

### 2.5 Tecnologias e Requisitos

- Python 3.8.10  
- Bibliotecas: numpy, matplotlib, mpl_toolkits.mplot3d  
- Ambiente gráfico compatível com matplotlib e suporte a animações

---

## 3 Extras

### 3.1 Licença

Este projeto está sob a licença MIT, permitindo uso livre, modificação e distribuição.

### 3.2 Referências

- Wikipedia: [Teorema da Uniformidade de Dini](https://pt.wikipedia.org/wiki/Teorema_da_uniformidade_de_Dini)  
- Documentação matplotlib: https://matplotlib.org/  
- Numpy: https://numpy.org/

### 3.3 Testes e Validações

Foram realizados testes para garantir que a convergência exibida no gráfico é uniforme, conforme esperado pelo conceito, utilizando diversos valores e verificando o erro máximo.

---

## 4 Contato

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Função contínua**: função sem interrupções ou saltos no intervalo analisado.

**Convergência pontual**: para cada ponto do domínio, a sequência de funções chega cada vez mais perto da função limite.

**Convergência uniforme**: a sequência de funções se aproxima da função limite ao mesmo tempo para *todos* os pontos do domínio.

**Intervalo fechado**: conjunto de pontos entre dois valores, incluindo os extremos.

**Raiz quadrada**: operação matemática que, para um número positivo, retorna outro número que multiplicado por ele mesmo dá o número original. 
