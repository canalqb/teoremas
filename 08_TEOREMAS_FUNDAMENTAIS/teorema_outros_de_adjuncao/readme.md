# 🧩 - De Adjuncao
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![LGN](https://img.shields.io/badge/Teorema-Adjunção-ff69b4.svg)](https://en.wikipedia.org/wiki/Adjunction)

## Frase do Teorema

> *O crescimento de uma estrutura pode ser descrito pela adição organizada de partes menores.* – Em outras palavras, podemos construir coisas maiores juntando componentes anteriores, seguindo regras claras.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `estimativa_adjunção.py`](#2-script-estimativa_adjunçãopy)  
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
O **Teorema da Adjunção** aparece em áreas como lógica, álgebra e topologia. Ele explica como estruturas complexas podem ser formadas pela **adição ordenada** de partes menores, respeitando regras de ligação ou junção.

### 1.2 Exemplos Práticos  
- Montar uma figura geométrica a partir de partes básicas  
- Construir uma árvore de decisões com base em nós anteriores  
- Criar um programa por meio da composição de funções menores  

### 1.3 Explicação Detalhada  
A ideia central é **crescer algo passo a passo**, onde cada novo passo depende dos anteriores. O crescimento pode ser linear, exponencial ou seguir padrões definidos por **regras recursivas**.

### 1.4 Aplicações  
- Combinatória e estruturas recursivas  
- Construção de linguagens formais  
- Modelagem de crescimento de redes e sistemas dinâmicos  
- Topologia algébrica e teoria das categorias  

### 1.5 Análise da Tabela  
A tabela gerada pelo script mostra como os valores **crescem ao longo dos níveis N**, e como se aproximam dos limites definidos por `2^N` (mínimo) e `2^(N+1)-1` (máximo).

---

## 2. Script `estimativa_adjunção.py`

### 2.1 Relação com o Teorema  
O script utiliza uma **regra recursiva simples** (baseada na soma de valores anteriores) para simular o crescimento de uma estrutura, **imitando o comportamento descrito no Teorema da Adjunção**.

### 2.2 Objetivo do Script  
- Simular o crescimento de uma sequência a partir de valores iniciais  
- Observar como esse crescimento se comporta comparado aos limites matemáticos inferiores (`2^N`) e superiores (`2^(N+1)-1`)  

### 2.3 Exemplo de Saída

```text
| N | Início | Fim  | Estimativa |
|---|--------|------|-------------|
| 0 | 1      | 1    | 1           |
| 1 | 2      | 3    | 2           |
| 2 | 4      | 7    | 3           |
| 3 | 8      | 15   | 5           |
| 4 | 16     | 31   | 8           |
| 5 | 32     | 63   | 13          |
| 6 | 64     | 127  | 21          |
| 7 | 128    | 255  | 34          |
| 8 | 256    | 511  | 55          |
| 9 | 512    | 1023 | 89          |
````

### 2.4 Funcionamento Interno

* Começa com valores base: 1 e 2
* A partir do terceiro termo, aplica:
  `valor_atual = anterior + anterior_anterior`
* Essa regra simula um crescimento baseado na **adição de estruturas menores anteriores**

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10**
* Nenhuma biblioteca externa
* Código puro, pronto para execução com:

```bash
python estimativa_adjunção.py
```

---

## 3 Extras

### 3.1 Licença

Distribuído sob a licença **MIT**. Sinta-se livre para usar, modificar e distribuir.

### 3.2 Referências

* Discussões sobre adjunção em teoria das categorias
* Wikipedia e literatura de lógica matemática
* Apostilas sobre crescimento recursivo em estruturas combinatórias

### 3.3 Testes e Validações

A sequência foi testada de `N = 0` a `N = 9` e os resultados seguem um padrão estável de crescimento, útil para análise didática.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Adjunção:** Nome dado à ideia de construir algo maior unindo partes anteriores, de forma organizada.
**Estimativa:** Aproximação de um valor com base em uma fórmula ou padrão.
**Estrutura Recursiva:** Quando uma coisa depende de si mesma ou de versões anteriores de si.
**Início e Fim:** Referem-se aos limites inferior (`2^N`) e superior (`2^(N+1) - 1`) para cada nível N.
**Convergência:** Quando os valores da estimativa se aproximam dos limites esperados.
**Heurística:** Regra prática para estimar ou simular algo complexo de forma simplificada.
