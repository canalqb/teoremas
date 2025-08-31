# 🧠 Representação de Kolmogorov–Arnold: Uma Demonstração Computacional

Este repositório apresenta uma demonstração computacional simplificada do **Teorema de Representação de Kolmogorov–Arnold**, um dos resultados mais surpreendentes da análise matemática e da teoria da computação.

---

## 📌 Sobre o Teorema de Kolmogorov–Arnold

> “Toda função contínua de múltiplas variáveis pode ser representada como uma composição finita de funções contínuas de uma única variável e de adição.”  
> — A.N. Kolmogorov, 1957

O **Teorema de Kolmogorov**, posteriormente generalizado por **V.I. Arnold**, estabelece que qualquer função contínua \( f: [0,1]^n \to \mathbb{R} \) pode ser decomposta como:

\[
f(x_1, x_2, ..., x_n) = \sum_{q=0}^{2n} \phi_q\left( \sum_{p=1}^{n} \psi_{q,p}(x_p) \right)
\]

Ou seja:

✅ Não é necessário multiplicação  
✅ Nem funções multivariadas intermediárias  
✅ Apenas **soma** e **funções univariadas compostas**

### 🌟 Por que isso é revolucionário?

- **Redução dimensional**: Constrói funções multivariadas usando apenas funções univariadas.
- **Base teórica de redes neurais**: Influenciou diretamente os teoremas de aproximação universal em redes neurais feedforward.
- **Não intuitivo**: Antes de Kolmogorov, acreditava-se que era impossível representar funções complexas de múltiplas variáveis sem operar diretamente sobre várias dimensões.

---

## 🎯 O que este projeto demonstra?

Neste exemplo, exploramos uma **forma reduzida** do teorema:

- A função original \( f(x, y) = \sin(x) \cdot \cos(y) \) é uma função bidimensional contínua.
- A função aproximada é construída seguindo a estrutura Kolmogoroviana com apenas **um termo**:

\[
f_{\text{approx}}(x, y) = \phi_1(\psi_1(x) + \psi_2(y))
\]

Com:
- \( \psi_1(x) = \sin(x) \)
- \( \psi_2(y) = \cos(y) \)
- \( \phi_1(z) = 0.5 \cdot \sin(z) \)

Essa aproximação é **intencionalmente simplificada** para fins didáticos e computacionais, mas preserva a essência do teorema: **usar apenas funções univariadas e adição** para construir uma função de duas variáveis.

---

## 🧪 Como o script funciona?

1. Gera amostras bidimensionais a partir de intervalos de potências de 2: \([2^n, 2^{n+1} - 1]\) para \(n = 0\) até \(29\).
2. Avalia a função original \( \sin(x)\cos(y) \) no grid gerado.
3. Avalia a função aproximada via Kolmogorov (reduzida).
4. Exibe visualmente, em gráficos 3D, a comparação entre a função original e sua aproximação.

---

## 📷 Visualização

O script gera dois gráficos lado a lado:

- ✅ **Gráfico 1**: Superfície da função original \( \sin(x) \cdot \cos(y) \)
- 🔁 **Gráfico 2**: Aproximação usando o modelo Kolmogorov-reduzido

Essa visualização destaca a **qualidade da aproximação** e como estruturas complexas podem emergir de construções extremamente simples.

---

## ⚙️ Requisitos

- Python 3.x
- `numpy`
- `matplotlib` 

--- 

## ▶️ Como Executar

Certifique-se de que as dependências estão instaladas executando:

`pip install numpy matplotlib`

Depois, execute o script diretamente com:

`python kolmogorov_representation_intervals_reduced.py`

O programa irá:

- Calcular a função original e sua aproximação;
- Exibir amostras numéricas dos resultados;
- Renderizar dois gráficos 3D comparativos: a função original vs. a aproximação via Kolmogorov.

---

## 📚 Referências Acadêmicas

- **Kolmogorov, A.N.** (1957). *On the representation of continuous functions of several variables by superpositions of continuous functions of one variable and addition*. *Doklady Akademii Nauk SSSR*.
- **Arnold, V.I.** (1957). *On functions of three variables*. *Doklady Akademii Nauk SSSR*.
- **Hecht-Nielsen, R.** (1987). *Kolmogorov’s Mapping Neural Network Existence Theorem*. *Proceedings of the International Conference on Neural Networks*.

Esses trabalhos fundamentam a teoria da representação funcional e influenciam diretamente áreas como redes neurais, compressão de dados e teoria da computação.

---

## 🧩 Notas e Curiosidades

- O Teorema de Kolmogorov é **não construtivo**: ele **garante a existência** das funções univariadas \( \phi_q \) e \( \psi_{q,p} \), mas **não fornece uma fórmula fechada** para elas.
- Na prática, como neste projeto, usamos aproximações simples e heurísticas para ilustrar o princípio estrutural do teorema.
- Apesar de não ser uma implementação exata da versão completa do teorema, essa aproximação evidencia como estruturas univariadas podem reproduzir comportamentos multivariados complexos.

---

## ✅ Conclusão

Este projeto exemplifica como uma das ideias mais contraintuitivas e poderosas da matemática moderna — a representação de funções multivariadas usando apenas composições de funções univariadas e adição — pode ser trazida à vida com ferramentas computacionais simples.

O **Teorema de Kolmogorov–Arnold** permanece como um marco teórico com desdobramentos profundos na análise funcional, aprendizado de máquina e ciência da complexidade.

---

  
## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
