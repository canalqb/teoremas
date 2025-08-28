# 📊 Simulação da Complexidade de Kolmogorov

Este projeto é uma simulação educacional inspirada na **teoria da complexidade de Kolmogorov**, usando Python. Ele mostra como, à medida que o comprimento das strings binárias cresce, a maioria delas se torna **incompressível**, ou seja, **não pode ser gerada por um programa mais curto que a própria string**.

---

## 🚀 Objetivo

Demonstrar, com base em uma tabela simples, que:

- Existem menos programas curtos do que possíveis strings longas.
- Portanto, a maioria das strings **não pode ser comprimida**.
- Isso reflete o **teorema da incompressibilidade** da complexidade de Kolmogorov.

---

## 📌 Tabela Gerada

O script gera uma tabela com as seguintes colunas:

| Coluna            | Significado |
|-------------------|-------------|
| `2^A`             | Quantidade de programas possíveis com até `A` bits |
| `PROCURANDO`      | Número máximo de strings que podem ser geradas por esses programas |
| `2^(A+1)-1`       | Maior valor representável com `A+1` bits (limite do universo de strings) |
| `% Incompressíveis` | Porcentagem de strings que **não podem ser geradas** por programas ≤ A bits |

---

## 📂 Estrutura

- `kolmogorov_simulation.py` → Script principal que gera a tabela.
- `README.md` → Este arquivo.

---

## 🧠 Fundamentos Teóricos

A **complexidade de Kolmogorov** de uma string é o tamanho do menor programa (em uma linguagem fixa e universal) que gera aquela string.

Segundo o teorema da incompressibilidade:

> A maioria das strings binárias de tamanho \( n \) são **incompressíveis**, ou seja, sua complexidade \( K(x) \geq n \).

---

## 🐍 Como executar

1. Certifique-se de ter Python 3 instalado.
2. Clone este repositório ou copie o script.
3. Execute o script:
 
---  

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
