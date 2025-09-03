# 🎯📊 - Teorema de Neyman–Pearson

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Estat%C3%ADstica-ff69b4.svg)](https://en.wikipedia.org/wiki/Neyman%E2%80%93Pearson_lemma)

## Frase do Teorema

> O melhor teste para decidir entre duas hipóteses é aquele que maximiza a chance de detectar a hipótese correta para um erro fixo – é como um radar superafiado para a verdade!

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `Teorema_de_Neyman_Pearson.py`](#2-script-teorema_de_neyman_pearsonpy)

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

O **Teorema de Neyman–Pearson** é uma ferramenta fundamental da estatística para decidir entre duas hipóteses de forma *mais eficiente possível*. Ele define qual é o melhor teste para maximizar a chance de detectar a hipótese verdadeira, mantendo o erro sob controle.

### 1.2 Exemplos Práticos

Imagine que você quer detectar se uma máquina está funcionando bem ou com defeito, baseado em medições. O teorema ajuda a criar um teste que, dado um nível de erro aceitável, maximize a chance de identificar corretamente o defeito.

### 1.3 Explicação Detalhada

A ideia central é comparar a razão entre as chances (probabilidades) dos dados acontecerem sob cada hipótese. Se essa razão for maior que um limite definido, rejeitamos a hipótese nula (H0). Assim, temos o teste *mais poderoso* para essa decisão.

### 1.4 Aplicações

* Testes estatísticos para decisões médicas, industriais ou financeiras.
* Construção de detectores em engenharia e ciência de dados.
* Modelagem e previsão baseada em dados reais.

### 1.5 Análise da Tabela

Na tabela a seguir, mostramos dados reais e valores previstos pelo modelo de regressão aplicado para entender e prever a variável y com base em x:

| x     | y (real) | y (previsto) | z     |
| ----- | -------- | ------------ | ----- |
| 1     | 1        | -172         | 1     |
| 2     | 3        | -171         | 3     |
| 4     | 7        | -168         | 7     |
| 8     | 8        | -162         | 15    |
| 16    | 21       | -150         | 31    |
| 32    | 49       | -125         | 63    |
| 64    | 76       | -77          | 127   |
| 128   | 224      | 18           | 255   |
| 256   | 467      | 210          | 511   |
| 512   | 514      | 595          | 1023  |
| 1024  | 1155     | 1366         | 2047  |
| 2048  | 2683     | 2912         | 4095  |
| 4096  | 5216     | 6020         | 8191  |
| 8192  | 10544    | 12301        | 16383 |
| 16384 | 26867    | 25126        | 32767 |
| 32768 | 51510    | 51821        | 65535 |

*Observação:* Para valores pequenos de x, o modelo previu valores negativos, o que não é realista, indicando que o modelo pode ser melhorado.

---

## 2. Script `Teorema_de_Neyman_Pearson.py`

### 2.1 Relação com o Teorema

O script utiliza conceitos inspirados no Teorema de Neyman–Pearson para ajustar um modelo matemático que permite prever valores e testar hipóteses com base em dados observados.

### 2.2 Objetivo do Script

* Receber dados em tripletas (x, y, z), onde x e z são potências de 2 e y é a variável alvo.
* Ajustar uma regressão polinomial de grau 2 para estimar y a partir de x.
* Fazer previsões para novos valores de x, como 65536.
* Comparar valores reais e previstos para avaliar o modelo.

### 2.3 Exemplo de Saída

```
x     | y (real) | y (previsto)
--------------------------------
65536 | 95823    | 109397
```

O modelo superestimou o valor real, sugerindo que ajustes mais complexos podem ser necessários.

### 2.4 Funcionamento Interno

* Recebe os dados de entrada.
* Utiliza regressão polinomial de grau 2 para ajustar uma curva aos dados (modelo quadrático).
* Aplica o modelo para prever valores futuros.
* Imprime os resultados reais e previstos para comparação.

### 2.5 Tecnologias e Requisitos

* Desenvolvido em **Python 3.8.10**.
* Depende da biblioteca **numpy** e **scikit-learn** para regressão polinomial.

---

## 3 Extras

### 3.1 Licença

Este projeto está sob a **licença MIT**, que permite uso, modificação e distribuição livre.

### 3.2 Referências

* [Neyman–Pearson lemma - Wikipedia](https://en.wikipedia.org/wiki/Neyman%E2%80%93Pearson_lemma)
* Documentação oficial do scikit-learn.
* Livros introdutórios de estatística e modelagem.

### 3.3 Testes e Validações

Testar o modelo comparando previsões para dados conhecidos e verificando se os erros são aceitáveis. Tentar melhorar o ajuste com modelos mais complexos quando necessário.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **Hipótese (H0, H1):** suposições que queremos testar (por exemplo, algo está certo ou errado).
* **Verossimilhança:** chance dos dados acontecerem sob uma hipótese.
* **Regressão polinomial:** técnica para ajustar uma curva aos dados, aqui uma curva de segundo grau (parábola).
* **Previsão:** valor estimado para dados futuros com base no modelo ajustado.
