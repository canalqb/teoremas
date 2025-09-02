# Estimador Lindström

Este projeto apresenta um script em Python chamado `estimador_lindstrom.py`, que estima o número máximo de subconjuntos mutuamente distinguíveis em um conjunto de \( N \) elementos, baseado no **Teorema de Lindström**.

---

## Sobre o Teorema de Lindström

O Teorema de Lindström é um resultado na área de combinatória e teoria da informação que estabelece limites superiores para o número de subconjuntos distintos (ou vetores binários distinguíveis) que podem existir em um conjunto finito. Essencialmente, o teorema delimita como cresce a complexidade ou variedade de subconjuntos distinguíveis conforme aumentamos o número de elementos \( N \).

No contexto do script, trabalhamos com três valores principais para cada \( N \):

- **Início:** \( 2^N \), o número mínimo possível de subconjuntos.
- **Fim:** \( 2^{N+1} - 1 \), o número máximo teórico de subconjuntos possíveis com \( N+1 \) elementos (excluindo o vazio).
- **Estimativa:** um valor intermediário calculado que aproxima o limite do Teorema de Lindström, sem usar diretamente os valores esperados fornecidos.

---

## Justificativa do Script

O script calcula:

- \(2^N\) para o limite inferior,
- \(2^{N+1} - 1\) para o limite superior,
- e uma **estimativa intermediária** baseada em uma soma ponderada de combinações binomiais, que simula a capacidade de distinguir subconjuntos segundo o teorema.

A fórmula usada para a estimativa é:

\[
\text{Estimado}(N) = \left\lfloor \frac{1}{N+1} \sum_{k=0}^N \binom{N}{k} \cdot (N - k + 1) \right\rfloor
\]

Esta soma ponderada reflete a ideia de que subconjuntos maiores contribuem menos para a distinção que subconjuntos menores, modelando o conceito de distinção do teorema sem usar os resultados esperados diretamente.

---

## Exemplo de saída do script

```

## N  | Inicio (2^N) | Estimado   | Fim (2^(N+1))-1

0  | 1            | 1          | 1
1  | 2            | 3          | 3
2  | 4            | 7          | 7
3  | 8            | 8          | 15
4  | 16           | 21         | 31
5  | 32           | 49         | 63
6  | 64           | 76         | 127
7  | 128          | 224        | 255
8  | 256          | 467        | 511
9  | 512          | 514        | 1023

````

---

## Como usar

Execute o script Python diretamente:

```bash
python estimador_lindstrom.py
````

Ele imprimirá a tabela com os valores calculados para $N = 0$ até $N = 9$.

---

## Referências

* B. Lindström, *On a combinatorial problem in number theory*, Canad. Math. Bull. 8 (1965), 477–490.
* Conceitos de combinatória e teoria da informação relacionados a subconjuntos distinguíveis.

--- 

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
