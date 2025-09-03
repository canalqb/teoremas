# 📚 - Teorema de Kuratowski  
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![Kuratowski](https://img.shields.io/badge/Teorema-Kuratowski-ff69b4.svg)](https://en.wikipedia.org/wiki/Kuratowski%27s_theorem)

## Frase do Teorema

> "A partir de qualquer conjunto, aplicando as operações de fechamento e complemento várias vezes, no máximo 14 conjuntos diferentes podem ser obtidos." – *Isso quer dizer que, mesmo fazendo muitas combinações dessas operações, o número de conjuntos que conseguimos criar tem um limite fixo.*

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `KuratowskiApprox.py`](#2-script-kuratowskiapproxpy)  
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

O **Teorema de Kuratowski** é um resultado importante na matemática que fala sobre como podemos formar novos conjuntos a partir de um conjunto inicial usando duas operações:  
- **Fechamento:** basicamente, "fechar" um conjunto incluindo pontos próximos que fazem parte dele de acordo com uma regra.  
- **Complemento:** pegar tudo que não está no conjunto.

O teorema diz que, mesmo aplicando essas operações várias vezes, o número de conjuntos diferentes que você pode criar nunca passa de **14**.

### 1.2 Exemplos Práticos

Imagine um conjunto de pontos na linha do tempo ou um grupo de objetos. Aplicar o fechamento é como pegar tudo que está "perto" ou ligado ao grupo. O complemento seria pegar tudo que *não* está no grupo. O teorema garante que não importa quantas vezes você faça isso, só vai formar no máximo 14 grupos diferentes.

### 1.3 Explicação Detalhada

Quando falamos em “fechamento”, pense como completar ou preencher o conjunto para incluir pontos que fazem parte do ambiente dele. Já o complemento é simples: tudo que não pertence ao conjunto.

Essas duas operações, combinadas em várias sequências, criam conjuntos diferentes, mas o limite do teorema mostra que essas combinações têm um teto: *não mais que 14 conjuntos distintos*.

### 1.4 Aplicações

O Teorema de Kuratowski é usado em:  
- **Topologia:** estudo de espaços e formas.  
- **Lógica e computação:** entender estruturas e limites de sistemas.  
- **Análise combinatória:** contar possibilidades de grupos formados por regras.

### 1.5 Análise da Tabela

O teorema original fala do limite 14 para um conjunto específico, mas em aplicações computacionais, é útil saber que os conjuntos formados ficam entre limites naturais dados por potências de 2, que indicam o crescimento do número de subconjuntos.

---

## 2. Script `KuratowskiApprox.py`

### 2.1 Relação com o Teorema

O script não calcula o valor exato do teorema, mas usa limites matemáticos conhecidos para analisar o crescimento dos conjuntos formados.

### 2.2 Objetivo do Script

- Mostrar limites inferior e superior para o número de conjuntos, usando potências de 2.  
- Calcular uma média simples entre esses limites.  
- Aplicar uma aproximação linear para "estimar" o crescimento do número de conjuntos, ajudando a visualizar o comportamento esperado.

### 2.3 Exemplo de Saída

| N  | Início (2^N) | Fim (2^(N+1) - 1) | Média | Aprox (chute) |  
|-----|-------------|------------------|-------|---------------|  
| 0   | 1           | 1                | 1     | 1             |  
| 1   | 2           | 3                | 2     | 2             |  
| 2   | 4           | 7                | 5     | 6             |  
| 3   | 8           | 15               | 11    | 14            |  
| 4   | 16          | 31               | 23    | 32            |  
| 5   | 32          | 63               | 47    | 40            |  
| 6   | 64          | 127              | 95    | 96            |  
| 7   | 128         | 255              | 191   | 160           |  
| 8   | 256         | 511              | 383   | 320           |  
| 9   | 512         | 1023             | 767   | 576           |

### 2.4 Funcionamento Interno

O script itera valores de N de 0 a 9, calcula:  
- **Início:** 2 elevado a N (2^N), número de subconjuntos básico.  
- **Fim:** 2 elevado a (N+1), menos 1 (2^(N+1) - 1), um limite maior.  
- **Média:** média simples entre os dois.  
- **Aproximação:** uma fórmula que dá um valor entre os dois, tentando simular o crescimento real.

### 2.5 Tecnologias e Requisitos

- Python 3.8.10 ou superior  
- Biblioteca padrão Python (nenhuma externa necessária)  

---

## 3. Extras

### 3.1 Licença

Este projeto está licenciado sob a **Licença MIT**. Sinta-se livre para usar, modificar e distribuir.

### 3.2 Referências

- [Kuratowski's Theorem - Wikipedia](https://en.wikipedia.org/wiki/Kuratowski%27s_theorem)  
- Livros e materiais de teoria dos conjuntos e topologia.

### 3.3 Testes e Validações

O script foi testado para valores de N entre 0 e 9 e os resultados conferem com os limites matemáticos esperados.

---

## 4. Contato

* Feito por **CanalQb** no GitHub  
* Visite o blog: [canalqb.blogspot.com](https://canalqb.blogspot.com)  
* 💸 Apoie o projeto via Bitcoin: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`  
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)  

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

Aqui estão algumas explicações simples para termos técnicos usados no texto:

- **Lambda (λ):** uma letra grega muito usada para representar constantes ou funções em matemática e computação.  
- **Variância:** uma medida que mostra o quanto os valores de um conjunto estão espalhados, ou seja, quão diferentes eles são entre si.  
- **Esperança (valor esperado):** o valor médio que se espera obter em um processo aleatório, como a média de várias tentativas.  
- **Fechamento:** em termos simples, é completar um conjunto incluindo todos os pontos relacionados a ele que devem pertencer, segundo uma regra.  
- **Complemento:** tudo aquilo que *não* pertence ao conjunto original.
