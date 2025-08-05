# Gerador de Ternas Pitagóricas

Este script gera ternas pitagóricas primitivas e não primitivas dentro de intervalos específicos baseados em potências de 2. Além de imprimir as ternas encontradas, ele também exporta os resultados em arquivos `.csv` e `.json`, e gera uma visualização gráfica dos pares `(a, b)`.

---

## Funcionalidades

* Geração de ternas pitagóricas **primitivas** usando o método de Euclides.
* Opção para gerar também ternas **não primitivas** (múltiplos das primitivas).
* Geração de ternas em intervalos de hipotenusas delimitados por potências de 2 (ex: entre $2^c$ e $2^{c+1} - 1$).
* Exportação dos resultados para arquivos:

  * `ternas_pitagoricas.csv` (formato tabular)
  * `ternas_pitagoricas.json` (formato estruturado)
* Visualização gráfica dos valores `a` e `b` usando Matplotlib.

---

## Requisitos

* Python 3.6 ou superior
* Biblioteca `matplotlib` (para geração do gráfico)

Instalação do Matplotlib (caso não tenha):

```bash
pip install matplotlib
```

---

## Uso

Basta executar o script:

```bash
python seu_script.py
```

O script:

1. Gera ternas para $c$ de 0 a 9, com hipotenusas entre $2^c$ e $2^{c+1} - 1$.
2. Imprime as ternas no terminal.
3. Exporta os resultados para `ternas_pitagoricas.csv` e `ternas_pitagoricas.json`.
4. Mostra um gráfico dos pares `(a, b)` das ternas encontradas.

---

## Configurações

Dentro da função `main()`, você pode configurar:

* `incluir_nao_primitivas = True`
  Para gerar ternas primitivas **e** seus múltiplos (não primitivas).

* `incluir_nao_primitivas = False`
  Para gerar somente ternas primitivas.

---

## Como funciona

O script usa o método clássico para gerar ternas pitagóricas primitivas:

$$
a = m^2 - n^2, \quad b = 2mn, \quad c = m^2 + n^2
$$

onde $m > n > 0$, $m$ e $n$ são coprimos e $m - n$ é ímpar.

Se a opção de não primitivas estiver ativada, ele gera múltiplos das ternas primitivas encontradas.

---

## Estrutura dos arquivos exportados

* **CSV:** Colunas com o intervalo da hipotenusa, e os valores $a$, $b$, $c$.
* **JSON:** Objeto com as chaves como intervalos e valores como listas de ternas representadas por dicionários `{a, b, c}`.

---

## Exemplo de saída no terminal

```
2–3 -> a = 3, b = 4, c = 5
4–7 -> a = 8, b = 6, c = 10
...
```
---

## 📬 Contato

Feito por [CanalQb no GitHub](https://github.com/canalqb)
Visite o blog: [canalqb.blogspot.com](https://canalqb.blogspot.com/)
💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`

