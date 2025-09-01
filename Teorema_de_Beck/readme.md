# 🧠 Teorema de Beck — Simulador em Python

Este repositório contém um simulador que gera uma tabela de valores baseada em uma variação empírica do chamado "Teorema de Beck", aplicada a uma estrutura binária crescente.

O objetivo é observar como um valor "esperado" evolui conforme o nível \( N \) aumenta, partindo de \( 2^N \) até \( 2^{(N+1)} - 1 \), comparando com um valor calculado por uma fórmula empírica baseada nos próprios dados.

---

## 📘 Sobre o Teorema (Adaptação)

O nome **Teorema de Beck**, neste projeto, é usado de forma **aplicada/experimental** para descrever um padrão de crescimento relacionado a estruturas binárias (como árvores completas ou grafos).

- Para cada nível \( N \), temos:
  - **Início**: \( 2^N \)
  - **Fim**: \( 2^{(N+1)} - 1 \)
  - **Esperado**: valor derivado empiricamente a partir de uma regra recursiva baseada no crescimento dos níveis anteriores.

---

## 📈 O que o script faz?

O script `teorema_beck_simulador.py` gera uma tabela com os seguintes dados:

| N | Início (\(2^N\)) | Esperado | Fim (\(2^{(N+1)} - 1\)) |
|---|------------------|----------|--------------------------|
| 0 | 1                | 1        | 1                        |
| 1 | 2                | 3        | 3                        |
| 2 | 4                | 7        | 7                        |
| 3 | 8                | 11       | 15                       |
| 4 | 16               | 19       | 31                       |
| 5 | 32               | 35       | 63                       |
| 6 | 64               | 67       | 127                      |
| 7 | 128              | 131      | 255                      |
| 8 | 256              | 259      | 511                      |
| 9 | 512              | 515      | 1023                     |

Os valores "Esperado" são calculados com base em uma fórmula recursiva específica:

```python
esperado[n] = esperado[n - 1] * 2 - 1
````

Com os valores iniciais definidos para os primeiros níveis.

---

## 🐍 Como executar

### Requisitos

* Python 3.6+
* Nenhuma biblioteca externa é necessária

### Passos

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/teorema-beck-simulador.git
cd teorema-beck-simulador
```

2. Execute o script:

```bash
python teorema_beck_simulador.py
```

### Saída esperada

```text
N   | Início (2^N)   | Esperado   | Fim (2^(N+1)-1)
-------------------------------------------------------
0   | 1              | 1          | 1
1   | 2              | 3          | 3
2   | 4              | 7          | 7
3   | 8              | 11         | 15
4   | 16             | 19         | 31
5   | 32             | 35         | 63
6   | 64             | 67         | 127
7   | 128            | 131        | 255
8   | 256            | 259        | 511
9   | 512            | 515        | 1023
```

---

## 🛠️ Como funciona a lógica "Esperado"

Os valores são gerados por uma **função recursiva empírica**, com base no seguinte:

* $\text{Esperado}_0 = 1$
* Para $N > 0$:

  $$
  \text{Esperado}_N = \text{Esperado}_{N-1} \times 2 - 1
  $$

Essa fórmula reflete um crescimento rápido, mas limitado, diferente de uma árvore binária cheia.

---

## 📄 Licença

Este projeto está disponível para fins acadêmicos e educacionais. Sinta-se à vontade para contribuir.

---

## 🙋‍♀️ Contribuições

Melhorias na modelagem, comentários ou testes adicionais são bem-vindos! Abra um Pull Request ou Issue.

--- 


## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
