# 📊 - Teorema de Cramér–Rao  
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![LGN](https://img.shields.io/badge/Teorema-Cramer--Rao-ff69b4.svg)](https://en.wikipedia.org/wiki/Cram%C3%A9r%E2%80%93Rao_bound)

## Frase do Teorema

> *"Nenhum estimador imparcial pode ter variância menor que o limite de Cramér–Rao."* – Em outras palavras: existe um limite natural para a **precisão teórica** de qualquer estimativa.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)
  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `Teorema_de_Cramer_Rao.py`](#2-script-teorema_de_cramer_raopy)
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

O **Teorema de Cramér–Rao** estabelece um limite inferior para a variância de qualquer **estimador imparcial** (ou seja, que não "puxe" os resultados para cima ou para baixo). Esse limite ajuda a avaliar **o quão bom** um estimador pode ser, em termos de **precisão**.

### 1.2 Exemplos Práticos

Se você tenta estimar a **média de uma população** com base em uma amostra, o teorema diz:  
> Existe uma variância mínima teórica que nenhum estimador imparcial pode ultrapassar.

### 1.3 Explicação Detalhada

Imagine que você está tentando adivinhar a altura média de todas as pessoas de um país. Você tira uma amostra, calcula a média e espera que seja próxima da real. O Teorema de Cramér–Rao te diz: *mesmo o melhor estimador possível (sem viés) ainda terá uma incerteza mínima* — e isso depende da **quantidade de informação disponível nos dados** (chamada de Informação de Fisher).

### 1.4 Aplicações

- Estatística inferencial
- Otimização de estimadores em aprendizado de máquina
- Análise de desempenho de sensores e medidores
- Engenharia de comunicações

### 1.5 Análise da Tabela

Exemplo de dados usados no projeto:

| x     | y      | z      |
|-------|--------|--------|
| 1     | 1      | 1      |
| 2     | 3      | 3      |
| 4     | 7      | 7      |
| 32768 | 51510  | 65535  |

- `x`: número de símbolos ou tamanho de entrada
- `y`: valor observado (estimado)
- `z`: valor de referência (limite máximo teórico)

---

## 2. Script `Teorema_de_Cramer_Rao.py`

### 2.1 Relação com o Teorema

O script utiliza um **modelo polinomial** para prever valores de `y` com base em `x` e simula o **limite teórico da precisão** da estimativa segundo o Teorema de Cramér–Rao.

### 2.2 Objetivo do Script

- Modelar os dados de forma ajustada
- Estimar a **variância mínima possível**
- Prever o valor de `y` para `x = 65536`
- Mostrar os resultados em um **gráfico interativo**

### 2.3 Exemplo de Saída

| x      | y observado | y ajustado | z      |
|--------|-------------|------------|--------|
| 1      | 1           | 1          | 1      |
| 2      | 3           | 3          | 3      |
| 4      | 7           | 7          | 7      |
| ...    | ...         | ...        | ...    |
| 32768  | 51510       | 51560      | 65535  |
| 65536  | *?*         | **95750**  | 95823  |

**Intervalo de confiança estimado:** Aproximadamente de **94000** a **97500**.

### 2.4 Funcionamento Interno

1. 📥 **Entrada**: Dados de entrada `x`, `y`, `z`
2. 📊 **Ajuste do modelo**: Regressão polinomial de grau 3
3. 🧠 **Simulação da variância mínima**: baseada nos resíduos do modelo
4. 📈 **Gráfico interativo**: Mostra os pontos, curva ajustada e previsões

### 2.5 Tecnologias e Requisitos

Requisitos:

```bash
pip install numpy plotly
````

Execução:

```bash
python Teorema_de_Cramer_Rao.py
```

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a licença MIT.
Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

### 3.2 Referências

* [Wikipedia – Cramér–Rao Bound](https://en.wikipedia.org/wiki/Cram%C3%A9r%E2%80%93Rao_bound)
* Informações sobre variância e estimadores
* Aplicações práticas em engenharia de estimação

### 3.3 Testes e Validações

* Script testado com Python **3.8.10**
* Validação visual do ajuste do modelo
* Comparação da previsão com valor real

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

* **Estimador**: fórmula ou processo usado para adivinhar um valor desconhecido.

* **Não tendencioso (ou imparcial)**: significa que, em média, a estimativa está correta.

* **Variância**: medida de quanto os resultados da estimativa variam.

* **Informação de Fisher**: um valor que mostra o quanto os dados "informam" sobre o que estamos estimando. Quanto maior, menor a incerteza.

* **Intervalo de confiança**: faixa de valores onde esperamos que a verdadeira resposta esteja.

* **Polinômio de grau 3**: fórmula com termos do tipo x, x², x³.

* **Resíduo**: diferença entre o valor observado e o valor previsto por um modelo.
 
