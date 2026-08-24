# 🧩 - De Simson
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Simson-ff69b4.svg)](https://en.wikipedia.org/wiki/Simson_line)

## Frase do Teorema

> **Se um ponto estiver no círculo que passa pelos três vértices de um triângulo, então as projeções desse ponto sobre os lados do triângulo estarão alinhadas.** – Ou seja, dá para traçar uma única reta passando por esses três pontos.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `simson.py`](#2-script-simsonpy)  
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

O **Teorema de Simson** mostra uma relação entre um ponto e um triângulo inscrito em um círculo. Ele afirma que, se o ponto estiver no círculo que passa pelos vértices do triângulo, então as projeções dele sobre os lados do triângulo (as "sombras" dele nos lados) vão sempre formar uma linha reta.

### 1.2 Exemplos Práticos

- Você pode usar esse teorema para verificar alinhamento de pontos no plano.
- É útil em geometria analítica, construções com régua e compasso, e até em animações gráficas.

### 1.3 Explicação Detalhada

Imagine um triângulo feito de palitos. Agora, pense em um ponto caminhando pelo círculo que passa pelos três vértices desse triângulo. Se você jogar uma luz nesse ponto de cima, as "sombras" dele nos lados do triângulo sempre cairão alinhadas numa única linha.

Isso só acontece **se o ponto estiver sobre o círculo**. Se ele sair do círculo, as projeções deixam de estar alinhadas.

### 1.4 Aplicações

- Geometria plana e analítica
- Programas de CAD (desenho técnico)
- Simulações com vetores e projeções
- Algoritmos gráficos

### 1.5 Análise da Tabela

O script mostra graficamente a formação da reta de Simson para diferentes tamanhos de triângulo, variando com a base `AB = 2^n` e o lado `BC = 2^n - 1` (conhecido como número de Mersenne).

---

## 2. Script `simson.py`

### 2.1 Relação com o Teorema

Esse script ilustra visualmente o **Teorema de Simson**. Ele permite verificar, para diferentes triângulos, que as projeções do ponto sobre os lados realmente estão alinhadas quando ele está no círculo.

### 2.2 Objetivo do Script

O objetivo é **demonstrar visualmente** o Teorema de Simson usando Python. Ele cria uma sequência de triângulos baseada em potências de 2 e números de Mersenne, e mostra a reta formada pelas projeções.

### 2.3 Exemplo de Saída

- Gráfico com o triângulo
- Circuncírculo em linha tracejada
- Projeções ortogonais em azul
- Reta de Simson em rosa tracejado

📷 *Cada gráfico mostra isso para um valor diferente de n (de 2 a 10).*

### 2.4 Funcionamento Interno

- Define o triângulo usando `AB = 2^n` e `BC = 2^n - 1`
- Calcula o terceiro ponto `C` de forma que o triângulo seja possível
- Determina o centro do círculo circunscrito
- Escolhe um ponto `P` no círculo
- Projeta `P` nos lados do triângulo
- Plota tudo com `matplotlib`

### 2.5 Tecnologias e Requisitos

- Python 3.8.10  
- Bibliotecas:
  - `numpy`
  - `matplotlib`

Para instalar:

```bash
pip install numpy matplotlib
````

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### 3.2 Referências

* Wikipedia: [Simson Line](https://en.wikipedia.org/wiki/Simson_line)
* Canal Qb Blog: [https://canalqb.blogspot.com](https://canalqb.blogspot.com)

### 3.3 Testes e Validações

Testado manualmente em:

* Python 3.8.10 no Windows
* Resolução gráfica padrão
* Scripts verificados até `n = 10`

---

## 4 Contato

* Feito por **CanalQb** no GitHub
* Visite o blog: canalqb.blogspot.com
  [https://canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Projeção ortogonal**:
É como uma "sombra" lançada perpendicularmente de um ponto até uma linha.

**Circuncírculo**:
É o círculo que passa pelos três vértices de um triângulo.

**Colineares**:
Três ou mais pontos estão colineares quando todos estão exatamente sobre a mesma linha reta.

**Número de Mersenne**:
É um número formado por `2^n - 1`, como 3, 7, 15, 31...

**Reta de Simson**:
É a linha reta formada pelas projeções de um ponto no círculo circunscrito sobre os lados do triângulo.

**Triângulo degenerado**:
Quando os três pontos do triângulo estão na mesma linha, ele "colapsa" e deixa de ser um triângulo real.

---

### ✅ O que fazer agora?

1. Salve o conteúdo acima em um arquivo chamado `README.md`.
2. Coloque-o na raiz do seu repositório GitHub.
3. Se quiser, posso gerar também o `LICENSE`, `.gitignore`, ou até o `requirements.txt`.
