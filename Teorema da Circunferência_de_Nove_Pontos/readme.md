# 🧮 - Circunferência de Nove Pontos com Potências de 2 e Números de Mersenne
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Matemática-Geometria%20Inspirada-ff69b4.svg)](https://en.wikipedia.org/wiki/Nine-point_circle)

## Frase do Conceito

> *Uma construção numérica inspirada na circunferência de nove pontos, combinando potências de dois e números de Mersenne* – *uma ponte entre geometria e aritmética de forma criativa e educativa.*

---

## Sumário

* [1. Introdução ao Conceito](#1-introdução-ao-conceito)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `CircunferenciadeNovePontos.py`](#2-script-circunferenciadenovepontospy)
  * [2.1 Relação com a Geometria](#21-relação-com-a-geometria)
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

## 1. Introdução ao Conceito

### 1.1 Resumo

Esse projeto apresenta um script que simula elementos inspirados na circunferência de nove pontos usando **potências de 2** e seus **números de Mersenne posteriores**.

### 1.2 Exemplos Práticos

- Para `n = 3`, temos `2^3 = 8`, e o próximo número de Mersenne é `31`.
- O script cria relações fictícias com pontos da geometria do triângulo: pontos médios, pés das alturas e pontos médios vértice-ortocentro.

### 1.3 Explicação Detalhada

Na geometria, a circunferência de nove pontos passa por nove locais importantes de um triângulo. Aqui, simulamos isso numericamente:

- Os valores de entrada vêm de potências de 2 (`2^n`)
- Os valores "geométricos" são simulados com operações aritméticas como:
  - Médias
  - Raízes quadradas
  - Combinações lineares

### 1.4 Aplicações

*Didáticas*, *lúdicas* e *exploratórias*. Uma maneira de estimular a curiosidade matemática e conectar áreas diferentes da matemática.

### 1.5 Análise da Tabela

O script gera uma tabela no terminal com as seguintes colunas:

- **Potência base (2^n)**
- **Próximo número de Mersenne**
- **Pontos simulados:**
  - Médios dos lados
  - Pés das alturas
  - Médios vértice-ortocentro

---

## 2. Script `CircunferenciadeNovePontos.py`

### 2.1 Relação com a Geometria

Embora não represente um teorema verdadeiro, o script foi **inspirado no teorema da circunferência de nove pontos**, transformando-o numa simulação numérica com base em potências e primos especiais.

### 2.2 Objetivo do Script

- Iterar valores de `n` de 0 a 10
- Calcular `2^n`
- Identificar o **próximo número de Mersenne**
- Simular 9 pontos relacionados, como se fossem parte de um triângulo

### 2.3 Exemplo de Saída

```

🔢 n = 4
📌 2^4 = 16
🧠 Próximo número de Mersenne = 31 (p = 5)
🟠 Pontos da circunferência de 9 pontos (simulados):
📍 Médios dos lados: \[8.0, 15.5, 23.5]
📍 Pés das alturas: \[4.0, 5.57, 22.27]
📍 Médios vértice-ortocentro: \[11.75, 15.67, 9.4]

```

### 2.4 Funcionamento Interno

1. **`is_prime(n)`** – Verifica se o número é primo
2. **`next_mersenne(n)`** – Encontra o próximo primo de Mersenne após `2^n`
3. **`simulate_nine_point_circle(n, base, mersenne)`** – Simula os pontos geométricos com base nos valores
4. **Loop principal** – Executa a simulação de `n = 0` até `n = 10`

### 2.5 Tecnologias e Requisitos

- **Python 3.8.10**
- Bibliotecas padrão: `math`
- Sem dependências externas

---

## 3. Extras

### 3.1 Licença

Este projeto está sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### 3.2 Referências

- Wikipedia: [Circunferência de Nove Pontos](https://en.wikipedia.org/wiki/Nine-point_circle)
- Wikipedia: [Número de Mersenne](https://en.wikipedia.org/wiki/Mersenne_prime)

### 3.3 Testes e Validações

O script foi executado com sucesso em:

- Python 3.8.10 (Windows)
- Terminal padrão
- Resultados verificados manualmente

---

## 4. Contato

* Feito por **CanalQb** no GitHub  
* Visite o blog: [canalqb.blogspot.com](https://canalqb.blogspot.com)  
* 💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`  
* 📬 PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Mersenne:** número primo da forma `2^p - 1`  
**Ponto médio:** valor central entre dois números, ou seja, `(a + b) / 2`  
**Raiz quadrada:** valor que, multiplicado por si mesmo, dá o número original  
**Circunferência de nove pontos:** conceito geométrico em que nove pontos importantes de um triângulo estão numa mesma circunferência  
**Simulação:** representação aproximada ou simbólica, não exata  
