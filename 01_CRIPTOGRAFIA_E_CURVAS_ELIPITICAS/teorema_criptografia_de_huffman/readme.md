# 📦 - Teorema de Codificação de Huffman
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Codificação%20de%20Huffman-ff69b4.svg)](https://en.wikipedia.org/wiki/Huffman_coding)

## Frase do Teorema

> **"Eficiência máxima, compressão ideal!"** – Uma forma simples de entender o teorema de Huffman: quanto mais um símbolo aparece, menor deve ser seu código binário.

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `Teorema_de_Codificacao_de_Huffman.py`](#2-script-teorema_de_codificacao_de_huffmanpy)
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

O **Teorema de Codificação de Huffman** mostra como podemos **representar dados de forma eficiente**, atribuindo **códigos binários curtos aos símbolos mais comuns** e códigos mais longos aos menos frequentes. Isso resulta em **compressão de dados sem perda** de informação.

### 1.2 Exemplos Práticos

Imagine que você quer enviar uma mensagem composta de letras. Se a letra "A" aparece 80 vezes e a letra "Z" só aparece 1 vez, o ideal seria usar menos bits para "A" e mais bits para "Z", economizando espaço no total.

### 1.3 Explicação Detalhada

O algoritmo de Huffman constrói uma **árvore binária** onde os símbolos mais frequentes ficam mais próximos da raiz e recebem **códigos menores**. Os códigos gerados não se confundem entre si, pois nenhum é prefixo do outro.

### 1.4 Aplicações

- Compressão de arquivos (ZIP, JPEG, MP3)
- Transmissão de dados (telecomunicações)
- Armazenamento de textos e imagens em formatos compactos

### 1.5 Análise da Tabela

O script usa uma tabela com os seguintes campos:

| Símbolo | Significado                                      |
| ------- | ------------------------------------------------ |
| `x`     | Número de símbolos distintos                     |
| `y`     | Número mínimo de bits necessários para codificar |
| `z`     | Tamanho da maior palavra binária possível        |

---

## 2. Script `teorema_huffman_codificacao.py`

### 2.1 Relação com o Teorema

Este script implementa o **algoritmo de Huffman**, uma técnica de compressão de dados sem perda baseada na frequência dos símbolos, diretamente relacionada com os fundamentos da teoria da informação estabelecida por Shannon.

### 2.2 Objetivo do Script

Demonstrar a compressão eficiente de dados usando codificação de comprimento variável, onde símbolos mais frequentes recebem códigos mais curtos.

### 2.3 Exemplo de Saída

```
 DEMONSTRAÇÃO - TEOREMA DE CODIFICAÇÃO DE HUFFMAN
============================================================
 Texto original: 'este e um exemplo de texto para compressao de huffman'
 Tamanho original: 52 caracteres

  COMPRESSÃO:
 Tamanho comprimido: 42 bytes
 Número de códigos: 15

 Tabela de Códigos:
   ' ' → 110
   'a' → 011
   'c' → 11100
   'd' → 11101
   'e' → 10
   'f' → 11110
   'h' → 111110
   'm' → 1111110
   'n' → 1111111
   'o' → 010
   'p' → 0010
   'r' → 0011
   's' → 000
   't' → 11110
   'x' → 0010

 ANÁLISE DE EFICIÊNCIA:
   Taxa de compressão: 35.58%
   Entropia do texto: 3.9044
   Comprimento médio do código: 4.47
   Comprimento mínimo: 2
   Comprimento máximo: 7

 DESCOMPRESSÃO:
 Texto descomprimido: 'este e um exemplo de texto para compressao de huffman'
 Verificação: True
```

### 2.4 Funcionamento Interno

1. **Análise de Frequência**: Conta ocorrências de cada caractere
2. **Construção da Árvore**: Cria árvore binária baseada em frequências
3. **Geração de Códigos**: Atribui códigos binários aos caracteres
4. **Compressão**: Substitui caracteres por códigos binários
5. **Descompressão**: Reconstrói texto usando a árvore

### 2.5 Tecnologias e Requisitos

* **Python 3.8+**
* **Bibliotecas padrão**: `heapq`, `collections`
* **Otimização de memória**: Uso de `__slots__` e estruturas eficientes
* **Sem dependências externas** - totalmente autônomo

### 2.6 Execução

```bash
cd teorema_criptografia_de_huffman
python teorema_huffman_codificacao.py
```

Requisitos:

```bash
pip install numpy pandas plotly scikit-learn
```

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### 3.2 Referências

* Huffman Coding - Wikipedia: [https://en.wikipedia.org/wiki/Huffman\_coding](https://en.wikipedia.org/wiki/Huffman_coding)
* David Huffman - [https://en.wikipedia.org/wiki/David\_A.\_Huffman](https://en.wikipedia.org/wiki/David_A._Huffman)

### 3.3 Testes e Validações

* O script foi testado com Python 3.8.10
* As bibliotecas são de uso estável
* O modelo polinomial gera saída coerente com a tabela

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **Compressão sem perdas**: Significa que você pode recuperar exatamente os dados originais após a compressão.
* **Código binário**: É uma sequência de 0s e 1s usada para representar dados.
* **Árvore binária**: Estrutura usada para decidir os códigos com base em frequência.
* **Prefixo**: Em codificação, um código não pode começar com outro. Ex: se “A” é 0 e “B” é 01, isso causaria confusão.
* **Ajuste polinomial**: Técnica estatística que ajusta uma curva (parábola) para prever comportamentos futuros.
* **x**: Número total de símbolos diferentes.
* **y**: Número de bits usados com eficiência, de acordo com a frequência dos símbolos.
* **z**: Limite superior de bits se usarmos o mesmo número de bits para todos os símbolos (ex: 8 símbolos → 3 bits cada).
