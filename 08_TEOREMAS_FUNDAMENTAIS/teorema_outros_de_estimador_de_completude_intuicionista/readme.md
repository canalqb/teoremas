# 🧩 - De Estimador De Completude Intuicionista

## 🧾 Frase do Teorema

> A lógica proposicional intuicionista é completa em relação a modelos de Kripke – ou seja, toda fórmula válida na lógica intuicionista pode ser provada considerando a estrutura especial desses modelos.

## 📚 Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `estimador_completude_kripke.py`](#2-script-estimador_completude_kripkepy)

  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3 Extras](#3-extras)

  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referências)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4 📬 Contato](#4-📬-contato)
* [5. Nota](#5-nota)

---

# 1. Introdução ao Teorema

## 1.1 Resumo

O **Teorema da Completude Intuicionista**, proposto por *Saul Kripke*, afirma que a lógica proposicional intuicionista é *completa* em relação a uma classe especial de estruturas chamadas **modelos de Kripke**. Isso significa que toda fórmula válida na lógica intuicionista pode ser verificada através desses modelos.

## 1.2 Exemplos Práticos

Diferente da lógica clássica, na lógica intuicionista a verdade de uma fórmula pode variar conforme o "mundo" (estado) considerado, respeitando uma relação de acessibilidade entre esses mundos.

Exemplo:

* Se uma fórmula é verdadeira em um mundo, ela permanece verdadeira em todos os mundos acessíveis a partir dele (persistência da verdade).
* A fórmula *A ou não A* (A ∨ ¬A), típica da lógica clássica, nem sempre é válida intuicionisticamente.

## 1.3 Explicação Detalhada

* **Persistência da verdade**: Verdades são monotônicas ao longo da cadeia de mundos.
* **Modelos dinâmicos**: Os modelos de Kripke representam mundos possíveis que se relacionam via uma ordem parcial, refletindo o crescimento do conhecimento.
* **Rejeição do terceiro excluído**: A ausência do princípio do terceiro excluído distingue a lógica intuicionista da clássica.
* **Explosão combinatória**: O número de fórmulas válidas e de mundos possíveis cresce de forma não linear, muito maior que na lógica clássica.

## 1.4 Aplicações

O teorema é usado para fundamentar sistemas de prova e semântica na lógica intuicionista, que tem aplicações em:

* Teoria da computação e programação funcional.
* Verificação formal.
* Filosofia da matemática e construtivismo.

## 1.5 Análise da Tabela

O script do projeto gera uma tabela que mostra:

| N | Início (2^N) | Estimado (Kripke) | Fim (2^(N+1)-1) |
| - | ------------ | ----------------- | --------------- |
| 0 | 1            | 1                 | 1               |
| 1 | 2            | 3                 | 3               |
| 2 | 4            | 7                 | 7               |
| 3 | 8            | 12                | 15              |
| 4 | 16           | 26                | 31              |
| 5 | 32           | 52                | 63              |
| 6 | 64           | 90                | 127             |
| 7 | 128          | 162               | 255             |
| 8 | 256          | 318               | 511             |
| 9 | 512          | 582               | 1023            |

* **Início (2^N):** número clássico de estados binários possíveis com N variáveis.
* **Estimado (Kripke):** aproximação do crescimento intuicionista via modelos de Kripke.
* **Fim (2^(N+1)-1):** limite superior clássico.

---

# 2. Script `estimador_completude_kripke.py`

## 2.1 Relação com o Teorema

O script implementa uma fórmula aproximada para estimar o crescimento do número de mundos ou fórmulas válidas segundo a lógica intuicionista baseada no Teorema da Completude de Kripke.

## 2.2 Objetivo do Script

* Calcular valores crescentes baseados em 2^N (lógica clássica).
* Estimar a quantidade intuicionista de mundos possíveis e fórmulas válidas.
* Justificar matematicamente a explosão combinatória intuicionista inspirada nos modelos de Kripke.

## 2.3 Exemplo de Saída

```
N   | Início (2^N) | Estimado (Kripke) | Fim (2^(N+1)-1)
0   | 1            | 1                 | 1
1   | 2            | 3                 | 3
2   | 4            | 7                 | 7
3   | 8            | 12                | 15
4   | 16           | 26                | 31
5   | 32           | 52                | 63
6   | 64           | 90                | 127
7   | 128          | 162               | 255
8   | 256          | 318               | 511
9   | 512          | 582               | 1023
```

## 2.4 Funcionamento Interno

A estimativa é feita com a fórmula:

```
estimado = sum(2^i for i in range(N + 1)) + (N * (N - 1))
```

* A soma de potências de 2 representa o crescimento clássico.
* O termo quadrático (N \* (N - 1)) aproxima o crescimento não linear intuicionista dos modelos de Kripke.

## 2.5 Tecnologias e Requisitos

* Linguagem: Python 3+
* Sem dependências externas
* Executar via terminal: `python estimador_completude_kripke.py`

---

# 3 Extras

## 3.1 Licença

Este projeto está disponível sob a licença MIT, permitindo uso, modificação e distribuição livre.

## 3.2 Referências

* Kripke, Saul A. “Semantical Analysis of Intuitionistic Logic.” In Formal Systems and Recursive Functions, 1965.
* Troelstra, A. S., & van Dalen, D. *Constructivism in Mathematics: An Introduction*, 1988.

## 3.3 Testes e Validações

Este projeto oferece uma aproximação interpretativa, sem provas formais exatas. Pode servir como base para estudos mais avançados.

---

# 4 📬 Contato

* Feito por **CanalQb** no GitHub
* Visite o blog: [canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

# 5. Nota

* **N**: número de variáveis ou profundidade dos modelos.
* **2^N**: total de estados binários possíveis com N variáveis.
* **S\_k**: (não usado diretamente aqui, mas comum em análise de somas e sequências).
* **E**: valor esperado ou esperança matemática (conceito geral).
* **Estimado (Kripke)**: valor aproximado do número de mundos/fórmulas na lógica intuicionista segundo modelos de Kripke.
* O termo *(N \* (N - 1))* captura a complexidade extra da estrutura dos modelos intuicionistas.
