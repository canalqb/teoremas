# 🧩 - Teorema Seifert–van Kampen

[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Seifert–van%20Kampen-ff69b4.svg)](https://en.wikipedia.org/wiki/Seifert%E2%80%93van_Kampen_theorem)

## Frase do Teorema

> O teorema de Seifert–van Kampen permite **"colar" espaços topológicos** ao conhecer suas partes e a forma como elas se sobrepõem – ele nos diz como reconstruir um espaço maior a partir de pedaços menores conectados.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `seifert_van_kampen_mersenne.py`](#2-script-seifert_van_kampen_mersennepy)

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

O **Teorema de Seifert–van Kampen** é uma ideia central da **topologia algébrica** que descreve como entender um espaço grande baseado em espaços menores que se unem. No nosso exemplo, usamos **intervalos de potências de 2** e **números de Mersenne** para simular esse processo de "colagem".

---

### 1.2 Exemplos Práticos

Ao rodar o script, obtemos saídas como estas:

```
=== Seifert–van Kampen simbólico para n = 0 ===
U               = [1]
V               = [2, 3]
U ∩ V (Mersenne)= [1]
U ∪ V (colado)  = [1, 2, 3]
```

Cada linha representa:

* Um conjunto **U** representando um pedaço do espaço.
* Um conjunto **V** representando outro pedaço.
* Um **ponto comum** entre eles, que simboliza a "cola".
* A **união colada**, que junta os dois sem repetições.

---

### 1.3 Explicação Detalhada

*U* e *V* são intervalos que crescem com potências de 2:

* U = intervalo de 2^n até 2^(n+1) - 1
* V = intervalo de 2^(n+1) até 2^(n+2) - 1

A interseção entre eles é feita por um número especial chamado **número de Mersenne**, que é 2^(n+1) - 1. Esse número representa o elo de ligação entre os dois conjuntos.

---

### 1.4 Aplicações

Apesar de simbólico, esse modelo ajuda a entender:

* Como espaços podem se conectar.
* A ideia de **sobreposição e união controlada**.
* Conceitos básicos de **topologia**, **colagem** e **relações entre conjuntos**.

---

### 1.5 Análise da Tabela

| n | U             | V                | U ∩ V (Mersenne) | U ∪ V (colado)      |
| - | ------------- | ---------------- | ---------------- | ------------------- |
| 0 | \[1]          | \[2, 3]          | \[1]             | \[1, 2, 3]          |
| 1 | \[2, 3]       | \[4, 5, 6, 7]    | \[3]             | \[2, 3, 4, 5, 6, 7] |
| 2 | \[4, 5, 6, 7] | \[8, 9, ..., 15] | \[7]             | \[4, 5, ..., 15]    |

---

## 2. Script `seifert_van_kampen_mersenne.py`

### 2.1 Relação com o Teorema

O script simula o processo de união de espaços pela lógica do Teorema de Seifert–van Kampen, mas em **forma discreta e numérica**, facilitando o entendimento.

---

### 2.2 Objetivo do Script

Mostrar como conjuntos separados podem ser **"colados"** usando um ponto de interseção, representado pelo **número de Mersenne**, gerando uma união coerente entre os conjuntos.

---

### 2.3 Exemplo de Saída

Rodando o script, você verá saídas como estas para diferentes valores de `n`:

```
=== Seifert–van Kampen simbólico para n = 2 ===
U               = [4, 5, 6, 7]
V               = [8, 9, 10, 11, 12, 13, 14, 15]
U ∩ V (Mersenne)= [7]
U ∪ V (colado)  = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
```

---

### 2.4 Funcionamento Interno

Principais funções:

* `intervalo_potencia(n)`: retorna os números de 2^n até 2^{n+1} - 1.
* `numero_mersenne(n)`: calcula 2^n - 1, o elo de ligação entre U e V.
* `aplicar_teorema_svkm(n)`: monta U, V, interseção e a união "colada".
* `imprimir_resultado(...)`: exibe os resultados de forma formatada.

---

### 2.5 Tecnologias e Requisitos

* **Python**: 3.8.10
* Nenhuma biblioteca externa necessária
* Pode ser executado diretamente em terminal ou IDE

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a licença MIT.

---

### 3.2 Referências

* Wikipedia: [Seifert–van Kampen](https://en.wikipedia.org/wiki/Seifert%E2%80%93van_Kampen_theorem)
* Números de Mersenne: [Wikipedia](https://pt.wikipedia.org/wiki/N%C3%BAmero_de_Mersenne)

---

### 3.3 Testes e Validações

Rodado manualmente com `n = 0`, `1` e `2`. As saídas foram validadas conforme esperado.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)
  *Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Topologia algébrica**:
Área da matemática que estuda formas e espaços usando ferramentas de álgebra.

**Colagem**:
Processo de unir dois espaços ou conjuntos usando um ponto ou região comum.

**Número de Mersenne**:
Número da forma 2^n - 1. Chamado assim por causa do matemático Marin Mersenne.

**Interseção**:
É o que os conjuntos U e V têm em comum.

**União colada**:
A junção dos conjuntos U e V, considerando o ponto de interseção como ligação.
