# 🧩 - Complexa Dos Residuos

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Frase do conceito

> Se calcularmos os valores especiais chamados resíduos de uma função complexa em certos pontos e somarmos, podemos entender propriedades importantes da função, usando números especiais chamados números de Mersenne para explorar essas relações.

## Sumário

* [1. Introdução ao Conceito](#1-introdução-ao-conceito)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `residuos.py`](#2-script-residuospy)

  * [2.1 Relação com o Conceito](#21-relação-com-o-conceito)
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

## 1 Introdução ao Conceito

### 1.1 Resumo

Este projeto calcula valores chamados **resíduos** de uma função matemática que depende de um parâmetro chamado *n*. Esses resíduos são somados para mostrar uma propriedade importante da função. O cálculo envolve também os **números de Mersenne**, que são números especiais definidos como (2^n - 1).

### 1.2 Exemplos Práticos

Para cada valor de *n* de 0 a 10, o script encontra pontos especiais chamados *polos* da função, calcula os resíduos nesses pontos, e multiplica alguns resíduos pelos números de Mersenne correspondentes. Depois, plota esses valores para visualização.

### 1.3 Explicação Detalhada

- **Resíduos:** são números que ajudam a entender o comportamento da função em pontos onde ela "explode" ou é indefinida.
- **Polos:** são esses pontos especiais onde a função não é normal.
- **Números de Mersenne:** são números formados por (2^n - 1), usados aqui para analisar propriedades numéricas relacionadas aos resíduos.

### 1.4 Aplicações

Este tipo de análise é útil para entender funções complexas e suas propriedades em matemática avançada e física teórica.

### 1.5 Análise da Tabela

O script imprime uma tabela no console para cada valor de *n*, mostrando:

- O valor de a_n = 2^n
- O número de Mersenne M_n = 2^n - 1
- Os polos da função
- Os resíduos calculados em cada polo
- A soma dos resíduos multiplicada por uma constante para mostrar um resultado importante

---

## 2 Script `residuos.py`

### 2.1 Relação com o Conceito

O script automatiza o cálculo dos resíduos e a relação com os números de Mersenne, e plota os resultados para facilitar a visualização.

### 2.2 Objetivo do Script

- Calcular resíduos da função para valores de *n* entre 0 e 10.
- Mostrar como esses resíduos se comportam quando multiplicados por números de Mersenne.
- Exibir um gráfico com os resultados.
- Animar um ponto que se movimenta no gráfico, mostrando a trajetória desses valores conforme *n* varia.

### 2.3 Exemplo de Saída

```plaintext
--------------------------------------------------
n = 10, a_n = 2^10 = 1024, M_n = 2^10 - 1 = 1023
Polos de f(z): [-32*I, 32*I]
  Resíduo em z = -32*I: 0.5 + 15.98*I
  Resíduo em z = 32*I: 0.5 - 15.98*I
Integral de contorno ∮ f(z) dz = 6.28318530717959*I
--------------------------------------------------
````

### 2.4 Funcionamento Interno

* Usa a biblioteca **sympy** para manipular expressões simbólicas.
* Calcula polos e resíduos.
* Usa **matplotlib** para desenhar o gráfico e animar o ponto.
* Utiliza **numpy** para cálculos numéricos, especialmente para gerar cores.

### 2.5 Tecnologias e Requisitos

* Python 3.8.10
* Bibliotecas: sympy, numpy, matplotlib

---

## 3 Extras

### 3.1 Licença

Este projeto está sob a licença MIT — veja o arquivo LICENSE para detalhes.

### 3.2 Referências

* Documentação SymPy: [https://www.sympy.org](https://www.sympy.org)
* Documentação Matplotlib: [https://matplotlib.org](https://matplotlib.org)
* Números de Mersenne: [https://pt.wikipedia.org/wiki/Número\_de\_Mersenne](https://pt.wikipedia.org/wiki/Número_de_Mersenne)

### 3.3 Testes e Validações

O script imprime os resultados no console para revisão manual e plota um gráfico para validação visual.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5 Nota

**Integral:** soma dos pequenos pedaços de uma função para achar área ou outras grandezas.
**Função:** uma regra que transforma um número em outro número.
**Polos:** pontos onde a função não se comporta normalmente (explode ou fica indefinida).
**Resíduo:** número que mostra como a função se comporta perto de um polo.
**Número de Mersenne:** número especial da forma 2^n - 1, usado para estudar propriedades matemáticas.
**Parte real:** o número "normal" que compõe um número complexo.
**Parte imaginária:** a parte que multiplica o símbolo "i", que é a raiz quadrada de -1.
