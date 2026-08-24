# 🧩 - De Pappus
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  

## Frase do Projeto

> O volume e a área de superfícies geradas pela rotação de curvas podem ser calculados usando os comprimentos das curvas, áreas das regiões e as distâncias percorridas pelos seus centroides, facilitando o estudo de sólidos de revolução.

## Sumário

* [1. Introdução ao Conceito](#1-introdução-ao-conceito)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise dos Resultados](#15-análise-dos-resultados)  
* [2. Script `Pappus.py`](#2-script-pappuspy)  
  * [2.1 Objetivo do Script](#21-objetivo-do-script)  
  * [2.2 Exemplo de Saída](#22-exemplo-de-saída)  
  * [2.3 Funcionamento Interno](#23-funcionamento-interno)  
  * [2.4 Tecnologias e Requisitos](#24-tecnologias-e-requisitos)  
* [3. Extras](#3-extras)  
  * [3.1 Licença](#31-licença)  
  * [3.2 Referências](#32-referências)  
  * [3.3 Testes e Validações](#33-testes-e-validações)  
* [4. Contato](#4-contato)  
* [5. Nota](#5-nota)  

---

## 1. Introdução ao Conceito

### 1.1 Resumo  
Este projeto utiliza métodos matemáticos para calcular o comprimento de curvas, áreas de regiões e volumes de sólidos gerados pela rotação dessas curvas e regiões ao redor de um eixo. Para isso, é usado o conceito do centroide, que é o "ponto médio" ou "equilíbrio" de uma forma geométrica.  

### 1.2 Exemplos Práticos  
O programa calcula, para diferentes intervalos, o comprimento da curva, a posição do centroide da curva, a área da superfície gerada pela rotação, o volume do sólido formado pela rotação da área e outras medidas relacionadas.  

### 1.3 Explicação Detalhada  
Para cada intervalo:  
- O **comprimento da curva** é o tamanho do caminho da curva entre dois pontos.  
- O **centroide da curva (y_c)** é o ponto médio que representa a posição média da curva em relação ao eixo y.  
- A **distância percorrida pelo centroide** é o caminho que esse ponto médio percorre durante a rotação completa da curva (geralmente 2 vezes pi vezes o valor do centroide).  
- A **área da superfície gerada** é a área total da superfície que a curva cria ao girar ao redor do eixo.  
- A **área da região** é a área dentro da curva que será girada.  
- O **centroide da área (y_bar)** representa o ponto médio da área da região.  
- A **distância percorrida pelo centroide da área** é o caminho que o centroide da área percorre ao girar.  
- O **volume do sólido gerado** é o volume tridimensional criado ao girar a área ao redor do eixo.

### 1.4 Aplicações  
Esses cálculos são muito usados em engenharia, arquitetura e física para determinar volumes e áreas de objetos que possuem formas de revolução, como tanques, peças mecânicas e até objetos naturais.

### 1.5 Análise dos Resultados  
Os resultados mostram que, conforme o intervalo aumenta, o comprimento da curva, a área da região, a superfície gerada e o volume do sólido aumentam significativamente, mostrando a relação entre o tamanho da curva e o volume do sólido de revolução.

---

## 2. Script `Pappus.py`

### 2.1 Objetivo do Script  
O script calcula várias propriedades geométricas de curvas e regiões, incluindo comprimento, centroides, áreas, e volumes de sólidos gerados pela rotação dessas curvas e regiões ao redor de um eixo.

### 2.2 Exemplo de Saída  
Veja um trecho da saída para o intervalo n=3:  
```

Comprimento da curva: 8.4419
Centroide da curva (y\_c): 2.0807
Distância percorrida pelo centroide: 13.0736
Área da superfície gerada pela rotação da curva: 110.3659
Área da região: 14.6142
Centroide da área (y\_bar): 2.3355
Distância percorrida pelo centroide da área: 14.6745
Volume do sólido gerado pela rotação da área: 214.4563

```

### 2.3 Funcionamento Interno  
O script realiza integrações numéricas para calcular o comprimento da curva, a área da região e as posições dos centroides. Depois calcula os volumes e áreas de superfície usando as distâncias percorridas pelos centroides durante a rotação, conforme o método de Pappus.

### 2.4 Tecnologias e Requisitos  
- Python 3.8.10  
- Bibliotecas padrão para cálculo numérico e operações matemáticas (como math e possivelmente numpy/scipy)  

---

## 3. Extras

### 3.1 Licença  
Este projeto está licenciado sob a Licença MIT — veja o arquivo LICENSE para detalhes.

### 3.2 Referências  
- Conceitos de centroides e cálculo de volumes por rotação (método de Pappus)  
- Documentação oficial do Python 3.8.10  

### 3.3 Testes e Validações  
O script foi testado com múltiplos intervalos crescentes para validar a consistência dos cálculos de volumes e áreas.

---

## 4. Contato

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com ([https://canalqb.blogspot.com](https://canalqb.blogspot.com))  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

- **Centroide**: ponto médio ou centro de massa de uma figura geométrica, representando o equilíbrio.  
- **Comprimento da curva**: medida do tamanho do caminho de uma curva entre dois pontos.  
- **Área da região**: espaço dentro da curva que será girado.  
- **Distância percorrida pelo centroide**: o caminho que o ponto médio da curva ou área percorre ao girar 360 graus (2*pi vezes o centroide).  
- **Volume do sólido gerado**: volume tridimensional criado pela rotação da área ao redor de um eixo.  
- **Método de Pappus**: técnica para calcular volumes e áreas de superfícies geradas pela rotação usando propriedades do centroide.
