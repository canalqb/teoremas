# 🎲 - Teorema da Escolha  
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![LGN](https://img.shields.io/badge/Teorema-Escolha-ff69b4.svg)](https://en.wikipedia.org/wiki/Axiom_of_choice)

## Frase do Teorema

> *Dado um conjunto de conjuntos não vazios, é possível escolher um elemento de cada um deles.* – Em termos simples, mesmo que você tenha infinitos conjuntos com infinitos elementos, sempre é possível escolher um item de cada um.

---

## Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)  
  * [1.1 Resumo](#11-resumo)  
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)  
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)  
  * [1.4 Aplicações](#14-aplicações)  
  * [1.5 Análise da Tabela](#15-análise-da-tabela)  
* [2. Script `teorema_escolha.py`](#2-script-teorema_escolhapy)  
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
O **Teorema da Escolha** é um princípio lógico que afirma que, mesmo sem uma regra clara, podemos selecionar **um elemento de cada conjunto** em uma coleção de conjuntos não vazios.

### 1.2 Exemplos Práticos  
- Dado um grupo de gavetas com meias, o teorema diz que é possível escolher **uma meia de cada gaveta**, mesmo que existam infinitas gavetas.  
- Mesmo sem saber como escolher, a possibilidade de escolha está garantida.

### 1.3 Explicação Detalhada  
Esse teorema é muito usado em matemática avançada, mesmo que não seja sempre visível. Ele sustenta diversas construções que parecem "mágicas", porque garantem escolhas sem mostrar como fazê-las.

### 1.4 Aplicações  
- **Análise funcional**  
- **Teoria dos conjuntos**  
- **Topologia**  
- **Construções algébricas abstratas**  

### 1.5 Análise da Tabela  
No contexto deste projeto, o Teorema da Escolha **justifica a possibilidade de escolher** um valor entre dois limites (início e fim do intervalo), mesmo quando a fórmula não é explícita.

---

## 2. Script `teorema_escolha.py`

### 2.1 Relação com o Teorema  
O script usa a ideia de que é possível selecionar um valor estimado **dentro de um intervalo** definido para cada valor de `N`.  
Mesmo sem saber o valor exato, é possível definir **uma estimativa plausível** com base nos limites do intervalo.

### 2.2 Objetivo do Script  
Estimar o valor esperado dentro do intervalo `[2^N, 2^{N+1} - 1]` para valores de `N` entre 0 e 9, sem usar diretamente o valor esperado real.  
A fórmula usada é uma **média ponderada** entre início e fim.

### 2.3 Exemplo de Saída

```text
| N | Início | Fim  | Estimativa |
|---|--------|------|------------|
| 0 | 1      | 1    | 1.0        |
| 1 | 2      | 3    | 2.3        |
| 2 | 4      | 7    | 5.1        |
| 3 | 8      | 15   | 10.1       |
| 4 | 16     | 31   | 20.5       |
| 5 | 32     | 63   | 41.7       |
| 6 | 64     | 127  | 83.9       |
| 7 | 128    | 255  | 168.3      |
| 8 | 256    | 511  | 337.1      |
| 9 | 512    | 1023 | 674.7      |
````

### 2.4 Funcionamento Interno

1. Calcula o início: `inicio = 2 ** N`
2. Calcula o fim: `fim = 2 ** (N + 1) - 1`
3. Aplica média ponderada:
   `estimativa = 0.7 * inicio + 0.3 * fim`
4. Repete o processo para `N = 0` até `N = 9`

### 2.5 Tecnologias e Requisitos

* **Python 3.8.10**
* Nenhum pacote externo necessário
* Código direto e funcional
* Pode ser executado com:

```bash
python teorema_escolha.py
```

---

## 3 Extras

### 3.1 Licença

Este projeto está licenciado sob a **Licença MIT**.

### 3.2 Referências

* [Wikipedia - Axiom of Choice](https://en.wikipedia.org/wiki/Axiom_of_choice)
* Materiais de matemática discreta
* Discussões sobre médias ponderadas

### 3.3 Testes e Validações

Os valores foram comparados com dados reais para validar se a estimativa é próxima.
Você pode ajustar os pesos (0.7 e 0.3) para ver como isso afeta a precisão.

---

## 4 Contato

* Feito por CanalQb no GitHub
* Visite o blog: canalqb.blogspot.com \[[https://canalqb.blogspot.com](https://canalqb.blogspot.com)]
* 💸 Apoie o projeto via Bitcoin: 13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava
* PIX: [qrodrigob@gmail.com](mailto:qrodrigob@gmail.com)

*Readme.md corrigido por ChatGPT*

---

## 5. Nota

## 5. Nota

**Teorema da Escolha:** Garante que podemos escolher um elemento de cada conjunto, mesmo sem uma regra de escolha.

**Valor Esperado:** É uma média que representa o valor típico que se espera obter em uma situação.

**Média Ponderada:** Uma média onde alguns números têm mais "peso" que outros. Por exemplo: `0.7 * início + 0.3 * fim`.

**Início do Intervalo:** Corresponde a `2^N`.

**Fim do Intervalo:** Corresponde a `2^(N+1) - 1`.

**Estimativa:** Aproximação feita com base na posição entre início e fim.
 
