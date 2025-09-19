# 🔓 - Teorema do Mapeamento Aberto
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Teorema](https://img.shields.io/badge/Teorema-Mapeamento%20Aberto-ff69b4.svg)](https://pt.wikipedia.org/wiki/Teorema_do_mapeamento_aberto)

## Frase do Teorema

> Se uma transformação linear contínua entre dois espaços completos envia todo o espaço de partida para o de chegada (ou seja, é sobrejetora), então ela transforma conjuntos abertos em conjuntos abertos – *essa é a ideia do Teorema do Mapeamento Aberto*.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `open_mapping_viz.py`](#2-script-open_mapping_vizpy)
  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3 Extras](#3-extras)
  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referências)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4 Contato](#4-contato)
* [5. Nota](#5-nota)

---

## 1. Introdução ao Teorema

### 1.1 Resumo

O Teorema do Mapeamento Aberto é uma ferramenta poderosa em matemática. Ele diz que, se temos uma transformação linear entre dois espaços bem comportados (completos), e essa transformação cobre todo o espaço de destino, então ela **preserva a "abertura" dos conjuntos**.

### 1.2 Exemplos Práticos

Imagine que você está esticando uma malha circular usando uma função linear. Se essa função for contínua e sobrejetiva, o teorema garante que o resultado ainda terá "buracos" – ou seja, continuará sendo um conjunto aberto.

### 1.3 Explicação Detalhada

Esse teorema é útil para garantir que soluções de equações funcionais e sistemas lineares em espaços infinitos continuam tendo boas propriedades – como continuidade, existência e vizinhanças abertas.

### 1.4 Aplicações

- Equações diferenciais funcionais
- Sistemas lineares em espaços de funções
- Análise funcional
- Inteligência artificial (representações vetoriais)

### 1.5 Análise da Tabela

O script cria dois conjuntos de pontos: um baseado em potências de 2, outro nos chamados números de Mersenne (2^k - 1). Ambos são distribuídos no círculo e rotacionados por ângulos diferentes. Em seguida, são transformados por uma matriz linear **T** e visualizados antes e depois da transformação.

---

## 2. Script `open_mapping_viz.py`

### 2.1 Relação com o Teorema

A matriz **T** no script é uma transformação linear contínua e sobrejetiva (ou seja, cobre todo o plano). Ao aplicar **T** sobre conjuntos rotacionados do círculo, o script mostra que a imagem ainda "parece aberta", apoiando visualmente o Teorema do Mapeamento Aberto.

### 2.2 Objetivo do Script

Explorar visualmente como conjuntos abertos (como um círculo rotacionado) se transformam sob ações de operadores lineares contínuos.

### 2.3 Exemplo de Saída

- 📘 Domínio rotacionado com potências de 2: círculos cada vez mais densos
- 🔴 Imagem sob a matriz T: elipses ou figuras distorcidas, mas ainda abertas
- 🟢 Comparação com números de Mersenne mostra efeitos diferentes

### 2.4 Funcionamento Interno

1. Gera pontos em um círculo de raio 1.
2. Roda esses pontos por um ângulo crescente.
3. Aplica a matriz T.
4. Plota os pontos antes e depois da transformação.
5. Repete o processo para diferentes quantidades de pontos.

### 2.5 Tecnologias e Requisitos

- Python 3.8.10
- `numpy`
- `matplotlib`

Instalação com:

```bash
pip install numpy matplotlib
````

---

## 3 Extras

### 3.1 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais informações.

### 3.2 Referências

* Wikipedia – Teorema do Mapeamento Aberto
* Apostilas de Análise Funcional
* Livros de Álgebra Linear Avançada

### 3.3 Testes e Validações

Não são necessários testes automatizados neste projeto, pois o foco é visual. O script pode ser executado diretamente para gerar os gráficos.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com
  👉 [https://canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**linear**: algo que preserva soma e multiplicação por número

**transformação sobrejetiva**: quando todo ponto de destino pode ser alcançado a partir de algum ponto de origem

**contínua**: pequenas mudanças na entrada causam pequenas mudanças na saída

**aberto**: conjunto onde você pode andar um pouquinho em qualquer direção sem sair do conjunto

**Mersenne**: números na forma 2^k - 1

**potência de 2**: números como 2, 4, 8, 16, etc.

**raio**: distância do centro ao ponto da borda do círculo

**rotação**: girar um conjunto de pontos ao redor do centro

**espaço completo**: lugar onde sequências convergentes realmente "chegam" em algum ponto do espaço

**matriz**: tabela de números usada para transformar vetores

**imagem sob T**: resultado de aplicar a transformação T em um ponto ou conjunto
