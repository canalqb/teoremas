
# 🧠 Lei dos Grandes Números — Fraca e Forte

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)

Este repositório demonstra a **Lei dos Grandes Números** (tanto na forma **fraca** quanto na **forte**) por meio de simulações com Python. A ideia é mostrar, com um experimento simples, como a média amostral de variáveis aleatórias se aproxima da média populacional à medida que o tamanho da amostra aumenta.

---

## 📚 Sumário

- [📚 Sobre a Lei dos Grandes Números](#-sobre-a-lei-dos-grandes-números)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [🧪 O que o script faz](#-o-que-o-script-faz)
- [📊 Exemplo de saída](#-exemplo-de-saída)
- [▶️ Como executar](#️-como-executar)
- [📌 Observações](#-observações)
- [📖 Referências](#-referências) 

---

## 📚 Sobre a Lei dos Grandes Números

A **Lei dos Grandes Números (LGN)** é um princípio fundamental da estatística que afirma:

- **Forma Fraca:** A média amostral converge *em probabilidade* para a média verdadeira (esperança matemática) da população.
- **Forma Forte:** A média amostral converge *quase certamente* (com probabilidade 1) para a média verdadeira.

> À medida que o número de observações aumenta, a média amostral se aproxima da média teórica.

---

## 📁 Estrutura do Projeto

```

teoremas/
├── lei\_dos\_grandes\_numeros.py   # Script principal do experimento
└── README.md                    # Este arquivo

````

---

## 🧪 O que o script faz

O script `lei_dos_grandes_numeros.py`:

1. Gera 256 amostras independentes de uma distribuição **Bernoulli(0.5)**.
2. Divide essas amostras em blocos com tamanhos crescentes.
3. Calcula a **média amostral** de cada bloco.
4. Exibe os resultados em uma tabela.
5. Gera um gráfico que mostra como as médias se aproximam da média real (0.5), conforme o número de amostras cresce.

---

## 📊 Exemplo de saída

```plaintext
Dados da Amostra por Intervalo:

   Inicio  Fim  Tamanho  Media Amostral
0       1    2        1        1.000000
1       2    4        2        1.000000
2       4    8        4        0.250000
3       8   16        8        0.500000
4      16   32       16        0.375000
5      32   64       32        0.468750
6      64  128       64        0.515625
7     128  256      128        0.515625
````

Com o gráfico, você verá a **convergência da média amostral para 0.5** com clareza.

---

## ▶️ Como executar

1. Clone o repositório:

```bash
git clone https://github.com/canalqb/teoremas.git
cd teoremas
```

2. Instale as dependências:

```bash
pip install numpy matplotlib pandas
```

3. Execute o script:

```bash
python lei_dos_grandes_numeros.py
```

---

## 📌 Observações

* A distribuição utilizada neste experimento é a **Bernoulli(p = 0.5)**.
* O comportamento observado reflete a **Lei dos Grandes Números**: conforme o número de amostras aumenta, a média amostral se aproxima da média esperada.
* Você pode adaptar o código para usar outras distribuições (Normal, Exponencial, etc.).

---

## 📖 Referências

* 📘 [Wikipedia: Law of Large Numbers](https://en.wikipedia.org/wiki/Law_of_large_numbers)
* 📘 *A First Course in Probability* – Sheldon Ross
* 📘 [Khan Academy: LGN](https://pt.khanacademy.org/math/statistics-probability/probability-library)

--- 

📝 Licenciado sob a [MIT License](LICENSE)

```

---

### ✅ Próximos passos

- Substitua os links e o nome do autor com suas informações reais.
- Se desejar, inclua uma imagem do gráfico gerado no final do README (`![Gráfico](./img/saida.png)`).
- Adicione um `LICENSE` ao projeto (MIT, GPL etc.).

Se quiser, posso gerar automaticamente o gráfico, salvar como imagem, e ajudar a montar esse repositório GitHub completo. Deseja isso?
```

---
  
## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
