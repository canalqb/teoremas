# 🧠 - Teorema de Montel  
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Montel-ff69b4.svg)](https://en.wikipedia.org/wiki/Montel_theorem)

## Frase do Teorema

> *Toda família de funções holomorfas que é limitada em um domínio aberto é uma família normal.*  
> Isso significa que, mesmo que cada função tenha um comportamento diferente, ainda podemos garantir que todas juntas se comportam de forma controlada e previsível dentro de uma certa região.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `montel_potencias_mersennes.py`](#2-script-montel_potencias_mersennespy)
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
O **Teorema de Montel** mostra que, mesmo que você tenha um conjunto de funções complexas, se todas forem bem comportadas dentro de uma região (ou seja, *limitadas*), então é possível extrair uma parte delas que converge para um comportamento estável.

### 1.2 Exemplos Práticos  
Imagine um conjunto de ondas que mudam com o tempo. Mesmo que cada uma tenha uma forma diferente, o Teorema garante que você pode pegar algumas dessas ondas e encontrar um padrão comum que elas seguem, pelo menos em uma parte do tempo.

### 1.3 Explicação Detalhada  
Esse teorema fala sobre funções *holomorfas* (ou seja, suaves e bem comportadas no plano complexo). Quando todas essas funções estão "sob controle" (não explodem), o conjunto delas é chamado de *família normal*. Isso significa que elas se aproximam de forma ordenada, sem surpresas, quando observadas mais de perto.

### 1.4 Aplicações  
Usado em:

- Análise complexa
- Estudo de funções dinâmicas (como fractais)
- Verificação de estabilidade de sistemas
- Processos com convergência controlada

### 1.5 Análise da Tabela  
Como o script trabalha com potências de 2 e números de Mersenne, a análise da sequência mostra que, mesmo com crescimento rápido, os resultados mantêm padrão controlado. Esse comportamento está em sintonia com o Teorema de Montel.

---

## 2. Script `montel_potencias_mersennes.py`

### 2.1 Relação com o Teorema  
O script usa uma **família de funções complexas** construídas com base em potências de 2 e números de Mersenne. Ele mostra que, mesmo com movimentos, rotações e "tremores", o conjunto das funções continua sendo normal — ou seja, o **Teorema de Montel se mantém válido**.

### 2.2 Objetivo do Script  
Criar uma **animação visual** para demonstrar a estabilidade de uma família de funções complexas, mesmo sob transformações dinâmicas:

- Funções rotacionam com base no índice `n`
- Funções múltiplas de 5 têm pequenos deslocamentos oscilatórios ("tremores")
- Tudo isso preservando as condições do teorema

### 2.3 Exemplo de Saída  

O script salva um arquivo chamado:

```
montel\_potencias\_mersennes.gif
```

Este GIF mostra o círculo unitário sendo transformado por várias funções complexas que oscilam de forma controlada.

### 2.4 Funcionamento Interno  

- Cria 11 funções baseadas em potências de 2 (de 0 a 10)
- Gera ângulos com números de Mersenne
- Para cada `n`, faz:
  - Rotação para esquerda (se `n` par)
  - Rotação para direita (se `n` ímpar)
  - Tremor oscilatório (se `n` múltiplo de 5)
- Usa `matplotlib.animation` para criar a animação
- Salva o resultado como um GIF com `pillow`

### 2.5 Tecnologias e Requisitos  

- **Python 3.8.10**
- matplotlib
- numpy
- pillow

Instale com:

```bash
pip install matplotlib numpy pillow
````

---

## 3. Extras

### 3.1 Licença

Distribuído sob a licença MIT.

### 3.2 Referências

* Wikipédia – Teorema de Montel
* Visualizações matemáticas de funções complexas
* Discussões sobre famílias normais na análise complexa

### 3.3 Testes e Validações

Este script foi testado com Python 3.8.10 no Ubuntu. A animação é validada visualmente, mantendo consistência mesmo com transformações temporais.

---

## 4. Contato

* Feito por **CanalQb** no GitHub
* Visite o blog: canalqb.blogspot.com
  👉 [https://canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via **Bitcoin**: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* **PIX**: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**holomorfa**: função suave no plano complexo, sem "quebras" ou cantos
**função complexa**: função que recebe e retorna números com parte real e imaginária
**círculo unitário**: círculo de raio 1 no plano complexo
**número de Mersenne**: número da forma 2^p - 1
**potência de 2**: número da forma 2^n
**múltiplo de 5**: qualquer número que pode ser dividido por 5 sem sobra
**familia normal**: conjunto de funções que têm um comportamento controlado em uma certa região
**animação**: sequência de imagens exibidas rapidamente para mostrar movimento
**GIF**: formato de imagem que suporta animações curtas
