# 🧩 - De Konig
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-König-ff69b4.svg)](https://en.wikipedia.org/wiki/K%C3%B6nig%27s_theorem_(graph_theory))

## Frase do Teorema

> O tamanho máximo de um emparelhamento em um grafo bipartido é igual ao tamanho mínimo de um conjunto de vértices que toca todas as arestas – isso quer dizer que o máximo número de pares sem sobreposição é igual ao menor conjunto de pontos que "cobre" todas as conexões.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Aplicações](#12-aplicações)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Contexto de Árvores Binárias](#14-contexto-de-árvores-binárias)
* [2. Script `konig_sum_approx.py`](#2-script-konig_sum_approxpy)

  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3. Extras](#3-extras)

  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referências)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4 Contato](#4-contato)
* [5. Nota](#5-nota)

---

# 1. Introdução ao Teorema

## 1.1 Resumo

O **Teorema de König** é um resultado importante na área de **teoria dos grafos**. Ele nos mostra que o maior conjunto de pares (emparelhamento) sem sobreposição em um grafo bipartido tem o mesmo tamanho que o menor conjunto de vértices que cobre todas as arestas (conjunto de cobertura).

Esse resultado conecta duas ideias opostas: a máxima quantidade de "ligações" possíveis sem conflito, e o mínimo de pontos necessários para "controlar" essas ligações.

---

## 1.2 Aplicações

- **Algoritmos para emparelhamento máximo**: usados em problemas de alocação e casamento estável.
- **Análise de árvores binárias**: para entender a quantidade de elementos e somas de níveis.
- **Teoria da Computação**: análise de complexidade em estruturas hierárquicas.
- **Engenharia de Software**: otimização de estruturas e memória.
- **Matemática Discreta**: estudo de estruturas combinatórias e somas geométricas.

---

## 1.3 Explicação Detalhada

Imagine uma rede onde queremos conectar pares sem que nenhuma conexão se sobreponha. O Teorema de König diz que a maior quantidade possível dessas conexões (emparelhamento máximo) é igual ao menor conjunto de pontos que precisa ser escolhido para "tocar" todas as conexões (conjunto de cobertura).

No mundo das árvores binárias, a soma dos nós até o nível N é uma soma de potências de 2: começa com 1, depois 2, 4, 8 e assim por diante. A soma total até o nível N é:

* A soma de todos os números de 2 elevado à potência k, onde k vai de 0 até N.
* O resultado dessa soma é sempre 2 elevado à potência (N+1), menos 1.

---

## 1.4 Contexto de Árvores Binárias

Árvores binárias são estruturas onde cada nó pode ter até dois "filhos". O número de nós por nível cresce exponencialmente como 2 elevado a N (onde N é o nível).

Somando todos os nós até o nível N, temos um número entre:

- O menor valor, que é exatamente 2 elevado a N.
- O maior valor, que é 2 elevado a (N+1) menos 1.

Esse intervalo é fundamental para o script que criamos, que aproxima valores dentro desses limites.

---

# 2. Script `konig_sum_approx.py`

## 2.1 Relação com o Teorema

O script utiliza a ideia da soma geométrica de potências de 2 para representar a quantidade acumulada de elementos numa árvore binária até o nível N, respeitando os limites estabelecidos pelo Teorema de König e a natureza das estruturas binárias.

## 2.2 Objetivo do Script

- Calcular o valor mínimo (2 elevado a N) e máximo (2 elevado a N+1 menos 1) de nós acumulados.
- Estimar um valor aproximado intermediário que cresce com N.
- Facilitar o entendimento e uso prático desses valores em análises computacionais e matemáticas.

## 2.3 Exemplo de Saída

| N  | Início (2^N) | Estimado (Aproximado) | Fim (2^(N+1) - 1) |
|-----|--------------|-----------------------|------------------|
| 0   | 1            | 1                     | 1                |
| 1   | 2            | 2                     | 3                |
| 2   | 4            | 4                     | 7                |
| 3   | 8            | 10                    | 15               |
| 4   | 16           | 20                    | 31               |
| 5   | 32           | 40                    | 63               |
| 6   | 64           | 80                    | 127              |
| 7   | 128          | 160                   | 255              |
| 8   | 256          | 320                   | 511              |
| 9   | 512          | 640                   | 1023             |

## 2.4 Funcionamento Interno

O script:

- Recebe um valor N.
- Calcula os limites inferior (2^N) e superior (2^(N+1) - 1).
- Aplica uma função para aproximar um valor intermediário que cresce exponencialmente, mas não ultrapassa o limite superior.
- Exibe esses valores numa tabela fácil de entender.

## 2.5 Tecnologias e Requisitos

- Desenvolvido em **Python 3.8.10**.
- Dependências: nenhuma além da biblioteca padrão.
- Fácil execução em qualquer ambiente com Python instalado.

---

# 3. Extras

## 3.1 Licença

Este projeto está licenciado sob a licença MIT — veja o arquivo LICENSE para detalhes.

## 3.2 Referências

- [Teorema de König - Wikipedia](https://en.wikipedia.org/wiki/K%C3%B6nig%27s_theorem_(graph_theory))
- Apostilas e livros sobre teoria dos grafos e combinatória.
- Documentação oficial do Python.

## 3.3 Testes e Validações

Testes simples foram realizados para garantir que os valores calculados seguem os limites esperados para diferentes valores de N.

---

# 4 Contato

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*

---

# 5. Nota

- **Nível (N)**: representa a profundidade ou etapa na árvore binária.  
- **2^N**: potência de 2, ou seja, 2 multiplicado por ele mesmo N vezes.  
- **Soma geométrica**: soma de uma sequência onde cada termo é obtido multiplicando o anterior por uma constante (neste caso, 2).  
- **Emparelhamento**: seleção de pares em um grafo sem que eles se sobreponham.  
- **Conjunto de cobertura**: um grupo mínimo de pontos que "tocam" todas as conexões em um grafo.  
- **Bipartido**: grafo cujos vértices podem ser divididos em dois grupos, onde as arestas só conectam vértices de grupos diferentes.

Se algum termo parecer confuso, pergunte para receber explicações mais simples!
