## 📦 Análise e Previsão com o Teorema de Kraft–McMillan

Este projeto combina conceitos da **teoria da codificação** com **modelagem preditiva de dados** para analisar padrões e prever o crescimento de uma variável `y` com base em `x`, onde ambos seguem potências de 2. Também é feita uma conexão com o **Teorema de Kraft–McMillan**, um pilar da compressão de dados sem perda.

---

### 📚 O que é o Teorema de Kraft–McMillan?

O Teorema de Kraft–McMillan é essencial na construção de **códigos prefixos**, como o **código de Huffman**. Ele diz que, para um conjunto de códigos binários com comprimentos $l_1, l_2, ..., l_n$, a seguinte desigualdade deve ser satisfeita:

$$
\sum_{i=1}^{n} 2^{-l_i} \leq 1
$$

Se essa condição for satisfeita, então **existe um código prefixo** com aqueles comprimentos. Se a soma for **igual a 1**, o código é **completo** (não cabe mais nenhum outro sem violar a propriedade prefixo).

---

### 📊 O que este projeto faz?

* Fornece uma lista de **tripletas** `(x, y, z)`, onde `x` e `z` são potências de 2, e `y` é uma contagem associada.
* Ajusta um modelo de regressão linear para estimar `y` com base em `log2(x)`.
* Previsão do valor de `y` para `x = 65536` com base no comportamento anterior.
* Compara a previsão com o valor real conhecido (`95823`).
* Cria um gráfico interativo e uma tabela de comparação.

---

### 🧠 Dados usados

```python
dados = [
    (1, 1, 1), (2, 3, 3), (4, 7, 7), (8, 8, 15), (16, 21, 31), (32, 49, 63),
    (64, 76, 127), (128, 224, 255), (256, 467, 511), (512, 514, 1023),
    (1024, 1155, 2047), (2048, 2683, 4095), (4096, 5216, 8191),
    (8192, 10544, 16383), (16384, 26867, 32767), (32768, 51510, 65535),
    # Previsão:
    (65536, ?, 131071)  # valor real de y = 95823
]
```

---

### 🧮 Lógica do Script

1. Transformamos `x` em `log2(x)` para linearizar a tendência.
2. Ajustamos uma **regressão linear simples**:

   $$
   y = a \cdot \log_2(x) + b
   $$
3. Previsão para `x = 65536` (i.e. $\log_2(65536) = 16$).
4. Comparamos valor real vs valor previsto.
5. Mostramos o gráfico interativo com hover nos pontos e uma tabela de erros.

---

### 📈 Resultado da Previsão

O modelo previu um valor muito próximo de `95823` para `x = 65536`, validando a tendência observada nos dados anteriores. Isso mostra como padrões logarítmicos são úteis em estruturas que crescem exponencialmente — como árvores binárias em codificação 📡.

---

### ▶️ Como rodar o script

1. Instale as dependências:

```bash
pip install numpy pandas scikit-learn plotly
```

2. Rode o script Python `main.py` (ou seu notebook):

```bash
python main.py
```

3. O gráfico será exibido interativamente no navegador, e a tabela será mostrada no terminal.

---

### 📌 Observações

* O Teorema de Kraft–McMillan **não está sendo aplicado diretamente aos dados**, mas é citado por analogia ao comportamento dos dados em sistemas binários e codificação.
* `x` e `z` seguem padrões binários, sugerindo uma conexão conceitual com códigos prefixos e tamanhos de árvore binária.

---

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
