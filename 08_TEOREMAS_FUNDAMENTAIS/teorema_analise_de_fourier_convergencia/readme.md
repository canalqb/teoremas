# 🎵 - Fourier e Convergência na Aproximação de Ondas Quadradas

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  

## Frase do conceito

> Uma função complexa pode ser aproximada pela soma de ondas simples (senos), e quanto mais termos somamos, mais a aproximação fica parecida com a função original.

## Sumário

* [1. Introdução ao Conceito](#1-introdução-ao-conceito)

  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `fourier_animation.py`](#2-script-fourier_animationpy)

  * [2.1 Relação com o Conceito](#21-relação-com-o-conceito)  
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

## 1 Introdução ao Conceito

### 1.1 Resumo

Este conceito explica que qualquer forma de onda periódica, por mais complexa que seja, pode ser aproximada pela soma de ondas senoidais simples. Quanto mais termos adicionamos na soma, mais a forma se aproxima da função original — isso ajuda a entender sinais elétricos, sons, e outras ondas.

### 1.2 Exemplos Práticos

- Construção de ondas quadradas em eletrônica usando sinais senoidais.  
- Análise de sinais de áudio para comprimir ou modificar sons.  
- Processamento de imagens e dados em engenharia.

### 1.3 Explicação Detalhada

Imagine uma onda quadrada — um tipo de sinal que varia abruptamente entre dois valores. Para representá-la usando apenas ondas senoidais (ondas suaves, em forma de “S”), somamos várias delas, cada uma com frequências ímpares e amplitudes decrescentes.  
Com poucos termos, a aproximação é grosseira; adicionando mais termos, a forma fica mais parecida. Isso mostra que sinais complicados podem ser construídos a partir de sinais simples.

### 1.4 Aplicações

- Engenharia elétrica para modelar circuitos.  
- Análise de sinais em telecomunicações.  
- Síntese sonora em música digital.

### 1.5 Análise da Tabela

(Neste projeto não há tabela, mas caso houvesse, incluiríamos aqui uma comparação dos valores de aproximação para diferentes números de termos somados.)

---

## 2 Script `fourier_animation.py`

### 2.1 Relação com o Conceito

Este script ilustra a aproximação da onda quadrada por meio da soma das ondas senoidais, mostrando como a forma vai convergindo conforme mais termos são somados.

### 2.2 Objetivo do Script

Visualizar, por meio de gráficos animados, os “pulsos elétricos” que percorrem a linha da série de Fourier. A ideia é mostrar a diferença entre dois tipos de aproximações: usando potências de 2 e números de Mersenne (potências de 2 menos 1).

### 2.3 Exemplo de Saída

O script gera uma animação com vários gráficos lado a lado. Cada gráfico mostra uma curva aproximada da onda quadrada e um ponto vermelho que se move como um pulso elétrico, com velocidades e direções variadas.

### 2.4 Funcionamento Interno

- Calcula as somas parciais da série usando diferentes números de termos.  
- Gera gráficos com subplots para as diferentes aproximações.  
- Anima pontos que se movem ao longo dessas curvas para representar o pulso.  
- Salva o resultado final como um arquivo GIF para fácil visualização.

### 2.5 Tecnologias e Requisitos

- Python 3.8.10  
- Bibliotecas: `numpy`, `matplotlib`, `pillow` (para salvar GIF)  
- Ambiente com suporte a GUI para visualização da animação.

---

## 3 Extras

### 3.1 Licença

Projeto sob licença MIT — uso livre e aberto para modificações.

### 3.2 Referências

- Explicações simples sobre séries de Fourier podem ser encontradas em vídeos educacionais e artigos introdutórios na internet.  
- Documentação oficial do Matplotlib para animações.  

### 3.3 Testes e Validações

- O código foi testado em Python 3.8.10 com Matplotlib versão compatível.  
- GIF gerado pode ser aberto em qualquer visualizador padrão.

---

## 4 Contato

* Feito por CanalQb no GitHub  
* Visite o blog: canalqb.blogspot.com [https://canalqb.blogspot.com]  
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*

---

## 5 Nota

**Onda quadrada**: é um tipo de sinal que alterna abruptamente entre dois níveis, como um interruptor ligado/desligado.  
**Número de Mersenne**: é um número na forma 2^n - 1, onde n é um número inteiro positivo.  
**Senoide**: é uma onda suave, que tem o formato de “S” repetida, muito comum em fenômenos naturais.  
**Série de Fourier**: uma soma de várias ondas senoidais que, juntas, podem formar sinais complexos.  
**Frequência**: indica quantas vezes uma onda se repete por segundo.  
**Amplitude**: altura da onda, que indica a força ou intensidade do sinal.
