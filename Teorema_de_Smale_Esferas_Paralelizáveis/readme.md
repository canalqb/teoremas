# 🧮 - Teorema de Smale (Esferas Paralelizáveis)

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)

## Frase do Teorema

> **"As esferas de dimensão maior ou igual a 7 podem ser paralelizadas."**
> O Teorema de Smale afirma que, para dimensões $n \geq 7$, as esferas $S^n$ são paralelizáveis. Ou seja, podemos criar uma estrutura suave e não nula de vetores em todos os pontos da esfera para essas dimensões. Em dimensões menores, isso não é possível.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `teorema_smale.py`](#2-script-teorema_smalepy)

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

## 1. Introdução ao Teorema

### 1.1 Resumo

O **Teorema de Smale** trata da paralelização das esferas em diferentes dimensões. Para esferas de dimensão maior ou igual a 7 ($n \geq 7$), é possível definir um campo vetorial suave que não se anula em nenhum ponto da esfera. Em dimensões menores, essa paralelização não é possível.

### 1.2 Exemplos Práticos

Na prática, isso significa que para dimensões $n = 7$, $n = 8$, $n = 9$, etc., podemos ter um campo de vetores em cada ponto da esfera que não desaparece em nenhum momento. Mas, para $n < 7$, esse tipo de paralelismo não funciona, e qualquer tentativa de definir tal campo vetorial levaria a contradições.

### 1.3 Explicação Detalhada

Imagine que você tem uma esfera em 3 dimensões (como uma bola de futebol). Não é possível criar um campo de vetores que esteja presente em toda a superfície da esfera e que seja suave e não nulo (em todos os pontos da esfera). No entanto, para esferas em dimensões maiores, a situação muda e é possível fazer isso.

### 1.4 Aplicações

Esse teorema é importante em áreas como:

* **Topologia diferencial**: Para entender a geometria das variedades diferenciáveis.
* **Física teórica**: Onde as esferas aparecem em modelos de campos e interações.
* **Matemática pura**: Em estudos de homotopia e topologia algébrica.

### 1.5 Análise da Tabela

A tabela abaixo mostra os valores para diferentes valores de $N$ e a relação entre o início (2^N) e o fim (2^(N+1) - 1) para cada intervalo de $N$:

| N | Início (2^N) | Esperado pelo teorema | Fim (2^(N+1))-1 |
| - | ------------ | --------------------- | --------------- |
| 0 | 1            | 1                     | 1               |
| 1 | 2            | 2                     | 3               |
| 2 | 4            | 5                     | 7               |
| 3 | 8            | 9                     | 15              |
| 4 | 16           | 18                    | 31              |
| 5 | 32           | 52                    | 63              |
| 6 | 64           | 81                    | 127             |
| 7 | 128          | 134                   | 255             |
| 8 | 256          | 361                   | 511             |
| 9 | 512          | 596                   | 1023            |

O valor "Esperado pelo teorema" é calculado dentro do intervalo definido entre "Início (2^N)" e "Fim (2^(N+1))-1". Os valores são aproximados de forma aleatória para simular a saída do teorema.

## 2. Script `teorema_smale.py`

### 2.1 Relação com o Teorema

O script `teorema_smale.py` gera valores aproximados de acordo com o intervalo determinado pelo Teorema de Smale, usando a relação de potências de 2 para definir o início e o fim do intervalo para cada $N$.

### 2.2 Objetivo do Script

O objetivo do script é gerar uma tabela de valores com base no Teorema de Smale, mostrando a relação entre $N$, o valor inicial (2^N), o valor esperado pelo teorema e o valor final (2^(N+1) - 1).

### 2.3 Exemplo de Saída

A saída gerada pelo script será algo semelhante a:

```
N | Início (2^N) | Esperado pelo teorema | Fim (2^(N+1))-1
------------------------------------------------------------
0 | 1            | 1                     | 1
1 | 2            | 2                     | 3
2 | 4            | 5                     | 7
3 | 8            | 9                     | 15
4 | 16           | 18                    | 31
5 | 32           | 52                    | 63
6 | 64           | 81                    | 127
7 | 128          | 134                   | 255
8 | 256          | 361                   | 511
9 | 512          | 596                   | 1023
```

### 2.4 Funcionamento Interno

O script gera os valores de **"Esperado pelo teorema"** dentro do intervalo \[2^N, 2^(N+1) - 1] para cada valor de $N$. Utiliza a biblioteca `random` para simular a geração de valores dentro desse intervalo. Cada execução do script gera uma tabela diferente, pois os valores são aleatórios dentro dos intervalos.

### 2.5 Tecnologias e Requisitos

* Python 3.8.10 ou superior.
* Biblioteca `random` (já inclusa no Python).

## 3. Extras

### 3.1 Licença

Este projeto está licenciado sob a **Licença MIT**. Para mais detalhes, consulte o arquivo `LICENSE`.

### 3.2 Referências

* Teorema de Smale – [Wikipedia](https://en.wikipedia.org/wiki/Smale%27s_theorem)
* Python 3.8.10 – [Python Oficial](https://www.python.org/)

### 3.3 Testes e Validações

O script foi testado para diferentes valores de $N$, e os resultados estão dentro do intervalo esperado. A geração de números aleatórios é válida para este propósito.

## 4. Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

## 5. Nota

**Topologia**: O estudo das propriedades de objetos geométricos que permanecem invariantes sob transformações contínuas, como deformações ou estiramentos.

**Campo vetorial**: Em matemática, é um campo que associa a cada ponto de um espaço geométrico um vetor, que pode ser interpretado como uma seta com direção e magnitude.

**Aleatoriedade**:


Refere-se a eventos ou valores que são gerados sem um padrão determinístico, ou seja, de forma imprevisível.
