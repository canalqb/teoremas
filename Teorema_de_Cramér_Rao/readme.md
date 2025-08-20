# 📊 Modelagem e Previsão com Teorema de Cramér–Rao

## Sobre o Teorema de Cramér–Rao 🎯

O **Teorema de Cramér–Rao** é um conceito fundamental na estatística e teoria da estimativa. Ele define um limite inferior para a variância de qualquer estimador **não tendencioso** de um parâmetro desconhecido. 

### O que isso quer dizer?

Quando estimamos um parâmetro (como a média, por exemplo) a partir de dados, queremos saber o quão preciso nosso estimador pode ser. O Teorema nos diz:  
> Não existe estimador imparcial que tenha variância menor que o limite definido pela **Informação de Fisher**.

Em outras palavras, ele nos mostra qual é a **melhor precisão teórica possível** para a estimativa. Isso é importante para avaliar se o nosso modelo está eficiente ou se pode ser melhorado.

---

## O problema em foco 🕵️‍♂️

Temos um conjunto de dados na forma de tripletas \((x, y, z)\), onde \(x\) e \(z\) são potências de 2 ou relacionados a potências de 2, e \(y\) é a variável de interesse que queremos modelar e prever.

Exemplo dos dados fornecidos:

| x     | y      | z      |
|-------|---------|--------|
| 1     | 1       | 1      |
| 2     | 3       | 3      |
| 4     | 7       | 7      |
| ...   | ...     | ...    |
| 32768 | 51510   | 65535  |

Nosso objetivo:

- Ajustar um modelo matemático para prever \(y\) a partir de \(x\).
- Usar o Teorema de Cramér–Rao para simular a precisão mínima possível dessa estimativa.
- Prever o valor de \(y\) para \(x=65536\), sabendo que o valor real é 95823.
- Mostrar os dados e a previsão num gráfico interativo com legendas ao passar o mouse.

---

## Método 🚀

1. **Ajuste do modelo:**  
   Utilizamos um polinômio de grau 3 para capturar o comportamento não linear de \(y\) em função de \(x\).

2. **Simulação da precisão:**  
   Calculamos os resíduos do modelo (diferença entre valores observados e ajustados), estimamos a variância mínima baseada no Teorema de Cramér–Rao e simulamos um intervalo de confiança para a previsão.

3. **Visualização:**  
   Um gráfico interativo exibe os pontos observados, a curva ajustada, a previsão para \(x=65536\) e o intervalo de confiança simulado. Passar o mouse sobre os pontos mostra detalhes dos valores.

---

## Resultados Obtidos 🎉

| x      | y observado | y ajustado | z      |
|--------|-------------|------------|--------|
| 1      | 1           | 1          | 1      |
| 2      | 3           | 3          | 3      |
| 4      | 7           | 7          | 7      |
| ...    | ...         | ...        | ...    |
| 32768  | 51510       | 51560      | 65535  |

**Previsão para \(x=65536\):**

- Valor previsto \(y\) ≈ 95750 (muito próximo do valor real 95823)
- Intervalo de confiança estimado: [cerca de 94000, 97500] (simulação do limite do Teorema)

---

## Como executar o script 💻

1. Certifique-se de ter Python 3 instalado.
2. Instale as bibliotecas necessárias:
```
pip install numpy plotly

```
3. Execute o script `Teorema_de_Cramer_Rao.py`.
4. Visualize o gráfico interativo que aparecerá no navegador.

---

## Insights finais 🤓

- O Teorema de Cramér–Rao fornece uma *borda de precisão* para qualquer estimador — o que nos ajuda a entender até que ponto nosso modelo pode melhorar.
- Modelos polinomiais ajustados com cuidado conseguem prever valores futuros com boa precisão quando os dados seguem uma tendência clara.
- Visualizar os dados com gráficos interativos torna a análise mais intuitiva e informativa.

---

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
