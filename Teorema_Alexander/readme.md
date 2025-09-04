# 🧮 - Teorema Alexander

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Frase do Teorema

> "Para cada número N, existe um intervalo crescente definido por potências de 2, dentro do qual um valor esperado pode ser aproximado pela soma de números especiais que crescem exponencialmente." – Em outras palavras, conforme aumentamos N, a contagem ou valor esperado cresce dentro do intervalo definido por 2 elevado a N até 2 elevado a N+1 menos 1, de forma organizada e previsível.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `teorema_alexander.py`](#2-script-teorema_alexanderpy)

  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3. Extras](#3-extras)

  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referências)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4. Contato](#4-contato)
* [5. Nota](#5-nota)

---

## 1. Introdução ao Teorema

### 1.1 Resumo

Este conceito mostra como podemos organizar números em intervalos definidos pelas potências de 2, e calcular um valor esperado para cada intervalo usando somas de números que crescem de forma específica, chamados números de Mersenne. Isso ajuda a entender padrões de crescimento e distribuição dentro desses limites.

### 1.2 Exemplos Práticos

Para N = 0, o intervalo é de 1 até 1, e o valor esperado é 0.
Para N = 3, o intervalo é de 8 até 15, e o valor esperado calculado é 11.
Para N = 9, o intervalo vai de 512 até 1023, e o valor esperado chega a 1013.

### 1.3 Explicação Detalhada

* O **início do intervalo** é sempre 2 elevado a N (2^N).
* O **fim do intervalo** é 2 elevado a (N+1) menos 1 (2^(N+1) - 1), que é um número de Mersenne.
* O valor esperado é aproximado pela soma de todos os números de Mersenne desde 0 até N, onde cada número de Mersenne é 2 elevado a k menos 1 (2^k - 1).

### 1.4 Aplicações

Esse padrão pode ser útil para modelar crescimento exponencial, distribuir valores em faixas específicas e em computação para otimização de estruturas de dados que trabalham com potências de 2, como árvores binárias e segmentações.

### 1.5 Análise da Tabela

| N | Início (2^N) | Esperado (soma Mersenne) | Fim (2^(N+1)-1) |
| - | ------------ | ------------------------ | --------------- |
| 0 | 1            | 0                        | 1               |
| 1 | 2            | 1                        | 3               |
| 2 | 4            | 4                        | 7               |
| 3 | 8            | 11                       | 15              |
| 4 | 16           | 26                       | 31              |
| 5 | 32           | 57                       | 63              |
| 6 | 64           | 120                      | 127             |
| 7 | 128          | 247                      | 255             |
| 8 | 256          | 502                      | 511             |
| 9 | 512          | 1013                     | 1023            |

---

## 2. Script `teorema_alexander.py`

### 2.1 Relação com o Teorema

O script implementa a ideia do crescimento em intervalos de potências de 2 e calcula o valor esperado baseado na soma de números de Mersenne dentro desses limites.

### 2.2 Objetivo do Script

Gerar e exibir uma tabela com os valores do início do intervalo, o valor esperado calculado e o fim do intervalo para diferentes valores de N, mostrando a progressão do crescimento.

### 2.3 Exemplo de Saída

```
 N | Inicio (2^N) |  Esperado pelo Teorema |    Fim (2^(N+1)-1)
-----------------------------------------------------------------
 0 |            1 |                      0 |                  1
 1 |            2 |                      1 |                  3
 2 |            4 |                      4 |                  7
 3 |            8 |                     11 |                 15
 4 |           16 |                     26 |                 31
 5 |           32 |                     57 |                 63
 6 |           64 |                    120 |                127
 7 |          128 |                    247 |                255
 8 |          256 |                    502 |                511
 9 |          512 |                   1013 |               1023
```

### 2.4 Funcionamento Interno

* **mersenne\_number(k)**: calcula o número de Mersenne para k (2^k - 1).
* **valor\_esperado(N)**: soma todos os números de Mersenne de 0 até N para obter o valor esperado.
* Para cada N, calcula o início (2^N) e fim (2^(N+1) - 1) do intervalo.
* Imprime a tabela formatada.

### 2.5 Tecnologias e Requisitos

* Python 3.8.10 ou superior.

---

## 3. Extras

### 3.1 Licença

MIT License – uso livre e aberto.

### 3.2 Referências

* Documentação oficial do Python: [https://www.python.org/](https://www.python.org/)
* Conceitos de números de Mersenne e potências de 2: materiais de matemática básica e computação.

### 3.3 Testes e Validações

Testado no ambiente Windows 10 com Python 3.8.10, funcionando conforme esperado.

---

## 4. Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **Número de Mersenne**: números da forma "2 elevado a k menos 1", como 1, 3, 7, 15, etc., que crescem muito rápido.
* **Valor esperado**: aqui significa o resultado aproximado obtido ao somar esses números, uma forma de medir o crescimento acumulado.
* **Intervalo**: faixa entre dois números definidos pelas potências de 2, que ajuda a organizar os dados.
* **Potência de 2**: número obtido ao multiplicar 2 por ele mesmo várias vezes, por exemplo, 2, 4, 8, 16, etc.
* **Python 3.8.10**: versão da linguagem usada para garantir compatibilidade e funcionamento do script. 
