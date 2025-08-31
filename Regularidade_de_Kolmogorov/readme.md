# 🚀 Teorema de Regularidade de Kolmogorov — Demonstração Numérica

## ✨ O que é o Teorema de Regularidade de Kolmogorov?

O **Teorema de Regularidade de Kolmogorov** é um pilar fundamental na teoria dos processos estocásticos. Ele oferece condições suficientes para garantir que um processo aleatório \(X_t\) tenha trajetórias **contínuas** e com suavidade controlada, conhecida como **continuidade Hölder**.

### Enunciado simplificado do teorema:

Se existem constantes positivas \( \alpha, \beta, C > 0 \) tais que, para todos \( s, t \),

\[
\mathbb{E}[|X_t - X_s|^\alpha] \leq C |t - s|^{1 + \beta},
\]

então \(X_t\) possui uma versão com trajetórias **Hölder contínuas** para qualquer expoente \(\gamma\) que satisfaça

\[
0 < \gamma < \frac{\beta}{\alpha}.
\]

Em palavras simples: o teorema diz que, se os incrementos do processo são suficientemente “bem comportados” estatisticamente, então as trajetórias desse processo não serão abruptas — elas terão uma suavidade quantificável.

---

## 🎯 Para que serve este teorema?

- **Garantir a existência de versões contínuas de processos aleatórios**, fundamental em teoria da probabilidade.
- **Analisar a suavidade das trajetórias** de processos como o movimento browniano, ruídos gaussianos e outros.
- **Apoiar a modelagem matemática** em física, finanças, biologia e engenharia, onde trajetórias suaves são esperadas.
- **Fornecer base teórica para simulações e algoritmos** que dependem de propriedades de continuidade e regularidade.

---

## 💻 Sobre o script desta demonstração

Este projeto apresenta uma **simulação numérica simples** que ilustra o Teorema de Regularidade de Kolmogorov usando o movimento browniano:

- Gera múltiplas trajetórias simuladas do movimento browniano com passos discretos.
- Calcula os incrementos elevados a uma potência \(\alpha\) (tipicamente 2) para intervalos em potências de 2, ou seja, nos intervalos \([2^n, 2^{n+1} - 1]\) para \(n=0, 1, \ldots, 10\).
- Imprime no console as médias desses incrementos para cada intervalo, relacionando a análise à escala temporal.
- Identifica pontos de interconexão representativos em cada intervalo.
- Plota as trajetórias simuladas e um gráfico log-log dos incrementos, evidenciando a relação esperada pelo teorema.

Este código serve como uma ponte entre a teoria abstrata e a visualização prática, tornando mais palpável a ideia de regularidade em processos aleatórios.

---

## 📊 Por que analisar intervalos em potências de 2?

Estes intervalos escalonados permitem observar o comportamento do processo em diferentes “resoluções temporais”. É uma forma clássica e poderosa de investigar como a variabilidade do processo cresce com o tamanho do intervalo, fundamental para comprovar empiricamente as condições do teorema.

---

## 🚀 Experimente!

Execute o script para ver em ação como a média dos incrementos se comporta conforme o tamanho dos intervalos aumenta — você verá na prática a mágica do Teorema de Kolmogorov em garantir a suavidade das trajetórias do movimento browniano!

---

## 📚 Referências

- Kolmogorov, A.N. (1940). *Wienersche Spiralen und einige andere interessante Kurven im Hilbertschen Raum*.
- Revuz, D., Yor, M. (1999). *Continuous Martingales and Brownian Motion*.
- Kallenberg, O. (2002). *Foundations of Modern Probability*.
 

---

  
## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
