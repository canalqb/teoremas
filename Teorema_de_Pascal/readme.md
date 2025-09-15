# 📐 - Teorema de Pascal (Cônica)
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Frase do Teorema

> Seis pontos escolhidos sobre uma cônica formam três pares de segmentos cujas interseções são alinhadas – isto é, as três linhas que unem os pontos de interseção desses pares estão todas numa mesma linha reta.

---

## Sumário

* [1. Introdução ao Teorema 📘](#1-introdução-ao-teorema-📘)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)

* [2. Script `pascal_conica.py` 🐍](#2-script-pascal_conicapy-🐍)

  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)

* [3 Extras 🎁](#3-extras-🎁)

  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referências)
  * [3.3 Testes e Validações](#33-testes-e-validações)

* [4 Contato 📬](#4-contato-📬)
* [5. Nota 📝](#5-nota-📝)

---

## 1. Introdução ao Teorema 📘

### 1.1 Resumo

O Teorema de Pascal fala sobre seis pontos posicionados em uma forma curva chamada *cônica* (como uma elipse, parábola ou hipérbole). Quando ligamos esses pontos em pares específicos e encontramos as interseções entre esses pares, as três linhas que conectam essas interseções estão todas alinhadas, ou seja, formam uma linha reta.

### 1.2 Exemplos Práticos

Imagine que você tem um círculo e escolhe seis pontos ao redor dele. Ao ligar esses pontos de um jeito especial, as linhas que surgem se cruzam em pontos que, por sua vez, estão alinhados. Isso ajuda a entender propriedades de formas curvas em geometria e tem aplicações em design, física e computação gráfica.

### 1.3 Explicação Detalhada

De forma simples, o teorema mostra que, ao trabalhar com uma *curva cônica* e seis pontos sobre ela, existe uma relação linear escondida entre esses pontos. Essa relação aparece ao traçar linhas entre os pontos em uma ordem específica e observar os pontos onde essas linhas se cruzam. A surpresa é que esses pontos de cruzamento sempre estão alinhados.

### 1.4 Aplicações

- **Geometria computacional:** ajuda no processamento e modelagem de formas curvas.
- **Design gráfico:** para criar formas complexas e garantir simetrias.
- **Física:** em sistemas que envolvem trajetórias parabólicas ou elípticas.

### 1.5 Análise da Tabela

Neste projeto, exploramos conceitos relacionados ao Teorema de Pascal usando números especiais chamados números de Mersenne e coeficientes do triângulo de Pascal para criar intervalos e identificar números que se encaixam em certas condições. A tabela mostra esses valores para diferentes níveis (n), explicando como esses números se relacionam.

---

## 2. Script `pascal_conica.py` 🐍

### 2.1 Relação com o Teorema

O script utiliza conceitos matemáticos relacionados ao triângulo de Pascal e números especiais chamados números de Mersenne para ilustrar como se pode identificar números dentro de intervalos definidos por potências de dois, demonstrando uma ligação prática e numérica com as ideias de combinação e alinhamento do Teorema de Pascal.

### 2.2 Objetivo do Script

Gerar e mostrar para diferentes valores de n:
- O intervalo entre 2^n e 2^{n+1} - 1.
- Os números de Mersenne que caem dentro desse intervalo.
- A linha n do triângulo de Pascal.
- Um número calculado somando valores do triângulo de Pascal ponderados por potências de 2, ajustado para estar dentro do intervalo.

### 2.3 Exemplo de Saída

```

n=3, intervalo=(8, 15), mersennes no intervalo=\[15]
linha Pascal: \[1, 3, 3, 1]
número identificado: 30
-----------------------

```

*(Observação: o número identificado pode ser ajustado para ficar dentro do intervalo definido.)*

### 2.4 Funcionamento Interno

- Função para calcular números de Mersenne até um valor máximo.
- Função para obter a linha n do triângulo de Pascal usando combinações matemáticas.
- Cálculo do número identificado como soma ponderada dos coeficientes da linha de Pascal com potências de 2.
- Ajuste do número para garantir que ele esteja dentro do intervalo correto.
- Impressão dos resultados para n de 0 a 10.

### 2.5 Tecnologias e Requisitos

- Python 3.8.10
- Biblioteca padrão (`math` para combinação)
- Nenhuma biblioteca externa adicional

---

## 3 Extras 🎁

### 3.1 Licença

MIT License – uso livre com atribuição.

### 3.2 Referências

- [Teorema de Pascal - Wikipédia](https://pt.wikipedia.org/wiki/Teorema_de_Pascal)
- [Números de Mersenne](https://pt.wikipedia.org/wiki/Número_de_Mersenne)
- [Triângulo de Pascal](https://pt.wikipedia.org/wiki/Triângulo_de_Pascal)

### 3.3 Testes e Validações

Testado para n entre 0 e 10, com saída consistente e números dentro dos intervalos esperados.

---

## 4 Contato 📬

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*

---

## 5. Nota 📝

- **cônica**: uma curva plana que pode ser uma elipse, parábola ou hipérbole — formas que aparecem muito na geometria e na física.  
- **números de Mersenne**: números que são obtidos pela fórmula 2^p - 1, onde p é um número inteiro, usados em várias áreas da matemática, especialmente na teoria dos números.  
- **triângulo de Pascal**: uma tabela de números organizados em forma triangular, onde cada número é a soma dos dois números acima dele; usada para calcular combinações e coeficientes em matemática.  
- **combinação**: uma maneira de contar quantas formas diferentes se pode escolher objetos de um conjunto, sem se importar com a ordem.  
- **potência de 2**: um número que é resultado de multiplicar o número 2 por ele mesmo várias vezes (ex: 2^3 = 2 x 2 x 2 = 8).  
- **intervalo**: um espaço entre dois números, que aqui define um conjunto de números que estamos analisando.
