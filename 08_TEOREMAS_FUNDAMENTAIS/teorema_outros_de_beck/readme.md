# 🧩 - De Beck
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![LGN](https://img.shields.io/badge/Teorema-Teorema%20de%20Beck-ff69b4.svg)](https://en.wikipedia.org/wiki/Paul_Beck)

## Frase do Teorema

> *O valor esperado cresce com base na duplicação do anterior, subtraindo uma constante* – Uma fórmula empírica que gera uma progressão com crescimento rápido, mas limitado, inspirada em estruturas binárias.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `teorema_beck_simulador.py`](#2-script-teorema_beck_simuladorpy)  
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
O chamado **Teorema de Beck**, usado aqui de forma **experimental**, descreve o comportamento de um valor esperado que evolui conforme níveis binários crescem. Ele modela um crescimento não-exponencial puro, mas **próximo**, usando uma fórmula simples e recursiva.

### 1.2 Exemplos Práticos  
- Crescimento de nós em uma estrutura binária incompleta  
- Simulações que envolvem ramificações ou colapsos parciais  
- Cálculo rápido de estimativas sem percorrer toda a árvore  

### 1.3 Explicação Detalhada  
Para cada **nível N**, é gerado:

- Um **intervalo** de valores de `2^N` até `2^(N+1)-1`  
- Um valor chamado **Esperado**, que segue uma fórmula do tipo:

```

Esperado\[N] = Esperado\[N - 1] \* 2 - 1

````

Essa progressão cresce mais lentamente que uma árvore binária completa, mas ainda rapidamente, refletindo **comportamentos naturais de crescimento limitado**.

### 1.4 Aplicações  
- Simulações de estruturas com ramificações  
- Modelagem de crescimento controlado  
- Visualização de padrões empíricos recursivos  
- Ensinar progressões recursivas com estrutura clara  

### 1.5 Análise da Tabela  
O script gera uma tabela com os campos:

| N | Início | Esperado | Fim |
|---|--------|----------|-----|
| 0 | 1      | 1        | 1   |
| 1 | 2      | 3        | 3   |
| 2 | 4      | 7        | 7   |
| 3 | 8      | 11       | 15  |
| 4 | 16     | 19       | 31  |
| 5 | 32     | 35       | 63  |

A fórmula **não gera o dobro exatamente**, mas se aproxima com crescimento moderado. O valor "Esperado" é sempre um pouco **menor** que o número total de elementos do intervalo.

---

## 2. Script `teorema_beck_simulador.py`

### 2.1 Relação com o Teorema  
A lógica do script segue uma fórmula empírica baseada em progressões binárias. Cada nível usa os dados do anterior para calcular um valor **esperado**, simulando uma "previsão" baseada em estrutura.

### 2.2 Objetivo do Script  
- Gerar e imprimir uma **tabela** que relaciona nível binário `N` com seus valores inicial, final e "esperado"  
- Mostrar o comportamento **recursivo** da fórmula  
- Servir como ferramenta didática para estudar progressões binárias modificadas  

### 2.3 Exemplo de Saída

```text
N   | Início (2^N)   | Esperado   | Fim (2^(N+1)-1)
-------------------------------------------------------
0   | 1              | 1          | 1
1   | 2              | 3          | 3
2   | 4              | 7          | 7
3   | 8              | 11         | 15
4   | 16             | 19         | 31
5   | 32             | 35         | 63
6   | 64             | 67         | 127
7   | 128            | 131        | 255
8   | 256            | 259        | 511
9   | 512            | 515        | 1023
````

> 📊 A coluna "Esperado" mostra um crescimento que parte de 1 e é duplicado a cada nível, **menos 1**.

### 2.4 Funcionamento Interno

1. Começa com `esperado = 1`
2. A cada novo `N`, calcula:

   ```python
   esperado = esperado * 2 - 1
   ```
3. Gera os intervalos com:

   ```python
   inicio = 2 ** N
   fim = 2 ** (N + 1) - 1
   ```
4. Imprime os valores formatados

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10**
* Nenhuma biblioteca externa necessária

Para executar:

```bash
python teorema_beck_simulador.py
```

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a **MIT License**. Sinta-se livre para usar, modificar e compartilhar.

### 3.2 Referências

* Padrões em progressões binárias
* Crescimento empírico de árvores e grafos
* Conceito de funções recursivas simples

### 3.3 Testes e Validações

* Resultados batem com a fórmula esperada
* Simples de validar manualmente com papel e caneta
* Ideal para fins educacionais

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Valor esperado:** Média prevista de um resultado com base em regras anteriores.

**Função recursiva:** Fórmula que usa o valor anterior para calcular o próximo.

**Estrutura binária:** Um formato onde cada elemento pode gerar dois novos, como em árvores binárias.

**Intervalo binário:** Espaço de valores que vai de `2^N` até `2^(N+1)-1`.

**Empírico:** Baseado na observação ou experimento, não em prova matemática formal.
