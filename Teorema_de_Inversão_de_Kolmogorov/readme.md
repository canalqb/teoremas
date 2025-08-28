# 🌟 Teorema de Inversão de Kolmogorov e este Script 💡

Este repositório traz um **script em Python** que implementa uma aproximação da **função de distribuição acumulada (CDF)** de uma variável aleatória contínua a partir da sua função característica, utilizando o **Teorema de Inversão de Kolmogorov**. 🚀

---

## Sobre o Teorema de Inversão de Kolmogorov

O **Teorema de Inversão de Kolmogorov** é uma ferramenta fundamental na teoria das probabilidades que nos permite recuperar a distribuição acumulada \(F(x)\) de uma variável aleatória a partir da sua **função característica** \(\varphi(t)\).

De forma intuitiva, o teorema diz que, para toda variável aleatória \(X\), sua CDF pode ser escrita como uma integral envolvendo \(\varphi(t)\):

\[
F(x) = \frac{1}{2} - \frac{1}{\pi} \lim_{T \to \infty} \int_{-T}^{T} \frac{e^{-i t x} \varphi(t) - 1}{i t} dt
\]

✨ Isso é incrível, porque muitas vezes a função característica é mais fácil de manipular matematicamente que a própria CDF!

---

## Sobre este Script

Este código:

- Implementa a **função característica** da normal padrão, \(\varphi(t) = e^{-\frac{t^2}{2}}\), que é conhecida e suave.
- Usa a integral do **Teorema de Inversão de Kolmogorov**, aproximando o limite \(\lim_{T \to \infty}\) por um valor finito \(T = 2^A\), onde \(A\) varia de 0 a 8.
- Para cada valor de \(T\), calcula a aproximação da CDF no ponto \(x=0\) (sabemos que para a normal padrão, \(F(0) = 0.5\)).
- Mostra o resultado da aproximação e o intervalo correspondente para \(T\).

---

## Por que isso importa? 🤔

- **Aproximações práticas**: Na prática, não podemos integrar até o infinito, então o parâmetro \(T\) controla a precisão da aproximação.
- **Verificação numérica**: Podemos observar como o resultado converge para o valor esperado (0.5 para \(x=0\)) conforme \(T\) cresce.
- **Aplicações gerais**: Embora aqui aplicado à normal padrão, o método vale para qualquer distribuição com função característica conhecida.

---

## Exemplo de saída do script

```plaintext
 2^A |  Retorno Teorema |    Intervalo
----------------------------------------
    1 |     0.2387324146 | [1, 1]
    2 |     0.4073114293 | [2, 3]
    4 |     0.4761618351 | [4, 7]
    8 |     0.4953725875 | [8, 15]
   16 |     0.4993134552 | [16, 31]
   32 |     0.4999285633 | [32, 63]
   64 |     0.4999951846 | [64, 127]
  128 |     0.4999998583 | [128, 255]
  256 |     0.4999999986 | [256, 511]
````

Note como o valor se aproxima cada vez mais de **0.5**, mostrando o poder do teorema e da aproximação numérica!

---

## ⚠️ Como executar

1. Certifique-se de ter o Python instalado.
2. Instale o SciPy:

   ```
   pip install scipy
   ```
3. Execute o script e observe os resultados no terminal.

---

## Em resumo

Este projeto é uma **demonstração prática e didática** do Teorema de Inversão de Kolmogorov aplicado à distribuição normal padrão — um exemplo perfeito para quem quer entender a conexão profunda entre função característica e distribuições de probabilidade! 🌈✨

---  
 

## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
