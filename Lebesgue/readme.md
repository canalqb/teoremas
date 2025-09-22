# 📈 - Teorema de Lebesgue sobre Derivadas 
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Lebesgue%20sobre%20Derivadas-ff69b4.svg)](https://en.wikipedia.org/wiki/Lebesgue%27s_differentiation_theorem)

## Frase do Teorema

> **O Teorema de Lebesgue sobre Derivadas** afirma que se uma função pode ser integrada, então é possível recuperar essa função original, derivando sua integral, em quase todos os pontos do intervalo. – *Em termos simples: uma função integrável "vira" uma função suave (diferenciável quase em todo lugar) quando aplicamos a integral, e ao derivar essa nova função, obtemos de volta a função original (quase sempre).*

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `lebesgue_potencias2.py`](#2-script-lebesgue_potencias2py)
  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
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

## 1. Introdução ao Teorema

### 1.1 Resumo

O **Teorema de Lebesgue sobre Derivadas** é uma das principais ideias do cálculo moderno. Ele mostra que quando usamos uma função integrável para criar outra função através de uma integral, essa nova função será suave (ou seja, diferenciável) quase sempre.

### 1.2 Exemplos Práticos

- Se você tem uma função que representa uma taxa (por exemplo, velocidade ao longo do tempo), então a integral representa a posição.
- O teorema garante que, mesmo que a velocidade original seja irregular, ao integrá-la e depois derivar, recuperamos quase toda a velocidade original.

### 1.3 Explicação Detalhada

Imagine uma função simples, como f(x) = 3 em um intervalo. Sua integral acumulada cresce linearmente. Ao derivar essa integral, voltamos a f(x) = 3.

O Teorema de Lebesgue garante que isso funciona **mesmo quando f(x) não é contínua ou suave**, desde que seja integrável.

### 1.4 Aplicações

- Processamento de sinais e reconstrução de dados.
- Probabilidade: construção de distribuições acumuladas.
- Engenharia: análise de funções descontínuas (como sinais digitais).

### 1.5 Análise da Tabela

Neste projeto, usamos o teorema para gerar uma tabela baseada em potências de 2:

| N | Início (2^N) | Esperado pelo teorema | Fim (2^(N+1))-1 |
|---|--------------|------------------------|------------------|
| 0 | 1            | 0                      | 1                |
| 1 | 2            | 2                      | 3                |
| 2 | 4            | 8                      | 7                |
| 3 | 8            | 24                     | 15               |
| 4 | 16           | 64                     | 31               |
| 5 | 32           | 160                    | 63               |
| 6 | 64           | 384                    | 127              |
| 7 | 128          | 896                    | 255              |
| 8 | 256          | 2048                   | 511              |
| 9 | 512          | 4608                   | 1023             |

Esses valores foram calculados usando o próprio teorema, com uma função constante f(x) = N dentro de cada intervalo. O resultado da integral foi: **N * 2^N**.

---

## 2. Script `lebesgue_potencias2.py`

### 2.1 Relação com o Teorema

O script aplica o Teorema de Lebesgue diretamente: define uma função integrável, calcula sua integral, e mostra como a derivada dessa integral retorna à função original.

### 2.2 Objetivo do Script

- Demonstrar o teorema de forma prática.
- Gerar uma tabela com intervalos baseados em potências de 2.
- Mostrar a relação entre a integral acumulada e os valores esperados.

### 2.3 Exemplo de Saída

```bash
C:\Users\Notebook\Desktop\teoremas>python lebesgue_potencias2.py
N   | Início (2^N)   | Esperado pelo teorema   | Fim (2^(N+1))-1
----------------------------------------------------------------------
0   | 1              | 0                       | 1
1   | 2              | 2                       | 3
2   | 4              | 8                       | 7
3   | 8              | 24                      | 15
4   | 16             | 64                      | 31
5   | 32             | 160                     | 63
6   | 64             | 384                     | 127
7   | 128            | 896                     | 255
8   | 256            | 2048                    | 511
9   | 512            | 4608                    | 1023
````

### 2.4 Funcionamento Interno

* Define a função f(x) = N em cada intervalo \[2^N, 2^(N+1)-1].
* Calcula a integral como: **f(x) \* comprimento\_do\_intervalo**.
* Aplica a fórmula do teorema: **F(x) = N \* 2^N**.
* Gera e exibe a tabela.

### 2.5 Tecnologias e Requisitos

* **Python**: 3.8.10 ou superior
* Apenas bibliotecas padrão (`math`)

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

### 3.2 Referências

* Wikipedia: [Teorema de Lebesgue sobre Derivadas](https://en.wikipedia.org/wiki/Lebesgue%27s_differentiation_theorem)
* Apostilas de Análise Real
* Canal YouTube: CanalQb

### 3.3 Testes e Validações

* Testado no Python 3.8.10 (Windows 10)
* Sem dependências externas
* Saída confirmada com a lógica do teorema

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com → [https://canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* 📧 PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**integrável:**
Uma função é chamada de integrável quando podemos calcular sua "área sob a curva" sem problemas. Mesmo que ela tenha pontos irregulares, desde que não "exploda", é considerada integrável.

**derivada:**
É a taxa de variação de uma função. No caso de movimento, por exemplo, a derivada da posição é a velocidade.

**integral:**
É o processo contrário da derivada. Se a derivada mostra como algo muda, a integral mostra o total acumulado dessa mudança.

**quase todo ponto:**
Quer dizer: em todos os pontos, exceto em um conjunto tão pequeno que tem "medida zero". Pode ter infinitos pontos, mas mesmo assim ser "quase nada".

**função constante:**
Uma função que tem sempre o mesmo valor, não importa o valor de entrada.
