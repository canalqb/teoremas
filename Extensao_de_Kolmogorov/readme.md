# 📐 Teorema de Extensão de Kolmogorov

## ✨ Sobre o Teorema

O **Teorema de Extensão de Kolmogorov** é uma das pedras fundamentais da *teoria das probabilidades modernas*. Ele garante que, a partir de um conjunto de **distribuições marginais finito-dimensionais consistentes**, é possível construir um **processo estocástico completo**.

Em termos simples:

> Se temos todas as *pequenas peças* (isto é, distribuições conjuntas para subconjuntos finitos de variáveis aleatórias) e essas peças se encaixam perfeitamente, então podemos formar o *quebra-cabeça inteiro*: um processo \( X_t \) definido para todos os tempos \( t \).

Esse resultado é essencial na construção de objetos como o **movimento Browniano**, **ruídos gaussianos**, ou **processos temporais contínuos**.

---

## 🧪 O Script: `Extensao_de_Kolmogorov.py`

Este projeto implementa um experimento baseado no teorema.

- Para cada valor de \( n \) de 0 até 8, criamos intervalos do tipo:  
  \[
  [2^n, \ 2^{n+1} - 1]
  \]
  Esses intervalos correspondem aos domínios das distribuições marginais.

- Em cada intervalo, um ponto intermediário é selecionado como a **"procura pelo teorema"** – ele representa simbolicamente o local onde a *consistência marginal* é verificada.

- Para cada conjunto de índices, o script simula **variáveis gaussianas independentes**, representando marginais finito-dimensionais.

---

## 🔗 Relação entre Teorema e Código

O que *une* o teorema e o script é o seguinte:

- O **teorema garante a existência** de um processo global, desde que os *blocos marginais* estejam bem definidos e sejam compatíveis entre si.
- O **script simula** esses blocos, estrutura os intervalos de forma hierárquica (baseados em potências de 2) e permite observar **como os pedaços de um processo podem ser costurados**.

🧩 Cada linha da saída representa um **subconjunto finito** de índices no tempo, com o qual uma marginal gaussiana é associada.  
🧵 O ponto “procura pelo teorema” é a *linha de costura* simbólica entre as peças. Ele não prova o teorema, mas fornece uma *intuição poderosa* de como ele funciona.

---

## 📈 Exemplo de Saída

```plaintext
 n  Início  Procura pelo teorema  Fim  Tamanho do intervalo
 0       1                     1    1                     1
 1       2                     3    3                     2
 2       4                     6    7                     4
 3       8                    12   15                     8
 4      16                    24   31                    16
 5      32                    48   63                    32
 6      64                    96  127                    64
 7     128                   192  255                   128
 8     256                   384  511                   256
```
---
🚀 Experimente!
Você pode executar o script para gerar seus próprios blocos marginais e observar como o número de variáveis e o ponto de "procura" crescem conforme 
𝑛
n aumenta.

Esse é um ótimo exercício para estudantes e entusiastas da matemática aplicada, que desejam entender na prática como funciona a base da teoria dos processos estocásticos.

📚 Referência
Kolmogorov, A.N. (1933). Foundations of the Theory of Probability.
Este teorema é apresentado como parte da formulação axiomática da probabilidade.

---

  
## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
