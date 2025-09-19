# 📘 - Teorema de Luzin  
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![LGN](https://img.shields.io/badge/Teorema-Lei%20dos%20Grandes%20Números-ff69b4.svg)](https://en.wikipedia.org/wiki/Law_of_large_numbers)  

## Frase do Teorema

> Qualquer função que seja "medida bem" pode ser aproximada por uma função contínua, exceto em um conjunto muito pequeno — ou seja, quase toda função é "quase contínua" quando olhamos com cuidado.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `animacao_mola_luzin.py`](#2-script-animacao_mola_luzinpy)  
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

## 1 Introdução ao Teorema

### 1.1 Resumo

O teorema afirma que funções que parecem "bagunçadas" podem ser, em sua maior parte, aproximadas por funções suaves e contínuas, desde que ignoremos pequenas regiões. Isso ajuda a entender e manipular funções que não são perfeitamente contínuas.

### 1.2 Exemplos Práticos

- Em física, para modelar fenômenos com pequenas irregularidades.  
- Em análise de sinais, para aproximar sinais ruidosos por versões mais suaves.  
- Em computação gráfica, para suavizar imagens e superfícies irregulares.

### 1.3 Explicação Detalhada

Imagine que você tem uma função que, em alguns pontos, muda muito rápido ou é até "desconexa". O teorema diz que, se aceitarmos deixar de lado um conjunto muito pequeno de pontos, podemos encontrar uma função contínua que é quase igual a essa original na maior parte do domínio. É como "colar" a função descontinuada com uma função suave, ignorando algumas exceções.

### 1.4 Aplicações

- Simplificação de modelos matemáticos complexos.  
- Processamento de dados onde queremos ignorar ruídos pequenos.  
- Otimização e análise numérica, onde funções contínuas facilitam os cálculos.

### 1.5 Análise da Tabela

O script criado gera valores para potências de 2, aplicando uma função com descontinuidades específicas para ilustrar o conceito. Os pontos extremos (descontinuidades) são destacados para mostrar onde a função original "não se comporta bem".

---

## 2 Script `animacao_mola_luzin.py`

### 2.1 Relação com o Teorema

O script cria uma visualização animada onde pontos representam valores da função, incluindo descontinuidades, e aplicam movimentos tipo mola para dar uma sensação de estabilidade e oscilação controlada. Essa representação ilustra, de forma intuitiva, a ideia de aproximação e amortecimento da função original.

### 2.2 Objetivo do Script

Mostrar uma animação que ajuda a visualizar o comportamento da função, suas oscilações e o efeito amortecido até estabilizar, reforçando a ideia da "quase continuidade" do teorema.

### 2.3 Exemplo de Saída

Uma animação com pontos azuis que sobem e descem em amplitudes e frequências diferentes, simulando molas com energias distintas, até estabilizar na posição original. A animação também é salva em arquivo GIF.

### 2.4 Funcionamento Interno

- Calcula potências de 2 para x de 0 a 10.  
- Aplica função log2 com valores modificados em pontos específicos (8 e 128) para criar descontinuidades.  
- Calcula amplitudes máximas de oscilação (10% da distância até os limites do gráfico).  
- Cada ponto tem amplitude e frequência diferentes, para movimento variado.  
- O movimento é amortecido progressivamente até os pontos se estabilizarem.  
- A animação é salva em GIF com 20 frames por segundo.

### 2.5 Tecnologias e Requisitos

- **Python 3.8.10**  
- Bibliotecas: `numpy`, `matplotlib`, `pillow` (para salvar GIF)  
- Instalação das bibliotecas:  
  ```bash
  pip install numpy matplotlib pillow
````

---

## 3 Extras

### 3.1 Licença

MIT License — livre para uso, modificação e distribuição.

### 3.2 Referências

* [Animação com Matplotlib](https://matplotlib.org/stable/api/animation_api.html)
* [Teorema de Luzin - Wikipédia](https://pt.wikipedia.org/wiki/Teorema_de_Luzin)
* [Documentação Pillow](https://python-pillow.org/)

### 3.3 Testes e Validações

Testado em ambiente local com Python 3.8.10. GIF gerado e animação exibida corretamente.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **Função contínua**: uma função que não tem "pulos" ou "quebras", seu gráfico pode ser desenhado sem levantar o lápis do papel.
* **Descontinuidade**: ponto onde a função "pula" ou não está bem definida, tipo um corte no gráfico.
* **Amplitude**: altura máxima do movimento de oscilação, aqui usada para simular quanto cada ponto se move para cima e para baixo.
* **Frequência**: quantas oscilações acontecem por unidade de tempo; maior frequência = movimento mais rápido.
* **Amortecimento (decay)**: diminuição gradual da energia ou movimento até a estabilização, como uma mola que para de oscilar.
* **Log2(x)**: função matemática que calcula o logaritmo de base 2 de x, ou seja, responde à pergunta: "A que potência devemos elevar 2 para obter x?" 
