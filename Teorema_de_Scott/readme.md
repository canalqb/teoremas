# 📐 Estimador de Scott

Este projeto implementa um estimador baseado no que chamamos de **Teorema de Scott**, um modelo teórico que aproxima o número de elementos (ou nós) esperados entre dois níveis de uma estrutura binária, como em árvores binárias completas ou processos recursivos.

---

## 📖 O que é o Teorema de Scott?

O chamado **Teorema de Scott** não é um teorema clássico documentado na literatura formal, mas é interpretado aqui como uma **observação empírica** sobre o comportamento do crescimento de elementos entre níveis em estruturas exponenciais (como árvores binárias completas). 

Dado um nível `N`, temos:

- **Início**: \(2^N\) — o número mínimo de elementos em um nível `N` de uma árvore binária.
- **Fim**: \(2^{N+1} - 1\) — o número total de nós em uma árvore binária completa de profundidade `N`.
- **Estimado (Teorema)**: uma aproximação do total acumulado de nós esperados até o nível `N`, com base em uma função de crescimento empírica.

Este "teorema" serve como modelo didático para explorar funções de crescimento e suas aproximações computacionais.

---

## 📊 Exemplo de Saída

```text
N  | Início (2^N)   | Estimado (Teorema)     | Fim (2^(N+1))-1
------------------------------------------------------------
0  | 1              | 1                      | 1
1  | 2              | 1                      | 3
2  | 4              | 4                      | 7
3  | 8              | 11                     | 15
4  | 16             | 27                     | 31
5  | 32             | 62                     | 63
6  | 64             | 139                    | 127
7  | 128            | 305                    | 255
8  | 256            | 663                    | 511
9  | 512            | 1431                   | 1023
````

---

## 🧠 Justificativa do Script

O script utiliza uma aproximação empírica para o valor "esperado" a partir da soma cumulativa dos nós em uma estrutura binária. Em vez de copiar a coluna "Esperado pelo Teorema", a estimativa é gerada com base no seguinte modelo:

```python
estimado = round(sum(2 ** k for k in range(n)) * (1 + n / 5.0))
```

* `sum(2 ** k for k in range(n))` representa a soma dos nós até o nível `N-1`.
* O fator multiplicativo `1 + n / 5.0` ajusta a estimativa para acompanhar o crescimento observado nos dados empíricos.
* O valor final é arredondado para melhor aproximação.

Essa fórmula é empírica e pode ser ajustada para outros tipos de crescimento ou aplicações similares, como simulações de árvores, modelos recursivos ou estruturas de ramificação.

---

## 🖥️ Como usar

1. Clone este repositório:

```bash
git clone https://github.com/canalqb/teorema/estimador-scott.git
```

2. Execute o script:

```bash
python estimador_scott.py
```

3. O terminal exibirá a tabela com os valores para cada `N`.

---

## 📁 Estrutura

```
estimador-scott/
├── estimador_scott.py   # Script principal
└── README.md            # Este arquivo
```

---

## ✅ Requisitos

* Python 3.6+
* Nenhuma biblioteca externa necessária.

---

## 📌 Aplicações

* Modelagem de árvores binárias
* Análise de complexidade recursiva
* Estimativas de expansão de estados
* Ensino de estruturas de dados e funções exponenciais
 

## 📘 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
 

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
