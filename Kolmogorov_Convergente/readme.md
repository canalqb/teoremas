# 🧠 Teorema de Kolmogorov e Séries Convergentes

Este repositório explora o **Teorema de Convergência de Kolmogorov** aplicado a **séries de variáveis aleatórias independentes**, com uma simulação prática em Python para ilustrar como essas séries se comportam ao longo de intervalos crescentes definidos por potências de 2.

---

## 📘 Sobre o Teorema de Kolmogorov

O **Teorema de Kolmogorov** é um resultado fundamental da teoria da probabilidade. Ele estabelece condições sob as quais a **soma de variáveis aleatórias independentes** converge **quase certamente** (ou seja, com probabilidade 1).

### 🧮 Enunciado (forma clássica)

Seja $(X_n)$ uma sequência de variáveis aleatórias independentes, com:

* Esperança $\mathbb{E}[X_n] = 0$
* Variância $\operatorname{Var}(X_n) < \infty$

Se:

$$
\sum_{n=1}^\infty \operatorname{Var}(X_n) < \infty
$$

Então:

$$
\sum_{n=1}^\infty X_n \quad \text{converge quase certamente}
$$

Em termos simples: mesmo somando infinitas variáveis aleatórias, é possível garantir que o total **não explode**, desde que a variância total seja controlada.

---

## 🔬 Objetivo do Projeto

Este projeto busca:

1. Simular a **soma de variáveis aleatórias independentes** dentro de **intervalos definidos por potências de 2**.
2. Aplicar a condição do Teorema de Kolmogorov (controle da variância).
3. Visualizar como essas somas se comportam à medida que o intervalo cresce.
4. Relacionar os resultados com **pontos internos dos intervalos** ("centros de convergência").

---

## 📜 Estrutura do Script

### Arquivo: `Kolmogorov_Convergente.py`

#### O que o script faz:

* Define uma série de intervalos $[2^{A-1}, 2^A - 1]$ para $A = 1$ até $10$
* Para cada intervalo:

  * Gera variáveis aleatórias $X_n$ com esperança zero e variância $\frac{1}{n^{1.5}}$ (para garantir convergência)
  * Soma todos os $X_n$ do intervalo
  * Armazena o ponto médio do intervalo e o valor da soma
* Imprime os resultados e **plota um gráfico** com os pontos médios vs. as somas
* Mostra graficamente o comportamento da série sob o critério de Kolmogorov

#### Exemplo de saída:

```
2^A	Intervalo		Ponto_Médio	Soma Aleatória
2	[2, 3]		2.5		0.24678
4	[4, 7]		5.5		-0.15694
8	[8, 15]		11.5		0.02413
...
```

#### Exemplo de gráfico:

O gráfico mostra como a soma de variáveis aleatórias se estabiliza ou oscila suavemente, indicando convergência quase certa, conforme previsto pelo teorema.

---

## 📈 Gráfico Gerado

O gráfico ilustra:

* **Eixo X**: ponto médio do intervalo
* **Eixo Y**: soma das variáveis aleatórias no intervalo

A linha horizontal $y = 0$ serve como referência de estabilidade. Oscilações próximas a essa linha mostram convergência controlada.

---

## 🛠️ Requisitos

* Python 3.8+
* Bibliotecas:

```bash
pip install numpy matplotlib
```

---

## 🧩 Expansões Possíveis

* Comparar diferentes taxas de decaimento da variância (ex: $1/n^2$, $1/n$, $1/\log(n)^2$)
* Animar a convergência em tempo real
* Relacionar com números de Mersenne (como na sua tabela original)
* Exportar resultados para CSV ou DataFrame para análise estatística

---

## 📚 Referências

* Kolmogorov, A. N. (1933). *Foundations of the Theory of Probability.*
* Shiryaev, A. N. (1996). *Probability.*

---

## 📁 Licença

Este projeto é de domínio público para fins educacionais. Use, modifique e compartilhe como quiser.

---

## 🐍 Como executar

1. Certifique-se de ter Python 3 instalado.
2. Clone este repositório ou copie o script.
3. Execute o script:
 
---  

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
