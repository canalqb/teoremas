# 📊 - Teorema Central do Limite (TCL)
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Teorema%20Central%20do%20Limite-ff69b4.svg)](https://en.wikipedia.org/wiki/Central_limit_theorem)

## Frase do Teorema

> Quando coletamos várias amostras aleatórias e calculamos suas médias, essas médias começam a se comportar como uma distribuição normal – mesmo que os dados originais não sejam normais!

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `valida_tcl_intervalos.py`](#2-script-valida_tcl_intervalospy)
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

O **Teorema Central do Limite (TCL)** mostra como, mesmo quando temos dados de uma **distribuição qualquer**, se pegarmos **muitas amostras aleatórias** e **fizermos a média de cada uma**, essas médias vão **formar uma curva normal (sino)**.

### 1.2 Exemplos Práticos

- Dados de vendas diárias, altura de pessoas, tempo de resposta de um site, etc.
- Mesmo que os dados brutos sejam "bagunçados", a média de várias amostras começa a se alinhar com a forma da distribuição normal.

### 1.3 Explicação Detalhada

Imagine que temos uma população com média `mu` e desvio padrão `sigma`.  
Se pegarmos várias amostras com `n` elementos e calcularmos a média de cada amostra, essas médias vão se comportar como uma **nova distribuição normal**, com:

- Média = `mu`
- Desvio padrão = `sigma / sqrt(n)`

Ou seja, quanto maior o tamanho da amostra, **menor a variação entre as médias**.

### 1.4 Aplicações

- Validação de intervalos de confiança
- Justificativa para uso da distribuição normal em estatísticas
- Análise de dados em grandes volumes
- Qualidade industrial, pesquisa clínica, IA, etc.

### 1.5 Análise da Tabela

A tabela usada no script mostra:

- Quantas "procuras" (simulações) foram feitas
- Qual o **tamanho da amostra**
- E quantas médias **caíram no intervalo** entre -0.1 e +0.1

O padrão que surge: quanto maior o tamanho da amostra, **mais médias caem perto de zero**, confirmando o TCL.

---

## 2. Script `valida_tcl_intervalos.py`

### 2.1 Relação com o Teorema

O script mostra, na prática, que **a média de várias amostras** se aproxima da média real da população conforme o tamanho das amostras aumenta.

### 2.2 Objetivo do Script

Validar o Teorema Central do Limite através de **simulações numéricas**, contando **quantas médias caem dentro de um intervalo fixo**.

### 2.3 Exemplo de Saída

```text
Amostra de tamanho   1, procuras:   1 -> Proporção dentro do intervalo esperado: 0.00
Amostra de tamanho   2, procuras:   3 -> Proporção dentro do intervalo esperado: 0.33
Amostra de tamanho   4, procuras:   7 -> Proporção dentro do intervalo esperado: 0.00
Amostra de tamanho   8, procuras:   8 -> Proporção dentro do intervalo esperado: 0.38
Amostra de tamanho  16, procuras:  21 -> Proporção dentro do intervalo esperado: 0.24
Amostra de tamanho  32, procuras:  49 -> Proporção dentro do intervalo esperado: 0.41
Amostra de tamanho  64, procuras:  76 -> Proporção dentro do intervalo esperado: 0.63
Amostra de tamanho 128, procuras: 224 -> Proporção dentro do intervalo esperado: 0.63
````

🔍 Perceba que os valores **se estabilizam** e **aumentam** conforme o tamanho da amostra cresce.

### 2.4 Funcionamento Interno

1. Para cada linha da tabela:

   * Define `n` (tamanho da amostra) e `k` (quantas amostras sortear)
2. Sorteia `k` amostras aleatórias com `n` números da **distribuição normal padrão**
3. Calcula a média de cada amostra
4. Verifica se ela está no intervalo entre `-0.1` e `+0.1`
5. Conta a **proporção de acertos**

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10**
* Bibliotecas usadas:

```bash
pip install numpy matplotlib
```

* Para executar:

```bash
python valida_tcl_intervalos.py
```

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

### 3.2 Referências

* [Khan Academy – Teorema Central do Limite](https://pt.khanacademy.org/math/statistics-probability/sampling-distributions-library)
* [Wikipedia – Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem)

### 3.3 Testes e Validações

* Testado em Windows e Linux
* Resultados conferem com teoria do TCL
* Tabela e lógica replicável com outras distribuições

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

* **Média (mu)**: valor central dos dados.
* **Desvio padrão (sigma)**: medida da variação dos dados.
* **sqrt(n)**: significa "raiz quadrada de n".
* **Amostra**: subconjunto dos dados escolhidos aleatoriamente.
* **Distribuição normal**: gráfico em forma de sino que representa dados bem distribuídos ao redor da média.
* **Distribuição**: como os dados se espalham.
* **Intervalo de confiança**: faixa onde a média esperada deve cair com certa segurança.
* **População**: o conjunto total de dados.
* **Proporção dentro do intervalo**: fração das médias que ficaram próximas da média real.

--- 
