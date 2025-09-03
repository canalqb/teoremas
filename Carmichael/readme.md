# Teorema de Carmichael

## 🧾 Frase do Teorema

> *"Se um número composto $n$ satisfaz $a^{n-1} \equiv 1 \mod n$ para todo inteiro $a$ coprimo a $n$, então $n$ é um número de Carmichael."* – Este teorema caracteriza um tipo especial de número composto que se comporta como primo em testes de primalidade baseados no Pequeno Teorema de Fermat.

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
* [4 Contato](#4-📬-contato)

---

## 1. Introdução ao Teorema

### 1.1 Resumo

🔍 *Números de Carmichael* são inteiros **compostos** que, **apesar de não serem primos**, **passam nos testes de primalidade baseados no Pequeno Teorema de Fermat** para qualquer base coprima a eles.

🧠 Em outras palavras, **enganam o teste de Fermat**, o que os torna perigosos para algoritmos de criptografia e testes probabilísticos de primalidade.

---

### 1.2 Exemplos Práticos

* O número `561` é o **menor número de Carmichael**, e é composto por $3 \times 11 \times 17$.
* Outros exemplos famosos: `1105`, `1729`, `2465`, `2821`.

Mesmo sendo **compostos**, para qualquer base coprima $a$, vale:

$$
a^{n-1} \equiv 1 \mod n
$$

---

### 1.3 Explicação Detalhada

📌 Segundo a **condição de Korselt**, um número $n$ é Carmichael se:

1. $n$ é **composto**.
2. $n$ é **quadrado-livre** (não possui fatores primos repetidos).
3. Para **todo divisor primo** $p$ de $n$, temos:

$$
(p - 1) \mid (n - 1)
$$

Essas propriedades garantem que $n$ se comporte como primo nos testes de Fermat.

---

### 1.4 Aplicações

🔐 **Criptografia**: Os números de Carmichael são *exceções perigosas* em algoritmos como o RSA, que dependem de testes de primalidade.

🧪 **Teste de primalidade**: Mostram os limites de testes simples como Fermat, motivando o uso de algoritmos mais robustos como Miller-Rabin.

📚 **História matemática**: Estudados desde o século XIX, especialmente após a descoberta do contraexemplo `561` em 1899.

---

### 1.5 Análise da Tabela

A lista no script inclui os **primeiros 50 números de Carmichael conhecidos**, usados como base para identificação eficiente.

Trecho:

```python
carmichaels = [
    561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, ...
]
```

---

## 2. Script `Numeros_de_Carmichael.py`

### 2.1 Relação com o Teorema

O script é uma **ferramenta prática para identificar números de Carmichael** com base no teorema. Ele usa uma lista pré-calculada e busca os números de forma eficiente, evitando verificações computacionalmente caras.

---

### 2.2 Objetivo do Script

✅ Dado um conjunto de números, o script:

* Verifica se são números de Carmichael.
* Informa o número de Carmichael anterior e posterior mais próximos.
* Permite análise exploratória de forma instantânea.

---

### 2.3 Exemplo de Saída

```
🔍 Verificando números de Carmichael com lista pré-calculada...

Valor: 1155  
 → É número de Carmichael? Sim ✅  
 → Carmichael anterior: 1105  
 → Carmichael posterior: 1729  
--------------------------------------------------
Valor: 224  
 → É número de Carmichael? Não ❌  
 → Carmichael anterior: Nenhum encontrado  
 → Carmichael posterior: 561  
--------------------------------------------------
```

---

### 2.4 Funcionamento Interno

O script usa o módulo `bisect` para **busca binária eficiente** na lista ordenada de números de Carmichael.

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

---

### 2.5 Tecnologias e Requisitos

* 🐍 **Python 3.6+**
* 📦 Biblioteca padrão `bisect` (sem dependências externas)

---

## 3 Extras

### 3.1 Licença

📜 Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

### 3.2 Referências

* Korselt, A. (1899). *Première note sur les nombres pseudoprimes*.
* Riesel, H. (1994). *Prime Numbers and Computer Methods for Factorization*.
* OEIS: [A002997 – Carmichael numbers](https://oeis.org/A002997)
* Wikipedia: [Carmichael number](https://en.wikipedia.org/wiki/Carmichael_number)

---

### 3.3 Testes e validações

✅ Validação feita com base na lista OEIS
⚠️ Teste direto por definição disponível em scripts auxiliares (não incluídos neste repositório)

---

## 4 📬 Contato

* Feito por **[CanalQb](https://github.com/canalqb)** no GitHub
* Visite o blog: [canalqb.blogspot.com](https://canalqb.blogspot.com)
* 💸 Apoie o projeto via **Bitcoin**: `13Ve1k5ivByaCQ5yer6GoV84wAtf3kNava`
* 📧 PIX: `qrodrigob@gmail.com` 
