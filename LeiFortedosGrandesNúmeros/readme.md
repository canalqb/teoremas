# 📊 Lei Forte dos Grandes Números (Kolmogorov) - Simulação Interativa

---

## 🔍 O que é a Lei Forte dos Grandes Números?

A **Lei Forte dos Grandes Números (LFGN)** é um dos resultados mais fundamentais da teoria das probabilidades. Ela garante que, para uma sequência de variáveis aleatórias independentes e identicamente distribuídas (i.i.d.), a média das observações se aproxima **quase certamente** do valor esperado verdadeiro conforme o número de amostras cresce.

> ✳️ *"Quase certamente"* significa que a probabilidade da média **não** convergir para o valor esperado é zero — é uma forma extremamente forte de convergência.

---

## 🧠 Versão de Kolmogorov

Kolmogorov estendeu a LFGN para cobrir casos mais gerais, como sequências de variáveis **independentes, mas não necessariamente identicamente distribuídas**, contanto que satisfaçam certas condições sobre variância e crescimento.

---

## 📈 O que faz este projeto?

Este projeto contém um script Python que simula a **convergência da média amostral para a média verdadeira** usando a Lei Forte dos Grandes Números.

### 💡 Como o experimento foi pensado?

A simulação verifica a média amostral em pontos estratégicos:

- Potências de 2: \(2^A\)
- Números de Mersenne: \(2^{A+1} - 1\)

Esses pontos são usados frequentemente em provas matemáticas para controlar o comportamento da sequência de médias, pois permitem estimar o desvio da média com base em janelas de crescimento exponencial.

---

## 🧾 O que é exibido?

- Uma **tabela** mostrando as médias amostrais nos pontos \(2^A\) e nos correspondentes números de Mersenne.
- Um **gráfico** que ilustra como essas médias se aproximam da média verdadeira \(\mu\), conforme mais dados são considerados.

---

## 🚀 Objetivo

Demonstrar visual e numericamente a veracidade da **Lei Forte dos Grandes Números**, mesmo analisando a sequência em pontos discretos, como potências de 2 e Mersenne — uma abordagem inspirada nas ideias da própria prova de Kolmogorov.

---

## 📦 Requisitos

- Python 3.x
- Bibliotecas: `numpy`, `pandas`, `matplotlib`

> Basta rodar o script e observar a saída no terminal e no gráfico interativo!

---

## 📚 Aprendizado

Com este projeto, você poderá:

- Visualizar a **convergência quase certa** de médias amostrais;
- Entender o papel de potências de 2 e números de Mersenne em provas de teoremas;
- Explorar conceitos fundamentais de probabilidade com intuição e código.

---

*Feito com 📐 + 💻 para quem curte matemática aplicada.*  


---  

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
