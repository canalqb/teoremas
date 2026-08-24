# 📚 Teorema de Compactação

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Frase do Teorema

> **Teorema de Compactação** – O teorema descreve como um valor gerado de forma compacta pode se aproximar de um intervalo determinado por potências de 2, oferecendo uma maneira de entender como os números se distribuem dentro de um intervalo crescente.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)

* [2. Script `teorema_compactacao.py`](#2-script-teorema_compactacaopy)

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

O **Teorema de Compactação** descreve como podemos gerar um número dentro de um intervalo específico, onde os limites de cada intervalo são definidos por potências de 2. Este processo de compactação ajuda a entender como os números se distribuem dentro de intervalos crescentes, e como podemos aproximar resultados dentro desses intervalos.

### 1.2 Exemplos Práticos

Suponha que você tenha um número **N**. O valor **Início** do intervalo é dado por **2^N** e o **Fim** é dado por **2^(N+1) - 1**. Com isso, você pode prever que o número gerado estará sempre dentro desse intervalo.

Por exemplo:

* Para **N = 2**, o intervalo é de 4 a 7.
* Para **N = 5**, o intervalo é de 32 a 63.

### 1.3 Explicação Detalhada

Imagine que, ao realizar uma operação matemática ou computacional, você precisa gerar um número que deve estar dentro de um intervalo. O Teorema de Compactação nos permite prever onde esse número estará com base em **N**. O número será sempre maior ou igual a **2^N** e menor ou igual a **2^(N+1) - 1**.

Em outras palavras:

* Para **N = 3**, o número gerado estará entre **2^3 = 8** e **2^(3+1) - 1 = 15**.

### 1.4 Aplicações

Esse teorema tem aplicações em diversas áreas como:

* **Algoritmos de compressão:** Para gerar resultados que se ajustam a limites específicos.
* **Processamento de dados:** Para entender como os dados se distribuem em diferentes intervalos.
* **Sistemas de computação:** Para otimizar o uso de memória e tempo de execução.

### 1.5 Análise da Tabela

A tabela a seguir mostra os intervalos gerados para diferentes valores de **N**:

| **N** | **Início (2^N)** | **Esperado pelo Teorema** | **Fim (2^(N+1)-1)** |
| ----- | ---------------- | ------------------------- | ------------------- |
| 0     | 1                | 1                         | 1                   |
| 1     | 2                | 3                         | 3                   |
| 2     | 4                | 6                         | 7                   |
| 3     | 8                | 9                         | 15                  |
| 4     | 16               | 16                        | 31                  |
| 5     | 32               | 59                        | 63                  |
| 6     | 64               | 71                        | 127                 |
| 7     | 128              | 233                       | 255                 |
| 8     | 256              | 372                       | 511                 |
| 9     | 512              | 858                       | 1023                |

Os números "Esperado pelo Teorema" são gerados dentro de seus respectivos intervalos.

---

## 2. Script `teorema_compactacao.py`

### 2.1 Relação com o Teorema

O script `teorema_compactacao.py` utiliza o Teorema de Compactação para gerar números dentro de um intervalo determinado por **N**, como explicado anteriormente. O objetivo é aproximar os resultados "Esperados" dentro do intervalo definido por **2^N** e **2^(N+1)-1**.

### 2.2 Objetivo do Script

O script calcula valores "Esperados pelo Teorema", gerando números aleatórios dentro dos intervalos definidos, como se fosse uma simulação prática do teorema.

### 2.3 Exemplo de Saída

Quando o script é executado, ele gera uma tabela de valores com o intervalo definido e o valor "Esperado pelo Teorema". Exemplo:

```
Tabela de Valores Gerados:
N   Início (2^N)  Esperado pelo Teorema    Fim (2^(N+1))-1   
0   1              1                       1                  
1   2              3                       3                  
2   4              6                       7                  
3   8              9                       15                 
4   16             16                      31                 
5   32             59                      63                 
6   64             71                      127                
7   128            233                     255                
8   256            372                     511                
9   512            858                     1023               
```

### 2.4 Funcionamento Interno

O script trabalha com uma tabela pré-definida de valores de **N**, onde calcula **Início** e **Fim** com base em potências de 2. Em seguida, gera números aleatórios dentro do intervalo, simulando a aplicação do teorema.

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10** ou superior
* **Biblioteca random** para geração de números aleatórios

Para rodar o script, basta ter o Python instalado em sua máquina e executar o arquivo `teorema_compactacao.py`.

---

## 3. Extras

### 3.1 Licença

Este projeto é licenciado sob a **Licença MIT**.

### 3.2 Referências

* Teorema de Compactação
* [Lei dos Grandes Números](https://en.wikipedia.org/wiki/Law_of_large_numbers)

### 3.3 Testes e Validações

Os resultados gerados pelo script podem ser testados para garantir que estão dentro dos intervalos definidos por **2^N** e **2^(N+1)-1**. O valor "Esperado pelo Teorema" deve estar sempre dentro desses limites.

---

## 4. Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Nota sobre terminologia e conceitos técnicos:**

* **Esperado pelo Teorema**: Refere-se ao valor que o teorema prediz dentro do intervalo.
* **Intervalo**: A faixa de valores possíveis dentro dos quais um número pode cair.
