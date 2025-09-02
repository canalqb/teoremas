# 📐 Teorema Tarski-Exponencial

---

## 🧾 Frase do Teorema

> *"A verdade de uma linguagem formal suficientemente expressiva não é definível dentro dela mesma, e os valores esperados em suas interpretações numéricas crescem de forma controlada entre potências de 2."* – Este teorema delimita a capacidade de definição da verdade e estabelece limites para o crescimento lógico e numérico de propriedades dentro de sistemas formais.

---

## 📚 Sumário

- [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  - [1.1 Resumo](#11-resumo)  
  - [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  - [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  - [1.4 Aplicações](#14-aplicações)  
  - [1.5 Análise da Tabela](#15-análise-da-tabela)  
- [2. Script `tarski_approximation.py`](#2-script-tarski_approximationpy)  
  - [2.1 Relação com o Teorema](#21-relação-com-o-teorema)  
  - [2.2 Objetivo do Script](#22-objetivo-do-script)  
  - [2.3 Exemplo de Saída](#23-exemplo-de-saída)  
  - [2.4 Funcionamento Interno](#24-funcionamento-interno)  
  - [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)  
- [3. Extras](#3-extras)  
  - [3.1 Licença](#31-licença)  
  - [3.2 Referências](#32-referencias)  
  - [3.3 Testes e Validações](#33-testes-e-validações)
- [4 Contato](#4-contato)

---

## 1. Introdução ao Teorema

### 1.1 Resumo

O **Teorema Tarski-Exponencial** é uma aplicação computacional inspirada no Teorema de Tarski original. Ele se propõe a modelar o crescimento controlado de valores esperados dentro de **intervalos exponenciais**, partindo da ideia de que qualquer valor "verdadeiro" deve estar contido entre \(2^N\) e \(2^{N+1} - 1\), respeitando os limites lógicos da linguagem formal onde foi definido.

---

### 1.2 Exemplos Práticos

| N | Início \(2^N\) | Esperado (aproximado) | Fim \(2^{N+1} - 1\) |
|---|----------------|------------------------|---------------------|
| 0 | 1              | 1                      | 1                   |
| 1 | 2              | 3                      | 3                   |
| 2 | 4              | 6                      | 7                   |
| 3 | 8              | 12                     | 15                  |
| 4 | 16             | 25                     | 31                  |
| 5 | 32             | 44                     | 63                  |

Estes valores demonstram que, para cada nível \(N\), o valor resultante ou "esperado" cresce, mas sempre respeita os limites do intervalo definido pelo teorema.

---

### 1.3 Explicação Detalhada

A origem deste teorema está na lógica formal. O **Teorema de Tarski** prova que uma linguagem formal robusta (como a aritmética de Peano) **não pode conter uma definição interna da sua própria verdade**.

Aplicando isso a modelos numéricos, temos que os valores que representam verdades, propriedades ou interpretações **crescem com complexidade**, mas dentro de **intervalos previsíveis**, não arbitrários.

Ou seja, **a verdade não apenas é indefinível internamente, mas também se comporta de forma crescente e contida dentro de fronteiras bem definidas**.

---

### 1.4 Aplicações

Este teorema (e sua adaptação numérica) é aplicado em áreas como:

- **Lógica formal e teoria dos modelos**  
- **Criptografia** — crescimento exponencial como base da segurança  
- **Complexidade computacional** — limites de expressividade e crescimento  
- **Teoria da computação** — análise de máquinas de Turing e limites de prova  
- **Fundamentação matemática** — consistência e completude de sistemas formais

---

### 1.5 Análise da Tabela

A tabela apresentada define para cada \(N\):

- O **início** do intervalo (\(2^N\))  
- O **fim** do intervalo (\(2^{N+1} - 1\))  
- Um valor "esperado" ou calculado, que respeita os limites  

Essa análise mostra que os valores **não crescem linearmente**, mas também **não extrapolam os limites superiores**, criando uma **função de crescimento exponencial controlada** — exatamente o que o Teorema Tarski-Exponencial propõe.

---

## 2. Script `tarski_approximation.py`

---

### 2.1 Relação com o Teorema

O script foi projetado para **representar na prática** a ideia central do Teorema Tarski-Exponencial: **valores crescentes que respeitam intervalos definidos por potências de 2**.

Ele **não usa a coluna "esperado" como entrada**, e sim a deduz com base apenas nos limites dados (\(2^N\) e \(2^{N+1} - 1\)).

---

### 2.2 Objetivo do Script

O script tem como objetivo:

- Gerar uma **aproximação realista** de um valor verdadeiro/esperado para cada \(N\)  
- Demonstrar o crescimento ordenado dentro de intervalos exponenciais  
- Produzir uma **tabela interativa e clara** para análise teórica e prática  

---

### 2.3 Exemplo de Saída

```text
N   | Início (2^N)  | Aproximação  | Fim (2^(N+1))-1
--------------------------------------------------
0   | 1            | 1            | 1              
1   | 2            | 3            | 3              
2   | 4            | 6            | 7              
3   | 8            | 12           | 15             
4   | 16           | 25           | 31             
5   | 32           | 44           | 63             
6   | 64           | 86           | 127            
7   | 128          | 168          | 255            
8   | 256          | 321          | 511            
9   | 512          | 612          | 1023           
````

---

### 2.4 Funcionamento Interno

O script funciona da seguinte maneira:

1. Itera sobre valores de $N$, de 0 até 9.
2. Para cada $N$:

   * Calcula o início do intervalo: $2^N$
   * Calcula o fim do intervalo: $2^{N+1} - 1$
   * Aplica uma fórmula de **média ponderada** para gerar uma aproximação realista dentro do intervalo
3. Imprime uma tabela completa com os resultados

---

### 2.5 Tecnologias e Requisitos

* **Linguagem:** Python 3.x
* **Bibliotecas externas:** Nenhuma
* **Execução:** Via terminal ou script local
* **Compatibilidade:** Windows, Linux, macOS

---

## 3. Extras

---

### 3.1 Licença

Este projeto é distribuído sob a **Licença MIT** — de uso livre para fins acadêmicos, educacionais e de pesquisa.

---

### 3.2 Referências

* Alfred Tarski, *The Semantic Conception of Truth*, 1944
* Stanford Encyclopedia of Philosophy – Tarski's Truth Definitions
* Introdução à Teoria dos Modelos – Wilfrid Hodges
* Problemas de crescimento em algoritmos – Cormen et al.

---

### 3.3 Testes e Validações

Os resultados gerados foram validados manualmente e testados para garantir que:

* Nenhum valor sai dos limites definidos
* Os valores crescem com $N$
* A função de aproximação é **monótona crescente**

---


## 4. 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
