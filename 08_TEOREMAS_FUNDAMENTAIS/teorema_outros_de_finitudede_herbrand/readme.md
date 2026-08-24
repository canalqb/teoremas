# 🧩 - De Finitudede Herbrand
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Herbrand](https://img.shields.io/badge/Teorema-Finitude%20de%20Herbrand-ff69b4.svg)](https://en.wikipedia.org/wiki/Herbrand's_theorem)

## Frase do Teorema

> *"Mesmo que o universo lógico seja infinito, é possível provar certas verdades analisando apenas um número **finito** de casos."* – Ou seja, **basta olhar até certo ponto para garantir que uma fórmula seja verdadeira em geral**, mesmo em universos infinitos.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `herbrand_finitude_tabela.py`](#2-script-herbrand_finitude_tabelapy)
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

O **Teorema de Finitude de Herbrand** mostra que podemos encontrar provas de verdades lógicas examinando um número limitado de casos — mesmo que existam infinitas possibilidades. Isso é extremamente útil na **automação de provas matemáticas** e em **lógica computacional**.

### 1.2 Exemplos Práticos

- Em vez de analisar todas as infinitas combinações de variáveis possíveis para provar que uma fórmula é verdadeira, o teorema permite focar apenas nos primeiros níveis — o suficiente para provar a validade.
- Um sistema automático de prova pode parar cedo se detectar que **até um certo ponto** todas as instâncias satisfazem a fórmula.

### 1.3 Explicação Detalhada

Na lógica de primeira ordem, o **universo de Herbrand** contém todas as combinações possíveis de termos formados a partir de constantes e funções. Esse universo pode crescer rapidamente. O Teorema de Finitude afirma que:

```
Se uma fórmula é válida, existe um número N tal que todas as instâncias geradas até o nível N são suficientes para prová-la.

```

- O número de termos possíveis cresce **exponencialmente** com N.
- Mesmo assim, não precisamos ir ao infinito: existe um N finito que basta.

### 1.4 Aplicações

- **Lógica matemática**
- **Sistemas de prova automática**
- **Raciocínio artificial**
- **Verificação de validade de fórmulas complexas**

### 1.5 Análise da Tabela

O script calcula:

- **Início**: quantidade mínima de termos gerados até nível N (2^N).
- **Fim**: quantidade máxima possível até nível N+1, menos 1.
- **Estimado (Teorema)**: média entre os dois — uma boa aproximação para representar o crescimento e a "densidade" de termos analisados.

---

## 2. Script `herbrand_finitude_tabela.py`

### 2.1 Relação com o Teorema

O script é uma ferramenta **educacional** que mostra como cresce o número de instâncias de Herbrand com o nível `N`. Ele ajuda a visualizar o motivo pelo qual o teorema fala em **finitude**, mesmo em contextos infinitos.

### 2.2 Objetivo do Script

Gerar uma **tabela clara e intuitiva** com três valores por linha:

- O número mínimo de instâncias (`2^N`)
- O número máximo até o próximo nível (`2^(N+1) - 1`)
- Uma estimativa média entre esses dois valores

### 2.3 Exemplo de Saída

```

| N | Início (2^N) | Estimado (Teorema) | Fim (2^(N+1)-1) |
| - | ------------ | ------------------ | --------------- |
| 0 | 1            | 1                  | 1               |
| 1 | 2            | 2                  | 3               |
| 2 | 4            | 5                  | 7               |
| 3 | 8            | 11                 | 15              |
| 4 | 16           | 23                 | 31              |
| 5 | 32           | 47                 | 63              |
| 6 | 64           | 95                 | 127             |
| 7 | 128          | 191                | 255             |
| 8 | 256          | 383                | 511             |
| 9 | 512          | 767                | 1023            |

```

### 2.4 Funcionamento Interno

1. Para cada valor de N de 0 a 9:
   - Calcula o mínimo: `2^N`
   - Calcula o máximo: `2^(N+1) - 1`
   - Estima a média: `(mínimo + máximo) // 2`
2. Exibe os três valores lado a lado.

A estimativa representa uma média de termos que seriam necessários **na prática** para verificar a validade lógica.

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10**
* Nenhuma biblioteca externa

Para executar:

```bash
python herbrand_finitude_tabela.py
```

---

## 3 Extras

### 3.1 Licença

Distribuído sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para detalhes.

### 3.2 Referências

* Herbrand, J. (1930). *Recherches sur la théorie de la démonstration*.
* Enderton, H. B. (2001). *A Mathematical Introduction to Logic*.
* Stanford Encyclopedia of Philosophy – *Logic and Automated Theorem Proving*

### 3.3 Testes e Validações

O script foi testado para valores de N entre 0 e 9. Os resultados batem com os valores esperados da progressão geométrica:

```
Soma de termos até nível N: 2^(N+1) - 1
```

A estimativa média usada é `(2^N + (2^(N+1) - 1)) // 2`

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

📘 **Explicações de termos técnicos:**

* **Herbrand**: tipo de universo lógico com todos os termos possíveis gerados por constantes e funções.
* **Instâncias de Herbrand**: fórmulas obtidas ao substituir variáveis por termos do universo de Herbrand.
* **Exponencial**: crescimento que dobra a cada passo — por exemplo, 2, 4, 8, 16, etc.
* **Progressão geométrica**: sequência onde cada termo é multiplicado por um número fixo.
* **Válido universalmente**: uma fórmula verdadeira em qualquer situação possível.
* **Estimativa**: um valor aproximado calculado com base em uma média ou tendência.
