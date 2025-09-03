# 🧩 - Teorema de Regularidade de Kolmogorov

[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Kolmogorov](https://img.shields.io/badge/Teorema-Regularidade%20de%20Kolmogorov-ff69b4.svg)](https://en.wikipedia.org/wiki/Kolmogorov_continuity_theorem)

## Frase do Teorema

> Se os incrementos de um processo aleatório são controlados estatisticamente por uma certa média elevada a uma potência, então suas trajetórias serão suaves — ou seja, não vão ter "saltos" bruscos.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `kolmogorov_regularity_brownian_demo.py`](#2-script-kolmogorov_regularity_brownian_demopy)
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

O **Teorema de Regularidade de Kolmogorov** garante que, se os **incrementos** de um processo aleatório são "estatisticamente suaves", então o processo terá **trajetórias contínuas e bem comportadas**.

Ele responde à pergunta: *"Será que essa simulação aleatória não vai gerar caminhos com saltos e quebras?"*  
Resposta: *Depende da média dos incrementos.*

### 1.2 Exemplos Práticos

- O **movimento browniano** é um processo que **satisfaz** as condições do teorema.
- Se a média de |X_t - X_s|^2 for proporcional a |t - s|, temos suavidade.
- Em simulações com passos pequenos, as trajetórias não se tornam "caóticas".

### 1.3 Explicação Detalhada

Se existir uma **constante positiva** C tal que, ao calcular a média de |X_t - X_s|^α (por exemplo, α = 2), o resultado seja menor que C * |t - s|^{1 + β}, então o processo tem trajetórias suaves com uma regularidade chamada **Hölder**.

Na prática:  
*Quanto menores os incrementos médios (em potências), mais suave o caminho.*

### 1.4 Aplicações

- Física (modelos de difusão)
- Finanças (modelagem de preços)
- Processamento de sinais e imagens
- Matemática pura (existência de versões contínuas)
- Simulações com ruídos aleatórios

### 1.5 Análise da Tabela

O script avalia incrementos em **intervalos dobrados** (por exemplo, de 2 a 3, depois 4 a 7, 8 a 15, etc.).  
Essas médias **mostram como o processo se comporta em diferentes escalas de tempo**.  
É esperado que os valores médios dos incrementos **diminuam suavemente** com o tamanho do intervalo, demonstrando a regularidade das trajetórias.

---

## 2. Script `kolmogorov_regularity_brownian_demo.py`

### 2.1 Relação com o Teorema

O script simula trajetórias de movimento browniano e verifica, de forma empírica, se a condição do teorema está sendo satisfeita ao observar os **incrementos médios elevados a uma potência**.

### 2.2 Objetivo do Script

Mostrar visualmente e numericamente que **quanto maior o intervalo**, **menor a média dos incrementos elevados**, o que é exatamente o que o Teorema de Kolmogorov prevê para garantir trajetórias contínuas.

### 2.3 Exemplo de Saída

```plaintext
Intervalo [2, 3]: Média dos incrementos (alpha=2) = 0.019
Intervalo [4, 7]: Média = 0.017
Intervalo [8, 15]: Média = 0.009
Intervalo [16, 31]: Média = 0.004
...
````

Gráficos gerados:

* 📈 **Trajetórias simuladas** do movimento browniano
* 📉 **Gráfico log-log** da média dos incrementos vs. tamanho do intervalo

### 2.4 Funcionamento Interno

1. Simula **várias trajetórias** de movimento browniano (ex: 10 trajetórias com 2048 passos).
2. Para cada intervalo `[2^n, 2^{n+1} - 1]`, calcula a média de |X\_t - X\_s|^alpha.
3. Armazena os resultados e gera **gráficos explicativos**.
4. Relaciona com a regularidade prevista no teorema.

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10**
* Bibliotecas usadas:

```bash
pip install numpy matplotlib
```

---

## 3 Extras

### 3.1 Licença

Este projeto está sob a [MIT License](LICENSE).

### 3.2 Referências

* Kolmogorov, A.N. (1940). *Wienersche Spiralen und einige andere interessante Kurven im Hilbertschen Raum*.
* Revuz, D. & Yor, M. (1999). *Continuous Martingales and Brownian Motion*.
* Kallenberg, O. (2002). *Foundations of Modern Probability*.

### 3.3 Testes e Validações

* Verificações visuais por gráficos
* Valores médios consistentes com o teorema
* Regularidade confirmada empiricamente

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

### Termos Técnicos Explicados

* **Incremento**: diferença entre o valor de um processo em dois instantes (ex: X\_t - X\_s).
* **Média dos incrementos**: valor esperado (esperança) dos incrementos elevados a uma potência.
* **Hölder-contínuo**: tipo de suavidade que limita a variação do processo com o tempo.
* **Trajetória**: o "caminho" ou gráfico gerado por um processo estocástico.
* **Processo estocástico**: sequência de valores gerados ao longo do tempo com componentes aleatórias.
* **Log-log**: gráfico que usa escala logarítmica em ambos os eixos, útil para analisar comportamentos em escalas diferentes.
* **Esperança matemática**: valor médio esperado de uma variável aleatória.
* **Potência de 2**: intervalo como 2, 4, 8, 16, ... utilizado para explorar diferentes escalas.

---
