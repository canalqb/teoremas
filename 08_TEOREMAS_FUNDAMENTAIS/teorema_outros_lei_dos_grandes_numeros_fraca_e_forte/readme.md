# 🧩 - Lei Dos Grandes Numeros Fraca E Forte

[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)

## Frase do Teorema

> Se você repetir um experimento muitas vezes e calcular a média dos resultados, essa média vai se aproximar do valor real esperado – com grande confiança, ou até certeza total, dependendo da versão do teorema.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `lei_dos_grandes_numeros.py`](#2-script-lei_dos_grandes_numerospy)
  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3 Extras](#3-extras)
  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referencias)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4 Contato](#4-contato)
* [5. Nota](#5-nota)

---

## 1. Introdução ao Teorema

### 1.1 Resumo

A **Lei dos Grandes Números** garante que, quanto mais vezes você repetir um experimento aleatório (como lançar uma moeda), mais a média dos resultados vai se aproximar da média real esperada. Isso funciona tanto em um sentido mais "provável" quanto em um sentido mais "garantido", dependendo da versão do teorema.

### 1.2 Exemplos Práticos

- Jogar uma moeda milhares de vezes e contar quantas vezes sai cara.
- Medir a temperatura diária de uma cidade ao longo de muitos anos.
- Observar o tempo de resposta de um servidor em milhares de requisições.

### 1.3 Explicação Detalhada

O teorema tem duas formas:

- **Fraca:** a média amostral *provavelmente* se aproxima da média real.
- **Forte:** a média amostral *certamente* se aproxima da média real (com probabilidade total).

Em outras palavras, se você continuar coletando dados, será praticamente impossível que a média não se aproxime do valor correto.

### 1.4 Aplicações

- Estatísticas de amostragem
- Machine Learning (validação de modelos)
- Pesquisa de opinião e eleições
- Testes de qualidade em produção industrial

### 1.5 Análise da Tabela

A simulação gera uma tabela onde cada linha mostra:

- O intervalo da amostra analisada
- O tamanho do bloco
- A média observada naquele intervalo

Com isso, podemos ver a **convergência da média amostral para 0.5** (esperado para uma moeda justa) conforme o número de amostras aumenta.

---

## 2. Script `lei_dos_grandes_numeros.py`

### 2.1 Relação com o Teorema

Este script demonstra a Lei dos Grandes Números por meio de uma sequência de experimentos com distribuição Bernoulli (0 ou 1 com 50% de chance).

### 2.2 Objetivo do Script

Mostrar como a média amostral de variáveis aleatórias se aproxima da média teórica (0.5) à medida que a amostra cresce.

### 2.3 Exemplo de Saída

Dados da Amostra por Intervalo:
```plaintext
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

A saída também inclui um gráfico mostrando visualmente como a média amostral se aproxima de 0.5.

### 2.4 Funcionamento Interno

O script:

1. Gera 256 números aleatórios da distribuição Bernoulli(p = 0.5).
2. Divide os dados em blocos crescentes: 2, 4, 8, 16, etc.
3. Calcula e armazena a média de cada bloco.
4. Exibe uma tabela e um gráfico final com os resultados.

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10**
* Bibliotecas necessárias:

```bash
pip install numpy matplotlib pandas
```

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a [MIT License](LICENSE) — você pode usá-lo, modificá-lo e distribuí-lo livremente com os devidos créditos.

### 3.2 Referências

* 📘 [Wikipedia - Lei dos Grandes Números](https://en.wikipedia.org/wiki/Law_of_large_numbers)
* 📗 *A First Course in Probability* – Sheldon Ross
* 🎓 [Khan Academy - LGN](https://pt.khanacademy.org/math/statistics-probability/probability-library)

### 3.3 Testes e Validações

* Testado com diferentes sementes e distribuições (Bernoulli, Normal).
* Gráfico sempre converge para a média esperada quando N é grande.
* Código validado com múltiplas execuções.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

### Explicações de Termos Técnicos

* **Variável aleatória**: valor que muda de forma imprevisível, como o resultado de um dado ou moeda.
* **Bernoulli(p)**: experimento com dois resultados possíveis (como cara ou coroa), onde "p" é a chance de dar 1.
* **Esperança** (ou valor esperado): a média teórica dos resultados ao repetir o experimento muitas vezes.
* **Variância**: medida de quão espalhados os valores estão em relação à média.
* **Convergência em probabilidade**: significa que a chance da média se afastar do valor real fica cada vez menor.
* **Convergência quase certa**: significa que, com probabilidade 1, a média realmente vai se aproximar do valor real.

--- 
