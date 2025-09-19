# 📐 - Teorema de Liouville

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Frase do Teorema

> Se uma função complexa, que pode ser derivada em toda a extensão do plano, nunca ultrapassa um limite fixo, então ela não muda, ou seja, é constante.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script Liouville.py](#2-script-liouvillepy)

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

O teorema diz que uma função que pode ser “derivada” (função analítica) em todo o plano dos números complexos e que não cresce demais (ou seja, limitada) não pode variar. Ela é obrigatoriamente constante.

### 1.2 Exemplos Práticos

* Uma função que sempre retorna o número 5 é um exemplo simples e constante.
* Já uma função polinomial ou exponencial cresce rápido e não é limitada.

### 1.3 Explicação Detalhada

Se uma função complexa tem um limite máximo em seu valor absoluto para todos os números complexos, ela não pode ter “curvas” ou “mudanças” — isso é mostrado através de uma propriedade das derivadas dessas funções.

### 1.4 Aplicações

* Ajuda a entender o comportamento de funções analíticas.
* É usada para provar outras propriedades importantes na matemática, como o fato de que polinômios sempre têm raízes complexas.

### 1.5 Análise da Tabela

No script, avaliamos três funções em valores que crescem exponencialmente e mostramos os valores para observar quais são limitadas e constantes.

---

## 2. Script Liouville.py

### 2.1 Relação com o Teorema

O script demonstra, com exemplos numéricos e gráficos, a ideia central: funções constantes são limitadas, outras crescem rápido e não são limitadas.

### 2.2 Objetivo do Script

Avaliar funções em valores que crescem como potências de 2 e mostrar, via tabela e gráfico, a diferença entre funções constantes e não constantes.

### 2.3 Exemplo de Saída

A tabela mostra valores para n de 0 a 10, avaliando f1, f2 e f3 em 2^n e em 2^(n+1)-1. A exponencial cresce muito rápido, ocasionando valores muito grandes ou até overflow.

### 2.4 Funcionamento Interno

* Calcula valores para as funções:

  * f1(z) = constante 5
  * f2(z) = z² + 3z + 2
  * f3(z) = exp(z)
* Para cada n, calcula 2^n e 2^(n+1)-1, avalia as funções nesses pontos.
* Exibe uma tabela com esses valores.
* Plota todos os valores num único gráfico com escala logarítmica para evidenciar diferenças.

### 2.5 Tecnologias e Requisitos

* Python 3.8.10
* Bibliotecas: numpy, pandas, matplotlib

---

## 3 Extras

### 3.1 Licença

MIT License

### 3.2 Referências

* Conceitos de análise complexa (função analítica, função inteira)
* Documentação das bibliotecas usadas

### 3.3 Testes e Validações

* Atenção para erros de overflow na função exponencial com valores muito grandes (aviso padrão do Python)

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Função analítica:** função que pode ser derivada infinitas vezes em uma região, como polinômios ou exponenciais.
**Função inteira:** função analítica no plano todo dos números complexos.
**Valor absoluto (módulo):** medida da “distância” de um número complexo até a origem, sempre positiva.
**Overflow:** quando um número fica tão grande que não pode ser representado no computador.
**Escala logarítmica:** modo de mostrar valores muito grandes ou pequenos de forma mais compacta no gráfico.
