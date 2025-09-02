# Estimador Church-Turing

Este projeto é um pequeno experimento computacional que utiliza conceitos do **Teorema de Church–Turing** para estimar a quantidade de processos computáveis possíveis entre potências de 2 crescentes. O script `estimador_church_turing.py` gera uma tabela com três colunas principais:

- `Início (2^N)` — início do intervalo computacional
- `Fim (2^(N+1)-1)` — fim do intervalo computacional
- `Estimado (Teorema)` — estimativa baseada em propriedades do Teorema de Church–Turing

---

## 📘 Sobre o Teorema de Church–Turing

O **Teorema de Church–Turing** afirma que qualquer função que é intuitivamente computável pode ser calculada por uma máquina de Turing. Ou seja, **qualquer algoritmo que possa ser descrito logicamente pode ser simulado por uma máquina de Turing**.

Esse teorema unifica diversos modelos formais de computação — como o cálculo lambda de Church, funções recursivas de Gödel e máquinas de Turing de Turing — mostrando que todos são equivalentes em termos de poder computacional.

---

## 💡 O que o script faz?

O script calcula, para cada valor de `N`, os seguintes valores:

- `Início`: \( 2^N \)
- `Fim`: \( 2^{N+1} - 1 \)
- `Estimado`: Uma estimativa do número de computações possíveis no intervalo entre `2^N` e `2^{N+1} - 1`, usando uma função de crescimento controlada que respeita o limite superior (`fim`).

Essa estimativa **não assume que todas as possibilidades no intervalo são computações válidas**, refletindo a realidade de que:

> Nem toda configuração binária representa um programa válido ou uma computação significativa.

Isso está de acordo com o Teorema de Church–Turing, pois:
- Apenas **programas efetivamente computáveis** são contados
- O crescimento de possibilidades **acompanha o aumento de recursos**, mas **não é puramente exponencial**

---

## 🧠 Justificativa teórica

Conforme aumentamos `N`, temos mais espaço binário (maior fita, mais bits, mais memória, etc.), o que permite representar um número maior de funções computáveis.

Porém, não todas as combinações possíveis entre `2^N` e `2^{N+1}-1` são válidas computações. A função estimadora no script busca aproximar esse subconjunto computável, que cresce de forma controlada — nem linear, nem puramente exponencial.

O script respeita os seguintes princípios:

- Crescimento contínuo com `N`, refletindo o aumento de capacidade computacional
- Limite superior no intervalo (`fim`)
- Estimativa mais realista do número de computações **concretas e executáveis**

---

## ▶️ Como usar

Execute o script com Python:

```bash
python estimador_church_turing.py
````

A saída será uma tabela com os valores estimados até `N = 9`. Você pode alterar esse limite diretamente no script (variável `n_max`).

---

## 📄 Exemplo de saída

```
N   | Início (2^N)   | Estimado (Teorema)   | Fim (2^(N+1)-1)
-----------------------------------------------------------------
0   | 1              | 1                    | 1
1   | 2              | 2                    | 3
2   | 4              | 5                    | 7
3   | 8              | 9                    | 15
4   | 16             | 21                   | 31
5   | 32             | 44                   | 63
6   | 64             | 85                   | 127
7   | 128            | 170                  | 255
8   | 256            | 340                  | 511
9   | 512            | 512                  | 1023
```

---

## 🧾 Licença

Este projeto é livre para uso acadêmico e educacional. Sinta-se à vontade para adaptar a função de estimativa para modelos mais precisos ou alternativos. 

--- 

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
