# 🔍 - Análise do Teorema de Cauchy com Números de Mersenne  
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  

## Frase do Teorema

> Se uma função é bem comportada dentro de um círculo, o valor da integral dela ao redor desse círculo depende só do que acontece nos pontos dentro dele – mesmo que pareça complicado, a integral é muito simples quando o ponto está dentro do círculo e zero quando está fora.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `teorema_cauchy_mersenne.py`](#2-script-teorema_cauchy_mersennepy)  
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

Este conceito diz que, para funções que não dão “problema” dentro de um círculo, a integral delas ao redor desse círculo depende só dos valores nos pontos dentro dele. Se o ponto especial está dentro do círculo, a integral tem um valor fixo; se estiver fora, a integral é zero.

### 1.2 Exemplos Práticos

Imagine que você tenha uma corda amarrada em um círculo e quer saber a soma de forças atuando nela. Se nenhuma força está dentro do círculo, a soma total ao redor é zero. Se há uma força dentro, a soma segue uma regra simples e conhecida.

### 1.3 Explicação Detalhada

O script usa números especiais chamados **números de Mersenne** (que são 2 elevado a n menos 1) como pontos \(a\) para testar essa ideia. O círculo tem raio 1.  
Para cada n, calculamos a integral da função com um ponto singular em \(a\) e comparamos com o valor esperado segundo a regra. Se o ponto \(a\) está dentro do círculo (menor que 1), a integral deve ser igual a um valor específico; se estiver fora, deve ser zero.  

### 1.4 Aplicações

Esse conceito é útil em física para entender campos elétricos e magnéticos, engenharia para análise de sistemas complexos, e em matemática para resolver problemas que envolvem funções complexas.

### 1.5 Análise da Tabela

O script mostra que quando \(a\) está dentro do círculo (|a| < 1), a integral se comporta conforme esperado, e o erro entre o valor calculado e esperado é quase zero. Quando \(a\) está fora do círculo, a integral se aproxima de zero.

---

## 2 Script `teorema_cauchy_mersenne.py`

### 2.1 Relação com o Teorema

Este script verifica na prática como a integral ao redor do círculo muda conforme a posição do ponto \(a\). Ele compara o valor da integral com o esperado pelo conceito matemático, validando a teoria.

### 2.2 Objetivo do Script

Calcular valores de integrais complexas para funções específicas, usando números de Mersenne para testar o comportamento da integral no círculo unitário, e medir o erro entre o valor calculado e o valor esperado.

### 2.3 Exemplo de Saída

```

n= 0, a=   0.0, |a|=0.00, Integral=+0.00000+6.28319j, Esperado=+0.00000+6.28319j, Erro=2.46e-17
n= 1, a=   1.0, |a|=1.00, Integral=-0.00000+3.14159j, Esperado=+0.00000+0.00000j, Erro=3.14e+00
n= 2, a=   3.0, |a|=3.00, Integral=+0.00000+0.00000j, Esperado=+0.00000+0.00000j, Erro=2.22e-16
...

```

### 2.4 Funcionamento Interno

- Define um círculo de raio 1;
- Para cada n de 0 a 10, calcula o número de Mersenne \(a = 2^n - 1\);
- Define a função f(z) = z^n;
- Calcula a integral da função f(z)/(z - a) ao redor do círculo;
- Verifica se o ponto \(a\) está dentro do círculo para determinar o valor esperado da integral;
- Calcula o erro entre valor esperado e o calculado;
- Mostra gráficos com o erro absoluto e o valor absoluto dos números de Mersenne para visualização.

### 2.5 Tecnologias e Requisitos

- Python 3.8.10  
- Bibliotecas: numpy, scipy, matplotlib  

---

## 3 Extras

### 3.1 Licença

Este projeto está sob a licença MIT, permitindo uso, modificação e distribuição livre com atribuição.

### 3.2 Referências

- [Números de Mersenne - Wikipédia](https://pt.wikipedia.org/wiki/Número_de_Mersenne)  
- [Teorema de Cauchy - Wikipédia](https://pt.wikipedia.org/wiki/Teorema_de_Cauchy)  
- Documentação oficial de [SciPy](https://docs.scipy.org/doc/scipy/) e [Matplotlib](https://matplotlib.org/)  

### 3.3 Testes e Validações

O script imprime os valores numéricos e o erro para cada n, mostrando a precisão do cálculo e confirmando que o comportamento da integral segue a expectativa.

---

## 4 Contato

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com ([https://canalqb.blogspot.com](https://canalqb.blogspot.com))  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*

---

## 5 Nota

**Função:** é uma regra que associa cada entrada a uma saída específica, como uma receita que para cada ingrediente dá um prato.  

**Integral:** é a soma contínua de pequenas partes, como somar todas as áreas sob uma curva para achar a área total.  

**Número de Mersenne:** um número da forma (2 elevado a n) menos 1; por exemplo, para n=3, é 2³-1=7.  

**Erro Absoluto:** diferença entre o valor calculado e o valor esperado, mostrando o quanto o resultado se afastou do que deveria ser.  

**Raio do círculo:** distância do centro até a borda do círculo.  

**Valor esperado:** o resultado que a teoria prevê para a integral, usado para comparar com o valor calculado. 
