# 🧮 Teorema de Löwenheim-Skolem

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Teorema](https://img.shields.io/badge/Teorema-Löwenheim--Skolem-ff69b4.svg)](https://en.wikipedia.org/wiki/Löwenheim%E2%80%93Skolem_theorem)

## Frase do Teorema

> "Se uma teoria lógica tem um modelo infinito, então ela tem modelos de cardinalidade infinita de qualquer tamanho, incluindo modelos contáveis." – Este teorema trata da criação de modelos lógicos com diferentes números de elementos, ou seja, pode-se "compactar" ou "expandir" uma teoria para diferentes tamanhos, mantendo sua veracidade.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `teorema_löwenheim_skolem.py`](#2-script-teorema_löwenheim_skolempy)

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

O **Teorema de Löwenheim-Skolem** afirma que se uma teoria lógica tem um modelo infinito, então ela também tem modelos de qualquer cardinalidade infinita, incluindo modelos contáveis. Em outras palavras, você pode criar um modelo que representa a teoria com diferentes números de elementos, sem perder a consistência da teoria.

### 1.2 Exemplos Práticos

Imagine que você tem uma teoria sobre conjuntos. Se essa teoria pode ser representada por um conjunto infinito, então você pode representá-la por conjuntos de tamanhos muito pequenos (contáveis) sem que a teoria perca sua veracidade.

### 1.3 Explicação Detalhada

Se uma teoria lida com um conjunto infinito, ela pode ser expandida ou reduzida de tal maneira que o modelo resultante ainda mantém as mesmas propriedades, mas agora com um número diferente de elementos. A essência do teorema está em garantir que não importa o tamanho do conjunto no modelo, desde que a teoria seja válida, o modelo ainda será válido.

### 1.4 Aplicações

O Teorema de Löwenheim-Skolem tem aplicações em várias áreas da lógica matemática e da teoria dos modelos, como em álgebra, teoria dos conjuntos e lógica de primeira ordem. Ele também tem implicações importantes para a construção de modelos computacionais e sistemas de inteligência artificial.

### 1.5 Análise da Tabela

A tabela abaixo mostra como os valores de **Início** (2^N) e **Fim** (2^(N+1)-1) podem ser usados para gerar valores "Esperados pelo Teorema" que se encaixam dentro desses intervalos, conforme o modelo descrito no código.

| N | Início (2^N) | Esperado pelo Teorema | Fim (2^(N+1))-1 |
| - | ------------ | --------------------- | --------------- |
| 0 | 1            | 1                     | 1               |
| 1 | 2            | 3                     | 3               |
| 2 | 4            | 5                     | 7               |
| 3 | 8            | 10                    | 15              |
| 4 | 16           | 20                    | 31              |
| 5 | 32           | 58                    | 63              |
| 6 | 64           | 100                   | 127             |
| 7 | 128          | 192                   | 255             |
| 8 | 256          | 451                   | 511             |
| 9 | 512          | 783                   | 1023            |

---

## 2. Script `teorema_löwenheim_skolem.py`

### 2.1 Relação com o Teorema

Este script simula o processo descrito pelo Teorema de Löwenheim-Skolem, gerando um valor "Esperado pelo Teorema" dentro do intervalo \[2^N, 2^(N+1)-1], que é a faixa de valores definida para cada valor de **N**.

### 2.2 Objetivo do Script

O objetivo do script é gerar números "Esperados pelo Teorema" dentro de intervalos definidos pelas potências de 2, sem recorrer diretamente ao valor esperado. Isso é feito por meio de uma função que calcula um número aleatório dentro desses intervalos.

### 2.3 Exemplo de Saída

Quando executado, o script gera a seguinte tabela:

```
Tabela de Valores Gerados:
N   Início (2^N)  Esperado pelo Teorema    Fim (2^(N+1))-1   
0   1              1                       1                  
1   2              3                       3                  
2   4              5                       7                  
3   8              10                      15                 
4   16             20                      31                 
5   32             58                      63                 
6   64             100                     127                
7   128            192                     255                
8   256            451                     511                
9   512            783                     1023               
```

### 2.4 Funcionamento Interno

O script utiliza uma função `calcular_valor_esperado`, que gera um número aleatório dentro do intervalo determinado pelos valores de **Início** e **Fim** (baseados nas potências de 2). Esse número é então usado como o valor "Esperado pelo Teorema" para o respectivo valor de **N**.

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10** ou superior
* Biblioteca padrão do Python (não há dependências externas)

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### 3.2 Referências

* [Teorema de Löwenheim-Skolem - Wikipedia](https://en.wikipedia.org/wiki/Löwenheim%E2%80%93Skolem_theorem)
* [Python](https://www.python.org/)

### 3.3 Testes e Validações

O script foi testado para garantir que os valores "Esperados pelo Teorema" estão dentro dos intervalos corretos, e a geração aleatória respeita a estrutura da tabela.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **Teorema de Löwenheim-Skolem:** Refere-se à ideia de que uma teoria lógica, se tem um modelo infinito, pode ter modelos de qualquer tamanho, mesmo os menores.
* **Modelo:** Um modelo em lógica é uma interpretação ou uma estrutura matemática que torna uma teoria verdadeira.
* **Cardinalidade:** Cardinalidade se refere ao número de elementos de um conjunto. No contexto do teorema, fala-se de conjuntos com cardinalidade infinita.
