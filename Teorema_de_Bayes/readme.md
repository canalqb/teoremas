# 📊 - Teorema de Bayes  
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![LGN](https://img.shields.io/badge/Teorema-Teorema%20de%20Bayes-ff69b4.svg)](https://en.wikipedia.org/wiki/Bayes%27_theorem)

## Frase do Teorema

> *A probabilidade de uma hipótese muda quando novas evidências aparecem* – Em outras palavras, podemos atualizar nossa crença sobre algo à medida que novas informações são observadas.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `bayesian_search_estimator.py`](#2-script-bayesian_search_estimatorpy)  
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
O **Teorema de Bayes** é uma ferramenta da estatística que permite atualizar uma estimativa **à medida que novas evidências aparecem**. Ele é essencial em situações onde **não temos certeza absoluta**, mas podemos melhorar nossa previsão com base em dados observados.

### 1.2 Exemplos Práticos  
- Diagnóstico médico com base em sintomas  
- Sistemas de recomendação com base no comportamento do usuário  
- Atualização da busca por um item ou evento escondido (como feito neste script)  

### 1.3 Explicação Detalhada  
Imagine que você está procurando um documento perdido. Inicialmente, você acha que ele pode estar **em qualquer lugar com igual chance**. Ao encontrar pistas, você muda sua suposição. O Teorema de Bayes permite calcular essa **probabilidade atualizada**, que depende:

- Da chance original de estar em cada lugar  
- De quão provável é ver a pista em cada local  

### 1.4 Aplicações  
- Inteligência artificial  
- Análise de risco  
- Jogos e estratégia  
- Buscas em espaços grandes ou desconhecidos  
- Estimativa de localização com base em faixas ou intervalos  

### 1.5 Análise da Tabela  
A tabela mostra como o script estima **onde** está o item procurado, usando apenas os **intervalos de busca** e o tamanho relativo de cada um como _hipótese_. Quanto maior o intervalo, **maior a chance** atribuída a ele, assumindo distribuição uniforme.

---

## 2. Script `bayesian_search_estimator.py`

### 2.1 Relação com o Teorema  
Cada **intervalo** é tratado como uma **hipótese** (`H_i`), e a chance de o item estar ali é proporcional ao seu **tamanho**.  
O script aplica o Teorema de Bayes com **suposições simples**, considerando a **uniformidade** como hipótese base.

### 2.2 Objetivo do Script  
- Estimar, com base em **intervalos**, onde está algo que procuramos  
- Usar apenas a estrutura dos intervalos para estimar a **distribuição da busca**  
- Comparar essa estimativa com a procura **real**, sem usar a real como entrada  

### 2.3 Exemplo de Saída

Comparação entre Procura real e Procura estimado pelo modelo simples:
```text
   Inicio  Fim  Procura_estimado
0       1    2                 1
1       2    4                 3
2       4    8                 6
3       8   16                12
4      16   32                24
5      32   64                49
6      64  128                98
7     128  256               196
````

> 🔍 A estimativa é proporcional ao tamanho de cada faixa e escalada para se aproximar da procura total.

### 2.4 Funcionamento Interno

1. Cria uma tabela com colunas `Inicio` e `Fim`
2. Calcula o **tamanho** de cada intervalo
3. Assume que a chance é proporcional ao tamanho (`P(H)`)
4. Estima o ponto médio como **valor esperado da procura**
5. Escala os resultados para que somem aproximadamente o total real
6. Mostra a tabela final com os valores estimados

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10**
* Bibliotecas necessárias:

  * `pandas`
  * `numpy`

Para instalar:

```bash
pip install pandas numpy
```

---

## 3 Extras

### 3.1 Licença

Este projeto está sob a licença **MIT**. Você pode usar, modificar e distribuir à vontade.

### 3.2 Referências

* Thomas Bayes – matemático que propôs a ideia original
* Aplicações modernas em machine learning, medicina e estatística
* Noções de probabilidade condicional e distribuições a priori

### 3.3 Testes e Validações

* A estimativa foi comparada com uma tabela real
* Resultado qualitativamente semelhante
* Boa aproximação para fins **didáticos e exploratórios**

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Teorema de Bayes:** Permite calcular a chance de algo ser verdadeiro com base em uma evidência observada.

**Hipótese (H):** Uma suposição que queremos testar ou estimar (ex: o item está no intervalo 4–8).

**Probabilidade a priori:** A chance de algo antes de ver a evidência.

**Probabilidade posterior:** A chance de algo **depois** de ver a evidência.

**Verossimilhança:** A chance de ver a evidência **se** a hipótese for verdadeira.

**Distribuição uniforme:** Suposição de que todos os valores têm a mesma chance.

**Valor esperado:** Uma espécie de “média ponderada”, indicando onde esperar encontrar algo.
