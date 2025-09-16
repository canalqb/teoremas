# 📐 - Área do Círculo e Potências de 2

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## Frase do conceito

> A área de um círculo é calculada multiplicando *pi* pelo quadrado do seu raio – isso mostra o espaço dentro do círculo.

---

## Sumário

* [1. Introdução ao conceito](#1-introdução-ao-conceito)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)

* [2. Script `area_do_circulo.py`](#2-script-area_do_circulopy)

  * [2.1 Relação com o conceito](#21-relação-com-o-conceito)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)

* [3 Extras](#3-extras)

  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referências)
  * [3.3 Testes e Validações](#33-testes-e-validações)

* [4 Contato](#4-contato)

* [5. Nota](#5-nota)

---

## 1 Introdução ao conceito

### 1.1 Resumo

Este conceito explica como calcular a área de um círculo, usando o raio, que é a distância do centro até a borda. A fórmula básica é:

**Área = pi \* raio²**

onde **pi** é uma constante aproximada como 3.14.

### 1.2 Exemplos Práticos

Se o raio do círculo for 2, a área será aproximadamente 12.57, pois:

Área = 3.14 \* 2 \* 2 = 12.57

### 1.3 Explicação Detalhada

A área representa o espaço dentro do círculo. Ao elevar o raio ao quadrado, multiplicamos o raio por ele mesmo, depois multiplicamos pelo valor de pi para ajustar essa área à forma circular.

### 1.4 Aplicações

Esse cálculo é usado em várias áreas, como engenharia, arquitetura, design gráfico, e sempre que precisamos entender espaços circulares.

### 1.5 Análise da Tabela

Neste projeto, para cada valor de **n** de 0 a 10:

* Calculamos 2^n (potência de 2),
* Calculamos o número de Mersenne correspondente (2^n - 1),
* Consideramos esses valores como raios de círculos,
* Calculamos as áreas para esses raios.

Assim, vemos como a área cresce rapidamente quando o raio aumenta.

---

## 2 Script `area_do_circulo.py`

### 2.1 Relação com o conceito

O script calcula a área do círculo usando a fórmula mencionada, para diferentes valores de raio baseados em potências de 2 e números de Mersenne.

### 2.2 Objetivo do Script

Mostrar como o espaço dentro de círculos muda quando aumentamos o raio de forma exponencial, incluindo números especiais chamados de Mersenne.

### 2.3 Exemplo de Saída

```
n | 2^n | Mersenne (2^n - 1) | Área com raio 2^n | Área com raio Mersenne
-----------------------------------------------------------------
 0 |    1 |                 0 |             3.14 |                0.00
 1 |    2 |                 1 |            12.57 |                3.14
 2 |    4 |                 3 |            50.27 |               28.27
 3 |    8 |                 7 |           201.06 |              153.94
 4 |   16 |                15 |           804.25 |              706.86
 5 |   32 |                31 |          3216.99 |             3019.07
 6 |   64 |                63 |         12867.96 |            12468.98
 7 |  128 |               127 |         51471.85 |            50670.75
 8 |  256 |               255 |        205887.42 |           204282.06
 9 |  512 |               511 |        823549.66 |           820335.82
10 | 1024 |              1023 |       3294198.66 |          3287767.82
```

### 2.4 Funcionamento Interno

O script:

* Calcula 2^n e 2^n - 1,
* Usa esses valores para definir o raio,
* Calcula a área de cada círculo usando a fórmula da área,
* Imprime os resultados em formato de tabela.

### 2.5 Tecnologias e Requisitos

* Python 3.8.10
* Biblioteca padrão (math para valor de pi)

---

## 3 Extras

### 3.1 Licença

Este projeto está sob a licença MIT — sinta-se livre para usar, modificar e compartilhar.

### 3.2 Referências

* Fórmula da área do círculo: livros básicos de matemática
* Números de Mersenne: números da forma 2^n - 1, importantes em teoria dos números

### 3.3 Testes e Validações

O script foi testado para n de 0 até 10, confirmando que as áreas aumentam de acordo com a fórmula.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **pi**: constante matemática que representa a razão entre a circunferência e o diâmetro de um círculo, aproximadamente 3.14
* **potência de 2**: número obtido ao multiplicar 2 por ele mesmo várias vezes, por exemplo, 2^3 = 2 \* 2 \* 2 = 8
* **número de Mersenne**: número especial da forma 2^n - 1, onde n é um número inteiro; usado em matemática para estudos de números primos
* **raio**: distância do centro de um círculo até sua borda
* **área**: medida da superfície interna de uma forma geométrica
