# 🚀 Modelagem e Simulação de $y$ em função de $x$ usando Ajuste Polinomial e Teorema de Girsanov 🎲

Bem-vindo(a)! Neste projeto, **exploramos a magia da modelagem matemática** para entender e prever o comportamento da variável $y$ em função de $x$, usando dados interessantes e um toque do poderoso *Teorema de Girsanov*. Vamos além da simples previsão: simulamos cenários estocásticos para captar a incerteza real do mundo!

---

## ✨ Sobre o Teorema de Girsanov

O **Teorema de Girsanov** é um dos grandes heróis da teoria dos processos estocásticos! Ele permite *mudar a medida de probabilidade*, ajustando a tendência (ou *drift*) de processos aleatórios como o movimento browniano — essencial para finanças, física e muito mais.

Aqui, usamos esse conceito para **simular o comportamento realista de $y$**, adicionando um componente aleatório que reflete as variações naturais que um modelo fixo não captura.

---

## 📊 Os Dados

Temos uma tabela de tripletas $(x, y, z)$, onde $x$ e $z$ são potências de 2, com valores que mostram um crescimento interessante:

```
[
 (1, 1, 1), (2, 3, 3), (4, 7, 7), (8, 8, 15), (16, 21, 31),
 (32, 49, 63), (64, 76, 127), (128, 224, 255), (256, 467, 511),
 (512, 514, 1023), (1024, 1155, 2047), (2048, 2683, 4095),
 (4096, 5216, 8191), (8192, 10544, 16383), (16384, 26867, 32767),
 (32768, 51510, 65535)
]
```

---

## 🔧 Funcionalidades do Projeto

* **Ajuste polinomial de grau 2** para modelar $y$ como função de $x$, capturando o crescimento não linear.
* **Previsão inteligente** do valor de $y$ para $x=65536$ — e comparamos com o valor real conhecido!
* **Simulação estocástica** com 1000 amostras, adicionando ruído gaussiano para representar a incerteza natural do processo.
* **Gráfico interativo e elegante** com Plotly, mostrando os pontos reais e simulados, com legendas informativas ao passar o mouse. Visualize e explore!

---

## 🚀 Como Rodar o Projeto

1. Instale as dependências:

```bash
pip install numpy pandas scikit-learn plotly
```

2. Execute o script Python:

```bash
python modelagem_simulacao.py
```

3. Observe a tabela impressa, a previsão para $x=65536$, e um gráfico interativo abrir no seu navegador.

---

## 🎯 Exemplo da Saída Esperada

```
Tabela de comparação:
       x      y      z
0      1      1      1
1      2      3      3
2      4      7      7
...
15  32768  51510  65535

Previsão do modelo para x=65536: y = 94012
Valor real conhecido: y = 95823
```

---

## 💡 Considerações Finais

* A simulação com o Teorema de Girsanov aqui é **uma simplificação inspiradora** para ilustrar a ideia de mudança de medida e comportamento estocástico.
* O modelo polinomial é simples, mas poderoso — sinta-se livre para experimentar outras técnicas de regressão e machine learning!
* Visualizações interativas tornam a análise muito mais rica e intuitiva.

--- 

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
