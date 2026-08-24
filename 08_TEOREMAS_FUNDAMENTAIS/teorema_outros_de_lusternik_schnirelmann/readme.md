# 🧩 - De Lusternik Schnirelmann

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)

## Frase do Teorema

> O **Teorema de Lusternik-Schnirelmann** afirma que, ao trabalhar com espaços topológicos, pode-se determinar a quantidade mínima de pontos críticos necessários para resolver certos problemas topológicos de otimização. **De forma simplificada**, isso significa que existe uma quantidade mínima de pontos importantes para resolver problemas em espaços complexos.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `teorema_lusternik_schnirelmann.py`](#2-script-lusternik_schnirelmann_theorempy)

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

O **Teorema de Lusternik-Schnirelmann** é uma ferramenta importante para entender como determinar o número mínimo de pontos críticos necessários para a solução de problemas topológicos.

### 1.2 Exemplos Práticos

Imagine um cenário onde estamos tentando otimizar uma função em um espaço complexo. O Teorema de Lusternik-Schnirelmann nos ajuda a entender quantos pontos críticos (pontos de mínimo ou máximo) são necessários para garantir que encontramos a solução ótima.

### 1.3 Explicação Detalhada

O teorema trata de espaços **topológicos** e **funções** definidas nesses espaços. Em palavras simples, um **espaço topológico** pode ser visto como um espaço onde se podem "mover" pontos de diversas formas sem sair do espaço. O teorema se refere ao número mínimo de pontos onde é possível verificar mudanças importantes no comportamento de uma função, como mudanças de direção ou crescimento.

### 1.4 Aplicações

Esse teorema tem aplicações diretas em várias áreas como física, biologia e até em problemas de **otimização computacional**, onde buscamos soluções eficientes para problemas com muitas variáveis.

### 1.5 Análise da Tabela

A tabela fornecida é uma sequência de valores que seguem um padrão de crescimento exponencial, indicando uma relação entre o **Início (2^N)** e o **Fim (2^(N+1)-1)**. O objetivo é aproximar o valor esperado pelo teorema dentro desse intervalo.

---

## 2. Script `teorema_lusternik_schnirelmann.py`

### 2.1 Relação com o Teorema

O script desenvolvido tenta aproximar o valor esperado de acordo com os limites definidos pelo **Teorema de Lusternik-Schnirelmann**. Através da tabela gerada, podemos calcular os valores "Esperados pelo Teorema" como uma média entre o **Início** e o **Fim**.

### 2.2 Objetivo do Script

O objetivo do script é calcular os valores de "Esperado pelo Teorema" com base nos intervalos fornecidos. Esses valores são aproximados dentro do intervalo determinado pelos valores de **Início** (2^N) e **Fim** (2^(N+1) - 1), onde N varia de 0 a 9.

### 2.3 Exemplo de Saída

Ao executar o script, a saída será uma tabela como a seguinte:

```
N   Início (2^N)   Esperado pelo Teorema   Fim (2^(N+1))-1  
0   1               1                       1                
1   2               2                       3                
2   4               5                       7                
3   8               11                      15               
4   16              23                      31               
5   32              47                      63               
6   64              95                      127              
7   128             191                     255              
8   256             383                     511              
9   512             767                     1023             
```

### 2.4 Funcionamento Interno

O script gera os valores com base em uma fórmula simples para calcular o "Esperado pelo Teorema". Ele utiliza os valores de **Início** e **Fim** para determinar um valor intermediário que representa o esperado dentro desse intervalo. A lógica do script é clara e pode ser ajustada caso você deseje aplicar uma fórmula diferente para o cálculo do "Esperado".

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10** ou superior
* Nenhuma biblioteca externa é necessária para o funcionamento básico, mas o **NumPy** pode ser útil para cálculos mais avançados.

---

## 3. Extras

### 3.1 Licença

Este projeto é licenciado sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais informações.

### 3.2 Referências

* [Teorema de Lusternik-Schnirelmann - Wikipedia](https://en.wikipedia.org/wiki/Lusternik%E2%80%93Schnirelmann_theorem)
* [Lei dos Grandes Números - Wikipedia](https://en.wikipedia.org/wiki/Law_of_large_numbers)

### 3.3 Testes e Validações

Todos os cálculos realizados pelo script foram validados em relação aos intervalos apresentados na tabela. Testes adicionais podem ser feitos modificando a lógica de cálculo do "Esperado".

---

## 4. Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Variância**: A variância mede a dispersão de um conjunto de dados. Em termos simples, ela nos diz o quanto os dados variam em torno da média. Quanto maior a variância, maior é a diferença entre os dados.

**Esperança**: A esperança é o valor médio ou esperado de uma variável aleatória. Em termos simples, ela nos diz qual é o valor "esperado" se repetirmos o experimento várias vezes.

**Espaço Topológico**: Um espaço topológico é um conjunto de pontos, onde podemos definir noções de proximidade e continuidade, mas sem exigir uma medida precisa de distância.
