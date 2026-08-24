# 🧩 - De Maximum Modulus
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  

## Frase do Teorema

> "O maior valor do módulo de uma função analítica ocorre nas bordas do intervalo considerado" – Isso quer dizer que, para funções do tipo que estamos estudando, o valor máximo da função dentro de um intervalo não vai aparecer no meio, mas sempre perto das extremidades.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `MaximoModulo.py`](#2-script-maximomodulopy)  
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
Esse princípio básico de funções analíticas diz que o ponto onde a função atinge seu maior valor absoluto em um intervalo ocorre na borda, nunca no meio.

### 1.2 Exemplos Práticos  
Se você olhar para a função f(z) = z² nos intervalos criados a partir das potências de 2 e dos números de Mersenne, o maior valor de f(z) vai estar sempre no limite direito do intervalo.

### 1.3 Explicação Detalhada  
Quando estudamos funções que podem ser representadas por séries ou integrais (funções analíticas), elas têm um comportamento especial que impede que o valor máximo de seu módulo apareça no meio do caminho dentro de um intervalo aberto. Por isso, só nos extremos esse máximo pode ocorrer.

### 1.4 Aplicações  
Essa propriedade é importante em várias áreas da matemática, como análise complexa, e na física, onde permite saber que valores máximos de certas funções só ocorrem nas "fronteiras" dos sistemas estudados.

### 1.5 Análise da Tabela  
Os valores calculados mostram que para cada intervalo entre potências de 2 e os números de Mersenne, o valor máximo da função f(z) = z² ocorre sempre na borda direita do intervalo, confirmando a ideia acima.

---

## 2. Script `MaximoModulo.py`

### 2.1 Relação com o Teorema  
O script serve para calcular e visualizar o comportamento da função f(z) = z² nos intervalos formados por potências de 2 e números de Mersenne, evidenciando que o maior valor ocorre nas bordas.

### 2.2 Objetivo do Script  
- Gerar intervalos entre potências de 2 e números de Mersenne.  
- Calcular o valor da função no início e fim desses intervalos.  
- Encontrar o valor máximo da função dentro do intervalo.  
- Mostrar que o máximo acontece sempre nas bordas.  
- Exibir gráfico com esses dados.

### 2.3 Exemplo de Saída  
```

## Intervalo            |f(start)|   |f(end)|   Máx |f(z)|  Ponto máx

\[   2, 3   ]       4.00       9.00         9.00       3.00
\[   4, 7   ]      16.00      49.00        49.00       7.00
\[   8, 15  ]      64.00     225.00       225.00      15.00
\[  16, 31  ]     256.00     961.00       961.00      31.00
\[  32, 63  ]    1024.00    3969.00      3969.00      63.00
\[  64, 127 ]    4096.00   16129.00     16129.00     127.00
\[ 128, 255 ]   16384.00   65025.00     65025.00     255.00
\[ 256, 511 ]   65536.00  261121.00    261121.00     511.00
\[ 512, 1023]  262144.00 1046529.00   1046529.00    1023.00

```

### 2.4 Funcionamento Interno  
O script calcula potências de 2 e números de Mersenne, cria intervalos e avalia a função f(z) = z² nesses intervalos para encontrar máximos absolutos, que ocorrem nas bordas.

### 2.5 Tecnologias e Requisitos  
- Python 3.8.10  
- Bibliotecas: numpy, matplotlib  

---

## 3 Extras

### 3.1 Licença  
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.

### 3.2 Referências  
- [Funções Analíticas e Análise Complexa](https://pt.wikipedia.org/wiki/An%C3%A1lise_complexa)  
- [Números de Mersenne](https://pt.wikipedia.org/wiki/N%C3%BAmero_de_Mersenne)  

### 3.3 Testes e Validações  
Os testes foram feitos com os valores gerados para os intervalos definidos, mostrando sempre o máximo na borda direita.

---

## 4 Contato

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Analítica:** função que pode ser representada por uma soma infinita de potências e é suave, sem pontos angulosos ou descontinuidades.  
**Módulo:** valor absoluto de um número complexo, que indica sua distância da origem no plano.  
**Potências de 2:** números da forma 2 elevado a n, onde n é um número inteiro positivo.  
**Números de Mersenne:** números da forma 2^n - 1, importantes em teoria dos números.  
**Intervalo:** conjunto de números entre dois valores definidos, por exemplo, entre 2 e 3.  
**Função crescente:** função que aumenta seu valor conforme o argumento cresce.  
**Borda:** limite externo de um intervalo, onde começam ou terminam os valores analisados.  
**Máximo:** maior valor que uma função assume em um intervalo ou conjunto.  
**Script:** programa de computador escrito para executar uma tarefa específica.  
**Bibliotecas:** coleções de funções prontas que ajudam a programar mais rápido.
