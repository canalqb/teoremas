# 🧮 - Teorema Gauss–Bonnet

[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Teorema](https://img.shields.io/badge/Teorema-Gauss--Bonnet-ff69b4.svg)](https://en.wikipedia.org/wiki/Gauss–Bonnet_theorem)

## Frase do Teorema

> **A soma da curvatura total de uma superfície, somada à curvatura ao longo da sua borda, é proporcional à sua forma topológica.** – Ou seja, mesmo que a superfície seja dobrada ou distorcida (sem rasgar), essa soma continua a mesma dependendo apenas da "estrutura da superfície".

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)

* [2. Script `gauss_bonnet_powers.py`](#2-script-gauss_bonnet_powerspy)

  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)

* [3. Extras](#3-extras)

  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referências)
  * [3.3 Testes e Validações](#33-testes-e-validações)

* [4. Contato](#4-contato)

* [5. Nota](#5-nota)

---

## 1. Introdução ao Teorema

### 1.1 Resumo

O **Teorema de Gauss–Bonnet** relaciona a geometria de uma superfície com sua topologia. Em termos simples: **mesmo que você deforme uma superfície sem cortá-la, algumas quantidades matemáticas continuam constantes**. É uma ponte entre forma e estrutura.

### 1.2 Exemplos Práticos

* Dobrar um papel em forma de cilindro ou cone não muda a característica da superfície.
* Em jogos, animações e computação gráfica, o teorema garante que superfícies deformadas mantenham consistência estrutural.
* Em redes ou malhas computacionais, pode-se estimar propriedades globais a partir da forma local dos elementos.

### 1.3 Explicação Detalhada

O teorema diz que:

```
soma da curvatura total da superfície + soma da curvatura da borda = constante * característica da superfície
```

Essa **constante** é sempre 2 vezes o número pi (aproximadamente 6,28), e a **característica** depende apenas da "forma" (por exemplo, esfera = 2, disco = 1, toróide = 0).

### 1.4 Aplicações

* Topologia de superfícies 3D
* Análise de formas em geometria computacional
* Modelagem física de materiais
* Interpretação de gráficos e malhas em jogos

### 1.5 Análise da Tabela

A tabela gerada no script cria uma aproximação baseada na ideia de que **a característica da superfície (ou estrutura simulada)** pode ser expressa entre potências de 2. O número "esperado" representa a combinação de vértices e faces calculada com base em uma analogia com o teorema.

---

## 2. Script `gauss_bonnet_powers.py`

### 2.1 Relação com o Teorema

O script utiliza uma **estrutura inspirada** no Teorema de Gauss–Bonnet, simulando superfícies através de grafos planos com subdivisões que refletem mudanças topológicas. A coluna "esperado" representa uma soma simbólica de vértices e faces (elementos topológicos).

### 2.2 Objetivo do Script

* Construir uma tabela com 3 colunas principais:

  * Início (2 elevado a N)
  * Esperado (valor gerado com base na estrutura)
  * Fim (2 elevado a N+1 menos 1)
* Fazer com que o valor esperado esteja **dentro do intervalo** definido.

### 2.3 Exemplo de Saída

```bash
N   | Inicio  | Esperado (teorema)   | Fim
--------------------------------------------------
0   | 1       | 1                    | 1
1   | 2       | 2                    | 3
2   | 4       | 5                    | 7
3   | 8       | 9                    | 15
4   | 16      | 17                   | 31
5   | 32      | 33                   | 63
6   | 64      | 65                   | 127
7   | 128     | 129                  | 255
8   | 256     | 257                  | 511
9   | 512     | 513                  | 1023
```

### 2.4 Funcionamento Interno

* Para cada valor de N (de 0 a 9):

  * Calcula `inicio = 2^N`
  * Calcula `fim = 2^(N+1) - 1`
  * Cria um grafo ou estrutura com `V = 2^N` vértices
  * Simula um número de arestas (E) e faces (F)
  * Usa a fórmula de Euler (V - E + F = 2) para estimar F
  * Soma V + F como valor "esperado", respeitando os limites do intervalo

### 2.5 Tecnologias e Requisitos

* Python **3.8.10**
* Não é necessário instalar nenhuma biblioteca externa
* Código leve e executável via terminal ou Jupyter Notebook

---

## 3. Extras

### 3.1 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### 3.2 Referências

* Wikipedia: [Teorema de Gauss–Bonnet](https://en.wikipedia.org/wiki/Gauss–Bonnet_theorem)
* Livros de Geometria Diferencial
* Artigos sobre geometria em superfícies discretas

### 3.3 Testes e Validações

* O script foi testado em Python 3.8.10 (Windows)
* Os valores gerados respeitam os limites estabelecidos na tabela

---

## 4. Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com
  👉 [https://canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* 📧 PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**curvatura total**: soma das curvaturas locais em todos os pontos de uma superfície
**curvatura da borda**: quanto a borda de uma superfície se curva
**característica de Euler**: número que representa a forma de uma superfície (ex: esfera = 2, disco = 1)
**grafo planar**: uma rede de pontos e conexões que pode ser desenhada sem cruzamentos
**vértices**: pontos (ou nós) de uma estrutura ou grafo
**arestas**: conexões entre pontos (ou nós) em um grafo
**faces**: regiões delimitadas pelas arestas em uma malha
**estrutura topológica**: forma básica de um objeto, independentemente de como ele é esticado ou distorcido
