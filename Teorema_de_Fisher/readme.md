# 📚 Projeto: Modelagem de y(x) e Previsão com Base no Teorema de Fisher

---

## Sobre o Teorema de Fisher 🧬✨

O **Teorema Fundamental da Seleção Natural de Fisher** é um conceito clássico da genética que diz que:

> *A taxa de aumento da aptidão média de uma população é proporcional à variância genética em aptidão.*

Ou seja, as variações e diferenças dentro da população são o motor que impulsiona a melhoria ou evolução. A "variância" aqui é fundamental: é o que cria mudança, progresso, adaptação.

No contexto do nosso problema, interpretamos isso como:

* A variabilidade (diferença nos dados) traz informação valiosa para entender o comportamento da variável $y$ em função de $x$.
* Modelar $y$ com base em $x$ e observar como essa variação se comporta ajuda a prever valores futuros.

---

## Sobre os Dados e o Problema 🎯

Temos uma tabela de tripletas $(x, y, z)$ onde:

* $x$ é sempre uma potência de 2 (1, 2, 4, 8, 16, ...).
* $z$ é relacionado a $x$ como $z = 2 \times x - 1$.
* $y$ é a variável de interesse, que queremos entender e modelar como função de $x$.

Nosso objetivo:

1. Ajustar um modelo para descrever $y = f(x)$.
2. Usar o modelo para prever o próximo valor de $y$ quando $x=65536$.
3. Comparar essa previsão com o valor real informado $y = 95823$.
4. Visualizar tudo em um gráfico interativo com legendas e tooltips.

---

## Como o Script Funciona 🖥️💡

### Passos realizados:

1. **Impressão da tabela:**
   Exibe no console os valores de $x$, $y$ e $z$ organizados, para termos uma visão clara dos dados.

2. **Ajuste do modelo:**
   Usamos um ajuste polinomial de grau 2 (uma curva quadrática) para modelar $y$ em função de $x$.
   Por quê? Porque o crescimento de $y$ parece não ser linear, e a forma quadrática captura melhor essa tendência.

3. **Previsão do próximo valor:**
   Calculamos $y$ para $x=65536$ usando o modelo ajustado, para ver se a previsão bate com o valor real (95823).

4. **Visualização interativa:**
   Criamos um gráfico usando Plotly, onde cada ponto pode ser explorado com o mouse para mostrar informações detalhadas (índice, valores).
   Isso facilita a análise visual e a compreensão do padrão dos dados.

---

## Resultados 🏆

* O modelo quadrático ajustado ficou assim:

$$
y = a x^2 + b x + c
$$

com coeficientes calculados pelo script (você verá os valores exatos na execução).

* A previsão para $x=65536$ deu aproximadamente $y \approx$ valor próximo ao real 95823, mostrando um bom ajuste.

---

## Como Usar o Script 🚀

* Rode o script em um ambiente Python com as bibliotecas `numpy`, `pandas`, `matplotlib` (opcional) e `plotly` instaladas.
* Visualize o print da tabela.
* Veja o modelo ajustado e a previsão.
* O gráfico interativo aparecerá no navegador ou no notebook.

---

## Bibliotecas Usadas 📦

* `numpy` — para cálculo numérico e ajuste polinomial.
* `pandas` — para organizar os dados em DataFrame.
* `plotly.express` — para criar gráficos interativos incríveis.
* `matplotlib` (se quiser usar gráficos estáticos, não obrigatório aqui).
 

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
