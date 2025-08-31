# **README - Estimativa de Entropia com base no Teorema de Kolmogorov–Sinai**

✨ **Bem-vindo a este projeto incrível!** Aqui você vai aprender a estimar a entropia de uma sequência binária aleatória usando o poderoso *Teorema de Kolmogorov–Sinai* — uma ferramenta fundamental da teoria da informação e ergódica. Vamos nessa? 🚀

---

## **SOBRE A TEORIA**

O *Teorema de Kolmogorov–Sinai* (ou entropia KS) é um conceito fascinante da *teoria ergódica* que conecta o comportamento caótico dos sistemas dinâmicos com a geração de informação.

*Em termos simples:*
✨ **A entropia métrica mede a quantidade máxima de informação (aleatoriedade) produzida por um sistema ao longo do tempo.**

Aplicando à análise de sequências binárias:

* Estimamos a entropia observando o crescimento da entropia em **blocos de tamanho k**.
* A taxa de entropia por bit é dada por:

  *h = lim (k → ∞) Hₖ / k*

  Onde **Hₖ** é a entropia dos blocos de k bits.

Se a sequência for realmente aleatória, esperamos que *Hₖ / k* se aproxime de **1.0** — ou seja, **entropia máxima por bit**! 🎉

---

## **SOBRE O SCRIPT**

Este script Python (`entropia_ks.py`) é um verdadeiro aliado para medir a aleatoriedade da sua fonte de bits!

Ele faz o seguinte:

1. Gera uma sequência binária longa e segura com o módulo `secrets` 🔐 — que produz números aleatórios criptograficamente seguros.
2. Para cada bloco de tamanho **k** (de 1 até um valor máximo que você escolher), divide a sequência em blocos.
3. Conta a frequência de cada bloco para calcular a **entropia de Shannon** (Hₖ).
4. Calcula a **entropia por bit** dividindo Hₖ por k.
5. Mostra uma tabela clara e organizada com os resultados — perfeita para analisar a qualidade da aleatoriedade! 📊

---

## **EXEMPLO DE SAÍDA**

Veja como fica a saída do script para uma sequência idealmente aleatória:

```
📊 Análise de Entropia com base em Kolmogorov–Sinai  
Total de bits gerados: 100000  
Fonte: secrets.token_bytes  

 k | Blocos únicos | Total blocos | H_k (bits) | H_k / k  
---|----------------|---------------|-------------|--------  
 1 |              2 |        100000 |     1.000000 | 1.0000  
 2 |              4 |         50000 |     2.000000 | 1.0000  
 3 |              8 |         33333 |     3.000000 | 1.0000  
 4 |             16 |         25000 |     4.000000 | 1.0000  
```

*Na prática*, quanto mais próximo de **1.0** estiver *Hₖ / k*, mais aleatória e imprevisível é sua fonte! 🥳 Caso contrário, pode haver padrões ou redundâncias.

---

## **O QUE VOCÊ VAI APRENDER COM ESTE PROJETO**

* Como aplicar a teoria ergódica para analisar dados reais 🔍
* A relação entre **entropia empírica** e a qualidade da aleatoriedade
* Uso prático do Python para análise estatística e teoria da informação 🐍
* Avaliar se seu gerador de números aleatórios é confiável ou não 💡

---

## **REQUISITOS**

* Python 3.7 ou superior 🐍
* Sem dependências externas — apenas módulos padrão (`secrets`, `math`, `collections`)

---

## **COMO EXECUTAR**

1. Salve o arquivo `entropia_ks.py`.
2. No terminal, execute:

```
python entropia_ks.py
```

3. Quer testar com mais bits ou blocos maiores? Modifique o final do script:

```python
estimar_entropia_ks(n_bits=100_000, k_max=16)
```

---

## **ESTRUTURA DO PROJETO**

* `entropia_ks.py` — script principal de análise 🔧
* `README.md` — esta documentação 📚

---

## **REFERÊNCIAS INSPIRADORAS**

* A.N. Kolmogorov — Entropy per Unit Time as a Metric Invariant of Automorphisms
* C.E. Shannon — A Mathematical Theory of Communication
* Cover & Thomas — Elements of Information Theory

---

## **LICENÇA**

Este projeto é **open source** sob a licença **MIT**. Sinta-se livre para usar, modificar e compartilhar! ❤️

--- 
  
## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
