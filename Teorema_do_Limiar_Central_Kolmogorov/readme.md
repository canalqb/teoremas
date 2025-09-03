# 🔹 - Teorema do Limite Central (Kolmogorov)

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Limite%20Central-ff69b4.svg)](https://pt.wikipedia.org/wiki/Teorema_do_limite_central)

## Frase do Teorema

> A soma de muitas variáveis aleatórias independentes tende a seguir uma distribuição normal, mesmo que as variáveis originais não sejam normais – isso significa que, com bastante dados, o comportamento geral fica mais previsível e parecido com uma curva conhecida.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `Teorema_do_Limiar_Central_Kolmogorov.py`](#2-script-teorema_do_limiar_central_kolmogorovpy)

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

O **Teorema do Limite Central (TLC)** é um dos conceitos mais importantes da estatística. Ele diz que, quando somamos muitas variáveis aleatórias independentes, o resultado tende a se parecer com uma curva normal (também chamada de distribuição gaussiana), mesmo que as variáveis originais não sigam essa curva.

### 1.2 Exemplos Práticos

Imagine que você lance várias moedas e conte o número de caras. Cada moeda tem chance 50% de dar cara ou coroa. Se lançar só uma moeda, o resultado pode ser 0 ou 1 cara — sem padrão claro. Mas, se lançar 100 moedas, a distribuição do número total de caras se parece muito com a curva normal.

### 1.3 Explicação Detalhada

A versão de Kolmogorov do TLC é mais rigorosa e trabalha com variáveis que podem ter médias e variâncias diferentes. Desde que as variáveis sejam independentes e nenhuma tenha um peso excessivo na soma, a soma normalizada tende à distribuição normal padrão (média zero, desvio 1).

### 1.4 Aplicações

* Estatística inferencial para estimar médias e probabilidades.
* Ciências naturais e sociais para modelar fenômenos aleatórios.
* Controle de qualidade e processos industriais.
* Aprendizado de máquina e inteligência artificial, especialmente na modelagem de erros e ruídos.

### 1.5 Análise da Tabela

A tabela apresenta números na forma de potências de 2 e valores relacionados a limites superiores, como:

| 2^A | Retorno do teorema | 2^(A+1) - 1 |
| --- | ------------------ | ----------- |
| 1   | ?                  | 1           |
| 2   | ?                  | 3           |
| 4   | ?                  | 7           |
| 8   | ?                  | 15          |
| 16  | ?                  | 31          |

Isso mostra crescimento exponencial e pode estar relacionado a quantidades de variáveis somadas e a número de estados possíveis (como em árvores binárias).

---

## 2. Script `Teorema_do_Limiar_Central_Kolmogorov.py`

### 2.1 Relação com o Teorema

O script implementa uma simulação ou cálculo relacionado ao Teorema do Limite Central, focando especialmente na versão de Kolmogorov que permite variáveis com médias e variâncias diferentes.

### 2.2 Objetivo do Script

* Demonstrar numericamente como a soma de variáveis independentes se aproxima da normal.
* Validar a condição de crescimento das variâncias e independência.
* Gerar uma tabela ou gráfico que permita observar a convergência da soma para a distribuição normal.

### 2.3 Exemplo de Saída

```plaintext
Número de variáveis: 16  
Soma normalizada: valor aproximado de uma normal padrão  
Distribuição empírica: se aproxima da curva gaussiana  
```

### 2.4 Funcionamento Interno

* Gera variáveis aleatórias independentes com médias e variâncias definidas.
* Calcula a soma total e normaliza pela raiz da soma das variâncias.
* Avalia a convergência dessa soma para a normal padrão.
* Apresenta os resultados em tabela ou gráfico.

### 2.5 Tecnologias e Requisitos

* Python 3.8.10
* Bibliotecas: numpy, matplotlib (para gráficos, opcional)
* Ambiente de execução padrão para scripts Python.

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a licença MIT — veja o arquivo LICENSE para detalhes.

### 3.2 Referências

* Wikipedia: [Teorema do Limite Central](https://pt.wikipedia.org/wiki/Teorema_do_limite_central)
* Livro: “Probabilidade e Estatística” – autores diversos.

### 3.3 Testes e Validações

O script inclui testes para verificar a convergência da soma das variáveis e validação de condições de independência e variação.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**{Variável aleatória}:** é um valor que pode variar de forma imprevisível, como o resultado de um dado ou moeda.

**{Independência}:** significa que o resultado de uma variável não afeta o resultado da outra.

**{Média}:** é o valor esperado ou "central" que uma variável assume em média.

**{Variância}:** indica o quanto os valores de uma variável se afastam da média; é uma medida de dispersão.

**{Distribuição normal}:** é uma curva em forma de sino que descreve muitos fenômenos naturais, caracterizada por média e desvio padrão.
