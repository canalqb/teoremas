# 🔥 Entenda os Números de Carmichael e como identificá-los em Python!

Você já ouviu falar dos **números de Carmichael**? Eles são um caso muito curioso na teoria dos números e têm uma relação especial com o **Pequeno Teorema de Fermat**.

---

## O que são números de Carmichael? 🤔

Os números de Carmichael são números compostos que, curiosamente, **passam no teste de primalidade de Fermat para *qualquer* base coprima a eles**. Em outras palavras, eles enganam o teste de Fermat e parecem ser primos mesmo não sendo.

### Por que isso importa?

O **Pequeno Teorema de Fermat** diz que, se p é primo e a é um inteiro coprimo a p, então:

a^(p−1) ≡ 1 (mod p)

Este é um teste rápido para verificar primalidade, mas números de Carmichael são exceções que satisfazem essa congruência para *todos* os $a$ coprimos, mesmo sendo compostos! Por isso, também são chamados de **“pseudo-primos de Fermat universais”**.

---

## Como identificar números de Carmichael? 📋

Um número $n$ é número de Carmichael se:

1. $n$ é composto (não primo).
2. $n$ é **quadrado livre** (não tem fatores primos repetidos).
3. Para todo primo divisor p de 𝑛 n, 𝑝 − 1 p−1 divide 𝑛 − 1 n−1.

Essa última condição é conhecida como **condição de Korselt**, que caracteriza os números de Carmichael.

---

## O script Python para verificar Carmichael 🚀

Calcular se um número é Carmichael diretamente pode ser muito pesado para números grandes. Para resolver isso, usamos uma **lista pré-calculada de números de Carmichael conhecidos** e fazemos buscas rápidas.

### O que o script faz:

* Recebe uma lista de números “procurados”.
* Verifica se cada um está na lista de Carmichael.
* Para cada número, retorna:

  * Se é Carmichael ou não.
  * O número de Carmichael mais próximo anterior a ele.
  * O número de Carmichael mais próximo posterior a ele.

### Trecho principal do código (simplificado) Números_de_Carmichael.py:

```python
import bisect

carmichaels = [561, 1105, 1729, 2465, 2821, ...]  # lista conhecida

def eh_carmichael(n):
    return n in carmichaels

def busca_anterior(valor):
    pos = bisect.bisect_left(carmichaels, valor)
    return carmichaels[pos-1] if pos > 0 else None

def busca_posterior(valor):
    pos = bisect.bisect_right(carmichaels, valor)
    return carmichaels[pos] if pos < len(carmichaels) else None

# Para cada valor procurado, printa os resultados
for valor in procurados:
    print(f"Valor: {valor}")
    print(f" → Carmichael? {'Sim' if eh_carmichael(valor) else 'Não'}")
    print(f" → Carmichael anterior: {busca_anterior(valor)}")
    print(f" → Carmichael posterior: {busca_posterior(valor)}")
    print("—" * 30)
```

---

## Por que usar essa lista conhecida?

Testar diretamente a definição de Carmichael é computacionalmente caro para valores grandes, pois envolve verificar propriedades para múltiplos divisores e múltiplas bases. A lista pré-calculada oferece uma solução rápida e prática para análise e estudos.

---

## Curiosidade final 🎉

O menor número de Carmichael é **561**, que é produto de três primos distintos: 3 * 11 * 17. É um número “camaleão” no mundo dos primos!


---

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com 
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
