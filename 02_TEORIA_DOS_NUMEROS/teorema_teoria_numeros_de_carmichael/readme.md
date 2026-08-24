# 🎭 - Teorema dos Números de Carmichael

## 🧾 Frase do Teorema

> *Um número composto \$n\$ é um número de Carmichael se, para **todo** inteiro \$a\$ que seja **coprimo** a \$n\$, vale: \$a^{n-1} \equiv 1 \mod n\$* – Isso significa que **números de Carmichael se comportam como primos no teste de Fermat**, mesmo sendo compostos.

---

[![Siga o CanalQb](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRbdfT9pahbl33vIY111cMSCinslIwPR11m8cfO9wIK3D6Nhb3z6Q50CLnuPFeGutjqwgCkBvm7IOSroMK6cDOY8ntqwfDfe6sOUHNLsa8Rnq6qcOVEyJUSK-3Gt8-Cndemuta_Sk4B1c8AyWL3iWfwnYBWcKmdpxovS3LnuKFp_ngjrMna0cjvPcC2pp9/s320/CanalQb%20-%20Python%20-%20Caratheodory916.png)](https://youtu.be/xSp4gO8S-8Q)


## 📚 Sumário

* [1. Introdução ao Teorema](#1-introdução-ao-teorema)

  * [1.1 Resumo](#11-resumo)
  * [1.2 Exemplos Práticos](#12-exemplos-práticos)
  * [1.3 Explicação Detalhada](#13-explicação-detalhada)
  * [1.4 Aplicações](#14-aplicações)
  * [1.5 Análise da Tabela](#15-análise-da-tabela)
* [2. Script `Numeros_de_Carmichael.py`](#2-script-numeros_de_carmichaelpy)

  * [2.1 Relação com o Teorema](#21-relação-com-o-teorema)
  * [2.2 Objetivo do Script](#22-objetivo-do-script)
  * [2.3 Exemplo de Saída](#23-exemplo-de-saída)
  * [2.4 Funcionamento Interno](#24-funcionamento-interno)
  * [2.5 Tecnologias e Requisitos](#25-tecnologias-e-requisitos)
* [3 Extras](#3-extras)

  * [3.1 Licença](#31-licença)
  * [3.2 Referências](#32-referencias)
  * [3.3 Testes e validações](#33-testes-e-validações)
* [4 📬 Contato](#4-📬-contato)

---

## 1. Introdução ao Teorema

### 1.1 Resumo

Os **números de Carmichael** são compostos especiais que *enganam* o Pequeno Teorema de Fermat, que afirma:

> Se \$p\$ é primo e \$a\$ é coprimo a \$p\$, então:
> $a^{p-1} \equiv 1 \mod p$

Números de Carmichael são compostos \$n\$ tais que:

$a^{n-1} \equiv 1 \mod n$

para **todo** \$a\$ coprimo a \$n\$.

### 1.2 Exemplos Práticos

* O número **561** é o menor número de Carmichael:
  $3^{560} \equiv 1 \mod 561,\quad 5^{560} \equiv 1 \mod 561, \quad \text{etc.}$
  Mesmo sendo \$561 = 3 \cdot 11 \cdot 17\$, um composto!

* Outros exemplos: 1105, 1729, 2465...

### 1.3 Explicação Detalhada

A caracterização clássica de Carmichael vem de **Korselt (1899)**:

Um número composto \$n\$ é Carmichael **se e somente se**:

1. \$n\$ é **livre de quadrados** (não possui fator primo repetido),
2. Para **todo** primo \$p\$ que divide \$n\$, temos:
   $p - 1 \mid n - 1$

Isso permite verificar se um número é Carmichael **sem testar exponenciações**.

### 1.4 Aplicações

* **Testes de primalidade:** Carmichael mostra que o **teste de Fermat pode falhar**, pois números de Carmichael passam por ele.
* **Criptografia:** vulnerabilidades em sistemas que dependem de testes primitivos de primalidade.
* **Teoria dos números:** estudo da pseudo-primalidade, algoritmos probabilísticos, etc.

### 1.5 Análise da Tabela

O script trabalha com uma **tabela conhecida de números de Carmichael** extraída de fontes confiáveis (como OEIS e literatura clássica). Os números são crescentes e utilizados para buscas rápidas com `bisect`.

---

## 2. Script `Numeros_de_Carmichael.py`

### 2.1 Relação com o Teorema

O script aplica o **Teorema de Carmichael** de forma indireta: ele não verifica a condição de Korselt, mas usa uma **lista conhecida** e testada para verificar rapidamente se um número pertence ao conjunto.

### 2.2 Objetivo do Script

* Verificar se números fornecidos estão na lista de Carmichael.
* Encontrar o **número anterior e posterior mais próximo** da lista.
* Ajudar no estudo exploratório dos pseudo-primos.

### 2.3 Exemplo de Saída

```
Valor: 561
 → É número de Carmichael? Sim ✅
 → Carmichael anterior: Nenhum encontrado
 → Carmichael posterior: 1105
--------------------------------------------------
Valor: 514
 → É número de Carmichael? Não ❌
 → Carmichael anterior:  341
 → Carmichael posterior: 561
```

### 2.4 Funcionamento Interno

Funções principais:

```python
def eh_carmichael(n):
    return n in carmichaels

def busca_anterior(valor):
    pos = bisect.bisect_left(carmichaels, valor)
    return carmichaels[pos-1] if pos > 0 else None

def busca_posterior(valor):
    pos = bisect.bisect_right(carmichaels, valor)
    return carmichaels[pos] if pos < len(carmichaels) else None
```

Lista `carmichaels`: obtida de fontes confiáveis como OEIS (A002997).

### 2.5 Tecnologias e Requisitos

* **Python 3.6+**
* Módulo padrão `bisect` (não requer instalação externa)

---

## 3 Extras

### 3.1 Licença

Código open-source sob [MIT License](LICENSE).

### 3.2 Referências

* OEIS: [A002997](https://oeis.org/A002997)
* Korselt, A. (1899)
* Riesel, H. *Prime Numbers and Computer Methods for Factorization*
* Crandall & Pomerance, *Prime Numbers: A Computational Perspective*

### 3.3 Testes e validações

* Testado com dezenas de valores históricos.
* Cruzado com tabela OEIS.
* Resultados consistentes com literatura.

---

## 4 📬 Contato

* Feito por **CanalQb** no GitHub
* Visite o blog: [https://canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via **Bitcoin**: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* 💰 **PIX**: `qrodrigob@gmail.com`
