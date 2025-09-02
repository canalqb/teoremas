# kripke_completude_approx

## 📘 Sobre

Este projeto explora uma aplicação numérica do **Teorema da Completude da Lógica Modal**, com base na semântica de Kripke. A proposta central é estimar o crescimento da complexidade de modelos acessíveis conforme o número `N` de níveis ou profundidade aumenta, utilizando intervalos definidos por potências de 2.

A partir da estrutura de modelos de Kripke, o script tenta reproduzir ou aproximar uma métrica chamada de "valor esperado pelo teorema", que se acredita representar um comportamento acumulativo ou transitivo da acessibilidade entre mundos possíveis em lógica modal.

---

## 📚 Teorema da Completude da Lógica Modal (Kripke)

Na lógica modal, o **Teorema da Completude de Kripke** estabelece que toda fórmula que é semanticamente válida (ou seja, verdadeira em todos os modelos de Kripke) é também sintaticamente demonstrável dentro do sistema axiomático da lógica modal. E vice-versa.

> Em termos simples: tudo o que é logicamente verdadeiro em todos os mundos possíveis (na estrutura de Kripke) pode ser provado dentro da lógica modal, e tudo o que pode ser provado é válido nesses modelos.

### Modelos de Kripke

Um modelo de Kripke é composto por:

- Um conjunto de mundos possíveis `W`
- Uma relação de acessibilidade `R` ⊆ W × W
- Uma função de avaliação que define quais proposições são verdadeiras em quais mundos

A partir disso, uma fórmula é considerada **válida** se for verdadeira em todos os mundos de todos os modelos possíveis sob essa semântica.

---

## 🧮 Objetivo do Script

O script **kripke_completude_approx.py** tenta aproximar, por meios numéricos, o comportamento do crescimento do número de estados possíveis ou fórmulas válidas num universo de modelos de Kripke, com base em potências de dois. A motivação vem da observação empírica de que:

- Para cada `N`, o intervalo de mundos possíveis é de `2^N` até `2^(N+1) - 1`
- O número de possíveis variações dentro do intervalo é sempre `2^N`
- A acessibilidade entre mundos pode gerar uma explosão combinatória de estados

A coluna de **"valor esperado pelo teorema"** (informalmente dada) parece refletir esse crescimento, mas de forma acumulativa ou com base em regras não-lineares.

---

## 🔍 Justificativa

A lógica modal com semântica de Kripke é fortemente baseada em estruturas transitivas, reflexivas ou simétricas de mundos possíveis. Ao aumentar `N`, essas estruturas crescem exponencialmente. O script simula esse crescimento com:

- A base de crescimento: potências de dois
- Um modelo aproximado de transições ou expansões possíveis entre mundos acessíveis
- A tentativa de simular o acúmulo de complexidade em fórmulas válidas para N níveis

Esse comportamento é coerente com a forma como a lógica modal se comporta: mais mundos implicam mais caminhos acessíveis, mais fórmulas válidas e mais estruturas a considerar. Isso justifica o uso do teorema como base conceitual para o crescimento da função aproximada.

---

## ⚙️ Como funciona

O script imprime uma tabela com as seguintes colunas:

- `N`: profundidade do modelo
- `Início`: 2^N (ponto inicial do intervalo)
- `Fim`: 2^(N+1) - 1 (ponto final)
- `Aproximação`: um valor heurístico calculado para simular o comportamento esperado

Exemplo de saída:

```

## N | Inicio (2^N) | Fim (2^(N+1))-1 | Aproximação

0 |            1 |               1 |            1
1 |            2 |               3 |            4
2 |            4 |               7 |            8
3 |            8 |              15 |           16
...

```

---

## 💡 Considerações

Este projeto **não é uma prova formal** do teorema, mas sim uma exploração computacional dos padrões numéricos que emergem a partir das propriedades dos modelos de Kripke e da lógica modal.

É uma ferramenta didática para visualizar o crescimento das estruturas acessíveis conforme a profundidade lógica aumenta — algo difícil de visualizar apenas com definições formais.

---

## 🧠 Futuras melhorias

- Refinar o modelo de aproximação baseado em transições reais entre mundos
- Implementar diferentes tipos de relações (reflexiva, simétrica, etc.)
- Simular diretamente a geração de mundos e relações com grafos

--- 

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
