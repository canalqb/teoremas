# 🧩 - De Brianchon
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Brianchon](https://img.shields.io/badge/Teorema-Brianchon-ff69b4.svg)](https://en.wikipedia.org/wiki/Brianchon's_theorem)

## Frase do Teorema

> *Seis retas tangentes a uma cônica formam um hexágono. Se esse hexágono for fechado e os lados forem pares opostos, então as três diagonais que conectam vértices opostos se cruzam em um único ponto.* – Esse resultado mostra como, mesmo em formas curvas, certos alinhamentos criam simetrias perfeitas e pontos fixos de interseção.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `brianchon.py`](#2-script-brianchonpy)  
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
O **Teorema de Brianchon** mostra como seis retas que tocam uma forma oval (chamada cônica) formam um padrão especial. Se essas seis retas fizerem um hexágono, então três linhas desenhadas dentro dele sempre se encontram em um único ponto.

### 1.2 Exemplos Práticos
- Engenharia de estruturas
- Simulações com polígonos em geometria computacional
- Modelagem de sistemas ópticos

### 1.3 Explicação Detalhada
Imagine um oval e desenhe seis retas que tocam apenas um ponto dessa forma. Se você ligar essas retas de maneira ordenada, criando um hexágono, então as linhas que ligam vértices opostos vão se cruzar em um mesmo lugar — sempre.

### 1.4 Aplicações
Esse tipo de relação geométrica aparece em áreas como:
- Arquitetura
- Design gráfico
- Computação gráfica
- Inteligência artificial com geometria simbólica

### 1.5 Análise da Tabela

**Saída esperada:**
```

Ponto de interseção: (0.0000, 0.0000)

Coordenadas dos pontos do hexágono:
A: (6.0000, 0.0000)
B: (3.0000, 3.4641)
C: (-3.0000, 3.4641)
D: (-6.0000, 0.0000)
E: (-3.0000, -3.4641)
F: (3.0000, -3.4641)

```

---

## 2. Script `brianchon.py`

### 2.1 Relação com o Teorema
Este script demonstra visualmente o **Teorema de Brianchon**, permitindo que o usuário interaja com os pontos e observe em tempo real a formação do ponto de interseção das diagonais.

### 2.2 Objetivo do Script
- Mostrar como os vértices de um hexágono tangente a uma elipse se relacionam.
- Permitir mover os pontos do hexágono e observar o ponto de interseção mudar dinamicamente.

### 2.3 Exemplo de Saída
Após rodar o script, você verá um gráfico interativo e no terminal algo como:

```

Ponto de interseção: (0.0000, 0.0000)

Coordenadas dos pontos do hexágono:
A: (6.0000, 0.0000)
B: (3.0000, 3.4641)
C: (-3.0000, 3.4641)
...

````

### 2.4 Funcionamento Interno
- Usa `matplotlib` para criar a visualização.
- Usa eventos do mouse para permitir mover os pontos.
- Recalcula a interseção das diagonais automaticamente.
- Mostra os dados no gráfico e também imprime no console.

### 2.5 Tecnologias e Requisitos
- **Python 3.8.10**
- Bibliotecas:
  - `numpy`
  - `matplotlib`

Instale com:

```bash
pip install numpy matplotlib
````

---

## 3. Extras

### 3.1 Licença

Este projeto está licenciado sob a **MIT License**.

### 3.2 Referências

* Wikipedia: [Teorema de Brianchon](https://en.wikipedia.org/wiki/Brianchon's_theorem)
* Projeto visual baseado em [CanalQB](https://canalqb.blogspot.com)

### 3.3 Testes e Validações

✅ Testado com Python 3.8.10
✅ Testado no Windows 10
✅ Compatível com Linux e MacOS (interface gráfica necessária)

---

## 4 Contato

* Feito por **CanalQb** no GitHub
* Blog: [https://canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* 📧 PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

**cônica:**
uma forma curva fechada, como uma elipse, parábola ou hipérbole.

**diagonal:**
uma linha que liga dois pontos não consecutivos de um polígono.

**interseção:**
o ponto onde duas ou mais linhas se cruzam.

**tangente:**
uma reta que toca uma curva em apenas um ponto sem cortá-la.

**elipse:**
uma forma oval fechada, parecida com um círculo achatado.

**simetria:**
um tipo de equilíbrio visual onde partes se repetem ou se refletem.
