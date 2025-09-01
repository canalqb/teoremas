# 🧠 Yoneda Count Growth

Este repositório apresenta um experimento conceitual com base no **Teorema de Yoneda**, da teoria das categorias, modelando com um script Python o crescimento de uma estrutura inspirada por esse teorema.

A proposta é interpretar o crescimento cumulativo de "formas de ver" um objeto, tal como o Teorema de Yoneda sugere, utilizando uma sequência baseada em potências de 2.

---

## 🧩 O Teorema de Yoneda — Intuição e Aplicação

O **Teorema de Yoneda** é uma das ideias centrais da **teoria das categorias**. Ele afirma, de forma simplificada, que:

> **Um objeto é completamente determinado por todos os morfismos que partem de outros objetos em direção a ele.**

Ou seja, um objeto pode ser compreendido inteiramente por como ele é *visto* ou *mapeado* por outros objetos dentro da categoria.

### 💬 Em termos práticos:
Se você conhece todas as maneiras pelas quais os objetos de uma categoria se relacionam com um objeto \( A \), então isso é suficiente para caracterizar completamente \( A \).

Essa perspectiva transforma a noção de "o que um objeto é" em "como ele se comporta relacionalmente".

---

## 💻 O Script — Crescimento inspirando-se em Yoneda

O script `yoneda_count_growth.py` tenta simular o crescimento do número de "visões" ou "morfismos para um objeto" à medida que adicionamos novas camadas de estrutura.

### 🧠 Ideia central:

Para cada nível \( N \), calculamos:
- `Inicio (2^N)`: representa a quantidade inicial de objetos ou formas em um dado nível.
- `Fim (2^{N+1} - 1)`: representa o limite superior possível desse crescimento.
- `Estimado (Yoneda)`: é uma **soma cumulativa de todos os inícios anteriores**, representando o total de "formas de ver" acumuladas até esse ponto — o que remete diretamente à ideia de Yoneda: a totalidade de morfismos.

### 📐 Fórmula usada:
A estimativa se baseia na soma:
\[
\sum_{i=0}^{N} 2^i = 2^{N+1} - 1
\]

Essa expressão reflete exatamente a ideia de acúmulo relacional — ao estilo Yoneda — onde cada nova camada dobra a quantidade de "formas" e se soma às anteriores.

---

## 📊 Exemplo da Tabela Gerada

| N | Início (2^N) | Estimado (Yoneda) | Fim (2^(N+1) - 1) |
|---|--------------|-------------------|-------------------|
| 0 | 1            | 1                 | 1                 |
| 1 | 2            | 3                 | 3                 |
| 2 | 4            | 7                 | 7                 |
| 3 | 8            | 15                | 15                |
| 4 | 16           | 31                | 31                |
| 5 | 32           | 63                | 63                |
| ... | ...        | ...               | ...               |

---

## 📁 Arquivos

- `yoneda_count_growth.py`: Script principal. Gera e imprime a tabela de crescimento.
- `README.md`: Este arquivo com explicações conceituais e técnicas.

---

## ▶️ Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/yoneda-count-growth.git
   cd yoneda-count-growth


2. Execute o script com Python 3:

   ```bash
   python yoneda_count_growth.py
   ```

---

## ✨ Conclusão

Este projeto é um exercício matemático-computacional que explora a ideia do Teorema de Yoneda fora do contexto categórico puro, usando contagens binárias e crescimento exponencial para ilustrar a noção de *acúmulo de morfismos*.

Embora simplificado, este modelo abre espaço para reflexões sobre como ideias abstratas da matemática podem ser reinterpretadas computacionalmente.

---

## 📝 Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).

--- 


## 📬 Contato

* Feito por CanalQb no GitHub 
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: qrodrigob@gmail.com
