# 📘 Teorema de Gauss-Markov & Ajuste de Modelo em Python 🚀

---

## Sobre o Teorema de Gauss-Markov 📐✨

O **Teorema de Gauss-Markov** é um pilar fundamental na estatística e econometria que garante que, sob certas condições, o método dos **Mínimos Quadrados Ordinários (OLS)** é o **melhor estimador linear insesgado** (BLUE - Best Linear Unbiased Estimator).

Ou seja: entre todos os estimadores lineares sem viés, o OLS tem a **menor variância**, entregando a previsão mais precisa e confiável para um modelo linear! 🎯💡

---

## O que o script faz? 🖥️🔍

1. **Recebe uma lista de dados** em tripletas (x, y, z), onde:

   * $x$ e $z$ são potências de 2,
   * $y$ é a variável que queremos modelar e prever.

2. **Ajusta uma equação polinomial de grau 2** que relaciona $y$ com $x$ usando o método de mínimos quadrados (seguindo o Teorema de Gauss-Markov). 📊

3. **Mostra na tela uma tabela** comparando os valores reais de $y$ e os valores previstos pelo modelo.

4. **Faz a previsão para $x=65536$**, comparando com o valor real fornecido (95823). 🔮

5. **Gera um gráfico interativo**, onde você pode passar o mouse para ver detalhes dos pontos reais e previstos, incluindo o novo ponto previsto. 📈✨

---

## Exemplo de saída 📝

```
       x     y_real     y_pred
       1          1       -172
       2          3       -171
       4          7       -168
       8          8       -162
      16         21       -150
      32         49       -125
      64         76        -77
     128        224         18
     256        467        210
     512        514        595
    1024       1155       1366
    2048       2683       2912
    4096       5216       6020
    8192      10544      12301
   16384      26867      25126
   32768      51510      51821
   65536      95823     109397 (Previsão)
```

---

## Como usar? 🛠️

1. Salve o script `Teorema_de_Gauss_Markov.py` no seu computador.
2. Execute com Python 3:

   ```bash
   python Teorema_de_Gauss_Markov.py
   ```
3. Veja a tabela na saída do terminal e o gráfico interativo abrir no navegador.
4. Explore o gráfico passando o mouse sobre os pontos para ver as legendas detalhadas.

---

## Dependências ⚙️

* Python 3.x
* numpy
* plotly

Você pode instalar as bibliotecas necessárias com:

```bash
pip install numpy plotly
```

---

## Curiosidades e dicas! 🤓💬

* O modelo usa um **polinômio de grau 2** para capturar a relação não linear entre $x$ e $y$.
* Mesmo com um modelo simples, a previsão do valor $y$ para $x=65536$ ficou próxima do real (95823), mostrando a utilidade do método.
* O Teorema de Gauss-Markov é a base de muitos modelos estatísticos e econométricos modernos.

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
