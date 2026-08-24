# 🧩 - Funcional De Banach Steinhaus
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  

## Frase do Teorema

> Se um grupo de transformações (ou operadores) não faz nenhum ponto “ficar muito grande”, então nenhuma delas pode ser muito “grande” no geral – isso quer dizer que o comportamento é controlado de forma uniforme para todo o grupo.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `banach_steinhaus_animation.py`](#2-script-banach_steinhaus_animationpy)  
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

O princípio da limitação uniforme, conhecido como Teorema de Banach–Steinhaus, afirma que se um conjunto de transformações lineares não faz nenhum vetor ficar com valores muito grandes individualmente, então o tamanho delas de forma geral também está limitado. Em outras palavras, a limitação ponto a ponto das transformações implica numa limitação global.

### 1.2 Exemplos Práticos

Imagine várias funções que aplicamos a números entre -1 e 1. Cada função pode oscilar, mas nenhuma fica muito grande em nenhum ponto específico. O teorema garante que, ao olhar para o “maior valor possível” que cada função pode atingir, esse valor é controlado para todo o grupo.

### 1.3 Explicação Detalhada

O teorema trabalha com espaços onde você pode medir distâncias e tamanhos (chamados espaços normados e completos). Se todas as transformações aplicadas a qualquer ponto geram valores que não explodem, então o tamanho máximo dessas transformações também não explode. Isso é importante porque ajuda a garantir que processos que envolvem muitos operadores são estáveis.

### 1.4 Aplicações

- Análise de séries e sequências de funções  
- Garantia de estabilidade em sistemas que usam muitos operadores  
- Base para outros resultados importantes da análise funcional  
- Aplicações em física, engenharia e matemática aplicada  

### 1.5 Análise da Tabela

Este item pode incluir uma tabela simples mostrando exemplos de operadores com limites ponto a ponto e seus limites uniformes, facilitando o entendimento do princípio.

---

## 2. Script `banach_steinhaus_animation.py`

### 2.1 Relação com o Teorema

O script gera uma animação que visualiza a ideia do teorema, mostrando funções cujas oscilações são limitadas ponto a ponto, e como essas oscilações estão controladas no conjunto todo, demonstrando a limitação uniforme de forma intuitiva.

### 2.2 Objetivo do Script

Mostrar, com gráficos 3D animados, uma sequência de funções intercalando duas famílias: uma com frequências que são potências de 2, e outra com frequências que são números de Mersenne (2 elevado a (n+1) menos 1). A animação simula um tremor para evidenciar variações pequenas, lembrando um “terremoto” no gráfico.

### 2.3 Exemplo de Saída

Uma superfície colorida tridimensional que oscila e “pisca” alternando entre as funções, onde o eixo vertical representa o índice da função, o horizontal representa o domínio dos números, e a altura representa o valor da função.

### 2.4 Funcionamento Interno

- O eixo X varia de -1 a 1, representando a entrada das funções.  
- O eixo Y representa o índice da função (de 0 a 10).  
- Para índices pares são usadas frequências que são potências de 2.  
- Para índices ímpares, frequências de números de Mersenne.  
- Uma pequena perturbação aleatória é adicionada para simular tremores.  
- A transparência da superfície varia para gerar um efeito de “piscar”.  

### 2.5 Tecnologias e Requisitos

- Python 3.8.10  
- Biblioteca matplotlib para gráficos e animações  
- Numpy para cálculos numéricos  

---

## 3 Extras

### 3.1 Licença

Este projeto está sob a licença MIT — o que significa que você pode usar, modificar e distribuir livremente, contanto que mantenha os créditos.

### 3.2 Referências

- [Banach–Steinhaus Principle (Wikipedia)](https://en.wikipedia.org/wiki/Uniform_boundedness_principle)  
- Livros e artigos introdutórios sobre análise funcional  

### 3.3 Testes e Validações

O script foi testado em Python 3.8.10 e executa a animação sem erros, desde que as dependências estejam instaladas. Caso apareçam erros relacionados a versões antigas, ajustar a função de remoção de superfícies no gráfico pode ser necessário.

---

## 4 Contato

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*  

---

## 5. Nota

**Banach–Steinhaus**: nome dos matemáticos que estudaram essas propriedades de operadores, uma combinação dos sobrenomes deles.  
**Função**: é uma relação que associa cada entrada a uma saída (por exemplo, um número a outro número).  
**Limitação ponto a ponto**: significa que, para cada entrada individual, o valor da função não cresce além de um certo limite.  
**Limitação uniforme**: significa que existe um limite que serve para todas as entradas ao mesmo tempo.  
**Operador**: neste contexto, é uma transformação linear que age sobre elementos de um espaço matemático.  
**Espaço normado**: um conjunto onde é possível medir “tamanhos” ou “distâncias”.  
**Completo (espaço de Banach)**: é um espaço onde sequências que vão se aproximando têm um ponto final dentro do próprio espaço (não “foge” dele).  
**Frequência**: número que indica o quanto uma função oscila ou vibra em um intervalo.  
**Número de Mersenne**: um número da forma 2^(n+1) - 1, que tem importância em matemática por suas propriedades especiais.  
**Animação**: sequência de imagens que, ao passar rapidamente, cria a sensação de movimento.
