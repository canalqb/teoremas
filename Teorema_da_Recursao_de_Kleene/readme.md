# Kleene Fixed Point Simulation

Este repositório apresenta uma simulação baseada no **Teorema da Recursão de Kleene**, um conceito fundamental da teoria da computação, utilizando um script Python que estima, para diferentes valores de `N`, quantos "programas" (representados por números naturais) satisfazem condições inspiradas na autorreferência proposta pelo teorema.

---

## 🧠 O que é o Teorema da Recursão de Kleene?

O **Teorema da Recursão de Kleene** (também conhecido como **Teorema do Ponto Fixo de Kleene**) afirma que:

> Para toda função total computável \( f \), existe um índice \( e \) tal que:
> \[
\varphi_e = \varphi_{f(e)}
\]
Ou seja, existe um programa (representado por \( e \)) que, ao ser executado, tem o mesmo comportamento do programa gerado por aplicar \( f \) sobre ele mesmo.

Este resultado é um dos pilares da computabilidade e demonstra que é possível construir **programas autorreferentes**, ou seja, que acessam ou manipulam seu próprio código — conceito fundamental para:

- Metaprogramação
- Quines (programas que imprimem seu próprio código)
- Autocompiladores
- Análise estática de código
- Autorreferência lógica e matemática
- Fundamentos teóricos de vírus de computador

---

## 📈 Justificativa do Script

Inspirado nesse teorema, o script `kleene_count_simulation.py` simula o comportamento de autorreferência computacional ao estimar quantos "programas", em cada intervalo `[2^N, 2^(N+1) - 1]`, satisfazem uma condição que aproxima um ponto fixo computável.

Como não é viável identificar pontos fixos reais em uma enumeração abstrata de programas, o script utiliza uma **heurística baseada na estrutura binária do índice** para estimar a frequência de "pontos fixos simulados".

A lógica é a seguinte:

- Cada número natural representa um possível programa.
- Para cada intervalo entre `2^N` e `2^(N+1)-1`, é aplicado um critério de autorreferência computável.
- Se um número \( i \) for divisível pelo tamanho de sua representação binária (ou uma função correlata), ele é considerado como satisfazendo uma "condição de ponto fixo".

Essa abordagem produz uma contagem crescente com o tamanho do intervalo, refletindo o crescimento do número de possíveis programas autorreferentes conforme o espaço aumenta — exatamente o tipo de tendência sugerida pelo teorema de Kleene.

---

## 🔢 Estrutura da Simulação

A saída do script apresenta a seguinte tabela:

| N | Início (2^N) | Estimativa de Pontos Fixos | Fim (2^(N+1) - 1) |
|---|--------------|-----------------------------|-------------------|
| 0 | 1            | 1                           | 2                 |
| 1 | 2            | 1                           | 4                 |
| 2 | 4            | 2                           | 8                 |
| 3 | 8            | 2                           | 16                |
| 4 | 16           | 4                           | 32                |
| ... | ...        | ...                         | ...               |

Esta tabela ilustra a ideia de que, à medida que o número de possíveis programas cresce, também cresce a quantidade de programas que satisfazem uma condição autorreferente — alinhando-se ao espírito do Teorema da Recursão de Kleene.

---

## 📜 Conclusão

Este projeto não tenta provar o teorema, mas sim **visualizar sua implicação prática**: o crescimento do número de programas autorreferentes em espaços de codificação maiores. Ao usar uma heurística simples e computável, aproximamos esse crescimento para diferentes potências de 2.

A simulação mostra como conceitos profundos da teoria da computação podem ser explorados computacionalmente, mesmo sem recorrer a máquinas universais ou lógica formal completa.

---

--- 

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
