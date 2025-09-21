# 📚 - Teorema de Borel–Cantelli  
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![LGN](https://img.shields.io/badge/Teorema-Borel–Cantelli-ff69b4.svg)](https://pt.wikipedia.org/wiki/Teorema_de_Borel-Cantelli)

## Frase do Teorema

> Se a soma das chances de uma sequência de acontecimentos for pequena o bastante, então quase nunca veremos muitos desses acontecimentos acontecerem; mas se a soma dessas chances for grande e os acontecimentos forem independentes, então veremos muitos desses acontecimentos acontecerem no longo prazo.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `borel_cantelli_animation.py`](#2-script-borel_cantelli_animationpy)  
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

O que esse resultado nos diz é que, ao observarmos uma sequência de eventos que acontecem com certas chances, podemos prever se esses eventos vão acontecer muitas vezes ou quase nunca no futuro. Se a soma das chances for limitada, quase nunca veremos muitos eventos acontecendo. Se a soma for muito grande e os eventos não influenciarem uns aos outros, então veremos muitos desses eventos ocorrerem.

### 1.2 Exemplos Práticos

- Imagine uma máquina que pode falhar em certos momentos, e a chance de falha muda com o tempo. Esse resultado ajuda a saber se, no longo prazo, a máquina vai falhar infinitas vezes ou não.  
- Em jogos de azar, podemos usar isso para entender se um evento raro vai acontecer muitas vezes ao longo de várias jogadas.

### 1.3 Explicação Detalhada

O foco está em sequências de eventos, que são acontecimentos que podem ou não ocorrer. Quando somamos as chances de todos esses eventos, duas situações aparecem:  

- Se essa soma é pequena (ou finita), então é muito improvável que muitos desses eventos aconteçam.  
- Se essa soma é grande (ou infinita), e os eventos são independentes, então quase certamente muitos desses eventos irão acontecer.

### 1.4 Aplicações

- Análise de séries temporais para identificar se certos picos ou anomalias vão ocorrer várias vezes.  
- Sistemas de comunicação para estimar a frequência de erros ao longo do tempo.  
- Processos estocásticos em finanças, para prever a ocorrência de eventos extremos.

### 1.5 Análise da Tabela

O script usa duas sequências numéricas relacionadas ao crescimento de eventos e suas chances:  

- Potências de 2 (2^n), que crescem muito rápido.  
- Números de Mersenne (2^(n+1) - 1), que também crescem rápido e têm propriedades matemáticas especiais.  

Esses números ajudam a representar visualmente a soma das chances dos eventos.

---

## 2. Script `borel_cantelli_animation.py`

### 2.1 Relação com o Teorema

O script cria uma animação 3D que mostra eventos ocorrendo em sequência, representando visualmente as chances associadas a cada evento. Ele destaca como essas chances se acumulam, o que ajuda a entender se veremos muitos ou poucos desses eventos no longo prazo.

### 2.2 Objetivo do Script

- Gerar um gráfico 3D vertical (proporção 9:16) com pontos baseados nas potências de 2 e números de Mersenne para n de 0 a 10.  
- Animar esses pontos aparecendo um por um, conectados por linhas.  
- Mostrar a soma das chances visualmente ao longo do tempo.  
- Salvar a animação em um arquivo GIF de 20 segundos.

### 2.3 Exemplo de Saída

- Janela de animação 3D exibindo pontos vermelhos (eventos) e linhas azuis conectando-os.  
- Arquivo `borel_cantelli_animation.gif` com a animação pronta para ser compartilhada.

### 2.4 Funcionamento Interno

- Cada ponto representa um evento e sua chance relativa normalizada.  
- Os eixos mostram o índice do evento e as medidas de chance.  
- A animação mostra os pontos surgindo sequencialmente e as linhas ligando esses pontos para facilitar a visualização da soma acumulada.

### 2.5 Tecnologias e Requisitos

- Python 3.8.10  
- Bibliotecas: matplotlib, numpy  
- Sistema operacional com suporte para exibição gráfica (GUI) e gravação de GIFs.

---

## 3 Extras

### 3.1 Licença

Este projeto está sob licença MIT. Sinta-se livre para usar, modificar e distribuir.

### 3.2 Referências

- [Borel–Cantelli - Wikipédia](https://pt.wikipedia.org/wiki/Teorema_de_Borel-Cantelli)  
- [Documentação matplotlib](https://matplotlib.org/stable/index.html)  
- Livros introdutórios de probabilidade e estatística.

### 3.3 Testes e Validações

O script foi testado em Python 3.8.10 com matplotlib 3.x e numpy 1.x. A animação foi validada para visualização clara e exportação correta do GIF.

---

## 4 Contato

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**Teorema**: é uma afirmação matemática comprovada, baseada em regras e deduções lógicas.  
**Independência**: significa que o resultado de um evento não influencia o resultado de outro.  
**Probabilidade**: chance de um evento acontecer, variando de 0 (impossível) a 1 (certeza).  
**Potência de 2**: número que se obtém ao multiplicar 2 por ele mesmo várias vezes, por exemplo, 2^3 = 2×2×2 = 8.  
**Número de Mersenne**: número da forma 2^(n+1) - 1, famoso em matemática por sua relação com números primos especiais.  
**Soma infinita**: quando adicionamos uma série de números que não tem limite finito, cresce sem parar.  
**Sequência de eventos**: lista de acontecimentos que podem ocorrer um após o outro.  
**Normalização**: ajuste dos números para um intervalo padrão (como 0 a 1) para facilitar comparação e visualização.
