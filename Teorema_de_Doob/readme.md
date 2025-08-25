# Demonstração do Teorema de Doob com Martingales 🎲📈

## Sobre o Teorema de Doob 🧠

O **Teorema de Doob** é um resultado fundamental em teoria das probabilidades, especialmente em martingales.
Ele afirma que, para um martingale, o valor esperado futuro condicionado à informação presente é exatamente o valor presente.
Em outras palavras: **a melhor previsão do futuro, dado o que sabemos hoje, é justamente o que temos agora!** 🔮

---

## O que este script faz? 📝

* Simula **500** trajetórias independentes de um martingale simples, onde cada passo é +1 ou -1 aleatoriamente.
* Calcula o valor do martingale num tempo presente `t` e num tempo futuro `T > t`.
* Agrupa as trajetórias por valores próximos do martingale no tempo `t` e calcula a média condicional do valor no tempo `T`.
* Mostra que essa média condicional é muito próxima do valor presente — confirmando a essência do Teorema de Doob na prática! 🎯

---

## Como usar? ⚙️

1. Certifique-se que tem Python 3 e a biblioteca `numpy` instalada:

   ```bash
   pip install numpy
   ```
2. Execute o script:

   ```bash
   python seu_script.py
   ```
3. Veja no terminal os valores agrupados e a diferença entre a média condicional do futuro e o valor atual.

---

## Parâmetros ajustáveis 🛠️

| Parâmetro | Descrição                       | Valor padrão |
| --------- | ------------------------------- | ------------ |
| `N`       | Número de passos do martingale  | 1000         |
| `M`       | Número de trajetórias simuladas | 500          |
| `t`       | Tempo presente                  | 500          |
| `T`       | Tempo futuro (deve ser > `t`)   | 700          |

Você pode alterar esses valores direto no script para testar diferentes cenários.

---

## Exemplo da saída 🖥️

```
   Bin Mt    Média Mt    Média MT  Diferença
------------------------------------------
       1        1.02        1.01     0.0070
       2        2.05        2.03     0.0180
       3        3.00        3.01     0.0100
...

Observação:
A média de MT condicional ao valor de Mt é aproximadamente igual a Mt,
demonstrando a propriedade do martingale prevista pelo Teorema de Doob.
```

---

## Referências 📚

* Doob, J.L. (1953). *Stochastic Processes*.
* Williams, D. (1991). *Probability with Martingales*.
 

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
