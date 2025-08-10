# 🔍 Entendendo o Teorema de Euler-Fermat e seu uso prático

O **Teorema de Euler-Fermat** é uma pedra fundamental da *teoria dos números* e uma poderosa generalização do Pequeno Teorema de Fermat. 📚

Ele diz o seguinte: para dois números inteiros positivos **a** e **n**, onde **a** é *coprimo* com **n** (ou seja, o máximo divisor comum entre eles é 1), vale esta propriedade importante:

> **a elevado a phi(n), módulo n, é igual a 1**

Aqui, **phi(n)** é a função *totiente de Euler*, que conta quantos números entre 1 e n são coprimos com n.

Matematicamente:

**a^phi(n) mod n = 1**

---

## 💡 O que são *coprimos* e *totiente*?

* **Números coprimos** são dois números inteiros que não compartilham nenhum divisor maior que 1.
  Exemplo: 8 e 15 são coprimos porque os divisores comuns são apenas 1. Já 8 e 12 não são, porque ambos são divisíveis por 2 e 4.

* A função **totiente de Euler**, escrita como **phi(n)**, é a quantidade de números positivos até n que são coprimos com n.
  Por exemplo:

  * phi(8) = 4, pois os números coprimos com 8 entre 1 e 8 são 1, 3, 5 e 7
  * phi(7) = 6, porque 7 é primo, e todos os números de 1 até 6 são coprimos com 7

---

## 🖥️ Sobre o script que criamos

Nosso script percorre vários intervalos de números e, para cada número procurado, verifica:

* Se ele é primo ou não
* Calcula o valor do totiente phi(n)
* Testa a propriedade de Euler-Fermat usando a base 2

Exemplo do que o script imprime:

* **Número:** 49
* **Primo?** Não
* **Totiente φ(49):** 42
* **Verificação:** 2^42 mod 49 == 1? **Sim** (ou seja, passa no teste)

---

## 🔎 Resultados interessantes que vimos

* **Primos verdadeiros**, como 3, 7 e 467, passam no teste com facilidade ✅
* Alguns **compostos "pseudoprimos"**, como 21 e 49, também passam no teste para base 2 — eles são números que "enganam" esse teste ⚠️
* Outros compostos, como 8, 76 e 224, falham no teste, confirmando que não são primos ❌

---

## 🎯 Conclusão

O Teorema de Euler-Fermat é um excelente ponto de partida para testes rápidos de primalidade e para entender propriedades dos números inteiros. Porém, ele sozinho não garante que um número que passe no teste seja primo, pois existem os pseudoprimos.

Para testes mais confiáveis, podemos usar múltiplas bases ou métodos avançados, como o teste de Miller-Rabin.

---

Quer que eu te ajude a criar um script mais completo para explorar tudo isso? 🚀

--- 

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com 
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
