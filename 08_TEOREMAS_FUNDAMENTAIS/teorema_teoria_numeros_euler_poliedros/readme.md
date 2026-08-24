# 🧩 - Numeros Euler Poliedros
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Euler%20para%20Poliedros-ff69b4.svg)](https://pt.wikipedia.org/wiki/Caracter%C3%ADstica_de_Euler)

## Frase do Teorema

> Em qualquer poliedro convexo, o número de vértices menos o número de arestas mais o número de faces sempre resulta em 2. – Uma regra simples que mostra como os cantos, lados e superfícies de um sólido estão conectados.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `teorema_euler_verificador.py`](#2-script-verificar_eulerpy)
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

O **Teorema de Euler para poliedros convexos** é uma fórmula que relaciona:

- O número de *vértices* (cantos),
- O número de *arestas* (linhas que ligam os cantos),
- E o número de *faces* (superfícies planas).

A fórmula é:

```

V - A + F = 2

```

Ou seja, o número de vértices menos o número de arestas mais o número de faces sempre dá 2.

---

### 1.2 Exemplos Práticos

🔹 **Cubo**  
- Vértices: 8  
- Arestas: 12  
- Faces: 6  
- Resultado: 8 - 12 + 6 = 2 ✅

🔹 **Tetraedro**  
- Vértices: 4  
- Arestas: 6  
- Faces: 4  
- Resultado: 4 - 6 + 4 = 2 ✅

---

### 1.3 Explicação Detalhada

Essa regra funciona para qualquer *poliedro convexo*, ou seja, uma figura sólida em que todas as suas partes "apontam para fora" (sem buracos ou dobras para dentro). O teorema mostra que, mesmo que mudemos o tamanho ou o formato das partes, a relação entre vértices, arestas e faces continua a mesma.

---

### 1.4 Aplicações

- ✔️ Verificação da consistência de modelos 3D
- ✔️ Ensino de geometria e topologia
- ✔️ Análise de formas em design gráfico e jogos
- ✔️ Programas de modelagem matemática

---

### 1.5 Análise da Tabela

| Poliedro     | Vértices (V) | Arestas (A) | Faces (F) | V - A + F |
|--------------|--------------|-------------|-----------|-----------|
| Tetraedro    | 4            | 6           | 4         | 2         |
| Cubo         | 8            | 12          | 6         | 2         |
| Octaedro     | 6            | 12          | 8         | 2         |
| Icosaedro    | 12           | 30          | 20        | 2         |
| Dodecaedro   | 20           | 30          | 12        | 2         |

---

## 2. Script `teorema_euler_verificador.py`

### 2.1 Relação com o Teorema

O script aplica diretamente a fórmula de Euler para verificar se os dados inseridos sobre um poliedro são consistentes com essa regra.

---

### 2.2 Objetivo do Script

✅ Permitir que qualquer pessoa insira os valores de **vértices**, **arestas** e **faces** e veja se a relação do Teorema de Euler é verdadeira para aquele caso.

---

### 2.3 Exemplo de Saída

```bash
=== Verificador do Teorema de Euler (Poliedros) ===
Digite o número de vértices (V): 8
Digite o número de arestas (A): 12
Digite o número de faces (F): 6

V - A + F = 8 - 12 + 6 = 2
✅ O Teorema de Euler é satisfeito!
````

---

### 2.4 Funcionamento Interno

O código solicita ao usuário três números inteiros: V, A e F.
Ele calcula a expressão `V - A + F` e verifica se o resultado é igual a 2.

---

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10**
* Código simples, sem bibliotecas externas

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

### 3.2 Referências

* Wikipedia: [Características de Euler](https://pt.wikipedia.org/wiki/Caracter%C3%ADstica_de_Euler)
* Khan Academy: "Poliedros e suas características"
* Livro: *A Matemática e Suas Aplicações*, de Eliezer e outros

---

### 3.3 Testes e Validações

Foram testados os cinco sólidos de Platão, além de poliedros criados manualmente. Todos retornaram corretamente **2** para `V - A + F`.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Convexo:**
Uma forma é convexa quando nenhuma parte dela está "afundada" para dentro. Imagine uma bexiga cheia de ar.

**Poliedro:**
Sólido tridimensional com faces planas, como cubos, pirâmides e prismas.

**Face:**
Cada uma das superfícies planas de um poliedro.

**Aresta:**
Segmento de linha onde duas faces se encontram.

**Vértice:**
Ponto onde três ou mais arestas se encontram.

**Euler:**
Matemático suíço (1707–1783) que contribuiu para muitas áreas da matemática, inclusive geometria e topologia.
