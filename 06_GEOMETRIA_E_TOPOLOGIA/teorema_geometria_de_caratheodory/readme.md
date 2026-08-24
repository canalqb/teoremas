# 🧩 - De Caratheodory
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Carathéodory-ff69b4.svg)](https://en.wikipedia.org/wiki/Carath%C3%A9odory%27s_theorem_(convex_hull))

## Frase do Teorema

> *Se um ponto está dentro do envoltório convexo de um conjunto no espaço, ele pode ser escrito como uma combinação de no máximo (d+1) pontos desse conjunto, onde d é a dimensão do espaço.* – Em termos simples: **em um espaço tridimensional, qualquer ponto dentro de um conjunto de pontos pode ser explicado usando no máximo 4 deles.**

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `Caratheodory.py`](#2-script-caratheodorypy)
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

O **Teorema de Carathéodory** é uma ferramenta da matemática que trata da forma como pontos em um espaço podem ser combinados para representar outros pontos. Em espaços tridimensionais, por exemplo, isso significa que qualquer ponto dentro de uma forma (como um volume) pode ser explicado usando apenas **4 pontos do conjunto original**.

### 1.2 Exemplos Práticos

- Representar um ponto dentro de uma nuvem de dados 3D como uma mistura de apenas 4 pontos conhecidos.
- Comprimir dados tridimensionais mantendo a estrutura.
- Utilizado em aprendizado de máquina e otimização para reduzir complexidade.

### 1.3 Explicação Detalhada

Imagine que você tem vários pontos flutuando no espaço. Agora, escolha um ponto que esteja “dentro” do grupo. O teorema diz que, mesmo que você tenha mil pontos, você precisa de no máximo 4 deles para "explicar" esse ponto dentro.

É como dizer: “Você não precisa de todos para contar a história — só dos mais relevantes”.

### 1.4 Aplicações

- 💡 Visualização 3D de dados
- 📊 Compressão de representações
- 🧠 Inteligência artificial: otimização de modelos
- 🧮 Geometria computacional

### 1.5 Análise da Tabela

O script imprime uma tabela como esta:

```

## Tabela de pontos Mersenne (x, y, z):

## Index |     X |     Y |     Z

       0 |     1 |     2 |     3
       1 |     3 |     6 |     9
       2 |     7 |    14 |     1
       ...
   ## 10 |     7 |    14 |     1

Ponto convexo (média dos pontos): (7.55, 7.82, 6.27)

```

O ponto médio (convexo) representa uma *combinação de todos*, mas segundo o teorema, bastam 4 desses pontos para gerar esse mesmo resultado.

---

## 2. Script `Caratheodory.py`

### 2.1 Relação com o Teorema

O script mostra visualmente a afirmação do Teorema de Carathéodory. Ele gera um conjunto de pontos com base em números de **Mersenne**, calcula o ponto convexo e **mostra visualmente** como esse ponto se conecta aos demais no espaço.

### 2.2 Objetivo do Script

- 📌 Demonstrar como pontos formam um ponto médio convexo
- 🎞️ Gerar uma **animação 3D** com os pontos se conectando ao ponto convexo
- 💠 Visualização limpa e sem base, com rotação livre

### 2.3 Exemplo de Saída

- ✅ Tabela de pontos (exibida no console)
- ✅ Animação 3D salva como `caratheodory_3d.gif`

### 2.4 Funcionamento Interno

- Gera os pontos 3D com base na fórmula dos números de Mersenne.
- Calcula a média (ponto convexo).
- Anima a aparição sequencial dos pontos.
- Cria conexões entre o ponto convexo e os pontos originais.
- Remove todas as grades, eixos e rótulos para uma visualização limpa.

### 2.5 Tecnologias e Requisitos

- ✅ Python **3.8.10**
- ✅ matplotlib
- ✅ numpy
- ✅ pillow (para salvar o GIF)

Instale com:

```bash
pip install matplotlib numpy pillow
````

---

## 3 Extras

### 3.1 Licença

Distribuído sob licença **MIT**. Consulte `LICENSE` para mais informações.

### 3.2 Referências

* [Wikipedia: Teorema de Carathéodory](https://en.wikipedia.org/wiki/Carath%C3%A9odory%27s_theorem_%28convex_hull%29)
* [Geometria Convexa - Introdução](https://pt.wikipedia.org/wiki/Geometria_convexa)

### 3.3 Testes e Validações

* ✅ Testado com Python 3.8.10 no Windows
* ✅ Compatível com matplotlib 3.1+
* ✅ GIF gerado com sucesso

---

## 4 Contato

* Feito por **CanalQb** no GitHub
* Visite o blog: canalqb.blogspot.com → [https://canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)
  *Readme.md corrigido por ChatGPT*

---

## 5. Nota

**convexo**: um conjunto é convexo quando qualquer ponto entre dois pontos do conjunto também está dentro dele
**ponto convexo**: ponto que pode ser escrito como média ponderada de outros
**dimensão (d)**: número de direções independentes de um espaço (em 3D: altura, largura, profundidade)
**números de Mersenne**: números da forma 2^(n+1) - 1, usados como base para gerar os pontos
**espaço tridimensional**: espaço com 3 eixos: x, y e z
**combinação convexa**: média ponderada de pontos onde os pesos somam 1 e são positivos
