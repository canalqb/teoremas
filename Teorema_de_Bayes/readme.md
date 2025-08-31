# Estimativa Bayesiana para Localização do Teorema

## Sobre o Teorema de Bayes

O **Teorema de Bayes** é uma ferramenta fundamental na estatística e na teoria da probabilidade que permite atualizar a probabilidade de uma hipótese com base em novas evidências. Formalmente, ele é expresso como:

$$
P(H|E) = \frac{P(E|H) \times P(H)}{P(E)}
$$

onde:

* $P(H|E)$ é a probabilidade posterior da hipótese $H$ dado a evidência $E$;
* $P(E|H)$ é a verossimilhança, ou a probabilidade de observar a evidência $E$ se a hipótese $H$ for verdadeira;
* $P(H)$ é a probabilidade a priori da hipótese $H$;
* $P(E)$ é a probabilidade da evidência $E$ observada.

O teorema é amplamente usado para tomar decisões e estimar parâmetros em contextos onde há incerteza e evidências parciais.

---

## Sobre o Script

O script em Python implementa uma abordagem simples para estimar a distribuição da busca por um teorema em diferentes intervalos, baseando-se apenas nos intervalos de busca e no princípio do Teorema de Bayes.

### Dados usados:

* Uma tabela com intervalos definidos por colunas `Inicio` e `Fim`.
* Não utiliza diretamente os valores da coluna `Procura` (que seriam os dados observados), apenas para comparação.

### Funcionamento do Script:

1. **Definição das hipóteses $H_i$:**

   Cada hipótese corresponde ao teorema estar em um intervalo específico definido por `Inicio` e `Fim`.

2. **Probabilidade a priori $P(H_i)$:**

   Calculada proporcionalmente ao tamanho do intervalo, assumindo que o teorema pode estar uniformemente distribuído em todos os pontos do espaço considerado.

3. **Estimativa do valor esperado da procura:**

   Assume que a procura está uniformemente distribuída dentro do intervalo, estimando o valor esperado como o ponto médio do intervalo.

4. **Normalização:**

   A soma das estimativas é escalada para coincidir com a soma dos valores reais observados (total da procura).

5. **Resultado:**

   O script exibe uma tabela comparando os valores estimados para a procura em cada intervalo.

---

## Exemplo de saída

```
Comparação entre Procura real e Procura estimado pelo modelo simples:

   Inicio  Fim  Procura_estimado
0       1    2                 1
1       2    4                 3
2       4    8                 6
3       8   16                12
4      16   32                24
5      32   64                49
6      64  128                98
7     128  256               196
```

---

## Como usar

1. Salve o script `bayesian_search_estimator.py` no seu computador.
2. Execute com Python 3:

   ```bash
   python bayesian_search_estimator.py
   ```
3. Observe a saída no terminal, que mostra a comparação entre a procura real e a estimada.

---

## Possíveis melhorias

* Incorporar evidências reais para refinar a verossimilhança $P(E|H)$.
* Utilizar distribuições mais realistas (por exemplo, gaussianas) para modelar a localização da procura dentro dos intervalos.
* Aplicar o Teorema de Bayes para atualizar as probabilidades a partir de evidências observadas.

---

## Código do Script

```python
import numpy as np
import pandas as pd

# Dados originais da tabela (sem usar 'Procura' no cálculo)
data = {
    "Inicio": [1, 2, 4, 8, 16, 32, 64, 128],
    "Fim":    [2, 4, 8, 16, 32, 64, 128, 256]
}

df = pd.DataFrame(data)
df['Tamanho'] = df['Fim'] - df['Inicio']

# Prior proporcional ao tamanho do intervalo
total_tamanho = df['Tamanho'].sum()
df['P_H'] = df['Tamanho'] / total_tamanho

# Para estimar o "valor esperado da procura" em cada intervalo,
# vamos assumir que o valor está distribuído uniformemente no intervalo,
# e usar o centro do intervalo como estimativa do valor esperado

df['Procura_estimado'] = ((df['Inicio'] + df['Fim']) / 2).astype(int)

# Agora normalizamos a coluna estimada para aproximar o total de "Procura" observada
# Para comparação: o total esperado da "Procura" (com base no dado original)
total_procura_real = 1+3+7+8+21+49+76+224  # soma da coluna real (se quiser comparar)

# Escalar os valores estimados para que a soma seja igual ao total da procura real
soma_estimado = df['Procura_estimado'].sum()
df['Procura_estimado'] = (df['Procura_estimado'] / soma_estimado) * total_procura_real
df['Procura_estimado'] = df['Procura_estimado'].round().astype(int)

# Exibir a tabela comparativa
print("Comparação entre Procura real e Procura estimado pelo modelo simples:\n")
print(df[['Inicio', 'Fim', 'Procura_estimado']])
```
 

---

  
## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
