# 🔢 - Teorema da Infinitude dos Primos

## 🧾 Frase do Teorema

> *"Há infinitos números primos"* – Não existe um conjunto finito que contenha todos os números primos; sempre é possível encontrar mais.

## 📚 Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `infinitude_primos_euclides.py`](#2-script-infinitude_primos_euclidespy)
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
* [5 Nota](#5-nota)

---

# 🔢 - Teorema da Infinitude dos Primos

Este repositório contém uma implementação em Python que ilustra, de forma prática, a **infinitude dos números primos**, conforme demonstrado pelo matemático **Euclides** por volta de 300 a.C.

Através de uma abordagem computacional simples, o script `infinitude_primos_euclides.py` simula o argumento clássico:  
> *"Seja uma lista de primos conhecidos. Multiplicando todos eles e somando 1 ao produto, o número resultante ou é primo, ou possui fatores primos que não estavam na lista inicial."*

## 1. Introdução ao Teorema

### 1.1 Resumo

O teorema afirma que não existe um número finito de primos. Ou seja, o conjunto dos números primos é *infinito*. Essa ideia foi provada pela primeira vez por Euclides usando uma técnica elegante e simples.

### 1.2 Exemplos Práticos

O script realiza múltiplas etapas para mostrar intervalos de números e os primos dentro deles, provando que sempre há mais primos para descobrir.

### 1.3 Explicação Detalhada

Ao multiplicar todos os primos conhecidos e adicionar 1, obtemos um número que não é divisível por nenhum dos primos anteriores. Isso implica que ele próprio é primo ou tem fatores primos novos, provando a infinitude dos primos.

### 1.4 Aplicações

- Fundamentos da teoria dos números
- Criptografia baseada em números primos
- Algoritmos de geração de primos para segurança computacional

### 1.5 Análise da Tabela

A tabela gerada pelo script mostra os intervalos analisados, a quantidade de primos encontrados e o resultado da verificação do número "produto + 1".

## 2. Script `infinitude_primos_euclides.py`

### 2.1 Relação com o Teorema

Implementa a ideia de Euclides com um método computacional, gerando primos em intervalos crescentes e verificando a propriedade do produto + 1.

### 2.2 Objetivo do Script

Demonstrar, com código, a infinitude dos números primos, por meio da construção progressiva de conjuntos primos e checagem da propriedade de Euclides.

### 2.3 Exemplo de Saída

```bash
* ID | Intervalo     | Qtd. de Primos | Produto + 1 (Euclides)
* 0  | [1, 1]       | 0              | -
* 1  | [2, 3]       | 2              | 7 (Primo)
* 2  | [4, 7]       | 1              | 43 (Primo)
* 3  | [8, 15]      | 2              | 1807 (Primo)
* 4  | [16, 31]     | 5              | 3263443 (Primo)
````

> *Nota: valores podem variar dependendo dos intervalos analisados.*

### 2.4 Funcionamento Interno

O script realiza:

1. Geração de primos com o Crivo de Eratóstenes em intervalos do tipo `[2^i, 2^{i+1}-1]`.
2. Atualização do conjunto de primos conhecidos.
3. Cálculo do produto dos primos e soma de 1.
4. Verificação da primalidade do número obtido.
5. Impressão dos resultados em formato tabular.

### 2.5 Tecnologias e Requisitos

* **Python 3.6+**
* Biblioteca padrão (`math`)

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a **MIT License**.

### 3.2 Referências

* Euclides, *Elementos*, ca. 300 a.C.
* Crivo de Eratóstenes — método clássico para geração de números primos.

### 3.3 Testes e Validações

Testes manuais realizados para garantir que a geração de primos e a verificação da propriedade de Euclides estejam corretas.

## 4 📬 Contato

* Feito por **CanalQb** no GitHub
* Visite o blog: [canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

## 5 Nota

Este projeto visa principalmente fins didáticos e de aprendizagem sobre números primos e sua infinitude comprovada por Euclides.
 
