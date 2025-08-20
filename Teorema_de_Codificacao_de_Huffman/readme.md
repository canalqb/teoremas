# 🎯 Teorema de Codificação de Huffman + Ajuste Polinomial com Python

> **"Eficiência máxima, compressão ideal!"** — Huffman, provavelmente.

## 📚 Sobre o Teorema

O **Teorema de Codificação de Huffman** é um dos pilares da teoria da informação. Criado por David Huffman em 1952, ele propõe um método ótimo para compressão de dados sem perdas.

Em essência:

* Caracteres (ou dados) mais frequentes recebem códigos menores.
* Os menos frequentes, códigos maiores.
* O resultado? **Compressão eficiente** com **reconstrução perfeita** da informação original.

## 🧠 O que este script faz?

Este projeto não implementa diretamente a árvore de Huffman, mas **analisa os limites teóricos da codificação** com base em três grandezas:

| Símbolo | Significado                                      |
| ------- | ------------------------------------------------ |
| `x`     | Número de símbolos distintos                     |
| `y`     | Número mínimo de bits necessários para codificar |
| `z`     | Tamanho da maior palavra binária possível        |

A ideia é mostrar como o número de bits cresce em função do número de símbolos e como isso se relaciona com a **eficiência do código**.

---

## 🔍 O que está acontecendo no script?

1. **Importação de bibliotecas úteis**:

   * `numpy`, `pandas`, `plotly`, `sklearn`: para manipulação, modelagem e visualização dos dados.

2. **Definição de dados reais**:

   * Conjuntos de valores `x`, `y`, `z` representando a relação entre número de símbolos e comprimento de codificação.

3. **Ajuste Polinomial**:

   * Um modelo polinomial de grau 2 é ajustado para prever como `y` (número de bits) cresce com `x`.

4. **Predição do futuro** (✨):

   * Calcula `y` para `x = 65536`, o próximo passo na tabela.
   * Compara com `z`, o valor máximo esperado segundo o Teorema de Huffman.

5. **Visualização Interativa**:

   * Um gráfico interativo usando Plotly mostra os pontos reais e a curva do modelo polinomial, ilustrando o crescimento do custo de codificação.

---

## 📈 Gráfico gerado

O gráfico mostra:

* Pontos reais (valores tabulados de `x`, `y`, `z`)
* A curva do modelo polinomial representando a tendência de crescimento de `y`
* Tooltip interativa com os valores `x`, `y`, `z`

---

## 🧪 Exemplo de saída (console)

```
     x      y      z
     1      1      1
     2      3      3
     4      7      7
     8      8     15
    ...
 32768  51510  65535
 65536 109398 131071
```

Note como `y` cresce rapidamente, mas ainda mantém-se abaixo de `z` — uma demonstração prática do limite teórico de Huffman.

---

## ⚠️ Observações técnicas

* Um warning do `sklearn` aparece ao prever valores fora do dataframe original. Isso não afeta a execução.
* O modelo polinomial é apenas uma aproximação; Huffman é mais eficiente que uma simples função matemática.

---

## 💡 Conclusão

Este projeto é uma bela combinação de **teoria da computação**, **estatística** e **visualização de dados** para entender um dos teoremas mais importantes da compressão de dados.

🎉 **Experimente, visualize, explore!**
Veja como a matemática explica o limite da codificação — e como Huffman chegou lá primeiro.

---

## 🚀 Como executar

```bash
python Teorema_de_Codificacao_de_Huffman.py
```

Certifique-se de ter instalado as bibliotecas:

```bash
pip install numpy pandas plotly scikit-learn
```

---

## 📂 Estrutura

```
📁 Teoremas/
│
├── Teorema_de_Codificacao_de_Huffman.py
└── README.md  ← você está aqui 😄
```

---

## 🧠 Curiosidade

> Huffman desenvolveu seu algoritmo como parte de um trabalho de classe. Seu professor, Robert Fano, também criou outro método de codificação (Fano Coding)... que foi superado pelo aluno. 😅 

---

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
