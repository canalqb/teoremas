# 🧠 **Teorema Fraco de Goldbach com Tabela de Intervalos**

Este projeto aplica o **Teorema Fraco de Goldbach** para validar uma série de valores definidos dentro de uma tabela construída a partir de potências de 2 e números de Mersenne.

---

## 📚 **O que é o Teorema Fraco de Goldbach?**

> *Todo número ímpar maior que 5 pode ser escrito como a soma de três números primos.*

Este é um dos resultados mais elegantes da *teoria dos números*, proposto por **Christian Goldbach** no século XVIII e finalmente **provado por Harald Helfgott em 2013**.

Diferente do Teorema Forte (ainda não provado), o Teorema Fraco foi demonstrado com sucesso utilizando ferramentas da análise matemática moderna.

---

## 📊 **A Tabela de Intervalos**

Este projeto usa a seguinte tabela:

| **Início** | **Meio** | **Fim** |
| ---------: | -------- | ------: |
|          1 | 1        |       1 |
|          2 | 3        |       3 |
|          4 | 7        |       7 |
|          8 | 8        |      15 |
|         16 | 21       |      31 |
|         32 | 49       |      63 |
|         64 | 76       |     127 |
|        128 | 224      |     255 |
|        256 | 467      |     511 |
|        512 | 514      |    1023 |
|       1024 | 1155     |    2047 |
|       2048 | 2683     |    4095 |

* A coluna **Fim** segue a fórmula:
  📐 *Fim = 2 × Início - 1*
  que produz exatamente os **números de Mersenne**.
* A coluna **Meio** representa valores ímpares entre *Início* e *Fim*, os quais serão testados pelo Teorema Fraco de Goldbach.

---

## 🧪 **O que o script faz?**

O script `goldbach_weak.py` executa os seguintes passos:

1. Lê cada linha da tabela.
2. Verifica se o valor da coluna **Meio** pode ser expresso como a **soma de três números primos**.
3. Exibe o resultado da verificação, detalhando a decomposição (quando encontrada).

---

## 🔍 **Exemplo de Saída**

```bash
Início: 16, Meio: 21, Fim: 31
✅ 21 = 2 + 2 + 17
```

---

## ⚙️ **Como executar**

Você precisa ter Python 3 instalado.

1. Instale a dependência:

```bash
pip install sympy
```

2. Execute o script:

```bash
python goldbach_weak.py
```

---

## 🧠 **Justificativa Matemática**

O script valida que cada um dos valores do meio e pode ser escrito como a soma de **três números primos** ou não.

📌 Além disso, a estrutura da tabela faz referência a potências de 2, com o **Fim** sempre sendo um **número de Mersenne** (forma `2ⁿ - 1`), criando um contexto binário-matemático interessante.

---

## 🧩 **Relação entre os Conceitos**

* **Teorema Fraco de Goldbach** → Testa se um número ímpar pode ser somado por 3 primos.
* **Potências de 2** → Estruturam os limites inferiores da tabela.
* **Números de Mersenne** → São os limites superiores (*Fim = 2 × Início - 1*).
* **Coluna "Meio"** → Serve como o valor a ser testado, dentro do intervalo \[Início, Fim].

---

## ✅ **Conclusão**

Este projeto une:

* 🧠 *Teoria clássica dos números*
* ⚙️ *Programação em Python*
* 🔢 *Números primos e de Mersenne*

para validar propriedades matemáticas reais de maneira computacional.

---

💡 *Explore a beleza dos números e da lógica com uma pitada de código!*

---

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
