# 🧠 - Teorema Casorati–Weierstrass
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Complex Analysis](https://img.shields.io/badge/Teorema-Casorati--Weierstrass-ff69b4.svg)](https://en.wikipedia.org/wiki/Casorati%E2%80%93Weierstrass_theorem)

## Frase do Teorema

> *O Teorema de Casorati–Weierstrass afirma que se uma função tem uma singularidade essencial em um ponto, então, perto desse ponto, os valores da função ficam "bagunçados", ou seja, ela assume valores arbitrariamente próximos de qualquer número complexo.* – **Mesmo que pareça haver um padrão, a função se comporta de forma imprevisível perto de uma singularidade essencial.**

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `Casorati–Weierstrass.py`](#2-script-casorati–weierstrasspy)
  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3. Extras](#3-extras)
  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referências)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4. Contato](#4-contato)
* [5. Nota](#5-nota)

---

## 1. Introdução ao Teorema

### 1.1 Resumo

O Teorema de Casorati–Weierstrass trata do comportamento das funções complexas **perto de pontos perigosos**, chamados de *singularidades essenciais*. Ele mostra que nessas regiões, a função assume **todos os valores possíveis do plano complexo**, sem seguir um padrão previsível.

### 1.2 Exemplos Práticos

A função `f(z) = e^(1/z)` tem uma singularidade essencial em `z = 0`. Perto desse ponto, os valores de `f(z)` **variam muito rapidamente**, criando um "caos" visual quando plotados.

### 1.3 Explicação Detalhada

Mesmo que `z` fique *muito próximo de zero*, `f(z)` pode assumir **valores enormes, minúsculos, positivos, negativos ou até com partes imaginárias gigantes**. Isso mostra que **não há limite nem direção fixa** – um comportamento totalmente diferente de outras funções mais comportadas.

### 1.4 Aplicações

Esse teorema é útil em:

- Análise de funções complexas
- Estudo de caos e dinâmica complexa
- Processamento de sinais e transformadas complexas
- Geração de fractais e arte matemática

### 1.5 Análise da Tabela

O script gera uma tabela com:

- O ponto de entrada `z`
- O valor da função `f(z)`
- A **velocidade de rotação de cada ponto** (em graus por frame)

Esses pontos são representados no gráfico com cores e movimentos diferentes para **visualizar o "caos" criado pela singularidade essencial**.

---

## 2. Script `Casorati–Weierstrass.py`

### 2.1 Relação com o Teorema

O script mostra graficamente como os valores de `f(z) = e^(1/z)` se comportam perto de uma singularidade essencial. A animação reforça visualmente o que o teorema afirma.

### 2.2 Objetivo do Script

- Plotar valores de `f(z)` para pontos `z` específicos (potências de 2 e números de Mersenne)
- Mostrar esses valores rotacionando com **velocidades diferentes**
- Visualizar a "densidade de valores" em torno da singularidade

### 2.3 Exemplo de Saída

```text
Index | Tipo             | z (input)   | f(z) (output)         | Velocidade (°/frame)
-------------------------------------------------------------------------------------
0     | Potência de 2    | 1+0j        | 2.718...              | 0.79
...
15    | Número de Mersenne | 2047+0j   | 1.0004...             | 0.76
````

E então é exibido um gráfico animado onde cada ponto gira de forma independente.

### 2.4 Funcionamento Interno

* Os pontos são processados e centralizados
* Cada ponto recebe uma **velocidade angular única**
* `matplotlib` anima o gráfico, com rotação independente por ponto

### 2.5 Tecnologias e Requisitos

* Python **3.8.10**
* Bibliotecas:

  * `numpy`
  * `matplotlib`

Instale com:

```bash
pip install numpy matplotlib
```

---

## 3. Extras

### 3.1 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

### 3.2 Referências

* Wikipedia: [Casorati–Weierstrass Theorem](https://en.wikipedia.org/wiki/Casorati%E2%80%93Weierstrass_theorem)
* Complex Analysis Textbooks
* CanalQB no GitHub e Blogspot

### 3.3 Testes e Validações

✅ Rodado em Python 3.8.10
✅ Verificado com animação funcional
✅ Tabela e animação sincronizadas com precisão

---

## 4. Contato

* Feito por **CanalQb** no GitHub
* Visite o blog: [canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via **Bitcoin**: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* **PIX:** [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **Singularidade essencial**: ponto onde a função se comporta de forma totalmente imprevisível.
* **Plano complexo**: é como um plano cartesiano, mas os valores têm parte real e parte imaginária.
* **Função exponencial complexa**: uma função como `e^(1/z)` que cresce muito rápido e gira no plano.
* **Número de Mersenne**: número que segue a fórmula `2^p - 1`, geralmente usado em criptografia e teoria dos números.
* **Velocidade angular**: o quanto um ponto gira por unidade de tempo (ou frame), medida aqui em graus por frame.
