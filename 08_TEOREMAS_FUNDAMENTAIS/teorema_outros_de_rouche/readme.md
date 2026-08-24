# 🧩 - De Rouche
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)  

## Frase do Teorema

> Se duas funções são parecidas na borda de uma região, elas têm o mesmo número de zeros dentro dessa região – uma forma simples de contar onde uma função zera sem precisar achar cada ponto.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `Rouche.py`](#2-script-rouchepy)  
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

## 1 Introdução ao Teorema

### 1.1 Resumo  
O teorema permite comparar duas funções dentro de uma região para saber quantos zeros uma delas tem, apenas olhando seus valores na borda dessa região. Isso facilita a análise de funções complexas sem precisar resolver equações complicadas.

### 1.2 Exemplos Práticos  
Imagine querer saber quantas soluções uma equação polinomial tem dentro de um círculo no plano sem calcular todas as soluções. Usando esse resultado, podemos garantir o número de zeros com uma análise simples.

### 1.3 Explicação Detalhada  
O teorema diz que, se uma função "g" for menor que outra função "f" na borda de uma região, então "f" e "f + g" têm o mesmo número de zeros dentro dela. Isso acontece porque a soma não altera a contagem de pontos onde a função zera, desde que a perturbação seja pequena na borda.

### 1.4 Aplicações  
Usado em análise complexa, física matemática, engenharia e qualquer área que precise estimar raízes de funções complexas, especialmente polinômios e séries.

### 1.5 Análise da Tabela  
A tabela mostra valores da função para pontos importantes como potências de 2 e números especiais chamados Mersennes, ajudando a visualizar o comportamento da função e a identificar regiões onde ela muda de sinal.

---

## 2 Script `Rouche.py`

### 2.1 Relação com o Teorema  
O script calcula valores da função f(z) = z^5 + 3z + 1 em pontos estratégicos, como potências de 2 e números de Mersenne, e identifica aproximações de zeros entre esses pontos para ilustrar o conceito do teorema.

### 2.2 Objetivo do Script  
Demonstrar como podemos estimar os zeros de uma função e visualizar seu comportamento através de uma tabela de valores e um gráfico com pontos destacados.

### 2.3 Exemplo de Saída  
```

```
z     |  f(z) = z^5 + 3z + 1
```

---

-8.000 |    -32791.0000  (Potência de 2)
-4.000 |     -1035.0000  (Potência de 2)
-2.000 |       -37.0000  (Potência de 2)
-1.000 |        -3.0000  (Potência de 2)
-0.500 |        -0.5312  (Potência de 2)
-0.250 |         0.2490  (Potência de 2)
0.250 |         1.7510  (Potência de 2)
0.500 |         2.5312  (Potência de 2)
1.000 |         5.0000  (Potência de 2)
2.000 |        39.0000  (Potência de 2)
3.000 |       253.0000  (Mersenne)
4.000 |      1037.0000  (Potência de 2)
7.000 |     16829.0000  (Mersenne)
8.000 |     32793.0000  (Potência de 2)

Raízes aproximadas encontradas entre os pontos:
-0.33199 -> f(z) = -7.91953e-07

```

### 2.4 Funcionamento Interno  
- Calcula valores da função em pontos escolhidos (potências de 2 e Mersennes).  
- Procura intervalos onde a função muda de sinal, indicando um zero.  
- Aplica um método simples para achar uma raiz aproximada nesses intervalos.  
- Gera gráfico com pontos destacados e legendas que mostram os valores arredondados.  

### 2.5 Tecnologias e Requisitos  
- Python 3.8.10  
- Bibliotecas: numpy, matplotlib  

---

## 3 Extras

### 3.1 Licença  
MIT License – uso livre, com créditos ao autor.

### 3.2 Referências  
- Livros e cursos introdutórios de análise complexa e polinômios.  
- Wikipedia e materiais online sobre números de Mersenne e análise numérica.

### 3.3 Testes e Validações  
O script foi testado para vários valores e funções similares para garantir consistência na aproximação dos zeros.

---

## 4 Contato

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

- **λ (lambda)**: símbolo grego usado para representar valores ou constantes, como números que mudam de acordo com o contexto.  
- **Função**: regra que associa cada número de entrada a um único número de saída.  
- **Número de Mersenne**: número da forma 2^p - 1, onde p é um número primo; usados em matemática para estudar propriedades especiais dos números.  
- **Raiz de uma função**: ponto onde o valor da função é zero, ou seja, onde a curva toca o eixo horizontal.  
- **Bissecção**: método simples para encontrar zeros de uma função dividindo intervalos ao meio repetidamente.  
- **Polinômio**: expressão matemática feita de somas de potências de um número multiplicadas por coeficientes.
