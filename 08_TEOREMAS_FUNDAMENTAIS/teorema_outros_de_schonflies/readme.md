# 🧩 - De Schonflies
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)  

## Frase do Teorema

> Toda curva simples fechada no plano pode ser transformada em um círculo sem cortes ou sobreposições – isso significa que essas curvas são topologicamente iguais a um círculo.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `schoenflies_intervalos.py`](#2-script-schoenflies_intervalospy)  
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

## 1 Introdução ao Teorema

### 1.1 Resumo  
O *Teorema de Schönflies* afirma que qualquer curva fechada e simples (sem cruzamentos) no plano pode ser deformada, sem rasgar ou colar, em um círculo. Isso significa que do ponto de vista topológico, essas curvas são equivalentes a um círculo perfeito.

### 1.2 Exemplos Práticos  
Imagine que você desenhou uma forma irregular e fechada em uma folha de papel, como um polígono curvado. O teorema garante que essa forma pode ser “esticada” ou “dobrada” suavemente até virar um círculo, sem cortes.

### 1.3 Explicação Detalhada  
Em matemática, especialmente em topologia, estudar propriedades que não mudam com deformações é importante. O teorema diz que as curvas simples fechadas não têm “furos” ou “nós”, logo são “como um círculo”.  

### 1.4 Aplicações  
- Topologia geral  
- Geometria computacional  
- Análise de formas e imagens  

### 1.5 Análise da Tabela  
Apesar do teorema em si não definir sequências numéricas, a tabela apresentada trabalha com potências de 2 e números de Mersenne (que são da forma 2^(N+1) - 1). Essa sequência pode ser usada para delimitar intervalos numéricos que representam contagens ou índices em certos contextos matemáticos ou computacionais.

---

## 2 Script `schoenflies_intervalos.py`

### 2.1 Relação com o Teorema  
O script utiliza os conceitos matemáticos das potências de 2 e números de Mersenne para gerar intervalos numéricos que, simbolicamente, representam limites relacionados ao conceito de “intervalos completos” em sequências, algo que pode ser associado à ideia do teorema no sentido de delimitar estruturas simples e completas.

### 2.2 Objetivo do Script  
Gerar uma tabela com:  
- **N**  
- O valor de início do intervalo (2^N)  
- Um valor calculado internamente, baseado em potências de 2 e propriedades de N  
- O valor final do intervalo (2^(N+1) - 1)  

Tudo isso sem usar diretamente valores externos da tabela “Esperado pelo teorema”, focando somente nas potências de 2 e números de Mersenne.

### 2.3 Exemplo de Saída  

```

## N | Inicio (2^N) |   Valor Teorema | Fim (2^(N+1)-1)

0 |            1 |               1 |               1
1 |            2 |               3 |               3
2 |            4 |               7 |               7
3 |            8 |              15 |              15
4 |           16 |              27 |              31
5 |           32 |              55 |              63
6 |           64 |             111 |             127
7 |          128 |             215 |             255
8 |          256 |             399 |             511
9 |          512 |             799 |            1023

```

### 2.4 Funcionamento Interno  
- Para cada N, o script calcula o intervalo [2^N, 2^(N+1)-1].  
- Calcula um valor intermediário usando a soma dos bits de N e potências de 2, garantindo que o resultado fique dentro do intervalo.  
- Essa abordagem usa somente operações com potências de 2, conforme solicitado.  

### 2.5 Tecnologias e Requisitos  
- Python 3.8.10 ou superior  

---

## 3 Extras

### 3.1 Licença  
Este projeto está licenciado sob a licença MIT.

### 3.2 Referências  
- Wikipedia: [Teorema de Schönflies](https://en.wikipedia.org/wiki/Sch%C3%B6nflies_theorem)  
- Números de Mersenne: [https://pt.wikipedia.org/wiki/N%C3%BAmero_de_Mersenne](https://pt.wikipedia.org/wiki/N%C3%BAmero_de_Mersenne)  

### 3.3 Testes e Validações  
Testado no Windows 10 e Ubuntu 20.04 com Python 3.8.10

---

## 4 Contato

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*  

---

## 5. Nota

**Potência de 2**: número obtido multiplicando 2 por ele mesmo N vezes. Por exemplo, 2^3 significa 2×2×2 = 8.  
**Número de Mersenne**: número que é uma potência de 2 menos 1, como 3, 7, 15, 31, etc. (exemplo: 2^(N+1)-1).  
**Soma dos bits**: número de dígitos “1” na representação binária de um número. Por exemplo, 5 em binário é 101, que tem 2 bits iguais a 1.  
**Intervalo**: conjunto de números entre um valor inicial e um valor final, incluindo ambos.  
