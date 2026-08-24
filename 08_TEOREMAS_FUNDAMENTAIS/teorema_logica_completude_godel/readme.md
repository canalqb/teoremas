# 🧩 - Completude Godel

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)

## Frase do Teorema

> **Teorema da Completude de Gödel** – *Afirma que, em um sistema formal suficientemente forte, todas as proposições verdadeiras dentro desse sistema podem ser provadas dentro do próprio sistema.*

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `teorema_completude_godel.py`](#2-script-teorema_completude_godelpy)

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

## 1 Introdução ao Teorema

### 1.1 Resumo

O **Teorema da Completude de Gödel** garante que, em um sistema formal suficientemente poderoso (como a aritmética de Peano), todas as proposições verdadeiras dentro desse sistema podem ser provadas por ele mesmo. Ou seja, não existem "verdades ocultas" dentro desse sistema que não possam ser demonstradas formalmente.

### 1.2 Exemplos Práticos

Em termos simples, se você tem um sistema lógico que descreve números e suas propriedades, o teorema afirma que, se algo for verdadeiro dentro desse sistema, então você pode provar que isso é verdade usando as regras do sistema.

### 1.3 Explicação Detalhada

O Teorema de Completude de Gödel foi um grande avanço na lógica matemática. Ele estabelece uma conexão entre a verdade das proposições e a capacidade de prová-las dentro do próprio sistema. Ao contrário dos Teoremas da Incompletude, que dizem que existem proposições verdadeiras que não podem ser provadas, o teorema da completude diz que tudo o que é verdadeiro dentro do sistema pode ser demonstrado.

### 1.4 Aplicações

Este teorema é fundamental para a compreensão da lógica matemática e da teoria dos sistemas formais. Ele mostra que, para sistemas lógicos fortes, não há "fórmulas verdadeiras" que são inalcançáveis — elas podem ser provadas dentro do sistema.

### 1.5 Análise da Tabela

A tabela gerada a seguir contém valores aleatórios que são calculados dentro de intervalos definidos pelo teorema. Cada valor na coluna "Esperado pelo Teorema" está dentro do intervalo definido por **2^N** (Início) e **2^(N+1)-1** (Fim). O script utiliza esse intervalo para gerar um valor aleatório dentro dele para cada valor de N.

## 2 Script `teorema_completude_godel.py`

### 2.1 Relação com o Teorema

O script **teorema\_completude\_godel.py** gera uma tabela onde o valor "Esperado pelo Teorema" é calculado como um número aleatório dentro do intervalo definido por **2^N** e **2^(N+1)-1**. Isso está diretamente relacionado ao Teorema da Completude de Gödel, pois, para qualquer N, estamos tratando de um valor que pode ser provado dentro do sistema.

### 2.2 Objetivo do Script

O objetivo deste script é gerar valores aleatórios dentro de um intervalo específico para cada valor de N de 0 a 9. Esses valores são comparáveis aos "valores esperados" pelo Teorema, gerando uma tabela que ilustra esses resultados.

### 2.3 Exemplo de Saída

A saída do script gera uma tabela como a seguinte:

```
Tabela de Valores Gerados:
N  Início (2^N)      Esperado pelo Teorema        Fim (2^(N+1)) - 1
0  1                 1                             1               
1  2                 2                             3               
2  4                 4                             7               
3  8                 8                             15              
4  16                26                            31              
5  32                59                            63              
6  64                90                            127             
7  128               247                           255             
8  256               312                           511             
9  512               602                           1023            
```

### 2.4 Funcionamento Interno

* **Função `gerar_valor_aleatorio(n)`**: Gera um valor aleatório entre **2^N** e **2^(N+1)-1**.
* **Função `gerar_tabela()`**: Gera a tabela completa para N de 0 a 9, com os valores de Início, Esperado e Fim.
* **Função `imprimir_tabela()`**: Exibe a tabela no formato organizado no console.

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10** ou versão superior.
* **Bibliotecas**: O script usa a biblioteca padrão do Python para a geração de números aleatórios e impressão de tabelas.

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a **Licença MIT**. Consulte o arquivo LICENSE para mais detalhes.

### 3.2 Referências

* **Teorema da Completude de Gödel**: [Wikipedia](https://pt.wikipedia.org/wiki/Teorema_da_completude_de_G%C3%B6del)
* **Teorema da Incompletude de Gödel**: [Wikipedia](https://pt.wikipedia.org/wiki/Teorema_da_incompletude_de_G%C3%B6del)

### 3.3 Testes e Validações

O script foi testado em ambientes Python 3.8.10 e superior, e a geração de números aleatórios foi validada para garantir que os valores estão dentro dos intervalos corretos.

## 4 Contato

* Feito por **CanalQb** no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

## 5 Nota

**Nota**:

* **Teorema**: Um teorema é uma afirmação matemática que foi rigorosamente provada com base em definições e axiomas aceitos.
* **Aritmética de Peano**: Um sistema formal que descreve as propriedades dos números naturais, como a adição e multiplicação.
* **Sistema Formal**: Um conjunto de regras e símbolos usados para construir provas matemáticas. 
