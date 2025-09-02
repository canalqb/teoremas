# Teorema de Mostowski e Crescimento Recursivo

## O que é o Teorema de Mostowski?

O **Teorema de Mostowski** é um resultado importante na lógica matemática, especialmente em teoria dos modelos e teoria dos ordinais. Ele trata da existência e unicidade de funções normais que definem pontos fixos transfinito — ou seja, a construção de ordinais fixos a partir de processos recursivos.

Em termos mais aplicáveis, o teorema pode ser interpretado para modelar o crescimento de estruturas matemáticas ou computacionais que se expandem recursivamente, como árvores binárias, fórmulas lógicas, ou sequências construídas por duplicação e acumulação.

---

## Para que serve este teorema no contexto do script?

Neste contexto, o teorema é usado para descrever o **crescimento exponencial e acumulativo de estruturas que se duplicam a cada nível**, algo típico em processos recursivos com ramificação binária.

A ideia fundamental é a seguinte recursão:

$$
M(0) = 1 \quad \text{(estrutura base)} \\
M(n+1) = 2 \times M(n) + 1
$$

Ou seja, a quantidade esperada de estruturas no nível $n+1$ é o dobro do que foi gerado no nível anterior, acrescido de uma unidade para representar uma nova camada ou nó.

---

## Justificativa do script `mostowski_growth_table.py`

O script implementa essa regra de crescimento para gerar uma tabela que mostra:

* O valor inicial $2^N$, que indica a base do crescimento exponencial.
* O valor esperado pelo teorema, calculado pela recorrência $M(n+1) = 2 M(n) + 1$.
* O valor máximo $2^{N+1} - 1$, que representa o limite superior natural da expansão (número total de nós em uma árvore binária completa).

Dessa forma, o script ilustra como a aplicação do Teorema de Mostowski permite prever o crescimento de estruturas recursivas e comparar esse crescimento com limites teóricos conhecidos.

---

## Exemplo de saída do script

```
N   | Inicio (2^N)     | Esperado pelo teorema      | Fim (2^(N+1))-1
----------------------------------------------------------------------
0   | 1                | 1                          | 1
1   | 2                | 3                          | 3
2   | 4                | 7                          | 7
3   | 8                | 15                         | 15
4   | 16               | 31                         | 31
5   | 32               | 63                         | 63
6   | 64               | 127                        | 127
7   | 128              | 255                        | 255
8   | 256              | 511                        | 511
9   | 512              | 1023                       | 1023
```

---

## Considerações finais

Este script é uma forma simples e didática de aplicar conceitos do Teorema de Mostowski para modelar crescimento recursivo. Ele pode ser útil em áreas como:

* Lógica matemática e teoria dos modelos.
* Análise de algoritmos recursivos.
* Estudo de árvores e estruturas de dados.
* Pesquisa em computabilidade e complexidade. 
--- 

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
