## 🧮 **Teorema Fundamental da Aritmética**

### ✨ *A essência dos números inteiros!*

O **Teorema Fundamental da Aritmética** afirma que:

> 📌 *Todo número inteiro maior que 1 pode ser escrito de forma única como um produto de números primos, desconsiderando a ordem dos fatores.*

Ou seja, não importa como você chegue até a fatoração — o resultado *sempre* será o mesmo em termos de primos e seus expoentes. 🌟

---

## 🔍 **Explorando na prática com Python!**

O script `teorema_fundamental_da_aritmetica.py` nos mostra como esse teorema funciona na prática. Ele percorre *intervalos de números crescentes* e exibe a **fatoração em primos** de cada um deles. 🧠💻

### 📂 Como funciona o script?

```python
from sympy import factorint
```

🔧 Usamos a biblioteca `sympy`, que tem uma função poderosa chamada `factorint()` — ela retorna os fatores primos de um número, juntamente com seus expoentes.

---

### 🧭 O que o script faz?

1. 🔢 Divide os números em **intervalos** baseados em potências de 2:
   Exemplo: \[1,1], \[2,3], \[4,7], \[8,15], \[16,31]

2. 🧠 Para cada número `n` no intervalo:

   * Calcula sua fatoração prima
   * Exibe o resultado no formato:

     ```bash
     número = fator1 * fator2^expoente * ...
     ```

3. 🌟 **Destaques visuais**:
   Alguns números definidos em `destaques = {1, 3, 7, 8, 21, 49, 76}` são impressos com mais ênfase:

   ```bash
   >>>>> 3 = 3 <<<<<
   ```

---

## 🧾 **Exemplo de saída (resumo):**

```bash
Intervalo [2, 3]:
------------------------------
2 = 2
>>>>> 3 = 3 <<<<<
```

```bash
Intervalo [8, 15]:
------------------------------
>>>>> 8 = 2^3 <<<<<
9 = 3^2
...
```

```bash
Intervalo [16, 31]:
------------------------------
...
>>>>> 21 = 3 * 7 <<<<<
...
```

---

## 🧠 **Por que isso é importante?**

✨ A fatoração em primos é a *base de toda a aritmética*.
É usada em:

* Criptografia 🔐
* Algoritmos de computador 🖥️
* Teoria dos números 📘
* Resolução de problemas matemáticos 🧩

O script é uma ferramenta didática que ajuda a **visualizar o poder e a universalidade dos números primos**! 🚀

---

## ✅ **Resumo final**

**Teorema Fundamental da Aritmética** = *A identidade única de cada número*
**Script em Python** = *Visualização prática e interativa dessa identidade*

🔁 E não importa o número, se ele for maior que 1...
➡️ **Ele tem uma assinatura única feita de primos!**

---

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com 
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
