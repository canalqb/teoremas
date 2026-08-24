# 🧩 - De Desargues

[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Frase do Conceito

> "Se dois triângulos estão em perspectiva a partir de um ponto, então eles também estão em perspectiva a partir de uma linha." – Em outras palavras, o Teorema de Desargues mostra uma relação especial entre dois triângulos que estão "alinhados" de uma forma particular, conectando pontos e linhas de maneira única.

## Sumário

* [1. Introdução ao Conceito 📘](#1-introdução-ao-conceito-📘)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `intervalos_desargues.py` 🐍](#2-script-intervalos_desarguespy-🐍)

  * [2.1 Relação com o Conceito](#21-relação-com-o-conceito)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3. Extras 🎁](#3-extras-🎁)

  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referencias)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4. Contato 📬](#4-contato-📬)
* [5. Nota 📝](#5-nota-📝)

---

## 1. Introdução ao Conceito 📘

### 1.1 Resumo

O conceito abordado relaciona a ideia do Teorema de Desargues, que fala sobre como dois triângulos podem ser relacionados via pontos e linhas. A partir disso, exploramos intervalos numéricos que crescem de forma exponencial (base 2), que formam sequências contínuas e não se sobrepõem, trazendo uma maneira de visualizar conceitos matemáticos de forma simples.

### 1.2 Exemplos Práticos

O script gera intervalos de números que começam em 2 elevado a n e terminam em um valor um pouco menor que 2 elevado a (n+1). Por exemplo:

- Para n = 0, o intervalo é [1, 1]
- Para n = 1, o intervalo é [2, 3]
- Para n = 2, o intervalo é [4, 7]

E assim por diante, até n = 10.

### 1.3 Explicação Detalhada

Cada intervalo é definido por potências de dois, formando blocos consecutivos que não se sobrepõem. Entre esses blocos, identificamos pontos de cruzamento, que são os números que fazem a transição de um intervalo para outro, ou seja, o último número de um intervalo e o primeiro número do próximo são vizinhos.

O script calcula também o ponto médio de todos os intervalos juntos — o número que está no meio do menor e maior valor entre todos os intervalos — e lista valores próximos a números especiais chamados números de Mersenne, que são valores da forma 2 elevado a n menos 1 (como 3, 7, 15, etc).

### 1.4 Aplicações

Essas estruturas e análises podem ser usadas para:

- Entender distribuições e sequências numéricas de forma intuitiva
- Estudar propriedades matemáticas ligadas à geometria e à aritmética
- Visualizar conceitos abstratos, como o que está por trás do Teorema de Desargues, por meio de sequências numéricas e suas relações

### 1.5 Análise da Tabela

O script gera uma tabela com os intervalos e seus pontos internos, detalhando os pontos médios e os valores próximos a números de Mersenne, que ajudam a identificar padrões e relações entre os números.

---

## 2. Script `intervalos_desargues.py` 🐍

### 2.1 Relação com o Conceito

Este script utiliza a ideia de intervalos crescentes baseados em potências de dois para ilustrar uma relação de "perspectiva" numérica, inspirada na analogia geométrica do Teorema de Desargues.

### 2.2 Objetivo do Script

- Gerar intervalos numéricos específicos e consecutivos
- Verificar se os intervalos se sobrepõem (eles não se sobrepõem)
- Calcular o ponto médio dos extremos desses intervalos
- Criar uma sequência contínua que inclui todos os números entre os limites dos intervalos
- Identificar pontos de cruzamento entre intervalos consecutivos
- Listar pontos internos e próximos aos números especiais de Mersenne dentro de cada intervalo

### 2.3 Exemplo de Saída

```plaintext
Intervalos gerados:
n=0: [1, 1]
n=1: [2, 3]
n=2: [4, 7]
n=3: [8, 15]
n=4: [16, 31]
n=5: [32, 63]
n=6: [64, 127]
n=7: [128, 255]
n=8: [256, 511]
n=9: [512, 1023]
n=10: [1024, 2047]

Não há intervalos que se sobrepõem.

Ponto médio entre os extremos de todos os intervalos: 1024.0

Sequência contínua gerada (de 1 a 2047), total de 2047 números.

Pontos de cruzamento entre intervalos consecutivos:
Ponto entre 1 e 2
Ponto entre 3 e 4
Ponto entre 7 e 8
...
````

### 2.4 Funcionamento Interno

O script está dividido em funções que:

* Geram intervalos baseados em potências de dois
* Listam esses intervalos no console
* Verificam se algum intervalo se cruza com outro
* Calculam o ponto médio entre o menor e maior número de todos os intervalos
* Criam uma sequência contínua de números entre o menor e maior extremos
* Identificam pontos onde intervalos consecutivos se tocam
* Calculam pontos médios internos e variações próximas aos números de Mersenne dentro dos intervalos

### 2.5 Tecnologias e Requisitos

* Python 3.8.10
* Nenhuma biblioteca externa necessária, apenas funções básicas do Python

---

## 3. Extras 🎁

### 3.1 Licença

Este projeto está licenciado sob a licença MIT.

### 3.2 Referências

* Teorema de Desargues – Wikipédia: [https://pt.wikipedia.org/wiki/Teorema\_de\_Desargues](https://pt.wikipedia.org/wiki/Teorema_de_Desargues)
* Números de Mersenne – Wikipédia: [https://pt.wikipedia.org/wiki/Número\_de\_Mersenne](https://pt.wikipedia.org/wiki/Número_de_Mersenne)

### 3.3 Testes e Validações

Foram testados intervalos até n=10 e verificada a não sobreposição, além do cálculo correto dos pontos médios e dos pontos especiais dentro dos intervalos.

---

## 4. Contato 📬

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota 📝

**λ (lambda):** Símbolo usado para representar valores que podem variar. Aqui, não usamos diretamente, mas se aparecer, pense nele como um número qualquer.

**Variância:** Medida de quanto os valores em um conjunto se espalham em torno da média. É um jeito de medir a "dispersão" dos dados.

**Esperança (média):** É o valor esperado, ou seja, o valor médio que se espera encontrar em um conjunto de dados ou num experimento aleatório.

**Número de Mersenne:** Número especial da forma "dois elevado a n menos um" (por exemplo, 3, 7, 15), usados em matemática para vários estudos, inclusive sobre primos.

**Ponto médio:** É o número que fica exatamente no meio entre dois números, somando-os e dividindo por dois.
