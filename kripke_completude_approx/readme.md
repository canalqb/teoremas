# 🔐 - Teorema da Completude da Lógica Modal (Kripke)  
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![LGN](https://img.shields.io/badge/Teorema-Completude%20da%20Lógica%20Modal-ff69b4.svg)](https://en.wikipedia.org/wiki/Modal_logic#Completeness)  

## Frase do Teorema

> Toda fórmula que é verdadeira em todos os modelos possíveis de Kripke pode ser provada dentro da lógica modal, e vice-versa.  
> – Isso significa que tudo que é *verdade* dentro da semântica (mundo dos modelos) pode ser demonstrado usando as regras da lógica modal.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `kripke_completude_approx.py`](#2-script-kripke_completude_approxpy)  
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

# 1. Introdução ao Teorema

## 1.1 Resumo

O **Teorema da Completude da Lógica Modal**, demonstrado por Kripke, garante que a lógica modal é **completa**: tudo que é *verdade* em todos os modelos possíveis pode ser provado dentro da lógica. Isto cria uma ponte entre a **semântica** (como interpretamos os mundos possíveis) e a **sintaxe** (as regras que usamos para provar as fórmulas).

## 1.2 Exemplos Práticos

Imagine que você tenha diferentes "mundos" ou situações possíveis, e quer saber se uma certa afirmação é verdadeira em todos eles. A lógica modal ajuda a formalizar isso. O teorema diz que, se essa afirmação for verdadeira em todos esses mundos, existe uma maneira de provar isso formalmente.

## 1.3 Explicação Detalhada

Um modelo de Kripke é formado por:

- Um conjunto de **mundos possíveis** (W), que representam situações diferentes.
- Uma **relação de acessibilidade** (R) que diz quais mundos podem "ver" outros mundos.
- Uma função que indica se uma proposição é verdadeira em um determinado mundo.

A completude indica que, se uma fórmula é verdadeira em todos os mundos de todos os modelos possíveis com essa estrutura, então existe uma prova formal para ela dentro da lógica modal.

## 1.4 Aplicações

- **Verificação formal** em ciência da computação: garantir que sistemas funcionem em todos os estados possíveis.  
- **Inteligência Artificial**: raciocínio sobre crenças, desejos e intenções.  
- **Filosofia**: estudo de possibilidade e necessidade.  

## 1.5 Análise da Tabela

O script cria uma tabela que mostra como o número de possíveis mundos e seus relacionamentos cresce exponencialmente com o aumento da profundidade `N`. Isso ajuda a visualizar a complexidade crescente dos modelos de Kripke.

---

# 2. Script `kripke_completude_approx.py`

## 2.1 Relação com o Teorema

O script explora numericamente a ideia do teorema, simulando o crescimento do número de estados ou fórmulas válidas conforme aumentamos o número de níveis da lógica modal.

## 2.2 Objetivo do Script

Calcular e aproximar o crescimento da complexidade de modelos acessíveis de Kripke para diferentes profundidades `N`, usando intervalos baseados em potências de 2.

## 2.3 Exemplo de Saída

```

## N | Inicio (2^N) | Fim (2^(N+1))-1 | Aproximação

0 |            1 |               1 |            1
1 |            2 |               3 |            4
2 |            4 |               7 |            8
3 |            8 |              15 |           16
...

```

## 2.4 Funcionamento Interno

- Para cada nível `N`, define um intervalo de mundos possíveis de tamanho `2^N`.
- Calcula um valor heurístico que tenta refletir o crescimento do número de estados ou fórmulas possíveis dentro desse intervalo.
- Imprime esses valores para mostrar o padrão de crescimento.

## 2.5 Tecnologias e Requisitos

- **Python 3.8.10**  
- Bibliotecas usadas: nenhuma externa específica, apenas bibliotecas padrão do Python.

---

# 3 Extras

## 3.1 Licença

Este projeto está sob licença MIT. Sinta-se livre para usar, modificar e distribuir.

## 3.2 Referências

- Kripke, S.A. (1963). *Semantical Considerations on Modal Logic*. Acta Philosophica Fennica.  
- Blackburn, P., de Rijke, M., Venema, Y. (2001). *Modal Logic*. Cambridge University Press.  
- https://en.wikipedia.org/wiki/Modal_logic#Completeness

## 3.3 Testes e Validações

Os valores produzidos pelo script são aproximações heurísticas e não provas formais, mas ilustram bem o crescimento da estrutura dos modelos.

---

# 4 Contato

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*

---

# 5. Nota

**Mundos possíveis:** diferentes cenários ou situações que podem ocorrer, considerados na lógica modal.

**Relação de acessibilidade:** uma conexão que indica se um mundo "pode acessar" ou "ver" outro mundo, essencial para entender como a verdade de proposições se propaga.

**Valor esperado:** aqui, uma aproximação numérica que tenta medir a complexidade ou o "peso" do crescimento dos estados acessíveis.

**Completude:** garantia de que tudo que é verdadeiro na semântica pode ser demonstrado pela lógica.

**Profundidade (N):** quantidade de níveis que a lógica modal considera, influenciando o tamanho do modelo de Kripke.
