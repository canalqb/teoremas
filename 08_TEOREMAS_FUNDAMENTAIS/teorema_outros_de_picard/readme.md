# 🧩 - De Picard

[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Picard--Lindelöf-ff69b4.svg)](https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem)

## Frase do Teorema

> Se uma equação diferencial for bem comportada, então ela terá uma única solução possível. – Isso significa que, sob certas condições, conseguimos prever exatamente como a solução irá se comportar.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `Picard.py`](#2-script-picardpy)

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

O **teorema de Picard** (ou Picard-Lindelöf) garante que, quando uma equação diferencial simples está bem definida e segue regras previsíveis, ela tem **uma única solução**. Isso é essencial em matemática, física e engenharia.

---

### 1.2 Exemplos Práticos

* Modelos de crescimento populacional.
* Previsão de temperatura em processos térmicos.
* Movimento de um corpo em queda com resistência do ar.

---

### 1.3 Explicação Detalhada

Esse teorema se aplica a equações do tipo:

```
dy/dx = f(x, y)  com condição inicial y(x0) = y0
```

Se a função `f(x, y)` for contínua e não crescer de forma descontrolada (tecnicamente: se satisfizer uma **condição de Lipschitz**), então a solução existe e é única.

---

### 1.4 Aplicações

* Resolver problemas de engenharia com segurança.
* Usar simulações computacionais confiáveis.
* Aplicar métodos numéricos como o de Euler ou Runge-Kutta com garantias de resultado.

---

### 1.5 Análise da Tabela

O script apresenta uma tabela de potências de 2 e seus números de **Mersenne** (2ⁿ - 1):

```
     n  2^n (Início)  Mersenne (Fim)  Distância
     0      1              0              1
     1      2              1              1
     2      4              3              1
     ...
    10   1024           1023              1
```

Todas as distâncias são sempre 1, já que 2ⁿ - (2ⁿ - 1) = 1. Isso mostra um padrão interessante e fixo.

---

## 2. Script `Picard.py`

### 2.1 Relação com o Teorema

O script usa o **método de Picard**, uma forma numérica de resolver equações diferenciais simples, baseado na ideia do teorema.

---

### 2.2 Objetivo do Script

* Mostrar graficamente como o método de Picard aproxima a solução da equação diferencial.
* Ilustrar a relação entre potências de 2 e seus números de Mersenne por meio de curvas.

---

### 2.3 Exemplo de Saída

```
Tabela de distâncias entre potências de 2 e seus Mersennes:

     n  2^n (Início)  Mersenne (Fim)  Distância
     0      1              0              1
     1      2              1              1
     ...
    10   1024           1023              1
```

Em seguida, um gráfico com curvas coloridas mostra as transições entre 2ⁿ e 2ⁿ - 1 com uma curvatura suave.

---

### 2.4 Funcionamento Interno

* Gera os valores de 2ⁿ para `n = 0 até 10`.
* Calcula os números de Mersenne.
* Cria uma tabela com a distância entre eles.
* Plota curvas suaves (arcos) entre cada par (2ⁿ, 2ⁿ - 1).

---

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10**
* Bibliotecas:

  * `numpy`
  * `matplotlib`
  * `pandas`

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a licença **MIT**.

---

### 3.2 Referências

* [Wikipedia - Picard–Lindelöf theorem](https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem)
* [Teoremas clássicos de EDOs](https://pt.wikipedia.org/wiki/Equa%C3%A7%C3%A3o_diferencial_ordin%C3%A1ria)

---

### 3.3 Testes e Validações

* Script testado no terminal Windows.
* Funcionando corretamente com Python 3.8.10.

---

## 4 Contato

* Feito por **CanalQb** no GitHub
* Visite o blog: canalqb.blogspot.com → [https://canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* 📧 PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **Teorema**: uma regra ou verdade matemática que foi provada com lógica e fatos.
* **Equação diferencial**: uma equação que descreve como algo muda (por exemplo, velocidade, temperatura, etc).
* **Lipschitz**: uma condição matemática que garante que a função não muda bruscamente.
* **Mersenne**: um tipo especial de número que é sempre 1 a menos que uma potência de 2.
* **Método de Picard**: um jeito de resolver uma equação passo a passo, usando aproximações.
* **Script**: um pequeno programa feito para rodar uma tarefa específica.
