# 📘 *Teorema de Itô* e Script de Modelagem Estocástica

## 🔍 Sobre o **Teorema de Itô**

O **Teorema de Itô** é um resultado fundamental do *cálculo estocástico*, área da matemática que estuda processos aleatórios, como o movimento browniano 🐾. Ele fornece uma regra para calcular a diferencial de funções de processos estocásticos, semelhante à regra da cadeia no cálculo clássico, mas levando em conta o comportamento aleatório e a variação quadrática desses processos.

Formalmente, para um processo estocástico $X_t$ e uma função $f(t, X_t)$, o Teorema de Itô estabelece que:

$$
df(t, X_t) = \frac{\partial f}{\partial t} dt + \frac{\partial f}{\partial x} dX_t + \frac{1}{2} \frac{\partial^2 f}{\partial x^2} (dX_t)^2
$$

Esse teorema é essencial para modelar e analisar sistemas com ruído e incerteza, muito usados em finanças 💰, física ⚛️, biologia 🧬 e engenharia ⚙️.

---

## 🖥️ Sobre o Script `Teorema_de_Ito.py`

Este script executa os seguintes passos:

1. **Carrega os dados**: uma lista de tripletas $(x, y, z)$, onde $x$ e $z$ são potências de 2, e $y$ é a variável de interesse.
2. **Modela $y$ em função de $x$** usando um *modelo polinomial de grau 2*.
3. **Faz a previsão** de $y$ para $x = 65536$.
4. **Simula o comportamento estocástico** de $y$ no intervalo entre os últimos valores, incorporando ruído browniano inspirado no *Teorema de Itô*.
5. **Gera um gráfico interativo** com os pontos reais, a simulação e legenda ao passar o mouse 🖱️.
6. **Exibe uma tabela comparativa** com valores observados, previstos e erro absoluto.

---

## 📊 Resultado Exemplo (últimas linhas da tabela)

```
    x  y_observado    y_previsto  erro_absoluto
 2048         2683   2912.192888     229.192888
 4096         5216   6020.230225     804.230225
 8192        10544  12301.702425    1757.702425
16384        26867  25126.236929    1740.763071
32768        51510  51821.666355     311.666355
65536        95823 109397.966881   13574.966881
```

---

## 🚀 Como usar o script

* Tenha **Python 3** instalado.
* Instale as dependências necessárias com:

```bash
pip install numpy pandas scipy plotly
```

* Rode o script no terminal:

```bash
python Teorema_de_Ito.py
```

* O gráfico interativo abrirá no navegador e a tabela de comparação será mostrada no console 🖥️.

---

## ⚠️ Observações importantes

* O modelo polinomial é uma *aproximação simples* e pode não capturar toda a complexidade dos dados.
* A simulação estocástica é uma implementação básica inspirada no Teorema de Itô, para ilustrar o efeito do ruído.
* O erro para o último ponto é relativamente alto, indicando que modelos mais avançados podem ser necessários para previsões mais precisas 🔍.

--- 

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
