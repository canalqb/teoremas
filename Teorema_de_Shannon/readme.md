## 🧠 Teorema de Shannon – Capacidade do Canal

### 📍 O que é?

O **Teorema de Shannon**, proposto por Claude Shannon em 1948, é um dos pilares da **Teoria da Informação**. Ele define o **limite máximo teórico** para a taxa de transmissão de dados em um canal de comunicação com ruído, sem perda de informação.

A fórmula é:

$$
C = B \cdot \log_2(1 + \frac{S}{N})
$$

Onde:

* **C** = capacidade do canal (bits por segundo)
* **B** = largura de banda (Hz)
* **S/N** = relação sinal/ruído (razão)

📌 Em outras palavras: **não importa o quão bom seja o código de compressão**, **nenhum sistema pode transmitir mais que C sem erros**, dado um canal com largura de banda e ruído fixos.

---

## 🧪 Sobre o Script

**Arquivo**: `Teorema_de_Shannon.py`
**Objetivo**: Modelar a variável `y` (capacidade observada) em função de `x` (potências de 2), usando uma **regressão polinomial de grau 2**.
**Aplicação prática**: Tentar prever a capacidade observada para o próximo valor de `x = 65536`.

---

## 🧩 Dados Utilizados

Cada linha representa uma tripleta `(x, y, z)`, onde:

* **x**: valor base (potência de 2)
* **y**: capacidade de canal medida ou estimada
* **z**: valor máximo possível (também potência de 2 - 1)

| x     | y     | z      |
| ----- | ----- | ------ |
| 1     | 1     | 1      |
| 2     | 3     | 3      |
| 4     | 7     | 7      |
| ...   | ...   | ...    |
| 32768 | 51510 | 65535  |
| 65536 | 95823 | 131071 |

---

## 🧠 Modelagem Matemática

Foi utilizado **Scikit-learn** para ajustar um **modelo polinomial de grau 2** à relação entre `x` e `y`.
O modelo gerou valores de `y_pred` para cada `x`, tentando se aproximar da `y` real.

### 📉 Saída do script:

```
    x     y      z  y_pred
    1     1      1    -173
    2     3      3    -171
    4     7      7    -168
    8     8     15    -162
   16    21     31    -150
   32    49     63    -126
   64    76    127     -78
  128   224    255      18
  256   467    511     211
  512   514   1023     595
 1024  1155   2047    1366
 2048  2683   4095    2912
 4096  5216   8191    6020
 8192 10544  16383   12302
16384 26867  32767   25126
32768 51510  65535   51822
65536 95823 131071  109398
```

✅ **O modelo conseguiu prever `y ≈ 109398` para `x = 65536`**, sendo que o valor real é **95823** — um erro aceitável considerando a simplicidade do modelo.

---

## 📊 Visualização

O gráfico interativo (se Plotly estiver instalado) mostra:

* **Pontos azuis**: valores reais de `y`
* **Linha de tendência**: valores previstos (`y_pred`)
* **Tooltip interativo** ao passar o mouse

---

## 🧰 Tecnologias Usadas

* Python 🐍
* Pandas
* Scikit-learn
* Plotly

---

## 🚀 Como Rodar

1. Instale os pacotes necessários:

   ```bash
   pip install pandas scikit-learn plotly
   ```

2. Execute o script:

   ```bash
   python Teorema_de_Shannon.py
   ```

---

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
