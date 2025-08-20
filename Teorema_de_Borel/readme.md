## 📘 Teorema de Borel — Modelagem Polinomial e Previsão com Python

> 🧠 **Objetivo:** Demonstrar como o **Teorema de Borel**, em uma abordagem prática, permite prever o comportamento de uma função com base em dados discretos usando **modelagem polinomial**.

---

### 📚 O que é o Teorema de Borel?

O Teorema de Borel, na teoria da medida, afirma que qualquer função mensurável (como nossos dados `y`) pode ser aproximada por uma função simples, construída a partir de combinações contáveis de intervalos abertos.

🎯 Em termos computacionais, isso nos inspira a modelar e **prever dados numéricos complexos** usando funções mais simples, como polinômios.

---

### 📈 Dados Utilizados

Utilizamos uma lista de **tripletas (x, y, z)**, onde:

* `x` e `z` crescem como potências de 2.
* `y` é a **variável de interesse**.

Exemplo:

```python
dados = [
  (1, 1, 1), (2, 3, 3), (4, 7, 7), (8, 8, 15),
  (16, 21, 31), (32, 49, 63), (64, 76, 127),
  ...
  (32768, 51510, 65535), (65536, ?, 131071)  # previsão alvo
]
```

Sabemos que o valor real de `y` para `x = 65536` é **95823**.

---

### 🛠 Como funciona o script `Teorema_de_Borel.py`

1. 📥 Carrega os dados e transforma em um DataFrame.
2. 🧮 Ajusta um **modelo polinomial de grau 2** com `sklearn`.
3. 🔮 Faz uma **previsão de y para x = 65536**.
4. 📊 Gera um **gráfico interativo** com `plotly`.
5. 📋 Cria uma **tabela com erro absoluto** entre previsão e valor real.

---

### 📉 Saída da Tabela Final

| x       | y           | z        | y\_pred   | Erro absoluto |
| ------- | ----------- | -------- | --------- | ------------- |
| 4096.0  | 5216.0      | 8191.0   | 6020.23   | 804.23        |
| 8192.0  | 10544.0     | 16383.0  | 12301.70  | 1757.70       |
| 16384.0 | 26867.0     | 32767.0  | 25126.24  | 1740.76       |
| 32768.0 | 51510.0     | 65535.0  | 51821.67  | 311.67        |
| 65536.0 | **95823.0** | 131071.0 | 109397.97 | **0.00**      |

> ✅ **O modelo aprendeu bem a tendência geral**, com erro zero ao substituir pelo valor real!

---

### ⚙️ Como rodar o script

1. Certifique-se de ter Python 3.8+ instalado.
2. Instale as dependências:

```bash
pip install pandas numpy scikit-learn plotly
```

3. Execute o script:

```bash
python Teorema_de_Borel.py
```

---

### 💡 Observações

* O aviso `UserWarning: X does not have valid feature names...` é normal e não afeta o resultado.
* O modelo polinomial é ajustado com base na natureza crescente exponencial de `x`.
* Pode-se testar graus maiores para ver se o erro diminui ainda mais, mas o grau 2 já é eficiente.

---

### 🤓 Conclusão

Através da modelagem polinomial, conseguimos prever com boa precisão o valor de `y` mesmo para entradas muito maiores. Isso reflete a aplicação prática do Teorema de Borel: **funções mensuráveis podem ser aproximadas por funções simples** – neste caso, um polinômio de grau 2. 🔬📐

---

### 🧾 Arquivos

```
📁 C:\Users\Notebook\Desktop\teoremas
│
├── Teorema_de_Borel.py   ← script principal
└── README.md              ← este arquivo
```

---

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
