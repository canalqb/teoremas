# 🧮 - Teorema Complexidade de Kolmogorov

## 🧾 Frase do Teorema

> A maioria das strings binárias de tamanho *n* são **incompressíveis**, ou seja, não podem ser geradas por um programa mais curto que elas mesmas – refletindo o *teorema da incompressibilidade* da complexidade de Kolmogorov.

## 📚 Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `KolmogorovComplexity.py`](#2-script-kolmogorov_simulationpy)
  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3 Extras](#3-extras)
  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referencias)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4 📬 Contato](#4-📬-contato)
* [5. Nota](#5-nota)

---

# 1. Introdução ao Teorema

## 1.1 Resumo

A **complexidade de Kolmogorov** mede o tamanho do menor programa capaz de gerar uma dada string. O teorema da incompressibilidade afirma que, para strings longas, a maioria é **incompressível** — seu menor programa é tão grande quanto a própria string.

## 1.2 Exemplos Práticos

Considere uma string binária aleatória muito longa. É praticamente impossível encontrar um programa que a gere com menos bits do que seu próprio tamanho.

## 1.3 Explicação Detalhada

Isso acontece porque o número de programas curtos possíveis é muito menor que o número total de strings longas possíveis, logo a maioria das strings não pode ser produzida por programas curtos.

## 1.4 Aplicações

Esse conceito é fundamental em teoria da informação, compressão de dados, criptografia e na análise da aleatoriedade de sequências.

## 1.5 Análise da Tabela

O script gera uma tabela mostrando:

| Coluna             | Significado                                                |
|--------------------|------------------------------------------------------------|
| `2^A`              | Quantidade de programas possíveis com até `A` bits        |
| `PROCURANDO`       | Número máximo de strings geradas por esses programas      |
| `2^(A+1)-1`        | Maior valor representável com `A+1` bits                   |
| `% Incompressíveis` | Percentual de strings que **não podem ser geradas** por programas ≤ A bits |

Essa tabela ilustra quantitativamente a impossibilidade de compressão para a maioria das strings.

---

# 2. Script `KolmogorovComplexity.py`

## 2.1 Relação com o Teorema

O script simula o teorema da incompressibilidade mostrando como o número de programas curtos é insuficiente para gerar todas as strings longas possíveis.

## 2.2 Objetivo do Script

Gerar e exibir uma tabela simples para demonstrar a relação entre o tamanho dos programas e a quantidade de strings geráveis, evidenciando a grande proporção de strings incompressíveis.

## 2.3 Exemplo de Saída

```

## A  | 2^A      | PROCURANDO | 2^(A+1)-1 | % Incompressíveis

1  | 2        | 2          | 3         | 33.33%
2  | 4        | 4          | 7         | 42.86%
3  | 8        | 8          | 15        | 46.67%
...

```

## 2.4 Funcionamento Interno

O script calcula potências de 2 para os valores `A`, `PROCURANDO` (máximo de strings geráveis), e o limite máximo de strings possíveis para `A+1` bits. Em seguida, calcula a porcentagem de strings incompressíveis.

## 2.5 Tecnologias e Requisitos

* Python 3.x  
* Biblioteca padrão (sem dependências externas)

---

# 3 Extras

## 3.1 Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

## 3.2 Referências

* [Kolmogorov Complexity - Wikipedia](https://en.wikipedia.org/wiki/Kolmogorov_complexity)  
* CanalQb Blog: [https://canalqb.blogspot.com](https://canalqb.blogspot.com)

## 3.3 Testes e Validações

Testado em Python 3.7+ para garantir consistência nos cálculos e na geração da tabela.

---

## 4 📬 Contato

* Feito por CanalQb no GitHub  
* Visite o blog: [canalqb.blogspot.com](https://canalqb.blogspot.com)  
* 💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*

---

# 5. Nota

Este README foi elaborado para facilitar o entendimento da complexidade de Kolmogorov e auxiliar na execução e estudo do script de simulação. 
