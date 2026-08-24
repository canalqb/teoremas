# 🔢 - Teorema de Euler-Fermat

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)

## 💬 Frase do Teorema

> Para dois números **a** e **n** que não compartilham divisores além do 1, a elevado à quantidade de números menores que n que não dividem n, deixa resto 1 quando dividido por n.
> *Ou seja: a^phi(n) mod n = 1.*

## 📑 Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `Teorema_de_Euler–Fermat.py`](#2-script-teorema_de_euler–fermatpy)

  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3. Script `verifica_totiente_coprimos.py`](#3-script-verifica_totiente_coprimospy)

  * [3.1 Relação com o Teorema](#31-relação-com-o-teorema)
  * [3.2 Objetivo do Script](#32-objetivo-do-script)
  * [3.3 Exemplo de Saída](#33-exemplo-de-saída)
* [4. Extras](#4-extras)

  * [4.1 Licença](#41-licença)
  * [4.2 Referências](#42-referências)
  * [4.3 Testes e Validações](#43-testes-e-validações)
* [5. Contato](#5-contato)
* [6. Nota](#6-nota)

---

## 1. Introdução ao Teorema

### 1.1 Resumo

O **Teorema de Euler-Fermat** é uma regra da *teoria dos números* que estende o conceito do Pequeno Teorema de Fermat. Ele ajuda a entender o comportamento de potências em relação a divisões, especialmente útil em criptografia.

### 1.2 Exemplos Práticos

Se escolhermos um número **a** que não divide o número **n**, e levantarmos **a** à potência de *phi(n)* (que é uma função que conta quantos números menores que n não têm fatores em comum com n), o resultado dividido por n deixa resto 1.

### 1.3 Explicação Detalhada

*Coprimidade* significa que dois números não têm nenhum divisor em comum, exceto 1. Por exemplo, 8 e 15 são coprimos porque não dividem nenhum número além de 1 juntos. Já 8 e 12 não são, porque dividem 2 e 4 também.

A função *totiente de Euler*, phi(n), conta quantos números entre 1 e n são coprimos com n. Por exemplo, phi(8) é 4, porque 1, 3, 5 e 7 não dividem 8.

O teorema diz que se a e n forem coprimos, então:

**a^phi(n) mod n = 1**

Ou seja, se dividirmos a elevado a phi(n) por n, o resto é 1.

### 1.4 Aplicações

Esse teorema é usado em criptografia, principalmente em sistemas que dependem de propriedades matemáticas dos números, como RSA, onde entender a relação entre números e seus restos é crucial.

### 1.5 Análise da Tabela

Os scripts analisam intervalos de números, mostrando quais passam no teste do teorema, relacionando com números primos e compostos, destacando os chamados pseudoprimos (compostos que “enganam” o teste).

---

## 2. Script `Teorema_de_Euler–Fermat.py`

### 2.1 Relação com o Teorema

O script verifica a propriedade do Teorema de Euler-Fermat para uma base fixa a=2 em diversos números, mostrando se eles passam ou não no teste.

### 2.2 Objetivo do Script

Testar números em intervalos específicos para confirmar se eles obedecem a regra **2^phi(n) mod n = 1**, e informar se são primos ou não.

### 2.3 Exemplo de Saída

```
🔎 Análise usando Teorema de Euler–Fermat (base a=2)

Intervalo: [1, 1]
Número Procurado: 1
 → É primo? Não
 → Totiente φ(1) = 1
 → Verificação Euler-Fermat: 2^φ(n) mod n == 1? Sim
----------------------------------------
...
```

### 2.4 Funcionamento Interno

O script usa funções da biblioteca `sympy` para:

* Checar se o número é primo
* Calcular o totiente phi(n)
* Verificar a propriedade do teorema, calculando 2 elevado a phi(n) módulo n

### 2.5 Tecnologias e Requisitos

* Python 3.8.10
* Biblioteca `sympy` (para funções matemáticas avançadas)
* Módulo `math` para cálculo do máximo divisor comum (gcd)

---

## 3. Script `verifica_totiente_coprimos.py`

### 3.1 Relação com o Teorema

Esse script calcula manualmente o totiente de Euler, contando números coprimos a n, reforçando o conceito usado no teorema.

### 3.2 Objetivo do Script

Exibir uma tabela comparativa de números e seus totientes para diferentes intervalos, relacionando com números especiais (potências de 2 e números de Mersenne).

### 3.3 Exemplo de Saída

```
Início | Procurado | Fim | Totiente(phi(Fim))
     1 |        1 |   1 |                  1
     2 |        3 |   3 |                  2
     4 |        7 |   7 |                  6
     8 |        8 |  15 |                  8
    16 |       21 |  31 |                 30
    32 |       49 |  63 |                 36
    64 |       76 | 127 |                126
   128 |      224 | 255 |                128
   256 |      467 | 511 |                432
```

---

## 4. Extras

### 4.1 Licença

Projeto sob licença **MIT** — veja o arquivo LICENSE para detalhes.

### 4.2 Referências

* [Teorema de Euler-Fermat - Wikipedia](https://en.wikipedia.org/wiki/Euler%27s_theorem)
* [Função Totiente de Euler](https://en.wikipedia.org/wiki/Euler%27s_totient_function)
* [Pequeno Teorema de Fermat](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem)

### 4.3 Testes e Validações

Os scripts foram testados com múltiplos intervalos e validam os conceitos conforme esperado, evidenciando os pseudoprimos e os primos verdadeiros.

---

## 5. Contato

* Feito por **CanalQb** no GitHub
* Visite o blog: [canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 6. Nota

* **Coprimos**: números que não têm nenhum divisor comum além do 1. Exemplo: 8 e 15 são coprimos porque só dividem 1 em comum.
* **Totiente de Euler (phi(n))**: número de inteiros positivos menores ou iguais a n que são coprimos com n.
* **Base (a)**: número escolhido para elevar à potência phi(n). No script usamos a=2 para simplificar.
* **Pseudoprimos**: números compostos que passam no teste do teorema para alguma base, “enganando” o teste de primalidade.

--- 
