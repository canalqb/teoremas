# 🧮 - Propriedade da Simetria das Derivadas Parciais (Teorema de Schwarz)  
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Frase do conceito

> A ordem na qual calculamos as derivadas parciais de uma função duas vezes, uma em relação a x e outra em relação a y, não altera o resultado — ou seja, as derivadas mistas são iguais.

## Sumário

* [1. Introdução ao conceito](#1-introdução-ao-conceito)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
* [2. Script `Schwarz.py`](#2-script-schwarzpy)

  * [2.1 Relação com o conceito](#21-relação-com-o-conceito)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3. Extras](#3-extras)

  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referencias)
  * [3.3 Testes e Validações](#33-testes-e-validações)
* [4. Contato](#4-contato)
* [5. Nota](#5-nota)

---

## 1. Introdução ao conceito

### 1.1 Resumo

Quando temos uma função que depende de duas variáveis, podemos calcular sua taxa de variação primeiro em uma variável e depois na outra, e isso deve dar o mesmo resultado independentemente da ordem em que fazemos essas operações.  

### 1.2 Exemplos Práticos

Imagine que a função representa a temperatura em um ponto de uma chapa metálica, variando em x e y. A taxa com que a temperatura muda ao variar primeiro x e depois y será igual à taxa de variação se fizermos y primeiro e depois x.  

### 1.3 Explicação Detalhada

As derivadas parciais mostram como a função muda em uma direção. A propriedade da simetria diz que a ordem dessas mudanças não altera o resultado final — desde que a função seja suficientemente "suave" (ou seja, tenha derivadas contínuas).  

### 1.4 Aplicações

Essa propriedade é fundamental em física e engenharia, por exemplo, em mecânica dos fluidos e em equações diferenciais, garantindo consistência nos cálculos envolvendo taxas de variação em múltiplas direções.  

---

## 2. Script `Schwarz.py`

### 2.1 Relação com o conceito

Este script mostra, com cálculos numéricos, que as derivadas mistas (∂²f/∂x∂y e ∂²f/∂y∂x) de uma função real diferem muito pouco, confirmando a propriedade da simetria.  

### 2.2 Objetivo do Script

O script calcula a diferença entre essas derivadas para vários pontos e plota essa diferença em um gráfico 3D. Também cria uma animação visual interessante, onde linhas representando retângulos e quadrados se movimentam de fora até formarem o contorno da área analisada.  

### 2.3 Exemplo de Saída

O gráfico 3D mostra a superfície da diferença entre as derivadas, que é próxima de zero, com linhas animadas que se juntam para formar o contorno do domínio.  

### 2.4 Funcionamento Interno

- Define uma função f(x,y) para ser analisada.  
- Calcula numericamente as derivadas mistas usando pequenas variações (diferença finita).  
- Cria uma grade de pontos baseados em potências de 2 para melhor visualização.  
- Gera uma superfície 3D da diferença das derivadas.  
- Anima linhas que saem de posições aleatórias fora do gráfico, movendo-se suavemente para formar o contorno da grade.  
- Mantém a imagem final por alguns segundos antes de reiniciar a animação.  

### 2.5 Tecnologias e Requisitos

- Python 3.8.10  
- Bibliotecas: `numpy` para cálculo numérico e `matplotlib` para visualização gráfica e animação.  

---

## 3. Extras

### 3.1 Licença

MIT License — livre para uso, modificação e distribuição.  

### 3.2 Referências

- Conceito da simetria das derivadas parciais, conhecido popularmente como propriedade do “Teorema de Schwarz”.  
- Documentação do matplotlib: https://matplotlib.org/  
- Documentação do numpy: https://numpy.org/  

### 3.3 Testes e Validações

Testado em Python 3.8.10 com matplotlib 3.3.0 e numpy 1.19.2. A animação funciona bem em sistemas Windows, Linux e Mac.  

---

## 4. Contato

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*  

---

## 5. Nota

{**Derivada parcial**}: é a taxa de variação de uma função em relação a uma única variável, mantendo as outras variáveis fixas.  

{**Derivada mista**}: quando calculamos a derivada parcial duas vezes, cada vez em uma variável diferente.  

{**Função suave**}: uma função que pode ser diferenciada várias vezes sem "quebrar" ou apresentar irregularidades.  

{**FPS**}: sigla para "frames por segundo", indica a quantidade de imagens exibidas por segundo em uma animação.  

{**Diferença finita**}: método numérico que aproxima derivadas calculando variações pequenas e dividindo as mudanças obtidas.  

{**Python 3.8.10**}: versão do Python utilizada para garantir compatibilidade do código.   
