## Post Resumo: Números Coprimos e Totiente de Euler

**Números coprimos** são dois números que têm como único divisor comum o número 1. Por exemplo, 8 e 15 são coprimos, porque nenhum outro número além do 1 divide ambos.

---

### O que é o Totiente de Euler?

O **totiente de Euler**, denotado por phi(n), é uma função que conta quantos números entre 1 e n são coprimos com n. Ou seja:

phi(n) = quantidade de k com 1 <= k <= n e mdc(k, n) = 1

---

### Exemplo:

* phi(8) = 4 porque os números coprimos com 8 entre 1 e 8 são 1, 3, 5, 7.

---

### O script

O script abaixo calcula phi(n) para os valores da tabela, onde:

* **Início** são potências de 2;
* **Fim** são números da forma $2^m - 1$ (números de Mersenne);
* **Procurado** são valores da tabela que queremos relacionar.

```python
from math import gcd 

def phi(n):
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1
    return result

inicio = [1, 2, 4, 8, 16, 32, 64, 128, 256]
procurado = [1, 3, 7, 8, 21, 49, 76, 224, 467]
fim = [1, 3, 7, 15, 31, 63, 127, 255, 511]

print("Início | Procurado | Fim | Totiente(phi(Fim))")
for i, f in enumerate(fim):
    if f == 1:
        phi_val = 1
    else:
        phi_val = phi(f)
    print(f"{inicio[i]:6} | {procurado[i]:8} | {fim[i]:3} | {phi_val:18}")
```

---

### Saída do script

```
Início | Procurado | Fim | Totiente(phi(Fim))
     1 |        1 |   1 |                  1
     2 |        3 |   3 |                  2
     4 |        7 |   7 |                  6
     8 |        8 |  15 |                  8
    16 |       21 |  31 |                 30
    32 |       49 |  63 |                 36
    64 |       76 | 127 |                126
   128 |      224 | 255 |                128
   256 |      467 | 511 |                432
```

---

### Conclusão

* A função totiente nos ajuda a entender propriedades dos números, especialmente em criptografia e teoria dos números.
* Essa tabela relaciona potências de 2, números de Mersenne e valores próximos ao totiente de Euler, mostrando a importância dos números coprimos para análise dos ciclos e grupos multiplicativos.

Se quiser, posso ajudar a criar um post visual ou explicações mais detalhadas! Quer?

--- 

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com 
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
