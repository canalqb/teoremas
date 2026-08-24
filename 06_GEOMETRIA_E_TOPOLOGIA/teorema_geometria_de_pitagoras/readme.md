# 📐 - Teorema das Ternas Pitagóricas  
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![LGN](https://img.shields.io/badge/Teorema-Ternas%20Pitagóricas-ff69b4.svg)](https://en.wikipedia.org/wiki/Pythagorean_triple)

## Frase do Teorema

> Uma terna pitagórica é um conjunto de três números inteiros a, b e c que satisfazem a relação a² + b² = c² – ou seja, eles representam os lados de um triângulo retângulo com medidas inteiras.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `pitagoricas.py`](#2-script-pitagoricaspy)  
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

# 1. Introdução ao Teorema

## 1.1 Resumo

As **ternas pitagóricas** são conjuntos de três números inteiros que satisfazem a relação fundamental dos triângulos retângulos: a² + b² = c². Essas ternas podem ser **primitivas** (quando a, b e c não têm nenhum divisor comum além do 1) ou **não primitivas** (múltiplos das primitivas).

## 1.2 Exemplos Práticos

Exemplo clássico: (3, 4, 5), pois 3² + 4² = 9 + 16 = 25 = 5².

Outros exemplos incluem (5, 12, 13) e (8, 15, 17).

## 1.3 Explicação Detalhada

O script gera essas ternas usando o método de Euclides:

- Para dois números inteiros m e n, com m > n > 0, onde m e n são coprimos e têm paridade diferente (um é par, outro é ímpar),
- Calcula-se:  
  * a = m² - n²  
  * b = 2 * m * n  
  * c = m² + n²  
- Essas fórmulas garantem que (a, b, c) formam uma terna pitagórica primitiva.

Se for permitido gerar ternas não primitivas, o script também cria múltiplos desses valores.

## 1.4 Aplicações

- Estudo de propriedades de números inteiros.  
- Problemas clássicos em matemática e educação.  
- Aplicações em computação gráfica e geometria.

## 1.5 Análise da Tabela

O script organiza as ternas em intervalos de hipotenusa delimitados por potências de 2, mostrando como elas se distribuem e facilitando análises quantitativas e gráficas.

---

# 2. Script `pitagoricas.py`

## 2.1 Relação com o Teorema

O script é uma implementação computacional prática do método para gerar ternas pitagóricas, ilustrando de forma automatizada a geração de múltiplas soluções para o teorema clássico.

## 2.2 Objetivo do Script

Gerar ternas pitagóricas primitivas e não primitivas dentro de intervalos de hipotenusa delimitados por potências de 2, exportar os resultados e plotar graficamente os pares (a, b).

## 2.3 Exemplo de Saída

```

2–3 -> a = 3, b = 4, c = 5
4–7 -> a = 8, b = 6, c = 10
...

```

## 2.4 Funcionamento Interno

- Para cada valor c entre 2^c e 2^(c+1)-1, o script gera ternas.  
- Usa o método de Euclides para encontrar ternas primitivas.  
- Se habilitado, gera múltiplos para ternas não primitivas.  
- Salva resultados em arquivos CSV e JSON.  
- Cria um gráfico dos valores a e b usando Matplotlib.

## 2.5 Tecnologias e Requisitos

- **Python 3.8.10**  
- Biblioteca externa: `matplotlib` (para visualização gráfica)  

Para instalar:

```bash
pip install matplotlib
````

---

# 3 Extras

## 3.1 Licença

Licença MIT — código aberto para uso e modificação.

## 3.2 Referências

* Euclides, *Elementos*
* [https://en.wikipedia.org/wiki/Pythagorean\_triple](https://en.wikipedia.org/wiki/Pythagorean_triple)
* [https://en.wikipedia.org/wiki/Euclid%27s\_formula](https://en.wikipedia.org/wiki/Euclid%27s_formula)

## 3.3 Testes e Validações

Os resultados são validados pela fórmula clássica, garantindo que as ternas satisfazem a equação pitagórica.

---

# 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

# 5. Nota

**Primitiva:** uma terna pitagórica é primitiva se os três números não têm nenhum divisor comum além de 1.

**Não primitiva:** múltiplos das ternas primitivas, ou seja, todas as três medidas são multiplicadas pelo mesmo número inteiro.

**Coprimos:** dois números que não têm nenhum divisor comum maior que 1.

**Hipotenusa:** o lado mais longo do triângulo retângulo, oposto ao ângulo de 90 graus.

**Potência de 2:** números na forma 2 elevado a um número inteiro, como 2, 4, 8, 16, etc., usados aqui para delimitar intervalos de hipotenusas.
