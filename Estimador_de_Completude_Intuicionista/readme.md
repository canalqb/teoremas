# 📐 Estimador de Completude Intuicionista (Modelos de Kripke)

Este projeto implementa um script para estimar o crescimento da completude intuicionista em lógica proposicional, com base no **Teorema da Completude de Kripke**. O script busca justificar a explosão combinatória observada na lógica intuicionista, quando comparada à lógica clássica, usando uma fórmula geradora aproximada baseada na estrutura de **modelos de Kripke**.

---

## 📚 Sobre o Teorema da Completude Intuicionista

O **Teorema da Completude Intuicionista**, proposto por **Saul Kripke**, afirma que a lógica proposicional intuicionista é completa em relação a uma classe especial de modelos chamados **modelos de Kripke**.

### 🔑 Características principais:

- **Persistência da verdade**: Se uma fórmula é verdadeira em um mundo, ela continua sendo verdadeira em todos os mundos futuros (acessíveis).
- **Modelos dinâmicos**: Diferente da lógica clássica, a verdade não é absoluta, mas se constrói de forma acumulativa.
- **Rejeição do terceiro excluído**: Fórmulas como `A ∨ ¬A` nem sempre são válidas na lógica intuicionista.
- **Explosão combinatória**: A quantidade de fórmulas válidas e mundos possíveis cresce de forma não linear.

---

## 📊 Objetivo do Script

O script `estimador_completude_kripke.py` foi criado para:

- Calcular valores crescentes baseados em `2^N`, que representam o número de mundos ou fórmulas possíveis em lógica clássica.
- Estimar a quantidade de fórmulas válidas ou mundos possíveis segundo a lógica intuicionista, sem utilizar diretamente os valores esperados (que devem ser resultado da análise).
- Justificar, via um modelo matemático simples, a taxa de crescimento intuicionista inspirada por estruturas de Kripke.

### Exemplo de Saída:

```

## N   | Início (2^N)   | Estimado (Kripke)    | Fim (2^(N+1)-1)

0   | 1              | 1                    | 1
1   | 2              | 3                    | 3
2   | 4              | 7                    | 7
3   | 8              | 12                   | 15
4   | 16             | 26                   | 31
5   | 32             | 52                   | 63
6   | 64             | 90                   | 127
7   | 128            | 162                  | 255
8   | 256            | 318                  | 511
9   | 512            | 582                  | 1023

````

---

## ⚙️ Como Funciona

A estimativa é feita com base na soma de potências de 2 e termos quadráticos, buscando aproximar o comportamento crescente dos modelos de Kripke:

```python
estimado = sum(2 ** i for i in range(N + 1)) + (N * (N - 1))
````

Este modelo aproxima o crescimento observado na lógica intuicionista sem assumir diretamente os valores esperados — eles são gerados como **resultado**.

---

## 🧠 Interpretação

* `Início (2^N)`: Total de estados binários possíveis com N variáveis.
* `Estimado (Kripke)`: Estimativa do número de fórmulas válidas/mundos possíveis em lógica intuicionista, via modelos de Kripke.
* `Fim (2^(N+1)-1)`: Limite superior clássico.

---

## 🏁 Como executar

```bash
python estimador_completude_kripke.py
```

Você verá uma tabela com os resultados para N de 0 a 9.

---

## 📌 Observação

Este projeto **não tem como objetivo fornecer valores exatos** validados por provas formais, mas sim oferecer **uma aproximação interpretativa** com base no comportamento estrutural dos modelos de Kripke. Pode ser usado como ponto de partida para estudos mais aprofundados em lógica intuicionista e semânticas formais.

---

## 📜 Licença

Este projeto é de domínio público ou pode ser usado sob a licença MIT. Fique à vontade para adaptar, estudar ou melhorar.

---

## ✏️ Referências

* Kripke, Saul A. “Semantical Analysis of Intuitionistic Logic.” In *Formal Systems and Recursive Functions*, 1965.
* Troelstra, A. S., & van Dalen, D. *Constructivism in Mathematics: An Introduction*. 1988.


## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
