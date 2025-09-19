## 🧮 - Teorema de Jordan

[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Jordan](https://img.shields.io/badge/Teorema-Funções%20de%20Variação%20Limitada-ff69b4.svg)](https://pt.wikipedia.org/wiki/Fun%C3%A7%C3%A3o_de_varia%C3%A7%C3%A3o_limitada)

## Frase do Teorema

> *Toda função com variação limitada pode ser representada como a diferença entre duas funções crescentes.* – Ou seja, se uma função sobe e desce, mas sem “explodir” em variações muito bruscas, dá pra reescrevê-la usando só duas funções que só crescem.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `teorema_jordan_animado.py`](#2-script-teorema_jordan_animadopy)

  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3 Extras](#3-extras)

  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referências)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4 Contato](#4-contato)
* [5. Nota](#5-nota)

---

## 1. Introdução ao Teorema

### 1.1 Resumo

O *Teorema de Jordan* afirma que uma função que **não varia de forma infinita** pode ser escrita como a **diferença entre duas funções que só crescem**. Isso ajuda a analisar e entender funções que parecem complicadas, mas têm comportamento “limitado”.

---

### 1.2 Exemplos Práticos

* Sinais com oscilações suaves, como curvas senoidais ou variações de temperatura ao longo do dia.
* Funções que sobem e descem mas sem explosões ou picos extremos.

---

### 1.3 Explicação Detalhada

Se você pegar uma função qualquer $f(n)$, e ela **não oscilar violentamente**, ou seja, tiver uma *variação total finita*, então dá pra separar essa função em duas partes:

* Uma função que **só cresce** (chamada de f1),
* E outra função que **também só cresce** (chamada de f2),
* E fazer: `f(n) = f1(n) - f2(n)`

Mesmo que f oscile (suba e desça), essa decomposição é possível sempre que as variações forem "controladas".

---

### 1.4 Aplicações

* 💡 Análise de sinais discretos
* 🎚️ Processamento de áudio e controle de ruído
* 📈 Análise de dados com tendências e oscilações
* 🤖 Treinamento de IA para reconhecer padrões crescentes/decrescentes
* 💧 Simulação de perturbações (como ondas na água)

---

### 1.5 Análise da Tabela

O script imprime uma tabela com:

* Os valores de entrada (n),
* A função com ondas (`f(n)`),
* As funções crescentes `f1(n)` e `f2(n)`,
* E a reconstrução `f1 - f2`.

Isso ajuda a ver, ponto a ponto, como a decomposição se comporta.

---

## 2. Script `teorema_jordan_animado.py`

### 2.1 Relação com o Teorema

O script é um exemplo direto do que o teorema propõe. Ele pega uma função discreta com variação limitada e:

* Cria curvas oscilantes com base em potências de 2 e números de Mersenne,
* Aplica uma decomposição crescente,
* E exibe tudo com gráficos animados.

---

### 2.2 Objetivo do Script

Mostrar, de forma visual e animada, como uma função oscilante pode ser representada como a diferença de duas funções crescentes.

---

### 2.3 Exemplo de Saída

* 4 gráficos exibidos lado a lado:

  * f(n)
  * f1(n)
  * f2(n)
  * f1(n) - f2(n)

* Cada ponto tem um valor numérico visível,

* Uma “onda” aparece nos gráficos, como se uma pedra tivesse sido jogada no meio das curvas,

* O GIF final é salvo como `animacao_teorema_jordan.gif`.

---

### 2.4 Funcionamento Interno

1. Cria valores com base em `log2(2^n - 1) + senoidal`.
2. Calcula a **variação total** e faz a decomposição crescente.
3. Mostra os gráficos com valores e **animações realistas de ondas**.
4. Exporta o resultado em GIF.

---

### 2.5 Tecnologias e Requisitos

* 🐍 Python **3.8.10**
* 📦 Bibliotecas:

  * `numpy`
  * `matplotlib`
  * `pandas`
  * `pillow` (para salvar GIF)

Instale com:

```bash
pip install numpy matplotlib pandas pillow
```

---

## 3 Extras

### 3.1 Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).

---

### 3.2 Referências

* [Wikipedia - Funções de Variação Limitada](https://pt.wikipedia.org/wiki/Fun%C3%A7%C3%A3o_de_varia%C3%A7%C3%A3o_limitada)
* [Teorema de Jordan](https://en.wikipedia.org/wiki/Bounded_variation)
* Artigos acadêmicos sobre decomposição de funções

---

### 3.3 Testes e Validações

* ✅ Testado no Windows com Python 3.8.10
* ✅ Verificado que os valores batem com a função original
* ✅ GIF gerado com sucesso na pasta do projeto

---

## 4 Contato

* Feito por **CanalQb** no GitHub
* Visite o blog: canalqb.blogspot.com → [https://canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* 📬 PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**função crescente:**
Uma função onde os valores só aumentam ou ficam iguais, nunca diminuem.

**variação limitada:**
Quer dizer que a soma de todas as subidas e descidas da função tem um valor total que não explode (é finito).

**log2:**
Função logarítmica na base 2. Cresce devagar, usada para representar escalas como potências.

**senoidal:**
Uma curva que sobe e desce suavemente, como uma onda.

**número de Mersenne:**
Número da forma `2^n - 1`. Usado muito em criptografia e teoria dos números.

**função discreta:**
Uma função que trabalha com valores separados (como n = 1, 2, 3...), em vez de um intervalo contínuo.

**decomposição:**
Separar uma função complicada em partes mais simples que são mais fáceis de analisar.
