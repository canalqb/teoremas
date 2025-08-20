# 🧠 Teorema de Goldbach-Levy & Script

## ✨ Sobre o Teorema de Goldbach-Levy

O **Teorema de Goldbach-Levy** é uma curiosidade matemática fascinante que diz o seguinte:

> **Todo número ímpar maior que 5 pode ser escrito como a soma de um número primo e dois números primos distintos (ou iguais).**

Este teorema é uma variação do famoso **Teorema Fraco de Goldbach**, que já sugere que **todo número ímpar maior que 7 é a soma de três primos**. No caso do Teorema de Levy, a ideia é explorar essa decomposição **usando números de Mersenne** — que são números da forma:

```
Mₙ = 2ⁿ - 1
```

Os primeiros números de Mersenne são: `1, 3, 7, 15, 31, 63, 127, ...`
Eles possuem propriedades especiais e aparecem em diversas áreas da matemática, como criptografia, teoria dos números e computação.

---

## 🧾 Sobre o Script

Este script tem como objetivo **verificar e ilustrar uma decomposição de números em somas de números de Mersenne**, com base numa tabela fornecida.

### 📌 O que o script faz:

1. **Valida uma tabela de intervalos** (`tabela`) contendo tuplas `(inicio, meio, fim)` e verifica se:

   * `fim == 2 * inicio - 1`
   * `meio` está dentro do intervalo `[inicio, fim]`
   * O número `meio` pode ser decomposto **em soma de números de Mersenne ≤ fim**

2. Utiliza uma função recursiva `pode_decompor()` que tenta encontrar uma soma de números de Mersenne para atingir o valor desejado (`meio` ou outros números do intervalo).

3. A função `decompor_intervalo()` imprime a decomposição de **todos os números entre `1` e `4095`**, mostrando se cada número pode ser formado por uma soma de Mersennes.

---

## ⚙️ Como usar

Basta rodar o script com Python:

```bash
python Levy.py
```

Você verá no terminal:

* A validação da tabela de intervalos
* A decomposição de todos os números de `1` a `4095` em somas de Mersennes

---

## 📚 Exemplo de saída:

```
Inicio: 16, Meio: 21, Fim: 31
Decomposição de 21 em soma de Mersennes <= 31: [15, 3, 3]
----------------------------------------
...
1023: [511, 255, 255, 1, 1]
```

---

## 🤔 Curiosidade

Você pode pensar neste script como uma forma alternativa de validar ideias relacionadas ao Teorema de Goldbach-Levy, **mas utilizando um conjunto muito especial de números primos** — os **Mersennes**!

---

## 🛠️ Estrutura do Código

* `pode_decompor(valor, mersennes)`
  -> Função recursiva que tenta decompor um número em soma de Mersennes.

* `validate_table(tabela)`
  -> Verifica a validade de cada linha da tabela e imprime a decomposição do "meio".

* `decompor_intervalo(inicio, fim)`
  -> Imprime a decomposição de todos os números entre `inicio` e `fim`.

---

## 🧠 Conclusão

Esse script é uma bela mistura de matemática pura com programação prática! Ele permite:

* Explorar propriedades dos números de Mersenne 🧮
* Investigar padrões numéricos 🧩
* Brincar com decomposições e curiosidades matemáticas 💡

---

Se quiser expandir, você pode adaptar o script para:

* Usar apenas **números de Mersenne primos**
* Testar outras variações do teorema
* Criar visualizações 📊

---

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
