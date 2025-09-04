# 🧮 - Teorema Classificação de Superfícies  
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Frase do Teorema

> Toda superfície compacta sem borda pode ser classificada de acordo com seu número de "furos" (gênero) e orientabilidade, o que determina sua forma topológica de forma única e completa.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `classificacao_superficies.py`](#2-script-classificacao_superficiespy)  
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

O conceito central é que todas as superfícies sem bordas podem ser identificadas por quantos "furos" (gêneros) elas têm e se são orientáveis (tem um lado "de cima" e "de baixo") ou não. Isso permite catalogar todas as superfícies possíveis com base nesses números.

### 1.2 Exemplos Práticos

- Uma esfera tem 0 furos e é orientável.  
- Um toro (como uma rosquinha) tem 1 furo e é orientável.  
- Uma garrafa de Klein não é orientável e tem uma estrutura diferente.

### 1.3 Explicação Detalhada

O "gênero" (g) representa a quantidade de buracos ou "furos" na superfície. Para superfícies orientáveis, a característica de Euler (χ), que é um número que expressa a forma geral da superfície, é dada por:  

χ = 2 - 2 * g  

Quanto maior o gênero, mais complexa é a superfície. O número de superfícies distintas cresce rapidamente com o aumento de g, ficando entre potências de 2.

### 1.4 Aplicações

Este conceito é usado em várias áreas da matemática, física e ciência da computação, como topologia, estudo de formas no espaço, análise de superfícies em gráficos e modelagem 3D.

### 1.5 Análise da Tabela

A tabela mostra para cada N (que pode ser entendido como um índice de complexidade), o gênero (quantidade de furos) cresce como 2^N, enquanto a contagem esperada de superfícies distintas fica entre 2^N e 2^(N+1)-1, que são intervalos de números exponenciais que aumentam rápido conforme N cresce.

---

## 2. Script `classificacao_superficies.py`

### 2.1 Relação com o Teorema

O script ilustra essa relação entre N, gênero (g = 2^N), e a característica de Euler (χ = 2 - 2g) para superfícies orientáveis, reforçando o crescimento exponencial do número de superfícies possíveis.

### 2.2 Objetivo do Script

Mostrar a relação simples entre o índice N, o gênero da superfície, um número complementar chamado número de Mersenne (2^N - 1), e a característica de Euler, de forma clara e direta.

### 2.3 Exemplo de Saída

```

## N | Gênero g=2^N | Mersenne M\_N=2^N-1 | Euler χ=2-2g

0 |          1 |                  0 |            0
1 |          2 |                  1 |           -2
2 |          4 |                  3 |           -6
3 |          8 |                  7 |          -14
4 |         16 |                 15 |          -30
5 |         32 |                 31 |          -62
6 |         64 |                 63 |         -126

```

### 2.4 Funcionamento Interno

- Para cada N de 0 até o máximo definido (default 6), calcula:  
  * **Gênero g** = 2 elevado a N  
  * **Número de Mersenne M_N** = (2 elevado a N) menos 1  
  * **Característica de Euler χ** = 2 menos 2 vezes g  
- Imprime os valores em uma tabela formatada.

### 2.5 Tecnologias e Requisitos

- Desenvolvido em **Python 3.8.10** ou superior.  
- Funciona em qualquer sistema com interpretador Python.

---

## 3 Extras

### 3.1 Licença

Este projeto é licenciado sob a Licença MIT — veja o arquivo LICENSE para detalhes.

### 3.2 Referências

- Classificação das superfícies — explicações gerais na topologia.  
- Característica de Euler — conceito básico em geometria e topologia.

### 3.3 Testes e Validações

O script pode ser executado diretamente e comparado com os valores teóricos conhecidos para verificar consistência.

---

## 4 Contato

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Gênero (g):** representa o número de "furos" ou "buracos" da superfície — uma medida da sua complexidade topológica.

**Número de Mersenne (M_N):** é um número na forma 2^N - 1, usado aqui apenas como referência complementar para acompanhar o crescimento do gênero.

**Característica de Euler (χ):** número que descreve a forma geral da superfície, calculado para superfícies orientáveis como 2 - 2 * g, que indica propriedades topológicas importantes.

**Orientável:** significa que a superfície tem dois lados distintos (como a esfera ou o toro), diferente de superfícies não orientáveis (como a garrafa de Klein).
 
