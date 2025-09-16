# ⚙️ - Teorema do Argumento de Cauchy

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Frase do teorema

> A diferença entre a quantidade de zeros e polos de uma função dentro de uma curva fechada pode ser calculada pelo caminho que a função faz no plano complexo quando percorremos essa curva — isto ajuda a entender onde estão os zeros e polos sem precisar encontrá-los diretamente.

## Sumário

* [1. Introdução ao teorema ⚡](#1-introdução-ao-teorema-⚡)

  * [1.1 Resumo ✨](#11-resumo-✨)
  * [1.2 Exemplos práticos 🧮](#12-exemplos-práticos-🧮)
  * [1.3 Explicação detalhada 🔍](#13-explicação-detalhada-🔍)
  * [1.4 Aplicações 🚀](#14-aplicações-🚀)
  * [1.5 Análise da tabela 📊](#15-análise-da-tabela-📊)
* [2. Script Argumento\_de\_Cauchy.py 🐍](#2-script-argumento_de_cauchypy-🐍)

  * [2.1 Relação com o teorema 🔗](#21-relação-com-o-teorema-🔗)
  * [2.2 Objetivo do script 🎯](#22-objetivo-do-script-🎯)
  * [2.3 Exemplo de saída 💻](#23-exemplo-de-saída-💻)
  * [2.4 Funcionamento interno ⚙️](#24-funcionamento-interno-⚙️)
  * [2.5 Tecnologias e requisitos 🧰](#25-tecnologias-e-requisitos-🧰)
* [3. Extras 📚](#3-extras-📚)

  * [3.1 Licença 📄](#31-licença-📄)
  * [3.2 Referências 📖](#32-referências-📖)
  * [3.3 Testes e validações 🧪](#33-testes-e-validações-🧪)
* [4. Contato 📬](#4-contato-📬)
* [5. Nota 📝](#5-nota-📝)

---

## 1. Introdução ao teorema ⚡

### 1.1 Resumo ✨

O resultado aqui mostra que, para uma função que pode ter *zeros* (onde a função vira zero) e *polos* (onde ela "explode"), a diferença entre o número desses pontos dentro de uma curva fechada pode ser determinada ao analisar o caminho da função no plano complexo. Isso evita precisar encontrar diretamente todos os zeros e polos.

### 1.2 Exemplos práticos 🧮

Imaginemos uma função que tem zeros em números que são potências de 2 (como 1, 2, 4, 8, 16...) e polos em números chamados de "mersennes" (números da forma 2^k - 1, como 0, 1, 3, 7, 15...). Para diferentes tamanhos de curva, podemos contar quantos zeros e polos estão dentro e calcular essa diferença.

### 1.3 Explicação detalhada 🔍

* *Zero*: ponto onde a função vale zero.
* *Polo*: ponto onde a função cresce para infinito (ou seja, "explode").
* O caminho da função ao redor da curva "registra" a diferença entre esses pontos.
* Calculamos um integral ao longo da curva que dá essa diferença.

### 1.4 Aplicações 🚀

Esse método pode ser usado para:

* Estimar a quantidade de zeros e polos em regiões complexas.
* Analisar estabilidade em engenharia.
* Ajudar no estudo de funções complexas sem precisar achar suas raízes explicitamente.

### 1.5 Análise da tabela 📊

A tabela resultante mostra, para cada valor n de 0 a 10:

* O tamanho da curva (raio R) considerada.
* Quantidade de zeros e polos dentro da curva.
* Diferença entre essas quantidades.
* Representação dos zeros (potências de 2) e polos (mersennes).
* Valor estimado do cálculo integral que confirma essa diferença.

---

## 2. Script Argumento\_de\_Cauchy.py 🐍

### 2.1 Relação com o teorema 🔗

O script simula o cálculo da diferença entre zeros e polos dentro de curvas circulares que crescem com n, usando potências de 2 para zeros e números mersennes para polos.

### 2.2 Objetivo do script 🎯

* Calcular o valor da integral que estima a diferença entre zeros e polos.
* Mostrar a contagem exata de zeros e polos dentro da curva.
* Apresentar uma comparação entre a contagem e o valor da integral.

### 2.3 Exemplo de saída 💻

```plaintext
n | Raio R       | Zeros dentro | Polos dentro | Z - P (contagem) | Zeros           | Polos (Mersenne)          | Z-P (estimado)
------------------------------------------------------------------------------------------------------------------------
 0 | 1.5          | 1            | 1            | 0                | 2^0             | 2^0-1                     | -0.0000
 1 | 2.5          | 2            | 2            | 0                | 2^0 2^1         | 2^0-1 2^1-1               | 0.0000
... (continua até n=10)
```

### 2.4 Funcionamento interno ⚙️

* Define os zeros e polos para cada n.
* Calcula a função e sua derivada numericamente no plano complexo.
* Usa uma curva circular para integrar a função derivada/função.
* Conta quantos zeros e polos estão dentro do círculo definido pelo raio.
* Compara o valor do integral com a contagem.

### 2.5 Tecnologias e requisitos 🧰

* Python 3.8.10
* Biblioteca numpy para cálculos numéricos
* Terminal ou ambiente que rode Python com saída padrão

---

## 3. Extras 📚

### 3.1 Licença 📄

Código aberto sob a licença MIT.

### 3.2 Referências 📖

* Conceitos básicos de análise complexa
* Definições de zeros e polos em funções complexas
* Funções potenciais e números de Mersenne

### 3.3 Testes e validações 🧪

O script foi testado para n entre 0 e 10, confirmando que o valor do cálculo integral bate com a contagem exata de zeros e polos dentro da curva.

---

## 4. Contato 📬

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota 📝

* **Zero**: ponto onde a função se anula, ou seja, seu valor é exatamente zero.
* **Polo**: ponto onde a função cresce para valores muito grandes, próximos do infinito.
* **Integral**: soma contínua que calcula área ou variação ao longo de uma curva.
* **Plano complexo**: espaço onde os números têm uma parte real e uma parte imaginária (usando 'i' para a raiz de -1).
* **Função derivada**: medida de como a função muda em relação a mudanças pequenas na entrada.
