# 🧩 - Kolmogorov Convergente

## Frase do Teorema

> Se a **variância total** de uma sequência de variáveis aleatórias independentes for **finita**, então a soma dessa sequência **não explode**: ela converge com **certeza total** (ou seja, com probabilidade 1).

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `KolmogorovConvergente.py`](#2-script-kolmogorov_convergentepy)
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

O **Teorema de Kolmogorov** sobre séries convergentes afirma que:

> Se somarmos variáveis aleatórias independentes, cada uma com **valor médio zero** e variância suficientemente pequena, a soma **vai convergir** com certeza total.

Ou seja, mesmo com infinitos termos, conseguimos controlar o resultado **se o desvio total estiver sob controle**.

### 1.2 Exemplos Práticos

- Modelar ruídos em sinais digitais que somados não afetam a estabilidade do sistema.
- Estimar flutuações financeiras ao longo do tempo com segurança.
- Analisar erros acumulados em medições repetidas de sensores.

### 1.3 Explicação Detalhada

O teorema exige que cada variável aleatória tenha:

- **Esperança (média)** igual a **zero**  
- **Variância (medida da dispersão)** que seja **finita**

Se a **soma de todas as variâncias** for um número finito (ex: 3.57 ou 11.2), então a soma das variáveis aleatórias também **será um número fixo**, com **probabilidade total**.

**"Quase certamente"** significa: o evento acontece com **probabilidade 1**, embora eventos extremamente raros ainda possam ocorrer.

### 1.4 Aplicações

- Probabilidade teórica
- Estatística robusta
- Inteligência artificial (processamento de ruídos)
- Criptografia e análise de sinais

### 1.5 Análise da Tabela

O script gera uma tabela onde:

- Cada linha representa um **intervalo de potências de 2** (como de 4 a 7, ou de 8 a 15)
- Calcula-se a **soma de variáveis aleatórias** nesse intervalo
- Compara-se o **ponto médio** com essa soma
- Observa-se como essa soma **permanece sob controle**, sem crescer demais

---

## 2. Script `KolmogorovConvergente.py`

### 2.1 Relação com o Teorema

O script **demonstra na prática** o Teorema de Kolmogorov:

- Cria variáveis aleatórias com variância que **decresce com n**
- Garante que a soma das variâncias seja finita
- Mostra que a **soma total se estabiliza**, como o teorema prevê

### 2.2 Objetivo do Script

* Simular somas parciais de variáveis aleatórias
* Usar intervalos do tipo `[2^{A-1}, 2^A - 1]` para diferentes valores de A
* Mostrar graficamente que a série converge
* Relacionar com o ponto médio do intervalo (centro de convergência)

### 2.3 Exemplo de Saída

```

2^A	Intervalo		Ponto\_Médio	Soma Aleatória
2	\[2, 3]		2.5		0.24678
4	\[4, 7]		5.5		-0.15694
8	\[8, 15]		11.5		0.02413
...

````

### 2.4 Funcionamento Interno

O script:

1. Define um intervalo com base em potências de 2
2. Para cada `n` no intervalo:
   * Gera um número aleatório `X_n` com valor médio 0
   * Variância igual a `1 / n^1.5` (decai rápido)
3. Soma os `X_n` e registra o ponto médio e o valor total
4. Plota um gráfico com ponto médio vs. soma
5. Mostra visualmente a **convergência** das somas

### 2.5 Tecnologias e Requisitos

- **Python 3.8.10**
- **Bibliotecas necessárias**:

```bash
pip install numpy matplotlib
````

---

## 3 Extras

### 3.1 Licença

Este projeto é de **domínio público educacional**.
Pode ser usado, adaptado e distribuído livremente.

### 3.2 Referências

* Kolmogorov, A. N. (1933). *Foundations of the Theory of Probability.*
* Shiryaev, A. N. (1996). *Probability.*

### 3.3 Testes e Validações

* Verificações manuais da convergência foram feitas comparando diferentes potências.
* A variância escolhida (1/n^1.5) garante que a soma total da variância seja finita.
* Resultados consistentes com a teoria e literatura.

---

## 4 Contato

* Feito por **CanalQb** no GitHub
* Visite o blog: [canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

### Termos Técnicos Explicados

* **Variância**: medida de quão longe os valores estão da média. Quanto maior a variância, mais espalhados os valores estão.
* **Esperança** (ou média esperada): valor médio que uma variável tende a assumir após muitas repetições.
* **Quase certamente**: um evento que acontece com **probabilidade total (100%)**, exceto em casos raríssimos.
* **Convergência**: significa que a soma **se estabiliza** e não cresce indefinidamente.
* **Variável aleatória**: um número que surge de um experimento com incerteza, como o resultado de um dado.
* **Potências de 2**: números como 2, 4, 8, 16, 32, etc. Muito usados em ciência da computação e análise de algoritmos.

---
