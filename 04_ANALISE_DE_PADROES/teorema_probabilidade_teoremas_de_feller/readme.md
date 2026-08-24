# 🧩 - Teoremas De Feller
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![Feller](https://img.shields.io/badge/Teorema-Feller-4B0082.svg)](https://en.wikipedia.org/wiki/William_Feller)

## Frase do Teorema

> A média ajustada de valores em intervalos discretos binários converge para a média teórica do intervalo, garantindo estabilidade nas distribuições discretas mesmo quando as variáveis não são idênticas.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `teorema_de_feller.py`](#2-script-teorema_de_fellerpy)  
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

O **Teorema de Feller** é uma extensão da *Lei dos Grandes Números*, garantindo que a média de uma sequência de variáveis aleatórias independentes, mesmo que não idênticas, converge para a média esperada, desde que certas condições sejam atendidas. Aqui, ele é aplicado para analisar médias em intervalos discretos definidos por potências de 2.

### 1.2 Exemplos Práticos

Imagine dividir números inteiros em blocos que começam e terminam em potências de 2 (exemplo: de 32 a 63). A média dos números desse intervalo pode ser aproximada por um "meio ajustado", que é um valor próximo da média exata do intervalo, facilitando cálculos e análises.

### 1.3 Explicação Detalhada

Cada intervalo é da forma [2^k, 2^(k+1) - 1]. O teorema nos diz que a média dos valores dentro desse intervalo converge para a média esperada — calculada simplesmente pela média entre o início e o fim do intervalo.

O “meio ajustado” é uma tentativa prática de representar essa média, talvez com um pequeno ajuste para melhor encaixe em dados reais.

### 1.4 Aplicações

- Estatísticas de distribuições discretas  
- Modelagem de dados binários  
- Análise de algoritmos que usam partições binárias  
- Otimização de aproximações em séries de dados discretos  

### 1.5 Análise da Tabela

| Início (2^ID) | Fim (2^(ID+1) - 1) | Meio (ajustado) | Média Teórica | Desvio (Meio - Média) |
| ------------- | ------------------- | --------------- | ------------- | --------------------- |
| 32            | 63                  | 49              | 47            | +2                    |
| ...           | ...                 | ...             | ...           | ...                   |

O desvio mostra a diferença entre o meio ajustado e a média exata, geralmente pequena, indicando a boa aproximação do meio ajustado.

---

## 2. Script `teorema_de_feller.py`

### 2.1 Relação com o Teorema

Este script implementa a análise do Teorema de Feller para intervalos binários, calculando médias teóricas e comparando com meios ajustados fornecidos manualmente.

### 2.2 Objetivo do Script

Facilitar a visualização e validação prática da convergência das médias em intervalos discretos e demonstrar a aplicabilidade do teorema na análise de dados discretos.

### 2.3 Exemplo de Saída

```plaintext
Intervalo: [32, 63]
Média Teórica: 47
Meio Ajustado: 49
Desvio: +2
...
````

### 2.4 Funcionamento Interno

* Define intervalos baseados em potências de 2
* Calcula médias teóricas para cada intervalo
* Compara com valores ajustados previamente
* Exibe tabela de resultados com desvio

### 2.5 Tecnologias e Requisitos

* Python 3.8.10 (ou superior)
* Biblioteca pandas (para manipulação de dados)

Instalação do pandas:

```
pip install pandas
```

---

## 3 Extras

### 3.1 Licença

Este projeto é **de domínio público**, podendo ser utilizado livremente para fins acadêmicos e educacionais.

### 3.2 Referências

* [Teorema de Feller - Wikipedia](https://en.wikipedia.org/wiki/William_Feller)
* Estatística básica e teoria das probabilidades

### 3.3 Testes e Validações

O script foi testado em Python 3.8.10 com dados de exemplo e validado com cálculos manuais da média.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Variável Aleatória**: valor numérico que representa o resultado de um experimento aleatório.

**Média Esperada**: também chamada de esperança, é o valor médio que se espera obter ao repetir um experimento muitas vezes.

**Variância**: medida que indica o quanto os valores de uma variável aleatória se dispersam em relação à média.

**Independência**: propriedade onde o resultado de um experimento não afeta o resultado de outro.

**Intervalo Binário**: conjunto de números inteiros entre duas potências consecutivas de 2, por exemplo, de 32 até 63. 
