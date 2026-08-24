# 🧩 - Leifortedosgrandesnumeros

## Frase do Teorema

> Se pegarmos uma sequência de variáveis aleatórias independentes, com valores médios bem definidos e variâncias controladas, então a **média dessas variáveis** se aproxima cada vez mais do valor médio verdadeiro, à medida que observamos mais dados – com **probabilidade 1**.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `LeiFortedosGrandesNumeros.py`](#2-script-leifortedosgrandesnumerospy)
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

A **Lei Forte dos Grandes Números (LFGN)** diz que, ao calcular a média de muitas observações independentes (como lançamentos de uma moeda ou dados de sensores), essa média **quase sempre** se aproxima do valor real esperado.

Ou seja, se continuarmos observando o sistema, a média amostral **não falha** em chegar no valor certo – **com probabilidade total**.

### 1.2 Exemplos Práticos

- Média de temperatura ao longo dos dias
- Número médio de acessos a um site por hora
- Resultados médios de uma loteria após milhões de sorteios

### 1.3 Explicação Detalhada

Imagine que você joga uma moeda justa milhares de vezes. A média de "caras" tende a se aproximar de 0.5.

A LFGN diz que, **com probabilidade igual a 1**, essa média vai mesmo se estabilizar em 0.5, mesmo que leve um tempo. Isso acontece porque:

- As variáveis são **independentes**
- Elas têm uma **esperança** (média teórica) bem definida
- A **variância** (desvio médio ao quadrado) não cresce demais

### 1.4 Aplicações

- Controle de qualidade na indústria
- Estimativas de risco no mercado financeiro
- Análise de confiabilidade em sistemas estatísticos

### 1.5 Análise da Tabela

O script mostra o comportamento da média amostral em pontos estratégicos:

- **Potências de 2**: 2, 4, 8, 16, ...
- **Números de Mersenne**: 3, 7, 15, 31, ...

Esses pontos ajudam a acompanhar o progresso da média e mostram como ela vai se aproximando do valor teórico.

---

## 2. Script `LeiFortedosGrandesNumeros.py`

### 2.1 Relação com o Teorema

O script demonstra, na prática, o que o teorema diz: conforme o número de amostras aumenta, a média das observações se estabiliza próximo da média verdadeira.

### 2.2 Objetivo do Script

- Gerar uma sequência de variáveis aleatórias (ex: normais com média 0)
- Calcular a média amostral em **pontos específicos**
- Comparar a média com a **média teórica esperada**
- Exibir os resultados em **tabela e gráfico**

### 2.3 Exemplo de Saída

```plaintext
N (ponto)      Média Amostral
------------------------------
2              0.137
3              0.501
4              0.233
7              0.291
8              0.121
15             0.071
...
````

E um gráfico como:

* Eixo X: número de amostras (N)
* Eixo Y: média amostral
* Linha horizontal mostrando a **média esperada (mu)**

### 2.4 Funcionamento Interno

O script:

1. Gera `N` observações com distribuição padrão (ex: normal com média 0)
2. Calcula a média amostral nos pontos `2^A` e `2^{A+1} - 1`
3. Armazena os pares (N, média)
4. Plota o gráfico da média amostral vs. número de amostras

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10**
* Bibliotecas necessárias:

```bash
pip install numpy pandas matplotlib
```

---

## 3 Extras

### 3.1 Licença

Este projeto é open source para fins educacionais.
Distribuição livre com créditos mantidos.

### 3.2 Referências

* Kolmogorov, A. N. – *Strong Law of Large Numbers*
* Feller, W. – *An Introduction to Probability Theory*
* Shiryaev, A. – *Probability*

### 3.3 Testes e Validações

* O código foi testado com diferentes distribuições e tamanhos de amostras
* O gráfico mostra convergência mesmo em sequências pequenas (\~2^10)
* Resultados confirmam visualmente a Lei Forte dos Grandes Números

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

### Explicações Simples de Termos Técnicos

* **Variável aleatória**: é um valor que muda com base em algum processo incerto (ex: lançamento de dado).
* **Esperança (ou valor esperado)**: é a média teórica de uma variável aleatória – o que você espera obter, em média.
* **Variância**: mede o quanto os valores se espalham em torno da média.
* **Convergência quase certa**: significa que, com probabilidade 1, a sequência se aproxima do valor verdadeiro.
* **Número de Mersenne**: números da forma `2^n - 1`, usados por terem propriedades especiais em matemática.
* **i.i.d.**: variáveis **independentes e com mesma distribuição**, como repetições de um experimento idêntico.

--- 
