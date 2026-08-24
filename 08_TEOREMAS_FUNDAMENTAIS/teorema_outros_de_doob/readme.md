# 🧩 - De Doob

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Doob](https://img.shields.io/badge/Teorema-Doob%20com%20Martingales-ff69b4.svg)](https://en.wikipedia.org/wiki/Martingale_(probability_theory))

## Frase do Teorema

> *"O valor esperado futuro de um martingale, condicionado ao presente, é igual ao valor atual."* – Ou seja, **a melhor previsão que conseguimos fazer sobre o futuro, sabendo tudo até agora, é justamente o que temos agora**.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `doob.py`](#2-script-doobpy)
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

## 1 Introdução ao Teorema

### 1.1 Resumo

O **Teorema de Doob** afirma que, ao lidarmos com um processo chamado *martingale*, o valor médio que esperamos no futuro (com base no que sabemos agora) é exatamente o valor atual. Isso significa que **não há tendência** — o processo não tende a subir nem descer no futuro apenas com base no que ocorreu até agora.

### 1.2 Exemplos Práticos

* Um jogo de cara ou coroa onde você ganha +1 ou perde -1 a cada rodada: o dinheiro esperado que você terá no futuro, sabendo quanto tem agora, é exatamente quanto você tem agora.
* Previsões de mercado onde as informações disponíveis já estão embutidas nos preços atuais — o preço esperado no futuro, condicionado ao hoje, é o preço de hoje.

### 1.3 Explicação Detalhada

Um *martingale* é uma sequência de valores ao longo do tempo onde **a média do valor futuro, dado tudo que sabemos até o presente, é o valor atual**.

- Se chamarmos o valor presente de `Mt`, e o futuro de `MT`, então:
```
Média condicional de MT dado Mt = Mt
```
- Isso quer dizer que **o valor presente já é, por si só, a melhor previsão do futuro**, considerando que não há tendências embutidas.

### 1.4 Aplicações

* **Finanças**: avaliação de ativos financeiros em mercados eficientes.
* **Jogos de azar**: estratégias de aposta que não funcionam a longo prazo.
* **Processos estocásticos**: base para muitos teoremas na probabilidade.

### 1.5 Análise da Tabela

O script `doob.py` agrupa as trajetórias por valores similares no tempo `t` (presente) e calcula a média condicional do valor no tempo `T` (futuro). A diferença entre essas duas médias deve ser **pequena**, mostrando que o valor esperado futuro **é igual ao valor presente** — confirmando o Teorema de Doob!

---

## 2 Script `doob.py`

### 2.1 Relação com o Teorema

Este script foi criado **especificamente para demonstrar na prática o Teorema de Doob** usando simulações numéricas com martingales.

### 2.2 Objetivo do Script

Mostrar que, mesmo com centenas de trajetórias aleatórias de um processo sem tendência (martingale), a **média dos valores futuros condicionados ao presente** se aproxima muito do **valor presente**.

### 2.3 Exemplo de Saída

```
## Bin Mt    Média Mt    Média MT  Diferença
   1        1.02        1.01     0.0070
   2        2.05        2.03     0.0180
   3        3.00        3.01     0.0100
...
```

**Interpretação:**  
Para cada grupo de trajetórias com valor `Mt` parecido, o valor médio de `MT` (futuro) é muito próximo de `Mt` (presente). Isso é exatamente o que o **Teorema de Doob** afirma! 🧠✅

### 2.4 Funcionamento Interno

1. Gera `M` trajetórias de um processo com `N` passos, onde cada passo é +1 ou -1 com mesma chance.
2. Seleciona dois tempos: `t` (presente) e `T` (futuro), onde `T > t`.
3. Agrupa os valores de `Mt` em intervalos (bins).
4. Calcula a média de `Mt` e `MT` dentro de cada grupo.
5. Exibe a diferença entre as médias.

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10**
* `numpy`

Para instalar dependências:

```bash
pip install numpy
````

Para executar:

```bash
python doob.py
```

Você pode ajustar os parâmetros diretamente no código:

| Parâmetro | Descrição                       | Valor padrão |
| --------- | ------------------------------- | ------------ |
| `N`       | Número de passos do martingale  | 1000         |
| `M`       | Número de trajetórias simuladas | 500          |
| `t`       | Tempo presente                  | 500          |
| `T`       | Tempo futuro (deve ser > `t`)   | 700          |

---

## 3 Extras

### 3.1 Licença

Distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### 3.2 Referências

* Doob, J.L. (1953). *Stochastic Processes*.
* Williams, D. (1991). *Probability with Martingales*.
* Wikipedia: [Martingale (probability theory)](https://en.wikipedia.org/wiki/Martingale_%28probability_theory%29)

### 3.3 Testes e Validações

Validação empírica via simulações numéricas. A média condicional estimada está **consistentemente próxima do valor atual**, validando o Teorema de Doob.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

🧾 **Termos Explicados de Forma Simples:**

* **Martingale**: processo aleatório onde a média do valor futuro, dado o presente, é igual ao valor atual. Não tem tendência para cima nem para baixo.
* **Condicional**: significa que estamos considerando apenas os cenários onde algo específico aconteceu.
* **Valor esperado**: é a média dos possíveis valores, ponderada pelas chances de acontecerem.
* **Simulação**: gerar dados artificiais por meio de sorteios aleatórios para estudar comportamentos matemáticos.
* **Bins**: agrupamentos por faixas de valores parecidos.
